from datetime import datetime as dt
import time
import os
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
lcd.clear()

def lcd_display(line1, line2, line3, line4):
	lcd.clear()
	lcd.write_string(line1)
	lcd.cursor_pos = (1, 0)
	lcd.write_string(line2)
	lcd.cursor_pos = (2, 0)
	lcd.write_string(line3)
	lcd.cursor_pos = (3, 0)
	lcd.write_string(line4)
    
def hult_intro():
    line1 = "Hello Hultians!"
    line2 = "Let's take the text"
    line3 = "adventure game to"
    line4 = "the next level."
    lcd_display(line1, line2, line3, line4)
    time.sleep(3)
    lcd.clear()

def display_intro():
    # ascii_art = [
        # " _                   ",
        # "|_| |  _  _| _| o __ ",
        # "| | | (_|(_|(_| | | |",
        # "                     ",
    # ]
    logo_line_1 = " _                  "
    logo_line_2 = "|_| |  _  _| _| o _ "
    logo_line_3 = "| | | (_|(_|(_| || |"
    logo_line_4 = "                    "
    lcd_display(logo_line_1, logo_line_2, logo_line_3, logo_line_4)
    time.sleep(2)
    lcd.clear()
    
    intro_line_1 = "Welcome to Aladdin"
    intro_line_2 = "Adventure!"
    intro_line_3 = "Guide Aladdin to"
    intro_line_4 = "rescue Jasmine."
    lcd_display(intro_line_1, intro_line_2, intro_line_3, intro_line_4)
    time.sleep(3)
    lcd.clear()

    # intro_text = [
        # "Welcome to Aladdin",
        # "Adventure!",
        # "Guide Aladdin to",
        # "rescue Jasmine."
    # ]

    # print("\n".join(ascii_art))
    # input("Press Enter to continue...")

    # for line in intro_text:
        # print(line)
    lcd_display("Press Enter", "to start...", "", "")
    input("Press Enter to start...")

def display_message(message):
    print("\n" + "\n".join(message.split('\n')))

def handle_input():
    game_state = {
        'location': 'start',
        'steps': 0
    }

    while True:
        location = game_state['location']

        if location == 'start':
            lcd_display("1: Start Adventure", "2: Exit", "", "")
            choice = input("1: Start Adventure\n2: Exit\n")
            if choice == '1':
                game_state['location'] = 'marketplace'
                game_state['steps'] += 1
            elif choice == '2':
                lcd_display("Goodbye!", "","","")
                print("Goodbye!")
                break

        elif location == 'marketplace':
            lcd_display("In marketplace.","1: Steal bread", "2: Leave","")
            display_message("In marketplace.\n1: Steal bread\n2: Leave")
            choice = input()
            if choice == '1':
                game_state['location'] = 'guards'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'guards':
            lcd_display("IGuards chase you.","1: Run", "2: Fight","")
            display_message("Guards chase you.\n1: Run\n2: Fight")
            choice = input()
            if choice == '1':
                game_state['location'] = 'jasmine'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'jasmine':
            lcd_display("Meet Jasmine.","1: Talk","2: Ignore","")
            display_message("Meet Jasmine.\n1: Talk\n2: Ignore")
            choice = input()
            if choice == '1':
                game_state['location'] = 'cave'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'cave':
            lcd_display("Enter cave.","1: Explore","2: Leave","")
            display_message("Enter cave.\n1: Explore\n2: Leave")
            choice = input()
            if choice == '1':
                game_state['location'] = 'lamp'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'lamp':
            lcd_display("Find magic lamp.","1: Rub lamp","2: Ignore","")
            display_message("Find magic lamp.\n1: Rub lamp\n2: Ignore")
            choice = input()
            if choice == '1':
                game_state['location'] = 'genie'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'genie':
            lcd_display("Genie appears.","1: Wish","2: No wish","")
            display_message("Genie appears.\n1: Wish\n2: No wish")
            choice = input()
            if choice == '1':
                game_state['location'] = 'palace'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'palace':
            lcd_display("Return to palace.","1: Confront Jafar","2: Avoid","")
            display_message("Return to palace.\n1: Confront Jafar\n2: Avoid")
            choice = input()
            if choice == '1':
                game_state['location'] = 'jafar'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'jafar':
            lcd_display("Fight Jafar.","1: Use magic","2: Sword","")
            display_message("Fight Jafar.\n1: Use magic\n2: Sword")
            choice = input()
            if choice == '1':
                game_state['location'] = 'victory'
                game_state['steps'] += 1
            elif choice == '2':
                game_state['location'] = 'fail'
                game_state['steps'] += 1

        elif location == 'victory':
            lcd_display("You Win!","Jafar defeated.","1: Quit","1: Restart")
            display_message("Jafar defeated!\n1: Quit\n2: Restart")
            choice = input()
            if choice == '1':
                lcd_display("Well Done Aladdin!", "Goodbye.","","")
                print("Well done Aladdin! Goodbye.\n")
                break
            elif choice == '2':
                game_state['location'] = 'start'
                game_state['steps'] = 0

        elif location == 'fail':
            lcd_display("Game Over","1: Restart","","")
            display_message("Game Over\n1: Restart")
            choice = input()
            if choice == '1':
                game_state['location'] = 'start'
                game_state['steps'] = 0

if __name__ == '__main__':
    # display_intro()
    # handle_input()
    time.sleep(10)
    hult_intro()
    display_intro()
    handle_input()
    
