#Sserda
#ME-Storage-Calculator
#version 0.2

#Changelog 5/1/24 9:15pm
#Added menu def
#Added exit condition to menu
#Added storage menu and switch case for each component
#Added result() and added basic target recognition
#Added processing to switch case in main()
#Refined exit conditions to menus

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
    while not mode in ["1", "EXIT"]:
        mode = input("Invalid mode: ").upper()
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
    while not select in ["1", "2", "3", "4", "5"]:
        select = input("Invalid selection: ")
    return select

def resultTable(selection, a, b = 0, c = 0, d = 0, quartz = 0, chargeQuartz = 0, iron = 0, redstone = 0, logicProc = 0):
    os.system("cls")
    if selection == "1k Storage Component":
        if a != 1:
            print(f"Target: {a}x {selection}s")
        else:
            print(f"Target: {a}x {selection}")
    if selection == "4k Storage Component":
        if b != 1:
            print(f"Target: {b}x {selection}s")
        else:
            print(f"Target: {b}x {selection}")
    if selection == "16k Storage Component":
        if c != 1:
            print(f"Target: {c}x {selection}s")
        else:
            print(f"Target: {c}x {selection}")
    if selection == "64k Storage Component":
        if d != 1:
            print(f"Target: {d}x {selection}s")
        else:
            print(f"Target: {d}x {selection}")
    print("---------------------------------------------------------")
    input("Press enter to continue...")

def main():

    a = 0              #1k
    b = 0              #4k
    c = 0              #16k
    d = 0              #64k
    quartz = 0         #Quartz (nether or otherwise; non charged)
    chargeQuartz = 0   #Charged Quartz
    iron = 0           #Iron
    redstone = 0       #Redstone
    logicProc = 0      #Logic Processor

    mode = menu()
    while mode != "EXIT":
        match mode:
            case "1":
                select = storageMenu()
                while select != "5":
                    match select:
                        case "1":
                            target = "1k Storage Component"
                            a = int(input("How many?: "))
                            while a < 1:
                                print("Invalid input. Must be a number greater than 0.")
                                a = int(input("How many?: "))
                            redstone += (4*a)
                            quartz += (4*a)
                            logicProc += a
                            resultTable(target, a, 0, 0, 0, quartz, 0, 0, redstone, logicProc)

                        case "2":
                            pass

                        case "3":
                            pass

                        case "4":
                            pass
                    select = storageMenu()
        mode = menu()

main()