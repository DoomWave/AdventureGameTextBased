name = input('Enter your name. ')
print(f'greetings {name}! welcome to this world!')
start = input('Do you want to go outside? or you prefer to stay here? (type: outside/stay) ')
if start == 'outside':
    print("Great! Let's go!")
    setting = input("Where do you want to go? there is a forest and a cave")
elif start == 'stay ':
    print('Well, enjoy the cold wooden walls.')
    quit()

if setting == 'forest':
    print('You get into the woods, is a bright day, but the biggest and long trees are covering the sun, making it a little darker, you hear a noise.')
    response = input("there's a sword in the floor, do you want to pick up and go where the sound comes from or leave it there?")
    if response == 'pick up':
        print('you pick the sword and going to the sound comes from.')
    elif response == 'leave it there':
        print('You leave the sword in the ground and going to the sound comes from.') 


if setting == 'cave':
    print('You go to the cave, is very dark ')