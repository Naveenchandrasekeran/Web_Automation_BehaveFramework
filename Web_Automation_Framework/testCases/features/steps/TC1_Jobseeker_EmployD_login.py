from behave import *

from Config import baseconfig
from Config.setupconfig import close_driver


@given(u'Jobseeker is on home screen')
def launch_home_screen(context):
    context.HomePage.location_access()



@given(u'Jobseeker  should click  start applying button in header')
def jobseeker_login(context):
    context.HomePage.Jobseeker_signin()



@when(u'Jobseeker should navigate to login screen')
def EmployD_login(context):
    context.LoginPage.continue_with_email_login()


@when(u'Jobseeker should enter email id and password')
def enter_credentials(context):
    context.SigninPage.enter_login_credentials(baseconfig.USER_EMAIL, baseconfig.USER_PWD)

@when(u'Jobseeker should  find jobseekername in jobseekerhomescreen')
def successful_login(context):
    context.SigninPage.jobseeker_name()

# @then(u'Browser should quit')
# def closebrowser(context):
#     context.close_browser()



