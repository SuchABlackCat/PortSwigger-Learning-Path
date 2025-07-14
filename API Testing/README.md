<h2>Project: Web cơ bản chứa API</h2>

<h3>1. Mục tiêu</h3>
<p>❓ API là gì?<br>
<i><b>API (Application Programming Interface)</b> là giao diện lập trình cho phép các ứng dụng giao tiếp với nhau.</i> Giống như "cầu nối" giữa frontend và backend.<br>
Ví dụ: Một app đọc sách cần lấy danh sách sách từ server → gọi API để lấy dữ liệu từ server.</p>

<p>❓ Project này làm gì?<br>
Tạo một hệ thống đơn giản cho phép người dùng lấy và thêm sách thông qua API.</p>

<p>Cụ thể:<br>
    <ul>
        <li>Có thể gọi <code>GET /api/books</code> để lấy danh sách sách. --> cho phép người dùng (hoặc giao diện web, app) xem toàn bộ dữ liệu hiện có.</li>
        <li>Có thể dùng <code>POST /api/books</code> để thêm sách mới. --> POST là cách gửi dữ liệu mới lên server → thêm sách vào cơ sở dữ liệu.</li>
        <li>Có API Key để bảo vệ (chỉ người có key mới truy cập được). --> API là công khai trên mạng. Nếu không có bảo vệ, bất kỳ ai cũng có thể truy cập. (VD: Nếu bạn công khai API mà không có API Key, bot/spammer có thể dùng tool tự động gọi API 1000 lần/giây để phá.)</li>
        <li>Có giới hạn tần suất gọi (rate limit).</li>
        <li>Có một trang HTML đơn giản để bấm nút test thử.</p></li>
    </ul>

<h3>2. Cấu trúc web và khái niệm</h3>
<pre>
simple-api-site/
├── index.html              # Giao diện web đơn giản (Frontend)
├── server.py               # Backend API sử dụng Flask
├── .env                    # Biến môi trường (chứa API_KEY)
│   └── API_KEY=123456789ABCDEF
└── requirements.txt        # Danh sách thư viện cần cài
    ├── Flask
    ├── Flask-Limiter
    └── python-dotenv
</pre>
<p>Một số khái niệm giải thích:
    <ul>
        <li>📌 Flask: framework siêu nhẹ giúp tạo web server bằng Python chỉ trong vài dòng.</li>
        <li>📌 API endpoint: một "địa chỉ" cụ thể để gửi yêu cầu.</li>
        <li>📌 HTTP method: các phương thức hành động khi làm việc với API: GET (lấy dữ liệu), POST (gửi dữ liệu), PUT (cập nhật), DELETE (xóa).</li>
        <li>📌 JSON (JavaScript Object Notation): cách phổ biến nhất để truyền dữ liệu giữa frontend và backend.</li>
    </ul>
</p>
