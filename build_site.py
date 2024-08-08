import os
import subprocess
import shutil
from convert_links import copy_and_convert_files

docs_dir = 'docs'
temp_docs_dir = 'temp_docs'
mkdocs_temp_file = 'mkdocs_temp.yml'
site_dir = 'site'

def create_temp_mkdocs_config():
    mkdocs_config_content = f"""
site_name: My Obsidian Notes
theme:
  name: material
docs_dir: {temp_docs_dir}
site_dir: {site_dir}
    """
    with open(mkdocs_temp_file, 'w', encoding='utf-8') as file:
        file.write(mkdocs_config_content)

def build_site():
    # Copy and convert markdown files
    copy_and_convert_files(docs_dir, temp_docs_dir)

    # Create temporary MkDocs config
    create_temp_mkdocs_config()

    # Build the site using MkDocs
    subprocess.run(['mkdocs', 'build', '--config-file', mkdocs_temp_file], check=True)

def deploy_site():
    # Deploy the site using MkDocs
    subprocess.run(['mkdocs', 'gh-deploy', '--config-file', mkdocs_temp_file], check=True)

def clean_up():
    # Clean up temporary files and config
    if os.path.exists(temp_docs_dir):
        shutil.rmtree(temp_docs_dir)
    if os.path.exists(mkdocs_temp_file):
        os.remove(mkdocs_temp_file)

if __name__ == '__main__':
    try:
        build_site()
        deploy_site()
        print("Site built and deployed successfully.")
    finally:
        clean_up()
