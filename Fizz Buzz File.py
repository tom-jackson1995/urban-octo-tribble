

def play_fizz_buzz(number):
    try:
        if number >= 0:
            if number % 3 == 0 and number % 5 == 0:
                print("Fizz Buzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)        
    except TypeError:
        print("Error, this method only takes whole Integer numbers, please try again")
    except ZeroDivisionError:
        print("Fizz Buzz as a game needs something to work with, numbers passed cannot include Zero (0)") 
    except NameError:
        print("Error, this method only takes whole Integer numbers, please try again")


play_fizz_buzz(tom)