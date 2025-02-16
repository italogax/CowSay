import os
import sys
import time

def cowsay(message):
    os.system('cls')
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
    
    time.sleep(1)
    cowsay(message)
    
    
    

