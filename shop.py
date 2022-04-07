 # Отображение товара

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
#
# my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# my_account.click()
# username=driver.find_element_by_id('username')
# username.send_keys('123@mail.ru')
# password=driver.find_element_by_id('password')
# password.send_keys('147258Zzxc!@_147')
# login=driver.find_element_by_xpath('//input [@value="Login"]')
# login.click()
#
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
# book=driver.find_element_by_css_selector('.post-181>a>img')
# book.click()
# book_name=driver.find_element_by_xpath('//h1')
# book_name_text=book_name.text
# assert book_name_text == 'HTML5 Forms'
# driver.quit()

# Колличество товаров в категории


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
#
# my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# my_account.click()
# username=driver.find_element_by_id('username')
# username.send_keys('123@mail.ru')
# password=driver.find_element_by_id('password')
# password.send_keys('147258Zzxc!@_147')
# login=driver.find_element_by_xpath('//input [@value="Login"]')
# login.click()
#
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
# html=driver.find_element_by_css_selector('.product-categories>:nth-child(2)>a')
# html.click()
# html_3=driver.find_elements_by_css_selector('.products>li')
# assert len(html_3) == 3
# driver.quit()


### сортировка товара

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('http://practice.automationtesting.in/')
# my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# my_account.click()
# username=driver.find_element_by_id('username')
# username.send_keys('123@mail.ru')
# password=driver.find_element_by_id('password')
# password.send_keys('147258Zzxc!@_147')
# login=driver.find_element_by_xpath('//input [@value="Login"]')
# login.click()
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
#
# select_value=driver.find_element_by_xpath('//select [@name="orderby"]')
# default_sorting_get_value=select_value.get_attribute('value')
# assert default_sorting_get_value == 'menu_order'
# from selenium.webdriver.support.select import Select
# select_value=driver.find_element_by_xpath('//select [@name="orderby"]')
# select=Select(select_value)
# select.select_by_value('price-desc')
# select_value=driver.find_element_by_xpath('//select [@name="orderby"]')
# sort_by_price_value=select_value.get_attribute('value')
# assert sort_by_price_value == 'price-desc'
# driver.quit()


######   отображение скидки товара

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get('http://practice.automationtesting.in/')
# my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# my_account.click()
# username=driver.find_element_by_id('username')
# username.send_keys('123@mail.ru')
# password=driver.find_element_by_id('password')
# password.send_keys('147258Zzxc!@_147')
# login=driver.find_element_by_xpath('//input [@value="Login"]')
# login.click()
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
#
# android=driver.find_element_by_css_selector('.post-169>:nth-child(1)')
# android.click()
# old_price=driver.find_element_by_css_selector('.price>del>span')
# old_price_text=old_price.text
# assert old_price_text == '₹600.00'
# new_price=driver.find_element_by_css_selector('.price>ins>span')
# new_price_text=new_price.text
# assert new_price_text == '₹450.00'
#
# img=WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR,'.images>a>img')))
# img.click()
# close=WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# close.click()
# driver.quit()




#### Проверка цены в корзине

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(20)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get('http://practice.automationtesting.in/')
# # my_account=driver.find_element_by_css_selector('#menu-item-50>a')
# # my_account.click()
# # username=driver.find_element_by_id('username')
# # username.send_keys('123@mail.ru')
# # password=driver.find_element_by_id('password')
# # password.send_keys('147258Zzxc!@_147')
# # login=driver.find_element_by_xpath('//input [@value="Login"]')
# # login.click()
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
# html5=driver.find_element_by_css_selector('.post-182>:nth-child(2)')
# html5.click()
# ######## basket=WebDriverWait(driver, 10).until(
# # ######    EC.text_to_be_present_in_element_value((By.CLASS_NAME, 'cartcontents'),'1 item'))
# # basket_1=driver.find_element_by_class_name('cartcontents')
# # basket_text=basket_1.text
# # assert basket_text == 1
# # price=driver.find_element_by_css_selector('li>a>span.amount')
# # price_get_text=price.text
# # assert price_get_text == '₹180.00'
#
# basket=driver.find_element_by_css_selector('#wpmenucartli>a')
# basket.click()
# subtotal=WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart_totals >table>tbody>tr>td>span'), '180.00'))
# total=WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.order-total>td>strong>span'), '189.00'))
# driver.quit()


###########################     работа в корзине
# import time
#
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get('http://practice.automationtesting.in/')
# shop=driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script('window.scrollBy(0,800);')
# html5=driver.find_element_by_css_selector('.post-182>:nth-child(2)')
# html5.click()
# time.sleep(40)
# js_data=driver.find_element_by_css_selector('.post-180>:nth-child(2)')
# js_data.click()
# time.sleep(5)
# basket=driver.find_element_by_css_selector('#wpmenucartli>a')
# basket.click()
# time.sleep(5)
# delete=driver.find_element_by_xpath('//a[@data-product_id="182"]')
# delete.click()
# undo=driver.find_element_by_css_selector('#page-34>div>div>div>a')
# undo.click()
# quantity=driver.find_element_by_xpath('//input[@name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantity.clear()
# quantity.send_keys('3')
# update_basket=driver.find_element_by_css_selector('.actions>:nth-child(2)')
# update_basket.click()
# quantity_attribute=quantity.get_attribute ('value')
# assert quantity_attribute == '3'
# time.sleep(10)
# apply_coupon=driver.find_element_by_css_selector('.coupon>:nth-child(3)')
# apply_coupon.click()
# message=driver.find_element_by_class_name('woocommerce-error')
# message_text=message.text
# assert 'Please' in message_text
# driver.quit()


######### покупка товара #####
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get('http://practice.automationtesting.in/')
shop=driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script('window.scrollBy(0,300);')
html5=driver.find_element_by_css_selector('.post-182>:nth-child(2)')
html5.click()
time.sleep(20)
basket=driver.find_element_by_css_selector('#wpmenucartli>a')
basket.click()

proceed_to_checkout=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a')))
proceed_to_checkout.click()

first_name=driver.find_element_by_id('billing_first_name')
first_name.send_keys('Maria')
last_name=driver.find_element_by_id('billing_last_name')
last_name.send_keys('Maria')
email=driver.find_element_by_id('billing_email')
email.send_keys('123@mail.ru')
phone=driver.find_element_by_id('billing_phone')
phone.send_keys('88003213232')
address=driver.find_element_by_xpath('//input[@name="billing_address_1"]')
address.send_keys('street')
address_2=driver.find_element_by_xpath('//input[@name="billing_address_2"]')
address_2.send_keys('apartment')
city=driver.find_element_by_xpath('//input[@name="billing_city"]')
city.send_keys('city')
county=driver.find_element_by_xpath('//input[@name="billing_state"]')
county.send_keys('county')
postcode=driver.find_element_by_xpath('//input[@name="billing_postcode"]')
postcode.send_keys('111111')
driver.execute_script('window.scrollBy(0,600);')
time.sleep(30)
check_payments=driver.find_element_by_id('payment_method_cheque')
check_payments.click()
place_order=driver.find_element_by_css_selector('.button.alt')
place_order.click()
thank_you=WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '.page-content>div>:nth-child(1)'),
                                           'Thank you. Your order has been received.'))
payment_method=WebDriverWait(driver,20).until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#page-35>div>div>ul>:nth-child(4)>strong'),
                                           'Check Payments'))
driver.quit()

