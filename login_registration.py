# Регистрация аккаунта

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
#
# my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# my_account.click()
# email_adress=driver.find_element_by_id('reg_email')
# email_adress.send_keys('123@mail.ru')
# password=driver.find_element_by_id('reg_password')
# password.send_keys('147258Zzxc!@_147')
# register=driver.find_element_by_xpath('//input[@value="Register"]')
# register.click()
#
# driver.quit()


# логин в систему

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')

my_account=driver.find_element_by_css_selector('#menu-item-50>a')
my_account.click()
username=driver.find_element_by_id('username')
username.send_keys('123@mail.ru')
password=driver.find_element_by_id('password')
password.send_keys('147258Zzxc!@_147')
login=driver.find_element_by_xpath('//input [@value="Login"]')
login.click()
logout=driver.find_element_by_css_selector('div#page-36>div>div>nav>ul>:nth-child(6)>a')
assert logout is not None
driver.quit()


