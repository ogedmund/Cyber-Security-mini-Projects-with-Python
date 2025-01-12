#File Integrity Monitoring
import hashlib 
import time 
import os 

files_to_monitor = ["/etc/passwd", "/etc/shadow"] 
hash_dict = {} 

def get_file_hash(file_path): 
    with open(file_path, 'rb') as f: 
        return hashlib.sha256(f.read()).hexdigest() 

def initialize_hashes(): 
    for file in files_to_monitor: 
        hash_dict[file] = get_file_hash(file) 

def check_integrity(): 
    for file, initial_hash in hash_dict.items(): 
        if not os.path.exists(file): 
            print(f"{file} not found!") 
            continue 
        current_hash = get_file_hash(file) 
        if current_hash != initial_hash: 
            print(f"A change has been detected in {file}!")
            

initialize_hashes()

while True: 
    check_integrity() 
    time.sleep(3600)

#When our program first runs, it calls the initialize_hashes() function and gets the current hash values of the files we provide in the files_to_monitor list.0Then, it enters a loop that will continue unless we terminate it in any way with while True:. In this loop, it first calls the check_integrity() function. The check_integrity() function compares the current hashes of the files in the files_to_monitor list with the hashes it just created during the first run and wrote into hash_dict . If there is a difference, it displays it on the screen. If there is no difference, our function ends and our code moves to the time.sleep(3600) line, which is the 2nd line in the while True: loop. After waiting 3600 seconds, it goes to the check_integrity() function which is in the first line of the loop. And this cycle continues until we end it. As you can see from the examples, Python offers highly advanced support in almost every aspect you may need. All that remains for us is to determine our needs correctly, install the right algorithms, then identify the best libraries for this purpose and get to work.
