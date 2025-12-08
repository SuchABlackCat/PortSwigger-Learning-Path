# Username Enumeration via Different Responses

**Level**: Apprentice

**Mục đích**: Hiểu cách phân biệt username hợp lệ bằng cách quan sát sự khác nhau trong response.</p>
<hr>

## 1. Chuẩn bị

Mở lab trong **Burp Browser**.

Copy danh sách username và password vào hai file riêng:

- `username.txt`
- `password.txt`

Hai file này sẽ được dùng để brute-force.

## 2. Bắt request đăng nhập
<p>Nhấn vào <strong>My Account</strong> để mở trang đăng nhập.</p>
<p>Nhập bất kỳ thông tin nào và bắt request <strong>POST /login</strong> trong Burp Suite.</p>

<h2>3. Gửi request vào Intruder</h2>
<p>Chọn request và bấm <strong>Send to Intruder</strong>.</p>

<h3>Cấu hình Intruder:</h3>
<ul>
  <li>Attack type: <strong>Sniper</strong></li>
  <li>Payloads: tải file <code>username.txt</code> vào Payload Set</li>
</ul>
<p>Sau đó nhấn <strong>Start Attack</strong>.</p>

<p><img width="1365" height="633" alt="image" src="https://github.com/user-attachments/assets/e197fdbe-25db-44b0-a448-d92f79640f55"></p>

<h2>4. Quan sát phản hồi để tìm username hợp lệ</h2>
<p>Khi Intruder chạy, hãy chú ý cột <strong>Length</strong>. Bạn sẽ thấy một payload có độ dài phản hồi khác biệt so với các payload còn lại.</p>


<p>Trong ví dụ này:</p>
<ul>
  <li>Các username sai → phản hồi: <strong>"Invalid username"</strong></li>
  <li>Username <strong>ajax</strong> → phản hồi: <strong>"Incorrect password"</strong></li>
</ul>
<p><img width="1259" height="723" alt="image" src="https://github.com/user-attachments/assets/cdf6ec21-2625-41f6-9858-085ca1837a15"></p>

<p>Do đó, ta có thể kết luận <strong>ajax</strong> là một username hợp lệ.</p>

<h2>5. Brute-force password</h2>
<p>Sau khi tìm được username hợp lệ, lặp lại quá trình trên nhưng lần này brute-force trường password.</p>

<p>Kết quả: mật khẩu tìm được là <strong>111111</strong>.</p>

<p><img width="1290" height="231" alt="image" src="https://github.com/user-attachments/assets/363080a6-2d61-4d93-ab2a-491fb05637d5"></p>
