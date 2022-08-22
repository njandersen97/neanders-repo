import time
import random
poll_time = 5

def do_thing():
    n = (bool(random.randint(0,1)))
    print(n)
    return(n)

def test_poll():
    completed = False
    while not completed:
        time.sleep(poll_time)
        try:
            do_thing()
            print('still polling')
        except Exception as e:
            print(e)

test_poll()