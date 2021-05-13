def browser(arg):
    return "Hi Dev!"+ str(arg)

def getData(func):
    print("hello")
    sum= 0
    for i in range(10):
        sum = sum + i
    v= func(sum)
    print(v)

getData(browser)

'''
clicked login -> gmail -> db(to get latest emails) ->


'''