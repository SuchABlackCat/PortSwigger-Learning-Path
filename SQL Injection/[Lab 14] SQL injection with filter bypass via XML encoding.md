<h1>SQL injection with filter bypass via XML encoding</h1>
<h2>1. Quan sát request XML</h2>
<p>Chọn <code>View Detail</code> một mặt hàng bất kì, ấn vào <code>Check Restock</code> để bắt request.</p>
<p><img width="1027" height="538" alt="image" src="https://github.com/user-attachments/assets/4488297a-f3ed-489c-b4a9-4032e1c7a8b9" />
</p>
<p>=> Injection nằm trong &ltstoreId&gt.</p>

<h2>2. Thử payload đơn giản</h2>
<pre>
<storeId>1 UNION SELECT NULL</storeId></pre>
<p><img width="1027" height="570" alt="image" src="https://github.com/user-attachments/assets/e9e980a1-0b1f-49a0-a560-8ffbd08017a7" />
</p>
<p>→ Bị WAF block.</p>
<p>WAF = Web Application Firewall: Một lớp tường lửa chặn các payload SQLi nhìn quá “gian” như: <code>UNION</code>, <code>SELECT</code>, <code>' OR 1=1 --</code>, <code>--</code>, <code>&ltscript&gt</code>
<p>=> Đây là lý do payload thẳng bị chặn.</p>
<p>=> Phải obfuscate để bypass WAF.</p>

<h2>3. Encode payload bằng Hackvertor</h2>
<p><b>Hackvertor</b> là một extension trong Burp Suite.<br>Nó mã hóa (encode) ký tự của ta thành dạng entity XML như:</p>
<ul>
  <li>"U" → &#85;</li>
  <li>"SELECT" → chuỗi các entity</li>
</ul>
<p>Nếu không thấy, vào tab <code>Extensions</code> -> <code>BApp Store</code> -> Search "Hackvector" -> Install.</p>
<p>Ta sẽ viết payload bình thường:</p>
<pre>1 UNION SELECT NULL</pre>
<p>Sau đó bôi đen payload -> Right-click -> Extensions -> Hackvertor → Encode → hex_entities</p>
<p>Hackvertor sẽ biến thành dạng:</p>
<pre>&ltstoreId&gt&lt@hex_entities&gt1 UNION SELECT NULL&lt/@hex_entities&gt&lt/storeId&gt</pre>
<p><img width="1028" height="570" alt="image" src="https://github.com/user-attachments/assets/4ad36792-01db-4fe9-960a-c5522ce0db39" />
</p>

<h2>4. Xác định số cột</h2>
  <p>Sau đó ta thử thêm null, null để xác định số cột:</p>
  <p><img width="1028" height="526" alt="image" src="https://github.com/user-attachments/assets/835a61aa-e1db-4f46-86b9-484861002b58" />
</p>

<h2>5. Lấy username, password</h2>
<p>Vậy chỉ có 1 cột. Ta cần trích xuất cả username và password trong 1 cột => Nối chuỗi.</p>
<p>Response sẽ xuất hiện dạng:</p>
<pre>administrator~p4ssw0rd123
carlos~abcxyz
wiener~test123
</pre>

<p><img width="1029" height="524" alt="image" src="https://github.com/user-attachments/assets/43f78156-2c26-4e58-bb67-bdc61535e18c" />
</p>



→ Lấy cặp admin.
