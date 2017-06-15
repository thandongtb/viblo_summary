# -*- coding: utf-8 -*-

import nlp

if __name__ == "__main__":
    title = "Philippines phá hủy để cứu vãn thành phố bị phiến quân chiếm đóng"
    content = "Cuộc giao tranh bước sang tuần thứ tư ở Marawi đến nay đã khiến hơn 200 người thiệt mạng và khiến hạ tầng ở thành phố này bị hư hại nghiêm trọng. Trong bối cảnh, phiến quân Hồi giáo Maute tiếp tục cố thủ ở một số khu vực của Marawi, quân đội Philippines những ngày gần đây đã tăng cường các cuộc không kích vào các mục tiêu của chúng. New York Times bình luận, quân đội Philippines dường như đang áp dụng chiến lược phá hủy để cứu vãn Marawi với việc ném bom các mục tiêu phiến quân ít nhất 2 lần mỗi ngày. Bị tàn phá trên diện rộng trong khi hầu hết cư dân đã phải sơ tán để tránh các cuộc giao tranh khiến Marawi giờ đây giống như một thành phố ma. Giới chức địa phương hiện đã lên kế hoạch cho một chương trình khôi phục Marawi sau khi chiến sự kết thúc song công việc tái thiết thành phố được dự đoán là một thách thức vô cùng lớn. Trong khi đó, các tay súng Hồi giáo hiện vẫn chiếm giữ một phần khu vực trung tâm Marawi, nắm các chốt kiểm soát ở một số cây cầu và gài các tay súng bắn tỉa ở một số nhà thờ trong thành phố. Do hàng trăm dân thường vẫn còn mắc kẹt ở Marawi khiến chiến dịch tiêu diệt phiến quân của quân đội trở nên khó khăn hơn. Ngoài ra, các tay súng phiến quân cố thủ trên các tòa nhà cao tầng cũng là yếu tố buộc binh sĩ Philippines phải giữ khoảng cách.Một tư lệnh quân đội cho biết, phiến quân Maute hiện kiểm soát khoảng 20% thành phố ở phía đông nam sông A gus, song chiến sự chỉ diễn ra ác liệt nhất ở khu vực khoảng 500m2.Đây là một cuộc chiến ở thành thị, một cuộc chiến mặt đối mặt. Chúng vẫn cố thủ. Cuộc chiến là hết nhà này đến nhà kia, tòa này đến tòa khác, Christopher Tampus, một tư lệnh đơn vị bộ binh, cho biết.Với việc kiểm soát vùng trời, quân đội Philippines đã tiến hành các cuộc không kích nhằm vào phiến quân. Các cuộc không kích đã hủy hoại nhiều cơ sở hạ tầng ở Marawi nhưng đến nay vẫn chưa thể đẩy lùi hoàn toàn phiến quân khỏi đây. Quân đội Philippines cho biết, phiến quân dùng các nhà thờ hoặc trường học công giáo để làm căn cứ chiến đấu, trong khi quân đội buộc phải tránh tấn công vì đây là những công trình tôn giáo được bảo vệ.Cuộc chiến ở Marawi cũng đánh dấu lần đầu tiên nhóm khủng bố Abu Sayyaf do tên Isnilon Hapilon đứng đầu và nhóm Maute bắt tay tiến hành một chiến dịch lớn. Ngoài ra, các tay súng ngoại quốc từ Indonesia, Malaysia, Ả rập Xê út, Yemen và Chechnya được cho là cũng tham gia vào cuộc chiến ở đây."

    title_segmentation = nlp.tokenizer_content(content=title)
    segmentation = nlp.tokenizer_content(content=content)

    keywords = nlp.keywords(segmentation)
    print keywords

    summary_sents = nlp.summarize(title=title_segmentation, text=segmentation)
    summary = '\n'.join(summary_sents)
    print summary