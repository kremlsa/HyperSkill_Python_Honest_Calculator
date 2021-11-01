# write your code here
def is_one_digit(_num1):
    try:
        return -10 < int(_num1.replace(".0", "")) < 10
    except ValueError:
        return False


def lazy_function(_num1, _num2, _oper):
    message = ""
    if is_one_digit(_num1) and is_one_digit(_num2):
        message += " ... lazy"
    if (_num1 == "1" or _num2 == "1") and _oper == '*':
        message += " ... very lazy"
    if (_num1 == "0" or _num2 == "0") and (oper in ['*', '+', '-']):
        message += " ... very, very lazy"
    if message != "":
        print("You are" + message)

def save_memory(_memory, _result):
    if not is_one_digit(str(_result)):
        return _result
    msg_index = 10
    messages = {10: "Are you sure? It is only one digit! (y / n)",
                11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
                12: "Last chance! Do you really want to embarrass yourself? (y / n)"}
    while msg_index < 13:
        print(messages.get(msg_index))
        ans = input()
        if ans == "n":
            return _memory
        if ans == "y":
            msg_index = msg_index + 1
    return _result



memory = 0
result = 0
while True:
    print("Enter an equation")
    calc = input()
    oper = calc.split(" ")[1]
    num1 = calc.split(" ")[0]
    num2 = calc.split(" ")[2]
    if num1 == 'M':
        num1 = str(memory)
    if num2 == 'M':
        num2 = str(memory)
    if not num1.replace('.','',1).isdigit() or not num2.replace('.','',1).isdigit():
        print( "Do you even know what numbers are? Stay focused!")
        continue
    if not oper in ['+', '-', '*', '/']:
        print( "Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    lazy_function(num1, num2, oper)

    if oper == '+':
        result = float(num1) + float(num2)
        print(result)
    if oper == '-':
        result = float(num1) - float(num2)
        print(result)
    if oper == '*':
        result = float(num1) * float(num2)
        print(result)
    if oper == '/':
        if float(num2) == 0:
            print("Yeah... division by zero. Smart move...")
            continue
        result = float(num1) / float(num2)
        print(result)
    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        if answer == 'y':
            memory = save_memory(memory, result)
            break
        if answer == 'n':
            break
    while True:
        print("Do you want to continue calculations? (y / n):")
        answer2 = input()
        if answer == 'y':
            break
        if answer == 'n':
            break
    if answer2 == 'y':
        continue
    if answer2 == 'n':
        break

