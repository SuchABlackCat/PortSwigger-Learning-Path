<h1>Blind SQL injection with conditional responses</h1>
<hr>
<p>Mở lab trong BurpSuite browser.</p>
<p>Tìm request có <code>Cookie: TrackingId=...</code></p>
<p>
  <img width="1027" height="467" alt="image" src="https://github.com/user-attachments/assets/4617ac16-ccf5-48bc-b4d9-d8a52964c26b" />

</p>
<p>Chuyển request này vào Repeater.</p>
<p>Khi ta gửi truy vấn đúng và sai:</p>
<p>
  <img width="1028" height="564" alt="image" src="https://github.com/user-attachments/assets/29d9cbfd-ed0a-4628-afa5-cae7592a38d9" />
  <img width="1028" height="568" alt="image" src="https://github.com/user-attachments/assets/422e120f-ba5b-4490-8f53-6e2e7038b0ae" />

</p>
<p>Chú ý đến đoạn kí tự <code>Welcome back!</code>.</p>
<p>Kiểm tra xem bảng <code>users</code> có tồn tại hay không:</p>
<p>
  <img width="1027" height="567" alt="image" src="https://github.com/user-attachments/assets/b81414a2-bad7-47f3-951e-c4a7a4fc383e" />

</p>
<ul>
  <li>Nếu thực sự có bảng <code>users</code> thì query sẽ trả về kí tự <code>'a'</code>.</li>
  <li><code>LIMIT 1</code> để trả về 1 dòng kết quả trên cùng.</li>
</ul>
<p>Tiếp tục thử xem có user là <code>administrator</code> không:</p>
<p>
  <img width="1027" height="567" alt="image" src="https://github.com/user-attachments/assets/e6b9259a-ba58-44dc-8a4b-fcef8d5550fa" />

</p>
<p>Thử nhiều lần xem độ dài password là bao nhiêu (<=10, <=9,...). Kết quả:</p>
<p>
  <img width="1028" height="569" alt="image" src="https://github.com/user-attachments/assets/52757a43-c8ee-4aec-95f4-fcc6ee9780d7" />

</p>
<p>Giờ đoán từng kí tự trong password:</p>
<p>Đầu tiên, ta gửi request này vào Intruder. Sửa payload để nó tự động thay đổi kí tự vào vị trí kí tự a</p>
<p>
  <img width="880" height="486" alt="image" src="https://github.com/user-attachments/assets/7c0c6176-f36b-4d61-a0df-1eb3f0bee9b2" />

</p>
<p>Phía bên phải, khung Payload, lần lượt config như sau:</p>
<ul>
  <li>Đảm bảo <code>Payload type: Simple list</code></li>
  <li>Phần <code>Payload Configuration</code>, điền từng kí tự một từ 0-9, a-z (hoặc tạo 1 file txt xong load lên cho nhanh).</li>
  <li>Chọn <code>Settings</code> ngoài cùng, phần <code>Grep-Match</code>, thêm từ "Welcome back" vào.</li>
</ul>
<p>Xong rồi, chọn <code>Start attack</code></p>
<p>Vậy kí tự đầu tiên là "q":</p>
<p>
  <img width="1282" height="155" alt="image" src="https://github.com/user-attachments/assets/ec0ff77d-3251-4555-91ae-678b5062fc6b" />

</p>
<p>Tiếp tục thay payload:</p>
<pre>TrackingId=xyz'+and+(select+substring(password,2,1)+from+users+where+username='administrator')='a
TrackingId=xyz'+and+(select+substring(password,3,1)+from+users+where+username='administrator')='a</pre>
<p>Làm tương tự cho đến khi có hết password: <code>qq4wmykrig9sj49y1bif</code></p>
