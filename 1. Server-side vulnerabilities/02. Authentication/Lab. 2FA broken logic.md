# 2FA broken logic
- Source: https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic
- Level: Practitioner

## Chuẩn bị
- Mở lab trong Burp Suite (Intercept: ON)
- Thông tin đăng nhập:
  - Tài khoản của mình: `wiener : peter`
  - Tài khoản nạn nhân: `carlos : montoya`

## Bước 1:

Vào **My Account**, log in vào tài khoản của mình. Chú ý đến yêu cầu 2FA sau khi login:

<img width="778" height="396" alt="image" src="https://github.com/user-attachments/assets/8ddff3ec-d303-4d51-a7b4-2fc3e05c6761" />

Điền bừa code và bắt request `POST /login2`:

<img width="1029" height="540" alt="image" src="https://github.com/user-attachments/assets/ee51d683-7d2b-4764-81e9-3014c3124980" />

Ta sẽ thấy có 1 parameter `verify` xác định user nào đang login

## Bước 2:

Log out và login lại để gửi request `GET /login2` dưới tên `carlos`:

<img width="1027" height="542" alt="image" src="https://github.com/user-attachments/assets/346aedf4-7821-4cd7-8e87-3be3c46e1baf" />

Lại log out và login lại để lấy request `POST /login2` nhưng đổi `verify=carlos`

<img width="1029" height="542" alt="image" src="https://github.com/user-attachments/assets/d1105b26-f832-4afb-bf52-66a5783a89b6" />

Gửi request vào Intruder. Đảm bảo `verify=carlos` và đặt chỗ gửi payload:

<img width="1037" height="436" alt="image" src="https://github.com/user-attachments/assets/3c4691d3-6880-44e0-8499-d52645a241bc" />

Chỉnh các cài đặt trong tab `Payload`:

<img width="338" height="639" alt="image" src="https://github.com/user-attachments/assets/df9e78e9-1c33-40f7-8a96-13cba8ced1c8" />


