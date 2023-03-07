import os
import sys


def file_rename(path, splitby: str, choice):
    files = os.listdir(path)

    for index, file in enumerate(files):
        os.rename(
            os.path.join(path, file),
            # os.path.join(path, "".join([file.split("_")[-1], ".pdf"])),
            os.path.join(path, file.split(splitby)[int(choice)]),
        )


if __name__ == "__main__":
    file_rename(sys.argv[1], sys.argv[2], sys.argv[3])

"""
$ python util/file_rename.py pdf '_' 3
"""
