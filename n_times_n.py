from random import randint
import time

game_running = True
reveiw = False
wrong_answer = []
count = 0
answer_count = 0
name = input("What is your Name? ")
# timer = pass
# streak = pass

def intro():
    print(" Let's Practice N times N!")
    print("Hello" + name+"!" + "Welcome")
    print("--------" * 7)

def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("Time Limit: %02d" % (elapsed))
        time.sleep(1)

intro()

while game_running == True:
    count += 1
    rand_number1 = randint(2, 9)
    rand_number2 = randint(2, 9)
    answer = rand_number1 * rand_number2

    print(str(rand_number1) + " X " + str(rand_number2))
    user_answer = input(" What's Your Answer? ")
    # stopwatch(4)
    if user_answer.isdigit() == True:
        if int(user_answer) == answer:
            answer_count += 1
            print(" Wow!!! Correct!! " + name)

        elif int(user_answer) != answer or user_answer == None:
            print(" Oops!!! Wrong!! " + name)
            wrong_answer.append([rand_number1, rand_number2])
            print(wrong_answer)

            if len(wrong_answer) > 9:
                print(" You Got 10 Questions Wrong. Do you wanna review them? ( Y / N ) ")
                user_choice = input("")
                if user_choice == "y" or user_choice == "Y":
                    print(" Review mode has been activated!! ")
                    reveiw = True
                    if reveiw == True:
                        for i in wrong_answer:
                            rand_number1 = i[0]
                            rand_number2 = i[1]
                            answer = int(rand_number1) * int(rand_number2)
                            print(rand_number1, " X ", rand_number2, " = ")
                            user_answer = input(print(" What's Your Answer? "))
                            if user_answer.isspace() or user_answer.isalpha():
                                print(" 숫자만 입력가능합니다. ")
                            if user_answer.isdigit():
                                if int(user_answer) == answer:
                                    print(" Correct!! ^_^ ")
                                else:
                                    print(" You Got This Wrong 2 Times! T_T ")
                if user_choice == "n" or user_choice == "N":
                    if answer_count != count:
                        print(" Your final SCORE is {} / {}. Well Done.".format(answer_count, count))
                        game_running = False
                elif user_choice.isdigit() or user_choice.isspace():
                    print(" y 또는 n을 입력해주세요. ")
    else:
        print(" 숫자만 입력 가능합니다. ")
