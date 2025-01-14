import pytsk3 #used for disk images

def list_deleted_files(image_path): 

    img_info = pytsk3.Img_Info(image_path) 
    fs_info = pytsk3.FS_Info(img_info)
    file_list = fs_info.open_dir(path="/") 
    print("Deleted Files:") 

    for file in file_list: 
    if '$' not in file.info.name.name.decode('utf-8'): 
        Try:
            file.read_random(0, 1) 
        except IOError: 
            print(file.info.name.name.decode('utf-8')) 

image_path = "/mnt/images/ntfs.img" 
list_deleted_files(image_path)
