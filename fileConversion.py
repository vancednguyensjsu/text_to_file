import os
import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path


# Function to find the file in a specified directory
def find_file(file_name, search_directory):
    search_path = Path(search_directory)
    for path in search_path.rglob(file_name):  # rglob searches recursively
        return path
    return None


# Conversion Functions
def text_to_xml(lines, xml_file, root_tag="root", element_tag="item"):
    root = ET.Element(root_tag)
    for line in lines:
        line = line.strip()
        element = ET.SubElement(root, element_tag)
        element.text = line
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    print(f"File converted to XML and saved as {xml_file}")


def text_to_csv(lines, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Line"])  # Header
        for line in lines:
            writer.writerow([line.strip()])
    print(f"File converted to CSV and saved as {csv_file}")


def text_to_json(lines, json_file):
    data = [line.strip() for line in lines]
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"File converted to JSON and saved as {json_file}")


# Function to convert file based on user choice
def convert_file(format_choice, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if format_choice == 'xml':
        xml_file = 'output.xml'
        text_to_xml(lines, xml_file)
    elif format_choice == 'csv':
        csv_file = 'output.csv'
        text_to_csv(lines, csv_file)
    elif format_choice == 'json':
        json_file = 'output.json'
        text_to_json(lines, json_file)
    else:
        print("Invalid format selected.")


if __name__ == "__main__":
    # Set the file name to find
    file_name = 'testing.txt'

    # Ask user to specify the directory to search in
    search_directory = input("Enter the directory path to search for the file: ").strip()

    # Search for the file
    file_path = find_file(file_name, search_directory)

    if file_path:
        print(f"File '{file_name}' found at: {file_path}")

        # Let user choose the conversion format
        print("Choose a format to convert the text file to:")
        print("1. XML")
        print("2. CSV")
        print("3. JSON")

        choice = input("Enter your choice (1/2/3): ").strip()

        format_choice = ""
        if choice == '1':
            format_choice = 'xml'
        elif choice == '2':
            format_choice = 'csv'
        elif choice == '3':
            format_choice = 'json'

        # Convert the file if the format choice is valid
        if format_choice:
            convert_file(format_choice, file_path)
        else:
            print("Invalid choice.")
    else:
        print(f"File '{file_name}' not found in the specified directory.")