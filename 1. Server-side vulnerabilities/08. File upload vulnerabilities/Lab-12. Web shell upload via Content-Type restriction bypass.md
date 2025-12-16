<h1>Lab: Web Shell Upload via Content-Type Restriction Bypass</h1>
<p><strong>Mục tiêu</strong>:</p>
<p>Lab có chức năng upload ảnh nhưng phần kiểm tra loại file dựa vào <b><i>Content-Type do người dùng gửi</i></b>.<br>
Ta sẽ lợi dụng điều này để upload web shell PHP và đọc nội dung tệp <code>/home/carlos/secret</code>.
</p>

<hr>

<h2>Bước 1: Đăng nhập tài khoản</h2>
<p>Sử dụng tài khoản: <code>weiner:peter</code>.<br>Sau khi đăng nhập xong, tính năng upload avatar hiện ra.</p>

<h2>Bước 2: Xác định nơi avatar được tải</h2>
<ol>
  <li>Upload một ảnh hợp lệ.</li>
  <li>Trở lại My Account, avatar mới xuất hiện.</li>
  <li>Right-click vào ảnh avatar mới, "Open in new tab".</li>
  <li>Nhìn URL để biết file được lưu trong <code>/files/avatars/</code></li>
</ol>

<h2>Bước 3: Tạo web shell PHP và upload thử</h2>
<p>Tạo file <code>exploit.php</code> với nội dung:</p>
<pre>&lt?php echo file_get_contents('/home/carlos/secret'); ?&gt</pre>
<p>Khi upload <code>.php</code>, server báo lỗi:<br> Chỉ cho phép <code>image/jpeg</code> hoặc <code>image/png</code>.</p>
<p><img width="1184" height="118" alt="image" src="https://github.com/user-attachments/assets/e1b662ba-701f-44f5-86e2-e1e8cc9a7e40" />
</p>
<p>=> Server chỉ kiểm tra <b><i>Content-Type trong body</i></b> → có thể chỉnh tay để bypass.</p> 

<h2>Bước 4: Bypass kiểm tra Content-Type</h2>
<ol>
  <li>Trong Burp, tìm request <code>POST /my-account/avatar</code>.</li>
  <li>Gửi sang <b>Repeater</b>.</li> <li>Trong phần file, sửa: <pre>Content-Type: image/jpeg</pre> thay vì loại MIME thật của file PHP. </li>
  <li>Gửi request → Upload thành công.</li> 
</ol> 
<p><img width="1030" height="571" alt="image" src="https://github.com/user-attachments/assets/baeda597-aa6d-4c5d-a4f0-893bdab09ad6" />
</p>

<h2>6. Gọi web shell để lấy secret</h2>
<ol>
  <li>Sau khi upload thành công, quay lại My Account</li>
  <li>Right-click, mở avatar trong tab mới</li>
  <li>Copy secret và submit là xong.</li>
</ol>
<p><img width="840" height="95" alt="image" src="https://github.com/user-attachments/assets/32b7bf90-9243-4fcf-89bd-d594a8ffc7cc" />
</p>
