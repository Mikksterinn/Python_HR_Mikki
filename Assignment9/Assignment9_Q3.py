file_input = input('Enter filename: ')
file_object = open(file_input, 'r')
str_max = 0
word_max = ''

for word in file_object:
    word = word.strip()
    if len(word) > str_max:
        str_max = len(word)
        word_max = word
word_max = '\''+word_max+'\''
print('Longest word is ', word_max, 'of length ', str_max)