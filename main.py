import os

# add in your phone number
phone_number = 0000000000 

def get_words(file_path):       
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text
    
def send_message(phoneNumber, message):
    os.system('osascript send.scpt {} "{}"'.format(phoneNumber, message))

def main():
    song = get_words('song.txt')
    for line in song:
        send_message(phone_number, line.strip())

if __name__ == '__main__':
    main()
