def play_fizz_buzz(number, numbers):
    try:
        for count in range (number, numbers):
            if count >= 0:
                if count % 3 == 0 and count % 5 == 0:
                    print("Fizz Buzz")
                elif count % 3 == 0:
                    print("Fizz")
                elif count % 5 == 0:
                    print("Buzz")
                else:
                    print(count)        
    except TypeError:
        print("Error, this method only takes whole Integer numbers, please try again")
    except ZeroDivisionError:
        print("Fizz Buzz as a game needs something to work with, numbers passed cannot include Zero (0)") 
    except NameError:
        print("Error, this method only takes whole Integer numbers, please try again")

play_fizz_buzz (1, 11)
