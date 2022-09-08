from multiprocessing.dummy.connection import Client
import time
from typing import KeysView
import django
from django.conf import settings
from django.forms import ValidationError
from django.test import tag
from selenium import webdriver
from django.test import LiveServerTestCase
from site import USER_BASE
from selenium.webdriver.common.action_chains import ActionChains
# from create_session_cookie import create_session_cookie
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.conf import settings
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth import (
    SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY,
    get_user_model
)
from django.test.client import RequestFactory

request = RequestFactory()
User= get_user_model()

class TestProjectListPage(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.user = User.objects.create_superuser(username='nayan',password='password', email='nayankhemka9@gmail.com')
        # self.user=user_model.objects.create_user(username="nayan",password="pass123")
        self.user.is_staff = True
        self.user.save()
        
    def tearDown(self):
        self.browser.quit()
    
    def login(self):
        self.browser.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.browser.find_element(By.NAME,"username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element(By.NAME,"password")
        password_input.send_keys('password')
        loginbttn=self.browser.find_element(By.CLASS_NAME,'submit-row')
        login=loginbttn.find_element(By.TAG_NAME,'input')
        login.click()

    def test_login(self):
        self.login()
        self.browser.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1.5)
        k=self.browser.find_element(By.TAG_NAME,"h3")
        self.assertIn(k.text,'User Account')
        k=self.browser.find_element(By.CLASS_NAME,"div-container").find_element(By.TAG_NAME,"a")
        k.click()
        t=self.browser.find_element(By.ID,'id-google-address')
        t.send_keys('Kolk')
        t.click()
        time.sleep(1)
        t.send_keys(Keys.BACKSPACE)
        time.sleep(4)
        t.click()
    
    def test_location(self):
        self.login()
        self.browser.get('%s%s' % (self.live_server_url, ''))
        # time.sleep(1)
        self.browser.find_element(By.LINK_TEXT,'Route').click()
        x=self.browser.find_element(By.ID,'id-google-address-a')
        x.send_keys('kelam')
        x.click()
        time.sleep(1)
        x.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        x.send_keys(Keys.DOWN)
        y=self.browser.find_element(By.ID,'id-google-address-c')
        y.send_keys('egmore')
        y.click()
        time.sleep(1)
        y.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        y.send_keys(Keys.DOWN)
        z=self.browser.find_element(By.ID,'id-google-address-d')
        z.send_keys('egmo')
        z.click()
        time.sleep(1)
        z.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        z.send_keys(Keys.DOWN)
        w=self.browser.find_element(By.ID,'id-google-address-b')
        w.send_keys('Vanda')
        w.click()
        time.sleep(1)
        w.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        w.send_keys(Keys.DOWN)
        self.browser.find_element(By.TAG_NAME,'h3').click()
        time.sleep(15)

    def test_directions(self):
        self.login()
        self.browser.get('%s%s' % (self.live_server_url, ''))
        # time.sleep(1)
        self.browser.find_element(By.LINK_TEXT,'Route').click()
        x=self.browser.find_element(By.ID,'id-google-address-a')
        x.send_keys('kelam')
        x.click()
        time.sleep(1)
        x.send_keys(Keys.BACKSPACE)
        x.send_keys(Keys.DOWN)
        y=self.browser.find_element(By.ID,'id-google-address-c')
        y.send_keys('egmore')
        y.click()
        time.sleep(1)
        y.send_keys(Keys.BACKSPACE)
        y.send_keys(Keys.DOWN)
        z=self.browser.find_element(By.ID,'id-google-address-d')
        z.send_keys('egmo')
        z.click()
        time.sleep(1)
        z.send_keys(Keys.BACKSPACE)
        z.send_keys(Keys.DOWN)
        w=self.browser.find_element(By.ID,'id-google-address-b')
        w.send_keys('Vanda')
        w.click()
        time.sleep(1)
        w.send_keys(Keys.BACKSPACE)
        w.send_keys(Keys.DOWN)
        self.browser.find_element(By.TAG_NAME,'h3').click()
        time.sleep(5)
        self.browser.find_element(By.ID,'dir-toggle').find_element(By.LINK_TEXT,'here').click()
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def test_s(self):
        self.login()
        self.browser.get('%s%s' % (self.live_server_url, ''))
        # time.sleep(1)
        self.browser.find_element(By.LINK_TEXT,'Route').click()
        x=self.browser.find_element(By.ID,'id-google-address-a')
        x.send_keys('kelam')
        x.click()
        time.sleep(1)
        x.send_keys(Keys.BACKSPACE)
        x.send_keys(Keys.DOWN)
        y=self.browser.find_element(By.ID,'id-google-address-c')
        y.send_keys('egmore')
        y.click()
        time.sleep(1)
        y.send_keys(Keys.BACKSPACE)
        y.send_keys(Keys.DOWN)
        z=self.browser.find_element(By.ID,'id-google-address-d')
        z.send_keys('egmo')
        z.click()
        time.sleep(1)
        z.send_keys(Keys.BACKSPACE)
        z.send_keys(Keys.DOWN)
        w=self.browser.find_element(By.ID,'id-google-address-b')
        w.send_keys('Vanda')
        w.click()
        time.sleep(1)
        w.send_keys(Keys.BACKSPACE)
        w.send_keys(Keys.DOWN)
        self.browser.find_element(By.TAG_NAME,'h3').click()
        time.sleep(2)
        self.browser.find_element(By.ID,'dir-toggle').find_element(By.LINK_TEXT,'here').click()
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 1200)")