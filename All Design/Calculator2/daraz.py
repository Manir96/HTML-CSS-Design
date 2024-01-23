
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/Monir/AppData/Local/Programs/Python/Python311/python.exe')
driver.get('https://www.daraz.com.bd/products/lanbena-nail-repair-essence-15ml-i183594329-s1127997617.html')
driver.maximize_window()
height = driver.execute_script('return document.body.scrollHeight')
print(height)
for j in range(0,height-800,30):
    driver.execute_script(f'window.scrollTo(0,{j});')
    time.sleep(0.2)
total_page = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[9]/div[1]/div[1]/div/div/div/div[3]/div[4]/ul/li[8]/a').text
total_page1 = int(total_page)
comment_list = []
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
all_comments =driver.find_elements(By.CLASS_NAME,'review-content-sl')
for k in all_comments:
    print(k.text)
    comment_list.append(k.text)



# for i in range(3):
for i in range(3,15):
    wait = WebDriverWait(driver,30)
    comment_element = wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[9]/div[1]/div[1]/div/div/div/div[3]/div[4]/ul/li[3]/a')))
    j=str(i)
    if(i==7):

        comment_element = wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[9]/div[1]/div[1]/div/div/div/div[3]/div[4]/ul/li['+j+']/a')))
    else:
        comment_element = wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[9]/div[1]/div[1]/div/div/div/div[3]/div[4]/ul/li[7]/a')))
    time.sleep(2)
    driver.execute_script('arguments[0].click();',comment_element)
    # driver.find_element(By.CLASS_NAME, 'ant-pagination-item-link').click()
    all_comments =driver.find_elements(By.CLASS_NAME,'review-content-sl')
    for k in all_comments:
        # print(k.text)
        comment_list.append(k.text)
print(comment_list)
print(len(comment_list))
time.sleep(50)
driver.quit()