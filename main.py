from selenium  import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

#cookie clicker
#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')




# get cookie and click in loop
# game loop
start_time = time.time()
end_time = time.time() + 1*60
curr_time= start_time
while time.time() < end_time:
    cookie= driver.find_element(By.ID, value='cookie')
    cookie.click()
    money= int(driver.find_element(By.ID, value='money').text)
    if time.time()-start_time>5:
        print('entered choice')
        start_time=time.time()
        store= driver.find_elements(by= By.CSS_SELECTOR, value='#store div:not(.grayed)')
        store.reverse()
        ids_of_items= [item.get_attribute('id') for item in store]

        print(len(store))
        for item_id in ids_of_items:
            print(item_id)
            while True:
                try:
                    store_item= driver.find_element(by= By.ID, value=item_id)
                    class_attribute_value = store_item.get_attribute('class')
                    if 'grayed' in class_attribute_value.split():
                        break
                    store_item.click()
                    print('item_bought=', item_id)
                except Exception as e:
                    print(e)
                    break
                
# end game loop
                
#get cookies per second
cookies_per_sec= driver.find_element(by=By.ID, value='cps').text
cookies_per_sec=float(cookies_per_sec.split(sep=': ')[1])
print(cookies_per_sec)


# close the tab 
# driver.close()

# quit the browser
driver.quit()