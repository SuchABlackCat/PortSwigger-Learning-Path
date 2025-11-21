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
  <p>Trong web, khi user chọn category Gifts, URL gọi:</p>
  <pre>https://insecure-website.com/products?category=Gifts</pre>
  <p>Ứng dụng tạo SQL:</p>
  <pre>SELECT * FROM products 
WHERE category = 'Gifts' AND released = 1;</pre>
  <p>Chỉ sản phẩm Gifts nào có <code>released = 1</code> mới được hiển thị trên web.</p>
  <p>Nếu muốn xem những sản phẩm có <code>released = 0</code> (hoặc tất cả), ta nhập payload sau vào URL:</p>
  <pre>...category=Gifts' or 1=1;--</pre>
  <p>SQL trở thành:</p>
  <pre>SELECT * FROM products 
WHERE category = 'Gifts' or 1=1;--' AND released = 1;</pre>
  <p>Phần sau <code>--</code>: <code>' AND released = 1;</code> bị biến thành comment.</p>
