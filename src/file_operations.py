
def read_message_from_file():
    location = input("Enter the location of the txt file: ")
    with open(location,  'r') as file:
        message = file.read()    
    return message



def save_message_to_file(message, fileName):
    with open(fileName, 'w') as file:
        file.write(message)


