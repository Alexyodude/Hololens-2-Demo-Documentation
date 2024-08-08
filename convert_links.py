import os
import re

# Directory containing the markdown files
docs_dir = 'docs'

# Regular expression to find [[wikilinks]]
wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')

def convert_wikilinks(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace [[wikilink]] with [wikilink](wikilink.md)
    converted_content = wikilink_pattern.sub(r'[\1](\1.md)', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(converted_content)

def convert_all_wikilinks(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                convert_wikilinks(os.path.join(root, filename))

if __name__ == '__main__':
    convert_all_wikilinks(docs_dir)
    print("Conversion completed.")
