import unittest
from hash_function import *


class PasswordHashingTest(unittest.TestCase):
    def test_hash_password(self):
        password = "password123"

        # Gọi hàm hash_password để mã hóa mật khẩu
        encoded_password = hash_password(password)

        # Kiểm tra xem kết quả trả về có phải là một chuỗi hex không
        self.assertIsInstance(encoded_password, str)
        self.assertRegex(encoded_password, r"^[0-9a-fA-F]+$")

    def test_verify_password(self):
        password = "password123"

        # Gọi hàm hash_password để mã hóa mật khẩu
        encoded_password = hash_password(password)

        # Gọi hàm verify_password để kiểm tra mật khẩu
        result = verify_password(password, encoded_password)

        # Kiểm tra xem kết quả trả về có phải là True không
        self.assertTrue(result)

    def test_verify_password_invalid(self):
        password = "password123"
        incorrect_password = "wrongpassword"

        # Gọi hàm hash_password để mã hóa mật khẩu
        encoded_password = hash_password(password)

        # Gọi hàm verify_password với mật khẩu không chính xác
        result = verify_password(incorrect_password, encoded_password)

        # Kiểm tra xem kết quả trả về có phải là False không
        self.assertFalse(result)

    def test_verify_password_modified(self):
        password = "password123"

        # Gọi hàm hash_password để mã hóa mật khẩu
        encoded_password = hash_password(password)

        # Sửa đổi chuỗi mã hóa để kiểm tra xác nhận mật khẩu thất bại
        modified_encoded_password = "0123456789abcdef0123456789abcde0"

        # Gọi hàm verify_password với chuỗi mã hóa bị sửa đổi
        result = verify_password(encoded_password, modified_encoded_password)

        # Kiểm tra xem kết quả trả về có phải là False không
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
