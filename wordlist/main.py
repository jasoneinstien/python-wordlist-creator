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
    else:
        pass


if  __name__ == "__main__":
    print("input max length")
    maxl = int(input())
    print("input min length")
    minl = int(input())
    chrs = None
    output = ""
    createwordlist(chrs , minl , maxl , output)
