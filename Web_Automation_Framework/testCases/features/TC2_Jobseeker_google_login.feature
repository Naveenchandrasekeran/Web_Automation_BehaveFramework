 Feature:  Jobseeker_google_Login

   @t2
  Scenario: Verify Jobseeker google  Login
    Given User is on home screen
    And User  should click  start applying button in header
    When User should select google login
    And User should enter email id and password in google login page
    Then User should  find jobseekername in jobseekerhomescreen