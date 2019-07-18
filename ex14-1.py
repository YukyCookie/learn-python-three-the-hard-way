from sys import argv

script, user_name1, user_name2 = argv
prompt = '>'

print(f"Hello, {user_name1}. Welcome to the zork and adventure!\nNow, let's go and have some fun")

first = input(prompt)
print(f"You choice is {first}. So,Opening the small mailbox reveals a leaflet. ")

second = input(prompt)
print(f"""Good choice {user_name1}. 
You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here. """)

print(f"""So, I hope that you had a good time {user_name1}. 
What about you, {user_name2}? Do you want to have a try?
""")