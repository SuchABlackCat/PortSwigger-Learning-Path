<h1>Visible error-based SQL injection</h1>
<hr>
<h2>1. Chặn request và tìm TrackingId</h2>
<h2>2. Xác nhận verbose error</h2>

<p>
  <img width="1027" height="568" alt="image" src="https://github.com/user-attachments/assets/bb2ba98c-ec86-4e10-9ca4-30771e1bff84" />

</p>

<p>
  <img width="1029" height="572" alt="image" src="https://github.com/user-attachments/assets/b8b97561-8538-4894-9a9c-a2a90ffb7bec" />

</p>
<h2>3. Chèn thử SELECT</h2>
<p>
  <img width="1030" height="571" alt="image" src="https://github.com/user-attachments/assets/b137941c-9a52-46e8-9139-3cc50fd08586" />

</p>
<p>Bị giới hạn số kí tự => Bỏ trackingId</p>
<p>
  <img width="1029" height="570" alt="image" src="https://github.com/user-attachments/assets/8a59bcde-0d94-4730-8d7f-4402a40ac351" />

</p>
<p>Bỏ trackingId -> Lỗi trả lại nhiều hơn 1 dòng</p>
<p>
  <img width="1028" height="570" alt="image" src="https://github.com/user-attachments/assets/7d1eaf2e-1cf6-4c2d-9f11-a08120b6a48d" />

</p>
<p>Lỗi trả lại nhiều hơn 1 dòng -> limit lại</p>
<p>
  <img width="1029" height="569" alt="image" src="https://github.com/user-attachments/assets/8d71b9a4-9ccf-4690-b405-5d864091eb35" />

</p>
<p>Hỏi mật khẩu thì lỗi thừa kí tự -> Phải rút ngắn query lại</p>
<p><img width="1027" height="568" alt="image" src="https://github.com/user-attachments/assets/50f4a780-0fa9-45df-9713-c483cd3e63db" />
  <img width="1027" height="568" alt="image" src="https://github.com/user-attachments/assets/f2ebe3e7-bbfd-436d-a822-d45c6954bcf1" />

</p>
