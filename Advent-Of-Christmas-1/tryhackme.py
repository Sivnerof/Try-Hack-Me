import os
import zipfile
import exiftool

directory = 'final-final-compressed'

# Open starter zip file "final-final-compressed.zip" if not already unzipped
if not os.path.exists(f'./{directory}'):
    print(f'Unzipping {directory}.zip...')
    with zipfile.ZipFile(f'./{directory}.zip', 'r') as zip_ref:
        print(f'Creating {directory} folder in current directory...')
        zip_ref.extractall(f'./{directory}')

# Store contents of "final-final-compressed" directory in list
directory_contents = os.listdir(f'./{directory}')

# Extract all zip files in "final-final-compressed" at current directory
for l in directory_contents:
    print(f'Unzipping ./{directory}/{l} to current directory...')
    with zipfile.ZipFile(f'./{directory}/{l}', 'r') as zip_ref:
        zip_ref.extractall('./')
    
    # Delete individual files in "final-final-compressed" directory
    print(f'Removing ./{directory}/{l}...')
    os.remove(f'./{directory}/{l}')

# Remove "final-final-compressed" directory
print(f'Removing ./{directory}...')
os.rmdir(f'./{directory}')

# Store contents of current directory / remove "final-final-compressed.zip", "tryhackme.py" from array
current_directory = os.listdir('./')
current_directory.remove('tryhackme.py')
current_directory.remove(f'{directory}.zip')


# Grab metadata for each file
print('Grabbing metadata from files...')
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(current_directory)


# Check for XMP Version 1.1, if found then increment count
target = "XMP:Version"
hits = 0
for d in metadata:
    if target in d.keys() and d[target] == 1.1:
        print('Target Found...')
        hits += 1


# Check each file line by line for the string "password"
password = ''
print('Looking for password file...')
for file in current_directory:
    try:
        with open(file, 'r') as reader:
            f = reader.readlines()
            for line in f:
                new_line = line.strip('\n')
                if 'password' in new_line:
                    print('Password Possibly Found...')
                    password = f'{new_line} and was found in {file}.'
    except:
        print(f'Can\'t read {file}, skipping...')
    
    # Remove files for cleanup
    print(f'Removing {file}...')
    os.remove(f'./{file}')


# Solutions
print('\n=====================RESULTS=====================')
print(f'Total File Count: {len(current_directory)}')
print(f'{target} 1.1 found {hits} times')
print(password)
