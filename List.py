with open("codecList.txt") as list:
    codecList = list.read()
    if 'bababoey' in codecList:
        print('string exists in file')
    else:
        print('your audio codec is currently not supported')
        print('=(')