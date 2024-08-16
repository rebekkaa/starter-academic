import os

# Function to merge all files in a folder
def merge_files(folder_path):
    for folder in os.listdir(folder_path):
        if folder.startswith('.') and os.path.isfile(os.path.join(folder_path, folder)):
            break
        folder = os.path.join(folder_path, folder)
         # open new file in write mode
        files = os.listdir(folder)
        for file in files:
            if file.startswith('.') and os.path.isfile(os.path.join(folder, file)):
                break
            if file.endswith('.bib'):
                with open(os.path.join(folder, file)) as f:
                    lines_in_file = f.readlines()
                    if 'inproceedings' in ''.join(lines_in_file):
                        print("true")
                        with open(folder_path+"/conferences.bib", 'a') as nf:
                        # open files to merge in read mode
                            nf.writelines(lines_in_file)
                            # insert a newline after reading each file
                            nf.write("\n")
                            nf.close()


# Call function from the main folder with the subfolders
merge_files("./content/publication")
