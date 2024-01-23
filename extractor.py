import config
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


WASHER_URL = config.URL

# Set path Selenium
CHROMEDRIVER_PATH = '/home/abhi/chromedriver-linux64/chromedriver' # Change this
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

# Get the response and print title
driver.get(WASHER_URL)
delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'tr')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

table = driver.find_element(By.ID,"statusTable")
rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
for row in rows:
    # Get the columns (all the column 2)        
    col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
    for c in col:
        print(c.text)

driver.close()

