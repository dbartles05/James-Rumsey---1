# All about the Function
# Dustyn Bartles
# 9/1/2021
# Jr

def myCountLetters(Answer):
    Lcount = 0
    Ucount = 0
    for l in Answer:
        if l.isupper():
            Ucount += 1
        else:
            Lcount += 1
    return Ucount,Lcount

running = True

Count = 0

while running:
    Answer = input('Please enter a string, no numbers: ')
    if Answer.upper() == 'Q':
        running = False
    else:
        if Answer.isalpha():
            Ucount,Lcount = myCountLetters(Answer)
            print(f"Here are your counts {Ucount}:{Lcount}")
            Count += 1
            print()

        else:
            print('Please no numbers.')
            print()
print("You played", Count, "Times, Thank you!")


