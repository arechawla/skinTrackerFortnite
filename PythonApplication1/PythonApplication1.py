from selenium import webdriver

#Opens chrome and goes to website
driver = webdriver.Chrome()   
driver.get("https://skin-tracker.com/fortnite/currentshop") 
#driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#Gets list of all items on the fortnite shop today
itemName = driver.find_elements_by_xpath('//h3')

numItems = len(itemName)

for i in range(numItems):
    print(itemName[i].text)