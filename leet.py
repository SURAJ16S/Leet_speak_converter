'''This program converts a string into Leet-Speak—a writing style that replaces characters with numbers and symbols that resemble the original characters.'''
import random
def cnvrt_to_leet(str):
    leet_dict = {
        'a': ['4', '@', '∆', '^', '∀', 'A', 'a'],
        'b': ['8', '3', '13', '6', 'B', 'b'],
        'c': ['(', '[', '<', 'C', 'c'],
        'd': ['0','D', 'd'],
        'e': ['3', '€', '£', 'Ǝ', 'E', 'e'],
        'f': ['ƒ', 'F', 'f'],
        'g': ['6', '9', 'G', 'g'],
        'h': ['#', 'H', 'h'],
        'i': ['1', '!', '|', 'I', 'i'],
        'j': [';', 'J', 'j', ']'],
        'k': ['|<', '/<', 'K', 'k'],
        'l': ['1', '|', '|_', '!', 'L', 'l'],
        'm': ['|\\/|', '^^', '|V|', '[V]', 'M', ' m'],
        'n': ['N', 'n'],
        'o': ['0', '()', '<>', 'O', 'o'],
        'p': ['9', 'P', 'p'],
        'q': [ '9', '0', 'Q', 'q'],
        'r': ['2', '12', 'R', 'r'],
        's': ['5', '$', 'Z', 'z', 'S', 's'],
        't': ['7', 'T', 't'],
        'u': ['v', 'U', 'u'],
        'v': ['\\/', 'V', 'v'],
        'w': ['vv', 'W', 'w'],
        'x': ['><', '}{', ')(', 'X', 'x'],
        'y': ['`/', '`/', 'Y', 'y'],
        'z': ['2', 'Z', 'z'],
        '1': ['I', '|', '!', '1', 'l'],
        '2': ['Z','z', '2'],
        '3': ['E', '3', 'Ǝ'],
        '4': ['A', '4'],
        '5': ['S','s', '5'],
        '6': ['G','b', '6'],
        '7': ['T', '7', '+'],
        '8': ['B', '8', 'I3'],
        '9': ['g', '9', 'q'],
        '0': ['O','o', '0', '()', '*', '[]'],
        ' ': ['_','-',' '] 
    }
    
    leet_text = ''
    
    for char in str:
        if char.lower() in leet_dict:
            leet_text += random.choice(leet_dict[char.lower()])
        else:
            leet_text += char 
    
    return leet_text

def main():
    while True:
        str = input("Enter a string: ")
        leet_string = cnvrt_to_leet(str)
        print("Leet-Speak Code : ", leet_string)

if __name__ == "__main__":
    main()
