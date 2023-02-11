from behave import *
from Config import baseconfig

@given(u'User is on jobseeker home screen')
def home_screen(context):
    context.HomePage.location_access()


@given(u'User  should click  startapplying button in header')
def  jobseeker_login(context):
    context.HomePage.Jobseeker_signin()


@when(u'User should select facebook login')
def facebook_login(context):
    context.LoginPage.facebook_login()



@when(u'User should enter email id and password in facebook login page')
def facebook_credentials(context):
    context.SigninPage.facebook_login_credentials(baseconfig.FACEBOOK_EMAIL, baseconfig.FACEBOOK_PASSWORD)


@then(u'User should  find jobseekername in jobseekerhomescreen')
def jobseeker_name_check(context):
    context.SigninPage.employ_jobseeker_name
