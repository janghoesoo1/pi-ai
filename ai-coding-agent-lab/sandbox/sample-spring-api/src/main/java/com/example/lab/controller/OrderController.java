package com.example.lab.controller;

import com.example.lab.entity.Order;
import com.example.lab.exception.ErrorResponse;
import com.example.lab.service.OrderService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor
public class OrderController {

    private final OrderService orderService;

    @GetMapping
    public List<Order> getOrdersByUser(@RequestParam Long userId) {
        return orderService.getOrdersByUser(userId);
    }

    @PostMapping
    public ResponseEntity<String> createOrder(
            @RequestParam Long userId,
            @RequestParam String productName,
            @RequestParam Integer amount) {
        // 의도적 문제: 성공 응답이 단순 String (ErrorResponse와 불일치)
        Order order = orderService.createOrder(userId, productName, amount);
        return ResponseEntity.ok("Order created: " + order.getId());
    }

    @PatchMapping("/{id}/cancel")
    public ResponseEntity<ErrorResponse> cancelOrder(@PathVariable Long id) {
        // 의도적 문제: 성공인데 ErrorResponse를 사용 (오용)
        orderService.cancelOrder(id);
        return ResponseEntity.ok(ErrorResponse.of(200, "Order cancelled successfully"));
    }
}
