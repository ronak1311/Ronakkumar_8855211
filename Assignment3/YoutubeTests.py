from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Test Case 1: Open YouTube and search for a video
driver.get("https://www.youtube.com")
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Software Quality Assurance and Test Engineering by Conestoga")
search_box.send_keys(Keys.RETURN)
time.sleep(4)

# Test Case 2: Click on the first video in the search results
first_video = driver.find_element(By.ID, "title-wrapper")
print(first_video)
first_video.click()
time.sleep(5)

# Test Case 3: Pause the video and then play it
play_pause_button = driver.find_element(By.CLASS_NAME, "ytp-play-button")
play_pause_button.click()
time.sleep(3)
play_pause_button.click()
time.sleep(3)

# Go back to the YouTube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Test Case 4: Open the YouTube Shorts page
trending_link = driver.find_element(By.XPATH, "//a[@title='Shorts']")
trending_link.click()
time.sleep(5)
driver.quit()
