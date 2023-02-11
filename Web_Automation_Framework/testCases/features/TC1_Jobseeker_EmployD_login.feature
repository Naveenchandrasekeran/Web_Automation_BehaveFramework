 Feature:  Jobseeker_Login

  Scenario: Verify Jobseeker_employd_Login
   Given Jobseeker is on home screen
   And Jobseeker  should click  start applying button in header
   When Jobseeker should navigate to login screen
   And Jobseeker should enter email id and password
   And Jobseeker should  find jobseekername in jobseekerhomescreen
 #  Then Browser should quit
