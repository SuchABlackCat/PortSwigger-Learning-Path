<h1>Remote code execution via web shell upload</h1>
<p>Lab có một chức năng upload ảnh bị lỗi: server không hề kiểm tra loại file, nội dung file, hay phần mở rộng.<br>
Điều này cho phép upload file khác ảnh lên server, sau đó truy cập file đó để chạy code tùy ý (RCE).</p>
<p><strong>Mục tiêu</strong>:</p>
<ul>
  <li>Upload web shell PHP</li>
  <li>Dùng web shell để đọc file: <code>/home/carlos/secret</code></li>
  <li>Nhập secret để hoàn thành lab</li>
</ul>

<hr>

<h2>Bước 1: Đăng nhập và upload file</h2>
<p>Mở lab bằng Burp Browser.</p>
<p>Đăng nhập bằng tài khoản: <code>wiener:peter</code>. Khi đó ta sẽ thấy chức năng upload avatar.</p>
<p><img width="733" height="563" alt="image" src="https://github.com/user-attachments/assets/d7b41b43-71b9-4fd2-bb62-eac3be718d24" />
</p>
<p>Sau khi upload → quay lại My account → Ảnh avatar mới được hiển thị.</p>

<h2>Bước 2: Tìm URL nơi file được lưu</h2>
<p>Khi ấn chuột trái để mở ảnh, ta thấy nó được lưu trong <code>/files/avatars/</code></p>
<p><img width="1363" height="683" alt="image" src="https://github.com/user-attachments/assets/2254461f-267a-4e36-905b-675a782986d7" />
</p>

<h2>Bước 3: Tạo web shell PHP và update thử</h2>
<p>Tạo một file tên <code>exploit.php</code> với nội dung:</p>
<pre>&lt;?php echo file_get_contents('/home/carlos/secret'); ?&gt;</pre>
<p>Web shell này rất đơn giản: khi truy cập file, server sẽ chạy PHP và trả về nội dung của file secret.</p>
<p>Dùng chức năng upload avatar của lab, upload <code>exploit.php</code>.<br>Server không validate gì nên file PHP được upload thành công.</p>
<p>Response sẽ báo "Image uploaded successfully" (mặc dù không phải ảnh).</p>
<p><img width="734" height="676" alt="image" src="https://github.com/user-attachments/assets/d0a91ff8-7ca6-4826-844d-129e055ad204" />
</p>


<h2>Bước 4: Thực thi web shell</h2>
<p>Trên URL của ảnh vừa ấn chuột trái để xem, ta nhập:</p>
<pre>/files/avatars/exploit.php</pre>
<p><img width="1184" height="135" alt="image" src="https://github.com/user-attachments/assets/31ac44a5-233b-41d1-9e4e-00ae75712b90" />
</p>
<p>Ấn Enter.</p>
<p><img width="1182" height="131" alt="image" src="https://github.com/user-attachments/assets/e089beab-f16e-4e61-b24a-0356fc9e58f0" />
</p>
<p>Copy secret và dán vào ô submit của banner lab → Lab Solved!</p>

