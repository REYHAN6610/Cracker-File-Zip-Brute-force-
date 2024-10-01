#Coba perbaiki 10 Bug ini jika lo jago😂😂😂😂

def bug1():
    return "Hello" + 1

def bug2():
    def infinite_loop():
        return infinite_loop()
    return infinite_loop()

def bug3():
    def deep_recursion(n):
        return deep_recursion(n + 1)
    return deep_recursion(1)

def bug4():
    return 10 % 0

def bug5():
    def inner():
        return x
    x = 10
    return inner()

def bug6():
    with open('existing_file.txt', 'w') as f:
        f.write('Hello World')
    with open('existing_file.txt', 'r') as f:
        return f.read()

def bug7():
    my_set = set()
    my_set.add([])
    return my_set

def bug8():
    def len():
        return "This is not the length function"
    return len("Hello")

def bug9():
    my_tuple = (1, 2, 3)
    return my_tuple[3:]

def bug10():
    my_dict = {'a': 1, 'b': 2}
    return my_dict['c']

def main():

if __name__ == "__main__":
    main()