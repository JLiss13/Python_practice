#For write hyperlinks in a directory to a .csv or .txt
import os 
Filepath=raw_input('Destination Filepath?')
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinks.csv'
Files=os.listdir(Filepath)
Files=filter(lambda k: '.pdf' in k, Files) # Filters out only strings that have .dwg
filenum=0
while filenum < len(Files):
    all_content=[]
    with open(hyperlink_directory) as f:
        all_lines = [line.strip() for line in f]
        all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    Individual_Filepaths=os.path.join(Filepath,Files[filenum])
    Individual_File=Files[filenum]
    if "As-Builts" in Individual_File:
        AsBuilt=1
    else: 
        AsBuilt=" "
    if "Conformed" in Individual_File:
        Conformed=1
    else: 
        Conformed=" "
    if "Contract" in Individual_File:
        Contract=1
    else: 
        Contract=" "
    Drawing_info=Individual_File.split(' ',2)
    Drawing_number=Drawing_info[1]
    ProjectType=Drawing_info[0]
    Individual_File=Drawing_info[2]
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths +'"'+','+'"'+ Individual_File +'"'+')'\
        +';'+ ProjectType +';'+ str(Drawing_number) +';'+ Individual_File +';'+';'+';'+';'+';'+ str(AsBuilt) +';'+ str(Conformed) +';'+ str(Contract)]
    all_content+=additional_line
    filenum=filenum+1 
    with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    
