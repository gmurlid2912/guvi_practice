from selenium import webdriver
from selenium.webdriver.common.by import By

#username = input("Enter the username: ")
username = "Admin"
#password = input("Enter the password: ")
password = "admin123"
driver = webdriver.Chrome()
driver.maximize_window()
# Open the OrangeHRM site
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.implicitly_wait(10) # provided for the site to load
driver.get(url)
# Entering username
luser = driver.find_element(By.NAME,'username')
luser.click()
luser.send_keys(username)
print("Username Entered")
# Entering password
lpwd = driver.find_element(By.NAME,'password')
lpwd.click()
lpwd.send_keys(password)
print("Password Entered")
# Clicking Login button
lbutton = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
lbutton.click()
#Checking if the user has been logged in or not
if "dashboard" in driver.current_url.lower():
    print("Test Case Login: Passed - Successful login")
else:
    print("Test Case Login: Failed - login unsuccessful")
driver.quit()
