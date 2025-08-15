import os
import csv

disk_path = "smb://"
csv_name = "file.csv"

files_to_add: list[list[str]] = [] # acumulation of files and folders to be added to csv at the end of the script
folders_to_add: list[list[str]] = []


for root, dirs, files in os.walk(disk_path):

    for one_file in files:
        if os.path.getsize(os.path.join(root, one_file)) > 500 * (1024 ** 2):
                files_to_add.append([os.path.join(root, one_file), one_file, "EXCEEDED"])

    for one_dir in dirs:
        if len(os.listdir(os.path.join(root, one_dir))) == 0:
            folders_to_add.append([os.path.join(root, one_dir), one_dir, "EMPTY"])


with open(csv_name, mode="w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Path", "Name", "Flag"])
    writer.writerows(folders_to_add)
    writer.writerows(files_to_add)




# Všetky súbory a foldry pridávam do csv až na konci, nech náhodou nezlihá otvorenie súboru v strede skriptu.

# Ak som to pochopil správne, tak nemusím nič zoraďovať, pretože empty je vždy pred exceeded. 
# Preto stačí ak pridam najprv riadky s empty a potom riadky s exceeded a je to zoradené. 

# Pri testovaní som musel použiť try a except, pretože k niektoré súbory boli zamknuté.
# V zadaní sa nič o tom nepíše tak som to dal preč.


