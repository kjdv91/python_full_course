#*args es una tupa de argumentos
def add(*args):
    sum =0

    for i in args:
        sum += i
    return sum

print(add(2,4,6))

# **kwargs


def hello(**kwargs):

    for key, value in kwargs.items():
        print(value,end=" ")

hello(name="Kevin", last_name = "Jaramillo")

