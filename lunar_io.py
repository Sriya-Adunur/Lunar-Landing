# Defines functions for input and output.
# CSC 101, Project 2
# Given code, Summer '22
# NOTE: Do not alter this file.

import sys


HEADER =\
 "     Time     |   Altitude   |   Velocity   |     Fuel     |   Throttle   "
RULE =\
 "--------------+--------------+--------------+--------------+--------------"
FOOTER =\
 "              |              CONTACT DETECTED              |              "
ROW = " %10d s | %10.2f m | %8.2f m/s | %9.2f kg |"


def get_name():
    """
    Get the LM's name.

    :return: The LM's name
    """
    return input("What is your lunar module's name? ")


def print_welcome(name):
    """
    Display the welcome message and table headers.

    :param name: A LM's name
    """
    print("\n\"'%s', Houston. You're GO for powered descent.\"\n" % name)
    print(HEADER)
    print(RULE)


def print_status(time, altitude, velocity, fuel):
    """
    Display the LM's status, prompting for throttle if necessary.

    :param time: A current time elapsed
    :param altitude: A current altitude
    :param velocity: A current velocity
    :param fuel: A current amount of fuel
    :return: The next throttle setting
    """
    print(ROW % (time, altitude, velocity, fuel), end = "")

    if fuel > 0:
        throttle = input(" ? ")
        if not sys.stdin.isatty():
            print("%s" % throttle)
        try:
            throttle = int(throttle)
        except:
            throttle = 0
    else:
        throttle = 0
        print(" 0")

    return throttle


def print_landing(time, velocity, fuel):
    """
    Display the LM's final status at landing.

    :param time: A current time elapsed
    :param velocity: A current velocity
    :param fuel: A current amount of fuel
    """
    print(FOOTER)
    print(ROW % (time, 0, velocity, fuel) + " SHUTDOWN")


def print_success(name):
    """
    Display the successful landing message.

    :param name: A LM's name
    """
    print("\n\"Houston, Tranquility Base here: the '%s' has landed.\"" % name)
    print("\"Roger, Tranqulity. We copy you on the ground.\"")


def print_error():
    """
    Display the partially successful landing message.
    """
    print("\n\"Contact -- bam! No denying that. We had contact.\"")
    print("\"The leg's in a crater, and the rim is right under the engine!\"")


def print_failure():
    """
    Display the failed landing message.
    """
    print("\n\"Fate has ordained that those who went to the Moon")
    print("to explore in peace will stay on the Moon to rest in peace.\"")
