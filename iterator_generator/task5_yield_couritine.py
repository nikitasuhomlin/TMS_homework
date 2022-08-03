def finding_word(word):
    print('Ищем слово :', word)
    while True:
        wrd = (yield)
        if word in wrd:
            print(wrd)

if __name__ == '__main__':
    search = finding_word('Питон')
    next(search)
    search.send('Nick Suh')
    search.send('Что-то бомбезное')
    search.send('Я люблю Питон') 