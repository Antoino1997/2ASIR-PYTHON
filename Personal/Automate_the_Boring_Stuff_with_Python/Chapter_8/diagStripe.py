import time

while True:
    for i in range(50):
        print('O' * i + '.' * (50 - i))
        time.sleep(0.01)

    for i in range(50):
        print('.' * i + 'O' * (50 - i))
        time.sleep(0.01)