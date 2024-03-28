from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Open the website
url = "https://www.mcdstuff.co.uk/portal.php?site=login&page=mcdonaldsUKLogin"
driver.get(url)

# login button click
button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "sso-login-button"))
)
button.click()
time.sleep(5)

# save language preferences
save_button = driver.find_element(By.ID, "btnSetPopup")
save_button.click()
time.sleep(5)

# enter the franchise manager
div_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='title' and contains(text(), 'Restaurant Managers & Franchisees')]"))
    )
div_element.click()
time.sleep(5)

username_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "UsernameInputTxtManagers"))
)
username_input.click()
username_input.clear()
username_input.send_keys("ee949499")

password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "PasswordInputManagers"))
    )

password_input.click()
password_input.clear()
password_input.send_keys("Cervantes_cag2016")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btnLoginManagers"))
)
login_button.click()
time.sleep(3)

# Wait for the div element to be clickable
div_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".tilemenu_tile[data-menu-item='/portal.php?site=hrAdmin&page=hrAdminEmployees&wrap'] .tilemenu_img"))
)

# Click the div element
div_element.click()
time.sleep(3)

input_element = driver.find_element("id", "filter")
input_element.click()
input_element.send_keys("hi")