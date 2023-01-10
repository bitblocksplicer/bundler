import os
import platform
from collections import Counter
import logging

logging.basicConfig(filename="debug.log", filemode= "w", format="%(asctime)s - %(message)s",level=logging.ERROR)
def clearing(): #clears the screen based on the OS.
    if platform.system() == "Linux":
        return os.system("clear")
    else:
        return os.system("cls")
        
allcodes = list()
categories = list() #includes before the ':' things in the list. not duplicates. It will be useful to create lists for each of them and iterate to append items.
counts = dict() #this dictionary has category names with its counts. it's just for information print and getting the category which has the least codes in order to get maximum number of bundles.
dct = dict() #this dictionary will have lists that includes codes for each category.
custommodelist = dict() # this dictionary includes how much codes will be included in each category in each bundle.
flag = list() #it will include "True" if custommode enabled. Else, it will be empty. Basically it's a list for checking purposes.
findthemaxforcust = list() #list to find "at most" bundle count by using min() method.
def getcategories(): #gets categories from before the ":" thing and adds them to categories list
    global categories
    for i in allcodes:
        splitted = i.split(":")[0] #splitting the lines with ":" and geting the first element of it
        categories.append(splitted) #adding to categories list.
    counts.update(Counter(categories))
    try:
        counts.pop("\n")
    except Exception as err:
        logging.debug(err) 
        pass 
    categories = list(dict.fromkeys(categories)) #removing the duplicates in categories list.

def createlists(): #adds lists to dct dictionary
    for i in categories:
        dct[i] = []

def addingtodct(counter): #adds codes to lists in dct dictionary
    for y in allcodes: #for each element of the list that includes each line of the readed file
        if categories[counter] in y: #if that element includes at this index of category element
            dct[categories[counter]].append(y)
        else:
            pass
            

def creatingbundles():
    filename = input("Bundled filename    :")
    line = "-"*10
    if True in flag:
        file2 = open(f"{str(filename)}.txt", "w")
        for i in categories:
            try:
                findthemaxforcust.append(int(len(dct[i])/custommodelist[i]))
            except Exception as err:
                logging.error(err)
                pass
        try:
            maxforcust = min(findthemaxforcust)
        except Exception as err:
            logging.error(err)
        input("Based on your selections, I can create at most {} bundles.".format(maxforcust))
        for i in range(maxforcust): #bundle count
            print(line)
            file2.write(str(line))
            file2.write("\n")
            for y in range(len(categories)): #categories in bundle count
                try:
                    for z in range(custommodelist[categories[y]]): #lines in bundle count
                        print(dct[categories[y]][0],end="") #bundles printing on terminal
                        file2.write(str(dct[categories[y]][0])) #bundles saving into the file
                        dct[categories[y]].pop(0) #and removing after saved into the file.
                except Exception as err:
                    logging.error(err)
                    pass
        file2.close()
        if not unbundledemptycheck() == False:
            print("Remaining codes exported as UNBUNDLED.txt to the same directory")
        else:
            print("No files created because there are no code left for unbundled file.")
        input("Sounds cool. Exit app: [Enter]    ")
        exit()
        
    else:
        for i in range(len(categories)*2):
            try:
                categories.pop(categories.index("\n"))
            except ValueError as err:
                logging.error(err)
                pass
        file2 = open("{}.txt".format(str(filename)),"w")
        for i in range(min(counts.values())):
            line = "-"*10
            print(line)
            file2.write(str(line))
            file2.write("\n")
            for y in range(len(categories)):
                print(dct[categories[y]][i],end="")
                file2.write(str(dct[categories[y]][i]))
        file2.close()
        print("\n")
        print("Bundle creating completed. {}.txt file was saved to the same directory.".format(filename))
    
def getremainings(num):
    maxbundlenum = min(counts.values())
    codelist = dct[categories[num]]
    if len(codelist) == maxbundlenum:
        codelist.clear()
    else:
        for i in range(maxbundlenum):
            codelist.pop(0)

def listeleme(): #Prints how many codes in categories, and asks to enter custom mode.
        print("-"*10)
        for i in counts.items():
            print(i[0],"-","x{}".format(i[1]))
        try:
            print("\n", f"It means I can create at most {min(counts.values())} bundles.")
        except:
            input("You didn't choose any file. [Enter] to return main menu.")
            return False
        print("-"*10)
        whatdoyoudo = input("""
[Enter] to continue
[C] to custom selection mode

Input   :""")
        if not whatdoyoudo:
            pass
        elif whatdoyoudo == "c" or whatdoyoudo == "C":
            custommode()


def multiplefiles(): #function to show the main file selection screen.
    multipfiles = list()
    clearing()
    print("The list of files in this dir:")
    arr = os.listdir(".")
    for i in enumerate(arr):
        print("[",i[0],"]",i[1])
    while True:
        clearing()
        for i in enumerate(arr):
            print("[",i[0],"]",i[1])
        print("-"*10)
        print("Added files to arrange:",multipfiles,sep="\n")
        print("-"*10)
        askselect = input("""Type the number of the file to select. 
Type d to done selecting.""")
        
        print("Added files to arrange:",multipfiles,sep="\n") 
        if "," in askselect:
            girilensayilar = askselect.split(",")
            try:
                for u in girilensayilar:
                    for i in enumerate(arr):
                        try:
                            if i[0] == int(u):
                                if i[1] in multipfiles:
                                    pass
                                else:
                                    multipfiles.append(i[1])
                        except Exception as err:
                            logging.debug(err)
                    
            except Exception as err:
                logging.debug(err)
                pass                      

        elif askselect == "d":
            try:
                for i in multipfiles:
                    file = open("{}".format(i))
                    allcodes.extend(file.readlines())
                    file.close()
                break
            except Exception as err:
                input("an error occurred. exiting.")
                exit()

        elif askselect == "":
            input("You selected nothing. If you done selecting files, just type \"d\"")
            continue
        else:
            for i in enumerate(arr):
                try:
                    if i[0] == int(askselect):
                        if i[1] not in multipfiles:
                            multipfiles.append(i[1])
                        else:
                            pass
                except Exception as err:
                    logging.debug(err)
            print("Added files to arrange:",multipfiles,sep="\n")
            continue

def checker():
    checklist = list()
    for i in range(len(categories)):
        checklist.append(bool(dct[categories[i]]))
    return checklist
        
def unbundledemptycheck():
    if any(checker()):
        file3 = open("UNBUNDLED.txt","w")
        for y in range(len(categories)):
            codelist = dct[categories[y]]
            print("\n")
            for y in codelist:
                try:
                    file3.write(y)
                except Exception as err:
                    logging.error(err)
                    pass
        file3.close()
    else:
        return False

def custommode():
    try:
        categories.pop(categories.index("\n"))
    except Exception as err:
        logging.error(err)
    for i in categories:
        print(i)
        dupselect = input(
            f"How many codes you want each bundle for {i.title()} category?")
        try:
            if not dupselect == "0":
                custommodelist[i] = int(dupselect)
            else:
                pass
        except Exception as err:
            logging.error(err)
    print(custommodelist)
    flag.append(True)



clearing()
print(f"(Operating system is detected as {platform.system()}.)")
print("v1.3.1")
print("""
This script organizes group of codes. Gets one code from a group and add it to one under the other. Original file will stay the same.
So input data will be:             .txt file with grouped codes
And output data will be :     .txt file with bundled codes, .txt file with unbundled codes.

""")
input("Press 'Enter to continue...")
arr = os.listdir(".")
while True:
    allcodes.clear()
    categories.clear()
    counts.clear()
    dct.clear()
    custommodelist.clear()
    arr = os.listdir(".")
    clearing()

    if multiplefiles() == False:
        continue
    else:
        pass
    clearing()
    print("Files are added.")
    getcategories()
    if listeleme() == False:
        continue
    else:
        pass
    clearing()
    createlists()
    for i in range(50):
        try:
            addingtodct(i)
        except Exception as err:
            logging.info(err)
            pass
    try:
        dct.pop("\n")
    except Exception as err:
        logging.error(err)
        pass
    creatingbundles()
    for i in range(250):
        try:
            getremainings(i)
        except Exception as err:
            logging.info(err)
            pass
    if not unbundledemptycheck() == False:
        print("Remaining codes exported as UNBUNDLED.txt to the same directory")
    else:
        print("No files created because there are no code left for unbundled file.")
    input("Sounds cool. [Enter]    ")
    print("""Choose what do you want to do:
        [1] Main Menu
        [2] Quit
        """)
    choose = input("Input    :")
    if choose == "1":
        continue
    elif choose == "2":
        input("God saved my böbreks. Press enter to cheers.")
        exit()
    else:
        input("You did something wrong. To go back to menu, just press enter.")
        exit()