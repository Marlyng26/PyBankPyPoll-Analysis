# import csv file
import csv

def readFile(fileName):
    Voter_Id=[]
    County=[]
    Candidates=[]
    
#row_count
    
    with open(fileName) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            Voter_Id.append(row[0])
            County.append(row[1])
            Candidates.append(row[2])
    return Voter_Id,County,Candidates
   
Voter_Id,County,Candidates=readFile('election_data.csv')
#Total Votes
print(len(Voter_Id))
candidate1=0
candidate2=0
candidate3=0
candidate4=0
candidate_set = list(set(Candidates))
print(candidate_set)


for candidate in Candidates:
    if candidate == candidate_set[0]:
        candidate1+=1
    elif candidate == candidate_set[1]:
        candidate2 += 1
    elif candidate == candidate_set[2]:
        candidate3 += 1
    elif candidate == candidate_set[3]:
        candidate4 += 1
        
print(candidate1, candidate2, candidate3, candidate4)

print('----------------------------------------------')
total_votes = len(Voter_Id)
print("{name} : {vote}% ({number})".format(name=candidate_set[0], vote=(candidate1/total_votes)*100, number=candidate1))
print("{name} : {vote}% ({number})".format(name=candidate_set[1], vote=(candidate2/total_votes)*100, number=candidate2))
print("{name} : {vote}% ({number})".format(name=candidate_set[2], vote=(candidate3/total_votes)*100, number=candidate3))
print("{name} : {vote}% ({number})".format(name=candidate_set[3], vote=(candidate4/total_votes)*100, number=candidate4))

can_votes = [candidate1, candidate2, candidate3, candidate4]
winnerIndex = can_votes.index(max(can_votes))

winnerName = candidate_set[winnerIndex]

print(winnerName)
