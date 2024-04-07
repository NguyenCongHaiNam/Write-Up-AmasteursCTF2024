## Description

> average southern californian reacts to DC weather. amazing scenery though at the time.

Find the coords of this image!

Grader Command: nc chal.amt.rs 1771



## Recon

Dựa vào những bức hình đề bài cho thì mình dự đoán ban đầu địa điểm ở một con suối hay con lạch nào đấy nhưng vẫn chưa hiểu `bathroom` đề bài đề cập là gì. Tạm gác lại, giờ cần tìm địa điểm trong ảnh trước đã. Bước đầu thì vẫn là ném lên [Google Image](https://lens.google.com/) xem nó có detect được không đã.
![image](https://github.com/NguyenCongHaiNam/Write-Up-AmasteursCTF2024/assets/116544941/8178d5f9-d5f8-4b1a-b10a-142edb95f144)![image](https://github.com/NguyenCongHaiNam/Write-Up-AmasteursCTF2024/assets/116544941/367bf8bc-83d2-4fbd-b4d9-93b0b6fcfd7c)

Có vẻ kết quả gần đúng nhưng chưa chính xác nên mình vẫn chưa thể xác định chính xác đây là địa điểm nào. Tìm kiếm trên đây một lúc thì mình đã tìm được clue khá khớp với hình ảnh

<img width="959" alt="image" src="https://github.com/NguyenCongHaiNam/Write-Up-AmasteursCTF2024/assets/116544941/4e49b82f-4ece-4734-b6a5-524820ee0494">

(***bài viết mình tìm thấy trên ig trong bài viết này và bài viết khi mình làm không giống nhau nhưng sol way thì vẫn thế***)

Xem qua trang ig này một lúc thì có vẻ là trang truyền thông của một quần thể du lịch nào đó có tên là MammothGear, tìm kiếm thêm thông tin trên mạng thì mình đưa ra được kết luận:

> Bức ảnh chụp ở một đoạn Hot Creek( suối nước nóng) trong quần thể MammothGear

Bây giờ thì tìm kiếm cái `review` mà đề bài đã đề cập trong `I remember needing to go to the bathroom near where these pictures were taken and then leaving a review` thôi. Nhắc đến review thì ta có thể nghĩ đến Google Map, một công cụ vô cùng phổ biến. Lục lọi một lúc thì mình tìm được![image](https://github.com/NguyenCongHaiNam/Write-Up-AmasteursCTF2024/assets/116544941/ca528932-2c6a-4e17-a34e-c960b5463e82)

Thông tin khá khớp với những giừ mình đã có, địa điểm là một "Hot Creek", có "bathroom" ở gần, nhưng đi sâu vào từng bức ảnh và street view mình vẫn không tìm được cái review đề bài đề cập. Quay lại vị trí phía trên mình để ý có một cái toilet tên là `Vault Toilets` khá nổi bật, thì đúng như vậy "go to the bathroom" trong đề bài ngoài nghĩa là đến nhà tắm hay đến bồn tắm ra thì còn có nghĩa là....![image](https://github.com/NguyenCongHaiNam/Write-Up-AmasteursCTF2024/assets/116544941/3b35fa32-9676-4093-afa9-174d9bf075ac)





