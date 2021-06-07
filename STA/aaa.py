import time,os,zipfile,re,shutil

print(os.listdir(r'C:\Users\Administrator\Desktop\westone\westone\STA_PACKAGE\smeetingsystem-server-web'))



def copy_file(copy_in_path, copy_out_path):
    for files in os.listdir(copy_in_path):
        if files != '.git':
            name = os.path.join(copy_in_path, files)
            back_name = os.path.join(copy_out_path, files)
            if os.path.isfile(name):
                if os.path.isfile(back_name):
                    shutil.copy(name, back_name)
                else:
                    shutil.copy(name, back_name)
            else:
                if not os.path.isdir(back_name):
                    os.makedirs(back_name)
                copy_file(name, back_name)

copy_file(r'C:\Users\Administrator\Desktop\westone\westone\STA_PACKAGE\smeetingsystem-server-web',r'C:\Users\Administrator\Desktop\westone\westone\STA_PACKAGE\kk')
