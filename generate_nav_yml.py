import os
import yaml

def generate_nav(docs_dir, base_url=''):
    nav = []
    for root, dirs, files in os.walk(docs_dir):
        # Convert root to POSIX-style path
        relative_root = os.path.relpath(root, docs_dir).replace(os.sep, '/')
        
        if relative_root == '.':
            relative_root = ''
        
        if not relative_root:
            for file in files:
                if file.endswith('.md'):
                    if file == 'Index.md':
                        title = 'Home'
                    else:
                        title = os.path.splitext(file)[0].replace('_', ' ').title()
                    nav.append({
                        title: os.path.join(base_url, file).replace(os.sep, '/')
                    })
        else:
            section_name = os.path.basename(relative_root)
            section_nav = []
            for file in files:
                if file.endswith('.md'):
                    if file == 'ndex.md':
                        title = section_name.title()
                    else:
                        title = file.replace('.md', '').replace('_', ' ').title()
                    section_nav.append({
                        title: os.path.join(relative_root, file).replace(os.sep, '/')
                    })
            if section_nav:
                nav.append({section_name.title(): section_nav})
    return nav

def update_mkdocs_yml(mkdocs_yml_path, docs_dir):
    nav = generate_nav(docs_dir)
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    config['nav'] = nav
    
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)
    print(f"Updated {mkdocs_yml_path} with new nav configuration.")

if __name__ == '__main__':
    mkdocs_yml_path = 'mkdocs.yml'
    docs_dir = 'docs'
    update_mkdocs_yml(mkdocs_yml_path, docs_dir)
