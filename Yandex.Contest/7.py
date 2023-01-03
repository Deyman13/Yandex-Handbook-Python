code = int(input())
interactor = int(input())
checker = int(input())
if interactor == 0 and code != 0:
    result = 3
elif interactor == 0 and code == 0:
    result = checker
if interactor == 1:
    result = checker
if interactor == 4 and code != 0:
    result = 3
elif interactor == 4 and code == 0:
    result = 4
if interactor == 6:
    result = 0
if interactor == 7:
    result = 1
if interactor == 2 or interactor == 3 or interactor == 5:
    result = interactor
print(result)




