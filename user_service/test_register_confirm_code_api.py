import unittest
from unittest.mock import patch
from main import register_confirm_code_email
from base_code.string_python_en import responses


class RegisterConfirmCodeEmailTest(unittest.TestCase):

    async def test_successful_registration(self):
        # Mock các hàm phụ thuộc
        with patch("main.query_data_by_email_with_max_id") as mock_query_code, patch(
            "main.check_time_range"
        ) as mock_check_time, patch(
            "main.save_data_for_login_register_in_table"
        ) as mock_save_data, patch(
            "main.hash_password"
        ) as mock_hash_password:
            # Thiết lập dữ liệu giả cho các hàm phụ thuộc
            mock_query_code.return_value = (
                1,
                "username1",
                "email1",
                "2023-03-08 12:00:00",
                "123456",
            )
            mock_check_time.return_value = True
            mock_hash_password.return_value = "hashed_password"

            # Gọi hàm `register_confirm_code_email` với dữ liệu yêu cầu
            request_data = {"pass": "password", "email": "email1", "code": "123456"}
            response = await register_confirm_code_email(request_data)

            # Xác minh kết quả trả về
            self.assertEqual(
                response["response"]["message"], responses["dang_ky_thanh_cong"]
            )
            self.assertEqual(response["response"]["status"], True)

            # Xác minh rằng các hàm phụ thuộc được gọi với các đối số chính xác
            mock_query_code.assert_called_once_with(email="email1")
            mock_check_time.assert_called_once_with(
                now_time="2023-03-08 12:00:00",
                created_time="2023-03-08 12:00:00",
                minute=3,
            )
            mock_save_data.assert_called_once_with(
                createdTime="2023-03-08 12:00:00",
                email="email1",
                password="hashed_password",
                username="username1",
            )

    async def test_invalid_code(self):
        # Mock các hàm phụ thuộc
        with patch("main.query_data_by_email_with_max_id") as mock_query_code, patch(
            "main.check_time_range"
        ) as mock_check_time, patch(
            "main.save_data_for_login_register_in_table"
        ) as mock_save_data, patch(
            "main.hash_password"
        ) as mock_hash_password:
            # Thiết lập dữ liệu giả cho các hàm phụ thuộc
            mock_query_code.return_value = (
                1,
                "username1",
                "email1",
                "2023-03-08 12:00:00",
                "123456",
            )
            mock_check_time.return_value = True

            # Gọi hàm `register_confirm_code_email` với dữ liệu yêu cầu
            request_data = {"pass": "password", "email": "email1", "code": "987654"}
            response = await register_confirm_code_email(request_data)

            # Xác minh kết quả trả về
            self.assertEqual(response["response"]["message"], responses["sai_code"])
            self.assertEqual(response["response"]["status"], False)

            # Xác minh rằng các hàm phụ thuộc được gọi với các đối số chính xác
            mock_query_code.assert_called_once_with(email="email1")
            mock_check_time.assert_called_once_with(
                now_time="2023-03-08 12:00:00",
                created_time="2023-03-08 12:00:00",
                minute=3,
            )
            mock_save_data.assert_not_called()

    async def test_expired_code(self):
        # Mock các hàm phụ thuộc
        with patch("main.query_data_by_email_with_max_id") as mock_query_code, patch(
            "main.check_time_range"
        ) as mock_check_time, patch(
            "main.save_data_for_login_register_in_table"
        ) as mock_save_data, patch(
            "main.hash_password"
        ) as mock_hash_password:
            # Thiết lập dữ liệu giả cho các hàm phụ thuộc
            mock_query_code.return_value = (
                1,
                "username1",
                "email1",
                "2023-03-08 11:57:00",
                "123456",
            )
            mock_check_time.return_value = False

            # Gọi hàm `register_confirm_code_email` với dữ liệu yêu cầu
            request_data = {"pass": "password", "email": "email1", "code": "123456"}
            response = await register_confirm_code_email(request_data)

            # Xác minh kết quả trả về
            self.assertEqual(
                response["response"]["message"], responses["code_bi_qua_thoi_gian"]
            )
            self.assertEqual(response["response"]["status"], False)

            # Xác minh rằng các hàm phụ thuộc được gọi với các đối số chính xác
            mock_query_code.assert_called_once_with(email="email1")
            mock_check_time.assert_called_once_with(
                now_time="2023-03-08 12:00:00",
                created_time="2023-03-08 11:57:00",
                minute=3,
            )
            mock_save_data.assert_not_called()

    async def test_invalid_request_data(self):
        # Gọi hàm `register_confirm_code_email` với dữ liệu yêu cầu không hợp lệ
        request_data = {}
        response = await register_confirm_code_email(request_data)

        # Xác minh kết quả trả về
        self.assertEqual(response["response"]["message"], responses["co_loi_xay_ra"])
        self.assertEqual(response["response"]["status"], False)
