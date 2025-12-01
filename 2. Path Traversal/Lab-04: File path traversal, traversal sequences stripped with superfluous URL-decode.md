# File path traversal, traversal sequences stripped with superfluous URL-decode
**Mục tiêu:** Đọc được nội dung file `/etc/passwd`  

---
Ứng dụng chặn trực tiếp chuỗi `../`, nhưng **URL‑decode 2 lần** trước khi dùng có thể bypass filter.

## Bước 1: Bắt request
- Vào **Proxy** → **Intercept ON** -> Mở lab trong Burp Browser
- Reload trang để bắt request tải ảnh
- Ta sẽ thấy request dạng:
```
GET /image?filename=1.jpg HTTP/1.1
```
<img width="1028" height="543" alt="image" src="https://github.com/user-attachments/assets/129874eb-eb9a-455a-b8d8-eca6147fe294" />

- Gửi request vào Repeater.

## Bước 2: Thay đổi tham số filename
Ứng dụng chặn `../` nhưng không chặn **double encoded traversal**:
- `../` được encode thành `%2e%2e%2f`
- Double‑encode → `%252e%252e%252f`

Lần lượt thử:
```
..%252fetc/passwd
..%252f..%252fetc/passwd
..%252f..%252f..%252fetc/passwd
```
<img width="1027" height="569" alt="image" src="https://github.com/user-attachments/assets/e507a385-9507-4986-88fb-345bd3ee973c" />

## Bước 3: Forward request
Sau khi có payload đúng, quay lại tab Proxy và bấm **Forward** để gửi request lên server là xong lab.
