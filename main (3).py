
#We divided each assignment by how many points they were worth
print('Enter your Large Project assignment grade (out of 50):')
Large_Project = float(input()) / 50
print('Enter your Small Project assignment grade (out of 20):') 
Small_Project = float(input()) / 20
print('Enter your Classwork assignment grade (out of 10):') 
Classwork_1 = float(input()) / 10
print('Enter your Classwork assignment grade (out of 10):')
Classwork_2 = float(input()) / 10
print('Enter your Classwork assignment grade (out of 10):')
Classwork_3 = float(input()) / 10
print('Enter your participation grade (out of 5)')
Participation_1 = float(input()) / 5
print('Enter your participation grade (out of 5)')
Participation_2 = float(input()) / 5
print('Enter your Entry Ticket assignment grade (out of 5):') 
Entry_Ticket1 = float(input()) / 5
print('Enter your Entry Ticket assignment grade (out of 5):') 
Entry_Ticket2 = float(input()) / 5
print('Enter your Entry Ticket assignment grade (out of 5):') 
Entry_Ticket3 = float(input()) / 5
#Here we multiplied each of the assignments by 100 to get the percents
Large_Project = Large_Project * 100 

Small_Project = Small_Project * 100 

Classwork = (Classwork_1 + Classwork_2 + Classwork_3) / 3 * 100 

Participation = (Participation_1 + Participation_2) / 2 * 100 


Entry_Ticket = (Entry_Ticket1 + Entry_Ticket2 + Entry_Ticket3) / 3 * 100 

average = (Large_Project * 0.35) + (Small_Project * 0.25) + (Classwork * 0.20) + (Participation * 0.15) + (Entry_Ticket * 0.5) / 5

average = str(average)
#printing the averages for each type of assignment
Large_Project = str(Large_Project)
print('Large Project = ' + Large_Project + '%')
Small_Project = str(Small_Project)
print('Small Project = ' + Small_Project + '%')
Classwork = str(Classwork)
print('Classwork = ' + Classwork + '%') 
Participation = str(Participation)
print('Participation = ' + Participation + '%')
Entry_Ticket = str(Entry_Ticket)
print('Entry Ticket = ' + Entry_Ticket + '%')
#printing out the average grades for all of the assignment
print('Your average is ' + average + '%') 


