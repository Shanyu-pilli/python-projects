print("wellcome to my computer quiz")

playing = input("Do you want to play? yes/no: ")

if playing.lower() != "yes":
    print("Ok have a nice day")
    quit()
print("lets play")
score = 0
#1
answer = input("what does CPU stand for? \n")
if answer.lower() == "central processing unit":
    print("correct answer")
    score += 1
else:
    print("incorrect answer")
#2
answer = input("what does GPU stand for? \n")
if answer.lower() == "graphics processing unit":
    print("correct answer")
    score += 1
else:
    print("incorrect answer")
#3
answer = input("what does RAM stand for? \n")
if answer.lower() == "random access memory":
    print("correct answer")
    score += 1
else:
    print("incorrect answer")
#4
answer = input("what does PSU stand for? \n")
if answer.lower() == "power supply":
    print("correct answer")
    score += 1
else:
    print("incorrect answer")

print("you got " + str(score) + "questions correct")
print("you got " + str((score/4) * 100) + "%.")
