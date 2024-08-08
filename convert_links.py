import os
import re
import shutil

def convert_obisidian_links_to_mkdocs(file_path, docs_dir):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define the regex pattern to find Obsidian links
    pattern = re.compile(r'\[\[(.*?)\]\]')
    
    def replacement(match):
        target = match.group(1)
        target_file = f"{target}.md"
        target_path = find_file_path(docs_dir, target_file)
        if target_path:
            # Calculate the relative path and remove the .md extension
            relative_path = os.path.relpath(target_path, os.path.dirname(file_path)).replace(os.sep, '/')
            relative_path_without_md = os.path.splitext(relative_path)[0]
            return f"[{target}]({'../'+ relative_path_without_md})"
        return match.group(0)
    
    # Replace Obsidian links with MkDocs links
    new_content = pattern.sub(replacement, content)
    
    return new_content

def find_file_path(root_folder, target_file):
    for root, _, files in os.walk(root_folder):
        if target_file in files:
            return os.path.join(root, target_file)
    return None

def process_and_copy_files(source_folder, target_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Convert links in the file
                new_content = convert_obisidian_links_to_mkdocs(file_path, source_folder)
                print(f'Processed: {file_path}')
                
                # Determine relative path and create target directory
                relative_path = os.path.relpath(file_path, source_folder).replace(os.sep, '/')
                target_path = os.path.join(target_folder, relative_path)
                
                # Create necessary directories in target folder
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Write the processed content to the target path
                with open(target_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f'Copied to: {target_path}')

# Set paths
source_folder = 'unprocessed'
target_folder = 'docs'

# Process and copy the files
process_and_copy_files(source_folder, target_folder)
