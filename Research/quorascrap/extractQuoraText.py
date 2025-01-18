import re
from bs4 import BeautifulSoup
import os
import json

def extract_paragraphs_from_html(html_content):
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
            paragraphsClean = []
            for paraitem in paragraphs:
                # Clean the text to remove \n, excessive spaces, and unwanted patterns using regex
                paraitem = paraitem.replace("\n", " ")  # Replace newline with a space
                paraitem = re.sub(r'\s+', ' ', paraitem)  # Replace multiple spaces with a single space
                paraitem = paraitem.strip()  # Strip leading/trailing spaces
                
                # Regex to remove unwanted patterns like "3", "Upvote", "4y", "·", etc.
                paraitem = re.sub(r'\b(Upvote|Downvote|\d{1,4}|\d{1,2}[a-zA-Z]+|·)\b', '', paraitem)
                paraitem = re.sub(r'\s+', ' ', paraitem)  # Remove extra spaces after regex removal
                paraitem = paraitem.strip()  # Strip again to clean up any leading/trailing spaces
                
                # Remove paragraphs that contain only symbols
                if re.match(r'^[^\w\s]+$', paraitem):  # Regex to match only symbols
                    continue  # Skip this paragraph
                
                if paraitem:  # Only append if the paragraph is not empty
                    paragraphsClean.append(paraitem)

            # Create a new JSON object for each div with cleaned paragraphs
            json_data.append({
                "div_content": paragraphsClean  # Use cleaned paragraphs here
            })

        return json_data

    except Exception as e:
        print(f"Error | Unable to process HTML file | {e}")
        return []

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

# Example usage
file_path = "quorascrap/What_s it like living with trauma_ - Quora.html"
json_data = extract_paragraphs_from_html(file_path)

# Save the JSON data to a file
output_file = "quoraData.json"
save_json_data(json_data, output_file)
