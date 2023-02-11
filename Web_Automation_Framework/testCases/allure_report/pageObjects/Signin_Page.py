from pageObjects.BasePage import BasePage
from pageObjects.Base_Actions import  *
from selenium.webdriver.common.by import By


class Signin_Page(BasePage):

    emailid_field_XPATH = (By.XPATH,"//input[@placeholder='Enter email address']")
    passwordid_field_XPATH = (By.XPATH,"// input[contains( @ placeholder, 'Enter password')]")
    next_button_XPATH =(By.XPATH,"//button[normalize-space()='Next']")
    jobseeker_name_XPATH =(By.XPATH,"//*[@id='root']/div/nav/div/div/div[2]/button/p")

    jobseerker_google_login_email_NAME=(By.NAME, "identifier")
    jobseerker_google_login_password_NAME = (By.NAME, "password")
    jobseerker_google_next_button_XPATH = (By.XPATH,"//*[@id='identifierNext']/div/button/span")
    jobseerker_google_next_button_PASS_CSS =(By.CSS_SELECTOR,"button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b'] span[class='VfPpkd-vQzf8d']")
    jobseerker_facebook_login__email_XPATH=(By.XPATH,"// input[ @ id = 'email']")
    jobseerker_facebook_login__pass_XPATH =(By.XPATH," // input[ @ id = 'pass']")
    jobseerker_facebook_login_button_XPATH =(By.ID,"loginbutton")

    jobseeker_header_XPATH=(By.XPATH,"// *[(text()='Job Seeker' ) or text()='Job Seeker Sign up']")

    jobseeker_explorejob_XPATH =(By.XPATH,"// *[contains(text(), 'Explore Jobs')]")

    def __init__(self, context):
        super().__init__(context)

    def enter_login_credentials(self, email, password):

        self.wait_locate_element_send_keys(self.emailid_field_XPATH, email)
        self.wait_click(self.next_button_XPATH)
        self.wait_in_seconds(5)
        Signin_Header_text = self.wait_get_wbElement_text(self.jobseeker_header_XPATH)
        print(Signin_Header_text)
        if Signin_Header_text == "Job Seeker Sign In":
         self.wait_locate_element_send_keys(self.passwordid_field_XPATH, password)
         self.wait_click(self.next_button_XPATH)
        elif Signin_Header_text == "Job Seeker Sign up":
         self.wait_in_seconds(5)
         print(Signin_Header_text)




    def google_login_credentials(self, google_email, google_password):

        self.switch_tab()
        self.wait_locate_element_send_keys(self.jobseerker_google_login_email_NAME, google_email)
        self.wait_in_seconds(5)
        self.wait_click(self.jobseerker_google_next_button_XPATH)
        self.wait_in_seconds(5)
        self.wait_locate_element_send_keys(self.jobseerker_google_login_password_NAME, google_password)
        self.wait_in_seconds(5)
        self.wait_click(self.jobseerker_google_next_button_PASS_CSS)
        self.wait_in_seconds(10)


    def facebook_login_credentials(self, google_email, google_password):

        self.switch_tab()
        self.wait_locate_element_send_keys(self.jobseerker_facebook_login__email_XPATH, google_email)
        self.wait_in_seconds(2)
        self.wait_locate_element_send_keys(self.jobseerker_facebook_login__pass_XPATH, google_password)
        self.wait_in_seconds(2)
        self.wait_click(self.jobseerker_facebook_login_button_XPATH)
        self.wait_in_seconds(10)


    def jobseeker_name(self):
        try:
          self.wait_in_seconds(2)
          jobseeke_name = self.wait_get_wbElement_text(self.jobseeker_name_XPATH)
          if jobseeke_name == "chiti":
             self.wait_click(self.jobseeker_explorejob_XPATH)
             print("EmployD_email_Jobseeker_Loginsuccessful")
          elif jobseeke_name == "naveenC":
             print("EmployD_google_Loginsuccessful")
             self.wait_click(self.jobseeker_explorejob_XPATH)
          elif jobseeke_name == "Job Seeker":
             print("EmployD_Facebook_Login_is successful")
             self.wait_click(self.jobseeker_explorejob_XPATH)
          else:
            print("Name doesn't match and element is not clickable")
        except AssertionError as e:
            print(e)
