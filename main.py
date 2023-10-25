# hugo's code

def encoder(user_input):
    result = ""
    for n in user_input:
        result += str((int(n) + 3)%10)
    return result


password = ""
while(True):
    print(
'''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
    user_input = int(input("Please enter an option: "))
    if(user_input == 1):
        password = encoder(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
    elif(user_input == 2):
        pass
    elif(user_input == 3):
        break




    