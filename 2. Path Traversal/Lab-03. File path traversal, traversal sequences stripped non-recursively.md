# File path traversal, traversal sequences stripped non-recursively

**Mục tiêu:** Đọc được nội dung file `/etc/passwd`  

---
**Điểm yếu:** Ứng dụng có lỗ hổng Path Traversal nhưng chỉ *strip traversal sequences một lần* → có thể bypass bằng nested traversal (`....//`)

## Bước 1: Truy cập lab

- Mở lab trong Burp Browser. Bật **Proxy → Intercept ON**
- Reload lại trang sản phẩm để bắt request chứa `filename=`.
<img width="1027" height="539" alt="image" src="https://github.com/user-attachments/assets/7fc4cf74-6cd3-4678-b886-a52e9d05127b" />

- Gửi request vào Repeater.

## Bước 2: Sửa tham số `filename` để bypass filter**
Vì filter chỉ strip `../` **một lần**, ta dùng dạng nested traversal. Lần lượt thử:
```
....//etc/passwd
....//....//etc/passwd
....//....//....//etc/passwd
```

Giải thích:
- `....//` khi strip một lần → trở thành `../`
- Lặp lại nhiều lần → tạo được đường dẫn thoát thư mục

<img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/53e97d6e-9ceb-42a7-befa-604b4341c60e" />

## Bước 3: Forward request**
Khi ta đã có payload đúng, quay lại tab Proxy để gửi request là xong.
