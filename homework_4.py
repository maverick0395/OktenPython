try:
    with open('./emails.txt', 'r') as file:
        for line in file:
            match line.split('@'):
                case [_, 'gmail.com\n']:
                    with open('./gmails.txt', 'a') as new_file:
                        new_file.write(line)
                case _:
                    pass

except FileNotFoundError:
    print("File not found")

except Exception as err:
    print(err)


