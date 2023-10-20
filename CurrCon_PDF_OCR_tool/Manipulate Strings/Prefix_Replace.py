#Created by Jordan Liss
# Replace any string in a file name
import os
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
Folder=raw_input("What directory are you working in?") # Must input a string with apostrophes
print Folder
Filetype=raw_input("What are the file types?")
old_prefix=raw_input("What is the old prefix you want change on to the every file in the folder?")
print old_prefix
new_prefix=raw_input("What is the new prefix you want?")
print new_prefix
Filenames=os.listdir(Folder) # Make list of directory a string array
Filenames=filter(lambda k: Filetype in k, Filenames) # Filters out only strings that have .dwg
for file_name in Filenames:
        old_file_path=os.path.join(Folder,file_name) # Grab old file path
        file_name=file_name.replace(old_prefix,new_prefix) # Grab old file path and replace old string with new string
        new_file_path=os.path.join(Folder,file_name) # Create new file path with renamed file
        print new_file_path # print new file path progress
        os.rename(old_file_path,new_file_path) # Replace old with new file path