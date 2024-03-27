import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from base_code.string_python_en import responses


class RegisterBasicTest(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch("main.query_database_for_login_register_by_email")
    def test_register_with_existing_email(self, mock_query_email):
        mock_query_email.return_value = True
        response = self.client.post(
            "/api/register_basic",
            json={"name": "test", "pass": "test", "email": "test@example.com"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "response": {
                    "message": responses["email_da_duoc_dang_ky"],
                    "status": False,
                }
            },
        )

    @patch("main.query_database_for_login_register_by_email")
    @patch("main.query_database_for_login_register_by_name")
    def test_register_with_existing_username(self, mock_query_name, mock_query_email):
        mock_query_email.return_value = False
        mock_query_name.return_value = True
        response = self.client.post(
            "/api/register_basic",
            json={"name": "test", "pass": "test", "email": "test@example.com"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "response": {
                    "message": responses["user_da_ton_tai"],
                    "status": False,
                }
            },
        )

    @patch("main.query_database_for_login_register_by_email")
    @patch("main.query_database_for_login_register_by_name")
    @patch("main.send_email_confirm_registration")
    def test_successful_registration(
        self, mock_send_email, mock_query_name, mock_query_email
    ):
        mock_query_email.return_value = False
        mock_query_name.return_value = False
        response = self.client.post(
            "/api/register_basic",
            json={"name": "test", "pass": "test", "email": "test@example.com"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "response": {
                    "message": responses["check_email_to_get_code"],
                    "status": True,
                }
            },
        )
        mock_send_email.assert_called_once()

    def test_invalid_request_data(self):
        response = self.client.post("/api/register_basic", json={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"response": {"message": responses["co_loi_xay_ra"], "status": False}},
        )
