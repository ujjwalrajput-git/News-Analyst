from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import pandas as pd
import os

def scrape_google_news_to_excel(num_pages=5):
    base_url = "https://news.google.com/search?q={}&hl=en-US&gl=US&ceid=US:en"
    search_query = "hdfc+bannk"  # Replace with your desired search query

    headlines_list = []
    sources_list = []
    dates_list = []
#    links_list = []

    for page_num in range(num_pages):
        url = base_url.format(search_query)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            headlines = soup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")
            dates = soup.find_all("time", class_="WW6dff uQIVzc Sksgp slhocf")
            sources = soup.find_all("div", class_="N0NI1d AVN2gc WfKKme")
#           sources_and_dates = soup.find_all("time", class_="WW6dff uQIVzc Sksgp slhocf") #class="WW6dff uQIVzc Sksgp slhocf" <-- SVJrMe
            
            

            for headline, sources, dates in zip(headlines, sources , dates):

            #    try:
            #    date = dates["datetime"]
            #    except AttributeError:
            #        date = "N/A"
                date = dates["datetime"]
                source = sources.a.text
                headline_text = headline.a.text
            #    headline_link = "https://news.google.com" + headline.a["href"]

                parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
                formatted_date = parsed_date.strftime("%H:%M  %d-%b-%y")
                
                headlines_list.append(headline_text)
                sources_list.append(source)
                dates_list.append(formatted_date)
            #    links_list.append(headline_link)

            time.sleep(2)  # Add a delay to avoid overloading the server

    data = {
        "Headline": headlines_list,
        "Source": sources_list,
        "Date": dates_list,
#        "Link": links_list
    }

    df = pd.DataFrame(data)

    save_directory = r"d:\github\News-Analyst"  # Replace with the desired directory path
    excel_filename = os.path.join(save_directory, "google_news_scraped_data.xlsx")

    df.to_excel(excel_filename, index=False)

    print(f"Scraping complete. Data saved to '{excel_filename}'.")

if __name__ == "__main__":
    scrape_google_news_to_excel()
