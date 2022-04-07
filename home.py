
# Добавление комментария
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')

driver.execute_script("window.scrollBy(0,600);")
selenium_ruby=driver.find_element_by_xpath('//a [@data-product_id="160"]')
selenium_ruby.click()
reviews=driver.find_element_by_css_selector('li.reviews_tab>a')
reviews.click()
star=driver.find_element_by_css_selector('.stars>span>:nth-child(5)')
star.click()
your_review=driver.find_element_by_id('comment')
your_review.send_keys('Nice book!')
name=driver.find_element_by_id('author')
name.send_keys('Maria')
email=driver.find_element_by_id('email')
email.send_keys('123@mail.ru')

driver.quit()