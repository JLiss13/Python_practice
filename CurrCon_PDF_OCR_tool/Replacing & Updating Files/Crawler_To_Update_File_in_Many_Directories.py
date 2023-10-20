import os
import shutil
import time, datetime
directory=raw_input('Parent Directory?')
status_directory='M:\Engineering\Current_Configuration\MTS_Rails\Metadata Extras\Status_Report.txt'
updated_file=raw_input('What is the hyperlink of the updated file?')
similiar_filename=os.path.split(updated_file)
similiar_filename=similiar_filename[1]
print similiar_filename
filenum=0
for root, dirs, files in os.walk(directory,topdown=False):
    for file in files:
        date_time=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if file.endswith(similiar_filename):
            shutil.copy(updated_file,os.path.join(root,similiar_filename))
            all_content=[]
            with open(status_directory) as f:
                all_lines = [line.strip() for line in f]
                all_content+=all_lines
                status_report=['=HYPERLINK('+'"'+os.path.join(root,similiar_filename)+'"'+','+'"'+similiar_filename+'")' +';'+ date_time]
                all_content+=status_report
                print status_report
            # Write gathered information to the destination csv file
            with open(status_directory, 'w') as f: # 'w'=Write permissions to file
                for line in all_content:
                    print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    