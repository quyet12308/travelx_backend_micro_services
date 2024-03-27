import unittest
import sqlite3
from catcha_code_for_send_email import query_data_by_email_with_max_id


class TestQueryDataByEmailWithMaxId(unittest.TestCase):

    def setUp(self):
        # Tạo kết nối tới cơ sở dữ liệu thử nghiệm
        self.conn = sqlite3.connect("database/catchat_code_for_send_email.db")
        self.cursor = self.conn.cursor()

        # Thêm dữ liệu vào bảng
        self.cursor.execute(
            f"INSERT INTO catchat_code_for_send_email (username,email ,createdTime,code) VALUES (?,?,?,?)",
            ("username1", "email1", "createdTime1", "code1"),
        )
        self.cursor.execute(
            f"INSERT INTO catchat_code_for_send_email (username,email ,createdTime,code) VALUES (?,?,?,?)",
            ("username2", "email2", "createdTime2", "code2"),
        )
        self.cursor.execute(
            f"INSERT INTO catchat_code_for_send_email (username,email ,createdTime,code) VALUES (?,?,?,?)",
            ("username3", "email3", "createdTime3", "code3"),
        )

        # Lưu thay đổi
        self.conn.commit()

    def tearDown(self):
        # Xóa dữ liệu thử nghiệm
        self.cursor.execute(
            "DELETE FROM catchat_code_for_send_email WHERE email = 'email1' OR email = 'email2' OR email = 'email3'"
        )

        # Lưu thay đổi và đóng kết nối
        self.conn.commit()
        self.conn.close()

    def test_query_data_by_email_with_max_id(self):
        # Gọi hàm muốn kiểm thử
        result = query_data_by_email_with_max_id("email2")

        # Kiểm tra xem kết quả trả về có đúng không
        self.assertEqual(result[1:], ("username2", "email2", "createdTime2", "code2"))


if __name__ == "__main__":
    unittest.main()
