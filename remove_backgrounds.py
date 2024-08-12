from PIL import Image
from rembg import remove
import os
from sys import argv

def remove_bg(input_path: str, output_path: str) -> Image:
    name = input_path.split('/')[-1]
    input = Image.open(input_path)
    print(f'Opening {name}')
    output = remove(input)
    print(f'Background for {name} removed')
    output.save(output_path)
    print('---------------------------------------------')

def get_all_files(root, file_ending) -> list[str]:
    paths = []
    for root, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(f'.{file_ending}'):
                paths.append(os.path.join(root, file))
    return paths
    
def append_filename_text(paths: list[str], old_file_ending: str, new_file_ending: str, text: str) -> list:
    new_paths = []
    for path in paths:
        path = path.removesuffix(f'.{old_file_ending}')
        path = path + text + '.' + new_file_ending
        new_paths.append(path)
    return new_paths
    
def remove_all_backgrounds(root_path, old_file_ending, new_file_ending, appended_text):
    paths = get_all_files(root_path, old_file_ending)
    new_paths = append_filename_text(paths, old_file_ending, new_file_ending, appended_text)
    for i in range(0, len(paths)):
        remove_bg(paths[i], new_paths[i]) 
    

if __name__ == '__main__':
    remove_all_backgrounds(argv[1], argv[2], argv[3], argv[4])