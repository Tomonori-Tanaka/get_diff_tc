# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os

class TcFromTcandJmode:
    """Gets and deals with 2 Tc (Curie temp.) values from tc mode and j mode in AkaiKKR code.

    It is assumed that the executed directory should be like below:
    executed dir
             ├ dirname_tc
             │       └ filename
             └ dirname_j
                     └ filename

    Args:
        filename (str): File name of output file that includes Tc value.
        dirname_tc (str): Directory name of tc mode. Default: "/tc"
        dirname_j (str): Directory name of j mode.
    """
    def __init__(self, filename, dirname_tc="/tc", dirname_j="/j"):
        self.filepath_tc_mode = os.getcwd() + dirname_tc + "/" + filename
        self.filepath_j_mode = os.getcwd() + dirname_j + "/" + filename

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
