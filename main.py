from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import csv


class VideoFinder():
    def __init__(self, channel_url, search_playlist_title="", video_title_split=()):
        self.channel_url = channel_url.rstrip("/") + "/"
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.search_url = "https://www.youtube.com/results?search_query="
        self.search_playlist_title = search_playlist_title
        self.video_title_split = video_title_split

    def start(self):
        item_titles = []
        self.browser.get(f"{self.channel_url}playlists")
        playlist_titles = self.browser.find_elements_by_id("video-title")
        if self.search_playlist_title != "":
            for playlist_title in playlist_titles:
                if playlist_title.text.lower() == self.search_playlist_title.lower():
                    playlist_title.click()
                    print(f"Clicked {self.search_playlist_title}")
        else:
            for index, playlist_title in enumerate(playlist_titles):
                print(f"{index}: {playlist_title.text}")
            reply = int(input("Which video you want? "))
            playlist_titles[reply].click()
            print(f"Clicked playlist")
        playlist_items = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located((By.ID, "playlist-items"))
        )
        for playlist_item in playlist_items:
            item_title = playlist_item.find_element_by_id(
                "video-title").text
            if len(self.video_title_split) != 0:
                index = self.video_title_split[1]
                item_title = item_title.split(self.video_title_split[0])[index]
            item_titles.append(item_title)
            print(f"Found {item_title}")
        file = open("video-links.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        for item_title in item_titles:
            self.browser.get(f"{self.search_url}{item_title}")
            video_link = self.browser.find_element_by_id(
                "thumbnail").get_attribute("href")
            writer.writerow([item_title, video_link])
            print(f"Writed {item_title}: {video_link}")
        print(f"Finished {self.search_playlist_title}!")

    def finish(self):
        self.browser.quit()

    def progress(self):
        self.start()
        self.finish()

#  video_title_split = ()
