import os.path
import time
import random

from PassGen import *
from Phone import *


def generate_random_int():
    return random.randint(1, 2)


def banner_menu(random_number):
    if os.path.exists('banner1.txt') and os.path.exists('banner2.txt'):
        with open(f'banner{random_number}.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line.strip('\n'))
                time.sleep(0.30)
    else:
        print('[!] Banner/(s) text file not found... Proceeding...')

    print('(1) Get Phone Number Information')
    print('(2) Generate a secure password')
    print('(99) Exit the program\n')


def validate_answer(prompt):
    while True:
        choice = input(prompt).strip().lower()
        possible_choices = ['y', 'n']

        if choice in possible_choices:
            return choice
        print("[!] Invalid input... Please enter y/n")


def passgen_options():
    print('[!] Gathering required informations...')
    print('[!] NOTE: AT LEAST 2 OF THE FOLLOWING CHARACTER SETS MUST BE CHOSEN.')

    digits = validate_answer("Use numbers (y/n): ")
    letters = validate_answer("Use letters (y/n):")
    punct = validate_answer("Use special characters (y/n): ")

    while True:
        try:
            length = int(input('Password length (default 6): '))
            if length < 6:
                print('Password must be at least 6 characters!')
            else:
                return digits, letters, punct, length
        except ValueError:
            print('[!] Invalid length... Please enter a number greater than 6')


def receive_phone_input():
    phone_no = input('Enter the phone number (+1123456789): ')
    return phone_no


def phone_info():
    lookup_phone = receive_phone_input()
    phone_to_search = Phone(lookup_phone)
    print(f'{phone_to_search.get_information()}')


def password_generation():
    try:
        digits, letters, punct, length = passgen_options()
        passgen_obj = PassGen(digits, letters, punct, length)
        generated_password = passgen_obj.generate_password()
        print(f'[*] Generated Password: {generated_password}')
    except Exception as e:
        print(f'Error generating password... Error: {e}')


def main():
    random_number = generate_random_int()
    banner_menu(random_number)

    while True:
        choice = input('Choose an option (1/2/99): ').strip()
        if choice == '1':
            phone_info()
        elif choice == '2':
            password_generation()
        elif choice == '99':
            print('Goodbye user...')
            break
        else:
            print('[!] Invalid choice... Please try again...')


if __name__ == '__main__':
    main()
