# pip install beautifulsoup4
import os
from bs4 import BeautifulSoup

def extract_content_from_file(file_path):
    extracted_data = {
        "title": "",
        "text_body": "",
        "comments": []
    }
    
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Read the HTML file
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        
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

if __name__ == "__main__":
    # File path
    file_path = "reditscrap/found_inner_peace_but_there_is_nothing_there.html"
    
    # Extract content
    extracted_data = extract_content_from_file(file_path)
    
    # Print extracted data
    print("Title:")
    print(extracted_data["title"])
    print("\nText Body:")
    print(extracted_data["text_body"])
    print("\nComments:")
    for comment in extracted_data["comments"]:
        print(f"- {comment}")
