from time import sleep


def temp():
    for i in range(10, -1, -1):
        sleep(1)
        print(i)


temp()
