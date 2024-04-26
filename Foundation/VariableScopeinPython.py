globalName = 'Global'

def LocalVariable():
    name = 'John'
    print('Hello ', name)


def GlobalVariable():
    print('Hello ', globalName)
    


LocalVariable()
GlobalVariable()
# print(name) # NameError variable scope error