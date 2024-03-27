from base_code.security_info import *
from email_with_python.send_emails_using_oulook_server import *

password = passwords["outlook"]
email = emails["outlook2"]
# # # print(password)
# #     # password = getpass.getpass("Enter password: ")
code = "000000"  # Thay bằng code bạn muốn gửi đi
to_email = emails["email_test_to_send"]  # Địa chỉ email của người nhận
result = send_email_forgot_password(
    email=email, username="test", password=password, code=code, to_email=to_email
)

if result == "Email sent successfully":
    print("ok")
else:
    print("something wrong to send email , please check your email again")
