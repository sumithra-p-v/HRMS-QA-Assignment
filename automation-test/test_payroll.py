from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open HRMS application
driver.get("YOUR_APPLICATION_URL")

# Check page loaded
title = driver.title

if title:
    print("Application opened successfully")
else:
    print("Application failed")

driver.quit()