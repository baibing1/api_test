import unittest
import requests
import json
from read_excel import *

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list('test_user_data.xlsx','TestUserLogin')

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list,'test_user')

