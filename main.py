from time import sleep
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

job_url = "https://www.linkedin.com/jobs/search/?currentJobId=3179371991&f_AL=true&f_E=3&f_WT=2&geoId=106057199&keywords=Python&location=Brasil&refresh=true&sortBy=R"
email = "Your_Email"
password = "Your_Password"
chrome_driver_path = "C:\Development\chromedriver.exe"

def login():
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys(email)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password, Keys.ENTER)

driver = selenium.webdriver.Chrome(chrome_driver_path)
driver.get(job_url)
driver.maximize_window()

login()
pages = driver.find_elements(By.CSS_SELECTOR, "ul li.artdeco-pagination__indicator")
pg_num = 1
on = True
while pg_num <= len(pages):
    jobs = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
    for job in jobs:
        sleep(4)
        job.click()
    pages = driver.find_elements(By.CSS_SELECTOR, "ul li.artdeco-pagination__indicator")
    try:
        pages[pg_num].click()
    except IndexError:
        pass
    pg_num += 1
    save = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
