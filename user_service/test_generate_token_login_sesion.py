import unittest
from base_code.get_token import generate_random_token_string
import string


class GenerateTokenTest(unittest.TestCase):
    def test_token_length(self):
        length = 10

        # Gọi hàm generate_random_token_string
        token = generate_random_token_string(length)

        # Kiểm tra độ dài của token
        self.assertEqual(len(token), length, "Độ dài token không đúng")

    def test_token_characters(self):
        length = 10

        # Gọi hàm generate_random_token_string
        token = generate_random_token_string(length)

        # Kiểm tra xem token chỉ chứa các ký tự chữ cái và số
        self.assertTrue(
            all(c in string.ascii_letters + string.digits for c in token),
            "Token không chứa cả chữ và số",
        )


if __name__ == "__main__":
    unittest.main()
