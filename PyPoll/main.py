import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath) as file:
    reader_csv = csv.reader(file, delimiter=',')
    #using delimerts to  denotes the bonds 
    votes=list(reader_csv)
    total_votes= len(votes) -1 # to remove the  headers
print("Election Results") 
print("-----------------------------") 

print(f"Total votes: {total_votes}")
#creating a dictionary for candidates
print("-----------------------------") 
candidates={}
# loop  through for each row in votes list. starting for 2 to remove the header
# finding candidate percentage  
for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
       candidates[row[2]] += 1
#loop through 
for candidate, vote_count in candidates.items():
    percentage= round((vote_count/total_votes)* 100,3)
    
    print(f"{candidate}:\t{percentage}%\t({vote_count})")
print("-----------------------------") 

#winning_number = 272892
Winner_name= 0
vote_list = []
for candidate, vote_count in candidates.items():
    vote_list.append(vote_count)
   
print(max(vote_list))
for candidate, vote_count in candidates.items():
    if max(vote_list) == vote_count:
        print(f'winner: {candidate}')
