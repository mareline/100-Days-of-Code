print('''     _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',     
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/ ''')

#Art from https://ascii.co.uk/art/cat
#Incomplete project

print("Hello! Welcome  to CatVille")
print("Your mission is to find your flamingo toy. Good luck!")

choice1  = input('Is your name Miso? Type "yes" or "no" \n').lower()
if choice1 == "yes":
    choice2 = input('Hi Miso! Where are you going? Type "1" for the litter box" or "2" for the bed. \n').lower()
    if choice2 == "2":
        choice3 = input('You feel well rested! What are you going to do next? Type "1" to wake Mareline up or Type "2" to do nothing.\n')
        if choice3 == "2":
            choice4 = input('Wow you\'re bored now, maybe it\'s time to find the toy. Where is it? Type "1" for toy box or "2" for under the bed.\n')
            if choice4 == "1":
                print("Wow, you made a mess in the living room and Mareline took all the toys away. Game over.")
            elif choice4 == "2":
                print("You went under the bed and found your flamingo toy! Time to play with Mareline :)")
else:
    print("Are you walking on the keyboard again Miso?")


    
