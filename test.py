from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import pandas as pd
import os

base_url = "https://news.google.com/search?q="
cps = ['HDFC','SBI','ICICI']  # Replace with your desired search query
num_pages=1

headlines_list = []
sources_list = []
dates_list = []
cps_list = []

for cp in cps:
    for page_num in range(num_pages):
    
        url = base_url+cp
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            headlines = soup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")
            dates = soup.find_all("time", class_="WW6dff uQIVzc Sksgp slhocf")
            sources = soup.find_all("div", class_="N0NI1d AVN2gc WfKKme")
            
            for headline, sources, dates in zip(headlines, sources , dates):
                date = dates["datetime"]
                source = sources.a.text
                headline_text = headline.a.text

                parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
                formatted_date = parsed_date.strftime("%H:%M  %d-%b-%y")
                
                headlines_list.append(headline_text)
                sources_list.append(source)
                dates_list.append(formatted_date)
                cps_list.append(cp)

            time.sleep(2)  # Add a delay to avoid overloading the server
        else:
            print("Unable to establish connection ")
            print(response)
            exit()
data = {
    "Company":cps_list,
    "Headline": headlines_list,
    "Source": sources_list,
    "Date": dates_list

}

df = pd.DataFrame(data)

save_directory = r"d:\github\News-Analyst"  # Replacable directory path
excel_filename = os.path.join(save_directory, "google_news_scraped_data.xlsx")

df.to_excel(excel_filename, index=False)

print(f"Scraping complete. Data saved to '{excel_filename}'.")
