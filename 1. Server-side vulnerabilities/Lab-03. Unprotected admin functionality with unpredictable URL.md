<h1>Unprotected admin functionality with unpredictable URL</h1>
<p>Đầu tiên, ta đang nghi ngờ ứng dụng có admin page ẩn. Vì vậy, ta thử xem trong source code xem có manh mối nào bị lộ không.</p>
<h2>Bước 1: View page source</h2>
<p>Right-Click -> View page source -> Ta thấy 1 đoạn code:</p>
<p><img width="785" height="685" alt="image" src="https://github.com/user-attachments/assets/4ec6abf6-d345-482a-8729-0e185bab23a8" />
</p>
<ul>
  <li>Dù <code>isAdmin=false</code>, toàn bộ đoạn code vẫn được gửi xuống cho mọi user.</li>
  <li>Nghĩa là ai cũng có thể xem URL <code>/admin-h8yfl6</code> bằng cách xem source.</li>
</ul>
<p>=> Lỗi: URL admin chỉ ẩn, không chặn.</p>

<h2>Bước 2: Kiểm thử URL được tiết lộ</h2>
<p>Ta sẽ thêm <code>/admin-h8yfl6</code> vào cuối URL để vào được admin page:</p>
<p><img width="992" height="390" alt="image" src="https://github.com/user-attachments/assets/90671835-1c51-4ae0-b1b4-b0923685f048" />
</p>
<p>Ta ấn delete user <code>Carlos</code> là xong!</p>
