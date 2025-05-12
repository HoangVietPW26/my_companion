import os
import datetime
import yagmail

def is_even_day():
    """Kiểm tra xem hôm nay có phải ngày chẵn trong tuần không (thứ 2, 4, 6)"""
    today = datetime.datetime.now().weekday()
    # 0 = thứ 2, 2 = thứ 4, 4 = thứ 6 (đều là ngày chẵn)
    return today in [1, 3, 5]

def send_reminder():
    """Gửi email nhắc nhở nếu hôm nay là ngày chẵn"""
    if not is_even_day():
        print(f"Hôm nay không phải ngày chẵn trong tuần. Không gửi nhắc nhở.")
        return
    
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    
    # Lấy thông tin từ biến môi trường
    sender_email = os.environ.get('EMAIL')
    app_password = os.environ.get('PASSWORD')
    receiver_email = os.environ.get('RECEIVER')
    
    # Nội dung email
    subject = f"Nhắc nhở trò chuyện với Claude - {today}"
    content = f"""
    Xin chào bạn,
    
    Đây là lời nhắc nhở cho cuộc trò chuyện với Claude vào lúc 10:15 hôm nay ({today}).
    
    Hãy chia sẻ kết quả của bạn trong 2 ngày qua và những khó khăn bạn đang gặp phải.
    
    Nhớ rằng mỗi bước tiến, dù nhỏ, đều đáng ghi nhận!
    
    Chúc bạn một ngày tốt lành,
    Chương trình nhắc nhở
    """
    
    try:
        # Gửi email bằng yagmail
        yag = yagmail.SMTP(sender_email, app_password)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=content
        )
        print(f"Đã gửi email nhắc nhở thành công vào {datetime.datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

if __name__ == "__main__":
    send_reminder()