package com.example.lab.service;

import com.example.lab.entity.Order;
import com.example.lab.entity.User;
import com.example.lab.repository.OrderRepository;
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
public class OrderService {

    private final OrderRepository orderRepository;
    private final UserRepository userRepository;

    // 이것만 @Transactional이 있어 불일치
    @Transactional(readOnly = true)
    public List<Order> getOrdersByUser(Long userId) {
        return orderRepository.findByUserId(userId);
    }

    // 의도적 문제: @Transactional 없음
    public Order createOrder(Long userId, String productName, Integer amount) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("User not found: " + userId));

        Order order = new Order();
        order.setUser(user);
        order.setProductName(productName);
        order.setAmount(amount);
        order.setStatus("PENDING");
        order.setCreatedAt(LocalDateTime.now());

        log.info("Creating order for user {}: {} ({})", userId, productName, amount);
        return orderRepository.save(order);
    }

    // 의도적 문제: @Transactional 없음 - 상태 변경이 롤백 보장 없이 동작
    public Order cancelOrder(Long orderId) {
        Order order = orderRepository.findById(orderId)
                .orElseThrow(() -> new IllegalArgumentException("Order not found: " + orderId));

        if ("COMPLETED".equals(order.getStatus())) {
            throw new IllegalStateException("Cannot cancel a completed order");
        }

        order.setStatus("CANCELLED");
        log.info("Order {} cancelled", orderId);
        return orderRepository.save(order);
    }
}
