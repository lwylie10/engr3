import time
import board
from analogio import AnalogIn
import analogio
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

while True:

    print(potentiometer.value)      # Display value
    time.sleep(0.25)    
    