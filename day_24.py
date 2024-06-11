# with open("name.txt", mode="w") as file:
#     file.write("My name is Yash.")

# with open("name.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("name.txt", "a") as file:
#     file.write("\nMy name is Ashwin.")
#     # print(contents)

# Writing letters for birthday Invitation

with open("./Input/Letters/starting_letter.txt") as file:
    full_content = file.read()
    # contents = file.readlines()
    # first_line = contents[0]


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        stripped_name = name.strip()
        # print(stripped_name)
        text = full_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as data:
            letter = data.write(text)
        # print(text)
# print(names)
