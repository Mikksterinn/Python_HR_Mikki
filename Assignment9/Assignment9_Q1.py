def open_file(filename):
    file_object = open(filename, 'r')
    return file_object

def read_file(file_object):
    string = ''
    for line in file_object:
        line = line.strip().replace(' ','')
        string += line
    #string = string.replace(' ','')
    return string


file_object = open_file('test.txt')
string = read_file(file_object)
print(string)