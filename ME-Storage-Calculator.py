#Sserda
#ME-Storage-Calculator
#version 0.4

#Changelog 5/1/24 10:27pm
#Began additions for 4k components
#Seperated raw materials and crafted materials
#Declared variables for missing resources
#Changed incorrect variables
#Refined variable parameter and printing order for better readability

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

def resultTable(selection, a, b = 0, c = 0, d = 0, quartz = 0, redstone = 0, gold = 0, silicon = 0, quartzGlass = 0, logicProc = 0):
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

    print("Crafted Materials: ")
    print()
    #Displays Logic Processors if needed
    if logicProc != 0:
        xLP, yLP = divmod(logicProc, 64)
        print(f"Logic Processor:    {xLP} Stack{'s'[:xLP^1]}, {yLP} Item{'s'[:yLP^1]}")
        print(f"    -Printed Logic Circuit [Gold]: {xLP} Stack{'s'[:xLP^1]}, {yLP} Item{'s'[:yLP^1]}")
        print(f"    -Printed Silicon [Silicon]:    {xLP} Stack{'s'[:xLP^1]}, {yLP} Item{'s'[:yLP^1]}")

    print("---------------------------------------------------------")

    print("Raw Materials: ")
    print()
    #Displays redstone if needed
    if redstone != 0:
        xr, yr = divmod(redstone, 64)
        print(f"Redstone:           {xr} Stack{'s'[:xr^1]}, {yr} Item{'s'[:yr^1]}")

    #Displays Quartz if Needed
    if quartz != 0:
        xq, yq = divmod(quartz, 64)
        print(f"Quartz:             {xq} Stack{'s'[:xq^1]}, {yq} Item{'s'[:yq^1]}")

    #Displays Gold if needed
    if gold != 0:
        xg, yg = divmod(gold, 64)
        print(f"Gold:               {xg} Stack{'s'[:xg^1]}, {yg} Item{'s'[:yg^1]}")

    #Displays Silicon if needed
    if silicon != 0:
        xS, yS = divmod(silicon, 64)
        print(f"Silicon:            {xS} Stack{'s'[:xS^1]}, {yS} Item{'s'[:yS^1]}")

    #Displays Quartz Glass if needed
    if quartzGlass != 0:
        xQG, yQG = divmod(quartzGlass, 64)
        print(f"Quartz Glass:       {xQG} Stack{'s'[:xQG^1]}, {yQG} Item{'s'[:yQG^1]}")



    input("Press enter to continue...")

def main():

    mode = menu()
    while mode != "EXIT":
        match mode:
            case "1":
                select = storageMenu()
                while select != "5":
                    #    Variable reset
                    a = 0              #1k
                    b = 0              #4k
                    c = 0              #16k
                    d = 0              #64k
                    quartz = 0         #Quartz (nether or otherwise; non charged)
                    redstone = 0       #Redstone
                    gold = 0           #Gold
                    silicon = 0        #Silicon
                    quartzGlass = 0    #Quartz Glass
                    glowstone = 0      #Glowstone Dust
                    diamonds = 0       #Diamonds
                    logicProc = 0      #Logic Processor
                    calculProc = 0     #Calculation Processor
                    engineerProc = 0   #Engineering Processor

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
                            gold = logicProc
                            silicon = logicProc
                            resultTable(target, a, 0, 0, 0, quartz, redstone, gold, silicon, 0, logicProc)

                        case "2":
                            target = "4k Storage Component"
                            print("How many?")
                            b = int(input(""))
                            while b < 1:
                                print("Invalid input. Must be a number greater than 0.")
                                b = int(input(""))
                            a = b * 3
                            resultTable(target, a, b, 0, 0, quartz, redstone, 0, 0, logicProc)

                        case "3":
                            pass

                        case "4":
                            pass
                    select = storageMenu()
        mode = menu()

main()