import wave_helper as helper
import os.path
from copy import deepcopy
import math


MAX_BIT = 32767
MIN_BIT = -32768

DEFAULT_FRAME_RATE = 2000
ONE_FRAME_RATE = 125

MAIN_MENU = "Press the number of what you want to do-\n" \
            "1. Change wav file\n" \
            "2. Consolidate two wav files\n" \
            "3. Compose the appropriate melody for the wav file\n" \
            "4. exit\n"

CHANGE_FILE_MENU = "Press the number of what you want to do-\n" \
            "1. Reversing the file\n" \
            "2. Increase file speed\n" \
            "3. Slow file speed\n" \
            "4. volume up\n" \
            "5. Volume down\n" \
            "6. low pass filter\n"

SECOND_MENU = "Press the number of what you want to do-\n" \
            "1. Save the file\n" \
            "2. Change the file\n"

INVALID_ERROR_MSG = "Invalid input.\n" \
                    "Please choose according to the instructions:"

FILE_REQUEST = "Please enter the file name -"
ORDER_FILE_REQUEST = "Please enter the Instructions for composing file name -"
CONSOLIDATE_FILE_REQUEST = "Please enter the two files names -"

NOT_EXIST_ERROR_MSG = "File does not exist."

FILE_ERROR_MSG = "File does not appropriate."

NEW_FILE_NAME_MSG = "Please enter name for the new file-"

SUCCESSFUL_SAVE_MSG = "File saved successfully"
UNSUCCESSFUL_SAVE_MSG = "The file save failed!"

CHAR_DICT = {'A': 440, 'B': 494, 'C': 523, 'D': 587,
             'E': 659, 'F': 698, 'G': 784, 'Q': 0}

VOLUME_CHANGE_FACTOR = 1.2


# General Reference Functions-


def get_pairs_average(pairs_lst):
    """
    A function that calculates the average pair for a list of pairs
    :param pairs_lst: List, lists of pairs and numbers
    :return: List, the average pair
    """
    sum_1 = 0
    sum_2 = 0

    for pair in pairs_lst:
        sum_1 += pair[0]
        sum_2 += pair[1]

    return [int(sum_1 / len(pairs_lst)), int(sum_2 / len(pairs_lst))]


def max_min_check(num):
    """
    A function that makes sure that a number is within the allowed range
    :param num: Int number
    :return: int, the number or maximum / minimum
    """
    if num >= MAX_BIT:
        return MAX_BIT
    elif num <= MIN_BIT:
        return MIN_BIT
    return num


def get_choose(menu_msg, optional_chooses):
    """
    A function that receives a value from the user,
     verifies that it is valid, and returns it
    :param menu_msg: String, explain to the user what is required
    :param optional_chooses: The number of options to choose
    :return: String, valid input
    """
    optional_lst = [str(i+1) for i in range(optional_chooses)]
    while True:
        new_input = input(menu_msg)
        if new_input in optional_lst:
            return new_input
        else:
            print(INVALID_ERROR_MSG)


def get_wav_file():
    """
    A function that gets some wav file to open, and opens it
    :return:  tuple, Represents sound
    """
    while True:
        file_name = input(FILE_REQUEST)
        # Check that the file exists -
        good_file = os.path.isfile(file_name)
        if not good_file:
            print(NOT_EXIST_ERROR_MSG)
            continue
        else:
            # Open the file
            opened_file = helper.load_wave(file_name)
            if opened_file == -1:  # Checks that the file opens well
                print(FILE_ERROR_MSG)
                continue
            else:
                return opened_file


def save_file(wav_file):
    """
    A function that saves sound to a file, as the user chooses
    :param wav_file: tuple, Represents sound
    """
    new_name = input(NEW_FILE_NAME_MSG)
    result = helper.save_wave(wav_file[0], wav_file[1], new_name)
    if result == 0:
        print(SUCCESSFUL_SAVE_MSG)
    else:
        print(UNSUCCESSFUL_SAVE_MSG)


# Functions related to file changes -


def change_file_action(wav_file=None):
    """
    A function that transfers the software to modify the file
    according to the user's request
    :param wav_file: Optional, a file we're already working on
    :return: tuple, Represents sound
    """
    # Getting a file to work on, if necessary-
    if wav_file is None:
        wav_file = get_wav_file()

    new_input = get_choose(CHANGE_FILE_MENU, 6)  # Get user selection

    if new_input == "1":
        return reversing(wav_file)

    elif new_input == "2":
        return change_speed_faster(wav_file)

    elif new_input == "3":
        return change_speed_slower(wav_file)

    elif new_input == "4":
        return change_volume(wav_file, True)

    elif new_input == "5":
        return change_volume(wav_file, False)

    elif new_input == "6":
        return low_pass_filter(wav_file)


def reversing(wav_file):
    """
    Function that reversing the file
    :param wav_file: tuple, Represents sound
    :return: tuple, Represents sound
    """
    new_wav_file = deepcopy(wav_file[1])
    new_wav_file.reverse()
    return wav_file[0], new_wav_file


def change_speed_faster(wav_file):
    """
    A function that accelerates the audio speed of the given file
    :param wav_file: tuple, Represents sound
    :return: tuple, Represents sound
    """
    new_sound = []
    # Passing the sound list, in two-by-one jumps
    for index in range(0, len(wav_file[1]), 2):
        new_sound.append(wav_file[1][index])

    return wav_file[0], new_sound


def change_speed_slower(wav_file):
    """
    A function that slows the audio speed of the given file
    :param wav_file: tuple, Represents sound
    :return: tuple, Represents sound
    """
    # Check the case of an empty list
    if len(wav_file[1]) == 0:
        return wav_file

    new_sound = []
     # Passing the sound list, except the last one
    for index in range(len(wav_file[1])-1):
        new_sound.append(wav_file[1][index])  # Adds it to the list
        # Creates and adds the average of the bit, and the next one
        avr = get_pairs_average([wav_file[1][index], wav_file[1][index+1]])
        new_sound.append(avr)

    new_sound.append(wav_file[1][len(wav_file[1])-1])   # Adds the last bit

    return wav_file[0], new_sound


def change_volume(wav_file, up):
    """
    A function that changes the volume of the audio
    :param wav_file: tuple, Represents sound
    :param up: Boolean, True boost. False to lower.
    :return: tuple, Represents sound after changing the volume
    """
    new_sound = []
    if up:
        factor = VOLUME_CHANGE_FACTOR
    else:
        factor = 1 / VOLUME_CHANGE_FACTOR

    for i in range(len(wav_file[1])):
        first_char = int(float(wav_file[1][i][0]) * factor)
        sec_char = int(float(wav_file[1][i][1]) * factor)

        # Check that the values ​​in the allowed range
        first_char = max_min_check(first_char)
        sec_char = max_min_check(sec_char)

        new_sound.append([first_char, sec_char])

    return wav_file[0], new_sound


def low_pass_filter(wav_file):
    """
    Audio dimming function
    :param wav_file: tuple, Represents sound
    :return: tuple, Represents sound after dimming
    """
    # Check the case of an empty or single list
    if len(wav_file[1]) <= 1:
        return wav_file

    new_sound = []
    lst_len = len(wav_file[1])

    # Dim the first bit
    avr = get_pairs_average([wav_file[1][0], wav_file[1][1]])
    new_sound.append(avr)

    # Dim the bits in the middle
    for index in range(1, lst_len-1):
        avr = get_pairs_average([wav_file[1][index-1],
                                 wav_file[1][index], wav_file[1][index+1]])
        new_sound.append(avr)

    # Dim the last bit
    if len(wav_file[1]) >= 2:
        avr =\
            get_pairs_average([wav_file[1][lst_len-1], wav_file[1][lst_len-2]])
        new_sound.append(avr)

    return wav_file[0], new_sound


# Functions related to the consolidation of two files-


def consolidate_two_files():
    """
    A function that unifies two audio files
    :return: tuple, Represents sound after unifies
    """
    file1, file2 = get_two_wav_file()

    # If the file rate is equal, we will arrange them by length-
    if file1[0] == file2[0]:
        if len(file1[1]) > len(file2[1]):
            sort_file, long_file = file2, file1
        else:
            sort_file, long_file = file1, file2

    # If the file rate is different, adjust the tempo and arrange by length-
    elif file1[0] < file2[0]:
        sort_file, long_file = short_past_list(file1, file2)
    else:
        sort_file, long_file = short_past_list(file2, file1)

    new_sound = []
    # Connecting the shared part
    for i in range(0, len(sort_file[1])):
        # Taking average between files-
        avr = get_pairs_average([sort_file[1][i], long_file[1][i]])
        new_sound.append(avr)

    # Adds a remainder of the long file
    for i in range(len(sort_file[1]), len(long_file[1])):
        new_sound.append(long_file[1][i])

    return long_file[0], new_sound


def get_two_wav_file():
    """
    The function accepts and opens two audio files
    :return: pair tuples, Represents sounds
    """
    while True:
        str_input = input(CONSOLIDATE_FILE_REQUEST)
        lst_input = str_input.split()

        # Test received exactly two files-
        if len(lst_input) != 2:
            print(INVALID_ERROR_MSG)
            continue

        # Check that both files exist-
        if not (os.path.isfile(lst_input[0]) and os.path.isfile(lst_input[0])):
            print(NOT_EXIST_ERROR_MSG)
            continue

        else:
            opened_file1 = helper.load_wave(lst_input[0])
            opened_file2 = helper.load_wave(lst_input[1])

            # Check that you can open both files
            if opened_file1 == -1 or opened_file2 == -1:
                print(FILE_ERROR_MSG)

            else:  # Everything is fine
                break

    return opened_file1, opened_file2


def short_past_list(slow_file, fast_file):
    """
    A function that accepts two audio files and adjusts their tempo,
    according to the slow one
    :param slow_file: tuple, Represents the slow sound
    :param fast_file: tuple, Represents the fast sound
    :return: pair tuples, Represents sounds- First Short !!
    """
    gcd = find_gcd(slow_file[0], fast_file[0])
    skip_rate = fast_file[0] // gcd
    take_rate = slow_file[0] // gcd

    new_sound = []
    for i in range(0, len(fast_file[1]), skip_rate):
        for j in range(take_rate):
            if i+j < len(fast_file[1]):
                new_sound.append(fast_file[1][i+j])

    # Returns the short audio first
    if len(slow_file[1]) > len(new_sound):
        return (slow_file[0], new_sound), slow_file
    return slow_file, (slow_file[0], new_sound)


def find_gcd(num1, num2):
    """
    A function that finds a maximum share divided for two numbers,
    According to Euclid's algorithm
    :param num1: int number
    :param num2: int number
    :return: int number, gcd
    """
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


# Functions related to composing melody-


def compose_melody():
    """
    A function that returns a melody according to the composing instructions
    :return: tuple, Represents the composing sound
    """

    new_sound = []
    instruc_lst = get_instructions_file()

    for char in range(0, len(instruc_lst), 2):
        frac = CHAR_DICT[instruc_lst[char]]
        time = int(instruc_lst[char+1])

        # Handling with case of Quiet
        if frac == 0:
            for i in range(time * ONE_FRAME_RATE):
                new_sound.append([0, 0])
        else:
            samples_per_cycle = DEFAULT_FRAME_RATE / frac
            for i in range(time * ONE_FRAME_RATE):
                one_bit = int(MAX_BIT *
                              math.sin(math.pi * 2 * (i / samples_per_cycle)))
                new_sound.append([one_bit, one_bit])
    return DEFAULT_FRAME_RATE, new_sound


def get_instructions_file():
    """
    A function that accepts the composition instructions file from the user
    :return: List, composition instructions
    """
    good_file = False
    while not good_file:
        file_name = input(ORDER_FILE_REQUEST)
        good_file = os.path.isfile(file_name)  # Check that the file exists
        if not good_file:
            print(NOT_EXIST_ERROR_MSG)

    instruc_lst = []
    open_file = open(file_name)

    for line in open_file:
        instruc_lst += line.split()

    open_file.close()
    return instruc_lst


# Main functions -


def main():
    """
    Main Function, Main Menu and Secondary Menu
    """
    # Main Menu-
    while True:
        new_input = get_choose(MAIN_MENU, 4)
        wav_file = None

        if new_input == '1':
            wav_file = change_file_action()

        elif new_input == '2':
            wav_file = consolidate_two_files()

        elif new_input == '3':
            wav_file = compose_melody()

        elif new_input == '4':
            break

        # Secondary Menu-
        while True:
            new_input = get_choose(SECOND_MENU, 2)

            if new_input == "1":
                save_file(wav_file)
                break

            elif new_input == "2":
                wav_file = change_file_action(wav_file)


if __name__ == '__main__':
    main()
