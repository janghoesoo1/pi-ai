package com.example.lab.service;

import com.example.lab.entity.User;
import com.example.lab.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class UserService {

    private final UserRepository userRepository;

    // 의도적 문제: @Transactional 없음, N+1 쿼리 발생
    public List<User> getAllUsersWithOrders() {
        List<User> users = userRepository.findAll();
        // N+1 문제: Lazy 로딩된 orders를 루프에서 접근
        for (User user : users) {
            log.debug("User {} has {} orders", user.getName(), user.getOrders().size());
        }
        return users;
    }

    // 의도적 문제: @Transactional 없음
    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }

    // 의도적 문제: @Transactional 없음, 민감 정보(이메일) 로그 출력
    public User createUser(String name, String email) {
        log.info("Creating user with email: {}", email);
        User user = new User();
        user.setName(name);
        user.setEmail(email);
        user.setCreatedAt(LocalDateTime.now());
        return userRepository.save(user);
    }

    // 이것만 @Transactional이 있어 불일치
    @Transactional
    public void deleteUser(Long id) {
        log.info("Deleting user with id: {}", id);
        userRepository.deleteById(id);
    }
}
