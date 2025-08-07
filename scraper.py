import requests
from bs4 import BeautifulSoup
import datetime

# The URL of the news website to scrape
URL = "https://www.bbc.com/news"
# The name of the file to save the headlines
OUTPUT_FILE = "headlines.txt"

def scrape_headlines():
    """
    Scrapes headlines from the specified URL and saves them to a text file.
    """
    print("Fetching headlines from BBC News...")
    
    try:
        # Set a User-Agent to mimic a browser and avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        # Send a request to fetch the HTML content of the page
        response = requests.get(URL, headers=headers)
        
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all h3 tags, as BBC often uses them for headlines.
        # This is a common tag for headlines on many news sites.
        # We look for h3 tags with a specific data-testid attribute for better accuracy.
        headline_tags = soup.find_all('h2', {'data-testid': 'card-headline'})
        
        if not headline_tags:
            print("No headlines found with the specified selector. The website structure might have changed.")
            return

        # Extract the text from each headline tag
        headlines = [tag.get_text().strip() for tag in headline_tags]

        # Save the headlines to a text file
        save_to_file(headlines)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_to_file(headlines):
    """
    Saves the list of headlines to a text file.
    """
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write(f"Top Headlines from BBC News\n")
        file.write(f"Scraped on: {timestamp}\n")
        file.write("="*40 + "\n\n")
        
        for i, title in enumerate(headlines, 1):
            file.write(f"{i}. {title}\n")
            
    print(f"✅ Success! {len(headlines)} headlines have been scraped and saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    scrape_headlines()