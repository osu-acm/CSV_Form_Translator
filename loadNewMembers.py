"""
This takes a the ACM signup form excel spreadsheet and translates it into CSV that is importable 
into ACM website. 

"""
import pandas

# Which columns to drop
columns_to_be_dropped = ["Have you signed up on the SLI page?","Timestamp","Enter your GitHub username to be added to OSU ACM's GitHub (optional):"]

members = pandas.read_csv('ACM.csv').drop(columns=columns_to_be_dropped)
members['LastName'] = 'NA'

for index in range(0, members["Name"].count()):
    temp = members["Name"][index].split()
    members["Name"][index]  = temp[0]
    try:
        members["LastName"][index] = temp[1]
    except:
        members["LastName"][index] = "NA"


# Re-arrange for the ACM website format
members = members[["LastName", "Name", "Email Address"]]

# Write to CSV
members.to_csv("membersConverted.csv", encoding='utf-8', header=False, index=False)