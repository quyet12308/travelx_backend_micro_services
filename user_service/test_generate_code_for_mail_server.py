import unittest
from base_code.get_code import generate_random_6_digit_number


class GenerateRandomCodeForMailServer(unittest.TestCase):
    def setUp(self):
        self.result = generate_random_6_digit_number()

    def test_lenght_of_code(self):

        # Kiểm tra độ dài của số ngẫu nhiên
        self.assertEqual(len(self.result), 6, "Độ dài code ko đúng")

    def test_type_of_code(self):
        # Kiểm tra kiểu dữ liệu trả về
        self.assertIsInstance(self.result, str, "Kiểu dữ liệu code không đúng")

    def test_isdigit_of_code(self):
        # Kiểm tra số ngẫu nhiên có phải là một số nguyên không
        self.assertTrue(self.result.isdigit(), "Số không phải là 1 số nguyên")

    def test_is_within_approx(self):
        # Kiểm tra số ngẫu nhiên có nằm trong khoảng từ 000000 đến 999999 không
        self.assertGreaterEqual(
            int(self.result), 0, "Số nằm ngoài khoảng từ 0 đến 999999"
        )
        self.assertLessEqual(
            int(self.result), 999999, "Số nằm ngoài khoảng từ 0 đến 999999"
        )


if __name__ == "__main__":
    unittest.main()
