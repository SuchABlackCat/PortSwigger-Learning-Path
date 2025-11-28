<h1>Basic SSRF against another back-end system</h1>
<p><strong>Mục tiêu</strong>:</p>
<p>Bài lab có chức năng <b>Check stock</b> gửi request từ server đến một địa chỉ nội bộ <code>192.168.0.X</code>.</p>
<p>Ta phải:</p>
<ul>
  <li>Quét dải IP nội bộ <code>192.168.0.1</code> → <code>192.168.0.255</code>.</li>
  <li>Tìm máy nào có admin interface chạy trên port <code>8080</code>.</li>
  <li>Khi tìm thấy admin interface, truy cập endpoint xóa user.</li>
  <li>Xóa user <code>carlos</code>.</li>
</ul>

<p>=> <b>Điểm khác với bài SSRF trước:</b> Admin interface không nằm ở <code>localhost</code>, mà nằm trong mạng nội bộ <code>192.168.0.X</code>.</p>

<hr>

<h2>Bước 1: Lấy request Check Stock</h2>
<p>Mở lab trong Burp Browser.</p>
<p>Chọn một sản phẩm bất kỳ → nhấn <b>Check stock</b>.<br>
Bắt request → Gửi qua Intruder.</p>
<p>Ta thấy tham số:</p>
<pre>stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&amp;storeId=1</pre>
<p><img width="1036" height="297" alt="image" src="https://github.com/user-attachments/assets/fe249f37-3221-477f-9bd2-7ad54faca521" />
</p>
<p>Đây là tham số ta sẽ thay đổi để ép server truy cập hệ thống nội bộ.</p>

<h2>Bước 2: Cấu hình Intruder để quét IP nội bộ</h2>
<p>Đổi stockApi thành: <code>stockApi=http://192.168.0.1:8080/admin</code></p>
<p>Ta sẽ scan octet cuối cùng – biến số từ 1 đến 255.<br>Bôi đen số <code>1</code> ở cuối địa chỉ → Nhấn <b>Add §</b> trong Intruder.</p>
<pre>http://192.168.0.§1§:8080/admin</pre>
<p>Trong <b>Payload</b>, phần <b>Payload Configuration</b>, điều chỉnh các tham số:</p>
<ul>
  <li>Payload type: <b>Numbers</b></li>
  <li>From: <b>1</b></li>
  <li>To: <b>255</b></li>
  <li>Step: <b>1</b></li>
</ul>
<p><img width="296" height="415" alt="image" src="https://github.com/user-attachments/assets/89d480b5-f01c-4bba-aad5-83d92d58efcc" />
</p>
<p>Nghĩa là Burp sẽ thử <code>192.168.0.1 → 192.168.0.2 → … → 192.168.0.255</code></p>
<p>Nhấn <b>Start attack</b>.</p>

<h2>Bước 3: Kết quả scan</h2>
<ul>
  <li>Hầu hết sẽ trả về lỗi (400, 404, 500…).</li>
  <li>Chỉ 1 IP sẽ trả về <b>Status 200</b> → IP này có admin interface.</li>
</ul>
<p><img width="1311" height="540" alt="image" src="https://github.com/user-attachments/assets/25073f99-7eb0-4be0-8a86-88b386810b3b" />
</p>
<p>Bấm vào request đó → Send to Repeater.</p>

<h2>Bước 4: Truy cập và xóa user <code>carlos</code> (qua SSRF)</h2>
<p>Trong Repeater, kiểm tra request:</p>
<pre>stockApi=http://192.168.0.137:8080/admin</pre>
<p>Server sẽ truy cập vào URL này và trả lại giao diện admin trong response.</p>

<p>Trong HTML, bạn sẽ thấy link xóa user dạng:</p>
<pre>/admin/delete?username=carlos</pre>
<p>Sửa request thành:</p>
<pre>stockApi=http://192.168.0.35:8080/admin/delete?username=carlos</pre>
<p>Quay lại tab Proxy → Gửi request → Server sẽ tự truy cập URL đó → User <code>carlos</code> bị xóa.</p>
