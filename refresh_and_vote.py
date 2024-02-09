from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


counter = 0
while True:
            # specify the url
    url = "https://polskifm.com/polonusy/?fbclid=IwAR35hdMFblN6HmLP6Iiw7ihIOj-44t5OQCMjBZtUnYSYSsQd4klBWWHPbR0&mibextid=Zxz2cZ"

        # create an instance of the webdriver
    driver = webdriver.Safari()

        # navigate to the url
    driver.get(url)

        # fullscreen the window
    # driver.maximize_window()


    # locate the cell using its xpath
    xpath = '//input[@name="vote[1601]" and @value="71648"]'
    cell = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # check if the element is located
    if cell:
        print("Cell element located successfully.")
    else:
        print("Unable to locate cell element.")

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", cell)

    # Check if the element is displayed
    if cell.is_displayed():
        print("Cell element is displayed.")
    else:
        driver.execute_script("arguments[0].click();", cell)
        print("Cell element clicked using javascript.")

    vote_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Głosuj'][@class='button']")))
    vote_button.click()
    counter+=1
    time.sleep(3)
    driver.close()
    print (counter)
    time.sleep(1)

    # close the browser
    # driver.quit()

