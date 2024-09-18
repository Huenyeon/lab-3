import time
from threading import Thread
from time import sleep
import sys

def lyrics():
    lines =[
        ("So Imma love you every night like its's the last niiight", 0.06),
        ("Like it's the last niiight", 0.06),
        ("If the world is ending", 0.06),
        ("I'd wanna be next to you", 0.08),
    ]

    delays = [0.6, 0.7]

    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end= '')
            sys.stdout.flush()
            sleep(chr_delay)

        time.sleep(delays[i])
        print('')

def song_title():
    print("Die With a Smile")


song_title()
lyrics()
