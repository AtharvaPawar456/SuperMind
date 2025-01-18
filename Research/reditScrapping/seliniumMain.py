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

def displayJsonData(jsondata: Dict[str, Any]) -> None:
    """
    Displays the extracted JSON data in the console.
    :param jsondata: The JSON data to display.
    """
    print("Title:")
    print(jsondata["title"])
    print("\nText Body:")
    print(jsondata["text_body"])
    print("\nComments:")
    for comment in jsondata["comments"]:
        print(f"- {comment}")

def saveJsonToFile(jsonData: Dict[str, Any], filePath: str) -> None:
    """
    Saves the JSON data to a specified file.
    :param jsonData: The data to save.
    :param filePath: Path of the file where JSON data will be saved.
    """
    try:
        with open(filePath, "w", encoding="utf-8") as file:
            json.dump(jsonData, file, ensure_ascii=False, indent=4)
        print(f"JSON data saved to {filePath}")
    except Exception as e:
        print(f"Error | Unable to save JSON to file | {e}")

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
        # "https://www.reddit.com/r/Mindfulness/comments/13ne26l/found_inner_peace_but_there_is_nothing_there/",
        # "https://www.reddit.com/r/infj/comments/10r9hbq/what_brings_you_peace_in_life/",
        # "https://www.reddit.com/r/Meditation/comments/1b6naam/what_is_your_trick_for_maintaining_inner_peace_in/",
        # "https://www.reddit.com/r/simpleliving/comments/x2f4wp/how_do_i_achieve_peace_i_want_nothing_more_that_a/",
        # "https://www.reddit.com/r/Journaling/comments/1ea8bap/what_brings_you_the_most_mental_peace/",
        # "https://www.reddit.com/r/Mindfulness/comments/1aezi5d/how_to_find_true_inner_peace/",
        # "https://www.reddit.com/r/socialskills/comments/fgkd5v/overthinkers_how_do_you_find_your_peace_of_mind/",
        # "https://www.reddit.com/r/productivity/comments/zx81t0/what_is_the_key_to_having_lasting_inner_peace/",
        # "https://www.reddit.com/r/simpleliving/comments/10lrwqm/how_do_i_be_at_peace_while_doing_nothing/"
        
        # "https://www.reddit.com/r/simpleliving/comments/1cz72jc/finding_joy_in_simple_living_what_brings_you_peace/",
        # "https://www.reddit.com/r/AskOldPeople/comments/1e9bp6g/whats_the_secret_to_living_a_peaceful_satisfied/",
        # "https://www.reddit.com/r/RandomThoughts/comments/198g6u0/whats_the_definition_of_peace_for_you/",
        # "https://www.reddit.com/r/SeriousConversation/comments/1cgdc4z/is_world_peace_actually_possible/",
        # "https://www.reddit.com/r/DeepThoughts/comments/143558m/is_being_at_peace_more_important_than_happiness/"
        
        "https://www.reddit.com/r/delhi/comments/1cpny5m/whats_your_trauma_and_how_does_it_impact_your_day/",
        "https://www.reddit.com/r/traumatoolbox/",
        "https://www.reddit.com/r/AskReddit/comments/16cc78f/what_immediately_tells_you_that_a_person_has_had/",
        "https://www.reddit.com/r/CPTSD_NSCommunity/comments/1cjk381/has_anyone_managed_to_actually_turn_their_life/",
        "https://www.reddit.com/r/Mindfulness/comments/1b2r3fp/how_does_one_actually_start_to_heal_and_move/",
        "https://www.reddit.com/r/malementalhealth/comments/n66moe/what_is_considered_trauma/",
        "https://www.reddit.com/r/CPTSD/comments/1bfcr13/coping_with_the_fact_that_you_caused_significant/",
        "https://www.reddit.com/r/CPTSD/comments/1f752ns/the_real_trauma_starts_the_moment_you_realize_you/",
        "https://www.reddit.com/r/CPTSD/comments/14xx5ie/how_does_your_trauma_affect_you_physically/",
        "https://www.reddit.com/r/Stress/",
        "https://www.reddit.com/r/lifehacks/comments/13za4de/are_there_any_life_hacks_for_when_u_r_extremely/",
        "https://www.reddit.com/r/college/comments/ykpx0o/how_do_you_guys_handle_the_stress_of_college/",
        "https://www.reddit.com/r/GetMotivated/comments/19ex4hi/need_your_help_what_actually_works_for_you_to/",
        "https://www.reddit.com/r/AskReddit/comments/6tmu7h/serious_redditors_what_healthy_ways_do_you_deal/",
        "https://www.reddit.com/r/GetMotivated/comments/1ecis0z/discussion_adults_how_do_you_deal_with_continous/",
        "https://www.reddit.com/r/developersIndia/comments/tdr9bn/how_do_you_handle_stress/",
        "https://www.reddit.com/r/selfimprovement/comments/to9iik/i_feel_like_i_cant_handle_stress_like_a_normal/",
        "https://www.reddit.com/r/lonely/",
        "https://www.reddit.com/r/loneliness/",
        "https://www.reddit.com/r/india/comments/14u04ar/loneliness_the_only_constant_in_my_life/",
        "https://www.reddit.com/r/Adulting/comments/1bh30a7/how_do_single_adults_cope_with_loneliness/",
        "https://www.reddit.com/r/bangalore/comments/10en66x/if_you_struggle_with_loneliness_focus_on_two/",
        "https://www.reddit.com/r/AskReddit/comments/a7sqwl/lonely_people_of_reddit_how_do_you_handle_the/",
        "https://www.reddit.com/r/selfimprovement/comments/11pzfmu/i_feel_like_im_dying_of_loneliness/",
        "https://www.reddit.com/r/bangalore/comments/1csqcbi/practical_tips_to_manage_loneliness_in_the_city/",
        "https://www.reddit.com/r/simpleliving/comments/ub2ue8/how_do_you_guys_deal_with_loneliness/",
        "https://www.reddit.com/r/lonely/comments/1d53v8c/how_do_you_cope_with_chronic_loneliness/"
        
        
    ]

    saveFolder = "reditscrap"
    os.makedirs(saveFolder, exist_ok=True)  # Ensure the folder exists

    for url in urllist:
        jsondata = openWebsiteAndScrape(url)
        if jsondata:
            # displayJsonData(jsondata)
            
            # Save JSON to file
            urlIdentifier = url.split("/")[-2]  # Extract unique identifier from URL
            filePath = os.path.join(saveFolder, f"{urlIdentifier}.json")
            saveJsonToFile(jsondata, filePath)
