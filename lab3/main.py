from SerizDeseriz_IGI import SerializerFactory


def int_wrap_decor(func):
    def wrapper(arg):
        if isinstance(arg, int):
            arg += 3
            print(arg)
        else:
            print("I am not int")
        return func(arg)

    return wrapper

@int_wrap_decor
def check_int(maybe_int):
    print("Passed value = " + str(maybe_int))

check_int(5)
check_int("blablabla")

def my_decor(func):
    def inner(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)
    return inner

class A:
    @my_decor
    def my_method(self):
        return 145
class B:
    pass

class C(A, B):
    pass


serializer = SerializerFactory.create_serializer("JSON")

ser = serializer.dumps(C)

des = serializer.loads(ser)

