from selenium import webdriver

driver= webdriver.Chrome()
ProductUrl = "https://www.amazon.com/Apple-iPhone-15-Pro-Max-Silicone-Case-MagSafe/dp/B0CHWRVW9R/ref=sr_1_1_sspa?crid=1LEMAJFQXP0HE&dib=eyJ2IjoiMSJ9.lCnVJJbsNNB7hzrSfkc2RlT-2TorwBSay8GYGyocncubUPJpZnGS7ETAVFgAPnLDEgVr939BOGP16zCVmMs06CLKS1Yh3Jpcq2RUp8zSoDiR2tBPtSmqSCeN4wIH65DVXg6TRyEdqkA3cWpZrcc-07cbvM55euPkZxRrOc5CJlor0qJhgBVkjBKRK0IfM3JdH-Tt6Xsnc_E9lBCS-Uze1ckSwTg0qYtUCgnST05fyuM.mEaorcfij2yo6QP--K5Uh7RkANY7yMeh5gXVpVvekcg&dib_tag=se&keywords=iphone+15+pro+max&qid=1708724066&sprefix=iphone+15+pro+max%2Caps%2C286&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
driver.get(ProductUrl)
Addtocart = driver.find_element("xpath",'/html/body/div[4]/div/div[3]/div[7]/div[8]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[16]/div[1]/span/span/span/input')
Addtocart.click()