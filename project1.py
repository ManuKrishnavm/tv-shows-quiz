
# Importing functions from the fx module that contain quiz logic
from project_fun.fx import *

# Introduction message for the quiz
print("\n\nThis is a quiz to test your knowledge about fiction and televised shows consisting of 10 Quesions:\n")
print('Rules:\n1.you will have 4 options to answer')
print('2.Option ranging between (A,B,C,D) will only be acceptable ')
print('3.Wrong option will be read as Wrong answering and will result in automatic skip')

# Loop to start the quiz upon user confirmation
while True:

    # Asking if the user is ready to start the quiz
    any = str(input('if ready enter Yes or No(Y/N):'))

    # Each function (fun1 to fun10) corresponds to a question in the quiz.
    # The result of the question is added to a list (1 for correct, 0 for wrong).
    if (any == 'y') or (any == 'Y'):

        counter = 0
        lst = []
        an1=fun1()
        if an1==1:
            lst.append(1)
        elif an1==0:
            lst.append(0)


        an2=fun2()
        if an1==1:
            lst.append(1)
        elif an2==0:
            lst.append(0)


        an3=fun3()
        if an3==1:
            lst.append(1)
        elif an3==0:
            lst.append(0)


        an4=fun4()
        if an4==1:
            lst.append(1)
        elif an4==0:
            lst.append(0)



        an5=fun5()
        if an5==1:
            lst.append(1)
        elif an5==0:
            lst.append(0)



        an6=fun6()
        if an6==1:
            lst.append(1)
        elif an6==0:
            lst.append(0)



        an7=fun7()
        if an7==1:
            lst.append(1)
        elif an7==0:
            lst.append(0)



        an8=fun8()
        if an8==1:
            lst.append(1)
        elif an8==0:
            lst.append(0)



        an9=fun9()
        if an9==1:
            lst.append(1)
        elif an9==0:
            lst.append(0)



        an10=fun10()
        if an10==1:
            lst.append(1)
        elif an10==0:
            lst.append(0)


        # After the quiz, user can choose to edit any answer
        while(True):

            # User selects the question number they wish to edit
            edit = str(input('do yu want to edit any ansers(Y/N):'))
            if (edit == 'y') or (edit == 'Y'):

                # Additional logic for editing other questions
                lol = int(input('Which question do you want to edit:'))
                if (lol == 1):
                    a1 = fun1()
                    if (a1 == 1):
                        lst[0] = 1
                    else:
                        pass
                if (lol == 2):
                    a1 = fun2()
                    if (a1 == 1):
                        lst[1] = 1
                    else:
                        pass
                if (lol == 3):
                    a1 = fun3()
                    if (a1 == 1):
                        lst[2] = 1
                    else:
                        pass
                if (lol == 4):
                    a1 = fun4()
                    if (a1 == 1):
                        lst[3] = 1
                    else:
                        pass
                if (lol == 5):
                    a1 = fun5()
                    if (a1 == 1):
                        lst[4] = 1
                    else:
                        pass
                if (lol == 6):
                    a1 = fun6()
                    if (a1 == 1):
                        lst[5] = 1
                    else:
                        pass
                if (lol == 7):
                    a1 = fun7()
                    if (a1 == 1):
                        lst[6] = 1
                    else:
                        pass
                if (lol == 8):
                    a1 = fun8()
                    if (a1 == 1):
                        lst[7] = 1
                    else:
                        pass
                if (lol == 9):
                    a1 = fun9()
                    if (a1 == 1):
                        lst[8] = 1
                    else:
                        pass
                if (lol == 10):
                    a1 = fun10()
                    if (a1 == 1):
                        lst[9] = 1
                    else:
                        pass
            # If the user doesn't want to edit answers, calculate the score
            elif (edit == 'N') or (edit == 'n'):
                break
        print('the quiz has been ended\n\n\n\n\n\n\n\n\n\n\n')
        print('________________RESULS________________\n'
              '+------------------------------------+')
        for i in lst:
            if(i==1):
                counter+=1
        print("| you answered", counter, "questions correctly |")
        n = 1
        print('+------------------------------------+')

        for i in lst:
            if i == 1:
                print('|    question number', n, 'was right     |')
            else:
                print('|    question number', n, 'was wrong     |')
            n += 1
        print('+------------------------------------+\n\n')
        print('If you want to take the quiz again:')
    elif (any == 'N') or (any == 'n'):
        print("Take the quiz when Your are ready")
        break
    else:
        print('please enter a valid query')



