
from pageObjects.BasePage import BasePage
from pageObjects.Base_Actions import  *
from selenium.webdriver.common.by import By


class Home_Page(BasePage):
    allow_service_XPATH = (By.XPATH, "//*[contains(text(),'Allow location services')]")
    home_body_CSS =(By.CSS_SELECTOR,"MuiTypography - root.MuiTypography - body1.css - 8po7e2")
    jobseeker_signin_XPATH=(By.XPATH,"//*[contains(text(),'Start Applying')]")
    #jobseeker_signin_XPATH =(By.XPATH,"//p[normalize-space() = 'Job Seeker']")
    employer_signin_XPATH = (By.XPATH,"//p[normalize-space() = 'Employer']")

    def __init__(self, context):
        super().__init__(context)

    def location_access(self):
        try:
            self.wait_in_seconds(2)
            location_Access = self.wait_get_wbElement_text(self.allow_service_XPATH)
            if location_Access == "Allow location services":
                self.wait_click(self.allow_service_XPATH)
            else:
                self.jobseeker(self)
        except AssertionError as e:
            print(e)

    def Jobseeker_signin(self):
      try:
        Jobseeker_value = self.wait_get_wbElement_text(self. jobseeker_signin_XPATH)
        print(Jobseeker_value)
        self.wait_in_seconds(2)
        if Jobseeker_value == "Start Applying":
            self.wait_click(self.jobseeker_signin_XPATH)
      except AssertionError as e:
            print(e)


