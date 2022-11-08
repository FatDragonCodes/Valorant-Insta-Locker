import keyboard, pyautogui, threading, time, time, os, ctypes, json, win32gui, win32con, sys
from colorama import Fore
from ctypes import windll

Active = False
Locked = False
Hidden = False
LINE_FLUSH = '\r\033[K'
UP_FRONT_LINE = '\033[F'
hwnd = win32gui.GetForegroundWindow()

defaults = {"SaveConfig": "U", "CONFIRMATION_BUTTON": "1588,691", "AGENT_COORDS": "579,561", "Activation_Key": "M", "Agent_Key": "O", "Confrm_Btn": "P", "Lock_Key": "I", "Hidden_Key": "INSERT", "Help_Key": "H"}

class Admin_Check():

    def Is_Admin():
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            os._exit(0)
            
class Keyboard():

    def Keyboard_Listner():
        global Active, Confirm_Coords, Agent_Coords, Locked, Hidden

        try:
            # Added Time.Sleep() to prevent script thinking user is spamming when they are not
            while 1:
                if keyboard.is_pressed(Activation_Key): 
                    match Active:
                        case True:
                            Active = False
                            print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Awake: "+str(Active))
                        case False:
                            if Confirm_Coords is None:
                                print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Missing Coords")
                            else:
                                Active = True
                                print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Awake: "+str(Active))
                    time.sleep(0.2)      
                if keyboard.is_pressed(Help_Key):
                    print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press "+Agent_Key+" To Set Agent Coords")
                    time.sleep(3),
                    print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press "+Confrm_Btn+" To Set Confirm Button Coords")
                    time.sleep(3)
                    print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press "+Lock_Key+ " To Allow/Prevent Changing Of Coords")
                    time.sleep(3)
                    print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press "+Hidden_Key+ " To Minimize/Maximize Menu")
                    time.sleep(0.2)
                if keyboard.is_pressed(Agent_Key):
                    if Locked is False:
                        Agent_Coords = pyautogui.position()
                        Agent_Coords = str(Agent_Coords[0]) + ',' + str(Agent_Coords[1])
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Agent Coords Comfirmed")
                        data = Config.Open_Config_File()
                        data["AGENT_COORDS"] = Agent_Coords
                        with open("agents.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                    else:
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Coords Locked")
                    time.sleep(0.2)
                if keyboard.is_pressed(Confrm_Btn):
                    if Locked is False:
                        Confirm_Coords = pyautogui.position()
                        Confirm_Coords = str(Confirm_Coords[0]) + ',' + str(Confirm_Coords[1])
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Comfirm Btn Coords Comfirmed")
                        data = Config.Open_Config_File()
                        data["CONFIRMATION_BUTTON"] = Confirm_Coords
                        with open("agents.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                    else:
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Coords Locked ")
                    time.sleep(0.2)
                if keyboard.is_pressed(Lock_Key):
                    if Locked == True:
                        Locked = False
                        windll.user32.BlockInput(False) # fail safe incase mouse is blocked and we disable activation
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Agent Coords Unlocked ")
                    else:
                            Locked = True
                            print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Agent Coords Locked ")
                    time.sleep(0.2)
                if keyboard.is_pressed(Hidden_Key):
                    if Hidden == True:
                        Hidden = False
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                    else:
                            Hidden = True
                            ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
                    time.sleep(0.2)

                # CONFIG MANGER
                if keyboard.is_pressed(SaveConfig_Key):
                    nopass = True

                    keys = [Activation_Key, Agent_Key, Confrm_Btn, Lock_Key, Hidden_Key, Help_Key, SaveConfig_Key]
                    for key in keys:
                        keyboard.unblock_key(key)
                    while nopass:
                        ansr = input(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"Load/Save/Delete/View/Default?: " ).lower()
                        if  ansr != "load" and ansr != "save" and ansr != "delete" and ansr != "view" and ansr != "default":
                            print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Invalid option")
                            time.sleep(2.5)
                        else:
                            nopass = False
                    if ansr == "save":
                        config_name = input(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"Name Config:" ).lower()
                        data = Config.Open_Config_File()
                        data[config_name] = Agent_Coords
                        with open("agents.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Saved Config: "+config_name)
                        time.sleep(0.2)
                    elif ansr == "load":
                        nopass = True
                        while nopass:
                            config_name = input(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"Config Name:" ).lower()
                            with open("agents.json", "r") as jsonFile:
                                data = json.load(jsonFile)
                            if config_name not in data:
                                print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Invalid Config")
                            else:
                                nopass = False
                        Agent_Coords = data[config_name]
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Loaded Config: "+config_name)
                        time.sleep(0.2)
                        data["AGENT_COORDS"] = Agent_Coords
                        with open("agents.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                        Utils.Block_Keys()
                    elif ansr == "delete":
                        nopass = True
                        while nopass:
                            config_name = input(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"Config Name:" ).lower()
                            with open("agents.json", "r") as jsonFile:
                                data = json.load(jsonFile)
                            if config_name not in data and config_name not in keys:
                                print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Invalid Config")
                                time.sleep()
                            else:
                                nopass = False
                        del data[config_name]
                        with open("agents.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                        print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Deleted: "+config_name)

                    elif ansr == "view":
                        pass
                    else:
                        pass
        except:
            pass

class Config():

    def Load():
        global Activation_Key, Agent_Key, Agent_Key, Confrm_Btn, Lock_Key, Hidden_Key, Help_Key, Confirm_Coords, Agent_Coords, SaveConfig_Key
        data = Config.Open_Config_File()
        Activation_Key = data["Activation_Key"]
        Agent_Key = data["Agent_Key"]
        Confrm_Btn = data["Confrm_Btn"]
        Lock_Key = data["Lock_Key"]
        Hidden_Key = data["Hidden_Key"]
        Help_Key = data["Help_Key"]
        Agent_Coords = data["AGENT_COORDS"]
        Confirm_Coords = data["CONFIRMATION_BUTTON"]
        SaveConfig_Key = data["SaveConfig"]

    def Open_Config_File():
        try:
            with open("agents.json", "r") as jsonFile:
                data = json.load(jsonFile)
                return data
        except Exception as e:
            print(UP_FRONT_LINE + LINE_FLUSH +Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Failed to load agents.json")


class Utils():

    def Start_Threads():
        threading.Thread(target=Keyboard.Keyboard_Listner, name='Checking_Key_Press').start()
        threading.Thread(target=Utils.Title_Writer, name='Title Writer').start()

    def Title_Writer():
        while 1:
            ctypes.windll.kernel32.SetConsoleTitleW("Fat Dragon ｜ Awake: "+str(Active) +" ｜ Agent Coord: "+str(Agent_Coords)+" ｜ Comfirm Coord: " +str(Confirm_Coords) + " ｜ Locked: "+str(Locked))
            time.sleep(1)
    def Clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def Block_Keys():
        keys = [Activation_Key, Agent_Key, Confrm_Btn, Lock_Key, Hidden_Key, Help_Key, SaveConfig_Key]
        for key in keys:
            keyboard.block_key(key)
        
class FATDRAGON():

    def Click_Agent(Agent_Coords, Confirm_Coords):

        windll.user32.BlockInput(True)

        global Active

        Agent_Coords = Agent_Coords.split(",")

        pyautogui.moveTo(int(Agent_Coords[0]) , int(Agent_Coords[1]), duration=0)

        for i in range(1):
            pyautogui.click()
            
        Confirm_Coords = Confirm_Coords.split(",")

        pyautogui.moveTo(int(Confirm_Coords[0]) , int(Confirm_Coords[1]), duration=0)
        for i in range(1):
            pyautogui.click()
        
        confirm = pyautogui.locateOnScreen("img/confirm.png", confidence=.5, grayscale=True)
        confirm2 = pyautogui.locateOnScreen("img/confirm2.png", confidence=.5, grayscale=True)

        if confirm is None and confirm2 is None:
            Active = False
            windll.user32.BlockInput(False)
            print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Agent Locked - Fattys Going To Sleep. ")
            time.sleep(5)
            print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press M To Awaken Fatty")
            time.sleep(2.5)

    def AgentSelectScreenFinder():
        global Active
        print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Awake: "+str(Active))

        while 1:
            if Active is True:
                    confirm2 = pyautogui.locateOnScreen("img/confirm2.png", confidence=.5, grayscale=True)
                    if confirm2 is not None:
                        FATDRAGON.Click_Agent(str(Agent_Coords), str(Confirm_Coords))
                    time.sleep(0.1)
            else:
                windll.user32.BlockInput(False)
                time.sleep(5)

    def Loading_Screen():
        global Locked
    
        ctypes.windll.kernel32.SetConsoleTitleW("Fat Dragon ｜ Loading")
        if Agent_Coords == "None" or Confirm_Coords == "None":
            Locked = False
            print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX + "[" +Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Remember To Set Coords!")
        else:
            Locked = True
            print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX + "[" +Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Loading Coords From Previous Run")
        time.sleep(2)
        ctypes.windll.kernel32.SetConsoleTitleW("Fat Dragon ｜ Loading.")
        print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX + "[" +Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Press H For Help!")
        time.sleep(2)
        ctypes.windll.kernel32.SetConsoleTitleW("Fat Dragon ｜ Loading..")
        print(UP_FRONT_LINE + LINE_FLUSH + Fore.LIGHTWHITE_EX + "[" +Fore.LIGHTGREEN_EX+"FATDRAGON"+Fore.LIGHTWHITE_EX+"] Written By Hades")
        time.sleep(2)
        ctypes.windll.kernel32.SetConsoleTitleW("Fat Dragon ｜ Loading...")

    def Main():
        Utils.Clear()
        os.system("mode 88,18")
        print(Fore.LIGHTGREEN_EX+"""
    
                                            \||/
                                            |  @___
                                  /\  /\   / (__,,,,|
                                 ) /^\) ^\/ _)
                                 )   /^\/   _)
                                 )   _ /  / _)
                             /\  )/\/ ||  | )_)
                            <  >      |(,,) )__)
                             ||      /    \)___)\\
                             | \____(      )___) )___
                              \______(_______;;; __;;;
    
                            """+Fore.LIGHTWHITE_EX+"""The Fat Dragon InstaLocker
        """)
    
        print()
        FATDRAGON.Loading_Screen()
        Utils.Start_Threads()
        FATDRAGON.AgentSelectScreenFinder()

Admin_Check.Is_Admin()
Config.Load()
Utils.Block_Keys()
FATDRAGON.Main()
