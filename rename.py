import os

# Set the directory where the files are located
directory = './results_new/atpe10'

# Traverse through all files in the directory
for filename in os.listdir(directory):
    # Check if the file starts with 'atpe4'
    if filename.startswith('atpe8'):
        # Construct the new file name by replacing 'atpe4' with 'atpe5'
        new_filename = 'atpe10' + filename[5:]
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed: {filename} -> {new_filename}')

for filename in os.listdir(directory):
    # Check if the file ends with 'ATPE4'
    if filename.endswith('ATPE8.csv'):
        # Construct the new file name by replacing 'ATPE4' with 'ATPE5'
        new_filename = filename[:-9] + 'ATPE10.csv'
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed: {filename} -> {new_filename}')

print("Renaming complete!")
