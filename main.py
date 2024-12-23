import datetime
import time
import Welcome


date_time = datetime.datetime.now()
date = date_time.date()
times = date_time.strftime("%H:%M:%S")

def get_age(name):
    while True:
        try:
            age = int(input("Enter {name}'s age: "))
            return age
        except ValueError:
            print("Invalid age, please input a valid age")
def love():
    me = input("Enter your name: ")
    print(f"{me}, welcome to our relationship compatibility checker app, now let's find out your age")
    time.sleep(2)
    my_age = get_age(me)
    partner = input("Enter your partner's name: ")
    p_age = get_age(partner)
    print(f"Great!, let us find out how compatible you are with {partner}")
    time.sleep(2)
    if my_age >= 18 and p_age >= 18:
        print(f"you and {partner} are adult, let us go into the questions aspect  as reported on {date} at {times}.")
    elif my_age >= 18:
        print(f"{partner} is still a minor therefore the relationship is illegal as reported on {date} at {times}")
    elif p_age >= 18:
        print(f"you are still a minor and you should focus on your studies  as reported on {date} at {times}")
    else:
        print("you are both minors, therefore, this app is not suitable for you")

def questions():
    question_1 = input("What is your favorite food: ")
    question_2 = input(f"What is {love.partner}'s favorite food")


def main():
    Welcome()
    love()
    questions()

main()