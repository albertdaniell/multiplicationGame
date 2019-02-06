import random
repeat = 'true'

def ask():
    question = 1
    wrong_answers=0
    correct_answers=0

    while repeat:



        num1 = int(random.randint(1, 100))
        num2 = int(random.randint(1, 10))
        print("Question number" , str(question), " [Total Questions:" ,str(int(question-1)),"Correct:",str(correct_answers),"Wrong:",str(wrong_answers),"]")
        print("---------------------------------")
        print("What is " + str(num1) + "*" + str(num2) + "?")
        try:
            ans = int(input("Ans: "))
        except ValueError:
            print("Input must be int")

        question +=1


        correct_ans = num1 * num2
        if ans == correct_ans:
            correct_answers+=1
            print("You are correct")

        else:
            wrong_answers+=1
            print("You are wrong,the answer is :" + str(correct_ans))


ask()