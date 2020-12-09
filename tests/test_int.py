import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app , db  #bcrypt
from application.models import Tasks

#set test variables for todo application 

test_todo_title_1 = "Job1"
test_todo_description_1 ="Description1"

class TestBase(LiveServerTestCase):
    
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/maxpa_qzrio/repositories/todo_app_day2/todo-list-app/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    # def test_server_is_up_and_running(self):
    #     response = urlopen("http://0.0.0.0:5000")
    #     self.assertEqual(response.code, 200)


class TestRegistration(TestBase):
    
    def test_registration(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be 
        redirected to the login page
        """

        # Click add  button link  menu link
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)
      #  assert url_for('/create') in self.driver.current_url
#         # Fill in registration form
#         self.driver.find_element_by_xpath('<xpath for registration email>').send_keys(test_admin_email)
#         self.driver.find_element_by_xpath('<xpath for registration first name>').send_keys(
#            test_admin_first_name)
#         self.driver.find_element_by_xpath('<xpath for registration last name>').send_keys(
#             test_admin_last_name)
#         self.driver.find_element_by_xpath('<xpath for registration password>').send_keys(
#    #       test_admin_password)
#         self.driver.find_element_by_xpath('<xpath for registration check password>').send_keys(
#             test_admin_password)
#         self.driver.find_element_by_xpath('<xpath for register button>').click()
#        time.sleep(1)

#         # Assert that browser redirects to login page
#         assert url_for('login') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)