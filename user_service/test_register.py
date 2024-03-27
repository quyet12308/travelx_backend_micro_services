import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from base_code.string_python_en import responses
from unittest import mock


# class TestRegistrationAPI(unittest.TestCase):

#     def setUp(self):
#         self.client = TestClient(app)

#     def test_register_basic(self):
#         # Tạo dữ liệu kiểm thử
#         request_data = {
#             "name": "test_user",
#             "pass": "testpass",
#             "email": "test@example.com",
#         }

#         # Gọi API `register_basic`
#         response = self.client.post("/api/register_basic", json=request_data)
#         data = response.json()

#         # Kiểm tra kết quả trả về từ API
#         self.assertTrue("response" in data)
#         self.assertTrue("message" in data["response"])
#         self.assertTrue("status" in data["response"])

#         # Kiểm tra các trường hợp kết quả trả về
#         if "message" in data["response"]:
#             if data["response"]["message"] == responses["email_da_duoc_dang_ky"]:
#                 self.assertFalse(data["response"]["status"])
#             elif data["response"]["message"] == responses["user_da_ton_tai"]:
#                 self.assertFalse(data["response"]["status"])
#             elif data["response"]["message"] == responses["check_email_to_get_code"]:
#                 self.assertTrue(data["response"]["status"])

# Phần xác nhận code với email hiện đang lỗi do vấn đề truy xuất với catcha database.
# def test_register_confirm_code_email(self):
#     # Tạo dữ liệu kiểm thử
#     request_data = {
#         "pass": "testpass",
#         "email": "test@example.com",
#         "code": "123456",
#     }

#     # Ghi đè hàm query_data_by_email_with_max_id
#     with mock.patch("main.query_data_by_email_with_max_id") as mock_query_data:
#         # Thiết lập giá trị trả về từ hàm query_data_by_email_with_max_id
#         mock_query_data.return_value = (
#             1,
#             "test_user",
#             "test@example.com",
#             "25-03-2024",
#             "123456",
#         )
#     # Gọi API `register_confirm_code_email`
#     response = self.client.post(
#         "/api/register_confirm_code_email", json=request_data
#     )
#     data = response.json()

#     # Kiểm tra kết quả trả về từ API
#     self.assertTrue("response" in data)
#     self.assertTrue("message" in data["response"])
#     self.assertTrue("status" in data["response"])

#     # Kiểm tra các trường hợp kết quả trả về
#     if "message" in data["response"]:
#         if data["response"]["message"] == responses["dang_ky_thanh_cong"]:
#             self.assertTrue(data["response"]["status"])
#         elif data["response"]["message"] == responses["sai_code"]:
#             self.assertFalse(data["response"]["status"])
#         elif data["response"]["message"] == responses["code_bi_qua_thoi_gian"]:
#             self.assertFalse(data["response"]["status"])


# if __name__ == "__main__":
#     unittest.main()
