INSERT INTO users (name, email, created_at) VALUES ('Alice', 'alice@example.com', '2026-01-01 10:00:00');
INSERT INTO users (name, email, created_at) VALUES ('Bob', 'bob@example.com', '2026-02-01 10:00:00');
INSERT INTO users (name, email, created_at) VALUES ('Charlie', 'charlie@example.com', '2026-03-01 10:00:00');

INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (1, 'Keyboard', 89000, 'COMPLETED', '2026-01-15 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (1, 'Mouse', 45000, 'COMPLETED', '2026-01-20 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (1, 'Monitor', 350000, 'PENDING', '2026-02-01 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (2, 'Laptop', 1500000, 'COMPLETED', '2026-02-10 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (2, 'Charger', 35000, 'CANCELLED', '2026-02-15 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (2, 'Webcam', 78000, 'PENDING', '2026-03-01 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (3, 'Headset', 120000, 'COMPLETED', '2026-03-05 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (3, 'Desk', 280000, 'PENDING', '2026-03-10 14:00:00');
INSERT INTO orders (user_id, product_name, amount, status, created_at) VALUES (3, 'Chair', 450000, 'PENDING', '2026-03-15 14:00:00');
