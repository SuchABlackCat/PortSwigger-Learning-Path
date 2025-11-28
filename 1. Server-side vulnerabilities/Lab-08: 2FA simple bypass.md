<h1>2FA Simple Bypass</h1>

<p>Trong lab này, cơ chế xác thực hai yếu tố (2FA) có thể bị bỏ qua. Bạn đã có sẵn username và password hợp lệ, nhưng không có mã 2FA. Mục tiêu của bạn là truy cập được vào trang tài khoản của <strong>Carlos</strong>.</p>

<h2>Thông tin đăng nhập</h2>
<ul>
  <li><strong>Tài khoản của bạn:</strong> wiener : peter</li>
  <li><strong>Tài khoản nạn nhân:</strong> carlos : montoya</li>
</ul>

<hr>

<h2>1. Đăng nhập vào tài khoản của bạn</h2>
<p>Vào trang <strong>My Account</strong> và đăng nhập bằng tài khoản <code>wiener : peter</code>.</p>
<p>Hệ thống sẽ yêu cầu mã 2FA với thông báo: <em>"Please enter your 4-digit security code."</em></p>
<p>Nhấn vào nút <strong>Email client</strong> để mở hộp thư và lấy mã 2FA.</p>

<h2>2. Quan sát URL của trang tài khoản</h2>
<p>Sau khi nhập mã 2FA và đăng nhập thành công, bạn sẽ vào trang tài khoản của mình.</p>
<p>Hãy chú ý URL lúc này, thường có dạng:</p>

<pre><code>/my-account</code></pre>

<p>Đây chính là URL mà bạn có thể truy cập sau khi qua bước 2FA.</p>
<p>Đăng xuất hoàn toàn khỏi tài khoản của bạn.</p>


<h2>3. Đăng nhập bằng tài khoản của Carlos</h2>
<p>Đăng nhập bằng username <code>carlos</code> và password <code>montoya</code>.</p>
<p>Bạn sẽ lại bị chặn ở bước nhập mã 2FA – nhưng lần này bạn không có email của Carlos.</p>

<h2>5. Bypass 2FA</h2>
<p>Ngay tại màn hình yêu cầu nhập mã 2FA, bạn chỉ cần sửa thủ công URL trên trình duyệt thành:</p>

<pre><code>/my-account</code></pre>

<p>Rồi nhấn Enter.</p>

<p>Nếu ứng dụng không kiểm tra lại trạng thái 2FA khi tải trang, bạn sẽ truy cập thẳng vào trang tài khoản của Carlos mà không cần mã xác thực.</p>
