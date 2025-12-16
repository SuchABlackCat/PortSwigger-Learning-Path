# File path traversal, validation of start of path

**Mục tiêu**: Đọc nội dung file `/etc/passwd`

---


Ứng dụng truyền đường dẫn đầy đủ của file ảnh thông qua một request parameter, ví dụ:

```
/var/www/images/1.jpg
```

Ứng dụng kiểm tra rằng đường dẫn bắt đầu bằng:

```
/var/www/images/
```

Nhưng sau phần kiểm tra này, nếu đường dẫn chứa `../`, ta vẫn có thể traverse để truy cập file ngoài thư mục cho phép.

## Bước 1: Bắt request

- Bật Proxy Intercept ON
- Mở lab trong Burp Browser
- Refresh trang để chặn request tải ảnh

Bạn sẽ thấy request có parameter:
```
filename=/var/www/images/71.jpg
```
<img width="1027" height="542" alt="image" src="https://github.com/user-attachments/assets/94704e3f-9ce7-43f9-9729-857359d65e5d" />

- Chuyển request vào Repeater.
## Bước 2: Chỉnh sửa payload để bypass validation

Ứng dụng chỉ kiểm tra phần đầu của path phải là:
```
/var/www/images/
```

Vì vậy payload phải giữ nguyên prefix hợp lệ, sau đó thêm path traversal:
```
/var/www/images/../../../etc/passwd
```

Giải thích:
- `/var/www/images/` → qua được bước kiểm tra "bắt đầu bằng…"
- `../../../` → quay 3 lần lên thư mục cha
- `etc/passwd` → file mục tiêu

<img width="1028" height="523" alt="image" src="https://github.com/user-attachments/assets/f9f2e39b-5523-42de-8135-325d8dc3ef27" />

## Bước 3: Forward request trong Burp
Quay lại Proxy, gửi request đã chỉnh sửa đến server là xong.
