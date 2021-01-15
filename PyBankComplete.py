import csv

def readFile(fileName):
    dates = []
    budget= []
    with open(fileName) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            dates.append(row[0])
            budget.append(row[1])
                #print(f'\t{row[0]} date {row[1]} for profile/loss ')
          
    #print(f'Processed {line_count} lines.')
    return dates,budget



dates,budget=      readFile('budget_data.csv')
#Total months 
print('total_num_months:' ,len(dates))

netprofitloss=0
#for loop
for x in budget:
    netprofitloss+=int(x)

print('total:',netprofitloss )

#forloop for average change 
# profit=0
# loss=0
# for x in budget:
#     if x.startswith('-'):
#         loss-=int(x)
#     else:
#         profit+=int(x)
# print((profit-loss)/len(budget))       
totalCount = len(budget)
sumValues = 0
sumChg = 0
greatestInc = 0
greatestDec = 0
gInchDte = ""
gDecDte = ""
i = 0
j = 1
#average change 
for value in budget:
    sumValues = sumValues + int(value)
    #calculate greatestst increase and decrease
    if j < totalCount:
        change = int(budget[j]) - int(budget[i])
        if change > greatestInc:
            greatestInc = change
            gInchDte = dates[j]
        if change < greatestDec:
            greatestDec = change
            gDecDte = dates[j]
        sumChg = sumChg + change
        i = i + 1
        j = j + 1

aveChg = sumChg / totalCount
format_float = "{:.2f}".format(aveChg)
print('average change:', format_float)

#greatest increase
print('greatest increase:',gInchDte, greatestInc)
print('greates decrease:',gDecDte, greatestDec)