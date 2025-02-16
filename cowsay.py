import sys

def cowsay(message):

    print(f"""
        {message}
        \\
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
    """)

message = ""
for cont in range(1, len(sys.argv)):
    message += ' ' + str(sys.argv[cont])
    cowsay(message)