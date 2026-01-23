# Offline password cracking

## Chuẩn bị
- My credentials: `wiener:peter`
- Victim's username: `carlos`

## Bước 1: 
Login với chức năng `Stay logged in`. Gửi request đó vào Repeater, ấn Send để xem response.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4bf0cb5d-e959-4e9a-8106-d8be00c75640" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/7be8a551-dc25-42fb-b6e5-cf2cc38484aa" />

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

Quay về Home, vào 1 bài viết bất kì.

Tạo 1 comment bất kì như hình:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/277d682f-06eb-43e4-a16f-5bec7b9cb2f7" />

Khi gửi comment đi và ấn Back to blog, ta sẽ thấy 1 thông báo:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b90e70e1-b85b-48c2-bd6a-0f274df315c5" />

Tức có lỗ hổng XSS ở đây.


## Bước 2


Đi đến exploit server. Lấy URL.

Quay lại blog. Gửi tiếp 1 comment chứa đoạn script (điền URL vừa copy vào `document.location`). 

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/93ae99d1-493e-4c80-b430-4ac6e34043e2" />

Quay lại exploit server. Ta sẽ thấy có 1 request chứa đoạn:

```
stay-logged-in: Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz
```

Decode bằng base64 ta có chuỗi:

```
carlos:26323c16d5f4dabff3bb136f2460a943
```
<img width="624" height="593" alt="image" src="https://github.com/user-attachments/assets/e3efa7ec-54f9-42ad-a203-0ee0d9fe2243" />

Thực hiện tìm kiếm và ta sẽ biết mật khẩu trước khi được hash bằng MD5 là `onceuponatime`

<img width="722" height="447" alt="image" src="https://github.com/user-attachments/assets/ce61a8b8-c9e1-400d-a65b-1e5d3c692322" />

Sau khi login bằng tài khoản `carlos:onceuponatime`, nhập lại password 1 lần nữa là xong lab:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b3416f3d-7425-493f-967d-2ead1bfd5f2e" />
