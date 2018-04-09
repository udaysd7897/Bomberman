LIBRARIES USED
1. os          :      For os.system("clear")
2. sys         :      For sys.stdin
3. getch       :      To take single character input
4. termios     :      To flush output and input streams
4. tty		   :	  putting the tty(function) into cbreak and raw modes

USAGE
python3 game.py

SYMBOLS USED
Walls      :      X(background white) 
Bricks     :      / 
Bomberman  :      B(Green) 
Enemy      :      E(Red)
explosion  :      e(Yellow) 
Bombs      :      Timer(2->1->0) (cyan) 

CONTROLS
w    :    Move Up
a    :    Move Left
s    :    Move Down
d    :    Move Right
b    :    Plant bomb at current location
q    :    Exit game

SCORING
Destroying brick   :   20 points
Killing enemy      :   100 points