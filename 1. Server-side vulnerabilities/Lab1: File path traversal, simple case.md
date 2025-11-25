<h1>File path traversal, simple case</h1>
<p>Mở BurpSuite.</p>
<p>Khi reload lại trang, bắt 1 trong các request có parameter <code>filename=...</code> và chuyển nó vào Repeater.</p>
<p><img width="1027" height="540" alt="image" src="https://github.com/user-attachments/assets/25d97018-99da-411b-81df-cd2315841ccc" />
</p>
<p>Ta lần lượt thử các payload vào <code>filename=...</code> để biết <code>/ect/passwd</code> nằm ở đâu:</p>
<pre>../etc/passwd
../../etc/passwd
../../../etc/passwd</pre>
<p>(<code>../</code> là quay về thư mục cha 1 lần)</p>
<p>Ta thành công lấy được pass:</p>
<p><img width="1028" height="525" alt="image" src="https://github.com/user-attachments/assets/ce21b94b-7dd2-4963-b231-375a8dfc3fa4" />
</p>
