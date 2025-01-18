# pip install selenium
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from typing import Dict, Any
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from typing import Dict, Any


driver_path = "C:/Users/Atharva Pawar/Downloads/Softwares/chromedriver-win64/chromedriver.exe"  # Replace with your driver path

def collateJsonFiles(folderPath: str, outputFileName: str = "collatedData.json") -> None:
    """
    Combines all JSON files in a specified folder into a single JSON file.
    The key for each entry in the final JSON is the file name without the extension.
    :param folderPath: The path to the folder containing the JSON files.
    :param outputFileName: The name of the output file for the collated JSON data.
    """
    collated_data: Dict[str, Any] = {}

    try:
        # Iterate through all files in the folder
        for file_name in os.listdir(folderPath):
            if file_name.endswith(".json"):  # Process only JSON files
                file_path = os.path.join(folderPath, file_name)
                
                # Read JSON file content
                with open(file_path, "r", encoding="utf-8") as json_file:
                    try:
                        file_content = json.load(json_file)
                        key = os.path.splitext(file_name)[0]  # Use file name without extension as the key
                        collated_data[key] = file_content
                    except json.JSONDecodeError as e:
                        print(f"Error | Unable to parse JSON file {file_name} | {e}")

        # Save collated data to a new JSON file
        output_file_path = os.path.join(folderPath, outputFileName)
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            json.dump(collated_data, output_file, ensure_ascii=False, indent=4)
        print(f"Collated JSON data saved to {output_file_path}")

    except Exception as e:
        print(f"Error | Unable to collate JSON files | {e}")


def extractData(html_content: str) -> list:
    """
    Extracts paragraphs from the given HTML content and returns a list of JSON objects.
    """
    try:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find all divs and check if they have all the required classes
        target_divs = soup.find_all("div", class_=lambda x: x and all(cls in x.split() for cls in [
            "qu-borderAll", "qu-borderColor--raised", "qu-boxShadow--small", "qu-mb--small", "qu-bg--raised"
        ]))
        
        if not target_divs:
            print("No div found with the specified classes.")
            return []

        # Extract data from each div and store it in a list of JSON objects
        json_data = []
        for div in target_divs:
            span_tags = div.find_all("span")
            
            if not span_tags:
                print("No span tags found inside a div with the specified classes.")
            
            paragraphs = []
            for span in span_tags:
                # Extract the text from each span and treat it as a paragraph
                paragraph = span.get_text(strip=True)
                if paragraph:  # Only add non-empty paragraphs
                    paragraphs.append(paragraph)
                    
            # Remove duplicates by converting to set and back to list
            paragraphs = list(set(paragraphs))
            
            # Clean the paragraphs by removing unwanted newline characters, extra spaces,
            # and unwanted patterns like "Upvote", numbers, "·", etc.
            for i, paraitem in enumerate(paragraphs):
                paraitem = paraitem.replace("\n", " ")  # Replace newline with a space
                paraitem = re.sub(r'\s+', ' ', paraitem)  # Replace multiple spaces with a single space
                paraitem = paraitem.strip()  # Strip leading/trailing spaces
                
                # Regex to remove unwanted patterns like "Upvote", numbers, "·", etc.
                paraitem = re.sub(r'\b(Upvote|Downvote|\d{1,4}|\d{1,2}[a-zA-Z]+|·)\b', '', paraitem)
                paraitem = re.sub(r'\b\.\b', '', paraitem)
                paraitem = re.sub(r'\s+', ' ', paraitem)  # Remove extra spaces after regex removal
                paraitem = paraitem.strip()  # Strip again to clean up any leading/trailing spaces
                
                # Remove paragraphs that contain only symbols
                if re.match(r'^[^\w\s]+$', paraitem):  # Regex to match only symbols
                    paragraphs[i] = ''  # Set to empty string for removal later
                
                if len(paraitem) <= 3:
                    paragraphs[i] = ''  # Set to empty string for removal later
                
                paragraphs[i] = paraitem

            # Filter out empty paragraphs and those ending with "?"
            paragraphs = [para for para in paragraphs if para and not para.endswith("?")]
            
            # Only append to json_data if there are paragraphs to include
            if paragraphs:
                json_data.append({
                    "comment": paragraphs  # Use cleaned paragraphs here
                })

        return json_data

    except Exception as e:
        print(f"Error | Unable to process HTML file | {e}")
        return []


def saveHtmlContent(html_content: str, title: str, folder: str) -> None:
    """
    Saves the HTML content to a file named after the page title in the specified folder.
    :param html_content: The HTML content to save.
    :param title: The title of the page (used as the file name).
    :param folder: The folder where the HTML file will be saved.
    """
    try:
        # Ensure the folder exists
        os.makedirs(folder, exist_ok=True)
        
        # Clean the title to be a valid file name (remove invalid characters)
        safe_title = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_" for c in title)
        
        # Set the file path
        file_path = os.path.join(folder, f"{safe_title}.html")
        
        # Write the HTML content to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML content saved to {file_path}")
        
    except Exception as e:
        print(f"Error | Unable to save HTML content | {e}")

def save_json_data(data: list, output_file: str) -> None:
    """
    Saves the extracted data to a JSON file.
    :param data: The JSON data to save.
    :param output_file: The output file path where data will be saved.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data saved to {output_file}")
    except Exception as e:
        print(f"Error | Unable to save data to JSON file | {e}")

def extract_last_item_from_url(url: str) -> str:
    """
    Extracts the last item from the URL when split by "/".
    :param url: The URL to process.
    :return: The last item after splitting by "/".
    """
    # Split the URL by "/" and get the last item
    pagetitle = url.rstrip('/').split('/')[-1]
    pagetitle = pagetitle.replace("-", "_")
    return pagetitle

def openWebsiteAndScrape(url: str, folder: str) -> Dict[str, Any]:
    """
    Opens a website using Selenium, scrapes its full HTML content, scrolls down 6 times, 
    waits for 30 seconds, and then extracts data.
    :param url: The URL of the website to scrape.
    :param folder: The folder to save the HTML file.
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

        # Wait for a specific element to be visible (modify this according to the site)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Upvote']")))

        # Scrape the full HTML content after scrolling
        page_source = driver.page_source
        page_source = page_source.replace("’", "'")  # Fixing apostrophes
        extracted_Json_data = extractData(page_source)
        
        last_item = extract_last_item_from_url(url)
        
        save_json_data(extracted_Json_data, f"{folder}/{last_item}.json")

        # Save the HTML content
        # saveHtmlContent(page_source, last_item, folder)

        return extracted_Json_data

    except Exception as e:
        print(f"Error | Unable to open website or scrape content | {e}")
        return {}

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    urllist = [
        "https://www.quora.com/What-s-it-like-living-with-trauma",
        "https://www.quora.com/What-are-the-signs-of-trauma",
        "https://www.quora.com/What-are-some-ways-to-overcome-past-trauma-and-live-a-normal-life-again-Is-it-even-possible-or-are-some-people-just-not-meant-to-be-happy",
        "https://www.quora.com/How-do-I-start-dealing-with-trauma",
        "https://www.quora.com/What-is-your-childhood-trauma-How-does-it-affect-you",
        "https://www.quora.com/What-are-some-examples-of-a-trauma-response",
        "https://www.quora.com/What-classifies-something-as-trauma",
        "https://www.quora.com/Can-you-share-your-childhood-trauma-and-how-did-you-manage-to-overcome-it",
        "https://www.quora.com/How-do-you-deal-with-unresolved-trauma",
        "https://www.quora.com/How-did-you-learn-to-cope-with-the-biggest-trauma-that-happened-in-your-life",
        "https://www.quora.com/How-do-I-cope-with-trauma-in-a-healthy-way",
        "https://www.quora.com/What-traumatic-experience-have-you-overcome",
        "https://www.quora.com/How-can-I-heal-from-my-childhood-trauma",
        "https://www.quora.com/How-do-people-feel-after-a-trauma?no_redirect=1",
        "https://www.quora.com/How-can-a-trauma-change-a-person",
        "https://www.quora.com/How-can-one-handle-a-trauma-that-impacts-your-life-too-much",
        "https://www.quora.com/How-does-being-traumatized-feel",
        "https://www.quora.com/What-are-the-side-effects-of-emotional-trauma",
        "https://www.quora.com/What-s-it-like-living-with-trauma",
        "https://www.quora.com/What-is-stress-and-how-is-it-caused",
        "https://www.quora.com/What-are-the-best-ways-to-handle-stress-and-stressful-situations",
        "https://www.quora.com/How-can-I-manage-my-stress-and-problems",
        "https://www.quora.com/How-can-we-get-rid-of-stress-in-our-life",
        "https://www.quora.com/What-is-stress-What-causes-stress",
        "https://www.quora.com/What-are-the-best-methods-to-relieve-stress",
        "https://www.quora.com/How-does-stress-affect-you",
        "https://www.quora.com/Is-stress-ever-good-useful-or-necessary",
        "https://www.quora.com/What-should-you-know-about-stress",
        "https://www.quora.com/What-are-some-ways-to-relieve-mental-stress",
        "https://www.quora.com/How-do-I-deal-with-my-feelings-of-extreme-loneliness-and-emptiness",
        "https://quora.com/What-are-your-experiences-of-loneliness",
        "https://www.quora.com/What-should-I-do-to-overcome-the-feeling-of-loneliness",
        "https://www.quora.com/How-lonely-are-you",
        "https://www.quora.com/Is-loneliness-a-common-problem-in-India-among-the-youth-What-is-driving-inside-them-Why-are-people-feeling-more-and-more-lonely-these-days",
        "https://www.quora.com/What-is-loneliness",
        "https://www.quora.com/What-are-the-ways-to-end-loneliness",
        "https://www.quora.com/How-do-you-deal-with-loneliness-Why-is-being-lonely-so-common",
        "https://www.quora.com/How-lonely-are-you-in-your-life-What-is-the-solution",
        "https://www.quora.com/What-do-you-think-about-loneliness",
        "https://www.quora.com/Why-do-people-feel-lonely",
        "https://www.quora.com/What-does-it-feel-like-to-be-lonely",
        "https://www.quora.com/How-do-I-live-in-loneliness",
        "https://www.quora.com/Is-loneliness-good",
        "https://www.quora.com/Why-am-I-always-so-lonely",
        "https://www.quora.com/How-can-one-start-to-enjoy-her-his-loneliness",
        "https://www.quora.com/What-is-loneliness-and-why-does-somebody-suffer-from-it",
        "https://www.quora.com/How-do-I-overcome-work-stress",
        "https://www.quora.com/What-makes-a-job-stressful",
        "https://www.quora.com/What-should-I-do-about-my-stressful-job-I-get-paid-well-and-I-learn-a-lot-but-it-s-the-most-stressful-I-ve-ever-had-and-it-is-affecting-my-health",
        "https://www.quora.com/How-do-you-deal-with-stress-while-looking-for-a-job",
        "https://www.quora.com/If-my-current-job-is-too-stressful-should-I-continue-or-change-jobs",
        "https://www.quora.com/How-can-I-cope-up-with-the-stress-at-work-and-keep-myself-relaxed"




    ]

    print(f"urllist: {len(urllist)}")

    # saveFolder = "quorascrap"  # Folder to save HTML content
    # for url in urllist:
    #     jsondata = openWebsiteAndScrape(url, saveFolder)
    #     # You can also choose to save jsondata to a file, but it's not in the original request
        
    # collateJsonFiles(saveFolder)
