# DEVELOPER BY @REDX_64

import os
import time
import smtplib
import ssl
from email.message import EmailMessage
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Initialize colorama and dotenv
init(autoreset=True)
load_dotenv()
# DEVELOPER BY @REDX_64
perm_file = "perm_ban.txt"
temp_file = "temp_ban.txt"

sender_email = os.getenv('sasisose24@gmail.com')
password = os.getenv('785797114@')

support_emails = [
    "support@whatsapp.com",
    "abuse@support.whatsapp.com",
    "privacy@support.whatsapp.com",
    "terms@support.whatsapp.com",
    "accessibility@support.whatsapp.com"
]


def banner():
    print(f"{Fore.CYAN}\n== 🕸️ 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 𝐑𝐄𝐃-𝐗 🕸️==={Style.RESET_ALL}")
    print(Fore.YELLOW + r"""
   ⣴⣾⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣉⣩⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣼⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷
⢠⣾⣿⣿⠉⣿⣿⣿⣿⣿⡄⠀⢀⣠⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠙⣿⣿⣧⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀
⠀⠀⠀⠀⠘⠿⢿⣿⣿⣿⣿⡄⠙⠻⠿⠿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡟⣩⣝⢿⠀⠀⣠⣶⣶⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣷⡝⣿⣦⣠⣾⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣮⢻⣿⠟⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠻⠿⠻⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿
⠀ ⠀⠀. ⢸⣿⣿⡿⠀⠀⠀⢀⣴⣿⣿⣿⣿⣟⣋⣁⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⠇⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛
""" + Style.RESET_ALL)
 # DEVELOPER BY @REDX_64
def is_banned(number):
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            if number in f.read():
                return "permanent"
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                if line.startswith(number + ","):
                    unban_time = int(line.strip().split(",")[1])
                    if time.time() < unban_time:
                        return "temporary"
    return None

def simulate_reports(number, total):
    print(f"\n⚙️ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 {total} 𝗕𝗮𝗻 𝗳𝗼𝗿 {number}...")
    for i in range(1, total + 1):
        print(f"{Fore.RED}☠️ 𝗦𝗲𝗻𝗱𝗶𝗻𝗴 𝗔𝘁𝘁𝗮𝗰𝗸 𝘁𝗼 {number} 𝗔𝗺𝗼𝘂𝗻𝘁 {i}")
        time.sleep(0.05)
    print(f"{Fore.GREEN}✅ {total} 𝗕𝗮𝗻 𝘄𝗮𝘀 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱👌💯 𝗼𝗻 𝗧𝗮𝗿𝗴𝗲𝘁🎯 {number}.")

def save_perm_ban(number):
    with open(perm_file, "a") as f:
        f.write(number + "\n")

def save_temp_ban(number, duration):
    unban_time = int(time.time() + duration)
    with open(temp_file, "a") as f:
        f.write(f"{number},{unban_time}\n")

def check_temp_expiry():
    if not os.path.exists(temp_file):
        return
    with open(temp_file, "r") as f:
        lines = f.readlines()
    active = []
    for line in lines:
        number, unban_time = line.strip().split(",") # DEVELOPER BY @REDX_64
        if time.time() < int(unban_time):
            active.append(line)
        else:
            print(f"{Fore.GREEN}✅ 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗯𝗮𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 𝗳𝗼𝗿 {number}.")
    with open(temp_file, "w") as f:
        f.writelines(active)

def ban_permanent():
    number = input("🐍𝗘𝗻𝘁𝗲𝗿 𝗧𝗮𝗿𝗴𝗲𝘁🎯 𝗡𝘂𝗺𝗯𝗲𝗿: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}❌ {number} 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 {is_banned(number)} 𝗯𝗮𝗻𝗻𝗲𝗱.")
        return
    confirm = input(f"⚠️ 𝗔𝗿𝗲 𝘆𝗼𝘂 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗽𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁𝗹𝘆 𝗯𝗮𝗻 {number}? (𝗬/𝗡): ").strip().lower()
    if confirm != 'y':
        print("❌ 𝗔𝗰𝘁𝗶𝗼𝗻 𝗰𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱.")
        return # DEVELOPER BY @REDX_64
    try:
        reports = int(input("🐛 𝗘𝗻𝘁𝗲𝗿 𝗔𝗺𝗼𝘂𝗻𝘁: "))
    except ValueError:
        print("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗶𝗻𝗽𝘂𝘁.")
        return
    simulate_reports(number, reports)
    save_perm_ban(number)
    print(f"{Fore.RED}🚫 𝗡𝘂𝗺𝗯𝗲𝗿 {number} 𝗪𝗶𝗹𝗹 𝗯𝗲  𝗽𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁𝗹𝘆 𝗕𝗮𝗻𝗻𝗲𝗱 𝗦𝗵𝗼𝗿𝘁𝗹𝘆 𝗦𝘁𝗮𝘆 𝘁𝘂𝗻𝗲𝗱.")
    reason = "This Number Have Been Stealing and scamming People On WhatsApp, destroying people WhatsApp account, sending negative Text, spamming virus, Sending nudes to different people on WhatsApp please He his Going against the Community guidelines please disable the account from using WhatsApp He hacked My Number and start using it to scam people Online And he his very dangerous Sending Different videos and pictures especially Nudes or sex stuff, please i beg of you WhatsApp support team work together and disable this number from Violating WhatsApp please, He is a Fraud, scammer,Thief, Sending spam messages, text viruses, And many of all negative attitude Please disable the account permanently from using WhatsApp account again he will continue doing so if yoi guy's didn't take action on time. Thank you"
    send_report_email(number, reason, reports)
    # DEVELOPER BY @REDX_64

def ban_temporary():
    number = input("🐊𝗘𝗻𝘁𝗲𝗿 𝗧𝗮𝗿𝗴𝗲𝘁🎯 𝗡𝘂𝗺𝗯𝗲𝗿: ").strip()
    if is_banned(number):
        print(f"{Fore.RED}❌ {number} 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 {is_banned(number)} 𝗯𝗮𝗻𝗻𝗲𝗱.")
        return
    confirm = input(f"⚠️ 𝗔𝗿𝗲 𝘆𝗼𝘂 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗯𝗮𝗻 {number}? (𝗬/𝗡): ").strip().lower()
    if confirm != 'y':
        print("❌ 𝗔𝗰𝘁𝗶𝗼𝗻 𝗰𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱.")
        return
    try:
        minutes = int(input("⏳𝗘𝗻𝘁𝗲𝗿 𝗕𝗮𝗻 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻 (𝗶𝗻 𝗺𝗶𝗻𝘂𝘁𝗲𝘀): "))
        reports = int(input("🔢 𝗘𝗻𝘁𝗲𝗿 𝗮𝗺𝗼𝘂𝗻𝘁: "))
    except ValueError:
        print("❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗶𝗻𝗽𝘂𝘁.")
        return
    simulate_reports(number, reports)
    save_temp_ban(number, minutes * 60)
    print(f"{Fore.YELLOW}⏳ {number} 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗯𝗮𝗻𝗻𝗲𝗱 𝗳𝗼𝗿 {minutes} minutes.")
    reason = f"This Number will Be Disable for some {minutes} Minutes because he Have Been Stealing and scamming People On WhatsApp, destroying people WhatsApp account, sending negative Text, spamming virus, Sending nudes to different people on WhatsApp please He his Going against the Community guidelines please disable the account from using WhatsApp He hacked My Number and start using it to scam people Online And he his very dangerous Sending Different videos and pictures especially Nudes or sex stuff, please i beg of you WhatsApp support team work together and disable this number from Violating WhatsApp please, He is a Fraud, scammer,Thief, Sending spam messages, text viruses, And many of all negative attitude Please disable the account permanently from using WhatsApp account again he will continue doing so if yoi guy's didn't take action on time. Thank you"
    send_report_email(number, reason, reports)

def unban_permanent():
    number = input(f"{Fore.YELLOW}📱 𝗘𝗻𝘁𝗲𝗿 𝗻𝘂𝗺𝗯𝗲𝗿 𝘁𝗼 𝗨𝗡𝗕𝗔𝗡 𝗳𝗿𝗼𝗺 𝗽𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁: ").strip()
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            lines = f.readlines()
        with open(perm_file, "w") as f:
            for line in lines:
                if line.strip() != number:
                    f.write(line)
        print(f"{Fore.GREEN}✅ {number} 𝘂𝗻𝗯𝗮𝗻𝗻𝗲𝗱 𝗳𝗿𝗼𝗺 𝗽𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁.")

def unban_temporary():
    number = input(f"{Fore.YELLOW}📱 𝗘𝗻𝘁𝗲𝗿 𝗻𝘂𝗺𝗯𝗲𝗿 to 𝗨𝗡𝗕𝗔𝗡 𝗳𝗿𝗼𝗺 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆: ").strip()
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            lines = f.readlines()
        with open(temp_file, "w") as f:
            for line in lines:
                if not line.startswith(number + ","):
                    f.write(line)
        print(f"{Fore.GREEN}✅ {number} 𝘂𝗻𝗯𝗮𝗻𝗻𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆.")
        
def send_report_email(target_number, reason, count):
    context = ssl.create_default_context()
    for i in range(count):
        msg = EmailMessage()
        msg['Subject'] = f"Report of WhatsApp Account (Attempt {i+1})"
        msg['From'] = sender_email
        msg['To'] = ", ".join(support_emails)
        msg.set_content(f"""Hello WhatsApp Support,

I would like to report the following WhatsApp number:

📱 Number: {target_number}
📝 Reason: {reason}

please take action immediately 
Thank you.
""")
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)
            print(f"✅ 𝗕𝗮𝗻 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 {i+1}/{count} 𝘀𝗲𝗻𝘁 𝘁𝗼 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽")
        except Exception as e:
            print(f"❌ 𝗕𝗮𝗻 𝗳𝗮𝗶𝗹𝗲𝗱 {i+1} 𝗳𝗮𝗶𝗹𝗲𝗱: {e}") # DEVELOPER BY @REDX_64
            break
            
def view_banned():
    print(f"\n{Fore.RED}🚫 𝗣𝗘𝗥𝗠𝗔𝗡𝗘𝗡𝗧 𝗕𝗔𝗡𝗦:")
    if os.path.exists(perm_file):
        with open(perm_file, "r") as f:
            print(f.read().strip() or "None")
    else:
        print("𝗡𝗼𝗻𝗲")

    print(f"\n{Fore.MAGENTA}⏳ 𝗧𝗘𝗠𝗣𝗢𝗥𝗔𝗥𝗬 𝗕𝗔𝗡𝗦:")
    if os.path.exists(temp_file):
        with open(temp_file, "r") as f:
            for line in f:
                number, unban_time = line.strip().split(",") # DEVELOPER BY @REDX_64
                remaining = int(unban_time) - int(time.time())
                if remaining > 0:
                    mins = remaining // 60
                    print(f"{number} — {mins} min left")
    else:
        print("𝗡𝗼𝗻𝗲")

# DEVELOPER BY @REDX_64
while True:
    check_temp_expiry()
    banner()
    print(f"{Fore.BLUE}1️⃣  𝗕𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁")
    print(f"{Fore.BLUE}2️⃣  𝗕𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{Fore.BLUE}3️⃣  𝗨𝗻𝗯𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁")
    print(f"{Fore.BLUE}4️⃣  𝗨𝗻𝗯𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{Fore.BLUE}5️⃣  𝗩𝗶𝗲𝘄 𝗕𝗮𝗻𝗻𝗲𝗱 𝗡𝘂𝗺𝗯𝗲𝗿𝘀")
    print(f"{Fore.BLUE}6️⃣  𝗘𝘅𝗶𝘁")

    choice = input(f"\n{Fore.RED}👉 𝗖𝗵𝗼𝗼𝘀𝗲 𝗮𝗻 𝗼𝗽𝘁𝗶𝗼𝗻 [𝟭-𝟲]: ").strip()

    if choice == "1":
        ban_permanent() # DEVELOPER BY @REDX_64
    elif choice == "2":
        ban_temporary()
    elif choice == "3":
        unban_permanent()
    elif choice == "4":
        unban_temporary()
    elif choice == "5":
        view_banned()
    elif choice == "6":
        print(f"{Fore.CYAN}👋 𝗘𝘅𝗶𝘁𝗶𝗻𝗴. 𝗦𝘁𝗮𝘆 𝘀𝗮𝗳𝗲, 𝐑𝐄𝐃-𝐗 𝗛𝗮𝗰𝗸𝗲𝗿!")
        break
    else:
        print(f"{Fore.RED}❌ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗵𝗼𝗶𝗰𝗲.")

    time.sleep(1)
