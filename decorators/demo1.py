def add_num_decorator(anyfunc):
    def wraperFunction(n1,n2):
        print('Action Before Add function')
        print(anyfunc(n1,n2))
        print('Action after Add function')
    return wraperFunction

@add_num_decorator
def add_two_num(number1,number2):
    return number1+number2

add_two_num(10,20)