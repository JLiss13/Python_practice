#Created by Jordan Liss
# Replace any string in a file name
import os
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
Folder=raw_input("What directory are you working in?") # Must input a string with apostrophes
print Folder
prefix=raw_input("What is the prefix you want to add on to the every file in the folder?")
print prefix
Filetype=raw_input("What are the file types?")
Filenames=os.listdir(Folder) # Make list of directory a string array
Filenames=filter(lambda k: Filetype in k, Filenames) # Filters out only strings that have .dwg
for file_name in Filenames:
        Old_string=file_name
        old_file_path=os.path.join(Folder,file_name) # Grab old file path
        New_string=prefix+file_name
        file_name=file_name.replace(Old_string,New_string) # Grab old file path and replace old string with new string
        new_file_path=os.path.join(Folder,file_name) # Create new file path with renamed file
        print new_file_path # print new file path progress
        os.rename(old_file_path,new_file_path) # Replace old with new file path