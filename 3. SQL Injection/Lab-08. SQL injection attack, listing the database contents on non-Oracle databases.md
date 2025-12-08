<h1>SQL injection attack, listing the database contents on non-Oracle databases</h1>
<p>Mục tiêu: Log in as admin</p>

<hr>
<p>Mở lab trong BurpSuite browser.</p>
<p>Chọn và bắt request <code>category=Gifts</code>.</p>
<p>Chuyển request sang Repeater để tiện sửa và gửi nhiều.</p>
<p>Xác định table:</p>
<p>
  <img width="1026" height="519" alt="image" src="https://github.com/user-attachments/assets/b7cd175a-9a81-4431-908c-51f0b03ea9b9" />

</p>
<p>Xác định column</p>
<p>
  <img width="1025" height="520" alt="image" src="https://github.com/user-attachments/assets/5b0d2a83-16c2-4b50-988f-e6dd930653f5" />

</p>
<p>Lấy data:</p>
<p>
  <img width="1026" height="522" alt="image" src="https://github.com/user-attachments/assets/77b387ea-2ea7-4f3d-b7ed-31793960fc82" />

</p>
<p>Chỉ cần log in bằng data này là xong lab!</p>
