import zipfile
from tqdm import tqdm
import os
red = "\033[91m"
yellow = "\033[93m"
green = "\033[92m"
grey = "\033[90m"
white = "\033[0m"
os.system("clear")

print(red+'''\n\tWait Some Requirements are Installing''')

# Installing requirements(python, python2, tqdm).
os.system("apt update")
os.system("apt install python python2 python3 -y")
os.system("clear")
print(red+"Modified by:"+yellow+"\n "Truthful Hacker")
print(red+"Channel Link:"+yellow+"\n https://www.youtube.com/channel/UCSDy3gFrJn8l1UbwMaEyDww")

print(green+"\n\tYou are using ZipCracker Tool.\n")
#print("This tool will crack ZIP file,\nwhich has weak Password\nkeep patience this take a while.")

# The zip file you want to crack its password.
zip_file = input(red+"[+] Enter zip file path:->"+yellow+"\n:->\033[92m ")

# The password list path you want to use.
wordlist = input(red+"[+] Enter wordlist path:->"+yellow+"\n:->\033[92m ")

# Initialize the Zip File object.
zip_file = zipfile.ZipFile(zip_file)

# Count the number of words in this wordlist.
n_words = len(list(open(wordlist, "rb")))

# Print the total number of passwords.
print("Total passwords to test:", n_words)

# Cracking function.
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print(green+"\n\n[+] Password found:->\033[93m","[", word.decode().strip(),']\033[0m\n\n')
    
            exit(0)
print(red+"[!] Password not found, try other wordlist.\033[0m")
