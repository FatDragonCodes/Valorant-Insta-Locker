# Fat Dragon Valorant InstaLocker 🐉
Simple program created using image recognition to detect when we are selecting an agent and lock a agent using user defined coordinates. This script is still in the early stages, meaning you will potentially find bugs or issues. Please submit these issues via the issues tab on this repository. I will fix these issues when i have free time. 

# Disclaimer ⚠️
I am in no way a professional developer, i do this in my free time for a challenge. I'm entirely self taught, any feedback and or improvements are greatly appreciated. This script was designed for personal usage, but a few friends recommended I share it. This script controls your mouse movement, meaning it should not result in a Anti-Cheat ban - with this in mind please use this at your own risk. 

# Default Binds ⌨️ 
U: Allows user to load, delete and save configs. Prompts will appear on the console with steps.\
I: Unlocks the active coords to allow you to set agent/confirm button coord locations \
O: Sets Agent coord locations\
P: Sets confirm button locations\
M: Enables/Disables the instalock script\
INSERT: opens and closes the clicker

# Setup ⚙️
[1] First lets make sure valorant is running in windowed full screen mode (this is required to allow us to search for images on screen)\
[2] Load a private game so we can setup coords\
[3] Make sure the coords are unlocked using the I toggle key.\
[4] Hover the agent you wish to instalock and press O. Once confirmed press I again to relock coords to prevent accidental changes\
[5] Now press U to begin saving config\
[6] Type save and press enter\
[7] Now enter the config name, your config should now have saved.\
[8] You can load this by pressing U, then typing load,  followed by the config name.\
- Video tut can be released if needed.

# FAQ 📙
**Will This Get Me Banned?**\
No, this controls the users mouse input and doesn't interfere with any game memory/integrity.\
**Can I Change Keybinds?**\
Currently there is no way to edit this using the program itself. Although you are able to manually update this by changing the appropriate values in the agents.json file\
**Why does the program require admin esc?**\
We require admin esc to ensure we can block user mouse inputs whilst attempting to insta lock, this prevents user error causing miss clicks.
