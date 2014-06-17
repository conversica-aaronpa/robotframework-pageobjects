import unittest
from po.loggingpage import LoggingPage


class LoggingTestCase(unittest.TestCase):

    def setUp(self):
        self.p = LoggingPage()

    def test_log_to_file_and_screen(self):
        self.p.log_stuff_to_stdout_and_file("hello world")

unittest.main()