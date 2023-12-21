import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def password():
    login_password = driver.find_element(By.XPATH,
                                             '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    Confirm_password = driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
    login_password_value = login_password.get_attribute("value")
    Confirm_password_value = Confirm_password.get_attribute("value")
    # Checking if the password matches
    if login_password_value == Confirm_password_value:
        print("Passwords matches: Registration successful!")
        time.sleep(5)
        save_date = driver.find_element(By.XPATH,
                                        '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save_date.click()
        print("Employee date has been saved")
    else:
        print("Passwords do not match: Please check the password entered.")
        CPasswordd = input("Re Enter the password: ")
        Confirm_passwordd = driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
        #Confirm_passwordd.click()
        Confirm_passwordd.clear()
        Confirm_passwordd.send_keys(CPasswordd)
        print("Password has been entered for confirmation")
        password()
def employee_id():
    # displaying the emp id
    emp_id = driver.find_element(By.XPATH,
                                 '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    emp_id_value = emp_id.get_attribute("value")
    print(f"The employee id created: {emp_id_value}")

def PIM_Create():
    print(driver.current_url)
    #Selecting PIM option
    pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    pim.click()
    if "pim" in driver.current_url:
        print("PIM option has been selected")
    else:
        print("PIM option has not been selected")
    #Selecting Add EMP option
    add_emp = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
    add_emp.click()
    if "addEmployee" in driver.current_url:
        print("Add Employee option has been selected")
        # Entering the first name
       # firstname = input("Enter the First Name of the employee: ")
        fname = driver.find_element(By.NAME, 'firstName')
        fname.click()
        fname.send_keys(firstname)
        print("Firstname entered")
        """# Entering the middlename
        middlename = input("Enter the Middle Name of the employee: ")
        mname = driver.find_element(By.NAME, 'middleName')
        mname.click()
        mname.send_keys(middlename)
        print("Middlename entered")"""
        # Entering the lastname
        #lastname = input("Enter the Last Name of the employee: ")
        lname = driver.find_element(By.NAME, 'lastName')
        lname.click()
        lname.send_keys(lastname)
        print("Lastname entered")
        employee_id()
        """# Creating login detail
        deatail_button = driver.find_element(By.XPATH,
                                             '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
        deatail_button.click()
        print("Hover button clicked")
        # Login username value entered
        Username = input("Enter the Username of the employee: ")
        login_username = driver.find_element(By.XPATH,
                                             '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
        login_username.click()
        login_username.send_keys(Username)
        print("Username has been entered")
        # Login password value entered
        Password = input("Enter the Password of the employee: ")
        login_password = driver.find_element(By.XPATH,
                                             '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
        login_password.click()
        login_password.send_keys(Password)
        print("Password has been entered")
        # confirm password value entered
        CPassword = input("Re Enter the password: ")
        Confirm_password = driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
        Confirm_password.click()
        Confirm_password.send_keys(CPassword)
        print("Password has been entered for confirmation")
        password()"""
        emp_id = driver.find_element(By.XPATH,
                                     '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        emp_id_value = emp_id.get_attribute("value")
        print(f"The employee id created: {emp_id_value}")
        save_date = driver.find_element(By.XPATH,
                                        '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save_date.click()
        print("Employee date has been saved")
        return emp_id_value
    else:
        print("Add Employee option has not been selected")
        PIM_Create()

def initial_login():
    #username = input("Enter the username: ")
    username = "Admin"
    #password_login = input("Enter the password: ")
    password_login = "admin123"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.implicitly_wait(10)  # provided for the site to load
    driver.get(url)
    print(driver.current_url)
    # Entering username
    luser = driver.find_element(By.NAME, 'username')
    luser.click()
    luser.send_keys(username)
    print("Username Entered")
    # Entering password
    lpwd = driver.find_element(By.XPATH,
                               '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    lpwd.click()
    lpwd.send_keys(password_login)
    print("Password Entered")
    # Clicking Login button
    lbutton = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    lbutton.click()
    # Checking if the user has been logged in or not
    if "dashboard" in driver.current_url.lower():
        print("Test Case Login: Passed - Successful login")
        PIM_Create()
    else:
        print("Test Case Login: Failed - login unsuccessful")
        initial_login()

def emp_edit():
    emp_list = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
    emp_list.click()
    print(driver.current_url)
    if "viewEmployeeList" in driver.current_url:
        print("User is on the Employee List Page")
        emp_name_holder = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name_holder.click()
        emp_name_holder.send_keys(firstname +" " + lastname)
        print("The employee name has been added")
        #driver.implicitly_wait(5)
        time.sleep(5)
        search_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search_button.click()
        print("Search result is displayed")
        driver.implicitly_wait(10)
        #time.sleep(5)
        emp_user_edit()
    else:
        print("User is not on the Employee List page")

def emp_user_edit():
    edit_user = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')
    edit_user.click()
    driver.implicitly_wait(5)
    job_details = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]')
    job_details.click()
    print("Job details option is selected")
    #driver.implicitly_wait(5)
    time.sleep(10)
    job_title = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
    job_title.click()
    print("job title option is clicked")
    time.sleep(2)
    job_title.send_keys(Keys.ARROW_DOWN)
    print("Job title as Account Manager is selected")
    #job_title.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    job_title.send_keys(Keys.RETURN)
    time.sleep(5)
    save_edit = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button')
    save_edit.click()
    print("edits are saved")
    time.sleep(5)
    emp_list = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
    emp_list.click()
    print(driver.current_url)
    if "viewEmployeeList" in driver.current_url:
        print("User is on the Employee List Page")
        emp_name_holder = driver.find_element(By.XPATH,
                                              '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name_holder.click()
        emp_name_holder.send_keys(firstname + " " + lastname)
        print("The employee name has been added")
        # driver.implicitly_wait(5)
        time.sleep(5)
        search_button = driver.find_element(By.XPATH,
                                            '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search_button.click()
        print("Search result is displayed")
        print("Edits are now updated")


def emp_del():
    emp_list = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
    emp_list.click()
    print(driver.current_url)
    if "viewEmployeeList" in driver.current_url:
        print("User is on the Employee List Page")
        emp_name_holder = driver.find_element(By.XPATH,
                                              '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name_holder.click()
        emp_name_holder.send_keys(firstname + " " + lastname)
        print("The employee name has been added")
        # driver.implicitly_wait(5)
        time.sleep(5)
        search_button = driver.find_element(By.XPATH,
                                            '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search_button.click()
        print("Search result is displayed")
        driver.implicitly_wait(10)
        # time.sleep(5)
        delete()
    else:
        print("User is not on the Employee List page")
def delete():
    del_user = driver.find_element(By.XPATH,
                                   '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]')
    del_user.click()
    driver.implicitly_wait(5)
    del_pop_yes = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]')
    del_pop_yes.click()
    print("User is deleted")
    time.sleep(5)
    driver.refresh()

print("Choose the operation needed")
print("1. Create an user")
print("2. Create & Edit an user data")
print("3. Create & Delete an user data")
print("4. Quit")
options = input("Choose from the above options:")

if options == "1":
    print("Create an user option is selected")
    firstname = input("Enter the First Name of the employee: ")
    lastname = input("Enter the Last Name of the employee: ")
    driver = webdriver.Chrome()
    driver.maximize_window()
    initial_login()
    exit()
elif options == "2":
    print("Create & Edit an user option is selected")
    firstname = input("Enter the First Name of the employee: ")
    lastname = input("Enter the Last Name of the employee: ")
    driver = webdriver.Chrome()
    driver.maximize_window()
    initial_login()
    emp_edit()
    exit()
elif options == "3":
    print("Create & Delete an user option is selected")
    firstname = input("Enter the First Name of the employee: ")
    lastname = input("Enter the Last Name of the employee: ")
    driver = webdriver.Chrome()
    driver.maximize_window()
    initial_login()
    emp_del()
    exit()
elif options == "4":
    exit()
