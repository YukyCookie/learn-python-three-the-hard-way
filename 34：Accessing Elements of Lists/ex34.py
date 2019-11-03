animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

for i in range(0, len(animals)):
    if i == 0:
        print(f"The animal at {i} is the {i + 1}st animal and is a {animals[i]} ")
        # print("The animal at {} is the {}st animal and is a {} ".format(i, i + 1, animals[i]))
    
    elif i == 1:
        print(f"The animal at {i} is the {i + 1}nd animal and is a {animals[i]} ")
        # print("The animal at {} is the {}nd animal and is a {} ".format(i, i + 1, animals[i]))

    elif i == 2:
        print(f"The animal at {i} is the {i + 1}rd animal and is a {animals[i]} ")
        # print("The animal at {} is the {}rd animal and is a {} ".format(i, i + 1, animals[i]))

    else:
        print(f"The animal at {i} is the {i + 1}th animal and is a {animals[i]} ")
        # print("The animal at {} is the {}th animal and is a {} ".format(i, i + 1, animals[i]))