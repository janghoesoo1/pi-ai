#!/usr/bin/env python3
"""experiments/ eval 점수 집계기.

OPERATING-GUIDE §4 "eval 작성이 멈추면 복리도 멈춘다" 원칙의 자동화 보조.
experiments/*.md 의 점수표(정확성/변경 통제/테스트 품질/설명 품질/안전성, 1~5)를
파싱해 실험별·항목별 평균을 내고, 임계 미달이면 '깎기'(17/18)를 권고한다.

수용률 70% ≈ 5점 만점 3.5점. 평균 < 3.5 인 항목/실험은 스킬 개선 신호로 본다.

사용: python3 ai-coding-agent-lab/tools/eval-summary.py
"""
import os
import re
import glob

THRESHOLD = 3.5  # 70% of 5
AXES = ["정확성", "변경 통제", "테스트 품질", "설명 품질", "안전성"]

HERE = os.path.dirname(os.path.abspath(__file__))
EXP_DIR = os.path.normpath(os.path.join(HERE, "..", "experiments"))

# "| 정확성 | 5 | ... |" 또는 "| 정확성 | 5 |" 형태에서 항목·점수 추출
ROW = re.compile(r"\|\s*([가-힣A-Za-z /]+?)\s*\|\s*([1-5])\s*\|")


def parse_file(path: str):
    scores = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ROW.search(line)
            if not m:
                continue
            axis = m.group(1).strip()
            if axis in AXES:
                scores[axis] = int(m.group(2))
    return scores


def main():
    files = sorted(glob.glob(os.path.join(EXP_DIR, "*.md")))
    rows = []
    for path in files:
        scores = parse_file(path)
        if scores:
            rows.append((os.path.basename(path), scores))

    if not rows:
        print("점수가 있는 experiments 파일이 없습니다.")
        return

    print(f"# eval 집계 ({len(rows)}개 실험, 임계 {THRESHOLD}/5 = 수용률 70%)\n")
    header = ["실험"] + AXES + ["평균"]
    print("| " + " | ".join(header) + " |")
    print("|" + "|".join(["---"] * len(header)) + "|")

    axis_totals = {a: [] for a in AXES}
    flags = []
    for name, scores in rows:
        vals = [scores.get(a) for a in AXES]
        present = [v for v in vals if v is not None]
        avg = sum(present) / len(present) if present else 0
        cells = [name[:42]] + [str(v) if v is not None else "-" for v in vals] + [f"{avg:.1f}"]
        print("| " + " | ".join(cells) + " |")
        for a in AXES:
            if scores.get(a) is not None:
                axis_totals[a].append(scores[a])
        low = [a for a in AXES if scores.get(a) is not None and scores[a] < THRESHOLD]
        if low:
            flags.append((name, low))

    print("\n## 항목별 평균")
    for a in AXES:
        vs = axis_totals[a]
        if vs:
            mark = " ⚠️ 임계미달" if (sum(vs) / len(vs)) < THRESHOLD else ""
            print(f"- {a}: {sum(vs)/len(vs):.2f}{mark}")

    print("\n## 깎기 권고 (17-agent-1on1 / 18-meta-tune 트리거)")
    if flags:
        for name, low in flags:
            print(f"- {name}: {', '.join(low)} 항목 임계 미달 → 해당 스킬 1:1 회고 권장")
    else:
        print("- 임계 미달 실험 없음. 현 스킬 유지.")


if __name__ == "__main__":
    main()
