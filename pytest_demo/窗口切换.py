"""
0）触发新窗口

1、什么情况下需要窗口切换？
   页面的操作，打开了一个新的窗口。你需要在新的窗口当中，去进行下一步的操作。

2、怎么知道要切换到哪个窗口？代码怎么知道哪个窗口是新的窗口？
   1）得到目前打开的所有窗口。---- 句柄。 每一个窗口都有一个句柄。
      列表。 --先后顺序   先出现的，先追加到列表。  最新的窗口，在列表的最后。 最先打开的窗口，在列表第1个。
      wins = driver.window_handles

   2）切换新窗口
      driver.switch_to.window(wins[-1])

   3) 在新的窗口里面，定位元素操作元素。
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")   # WebElement对象 - 1个对象对应1个元素
element.send_keys("selenium webdriver")
driver.find_element_by_id('su').click()  # 带来了内容上的变化


# 条件： '//a[text()=" - SeleniumHQ Browser Automation"]'这个元素要是可见或者存在的
loc = (By.XPATH,'//a[text()=" - SeleniumHQ Browser Automation"]')
# EC.visibility_of_element_located(loc)  # loc元素可见的条件
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_xpath('//a[text()=" - SeleniumHQ Browser Automation"]').click()  # 触发新的窗口出现

time.sleep(1)
# 获取所有的窗口句柄
wins = driver.window_handles
print(wins)
#　获取自己当前所在的窗口句柄
print(driver.current_window_handle)

# 切换到新的窗口，
driver.switch_to.window(wins[-1])
print("切换之后的句柄：",driver.current_window_handle)

# 等待元素可见，并对元素进行点击操作
loc = (By.XPATH,'//div[@class="download-button-container"]//a')
WebDriverWait(driver,15).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


# 退出会话
time.sleep(7)
driver.quit()