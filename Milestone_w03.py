# Actions

action_1 = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?\n ')

print(f'You choose the {action_1.upper()}\n')

# Choose the action
if action_1.upper().strip() == 'MATCH':
    print("With MATCH you can light a fire and spend the night, the fire can help you keep away from the animals. Or you can continue walking and get out of the forest as soon as possible, but there is a danger of being attacked by an animal, especially a bear. Which one do you choose 'WALK' or 'BONFIRE' \n")
    
    choose_1 = input('\nChoose WALK or BONFIRE \n')
    
    if choose_1.upper().strip() == 'WALK':
        #Challenge 1 WALK
        print('\nWhile you are walking you see a big bear, do you RUN or HIDE? \n')

        # Choose RUN or HIDE actions
        choose_run_hide = input('RUN or HIDE\n')

        if choose_run_hide.upper().strip() == 'RUN':
            print("You ran enough to up on a tree, and waited the bear go away. At morning the rescuers met you and helped you to go out saved of the forest. It was the best choice that you've made")

        elif choose_run_hide.upper().strip() == 'HIDE':
            print("You hided through the trees and kept in silence until the bear go away, and after you continued walking until meet the rescuers. You are so tired and hungry, but safed. I wasn't a the best choice.")

        else:
            print("After 3 days you were founded by the rescuers, you were malnourished, sick and with a lot bruises. It was the worst choice that you've made.")


    elif choose_1.upper().strip() == 'BONFIRE':
        #Challenge 2 BONFIRE
        print('\nWhile you are trying to do a bonfire, you need more wood. Go through the forest and see to ways, RIGHT or LEFT. Which you choose? \n')

        # Choose RIGHT or LEFT actions
        right_left = input('RIGHT or LEFT: \n')

        if right_left.upper().strip() == 'RIGHT':
            print('While you are walking you see forward a little log cabin, you meet an old man called Joe. He helped you and kept you safe at the morning called the rescuers. This was a good choice.')

        elif right_left.upper().strip() == 'LEFT':
            print("Along the way you founded a big lake. In this lake the team of rescuers searching for you. All was well and you are saved! The best choice you've mande.")

        else:
            print('you failed to light the fire, and you waited 2 days to be found by rescuers. It was the worst choice that you had made.')
   

# FLASHLIGHTs
elif action_1.upper().strip() == 'FLASHLIGHT':
    print("With FLASHLIGHT you can see all things along the way all the road. But you feel scared do you prefer HIDE youself among the trees to keep saved from the animals of start to SCREAM to the rescuers found you. \n")

    #Choose SCREAM or HIDE
    hide_scream = input('HIDE or SCREAM \n')

    if hide_scream.upper().strip() == 'HIDE':
        print('You hid and ended up sleeping. As you slept, the rescuers passed by you and did not find you. You are still completely lost.')

    elif hide_scream.upper().strip() == 'SCREAM':
        print('When you started screaming, you caught the attention of rescuers who were near the lake. However, you ran a great risk because you drew a lot of attention from the bears that surrounded you there. You took a big risk but it turned out fine in the end!')

    else:
        print('You are completely lost. Waiting to do some choices.')

# If you not choose anything
else:
    print('You failed! You need to do right choices in your life! Choises determ the future!')
