<h1>User ID controlled by request parameter, with unpredictable user IDs</h1>
<p>Mục tiêu: Truy cập vào tài khoản của <code>carlos</code> và lấy API key của anh ta.</p>

<p>Đầu tiên, ta cần tìm chỗ vô tình lộ ra <code>userId</code> trước.</p>
<p>Ta mở một blog bất kỳ, ví dụ bài đầu tiên.<br>Tên tác giả chính là <code>carlos</code>.</p>
<p>Khi click vào đó, trình duyệt chuyển sang page của carlos.</p>
<p>URL lúc này sẽ có dạng:</p>
<pre>?userId=abcxyz123...</pre>
<p>Chuỗi <code>abcxyz123...</code> này chính là userId thật của carlos.<br>Ta copy toàn bộ chuỗi userId này.</p>
<p>Login bằng user mà lab cung cấp (<code>weiner:peter</code>).</p>
<p>Sau khi đăng nhập, thay userId của mình bằng userId của carlos trên URL.</p>
<p>Copy API key của carlos và submit là xong.</p>
