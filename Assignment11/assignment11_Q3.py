def get_emails():
    email_input = input('Email address: ')
    email_list = []
    while email_input != 'q':
        email_list.append(email_input)
        email_input = input('Email address: ')
    return email_list

def get_names_and_domains(email_list):
    names_and_domains = []
    for val in email_list:
        #user, domain = val.rsplit('@', 1)
        names_and_domains.append(tuple(val.split('@')))
    return names_and_domains

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)