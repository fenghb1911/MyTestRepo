import platform
import datetime
# from mymodule import person1
import math
import json

def showPlatform():
    x = platform.system()
    print(x)

def BubbleSort1A(arr, n):
    isSorted = False
    while not isSorted:
        isSorted = True
        # i = 1
        # while i < n:
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                tmp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = tmp
                isSorted = False
            # i += 1
        n -= 1

if __name__ == "__main__":
    #----------------1 BubbleSort----------------
    # arr = [ 5, 2, 7, 4, 6, 3, 1 ]
    # print('before:')
    # for v in arr:
    #     print(v)
    # BubbleSort1A(arr, len(arr))
    # print('after:')
    # for v in arr:
    #     print(v)
    #----------------2 ----------------
    showPlatform()
    x = dir(platform)
    print(x)
    #----------------3----------------
    # _tmp = __import__('mymodule')
    # print(_tmp.person1["age"])
    #----------------4 datetime----------------
    # x = datetime.datetime.now()
    # print(x.strftime("%Y.%m.%d %H:%M:%S"))
    # print(x.strftime("%x %X"))
    #----------------5 math----------------
    # x = min(5, 10, 25)
    # y = max(5, 10, 25)
    # print(x)
    # print(y)
    #----------------6 json----------------
    # x = {
    #     "name": "John",
    #     "age": 30,
    #     "married": True,
    #     "divorced": False,
    #     "children": ("Ann","Billy"),
    #     "pets": None,
    #     "cars": [
    #         {"model": "BMW 230", "mpg": 27.5},
    #         {"model": "Ford Edge", "mpg": 24.1}
    #     ]
    # }
    # # print(json.dumps(x))
    # # print(json.dumps(x, indent=4))
    # # print(json.dumps(x, indent=4, separators=(". ", " = ")))
    # print(json.dumps(x, indent=4, sort_keys=True))
    #----------------7 string format----------------
    # quantity = 3
    # itemno = 567
    # price = 49
    # myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    # print(myorder.format(quantity, itemno, price))
    # myorder = "I have a {carname}, it is a {model}."
    # print(myorder.format(carname = "Ford", model = "Mustang"))