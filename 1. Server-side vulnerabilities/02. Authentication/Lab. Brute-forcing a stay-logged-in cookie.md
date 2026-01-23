# Brute-forcing a stay-logged-in cookie
- Level: Practitioner

## Chuẩn bị
- My credentials: `wiener:peter`
- Victim's username: `carlos`
- File `password.txt` chứa danh sách mật khẩu để brute-force

## Bước 1: 

Login với chức năng `Stay logged in`. Gửi request đó vào Repeater, ấn Send để xem response.

<img width="1337" height="529" alt="image" src="https://github.com/user-attachments/assets/be95abc3-eab9-409e-8c9d-5a321babdb3f" />

Khi đó, ta sẽ có 1 cookie `stay-logged-in` và dựa vào tab Inspector, chuỗi gốc là:

```
wiener:51dc30ddc473d43a6011e9ebba6ca770
```

(encode by base64)

Do plaintext là `wiener`, rất có thể đoạn mã `51dc30ddc473d43a6011e9ebba6ca770` là password `peter` nhưng được hash bằng MD5.

Ta kiểm chứng bằng cách hash MD5 chuỗi `peter`:

<img width="750" height="530" alt="image" src="https://github.com/user-attachments/assets/298d32d9-c116-4f64-b6e8-6ae05fbc1683" />

Vậy có thể khẳng định:

```
stay-logged-in cookie = username (plaintext) + password (hashed by MD5)
```

Logout ra khỏi tài khoản của mình.

## Bước 2

Login bằng username của nạn nhân `carlos`. Mật khẩu có thể điền bừa.

Quay lại lấy request `GET /my-account?id=wiener` (khi submit login) và gửi vào Intruder.

Config:
- Type of Attack: Sniper
- Payload: stay-logged-in cookie
- Xóa session

<img width="1038" height="437" alt="image" src="https://github.com/user-attachments/assets/216402ca-838b-43f5-90a8-024c6630883f" />

Trong tab Payload:
- Load file `password.txt` chứa danh sách các mật khẩu để bruteforce vào mục Payload configuration của tab Payload.
- Thêm các rule vào Payload processing:
  - `Hash: MD5`: hash password = MD5
  -  Thêm phần prefix vào payload là `carlos`
  -  Encode base64 mật khẩu trước khi hash
 
<img width="301" height="585" alt="image" src="https://github.com/user-attachments/assets/13fcf502-23ac-4ae5-ac83-a66fd7608d7c" />

Ấn Start Attack. Payload đúng là khi request status=200 như hình:

<img width="1308" height="541" alt="image" src="https://github.com/user-attachments/assets/ef097375-f9ea-4690-9ccf-4bc98ea3b3f3" />

Quay lại tab Proxy, sửa request `GET /my-account` y như request vừa bị brute force kèm cookie.

<img width="1366" height="541" alt="image" src="https://github.com/user-attachments/assets/208f9146-4801-42ff-a31d-42254ee75bca" />

Gửi request là xong lab:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d5aa3427-48ff-4232-8543-09a065aeac93" />
