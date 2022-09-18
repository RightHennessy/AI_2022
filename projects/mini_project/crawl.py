from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

driver = webdriver.Chrome("C:\MachineLearning\AI_2022\projects\mini_project\chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://www.google.co.kr/imghp?hl=ko')

keywords = ['porche panamera', 'porsche cayenne', 'porsche 911']

for keyword in keywords :
    createDirectory('./'+keyword+'_img_download')

    Keyword=driver.find_element(By.CLASS_NAME, 'gLFyf.gsfi')
    Keyword.send_keys(keyword)

    driver.find_element(By.CLASS_NAME,'Tg7LZd').click()

    elem =  driver.find_element(By.TAG_NAME, "body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        
    try:
        driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click()
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass

    links=[]
    images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

    for image in images:
        if image.get_attribute('src')!=None:
            links.append(image.get_attribute('src'))

    print(keyword+' 찾은 이미지 개수:',len(links))
    time.sleep(2)

    for k,i in enumerate(links):
        url = i
        start = time.time()
        urllib.request.urlretrieve(url, "./"+keyword+"/"+keyword+"_"+str(k)+".jpg")
    print(keyword+' ---다운로드 완료---')

driver.close()