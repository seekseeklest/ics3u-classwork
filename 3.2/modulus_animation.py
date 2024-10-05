import time
import os

repeats = 5
steps_per_second = 5

for i in range(8 * repeats):
    os.system("clear")
    
    if i % 8 == 0:
        print("   /\_/\  ")
        print("  ( o.o ) ")
    elif i % 8 == 1:
        print("    /\_/\  ")
        print("   ( o.o ) ")
    elif i % 8 == 2:
        print("     /\_/\  ")
        print("    ( o.o ) ")
    elif i % 8 == 3:
        print("    /\_/\  ")
        print("   ( o.o ) ")
    elif i % 8 == 4:
        print("   /\_/\  ")
        print("  ( o.o ) ")
    elif i % 8 == 5:
        print("  /\_/\  ")
        print(" ( o.o ) ")
    elif i % 8 == 6:
        print(" /\_/\  ")
        print("( o.o ) ")
    elif i % 8 == 7:
        print(" /\_/\ ")
        print("( o.o) ")

    time.sleep(1 / steps_per_second)
