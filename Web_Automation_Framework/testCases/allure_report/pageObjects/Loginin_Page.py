from pageObjects.BasePage import BasePage
from pageObjects.Base_Actions import  *
from selenium.webdriver.common.by import By

class Login_Page(BasePage):
    jobseeker_continuewithemail_XPATH =(By.XPATH,"// *[contains(text(), 'Continue with Email')]")
    jobseeker_gmail_login_CLASS=(By.CLASS_NAME,"// *[contains(text(), 'Continue With Google')]")
    jobseeker_facebook_login_CLASS=(By.CLASS_NAME,"// *[contains(text(), 'Continue with Facebook')]")


    def __init__(self, context):
        super().__init__(context)

    def continue_with_email_login(self):
        self.wait_in_seconds(5)
        try:
          Email_login=self.wait_get_wbElement_text(self.jobseeker_continuewithemail_XPATH)
          if Email_login == "Continue with Email":
            self.wait_click(self.jobseeker_continuewithemail_XPATH)
        except AssertionError as e:
          print(e)

    def Google_login(self):
        try:
            gmail_login = self.wait_get_wbElement_text(self.jobseeker_gmail_login_CLASS)
            print(gmail_login)
            self.wait_in_seconds(5)
            if gmail_login == "Continue With Google":
                self.wait_click(self.jobseeker_gmail_login_CLASS)
                self.wait_in_seconds(10)
            else:
                print("Google login button test doesn't match")
        except AssertionError as e:
            print(e)



    def facebook_login(self):
        try:
          facebook_login= self.wait_get_wbElement_text(self.jobseeker_facebook_login_CLASS)
          self.wait_in_seconds(5)
          if facebook_login == "Continue With Facebook":
            self.wait_click(self.jobseeker_facebook_login_CLASS)
            print("Button is clicked")
          self.wait_in_seconds(10)
         # else:
               # print("Unable to find facebook  login button")
        except AssertionError as e:
          print(e)








