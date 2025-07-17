name = input("What is your name? \n")
print("Hello, " + name + " wellcome to my adventure!")

answer = input("you are on dirt road, it has come to an end you can go left or right, which way like to go? (left/right)").lower()



if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross:").lower()
    if answer == "swim":
        print("You swim accross and eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles,run out water and you lost the game")
    else:
        print("not an valid option,You lose")
elif answer == "right":
    answer = input("you come to the bridge, it looks wobbly,do you want to cross it or head back?(back/cross)").lower()
    if answer == "back":
        print("you go back and loss")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger .do you talk to them (yes/no):").lower()
        if answer == "yes":
            print("you talk to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("you ignore the stranger and they offended and YOU LOSE!")
        else:
            print("not a valid option. You lose")
    else:
        print("not a valid option. You lose")

else:
    print("not a valid option. You lose")

print("Thank you for playing!", name)
