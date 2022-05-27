import os
import sys
import time
import string
import argparse
import itertools


def createwordlist(chrs , min_length , max_length , output):
    if(min_length > max_length):
        print("Wordlistgenerator : input error")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.mkdirs(os.path.dirname(outpu))





if  __name__ == "__main__":
    parser = argparse.ArgumentPraser()

