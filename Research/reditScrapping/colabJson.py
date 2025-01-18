import os
import json
from typing import Dict, Any

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

if __name__ == "__main__":
    folderPath = "reditscrap"
    collateJsonFiles(folderPath)
