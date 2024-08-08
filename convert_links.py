import os
import re
import shutil

# Directory containing the markdown files
docs_dir = 'docs'
temp_docs_dir = 'temp_docs'

# Regular expression to find [[wikilinks]]
wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')

def convert_wikilinks(content, current_path):
    def replacer(match):
        link = match.group(1)
        link_path = os.path.join(current_path, link)
        link_relative_path = os.path.relpath(link_path, docs_dir)
        return f'[{link}]({link_relative_path})'

    return wikilink_pattern.sub(replacer, content)

def copy_and_convert_files(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    
    for root, _, files in os.walk(dst):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                # Convert wikilinks considering the current file path
                converted_content = convert_wikilinks(content, root)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(converted_content)

if __name__ == '__main__':
    copy_and_convert_files(docs_dir, temp_docs_dir)
    print("Files copied and links converted.")
