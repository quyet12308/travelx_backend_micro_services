import unittest
from datetime import datetime
from pytz import timezone
from base_code.gettime import gettime2


class GetTime2Test(unittest.TestCase):
    def setUp(self):
        # Chuẩn bị môi trường cho các phương thức kiểm thử
        self.result = gettime2()

    def test_return_type(self):
        # Kiểm tra kiểu dữ liệu trả về
        self.assertIsInstance(self.result, str)

    def test_date_format(self):
        # Kiểm tra định dạng của chuỗi thời gian trả về
        expected_format = "%Y-%m-%d %H:%M:%S"
        self.assertEqual(
            datetime.strptime(self.result, expected_format).strftime(expected_format),
            self.result,
        )

    # đang lỗi không xác định được timezone từ 1 cái chuỗi vd : 2024-03-24 23:13:32
    # def test_time_zone(self):
    #     # Kiểm tra múi giờ
    #     expected_timezone = timezone("Asia/Ho_Chi_Minh")
    #     current_timezone = timezone(self.result)
    #     self.assertEqual(
    #         current_timezone, expected_timezone, f"time zone bị lỗi {current_timezone}"
    #     )


if __name__ == "__main__":
    unittest.main()
