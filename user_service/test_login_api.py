import unittest
from fastapi.testclient import TestClient
from main import app
from base_code.string_python_en import responses

client = TestClient(app)


class LoginBasicTest(unittest.TestCase):
    def test_login_success(self):
        request_data = {"name": "000000", "pass": "123456a"}

        response = client.post("/api/login_basic", json=request_data)
        data = response.json()

        # Kiểm tra kết quả trả về từ API
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["response"]["status"])
        self.assertEqual(data["response"]["message"], responses["dang_nhap_thanh_cong"])
        self.assertIsNotNone(data["response"]["token"])
        self.assertIsNotNone(data["response"]["email"])
        self.assertIsNotNone(data["response"]["avata_img"])

    def test_login_wrong_password(self):
        request_data = {"name": "000000", "pass": "wrong_password"}

        response = client.post("/api/login_basic", json=request_data)
        data = response.json()

        # Kiểm tra kết quả trả về từ API
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data["response"]["status"])
        self.assertEqual(data["response"]["message"], responses["sai_mat_khau"])

    def test_login_invalid_account(self):
        request_data = {"name": "nonexistent_user", "pass": "password"}

        response = client.post("/api/login_basic", json=request_data)
        data = response.json()

        # Kiểm tra kết quả trả về từ API
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data["response"]["status"])
        self.assertEqual(
            data["response"]["message"], responses["tai_khoan_chua_duoc_dang_ky"]
        )


if __name__ == "__main__":
    unittest.main()
