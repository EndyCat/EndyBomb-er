import requests
import services
import os
from colorama import *
init()
# Вверх
try:
	os.system('cls')
except:
	os.system('clear')
print(Fore.GREEN + '''███████╗███╗░░██╗██████╗░██╗░░░██╗██████╗░░█████╗░███╗░░░███╗██████╗░
██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗████╗░████║██╔══██╗
█████╗░░██╔██╗██║██║░░██║░╚████╔╝░██████╦╝██║░░██║██╔████╔██║██████╦╝
██╔══╝░░██║╚████║██║░░██║░░╚██╔╝░░██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
███████╗██║░╚███║██████╔╝░░░██║░░░██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░''')
print(Fore.YELLOW)
# вводы
print(Fore.YELLOW + 'Введи номер без кода. Пример(9699923455)')
input_number = input(">> ")
print(Fore.MAGENTA + 'Сколько нужно смс?')
sms = int(input(Fore.RED + ">> "))





def parse_number(number):
	msg = Fore.GREEN + "Правильность номера - OK"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(Fore.RED + "Номер введён не правильно. Ввиди номер без 7+ или 8")
		quit()
	return number
number = parse_number(input_number)



services.attack(number, sms)
