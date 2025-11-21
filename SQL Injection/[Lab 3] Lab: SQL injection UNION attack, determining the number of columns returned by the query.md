<h1>SQL injection UNION attack, determining the number of columns returned by the query</h1>
<p>Mục tiêu: xác định số cột bằng 1 query toàn NULL.</p>

<p>Mở lab trong browser BurpSuite.</p>
<p>Ta sẽ chọn <code>category=Pets</code>.</p>
<p>Bắt request trong BurpSuite:</p>
<p>
  <img width="1028" height="457" alt="image" src="https://github.com/user-attachments/assets/ded60d50-273f-4e1f-aaea-ff2dc57c447e" />
</p>
<p>Do mình nghĩ bài này sẽ phải gửi nhiều request, nên nếu cứ Forward đi Forward lại cũng không tiện. Vậy nên mình sẽ chuyển request này sang Repeater.</p>
<p>Chọn request -> Chuột phải, <code>Send to Repeater</code> -> Inject để đoán số cột.</p>
<p>
  <img width="1026" height="529" alt="image" src="https://github.com/user-attachments/assets/0e4ac080-7cac-4f6f-a47a-79aa2cec3ca9" />

</p>
<p>Lần lượt thử:</p>
<pre>Pets'+union+select+null
Pets'+union+select+null,null
Pets'+union+select+null,null,null
...
</pre>
<p>Thử tới khi nào không còn lỗi nữa.</p>
<p>
  <img width="1032" height="523" alt="image" src="https://github.com/user-attachments/assets/420d5ae2-9b95-4bcb-88bd-fb3f65a3a68e" />

</p>
<p>Ta quay lại tab Proxy để Forward lần cuối là xong lab!</p>
<p>
  <img width="1026" height="518" alt="image" src="https://github.com/user-attachments/assets/f6f5d6cc-5556-4c08-845c-09243f3895fb" />

</p>
