from selenium.webdriver.common.by import By

from pageObjects.Base_Actions import BaseActions
from utilities import configReader
from selenium.webdriver.support.select import Select



class BasePage(BaseActions):

   def __init__(self,context):
     super().__init__(context.driver)
  #  def __init__(self, driver):
   #    self.driver = driver

