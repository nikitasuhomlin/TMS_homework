# letter = 'а'

# with open('parse.txt') as f:
#     for line in f:
#         for word in line.split():
#             if letter in word:
#                 if word.endswith(letter):
#                     print(word)
#                     #print(list(word))


letter = 'а'

with open('parse.txt') as f:
    f.read()
    
    def grep(pattern):
        print("Looking for %а%", pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line)


if __name__ == '__main__':
    search = grep('а')
    print(search)






    