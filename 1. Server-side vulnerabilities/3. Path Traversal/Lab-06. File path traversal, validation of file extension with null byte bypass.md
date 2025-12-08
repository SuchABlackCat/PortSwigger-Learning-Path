# File path traversal, validation of file extension with null byte bypass
**Mục tiêu**: Đọc nội dung file `/etc/passwd`

---

Ứng dụng yêu cầu filename phải kết thúc bằng `.png`.

Nhưng ta có thể chèn null byte (`%00`) để đánh lừa ứng dụng:
- Phía server-side (C/PHP cũ) dừng đọc đường dẫn tại null byte.
- Phía validation logic vẫn thấy file kết thúc bằng `.png`.

→ Điều này cho phép gửi một file hợp lệ như:
```
../../../etc/passwd%00.png
```

Server sẽ mở file `/etc/passwd`, bỏ qua `.png` phía sau.

## Bước 1: Bắt request
- Mở lab trong Burp Browser.
- Reload lại page để bắt request

Ta sẽ thấy request kiểu:
```
GET /image?filename=1.jpg
```
<img width="1028" height="539" alt="image" src="https://github.com/user-attachments/assets/724eab3f-0685-47e0-a3cb-8a08ee4984db" />

- Gửi lại request vào Repeater.
## Bước 2: Tạo payload bằng Null Byte (%00)
Ứng dụng chỉ kiểm tra rằng filename phải kết thúc bằng .png, nên payload phải tuân theo:
```
../../../etc/passwd%00.png
```
<img width="1029" height="525" alt="image" src="https://github.com/user-attachments/assets/4f06b09f-65e0-498a-a9d4-85ca90eeb740" />


## Bước 3: Forward request
Sau khi đã có payload đúng, quay lại Proxy, gửi request đã chỉnh sửa tới server là xong.

