# Dinosaur Gamebot
- Game Link : http://www.trex-game.skipser.com/ 
- This is a automatic player game. The python code controls the dinosaur (player).
- Works using python's image processing library.
## pyautogui
   - Cross-platform GUI automation for human beings.
   - PyAutoGUI is a Python module for programmatically controlling the mouse and keyboard.

## Pillow
   - Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

### Working:
- The code converts a region ahead of the dinosaur into grayscale to check the presence of any obstacle.
- If obstacle appears the code controlls the dinosaur by pressing the respective keys to avoid the obstacles.
- The image coordinates vary depending on the screens resolution.
- Set the coordinates accordingly for perfect obstacle detection.


### Steps to run:
1) Install the following libraries using pip command:
    - pyautogui
    - Pillow
    - numpy
    
 2) Open the game in your browser. 
    Press "Windows + left-arrow" to place the game window onto the left half of your screen.
    
 3) Open the python file in Pycharm or any Python IDE of your choice.
    Press "Windows + right-arrow" to place the IDE window on the right half.
   
 4) Bring out the replay button of the game onto your left half of the screen 
 
 5) Run the code in the IDE on your right half of the screen.
    
   
