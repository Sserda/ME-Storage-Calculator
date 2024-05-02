#Sserda
#ME-Storage-Calculator
#version 0.1

#Changelog 5/1/24 6:21pm
#Added menu def
#Added exit condition to menu
#

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

def main():

    mode = menu()
    while mode != "EXIT":
        match mode:
            case "1":
                print("congrats")
        

main()