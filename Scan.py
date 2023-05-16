import Main
with open("codecList.txt") as list:
    codecList = list.read()
    if '0257' in codecList:
        print('string exists in file')
    else:
        print('your audio codec is currently not supported')
        print('=(')