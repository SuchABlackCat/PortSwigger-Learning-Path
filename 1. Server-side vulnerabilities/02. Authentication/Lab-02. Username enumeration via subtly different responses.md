# Username enumeration via subtly different responses

**Level**: Practitioner

**Mục tiêu**: Brute-force để tìm được username và password đúng.

---

## Chuẩn bị
2 file wordlist:
- `username.txt`: danh sách username
- `password.txt`: danh sách password

Mở lab bằng Burp Browser.

Bật `Intercept: ON` trong Burp Suite.

## Bước 1: Bắt request đăng nhập

- Truy cập trang login của lab.
- Thử login với username và password bất kỳ.

Burp sẽ chặn request → Forward để xem response.

Quan sát response trả về:

```
Invalid username or password
```

<img width="736" height="363" alt="image" src="https://github.com/user-attachments/assets/897c167d-9cfe-422b-980c-e2a334fb809c" />

## Bước 2: Gửi request vào Intruder

- Chuột phải vào request login trong Burp.

- Chọn `Send to Intruder`.

<img width="908" height="542" alt="image" src="https://github.com/user-attachments/assets/b462dfa5-8cd8-4d91-985c-ca5c1de532c7" />

<img width="1037" height="436" alt="image" src="https://github.com/user-attachments/assets/91587fd7-e5c2-4f77-b6ed-dc9f2bb7f16e" />

## Bước 3: Brute-force username

Sau đây ta sẽ brute force username theo file `username.txt` trước.

- Chọn vị trí chèn payload: 
  - Tìm tham số `username=`
  - Bôi đen giá trị username
  - Nhấn `Add §`

<img width="1039" height="488" alt="image" src="https://github.com/user-attachments/assets/2f311bc6-bab7-42fd-8d9a-6dacfe6a20af" />

- Load các username: Sang tab `Payloads`, đảm bảo các thông tin sau:
    - Payload type: `Simple list`
    - Payload Configuration: Nhấn `Load` -> Chọn file `username.txt` -> OK

<img width="339" height="486" alt="image" src="https://github.com/user-attachments/assets/26275586-f021-4da5-bc03-919524695efc" />

- Sang tab `Settings`
    - Tìm mục `Grep & Extract`
    - Nhấn `Add`
    - Chọn `Fetch response`
    - Bôi đen chuỗi: `Invalid username or password`
    - Nhấn OK

<img width="338" height="410" alt="image" src="https://github.com/user-attachments/assets/30c2f75f-ba2e-4159-97f7-c61afb31ecce" />

- Ấn `Start Attack`.

Phân tích:

- Hầu hết các response khác đều giống nhau.
- Chỉ có response này khác (không có dấu `.`)

<img width="1314" height="490" alt="image" src="https://github.com/user-attachments/assets/f9df16f5-add8-46b4-850d-1ec04e975f24" />

- Ta có thể suy ra response không có dấu `.` là username đúng: `alterwind`

## Bước 4: Brute-force password

Quay lại Intruder, làm tương tự với password để brute-force:

- Chọn vị trí payloads: 
  - Quay lại tab `Positions`
  - Xóa dấu § ở username (nếu còn)
  - Bôi đen giá trị sau `password=`
  - Nhấn `Add §`

<img width="1038" height="437" alt="image" src="https://github.com/user-attachments/assets/7152382c-8c52-400b-af19-8c40891fcc7a" />

- Load danh sách password:
  - Sang tab `Payloads`
  - Nhấn `Clear` để xóa payload cũ
  - Nhấn `Load` → chọn file `password.txt`

<img width="338" height="415" alt="image" src="https://github.com/user-attachments/assets/ae8ad2d8-3286-45a5-ad8e-d9809d22aec9" />

- Cấu hình lại `Grep & Extract`:
  - Nhấn `Clear` để xóa cấu hình cũ
  - Nhấn `Add` → `Fetch response`
  - Bôi đen `Invalid username or password`
  - Nhấn OK

<img width="339" height="408" alt="image" src="https://github.com/user-attachments/assets/e287c631-1962-4de3-9feb-ca8196c0d64b" />

- Ấn `Start Attack`.

<img width="1314" height="242" alt="image" src="https://github.com/user-attachments/assets/4ab1f93a-c3f8-4d79-99ff-5f4aa298aa7f" />

Quan sát các response, ta thấy được password là `7777777`.

Thử lại với username và password vừa tìm được là xong lab!
