def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def grep(pattern):
    line = yield "I have to yield something here?"  # receive the first one
    while True:
        if pattern in line:
            line = yield line  # send and receive in one yield statement
        else:
            raise ValueError("err")

if __name__ == '__main__':
    g = grep('super')

    item = g.send('hot')
    print(item)
    next(g)

    item = g.send('super')
    print(item)
    next(g)

    item = g.send('hot')
    print(item)
    next(g)










# def finding_word(word):
#     print('Ищем слово :', word)
#     while True:
#         text = (yield)
#         if word in text:
#             print(text)

# if __name__ == '__main__':
#     search = finding_word('Питон')
#     next(search)
#     search.send('Nick Suh')
#     search.send('Что-то бомбезное')
#     search.send('Я люблю Питон') 