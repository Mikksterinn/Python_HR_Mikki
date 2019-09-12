# palindrome function definition goes here
def is_palindrome(sentence):

    sentence_clean=''

    for chr in sentence:
        if chr.isalpha():
            sentence_clean += chr
    
    sentence_clean = sentence_clean.lower()
    sentence_mirror = sentence_clean[::-1]
    return(sentence_clean,sentence_mirror)

in_str = input("Enter a string: ")
in_str = '\"'+in_str+'\"'
(clean,mirror) = is_palindrome(in_str)

if clean == mirror:
    print(in_str, ' is a palindrome.')
else:
    print(in_str, 'is not a palindrome.')

# call the function and print out the appropriate message