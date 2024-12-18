import os
import re
import shutil

def convert_obisidian_links_to_mkdocs(file_path, docs_dir):
    # Read the file content as is (including any tab spacing)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define the regex patterns to find Obsidian links and image links
    link_pattern = re.compile(r'\[\[(.*?)\]\]')
    image_pattern = re.compile(r'!\[\[(.*?)\]\]')
    
    def link_replacement(match):
        target = match.group(1)
        target_file = f"{target}.md"
        target_path = find_file_path(docs_dir, target_file)
        if target_path:
            # Calculate the relative path and remove the .md extension
            relative_path = os.path.relpath(target_path, os.path.dirname(file_path)).replace(os.sep, '/')
            relative_path_without_md = os.path.splitext(relative_path)[0]
            return f"[{target}]({'../' + relative_path_without_md})"
        return match.group(0)
    
    def image_replacement(match):
        image_file = match.group(1)
        image_path = find_file_path(docs_dir, image_file)
        if image_path:
            # Calculate the relative path for the image
            relative_path = os.path.relpath(image_path, os.path.dirname(file_path)).replace(os.sep, '/')
            return f"![]({'../' + relative_path})"
        return match.group(0)
    
    # Replace Obsidian links and image links with MkDocs links
    content = link_pattern.sub(link_replacement, content)
    content = image_pattern.sub(image_replacement, content)

    # # Add "-" for indentation, converting it to a Markdown list
    # indented_line_pattern = re.compile(r'^(\t+)(.*)', re.MULTILINE)
    # content = indented_line_pattern.sub(lambda m: f"{m.group(1).replace('\t', '    ')}- {m.group(2)}", content)
    
    return content

def find_file_path(root_folder, target_file):
    for root, _, files in os.walk(root_folder):
        if target_file in files:
            return os.path.join(root, target_file)
    return None

def process_and_copy_files(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
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
                
                # Write the processed content to the target path, preserving indentation
                with open(target_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f'Copied to: {target_path}')
        
        # Copy non-Markdown files and directories
        for dir in dirs:
            src_dir = os.path.join(root, dir)
            dst_dir = os.path.join(target_folder, os.path.relpath(src_dir, source_folder))
            if not os.path.exists(dst_dir):
                shutil.copytree(src_dir, dst_dir)
                print(f'Copied directory: {src_dir} to {dst_dir}')
        
        for file in files:
            if not file.endswith('.md'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(target_folder, os.path.relpath(src_file, source_folder))
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src_file, dst_file)
                print(f'Copied file: {src_file} to {dst_file}')

def copy_image_folder(source_folder, target_folder, image_folder_name='images'):
    source_image_folder = os.path.join(source_folder, image_folder_name)
    target_image_folder = os.path.join(target_folder, image_folder_name)
    
    if os.path.exists(source_image_folder):
        if os.path.exists(target_image_folder):
            # If target image folder exists, merge contents
            for root, _, files in os.walk(source_image_folder):
                for file in files:
                    source_file = os.path.join(root, file)
                    relative_path = os.path.relpath(source_file, source_image_folder)
                    target_file = os.path.join(target_image_folder, relative_path)
                    os.makedirs(os.path.dirname(target_file), exist_ok=True)
                    shutil.copy2(source_file, target_file)
                    print(f'Copied image file to: {target_file}')
        else:
            # If target image folder doesn't exist, copy the whole directory
            shutil.copytree(source_image_folder, target_image_folder)
            print(f'Copied image folder to: {target_image_folder}')
    else:
        print(f"No image folder found at: {source_image_folder}")

# Set paths
source_folder = 'unprocessed'
target_folder = 'docs'

# Process and copy the files
process_and_copy_files(source_folder, target_folder)

# Copy the image folders (including custom image directories like 'Unity/images')
image_folders = ['images', 'Unity/images']
for image_folder in image_folders:
    copy_image_folder(source_folder, target_folder, image_folder)
