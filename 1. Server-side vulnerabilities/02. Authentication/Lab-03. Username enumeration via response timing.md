# Username enumeration via response timing

**Level**: Practitioner

**Mục tiêu**: Tìm username hợp lệ dựa trên thời gian phản hồi (response time), sau đó brute-force password và đăng nhập thành công.

---

Lab này không trả về thông báo lỗi khác nhau, nhưng:
- Response time khác nhau
- Khi username sai → response nhanh và gần như giống nhau
- Khi username đúng → server mất thêm thời gian để kiểm tra password → response chậm hơn

Ngoài ra:
- Lab có IP-based brute-force protection (chặn IP nếu login sai nhiều lần)
- Nhưng có thể bypass bằng header `X-Forwarded-For` để giả mạo IP


## Chuẩn bị
Tài khoản cho sẵn:
```
- Username: wiener
- Password: peter
```

2 file wordlist:
- `username.txt`: danh sách username
- `password.txt`: danh sách password

Mở lab bằng Burp Browser.

Bật `Intercept: ON` trong Burp Suite.

## Bước 1: Bắt request đăng nhập

- Truy cập trang login của lab.
- Thử login với username và password bất kỳ.
- Gửi request
- Chuột phải vào request POST /login
- Chọn `Send to Repeater` (để thử gửi request nhiều lần)

## Bước 2: Thử nghiệm trong Repeater & nhận diện cơ chế bảo vệ
- Trong Repeater, gửi request nhiều lần với login sai. Sau vài lần sai sẽ bị block IP:

<img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/b9416084-a9f5-4dcb-80fd-f16febb3343c" />

- Để đổi IP, ta sẽ thử thêm header `X-Forwarded-For` vào (đây là HTTP Header lưu IP user mỗi khi đi qua proxy, cho phép sửa IP tùy thích):

<img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/17a3c073-c94a-4e32-8da1-70cbc01d1d26" />

Server vẫn chấp nhận request => Server tin vào header `X-Forwarded-For`; đồng nghĩa ta có thể đổi giá trị header này để giả IP khác nhau, bypass brute-force protection

## Bước 3: Brute-force username (Timing attack)
- Gửi request sang Intruder (Chuột phải -> `Send to Intruder`)

- Trong Intruder, có 4 loại attack:
  - **Sniper**: 1 payload/vị trí/lần
  - **Battering Ram**: 1 payload nhiều vị trí/lần
  - **Pitchfork**: nhiều payload nhiều vị trí/lần (cùng index)
  - **Cluster Bomb**: mọi tổ hợp payload

  => Trong lab này ta sẽ chọn **Pitchfork**.

- Đảm bảo trong request có dòng sau (thêm `Add §`): `X-Forwarded-For: §1§`
- Thêm `Add §` vào chỗ `X-Forwarded-For` và `username=` như sau để tạo thành 2 nơi chèn payload:

<img width="1037" height="436" alt="image" src="https://github.com/user-attachments/assets/88db7bba-2106-4129-ac05-1df71b52b6c4" />

- Cấu hình vị trí chèn payload 1:

<img width="311" height="637" alt="image" src="https://github.com/user-attachments/assets/747a4e98-3893-4e47-b5ad-fe11f284350f" />

- Cấu hình vị trí chèn payload 2:

<img width="311" height="486" alt="image" src="https://github.com/user-attachments/assets/9b4f4395-d15b-45e5-9e8e-909da2b6ab60" />

*(Trong Payload configuration, chọn Load và chọn file `username.txt` để load các username trong file.)*

- Sau khi chạy xong thì ấn vào cột `Response received` để sort theo từ nhiều nhất xuống ít nhất:

<img width="1288" height="243" alt="image" src="https://github.com/user-attachments/assets/48e78a05-58cf-4c5e-b651-21f0fa46bf1c" />

Ta sẽ coi `username=pi`.

## Bước 4: Brute-force password

Làm tương tự username.

- Thay username mới trong request
- Đánh dấu lại payload vào `X-Forwarded-For` và `password=` như hình:

<img width="1037" height="438" alt="image" src="https://github.com/user-attachments/assets/a045960a-3e6f-46b9-9182-77d027c84302" />

- Với vị trí chèn payload tại `X-Forwarded-For`, có thể đổi 1-100 sang 101-200 để tránh bị block IP.
- Với vị trí chèn payload tại `password=`, ấn `Clear` và thay bằng `password.txt`.

- Ấn `Start Attack`.
- Nếu status code = 302 tức username và password đúng:

<img width="1290" height="242" alt="image" src="https://github.com/user-attachments/assets/bb70f10b-390c-4f26-9cd7-e5d10945f626" />

Quay lại lab login với username và password là xong lab!





