from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
driver.save_screenshot("baidu.png")

# 获取指定元素
driver.find_element_by_name("tj_trnews")
driver.find_element_by_name("tj_trnews").text

# 获取网页渲染后的源码
html = driver.page_source
print(html)

from lxml import etree
html_obj = etree.HTML(html)
html_obj.xpath("//a[@name='tj_trnews']/@href")

# 查找a标签，并点击
driver.find_element_by_name("tj_trnews").click()
driver.save_screenshot("baidu2.png")

# 输入文本
driver.find_element_by_id("ww").send_keys("APEC")
driver.save_screenshot("baidu2.png")

# 查找a标签并点击
driver.find_element_by_class_name("btn").click()
driver.save_screenshot("baidu3.png")

driver.find_element_by_xpath("//div[@id='1']//a").click()
driver.save_screenshot("baidu4.png")

# 查案标签页句柄列表
driver.window_handles
# 切换到指定标签页
driver.switch_to_window(driver.window_handles[1])

# 查看当前标签页的url地址
driver.current_url

driver.switch_to_window(driver.window_handles[0])
# 关闭当前标签页
driver.close()


# 关闭浏览器
driver.quit()
