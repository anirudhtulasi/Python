import re

print("RegX Calculator by Anirudh Tulasi\n")
print("Use x**y for X power Y\n")
print("Type QUIT to exit\n")

previous=0
run = True


def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'QUIT':
        print("Goodbye, Human")
        run = False
    else:
        equation =  re.sub('[a-zA-Z,.:()";_]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous=eval(str(previous)+ equation)


        #print("Result is",previous ) will print result in each iteration



while run:
    perform_math()
