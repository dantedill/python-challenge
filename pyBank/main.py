#import modules
import csv
import os

#source to read csv file
fileload = os.path.join("budget_data.csv")

#read to text file (analysis)
outputFile = os.path.join("analysis.text")

# Declare variables
totalMonths = 0  # initial value
revenuenetTotal = 0 # total of net Total
# need to get average change monthly(3)
 # initialize the list track monthly changes (netChange) for greatest increase(1) /greatest decrease(2)
monthlyChanges = []
# initialize months for greatest increase(1) /greatest decrease(2)  
months = []



# read csv file
with open (fileload)as budget_data:
    #create a csv reader object
    csvreader = csv.reader(budget_data)

    # read header row
    header = next(csvreader)

    # move to firstrow to value of first row with number values(1)(2)(3)
    firstrow = next(csvreader)

    # establish the previous row to add greatest increase(1) /greatest decrease(2) 
# revenue is index [1] (after headings)(1)(2)(3)
    previousRevenue = float(firstrow[1])

 #counting months to get average change(1)(2)(3)
    totalMonths += 1
     # adding the total of revenue loss/profit(1)(2)(3)
     # revenue is index [1] (after headings) (+=) will give the sum of  revenuenetTotal(1)(2)(3)
    revenuenetTotal += float(firstrow[1])
    

    # Loop to count Months (totalMonths)
    for row in csvreader :
        #counting months
        totalMonths += 1
       
        # adding the total of revenue loss/profit
            # revenue is index [1] (after headings) (+=) will give the sum of  revenuenetTotal
        revenuenetTotal += float(row[1])
        # calculate net change monthly(1)(2)(3)
        netChange = float(row[1]) - previousRevenue
        #add to list of monthly changes (1)(2)(3)
        monthlyChanges.append(netChange)

        #add thr first month that a change occurred (1)(2)
        # month index 0
        months.append(row[0])

        # Update the previous revenue
        previousRevenue = float(row[1])


        

      

        #update the previous revenue (1)(2)(3)
        previousRevenue = float(row[1])

    
# Getting the average monthly changes (total of monthlychanges / the number of monthlychanges)(3)
averageMonthlyChange = sum(monthlyChanges) / len(monthlyChanges)
# Value of the greatest increase((1)....read ["month", increase]
greatestIncrease = [months[0], monthlyChanges[0]]
# Value of the greatest increase((1)....read ["month", increase]
greatestdecrease = [months[0], monthlyChanges[0]]


# use loop to calculate the index of the greatest and least monthly changw
# Print monthly chages to look at data
for d in range(len(monthlyChanges)):
#        print(d)  print just see data

#calculate the greatest increase and decrease
        if(monthlyChanges[d] > greatestIncrease[1]):
         # if value is gt than greatest increase, that value becomes the new greatest increase
            greatestIncrease[1] = monthlyChanges[d]
        #update the month
        greatestIncrease[0] = months[d]


        if(monthlyChanges[d] < greatestdecrease[1]):
            
         # if value is gt than greatest decrease, that value becomes the new greatest decrease
            greatestdecrease[1] = monthlyChanges[d]
        #update the month
        greatestdecrease[0] = months[d]

   
   
   
   
    # generating output
output = (
        f"\n Financial Analysis \n" # read header and move to new line (\n)
        f"----------------\n"      
        f"\t Total Months: {totalMonths}\n" # (\t) tab line over to right
        f"\t Total:  ${revenuenetTotal:,.2f}\n"  # change string into float with 2 decmil places (:,.2f)
        f"\t Average Change:  ${averageMonthlyChange:,.2f}\n" 
        f"\t Greatest Increase in Profits: {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n "
         f"\t Greatest decrease in Profits: {greatestdecrease[0]} Amount ${greatestdecrease[1]:,.2f} \n "  
              )

 #print output to console/ terminal
print(output)

# read to text file
with open (outputFile, "w") as textFile:
 textFile.write(output)