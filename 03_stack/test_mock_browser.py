import unittest

import sys

sys.path.append("mock_broswer")

from mock_broswer import Browser


class TestMockBrowser(unittest.TestCase):
    def test_can_not_go_back_and_go_forward(self):
        browser = Browser()
        self.assertEqual(browser.go_back(), None)
        self.assertEqual(browser.go_forward(), None)

    def test_go_back_and_go_forward(self):
        browser = Browser()
        prefix = "https://example.com/page/"
        for i in range(5):
            browser.open(f"{prefix}{i+1}")
        self.assertEqual(browser.go_back(), f"{prefix}{4}")
        self.assertEqual(browser.go_back(), f"{prefix}{3}")
        self.assertEqual(browser.go_forward(), f"{prefix}{4}")

    def test_open_new_page_clear_forward_stack(self):
        browser = Browser()
        prefix = "https://example.com/page/"
        for i in range(5):
            browser.open(f"{prefix}{i+1}")
        browser.go_back()
        browser.go_back()
        browser.open(f"{prefix}{5}")
        self.assertEqual(browser.go_forward(), None)


if __name__ == '__main__':
    unittest.main()
