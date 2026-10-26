# ask users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File Type: ").lower()

        # check for 'i' or exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check if it's an image
        elif response in ['text', 'txt', 't']:
            return "text"

        else:
            print("Please enter a valid file type")
            return None


# main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}\n")

    if file_type == "xxx":
        break