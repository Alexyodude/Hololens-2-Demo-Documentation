import os
import shutil
import subprocess

def run_command(command):
    """Run a shell command and print the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    # Step 1: Run generate_nav_yml.py
    run_command("python generate_nav_yml.py")
    
    # Step 2: Delete everything inside the docs folder
    docs_dir = 'docs'
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
        os.makedirs(docs_dir)
        print(f"Cleared the {docs_dir} directory.")

    # Step 3: Run convert_links.py
    run_command("python convert_links.py")
    
    # Step 4: Delete the site folder
    site_dir = 'site'
    if os.path.exists(site_dir):
        shutil.rmtree(site_dir)
        print(f"Deleted the {site_dir} directory.")
    
    # Step 5: Run mkdocs gh-deploy
    run_command("mkdocs gh-deploy")

if __name__ == "__main__":
    main()
