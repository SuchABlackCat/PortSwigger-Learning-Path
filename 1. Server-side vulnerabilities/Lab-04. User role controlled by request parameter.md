<h1>User role controlled by request parameter</h1>
<p>Ở bài này, ta không còn cách truy cập trang admin thông qua URL đặc biệt như /admin-panel nữa. Nghĩa là nếu truy cập thẳng URL admin thì server sẽ chặn. Nhưng lab vẫn có lỗi — chỉ khác cách khai thác.</p>
<h2>Bước 1: Bắt request</h2>
<p>Mở lab trong browser Burp Suite. Ta dùng Burp để chặn mọi request gửi từ browser.</p>
<p>Khi bắt request, ta để ý thấy có dòng cookie dạng:</p>
<pre>Cookie: Admin=false...</pre>
<p>=> !!! Cookie nằm ở client, mà ứng dụng dựa vào giá trị Admin=true/false trong cookie để quyết định user có phải admin hay không.<br>=>Ta có thể sửa từ false thành true.</p>

<h2>Bước 2: Thay <code>Admin=false</code> thành <code>Admin=true</code></h2>
<p>Bất kỳ request nào có dòng <code>Admin=false</code>, ta đều sửa thành: <code>Admin=true</code> và rồi forward request đó.</p>
<p><img width="1313" height="556" alt="image" src="https://github.com/user-attachments/assets/0961e418-7f5e-440f-af49-986fbae25dbb" />
</p>
<p><b><i>Tại sao phải sửa mọi request?</i></b></p>
<p>Vì chỉ cần một request gửi sai (Admin=false), server sẽ coi ta là user thường.</p>
<p>Ta không cần đăng nhập tài khoản đã cho, vẫn có thể vào được Admin panel.</p>
<p><img width="1342" height="386" alt="image" src="https://github.com/user-attachments/assets/5a942767-e01d-4930-a97d-dc70525d8b5f" />
</p>
<p>Điều quan trọng lạ: MỌI REQUEST CÓ <code>Admin=false</code> ĐỀU PHẢI ĐỔI THÀNH <code>true</code></p>
<p>Sau đó, ta chỉ cần xóa tài khoản carlos là xong lab!</p>
<p><img width="1351" height="472" alt="image" src="https://github.com/user-attachments/assets/e03dff5c-8505-4ab6-be50-bf6e2cbb0d20" />
</p>
