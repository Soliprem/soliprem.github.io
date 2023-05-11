import os
from datetime import datetime

def get_formatted_title(file_name):
    file_name_without_ext = os.path.splitext(file_name)[0]
    words = file_name_without_ext.replace('_', ' ').split()
    return ' '.join(word.capitalize() for word in words)

def add_yaml_snippet(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    file_name = os.path.basename(file_path)
    title = get_formatted_title(file_name)
    creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')

    yaml_snippet = f'---\ntitle: "{title}"\ndate: {creation_date}\n---\n'
    new_content = yaml_snippet + content

    with open(file_path, 'w') as file:
        file.write(new_content)

directory = '/home/soliprem/.local/src/soliprem.github.io/content/notes/'

for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        add_yaml_snippet(file_path)
