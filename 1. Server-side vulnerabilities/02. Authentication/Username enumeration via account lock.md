# Username enumeration via account lock

## Chuẩn bị
- Mở lab trong Burp Suite browser (Intercept: ON)

Nhập bừa username và password:
<img width="741" height="344" alt="image" src="https://github.com/user-attachments/assets/146dab3d-3d43-4e83-98f8-0406e067fd91" />

Bắt request login trong Burp Suite:
<img width="1031" height="545" alt="image" src="https://github.com/user-attachments/assets/822acbcd-6bde-43d9-9c31-bf515a57541a" />

Gửi request vào Intruder. Vào tab Intruder, chọn Type of Attack là **Cluster Bomb**:
<img width="1041" height="595" alt="image" src="https://github.com/user-attachments/assets/f35bafdc-fdd7-4ea2-bb40-4fea8a12add7" />

Trong tab Payload, chọn Payload position đầu tiên. Trong Payload configuration, ấn Load để lấy các username trong file `username.txt`:
<img width="312" height="460" alt="image" src="https://github.com/user-attachments/assets/4476aeff-c30c-4b1e-b329-7163c383a1ec" />

Chọn Payload position thứ hai. Chọn Payload type là **Null payloads**. Trong Payload configuration, điền *Generate* **5** *payloads*:
<img width="336" height="342" alt="image" src="https://github.com/user-attachments/assets/e68225d5-47ac-4ab3-a007-2dbe911a0129" />
