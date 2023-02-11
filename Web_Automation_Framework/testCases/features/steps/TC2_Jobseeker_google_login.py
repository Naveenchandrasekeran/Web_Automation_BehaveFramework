from behave import *
from Config import baseconfig

@given(u'User is on home screen')
def home_screen(context):
    context.HomePage.location_access()


@given(u'User  should click  start applying button in header')
def jobseeker_login(context):
    context.HomePage.Jobseeker_signin()


@when(u'User should select google login')
def google_login(context):
    context.LoginPage.Google_login()


@when(u'User should enter email id and password in google login page')
def google_credentials(context):
    context.SigninPage.google_login_credentials(baseconfig.GOOGLE_EMAIL, baseconfig.GOOGLE_PASSWORD)


#@then(u'User should  find jobseekername in jobseekerhomescreen')
#def jobseeker_name(context):
   # context.SigninPage.jobseeker_name()
