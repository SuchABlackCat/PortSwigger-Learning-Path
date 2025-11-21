<h1>SQL injection UNION attack, finding a column containing text</h1>
<p>Mục tiêu: Inject 1 câu query với giá trị cho sẵn (<code>9zDgaw</code>)</p>

<h2>Cách làm</h2>
<p>Mở lab trong BurpSuite browser.</p>
<p>Chọn và bắt request <code>category=Gifts</code>.</p>
<p>Chuyển request sang Repeater để tiện sửa và gửi nhiều.</p>
<p>Xác định số cột:</p>
<p>
  <img width="1030" height="522" alt="image" src="https://github.com/user-attachments/assets/0856725d-094e-4b99-a614-ca3c7b06f47f" />

</p>
<p>Ta lần lượt thay kí tự với các giá trị NULL sao cho response trả về không lỗi là được:</p>
<p>
  <img width="1031" height="521" alt="image" src="https://github.com/user-attachments/assets/8da8f7a1-7051-47df-805d-f44ced61713a" />

</p>

<p>Trở về tab Proxy, gửi payload y hệt là xong lab!</p>
