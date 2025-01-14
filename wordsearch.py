import subprocess 
import os 

def dump_memory(): 
lime_path = './LiME/src/lime-$(uname -r).ko' 
    output_path = '/tmp/memdump.lime' 

     subprocess.run(['sudo', 'insmod', lime_path, f'path={output_path}', 'format=lime']) 
    return output_path 

def search_memory_with_volatility(memdump, keyword):
    command = [ 
                'volatility', 
                '-f', memdump, 
                '--profile=LinuxUbuntu_x64', 
                'linux_find_file', 
                '-F', keyword, 
                '-O', 'output_dir' 
              ] 

               process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

              stdout, stderr = process.communicate() 
              if process.returncode == 0: 
                  print(stdout.decode()) 
              else: 
                  print(f"Error: {stderr.decode()}") 

if __name__ == '__main__': 
    memdump_path = dump_memory() 
    search_keyword = input("Search keyword: ")
    search_memory_with_volatility(memdump_path, search_keyword)     
    os.remove(memdump_path)
