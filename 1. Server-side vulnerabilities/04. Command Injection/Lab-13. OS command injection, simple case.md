<h1>OS command injection, simple case</h1>

<h2>Bước 1: Chuẩn bị</h2>
<p>Mở Burp Suite → Proxy → Open Browser → Mở lab trong browser của Burp Suite → Bật Intercept: On</p>

<h2>Bước 2: Tìm request chứa tham số có thể bị chèn (recon)</h2>
<ul>
  <li>Trên web app, ấn vào 1 sản phẩm bất kỳ.</li>
  <li>Ấn <strong>Check Stock</strong> để tạo request.</li>
  <li>Quay lại Burp Suite, bắt request đó. Chú ý nội dung request phải có <code>productId=...&storeId=...</code></li>
</ul>

<h2>Bước 3: Gửi payload</h2>
<ul>
  <li>Thay <code>storeID</code> bằng <code>1|whoami</code>. Khi server ghép chuỗi vào lệnh gọi script, <code>whoami</code> được thực thi và output của nó xuất hiện trong response.</li>
  <li>Forward request đã sửa lên server.</li>
</ul>
<p><img width="1030" height="571" alt="image" src="https://github.com/user-attachments/assets/25b4507f-f3c6-4ea3-9556-f6a1afbc2e07" />
</p>
