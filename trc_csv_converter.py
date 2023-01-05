#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Xiao Zhu  
# Created Date: 1/5/2023
# version = '0.1'
# ---------------------------------------------------------------------------

import csv
import timeit

trc_filename = input("Enter the file name of .trc file (including .trc): ")
csv_filename = input("Enter the file name of .csv file to be converted (including .csv): ")
# Construct the header for new CAN trace in .CSV file

start = timeit.default_timer()

header_list = ['Message Number','Time Offset(ms)','Type','ID (hex)','Data Length',
               'Byte0','Byte1','Byte2','Byte3','Byte4','Byte5','Byte6','Byte7'] 

# Open the .trc file and create new .csv file
with open(trc_filename,'r') as f1, open(csv_filename,'w',newline="") as f2:
    print('Opening .trc file...')
    lines = f1.readlines()
    # Write the header to CSV file
    print('Creating new .csv file...')
    writer = csv.DictWriter(f2, fieldnames=header_list)
    writer.writeheader()
    count = 0
    print('Converting...')
    for line in lines:
        # Filter TRC file headers
        if list(line)[0]!= ';':
           line_split = line.split()
#          if CAN message is less than 8 bytes, fill the gaps with empty strings
           if len(line_split) == 12:
                line_split.append('')
                
           elif len(line_split) == 11:
                line_split.extend(['',''])
                
           elif len(line_split) == 10:
                line_split.extend(['','',''])
                
           elif len(line_split) == 9:
                line_split.extend(['','','',''])

           elif len(line_split) == 8:
                line_split.extend(['','','','',''])

           elif len(line_split) == 7:
                line_split.extend(['','','','','',''])          
 
           elif len(line_split) == 6:
                line_split.extend(['','','','','','',''])
           else:
                line_split = line_split
           # Write each row to CSV file
           writer.writerow({'Message Number':line_split[0],
                            'Time Offset(ms)':line_split[1],
                            'Type':line_split[2],
                            'ID (hex)':line_split[3],
                            'Data Length':line_split[4],
                            'Byte0':line_split[5],'Byte1':line_split[6],
                            'Byte2':line_split[7],'Byte3':line_split[8],
                            'Byte4':line_split[9],'Byte5':line_split[10],
                            'Byte6':line_split[11],'Byte7':line_split[12]})
                            
    stop = timeit.default_timer()
         
    print('File Converion Completed')
    print('Total Processing Time (Seconds): ', stop - start)

