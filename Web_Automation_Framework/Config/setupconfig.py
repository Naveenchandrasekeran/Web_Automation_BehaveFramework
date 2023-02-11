import os
import time
from Config import baseconfig
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

chromeOptions = Options()
#chromeOptions.add_argument("no-sandbox")
#chromeOptions.add_argument("--disable-extensions")
#chromeOptions.add_argument("--disable-dev-shm-usage")
#chromeOptions.add_argument("--headless")


def  initBrowser(strBrowserName):

  if strBrowserName == "":
     driver = webdriver.Chrome(executable_path="/Users/naveenc/PycharmProjects/Web_Automation/resources/drivers/Chrome_driver/chromedriver",chrome_options=chromeOptions)
  elif strBrowserName == "Chrome":
      driver = webdriver.Chrome(executable_path=baseconfig.CHROME_DRIVER_PATH,chrome_options=chromeOptions)
  elif strBrowserName == "Firefox":
      driver = webdriver.Firefox(baseconfig.FIREFOX_DRIVER_PATH)
  driver.implicitly_wait(100)

  return driver


def navigateToApp(driver, strAppUrl):
    """ To maximize, set timeouts, delete cookies from browser and launch the App Url """
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(strAppUrl)
    time.sleep(5)


def launchApp():

    driver = initBrowser(baseconfig.BROWSER)

    if baseconfig.BROWSER == "":
        navigateToApp(driver, baseconfig.DEV_URL)
    elif baseconfig.BROWSER == "DEV":
        navigateToApp(driver, baseconfig.DEV_URL)
    elif baseconfig.BROWSER == "PROD":
        navigateToApp(driver, baseconfig.PRDO_URL)
    return driver

def save_screenshots_on_failedScenarios(driver, strScenarioName):
    """ Folder for failed scenario screenshots | Save screenshots on failed scenarios """
    if not os.path.exists(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD):
        os.makedirs(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD)
    if not os.path.isfile(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png"):
        driver.save_screenshot(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")
    else:
        os.remove(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")
        driver.save_screenshot(baseconfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")

def close_driver(driver):
     driver.close()