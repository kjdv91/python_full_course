try:
    with  open('hello.txt') as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)