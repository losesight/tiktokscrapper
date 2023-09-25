from selenium import webdriver
from bs4 import BeautifulSoup
import time


##I'm lazy rn I'll put the rest of the code later 9.25.23



driver = webdriver.Chrome()
driver.get("Insert the link of the tiktok page you'd like")

time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))
for video in videos:
    print(video.a["href"])
