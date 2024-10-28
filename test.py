import sys
# 更換
package_path = r".\python-3.11.1\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Edge(executable_path='msedgedriver.exe')

# driver.get('https://www.google.com')

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('msedgedriver.exe')
driver = webdriver.Edge(service=service)
import time

driver.get('https://www.google.com')
time.sleep(1)  # 等待 5 秒
print(driver.title)

# 找到搜尋框
search_box = driver.find_element(By.NAME, 'q')

# 在搜尋框中輸入 "123"
search_box.send_keys('123')

# 提交搜尋
search_box.send_keys(Keys.RETURN)

input("按 Enter 鍵關閉瀏覽器...")
driver.quit()

# dates = ['20240326', '20240327']
# data1 = [155500, 200000]  
# data2 = [55500, 175000]


# x = np.arange(len(dates))


# width = 0.35  


# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, data1, width, label = 'Data 1')
# rects2 = ax.bar(x + width/2, data2, width, label = 'Data 2')


# ax.set_xlabel('Date')
# ax.set_ylabel('Data')
# ax.set_title('Data Comparison')
# ax.set_xticks(x)
# ax.set_xticklabels(dates)
# ax.legend()


# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy = (rect.get_x() + rect.get_width() / 2, height),
#                     xytext = (0, 3),  
#                     textcoords = "offset points",
#                     ha = 'center', va = 'bottom')
        
# autolabel(rects1)
# autolabel(rects2)

# plt.show()
