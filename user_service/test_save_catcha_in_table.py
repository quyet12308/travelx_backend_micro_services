import unittest
import sqlite3
from catcha_code_for_send_email import save_data_for_confirm_code_in_table


class TestSaveDataForConfirmCodeInTable(unittest.TestCase):

    def setUp(self):
        # Tạo kết nối tới cơ sở dữ liệu thử nghiệm
        self.conn = sqlite3.connect("database/catchat_code_for_send_email.db")
        self.cursor = self.conn.cursor()

        # Thêm dữ liệu vào bảng
        self.cursor.execute(
            f"INSERT INTO catchat_code_for_send_email (username,email ,createdTime,code) VALUES (?,?,?,?)",
            ("username", "email", "createdTime", "code"),
        )

        # Lưu thay đổi
        self.conn.commit()

    def tearDown(self):
        # Xóa dữ liệu thử nghiệm
        self.cursor.execute(
            "DELETE FROM catchat_code_for_send_email WHERE username = 'username' AND email = 'email' AND createdTime = 'createdTime' AND code = 'code'"
        )

        # Lưu thay đổi và đóng kết nối
        self.conn.commit()
        self.conn.close()

    def test_save_data_for_confirm_code_in_table(self):
        # Gọi hàm muốn kiểm thử
        save_data_for_confirm_code_in_table("username", "email", "createdTime", "code")

        # Kiểm tra xem dữ liệu đã được thêm vào bảng chưa
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT username, email, createdTime, code FROM catchat_code_for_send_email WHERE username = 'username' AND email = 'email' AND createdTime = 'createdTime' AND code = 'code'"
        )

        result = cursor.fetchone()

        # Kiểm tra xem kết quả trả về có đúng không
        self.assertEqual(result, ("username", "email", "createdTime", "code"))
