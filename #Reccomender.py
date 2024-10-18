
import pandas as pd
import random
# Boxing Reccomender Project backend

#ask if new/existing user
status = input("Are you a (new) or (existing) user?: ").lower()

# IF their a NEW user, ask for a username and check if it exists in txt file already

if status == "new":
        username = input("Enter a username: ")
        with open("/Users/johnpn/Desktop/box.txt",'r') as file:    #open file as readable first
                lines = file.readlines()
                file.close()
                username_taken = False
     
# for each line in txt file, if username == line[index0," "], return that the username is taken, otherwise continue to get a password and write into txt file
        for line in lines:
                cut = line.strip().split(",") # splits each line in lines by , and checks if a match of username in each line
                if (cut[0]) == username:
                        username_taken = True
                        print("username taken") # if a username is found to already exist, print taken
                        break

        if not username_taken:
                password = input("Password: ") #otherwise get password and write both to file then close file
                with open("/Users/johnpn/Desktop/box.txt",'a') as file:
                        file.write(username + "," + password + "\n")
                        file.close()

# IF EXISTING USER
elif status == "existing":
        username = input("Enter a username: ") #get a username

        with open("/Users/johnpn/Desktop/box.txt",'r') as file:    #open file as readable first
                lines = file.readlines()  # read all lines  
                user_found = False

        password = input("Password: ")
        for line in lines:                 # split by comma
              cut = line.strip().split(",")
              if ((cut[0]) == username and password == (cut[1])):    # if index of username and password match continue
                     user_found = True
                     print("Login Successful")
                     break
        if not user_found:
               print("username or password not found")  
else:
       print("Invalid")
       exit(0)

lvl = input("What experience level? (Beginner , Intermediate, Expert): ").lower()

goal = input("Whats your primary goal for this session? (Power, Speed, Defense): ").lower()

# readable csv
df = pd.read_csv('box.csv')

beginner_choices = []

# Check each row in the dataframe (iterating through rows), if row's lvl = input lvl. then if the rows
# if the row at index of the 'tag' is equal to the goal, add it to beginner choices, then print a random choice from beginner choices

for index,row in df.iterrows():
    #print(f"Checking row {index}: lvl={row['lvl']}, tag={row['tag']}")

    if row['lvl'].lower() == lvl:
        if row['tag'].lower() == goal:
           beginner_choices.append(row)

if beginner_choices:  # Check if we have any choices
        chosen_row = random.choice(beginner_choices)
        print(chosen_row, " | ")  # Adding the separator " | " when printing if desired
else:
        print("No matches found for your goal.")



