import os
import csv
import datetime
import collections 

csvpath = os.path.join('..', 'Resources', 'election_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     
   

    # next(csvreader, None)
    # next(csvfile)
    print("---------")
    header = "ELECTION RESULTS"
    print(header)
    
    print("--------------------")

    # total_votes = total rows minus the header(line 1)
    tot_votes = sum(1 for line in open(csvpath)) - 1
    
    print("Total Votes:", + tot_votes)
    
    print("--------------------")
    
    # Find names of candidates in row
    # Set counter for each candidate
    vest_ct = 0
    tor_ct = 0
    seth_ct = 0
    cord_ct = 0

    # Loop down the rows to count each candidate
    for row in csvreader:
        if row[2] == 'Vestal':
           vest_ct += 1

        if row[2] == 'Torres':
           tor_ct += 1

        if row[2] == 'Seth':
           seth_ct += 1

        if row[2] == 'Cordin':
           cord_ct += 1
    
    # Divide total of each candidate by "Total Votes"       
    vest_per = vest_ct / tot_votes 
    print('Vestal:', vest_ct,"({:.0%})".format(vest_per))
    
    tor_per = tor_ct / tot_votes 
    print('Torres:', tor_ct, "({:.0%})".format(tor_per))
    
    seth_per = seth_ct / tot_votes 
    
    print('Seth:', seth_ct, "({:.0%})".format(seth_per))
    
    cord_per = cord_ct / tot_votes 
    print('Cordin:', cord_ct, "({:.0%})".format(cord_per))
    
    print("--------------------")

    print("Winner: Vestal")



        
        