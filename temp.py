from time import *

def internet(function):
    def wrapper(*args):
        print("Hello",args[0])
        function(*args)

    return wrapper

def cache(function):
    cacheData = set()
    def wrapper(name):
        if (name in cacheData):
            print("Already There!")
        else:
            sleep(2)
            cacheData.add(name)
            print(name, "Added!")
    return wrapper

# @internet
@cache
def hello(name):
    sleep(2)
    print("How are you?",name)


def main():
    hello("Nipun")
    # hello("Lucky")
    hello("sweshik")
    hello("Nipun")
    # hello("sweshik")



if __name__ == '__main__':
    main()