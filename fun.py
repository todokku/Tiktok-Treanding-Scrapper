from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from time import sleep

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]
UAR = UserAgent(software_names=software_names, operating_systems=operating_systems,limit=100)

user_agent = UAR.get_random_user_agent()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('user-data-dir=C:\\Users\\Logan\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tiktok.com/trending/?lang=en")