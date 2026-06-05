package com.example.lab.controller;

import com.example.lab.entity.User;
import com.example.lab.repository.OrderRepository;
import com.example.lab.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;
    // 의도적 문제: Controller가 Repository를 직접 의존
    private final OrderRepository orderRepository;

    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsersWithOrders();
    }

    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        User user = userService.getUserById(id);
        if (user == null) {
            // 의도적 문제: GlobalExceptionHandler의 ErrorResponse를 사용하지 않고 raw exception
            throw new RuntimeException("User not found with id: " + id);
        }
        return user;
    }

    @PostMapping
    public User createUser(@RequestParam String name, @RequestParam String email) {
        // 의도적 문제: 입력 검증 없음, DTO 미사용
        return userService.createUser(name, email);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteUser(@PathVariable Long id) {
        // 의도적 문제: 비즈니스 로직이 Controller에 존재
        // 이 로직은 Service에 있어야 함
        if (!orderRepository.findByUserId(id).isEmpty()) {
            return ResponseEntity.badRequest().body("Cannot delete user with existing orders");
        }
        userService.deleteUser(id);
        return ResponseEntity.ok("User deleted");
    }
}
