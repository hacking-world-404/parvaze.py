from os import system as c
import time
import random

#------------- COLOUR ------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
 ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄ 
▐▌  ▐▌ ▄     ▀▄  ▀ ▄     ▐▌  ▐▌
▐▛▀▀▀▌ █ ▄▄▄  █     ▀▄▄▄ ▐▛▀▀▀▌
▐▌  ▐▌ ▀▄▄▄▀ ▄▄▀   ▀▄▄▄▀ ▐▌  ▐▌
{P} HACKING WORLD - FREE FIRE DIAMOND HACK VIP
""")

#------------- DIAMOND HACK -------------#
def diamond_hack():
    logo()
    c('espeak "Diamond Hack Starting"')
    uid = input(f"{Y}Enter Free Fire UID: ")

    print(f"\n{C}[+] Connecting to Garena Server...")
    time.sleep(2)
    print(f"{G}[✓] UID Verified: {uid}")
    time.sleep(1)

    print(f"{B}[+] Selecting Diamond Packages...\n")
    time.sleep(2)

    amounts = [500, 1000, 2000, 5000]
    for amount in amounts:
        print(f"{C}[*] Injecting {amount} Diamonds...")
        time.sleep(1.5)

    # Random problem message
    errors = [
        "[!] Server Connection Lost!",
        "[!] Account Session Expired!",
        "[!] Device Security Error Detected!",
        "[!] Invalid Packet Detected!",
        "[!] Unknown Server Error Occurred!"
    ]
    problem = random.choice(errors)
    print(f"\n{R}{problem}")
    time.sleep(2)
    print(f"{Y}[!] Please Restart Phone Or Try Again Later.\n")
    time.sleep(2)
    print(f"{R}[X] Connection Terminated.\n")
    time.sleep(1)

    input(f"{A}Press Enter To Exit...")

#------------- START TOOL -------------#
diamond_hack()