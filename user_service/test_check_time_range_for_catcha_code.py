import unittest
from base_code.gettime import check_time_range


class TestCheckTimeRange(unittest.TestCase):

    # def test_valid_time_format_true(self):
    #     created_time = "2023-03-08 14:25:00"
    #     now_time = "2023-03-08 15:00:00"
    #     minute = 30

    #     result = check_time_range(created_time, now_time, minute)
    #     self.assertEqual(result ,"format false","format false")

    def test_invalid_time_format_false(self):
        created_time = "08-03-2023 14:30:00"
        now_time = "08-03-2023 15:00:00"
        minute = 30

        result = check_time_range(created_time, now_time, minute)
        self.assertEqual(result, "format false", "format false")

    def test_check_time_range_within_range(self):
        created_time = "2023-03-08 10:00:00"
        now_time = "2023-03-08 10:05:00"
        minute = 10

        result = check_time_range(created_time, now_time, minute)

        self.assertTrue(result)

    def test_check_time_range_outside_range(self):
        created_time = "2023-03-08 10:00:00"
        now_time = "2023-03-08 10:15:00"
        minute = 10

        result = check_time_range(created_time, now_time, minute)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
