import unittest
import smtplib
from email_with_python.send_emails_using_oulook_server import (
    send_email_confirm_registration,
)


class SendEmailTest(unittest.TestCase):
    def test_send_email_confirm_registration(self):
        # Các thông số đầu vào cho hàm
        email = "sender@example.com"
        username = "testuser"
        password = "testpassword"
        code = "123456"
        to_email = "receiver@example.com"

        # Mock SMTP server
        class MockSMTP:
            def __init__(self, host, port):
                pass

            def ehlo(self):
                return (250, "OK")

            def starttls(self):
                return (220, "Ready to start TLS")

            def login(self, username, password):
                return (235, "Authentication successful")

            def sendmail(self, from_email, to_email, message):
                pass

            def quit(self):
                pass

        # Ghi đè smtplib.SMTP bằng MockSMTP
        smtplib.SMTP = MockSMTP

        # Gọi hàm send_email_confirm_registration
        result = send_email_confirm_registration(
            email, username, password, code, to_email
        )

        # Kiểm tra kết quả trả về
        self.assertEqual(result, "Email sent successfully")


if __name__ == "__main__":
    unittest.main()
