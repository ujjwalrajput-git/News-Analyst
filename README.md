# News Analyst

## Overview
News Analyst is a Python-based project designed to scrape news articles from Google News, analyze their sentiment using the VADER Sentiment Analysis tool, and store the results in an Excel file for further insights. This tool helps users monitor public sentiment for specific topics in real time.

## Features
- **Web Scraping:** Automatically collects news articles and metadata (headlines, sources, dates) from Google News.
- **Sentiment Analysis:** Assigns sentiment scores (negative, neutral, positive, compound) to each headline using the VADER Sentiment Analyzer.
- **Data Storage:** Exports the analyzed data to an Excel file for easy access and sharing.
- **Insights:** Calculates average sentiment scores for a quick overview of public opinion.

## Tech Stack
- **Languages:** Python
- **Libraries:**
  - BeautifulSoup: For web scraping
  - Requests: For sending HTTP requests
  - Pandas: For data manipulation and storage
  - NLTK: For sentiment analysis (VADER)
  - Tkinter (optional): For GUI integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/news-analyst.git
   cd news-analyst
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the NLTK VADER lexicon:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage

### Step 1: Web Scraping
1. Update the `cps` list in the script with your desired search queries (e.g., `['HDFC']`).
2. Set the number of pages to scrape with the `num_pages` variable.
3. Run the script to collect news articles:
   ```bash
   python news_scraper.py
   ```
4. The scraped data will be stored in an Excel file named `google_news_scraped_data.xlsx` in the specified directory.

### Step 2: Sentiment Analysis
1. The script will process the headlines using VADER Sentiment Analyzer.
2. Sentiment scores (negative, neutral, positive, compound) will be added to the DataFrame.
3. The results, including average sentiment scores, will be printed to the console.

## Example Output
- **Sample DataFrame (after analysis):**
  | Company | Headline                                      | Source           | Date      | neg   | neu   | pos   | compound |
  |---------|----------------------------------------------|------------------|-----------|-------|-------|-------|----------|
  | HDFC    | Markets log 4th day of rally on buying...    | Times of India   | 06-09-23  | 0.0   | 1.0   | 0.0   | 0.0000   |
  | HDFC    | HDFC Bank, ICICI Bank, Bank of Baroda...     | CNBCTV18         | 07-09-23  | 0.0   | 0.864 | 0.136 | 0.2960   |

- **Average Sentiment Scores:**
  - Average `neg`: 0.0274
  - Average `neu`: 0.8639
  - Average `pos`: 0.1085
  - Average `compound`: 0.1699

## Challenges
1. **Dynamic Website Structure:** Ensuring compatibility with changing Google News HTML layouts.
2. **Sentiment Accuracy:** Analyzing multilingual headlines effectively.
3. **Scraping Efficiency:** Avoiding server bans by introducing time delays and handling errors.

## Future Improvements
- Add support for more advanced sentiment analysis tools.
- Integrate a graphical user interface (GUI) for easier operation.
- Expand support to scrape and analyze news from additional sources.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any queries or suggestions, feel free to contact:
- **Ujjwal Rajput**
- Email: [ujjwalrajputofficial.in@gmail.com](mailto:ujjwalrajputofficial.in@gmail.com)
