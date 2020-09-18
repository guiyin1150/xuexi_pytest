"""

iframe  html里面的html  妈妈肚子里的宝宝

什么情况下要iframe切换 ？
  你要操作的元素，在iframe当中。

1、识别元素是否在iframe当中。F12

2、切换：1）切换到哪个iframe??
           iframe是标签对，是当前默认html的一个元素。   //iframe[@name="login_frame_qq"]

        driver.switch_to.frame()
        参数支持3种方式来确定切换到哪个一个iframe:
        1) iframe下标  从0开始   driver.switch_to.frame(3)
        2) iframe元素的name属性   driver.switch_to.frame("login_frame_qq")
        3) iframe这个webElment元素。  driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]))

"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# element = driver.find_element_by_id("kw")

# 1) 进入到有iframe的页面
# 操作到有iframe的页面当中。并接下来的步骤，是在iframe中找元素并操作。

# 2）切换
driver.switch_to.frame("login_frame_qq") # 进入了下一代html当中。

# 3) 在iframe当中的html了。

# 4) 回到默认的html页面当中 - 第一代
driver.switch_to.default_content()

# 5) 回到上一级的iframe - 上一代
driver.switch_to.parent_frame()


"""
windows切换
iframe切换

driver.switch_to.window/frame

1、什么情况下切换？
   操作触发了新窗口出现，你要在新的窗口当中，进行下一个操作。
   页面当中有iframe，并且你要进入iframe去进行下一个操作。

2、怎么切换？
   窗口： 1）获取所有的句柄 。window_handles
          2) 切换到新窗口：driver.switch_to.window(....)
          等待新的窗口出现。
          
   iframe:
          1) 定位iframe: 下标/name属性/webElement对象
          2）切换：driver.switch_to.frame(.....)。
             time.sleep(1)
             
          等待iframe可见。

预告： alert切换/鼠标操作/键盘操作/下拉列表操作

"""

