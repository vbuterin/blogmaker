import re
import os
import subprocess
import sys

def download_and_replace_image_links(file_path, dir1, dir2):
    # Create directories if they don't exist
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Find all image URLs in the text
    image_urls = re.findall(r'!\[[a-z]*\]\((https://[^\)]+)\)', content)
    
    for url in image_urls:
        # Extract the file name from the URL
        file_name = url.split('/')[-1]
        
        # Download the image using wget
        wget_command = f'wget --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -P {dir1} {url}'
        subprocess.run(wget_command, shell=True)
        
        # Replace the URL with the new path
        new_path = f'../../../../images/{dir2}/{file_name}'
        content = content.replace(url, new_path)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_path> <dir1> <dir2>")
    else:
        file_path = sys.argv[1]
        dir1 = sys.argv[2]
        dir2 = sys.argv[3]
        download_and_replace_image_links(file_path, dir1, dir2)
