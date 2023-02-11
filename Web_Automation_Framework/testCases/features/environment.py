
#from configurations.setupconfig import launchApp, save_screenshots_on_failedScenarios
from Config.setupconfig import *
from pageObjects.BasePage import BasePage
from pageObjects.Home_Page import Home_Page
from pageObjects.Jobseeker_Loginin_Page import Login_Page
from pageObjects.Jobseeker_Signin_Page import Signin_Page
from pageObjects.Jobseeker_Signup_Page import Signup_Page


def before_feature(context, feature):
    print("Before feature\n")



def before_scenario(context, scenario):
    print("\nScenario Name: " + scenario.name + "\n")
    context.driver = launchApp()
    context.Base_Page = BasePage(context)
    context.HomePage = Home_Page(context.Base_Page)
    context.LoginPage = Login_Page(context.Base_Page)
    context.SigninPage = Signin_Page(context.Base_Page)
    context.Signup_Page= Signup_Page(context.Base_Page)

 

def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("Scenario: " + scenario.name + " ----------------------------------------------------------FAILED\n")
        save_screenshots_on_failedScenarios(context.driver, scenario.name)
    elif scenario.status == "passed":
        print("Scenario: " + scenario.name + " ----------------------------------------------------------PASSED\n")
    context.driver.quit()

#def after_feature(context, feature):
   # context.BasePage.clear_cookies()
  #  print("Before feature\n")

