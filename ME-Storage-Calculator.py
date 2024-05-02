#Sserda
#ME-Storage-Calculator
#version 0.4

#Changelog 5/1/24 10:27pm
#Began additions for 4k components

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
    print("                                                                                                    version 0.4")
    print()
    print("Welcome to the ME Storage Calculator")
    print("Please select a mode.")
    print()
    print("1) Item Storage")
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
    print()
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

    if selection != "1k Storage Component":
        #Checks if crafting larger than 1k and displays the components you need to make beyond just materials
        print("Components:")
        print()
        print(f"1k Storage Components: {a}")
        if b > 0 and selection != "4k Storage Component":
            print(f"4k Storage Components: {b}")
        if c > 0 and selection != "16k Storage Component":
            print(f"16k Storage Components: {c}")
        print("---------------------------------------------------------")

    print("Materials: ")
    print()
    #Displays redstone if needed
    if redstone != 0:
        xr, yr = divmod(redstone, 64)
        print(f"Redstone:           {xr} Stack{'s'[:xr^1]}, {yr} Item{'s'[:yr^1]}")

    #Displays Quartz if Needed
    if quartz != 0:
        xq, yq = divmod(quartz, 64)
        print(f"Quartz:             {xq} Stack{'s'[:xq^1]}, {yq} Item{'s'[:yq^1]}")

    #Displays Logic Processors if needed
    if logicProc != 0:
        xLP, yLP = divmod(logicProc, 64)
        print(f"Logic Processor:    {xLP} Stack{'s'[:xLP^1]}, {yLP} Item{'s'[:yLP^1]}")

    #Displays Charged Quartz if needed
    if chargeQuartz != 0:
        xCQ, yCQ = divmod(chargeQuartz, 64)
        print(f"Charged Quartz:     {xCQ} Stack{'s'[:xCQ^1]}, {yCQ} Item{'s'[:yCQ^1]}")

    #Displays Iron if needed
    if iron != 0:
        xi, yi = divmod(iron, 64)
        print(f"Iron:               {xi} Stack{'s'[:xi^1]}, {yi} Item{'s'[:yi^1]}")

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
                            print("How many?")
                            a = int(input(""))
                            while a < 1:
                                print("Invalid input. Must be a number greater than 0.")
                                a = int(input(""))
                            redstone += (4*a)
                            quartz += (4*a)
                            logicProc += a
                            resultTable(target, a, 0, 0, 0, quartz, 0, 0, redstone, logicProc)

                        case "2":
                            target = "4k Storage Component"
                            print("How many?")
                            b = int(input(""))
                            while b < 1:
                                print("Invalid input. Must be a number greater than 0.")
                                b = int(input(""))
                            a = b * 3

                        case "3":
                            pass

                        case "4":
                            pass
                    select = storageMenu()
        mode = menu()

main()