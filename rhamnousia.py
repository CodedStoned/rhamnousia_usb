from blkinfo.filters import BlkDiskInfo
import json

blkd = BlkDiskInfo()
location = -1
quotes = 0
disks = blkd.get_disks()
json_o = json.dumps(disks)
name_index = json_o.find('name')
end_quote = json_o.find('')
name_start_index = 10
print(name_index)

for char in json_o:
    if char == "\"":
        quotes += 1
        
    if quotes == 5:
        end_quote = json_o.find("kname", quotes - 3)    
drive_name = json_o[name_start_index + 1:end_quote - 4]
drive = "/dev/" + drive_name
print(drive)
