 Feature:  Jobseeker_facebook_Login

   @t3
  Scenario: Verify Jobseeker facebook  Login
    Given User is on jobseeker home screen
    And User  should click  startapplying button in header
    When User should select facebook login
    And User should enter email id and password in facebook login page
    Then User should  find jobseekername in jobseekerhomescreen


