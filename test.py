import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

def scrape_google_news_to_excel(num_pages=5):
    base_url = "https://news.google.com/search?q={}&hl=en-US&gl=US&ceid=US:en"
    search_query = "hdfc+bannk"  # Replace with your desired search query

    headlines_list = []
    sources_list = []
    dates_list = []
    links_list = []

    for page_num in range(num_pages):
        url = base_url.format(search_query)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = soup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")
            sources_and_dates = soup.find_all("div", class_="SVJrMe")

            for headline, source_date in zip(headlines, sources_and_dates):
                try:
                    source = source_date.find("div", class_="BNeawe UPmit AP7Wnd").text
                except AttributeError:
                    source = "N/A"

                try:
                    date = source_date.find("time", class_="WW6dff uQIVzc Sksgp").text
                except AttributeError:
                    date = "N/A"

                headline_text = headline.a.text
                headline_link = "https://news.google.com" + headline.a["href"]

                headlines_list.append(headline_text)
                sources_list.append(source)
                dates_list.append(date)
                links_list.append(headline_link)

            time.sleep(2)  # Add a delay to avoid overloading the server

    data = {
        "Headline": headlines_list,
        "Source": sources_list,
        "Date": dates_list,
        "Link": links_list
    }

    df = pd.DataFrame(data)

    save_directory = r"d:\github\News-Analyst"  # Replace with the desired directory path
    excel_filename = os.path.join(save_directory, "google_news_scraped_data.xlsx")

    df.to_excel(excel_filename, index=False)

    print(f"Scraping complete. Data saved to '{excel_filename}'.")

if __name__ == "__main__":
    scrape_google_news_to_excel()
