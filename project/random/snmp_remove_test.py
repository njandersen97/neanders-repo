import types

class classA:
    def return_test(self):
        return True, 'rolback_commands'

class classB:
    def return_test(self):
        return (True, )

class classB2:
    def return_test(self):
        return True

def test_class(obj):
    return_test = obj.return_test()
    return_value = return_test
    return return_value[0]

def test_class2(obj):
    return_test = obj.return_test()
    return_value = return_test if type(return_test) == bool else return_test[0]
    return return_value

def main():
    print("Testing Method 1")
    print("Testing ClassA - Method1")
    objA = classA()
    testA = test_class(objA)
    print(testA)
    print("Testing ClassB - Method1")
    objB = classB()
    testB = test_class(objB)
    print(testB)
    if testA == testB:
        print("Method 1 succceds")

def main2():
    print("Testing Method 2")
    print("Testing ClassA - Method2")
    objA = classA()
    testA = test_class2(objA)
    print(testA)
    print("Testing ClassB - Method2")
    objB = classB2()
    testB = test_class2(objB)
    print(testB)
    if testA == testB:
        print("Method 2 succceds")


if __name__ == "__main__":
    main()
    main2()