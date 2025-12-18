# Broken brute-force protection, IP block

**Level**: Practitioner

**Mục tiêu**: Log in vào tài khoản nạn nhân

---

Trong lab này, web có 1 cơ chế phòng vệ: nếu login sai 3 lần thì sẽ bị block IP. 

Tuy nhiên, cơ chế này lại có lỗi logic nghiêm trọng: Mỗi lần login thành công → reset counter số lần login sai

VD: `login sai lần 1 → login sai lần 2 → login đúng (tài khoản của mình) → login sai lần 3 ...`

Attacker có thể tận dụng lỗi này để bruteforce mà không bị block IP.

## Bước 1: Chuẩn bị
- Tài khoản hợp lệ: `wiener:peter`
- File chứa các passwords để brute-force: chuyển list vào file `password.txt`
- Bật Burpsuite và mở lab trong browser của Burp

## Bước 2: Xác định cơ chế block IP

- Mở lab, bật Burp (Intercept ON).
- Login bằng username `carlos` và password bất kì.
- Bắt request và gửi nó vào Repeater.
- Thử login sai 3 lần liên tiếp.

=> IP bị block tạm thời

<img width="1029" height="569" alt="image" src="https://github.com/user-attachments/assets/32d844b3-d97a-434e-81ed-d8306ae9a928" />

## Bước 3: Attack Settings
### Bắt request login + gửi vào Burp Intruder
- Nhập username và password bất kỳ
- Bắt request POST /login
- Chuột phải → `Send to Intruder`
### Cấu hình Intruder
- Attack type: `Pitchfork` (chạy song song các payload ở nhiều vị trí theo 1 index)
- Payload positions: bôi đen vị trí chèn payload và chọn `Add §` như sau:
```username=§username§&password=§password§```
- Vào `Resource Pool`, đặt `Maximum concurrent requests = 1` (số lượng request gửi cùng lúc đến server)

<img width="1366" height="598" alt="image" src="https://github.com/user-attachments/assets/48d1af26-1b7e-44c9-ad9a-297287ac848a" />


### Payload position 1 – Username list
- Tạo một danh sách các list:
```
wiener
carlos
carlos
wiener
carlos
carlos
...
```
(số lần xuất hiện của `carlos` = số password định brute-force)
- Trong tab `Payloads`: `Payload position: 1` -> `Load` -> Load list username này vào.

### Payload position 2 – Password list
- Danh sách password phải đồng bộ với username list:
```
peter
<password1>
<password2>
peter
<password3>
<password4>
...
```
- Trong tab `Payloads`: `Payload position: 2` -> `Load` -> Load list password này vào.
- Nhấn `Start attack`.

## Bước 4: Phân tích kết quả
- Lọc ẩn các response có status 200
- Sắp xếp theo cột username
- Request nào có status = 302 là thành công
<img width="1290" height="240" alt="image" src="https://github.com/user-attachments/assets/bd912051-109a-4c7f-9973-371fec4e0cd1" />
- Login bằng tài khoản vừa có là xong lab!
