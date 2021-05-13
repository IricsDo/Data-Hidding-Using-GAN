# ***DATA HIDDING USING GAN***

Project này dựa trên bài báo gốc https://arxiv.org/pdf/1901.03892.pdf và nguồn https://github.com/DAI-Lab/SteganoGAN.
Mọi sao chép cần ghi rõ nguồn.

# I. TÓM TẮT
Sau khi kham khảo source code ở https://github.com/DAI-Lab/SteganoGAN, tôi quyết định xây dựng một giao diện để người dùng có thể thao tác trực quan hơn.

*Toàn bộ project được thực hiện trên hệ điều hành linux - Ubuntu 18.04, cấu hình phần cứng là CPU Intel i5 8th Gen, 12G RAM. GPU GeForce MX 130, 2G RAM.*

# II. HƯỚNG DẪN SỬ DỤNG GIAO DIỆN
Giao diện được viết bằng thư viện Tkinter.
## 1. Chuẩn bị thư viện
	
	pip install -r requirement.txt
## 2. Thay đổi đường dẫn làm việc	
Trong file main.py ở dòng 471 thay đường dẫn tới thư mục SteganoGAN được lưu (fullpath_work).

Trong file second_window.py ở dòng 19 thay đường dẫn tới thư mục SteganoGAN lưu (fullpath_work).
## 3. Cách dùng giao diện

Chạy câu lệnh sau ở trong thư mục vừa tải về.

	python3 main.py
Sẽ thấy một giao diện xuất hiện giống như sau

 ![This is the main window you see](/images/2.png)

Giao diện gồm có các nút chức năng sau và cách hoạt động:
+ Load image cover: Thực hiện chọn ảnh muốn giấu thông tin vào đó. Đường dẫn trực tiếp của ảnh sẽ được hiển thị kế bên.

	- Hình ảnh sẽ được hiển thị bên dưới dòng chữ: Cover Image
+ Load model : Thực hiện chọn mô hình cho việc giấu thông tin. Đường dẫn trực tiếp của mô hình sẽ được hiển thị kế bên.
+ Encoder : Thực hiện giấu tin với ảnh và mô hình đã chọn.
	- Hình ảnh sau khi giấu tin sẽ được hiển thị ở bên dưới dòng chữ: Steganographic 
	- và được lưu ở thư mục có đường dẫn là ../SteganoGAN/result/-/
+ Decoder : Thực hiện giải mã thông tin với ảnh vừa giấu.
+ Evaluate: Thực hiện đánh giá với ảnh đã được giấu thông tin. Các thông số đánh giá gồm:

	- Accuracy  - Đây là thông số độ chính xác của mô hình ( khi giải mã).

	- RS-BPP    - Đây là thông số số bit được giấu trên một pixel ( đã được mã hóa ReedSolomon).

	- PSNR	    - Đây là thông số tín hiệu trên nhiễu ( so sánh giữa ảnh trước giấu tin và sau khi đã giấu tin).

	- SSIM      - Đây là thông số tỉ số tương đồng cấu trúc của ảnh trước và sau khi giấu tin. Một thông số khác dùng để đánh giá.

+ Get Key  : Đây là chế độ tùy chọn, khi nhấn thông tin sẽ được mã hóa trước khi giấu.
+ Enter Key: Nút này là bắt buộc nếu người dùng đã nhấn Get Key ở trên, người dùng sẽ phải chọn khóa đã được tạo thông qua nút Get Key, nhập khóa vào thì thông tin sau khi giải mã mới chính xác, nếu không thông tin sẽ không thể đọc được.

	- Tệp khóa sẽ được lưu ở thư mục có đường dẫn là ../SteganoGAN/key/
	
Bên dưới Message encode là nơi để nhập thông tin cần giấu (văn bản).

Bên dưới Message decode là nơi thông tin được giải mã sẽ hiển thị.

+ Clear message : Khi nhấn toàn bộ văn bản ở bên duới Message encode và Message decode sẽ được xóa.
+ Open file: Thực hiện giấu một tệp được lưu dưới dạng .txt

	- Ô trống đầu tiên phía dưới là nơi hiển thị đường dẫn tới tệp txt muốn giấu.
	- Ô trống thứ hai sẽ là nơi hiển thị đường dẫn tới tệp txt đã được giải mã.
	- Tệp txt được lưu mặc định ở thư mục có đường đãn là ../SteganoGAN/message/

Có hai tùy chọn chế độ giấu tin cho người dùng là giấu tin là văn bản hoặc giấu tin là hình ảnh. Click chuột để chọn chế độ người dùng muốn sử dụng.

Chọn chế độ giấu tin là văn bản để sử dụng các chức năng nhập từ bàn phím hoặc mở từ một tệp txt.

Khi chọn chế độ giấu tin là hình ảnh, trước khi thực hiện nhấn nút Encoder cần phải:

Nhấn Open image: Xuất hiện một giao diện thứ hai giống như sau

![This is the second window you see](/images/1.png)

Ở giao diện này có các nút sau:

+ Open image: Thực hiện chọn hình ảnh cần giấu. Đường dẫn trực tiếp của hình ảnh sẽ được hiển thị kế bên.
+ Open text: Thực hiện chọn tệp txt, đó chính là hình ảnh đang ở dạng văn bản. Đường dẫn trực tiếp của hình ảnh sẽ được hiển thị kế bên.
+ Im2Tex: Thực hiện chuyển đổi hình ảnh sang văn bản.
	- Văn bản sau khi chuyển đổi từ  hình ảnh sẽ được lưu ở thư mục có đường dẫn là ../SteganoGAN/text_decode/
+ Tex2Im: Thực hiện chuyển đổi văn bản sang hình ảnh.
	- Hình ảnh sau khi chuyển đổi từ văn bản sẽ được lưu ở thư mục có đường dẫn là ../SteganoGAN/image_decode/

Nếu người dùng lỡ nhấn thóat cửa số thứ hai này, trước khi người dùng thực hiện chuyển đổi từ văn bản sang hình ảnh, người dùng cần phải nhập kích thước của hình ảnh muốn khôi phục với định dạng như sau:

` w:{width} h:{height}`

` Note: ở giữa là giấu cách, ví dụ: w:12 h:12 hoặc w:128 h:128`
	
rồi mới nhấn nút Tex2Im.
# III. HẠN CHẾ
Theo bài báo, mô hình cho kết quả tốt nhất là **Dense Encoder**. Tuy nhiên do phần cứng của máy tôi không đủ tốt, tôi chỉ chạy được những mô hình **Basic Encoder** do đó một số kết quả của hình ảnh sau khi *Enconder* tôi đưa cho bạn có chất lượng không được tốt.

Những mô hình pre-train các bạn thấy ở thư mục models là do tôi đã sử dụng Google Colab Pro để huấn luyện. Nhưng đa số chỉ huấn luyện với một vài vòng lặp cho nên mô hình chưa được tối ưu nhất. Bạn có thể không sử dụng các mô hình này của tôi, mà tự tay mình huấn luyện mô hình khác tốt hơn. Bạn có thể kham khảo cách huấn luyện tại source gốc (https://github.com/DAI-Lab/SteganoGAN).

