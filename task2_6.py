print('Напишите программу вычисления арифметического выражения заданного строкой')
def math_string(math_list : list) :
    result = 0.00
    remove = -1
    while len(math_list) != 1:
        bool_minus = False

        if "*" in math_list or "/" in math_list:
            try:
                i = math_list.index("*")
            except:
                i = len(math_list)
            try:
                i_2 = math_list.index("/")
            except:
                i_2 = len(math_list)
            if i > i_2:
                i = i_2
                bool_minus = True
            if bool_minus:
                result = float(math_list[i-1]) / float(math_list[i+1])
            else:
                result = float(math_list[i-1]) * float(math_list[i+1])
            remove = i
        elif "+" in math_list or "-" in math_list:
            try:
                i = math_list.index("+")
            except:
                i = len(math_list)
            try:
                i_2 = math_list.index("-")
            except:
                i_2 = len(math_list)
            if i > i_2:
                i = i_2
                bool_minus = True
            if bool_minus:
                result = float(math_list[i-1]) - float(math_list[i+1])
            else:
                result = float(math_list[i-1]) + float(math_list[i+1])
            remove = i

        for i in range(0,3):
            del math_list[remove-1]

        math_list.insert(remove-1,result)
    return math_list

def priority_operations(math_list: list):
    
    while "(" in math_list:
        new_list = []
        index_of_bracket_1 = 0
        index_of_bracket_2 = len(math_list)
        for i,item in enumerate(math_list):
            if item == "(":
                if "(" not in math_list[i+1:math_list.index(")")]:
                    index_of_bracket_1 = i
                    break
        index_of_bracket_2 = math_list.index(")")    
        for i in math_list[index_of_bracket_1+1:index_of_bracket_2]:
            new_list.append(i)
        for i in range(len(math_list[index_of_bracket_1:index_of_bracket_2+1])):
            del math_list[index_of_bracket_1]
        math_list.insert(index_of_bracket_1,math_string(new_list)[0])
    else:
        math_string(math_list)

text_math = "".join(input("Уравнение : ").split())

math_list = []

result = ""
for i in text_math:
    try:
        if not i.isdigit():
            math_list.append(result)
            result = ""
            math_list.append(i)
        if i.isdigit():
            result += i
    except:
        print('Недопустимый знак')
        break
math_list.append(result)

while "" in math_list:
    math_list.remove("")

priority_operations(math_list)
print(f"{text_math} = {eval(text_math)} eval")
print(f"{text_math} = {math_list[0]} result")