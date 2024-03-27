import unittest
import sqlite3
from login_register_database import save_data_for_login_register_in_table


class TestSaveDataForLoginRegisterInTable(unittest.TestCase):

    def setUp(self):
        # Tạo kết nối tới cơ sở dữ liệu thử nghiệm
        self.conn = sqlite3.connect("database/login_register.db")
        self.cursor = self.conn.cursor()

        # Thêm dữ liệu vào bảng
        self.cursor.execute(
            f"INSERT INTO basic_login_register2 (username, password,email,createdTime) VALUES (?,?,?,?)",
            ("username1", "password1", "email1", "createdTime1"),
        )

        # Lưu thay đổi
        self.conn.commit()

    def tearDown(self):
        # Xóa dữ liệu thử nghiệm
        self.cursor.execute(
            "DELETE FROM basic_login_register2 WHERE username = 'username1' AND password = 'password1' AND email = 'email1' AND createdTime = 'createdTime1'"
        )

        # Lưu thay đổi và đóng kết nối
        self.conn.commit()
        self.conn.close()

    def test_save_data_for_login_register_in_table(self):
        # Gọi hàm muốn kiểm thử
        save_data_for_login_register_in_table(
            "username2", "password2", "email2", "createdTime2"
        )

        # Kiểm tra xem dữ liệu đã được thêm vào bảng chưa
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT username,password, email, createdTime FROM basic_login_register2 WHERE username = 'username2' AND password = 'password2' AND email = 'email2' AND createdTime = 'createdTime2'"
        )
        result = cursor.fetchone()

        # Kiểm tra xem kết quả trả về có đúng không
        self.assertEqual(result, ("username2", "password2", "email2", "createdTime2"))


if __name__ == "__main__":
    unittest.main()
