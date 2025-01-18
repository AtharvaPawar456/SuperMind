# pip install selenium
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from typing import Dict, Any

driver_path = "C:/Users/Atharva Pawar/Downloads/Softwares/chromedriver-win64/chromedriver.exe"  # Replace with your driver path

def extractData(html_content: str) -> Dict[str, Any]:
    """
    Extracts the title, text body, and comments from the provided HTML content.
    :param html_content: The full HTML content of the web page.
    :return: A dictionary containing the extracted data.
    """
    extracted_data = {
        "title": "",
        "text_body": "",
        "comments": []
    }
    try:
        # Parse HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Extract <title>
        title_tag = soup.find("title")
        extracted_data["title"] = title_tag.get_text(strip=True) if title_tag else "No title found"
        
        # Extract text-body content
        text_body_div = soup.find("div", attrs={"slot": "text-body"})
        extracted_data["text_body"] = text_body_div.get_text(strip=True) if text_body_div else "No text body found"
        
        # Extract comments
        comment_divs = soup.find_all("div", attrs={"slot": "comment"})
        extracted_data["comments"] = [
            comment.get_text(strip=True) for comment in comment_divs
        ] if comment_divs else ["No comments found"]
        
    except Exception as e:
        print(f"Error | Unable to extract content | {e}")
    
    return extracted_data



def openWebsiteAndScrape(url: str) -> Dict[str, Any]:
    """
    Opens a website using Selenium, scrapes its full HTML content, and extracts data.
    :param url: The URL of the website to scrape.
    :return: Extracted data as a JSON object.
    """
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Open in maximized mode
        chrome_options.add_argument("--disable-infobars") # Disable browser notifications
        chrome_options.add_argument("--disable-extensions") # Disable extensions

        # Set up the WebDriver
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)
        print("Website opened successfully!")

        # Scrape the full HTML content
        page_source = driver.page_source
        page_source = page_source.replace("’", "'")
        extracted_data = extractData(page_source)

        return extracted_data

    except Exception as e:
        print(f"Error | Unable to open website or scrape content | {e}")
        return {}

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    urllist = [
        "https://www.quora.com/What-s-it-like-living-with-trauma"
        
        
    ]

    saveFolder = "reditscrap"
    os.makedirs(saveFolder, exist_ok=True)  # Ensure the folder exists

    for url in urllist:
        jsondata = openWebsiteAndScrape(url)
