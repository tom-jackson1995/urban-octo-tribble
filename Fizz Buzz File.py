def play_fizz_buzz(number, numbers):
    multi_1 = 3
    multi_2 = 5
    multi_3 = 7  
    try:
        for count in range (number, numbers):
            returning_list = [] 
            check = 1
            if count > 0:
                if count % multi_1 == 0:
                    returning_list.append("Fizz")
                    check += 1
                if count % multi_2 == 0:
                    returning_list.append("Buzz")
                    check += 1
                if count % multi_3 == 0:
                    returning_list.append("Bizz")
                    check += 1
                elif check < 1:
                    returning_list.append(str(count))
            print(",".join(returning_list))      
    except TypeError:
        print("Error, this method only takes whole Integer numbers, please try again")
    except ZeroDivisionError:
        print("Fizz Buzz as a game needs something to work with, numbers passed cannot include Zero (0)") 
    
