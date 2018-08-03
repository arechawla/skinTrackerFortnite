from selenium import webdriver
import smtplib    


emailAddress = "webscraperfortnite@gmail.com"
password = ""

def sendEmail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emailAddress, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(emailAddress, emailAddress, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


#Opens chrome and goes to website
driver = webdriver.Chrome()   
driver.get("https://skin-tracker.com/fortnite/currentshop") 
#driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#Gets list of all items on the fortnite shop today
itemName = driver.find_elements_by_xpath('//h3')

numItems = len(itemName)

desired = "MAVERICK"
subjectGood = "Skin Available"
msgGood = "Congrats! " + desired + " is available today!"

for i in range(numItems):
    if itemName[i].text == desired:
        print("Congrats! " + desired + " is available today!")
        sendEmail(subjectGood, msgGood)

