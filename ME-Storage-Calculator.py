#Sserda
#ME-Storage-Calculator
#version 0.1

#Changelog 5/1/24 6:21pm
#Added menu def
#Added exit condition to menu
#Added storage menu and switch case for each component

import os

def menu():
    os.system("cls")
    print("##   ##  #######             ####     ###    ####       ####   ##   ##  ####       ###     # #####  #####   ######   ")
    print("### ###   ##   #            ##  ##   ## ##    ##       ##  ##  ##   ##   ##       ## ##   ## ## ## ### ###   ##  ##  ")
    print("#######   ##               ##       ##   ##   ##      ##       ##   ##   ##      ##   ##     ##    ##   ##   ##  ##  ")
    print("## # ##   ####             ##       ##   ##   ##      ##       ##   ##   ##      ##   ##     ##    ##   ##   #####   ")
    print("##   ##   ##               ##       #######   ##      ##       ##   ##   ##      #######     ##    ##   ##   ## ##   ")
    print("##   ##   ##   #            ##  ##  ##   ##   ##  ##   ##  ##  ##   ##   ##  ##  ##   ##     ##    ### ###   ## ##   ")
    print("### ###  #######             ####   ##   ##  #######    ####    #####   #######  ##   ##    ####    #####   #### ##  ")
    print("                                                                                                    version 0.1")
    print()
    print("Welcome to the ME Storage Calculator")
    print("Please select a mode.")
    print()
    print("1) Item Storage")
    print()
    print("Type exit to close calculator")
    print()
    mode = input("").upper()
    while not mode in [1, "EXIT"]:
        mode = input("").upper()
    return mode

def storageMenu():
    os.system("cls")
    print("Storage ME Components")
    print("Please choose size of component")
    print("[1] 1k")
    print("[2] 4k")
    print("[3] 16k")
    print("[4] 64k")
    print("[5] Back")
    select = input("")
    while not select in [1, 2, 3, 4, 5]:
        select = input("")
    return select

def main():

    mode = menu()
    while mode != "EXIT":
        match mode:
            case "1":
                select = storageMenu()
                while select != 5:
                    match select:
                        case "1":
                            pass
                        case "2":
                            pass
                        case "3":
                            pass
                        case "4":
                            pass
        

main()