from argparse import Namespace
from time import sleep
from unittest import TestCase

from src.utils import Utils
from selenium import webdriver


class TestUtils(TestCase):
    def test_send_notification(self):
        Utils.args = Namespace()
        Utils.args.disable_apprise = False
        Utils.sendNotification("title", "body")

    def test_selenium(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        sleep(10)
