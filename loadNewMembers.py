"""
This takes a the ACM signup form excel spreadsheet and translates it into CSV that is importable 
into ACM website. 

"""
import pandas

# Which columns to drop
columns_to_be_dropped = ["Have you signed up on the SLI page?","Timestamp","Enter your GitHub username to be added to OSU ACM's GitHub (optional):"]

members = pandas.read_csv('ACM.csv').drop(columns=columns_to_be_dropped)
members['LastName'] = 'NA'

for index, member in members.iterrows():
    temp = member["Name"].split()
    try:
        member["Name"]  = temp[0]
    except:
        raise Exception("User with email {} doens't have a first name.".format(member["Email Address"]))
    try:
        member["LastName"] = temp[-1]
    except:
        member["LastName"] = "NA"


# Re-arrange for the ACM website format
members = members[["LastName", "Name", "Email Address"]]

# Write to CSV
members.to_csv("membersConverted.csv", encoding='utf-8', header=False, index=False)