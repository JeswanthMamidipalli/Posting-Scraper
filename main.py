# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from tabulate import tabulate

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigating towards our link
driver.get(url="https://hprera.nic.in/PublicDashboard")
time.sleep(10)

data = []


for i in range(5):
    # We are using the "next_button" to navigate from one posting to another

    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[{i + 1}]/div/div/a")))
    # next_button.click()
    driver.execute_script("arguments[0].click();", next_button)

    time.sleep(10)

    gstNo = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[13]/td[2]/span').text

    panNo = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/span').text

    name = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text

    permAdress = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[12]/td[2]/span').text

    data.append([gstNo, panNo, name, permAdress])

    cross_button = driver.find_element(By.XPATH, "//*[@id='modal-data-display-tab_project_main']/div/div/div[1]/button/span")
    cross_button.click()

driver.quit()

# The recorded data is well represented in the tabular form
headers = [" GSTIN No", "PAN No", "Name", "Permanent Address"]
table = tabulate(data, headers=headers, tablefmt="fancy_grid")
print(table)

