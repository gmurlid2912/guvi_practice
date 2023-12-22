import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def reset_pwd():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.implicitly_wait(10)  # provided for the site to load
    driver.get(url)
    frgpwd = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
    frgpwd.click()
    if "requestPasswordResetCode" in driver.current_url:
        print("User is on the reset page")
        username = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
        username.click()
        #getusr = input("Enter the username:")
        getusr = "Admin"
        username.send_keys(getusr)
        print("The username is entered")
        time.sleep(2)
        resetbtn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]')
        resetbtn.click()
        print("Reset button is clicked")
        time.sleep(2)
        if "sendPasswordReset" in driver.current_url:
            print("Resset password link is sent to the mail linked with the username")
        else:
            print("Check the username entered")
            reset_pwd()
    else:
        print("User is not on the reset page")
        reset_pwd()
def login_admin():
    # username = input("Enter the username: ")
    username = "Admin"
    # password = input("Enter the password: ")
    password = "admin123"
    # Open the OrangeHRM site
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.implicitly_wait(10)  # provided for the site to load
    driver.get(url)
    # Entering username
    luser = driver.find_element(By.NAME, 'username')
    luser.click()
    luser.send_keys(username)
    print("Username Entered")
    # Entering password
    lpwd = driver.find_element(By.NAME, 'password')
    lpwd.click()
    lpwd.send_keys(password)
    print("Password Entered")
    # Clicking Login button
    lbutton = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    lbutton.click()
    # Checking if the user has been logged in or not
    if "dashboard" in driver.current_url.lower():
        print("Test Case Login: Passed - Successful login")
        admintab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
        admintab.click()
        user_management()
    else:
        print("Test Case Login: Failed - login unsuccessful")
        login_admin()
def user_management():
    if "admin" in driver.current_url.lower():
        print("user is in the admin tab")
        print("performing validation process in admin page")
        usrmgnt = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
        usrmgnt.click()
        time.sleep(2)
        usrmgntusr = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li')
        usrmgntusr.click()
        driver.implicitly_wait(5)
        print("user option is selected")
        if "viewSystemUsers" in driver.current_url:
            print("user is on the user option page")
            time.sleep(5)
        else:
            print("user is not on the desired page", driver.current_url)
            #user_management()
        job()
    else:
        print("user is not in the admin tab")
        user_management()
def job():
    jobtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
    jobtab.click()
    print("user has selected the job tab")
    time.sleep(5)
    job_titles = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
    job_titles.click()
    print("job titles option is selected")
    driver.implicitly_wait(5)
    if "viewJobTitleList" in driver.current_url:
        print("user is on the job titles page")
        time.sleep(5)
        jobtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        jobtab.click()
        driver.implicitly_wait(5)
        pay_grade = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')
        pay_grade.click()
        driver.implicitly_wait(5)
        if "viewPayGrades" in driver.current_url:
            print("User is on the pay grade page")
            time.sleep(5)
            jobtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
            jobtab.click()
            #driver.implicitly_wait(5)
            emp_status = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')
            emp_status.click()
            driver.implicitly_wait(5)
            if "employmentStatus" in driver.current_url:
                print("User is on the employment status page")
                time.sleep(5)
                jobtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
                jobtab.click()
                job_category = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]')
                job_category.click()
                driver.implicitly_wait(5)
                if "jobCategory" in driver.current_url:
                    print("User is on the job category page")
                    time.sleep(5)
                    jobtab = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
                    jobtab.click()
                    work_shifts = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]')
                    work_shifts.click()
                    driver.implicitly_wait(5)
                    if "workShift" in driver.current_url:
                        print("User is on the work shift page")
                        time.sleep(5)
                    else:
                        print("User is not on the work shift page", driver.current_url)
                    organization()
                else:
                    print("User is not on the job category page", driver.current_url)
            else:
                print("user is not on the employment status page", driver.current_url)
        else:
            print("User is not on the pay grade page", driver.current_url)
    else:
        print("user is not on the job titles page", driver.current_url)
def organization():
    orgtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
    orgtab.click()
    print("User is on the organisation tab")
    time.sleep(5)
    gen_info = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')
    gen_info.click()
    print("General Information option is selected")
    driver.implicitly_wait(5)
    if "viewOrganizationGeneralInformation" in driver.current_url:
        print("User is on the General Information Page")
        time.sleep(5)
        orgtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
        orgtab.click()
        locations = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')
        locations.click()
        driver.implicitly_wait(5)
        if "viewLocations" in driver.current_url:
            print("User is on the Locations page")
            time.sleep(5)
            orgtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
            orgtab.click()
            structure = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')
            structure.click()
            driver.implicitly_wait(5)
            if "viewCompanyStructure" in driver.current_url:
                print("User is on the Structure page")
                time.sleep(5)
            else:
                print("User is not on the Structure page", driver.current_url)
            qualification()
        else:
            print("User is not on the Locations page", driver.current_url)
    else:
        print("User is not on the general information page", driver.current_url)
def qualification():
    qual_tab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
    qual_tab.click()
    print("User is on the qualification tab")
    time.sleep(5)
    skills = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
    skills.click()
    driver.implicitly_wait(5)
    if "viewSkills" in driver.current_url:
        print("User is on the Skills page")
        time.sleep(5)
        qual_tab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
        qual_tab.click()
        education = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')
        education.click()
        driver.implicitly_wait(5)
        if "viewEducation" in driver.current_url:
            print("User is on the Education page")
            time.sleep(5)
            qual_tab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
            qual_tab.click()
            licenses = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]')
            licenses.click()
            driver.implicitly_wait(5)
            if "viewLicenses" in driver.current_url:
                print("User is on the licenses page")
                time.sleep(5)
                qual_tab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
                qual_tab.click()
                languages = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]')
                languages.click()
                driver.implicitly_wait(5)
                if "viewLanguages" in driver.current_url:
                    print("User is on the language page")
                    time.sleep(5)
                    qual_tab = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
                    qual_tab.click()
                    memberships = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]')
                    memberships.click()
                    driver.implicitly_wait(5)
                    if "membership" in driver.current_url:
                        print("User is on the membership page")
                        time.sleep(5)
                    else:
                        print("User is not on the membership page", driver.current_url)
                    nationalitis_cb()
                else:
                    print("User is not on the language page", driver.current_url)
            else:
                print("User is not on the licenses page", driver.current_url)
        else:
            print("User is not on the education page")
    else:
        print("The user is not on the Skills page", driver.current_url)
def nationalitis_cb():
    nationalitis = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
    nationalitis.click()
    print("User has selected the nationalities page")
    driver.implicitly_wait(5)
    if "nationality" in driver.current_url:
        print("User is on the nationality page")
        time.sleep(5)
        corp_brand = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
        corp_brand.click()
        print("User has selected the corporate branding page")
        driver.implicitly_wait(5)
        if "addTheme" in driver.current_url:
            print("User is on the Corporate Branding page")
            time.sleep(5)
        else:
            print("User is not on the Corporate Branding Page")
        configuration()
    else:
        print("User is not on the nationality page", driver.current_url)
def configuration():
    config_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
    config_page.click()
    print("User has selected the configuration page")
    time.sleep(5)
    email_config = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]')
    email_config.click()
    driver.implicitly_wait(5)
    if "listMailConfiguration" in driver.current_url:
        print("User is on the Email Configuration page")
        time.sleep(5)
        config_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
        config_page.click()
        email_subs = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[2]')
        email_subs.click()
        driver.implicitly_wait(5)
        if "viewEmailNotification" in driver.current_url:
            print("User is on the Email Subscription page")
            time.sleep(5)
            config_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
            config_page.click()
            localization = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[3]')
            localization.click()
            driver.implicitly_wait(5)
            if "localization" in driver.current_url:
                print("User is on the localization page")
                time.sleep(5)
                config_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
                config_page.click()
                language_package = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[4]')
                language_package.click()
                driver.implicitly_wait(5)
                if "languagePackage" in driver.current_url:
                    print("User is on the Language Package page")
                    time.sleep(5)
                    config_page = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
                    config_page.click()
                    modules = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[5]')
                    modules.click()
                    driver.implicitly_wait(5)
                    if "viewModules" in driver.current_url:
                        print("User is on the Modules page")
                        time.sleep(5)
                        config_page = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
                        config_page.click()
                        socialmedia = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[6]')
                        socialmedia.click()
                        driver.implicitly_wait(5)
                        if "openIdProvider" in driver.current_url:
                            print("User is on the Social Media Authentication Page")
                            time.sleep(5)
                            config_page = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
                            config_page.click()
                            register_cli = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[7]')
                            register_cli.click()
                            driver.implicitly_wait(5)
                            if "registerOAuthClient" in driver.current_url:
                                print("User is on the Register OAuth Client Page")
                                time.sleep(5)
                                config_page = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
                                config_page.click()
                                ldap = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[8]')
                                ldap.click()
                                driver.implicitly_wait(5)
                                if "ldapConfiguration" in driver.current_url:
                                    print("User is in the LDAP Configuration Page")
                                    time.sleep(5)
                                else:
                                    print("User is not on the LDAP Configuration page", driver.current_url)
                                exit()
                            else:
                                print("User is not on the Register OAuth Client Page", driver.current_url)
                        else:
                            print("User is not in the Social Media Authentication page", driver.current_url)
                    else:
                        print("User is not on the Modules page", driver.current_url)
                else:
                    print("User is not on the Language Package page", driver.current_url)
            else:
                print("User is not on the localization page")
        else:
            print("User is not on the Email Subscription page", driver.current_url)
    else:
        print("User is not on the Email Configuration page", driver.current_url)
def login_menu():
    # username = input("Enter the username: ")
    username = "Admin"
    # password = input("Enter the password: ")
    password = "admin123"
    # Open the OrangeHRM site
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.implicitly_wait(10)  # provided for the site to load
    driver.get(url)
    # Entering username
    luser = driver.find_element(By.NAME, 'username')
    luser.click()
    luser.send_keys(username)
    print("Username Entered")
    # Entering password
    lpwd = driver.find_element(By.NAME, 'password')
    lpwd.click()
    lpwd.send_keys(password)
    print("Password Entered")
    # Clicking Login button
    lbutton = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    lbutton.click()
    # Checking if the user has been logged in or not
    if "dashboard" in driver.current_url.lower():
        print("Test Case Login: Passed - Successful login")
        time.sleep(5)
        admin_tab()
    else:
        print("Test Case Login: Failed - login unsuccessful")
        login_menu()
def admin_tab():
    admintab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
    admintab.click()
    if "viewSystemUsers" in driver.current_url:
        print("User is viewing the admin page")
        time.sleep(5)
        pim_tab()
    else:
        print("User is not viewing the admin page", driver.current_url)
def pim_tab():
    pimtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    pimtab.click()
    if "viewEmployeeList" in driver.current_url:
        print("User is viewing the PIM page")
        time.sleep(5)
        leave_tab()
    else:
        print("User is not viewing the PIM page", driver.current_url)
def leave_tab():
    leavetab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
    leavetab.click()
    if "viewLeaveList" in driver.current_url:
        print("User is viewing the leave page")
        time.sleep(5)
        time_tab()
    else:
        print("User is not viewing the leave page", driver.current_url)
def time_tab():
    timetab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span')
    timetab.click()
    if "viewEmployeeTimesheet" in driver.current_url:
        print("User is viewing the time page")
        time.sleep(5)
        recruitment_tab()
    else:
        print("User is not viewing the time page", driver.current_url)
def recruitment_tab():
    recruitmenttab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
    recruitmenttab.click()
    if "viewCandidates" in driver.current_url:
        print("User is on the Recruitment page")
        time.sleep(5)
        myinfo_tab()
    else:
        print("User is not on the Recruitment page", driver.current_url)
def myinfo_tab():
    myinfotab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')
    myinfotab.click()
    if "viewPersonalDetails" in driver.current_url:
        print("User is on My Info Page")
        time.sleep(5)
        performance_tab()
    else:
        print("User is not on the My Info Page", driver.current_url)
def performance_tab():
    perftab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
    perftab.click()
    if "searchEvaluatePerformanceReview" in driver.current_url:
        print("User is on the Performance Page")
        time.sleep(5)
        dashboard_tab()
    else:
        print("User is not on the Performance Page", driver.current_url)
def dashboard_tab():
    dashboardtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
    dashboardtab.click()
    if "dashboard" in driver.current_url:
        print("User is on the Dashboard Page")
        time.sleep(5)
        directory_tab()
    else:
        print("User is not on the Dashboard Page", driver.current_url)
def directory_tab():
    directorytab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
    directorytab.click()
    if "viewDirectory" in driver.current_url:
        print("User is on the Directory Page")
        time.sleep(5)
        maintanence_tab()
    else:
        print("User is not on the Directory Page", driver.current_url)
def maintanence_tab():
    maintanencetab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
    maintanencetab.click()
    if "purgeEmployee" in driver.current_url:
        print("User is on the Admin Access provider page")
        time.sleep(5)
        admin_pwd = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input')
        admin_pwd.click()
        print("Entering the admin password")
        password = "admin123"
        admin_pwd.send_keys(password)
        time.sleep(2)
        confirm = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/form/div[4]/button[2]')
        confirm.click()
        print("Admin authentication is done")
        time.sleep(5)
        print("User is on the maintenance page")
        time.sleep(5)
        claim_tab()
    else:
        print("User is not on the maintanence page", driver.current_url)
def claim_tab():
    claimtab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span')
    claimtab.click()
    if "viewAssignClaim" in driver.current_url:
        print("User is on the Claim Page")
        time.sleep(5)
        buzz_tab()
    else:
        print("User is not on Claim Page", driver.current_url)
def buzz_tab():
    buzztab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')
    buzztab.click()
    if "viewBuzz" in driver.current_url:
        print("User is on the Buzz Page")
        time.sleep(5)
        exit()
    else:
        print("User is not on the Buzz page", driver.current_url)


print("Choose the operation needed")
print("1. Password Reset Check Scenario")
print("2. Admin Page Options Check Scenario")
print("3. Menu Page Options Check Scenario")
print("4. Quit")
choose = input("Choose from the above option:")

if choose == "1":
    print("Password Reset Check Scenario option is selected")
    driver = webdriver.Chrome()
    driver.maximize_window()
    reset_pwd()
    driver.quit()
    exit()
elif choose == "2":
    print("Admin Page Options Check Scenario is selected")
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_admin()
    driver.quit()
    exit()
elif choose == "3":
    print("Menu Page Options Check Scenario is selected")
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_menu()
    driver.quit()
    exit()
elif choose == "4":
    print("Quit option is selected")
    exit()
