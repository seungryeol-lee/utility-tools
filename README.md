# Guide

1. Copy all files to rename and merge into a specified directory (e.g. `pdf/`).
2. (Optional) If the files are not sorted / indexed in alphanumerical order, execute `file_rename.py`, with positional argument `[directory] [string_to_split] [splitted_piece_to retain]`. Note that the name of the files should be according the order of preference for merging in the subsequent step.
3. To merge all `.pdf` files, execute `pdf_merge.py` with positional argument `[directory]`.
4. Move the merged PDF file to Windows system for viewing.


Example:
```bash
$ cp -a /mnt/c/Users/user/scientia/_attachments/Multi* pdf # copy all files
$ python util/file_rename.py pdf '_' 3
$ python util/pdf_merge.py pdf
$ mv pdf_merged.pdf /mnt/c/Users/user/Downloads/
```