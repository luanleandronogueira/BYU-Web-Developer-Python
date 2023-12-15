# initialization

# reading the external file

with open('hr_system.txt') as rh:
    for item in rh:
        # deleting spaces
        line = item.strip()

        # separing strings by spaces
        parts = line.split(' ')


        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = float(parts[3]) 

        amount = salary / 24
        
        if title.lower() == 'engineer': 
            amount += 1000

        print(f'Name: {name} (ID: {id}), Title:{title} - ${amount:.2f}')