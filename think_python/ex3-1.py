def right_justify(value):
    print(((70 - (len(value))) * ' ') + value)
    print(len(((70 - (len(value))) * ' ') + value))

right_justify('california girls!!!!!')