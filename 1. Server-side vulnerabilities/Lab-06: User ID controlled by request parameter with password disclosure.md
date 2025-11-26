<h1>User ID controlled by request parameter with password disclosure</h1>
<p>Mục tiêu: Truy cập trang của <code>administrator</code>, lấy mật khẩu rồi đăng nhập.</p>

<h2>Bước 1: Mở lab bằng Burp Browser và đăng nhập tài khoản được cấp</h2>
<p>Khi đăng nhập vào tài khoản thông thường, ta để ý URL trên thanh địa chỉ:</p>

<pre>?id=weiner</pre>
<p><img width="822" height="568" alt="image" src="https://github.com/user-attachments/assets/e3f8b8cc-9ad1-44c4-8c0c-ed19881d4463" />
</p>
<p>Điều này cho thấy ứng dụng lấy thông tin người dùng dựa trên tham số <code>id</code> ở URL.  
Nếu server không kiểm tra quyền, ta chỉ cần đổi giá trị này là có thể xem thông tin của người khác.</p>

<h2>Bước 2: Thử đổi ID sang tài khoản admin</h2>

<p>Vì ta biết username admin thường là <code>administrator</code>, ta thử đổi URL thành:</p>

<pre>?id=administrator</pre>
<p><img width="829" height="567" alt="image" src="https://github.com/user-attachments/assets/be5df126-b8b6-4067-8380-d40234a34922" />
</p>
<p>Trình duyệt sẽ gửi request tương ứng.  
Ta dùng Burp Suite để bắt response và xem server trả về gì.</p>

<h2>Bước 3: Xem response trong Burp – server trả về mật khẩu admin</h2>

<p>Trong response, ta thấy toàn bộ thông tin của admin được trả về, bao gồm cả <b>password</b>.  
Đây chính là lỗi: server không kiểm tra xem người dùng hiện tại có quyền xem dữ liệu đó hay không.</p>
<p><img width="1027" height="527" alt="image" src="https://github.com/user-attachments/assets/1ef8b17b-ac2a-45d1-b3d8-44394ff997f7" />
</p>
<h2>Bước 4: Đăng nhập bằng tài khoản administrator</h2>

<p>Sau khi có password:</p>
<ol>
  <li>Đăng xuất.</li>
  <li>Đăng nhập lại bằng username <code>administrator</code> và password vừa lấy.</li>
  <li>Vào Admin panel và xóa user <code>Carlos</code>.</li>
</ol>
