#Rhamnousia Backdoor

import os
import sys
import psutil

#var
path = "~/Desktop"
user_in = ""
def gain_access():

    print("hacking...")
    fat32_disks = []
    ntfs_disks = []
    ext4_disks = []
    disks = psutil.disk_partitions()
    print(disks)
    os.system("pause")
    for disk in disks:
        if disk[2] == "fat32":
            fat32_disks.append(disk[0])
        elif disk[2] == "ntfs":
            ntfs_disks.append(disk[0])
        elif disk[2] == "ext4":
            ext4_disks.append(disk[0])
    print(fat32_disks)
    print(ntfs_disks)
    print(ext4_disks)
    if len(ext4_disks) == 1:
        print("One linux drive.")
        os.system("cd "+ ext4_disks[0])
    elif len(ext4_disks) == 2:
        print("Two linux disks")
        os.system("cd "+ ext4_disks[1])
    if len(ntfs_disks) == 1:
        print("One windows drive.")
        os.system("cd "+ ext4_disks[0])
    elif len(ntfs_disks) == 2:
        print("Two windows disks")
        os.system("cd "+ ext4_disks[1])
    if len(fat32_disks) == 1:
        print("One fat32 drive.")
        os.system("cd "+ ext4_disks[0])
    elif len(fat32_disks) == 2:
        print("Two fat32 disks")
        os.system("cd "+ ext4_disks[1])
    return disks
def main_menu():

    print("+------------------+")
    print("|   Type \'hack\'    |")
    print("+------------------+")
    user_in = input("Rhamnousia> ")
    return user_in

user_in = main_menu()
# print(user_in)
if user_in == "hack":
    gain_access()
elif user_in == "help":
    print("Type \'hack\' to gain access. once completed, reboot and plug in chip.")
    system("clear")
    main_menu()
else:
    print("{} is not a valid command. please try again.".format(user_in))
