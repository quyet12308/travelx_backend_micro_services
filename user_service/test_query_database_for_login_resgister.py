import unittest
from login_register_database import query_database_for_login_register_by_name


class DatabaseQueryTestForLoginResgiter(unittest.TestCase):
    def test_query_exists(self):
        name = "000000"
        # name = "00000"

        # Gọi hàm query_database_for_login_register_by_name
        result = query_database_for_login_register_by_name(name)

        # Kiểm tra xem kết quả trả về có phải là một từ điển không
        self.assertIsInstance(
            result, dict, "Kết quả trả về không phải là dict hoặc là đã trả về none"
        )

    def test_check_result_has_elements(self):
        name = "000000"

        result = query_database_for_login_register_by_name(name)
        # Kiểm tra xem từ điển có chứa các khóa cần thiết không
        self.assertIn("id", result, "Không chứa id trong result")
        self.assertIn("username", result, "Không chứa username trong result")
        self.assertIn("email", result, "Không chứa email trong result")
        self.assertIn("password", result, "Không chứa password trong result")
        self.assertIn("birthday", result, "Không chứa birthday trong result")
        self.assertIn("avata_img", result, "Không chứa avata_img trong result")
        self.assertIn("createdTime", result, "Không chứa createdTime trong result")

    def test_query_not_exists(self):
        name = "Nonexistent"

        # Gọi hàm query_database_for_login_register_by_name
        result = query_database_for_login_register_by_name(name)

        # Kiểm tra xem kết quả trả về có phải là None không
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
