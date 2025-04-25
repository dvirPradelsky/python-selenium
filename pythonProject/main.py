import time

from Pages import product_page
from Pages.cart import Cart
from Pages.home_page import HomePage
from Pages.product_page import ProductPage
from Pages.store_page import StorePage




product_page.click_add_to_cart_button()
product_page.view_cart_button()

cart = Cart(driver=driver)
cart.verify_product_in_cart('Anchor Bracelet')

# #time.sleep(2)
# product_page_dvir = ProductPageDvir(driver=driver)
# product_page_dvir.first_click_add_to_cart_button()
# time.sleep(4)
# product_page_dvir.click_add_to_cart_button()
# #product_page_dvir.click_add_to_cart_button()
# time.sleep(10)

# search_products_fill = driver.find_element(By.XPATH, '//*[@id="wc-block-search__input-1"]')
# search_products_fill.send_keys('Anchor Bracelet')
# search_products_button = driver.find_element(By.XPATH, '//*[@id="block-7"]//button')
# search_products_button.click()
# time.sleep(4)

# shop_now_button = driver.find_element(By.XPATH, '//*[@id="post-2888"]')
# shop_now_button = driver.find_element(By.XPATH, '//*[@id="post-2888"]/div/div/section[1]/div[2]/div/div/div[
# 4]/div/div/a')

# print(driver.current_url) #Not work ! means we're still in the pop_up
# search_results_page = SearchResultsPage(driver=driver)
#
# search_results_page.filter_price_range(150, 300)
# time.sleep(10)
# search_results_page.verify_prices_range()
# time.sleep(10)
# x = 8

# @tests
# def test_results():
#     return True if x > 5 else False
