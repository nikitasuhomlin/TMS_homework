from pydoc import text


with open ('text.txt', 'w') as f:
    f.write('I am number one\n')
    f.write('I am number two\n')

    f.close()

with open('text.txt', 'a') as f:
    f.write('Added number three\n')
    f.write('Added number four\n')

    f.close()


    
    

