<h1>Basic SSRF against the local server</h1>
<p><strong>Mục tiêu</strong>:</p>
<p>Bài lab có chức năng <code>Check stock</code>.<br>Chức năng này gửi request từ <i>server</i> đến một URL nội bộ.</p><p></p>Ta sẽ lợi dụng điều này để:</p>
<ul>
  <li>Gửi server tới <code>http://localhost/admin</code>.</li>
  <li>Xem được trang admin thông qua SSRF.</li>
  <li>Xóa user <code>carlos</code>.</li>
</ul>

<hr>

<h2>Bước 1: Kiểm tra xem admin interface có chặn truy cập trực tiếp không</h2>
<p>Mở lab bằng Burp Browser và thử truy cập <code>/admin</code>. Bạn sẽ thấy trang báo lỗi, vì user bình thường không được phép truy cập trang admin.</p>

<h2>Bước 2: Khai thác chức năng Check Stock</h2>
<p>
Chọn một sản phẩm bất kỳ → Nhấn <b>Check stock</b>.  
Burp Suite sẽ bắt request này trong Proxy → Gửi request sang Repeater.
</p>

<p>Trong request, bạn sẽ thấy parameter <code>stockApi</code> dạng URL-encoded như sau:</p>

<pre>stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1</pre>
<p><img width="516" height="569" alt="image" src="https://github.com/user-attachments/assets/4e18fee5-210b-46d2-ac47-bdf4ce06871d" />
</p>
<p>Đây chính là địa chỉ mà <b>server sẽ tự truy cập đến</b> để lấy thông tin tồn kho.</p>


<h2>Bước 3: Đổi stockApi để SSRF vào localhost</h2>
<p>Ta sửa tham số <code>stockApi</code> thành URL admin nội bộ:</p>

<pre>stockApi=http://localhost/admin</pre>
<p><img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/a67f9489-d70d-45b1-91b8-608e86a174bb" />
</p>
<p>Khi gửi request trong Repeater, server sẽ tự truy cập <code>localhost/admin</code>.  
Do request đến từ chính máy chủ, access control sẽ bị bypass và ta xem được trang admin trong response.</p>

<h2>Bước 4: Tìm link xóa user</h2>
<p>Trong response từ <code>localhost/admin</code>, bạn sẽ thấy HTML chứa đường link dạng:</p>

<pre>&lt;a href="/admin/delete?username=wiener"&gt;Delete user&lt;/a&gt;</pre>
<p><img width="522" height="569" alt="image" src="https://github.com/user-attachments/assets/8d067925-6c19-4ec3-bcdd-c0d0af77f63c" />
</p>
<p>
Đây là endpoint dùng để xóa user.  
Ta chỉ cần gọi đúng endpoint nhưng thay username thành <b>carlos</b>.
</p>

<h2>Bước 5: Thực hiện SSRF để xóa user carlos</h2>

<p>Sửa lại tham số <code>stockApi</code> thành URL xóa user mục tiêu:</p>

<pre>stockApi=http://localhost/admin/delete?username=carlos</pre>

<p>Gửi request trong Repeater → Quay lại Proxy và nhấn <b>Forward</b> nếu cần.  
Khi server truy cập URL này, user <b>carlos</b> sẽ bị xóa.  
Bạn hoàn thành bài lab!</p>


