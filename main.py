from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv


class VideoFinder():
    def __init__(self, channel_url, search_playlist_title):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.channel_url = channel_url
        self.search_url = "https://www.youtube.com/results?search_query="
        self.search_playlist_title = search_playlist_title

    def start(self):
        item_titles = []
        self.browser.get(f"{self.channel_url}playlists")
        playlist_titles = self.browser.find_elements_by_id("video-title")
        if search_playlist_title != "":
            for playlist_title in playlist_titles:
                if playlist_title.text.lower() == search_playlist_title.lower():
                    playlist_title.click()
                    print(f"Clicked {search_title}")
        else:
            for index, playlist_title in enumerate(playlist_titles):
                print(f"{index}: {playlist_title.text}")
            reply = int(input("Which video you want? "))
            for index, playlist_title in enumerate(playlist_titles):
                if index == reply:
                    playlist_titles[reply].click()
            search_playlist_title = playlist_titles[reply].text
            print(f"Clicked {search_playlist_title}")
        playlist_items = bself.rowser.find_elements_by_id("playlist-items")
        for playlist_item in playlist_items:
            item_title = playlist_item.find_element_by_id(
                "video-title").text.split(" - ")[1]
            item_titles.append(item_title)
            print(f"Found {item_title}")
        file = open("video-links.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        for item_title in item_titles:
            self.browser.get(f"{search_url}{item_title}")
            video_link = self.browser.find_element_by_id(
                "thumbnail").get_attribute("href")
            writer.writerow([item_title, video_link])
            print(f"Writed {item_title}: {video_link}")

        print(f"Finished {search_playlist_title}")

    def finish(self):
        browser.quit()

    def progress(self):
        self.start()
        self.finish()
