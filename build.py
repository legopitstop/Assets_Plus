# Compile this project as a mcpack
import os
import zipfile
import json

LOCAL = os.path.dirname(os.path.realpath(__file__))

includes = [
    'manifest.json',
    'pack_icon.png',
    'LICENSE.md',
    'CHANGELOG.md',
    'README.md'
]

def add_folder(path:str, root_path:str=None):
    if os.path.exists(path):
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isfile(full_path):
                p = full_path.replace(LOCAL+'\\', '').replace('\\', '/')
                includes.append(p) # Tmep
            else: add_folder(full_path, root_path)

def write_file(zip:zipfile.ZipFile, filename: str, arcname: str):
    if filename.endswith('.json'): # Automatically minimize json
        try:
            with open(filename, 'r') as r:
                temp = json.load(r)
                data = json.dumps(temp)
                zip.writestr(arcname, data)
        except json.decoder.JSONDecodeError: zip.write(filename, arcname)
    else: zip.write(filename, arcname)

add_folder(os.path.join(LOCAL, 'models'), 'models')
add_folder(os.path.join(LOCAL, 'textures'), 'textures')

# Get the filename
filename = 'unset'
with open(os.path.join(LOCAL, 'manifest.json'), 'r') as r:
    data = json.load(r)
    v = str(data['header']['version']).replace(', ', '.').replace('[', '').replace(']', '')
    filename = 'Assets Plus RP v'+v

with zipfile.ZipFile(os.path.join(LOCAL, 'dist', filename+'.zip'), 'w') as zip:
    # zip.writestr('test.txt', 'This is a test')
    for file in includes:
        full_path = os.path.join(LOCAL, file)
        write_file(zip, full_path, file)

with zipfile.ZipFile(os.path.join(LOCAL, 'dist', filename+'.mcpack'), 'w') as mcpack:
    for file in includes:
        full_path = os.path.join(LOCAL, file)
        write_file(mcpack, full_path, file)

print('Done!')