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
    # search keyword in the line which contains the Tc value
    search_keyword = "Tc (in mean field approximation)"
    # index number in a splitted line to identify the Tc value
    index_number = 6

    def __init__(self, filename, dirname_tc="/tc", dirname_j="/j"):
        self.filepath_tc_mode = os.getcwd() + dirname_tc + "/" + filename
        self.filepath_j_mode = os.getcwd() + dirname_j + "/" + filename

    def get_tc(self, filepath):
        with open(filepath, mode='r', encoding='utf-8') as file:
            line_list = file.readlines()

        for line in line_list:
            if self.search_keyword in line:
                tc_value = line.split()[self.index_number]
        # check whether tc_value is set or not
        try:
            tc_value
        except NameError:
            print("Failed to catch Tc value. Check the output file or script file.")

        # The default format of Tc value in AkaiKKR is "xxxxx.xxxK", thus remove "K" in the end.
        tc_value = tc_value.replace("K", "")
        tc_value = float(tc_value)

    def print(self):
        print(self.filepath_tc_mode)
        print(self.filepath_j_mode)


if __name__ == '__main__':
    filename = "output.dat"
    dirname_tc = "/tc"
    dirname_j = "/j"
    test_instance = TcFromTcandJmode(filename, dirname_tc, dirname_j)
    test_instance.print()
    test_instance.get_tc(test_instance.filepath_j_mode)
