# encoding=gbk
import os
import shutil,zipfile

# old_string = '/*EVENTSTART_DEST*/'
# new_string = '/*EVENTSTART_DEST*/'
# with open(r'E:\bulidpackage\CDZsystemParams.js','r',encoding='utf-8') as f1:
#     content = f1.read()
#     aaa = re.compile(r'\/\*EVENTSTART_SRC\*\/(.*?)\/\*EVENTEND_SRC\*\/',re.DOTALL)
#     hd_new_content = new_string + aaa.findall(content)[0]
#     print(hd_new_content)
#
# def insertrandomproperty(file):
#     with open(file, 'r') as oldfile:
#         content = oldfile.read()
#         checkandinsert(content, file)
# def checkandinsert(content, file):
#     new_content = content.replace(old_string, hd_new_content)
#     with open(file, 'w') as newfile:
#         newfile.write(new_content)
#
# if __name__ == '__main__':
#     insertrandomproperty(r'E:\bulidpackage\HDsystemParams(1).js')


# def content_blank_replace(copycontent,outcontent,copy_start,copy_end,out_string):
#     old_string = out_string
#     new_string = out_string
#     with open(copycontent, 'r', encoding='utf-8') as f1:
#         content = f1.read()
#         aaa = re.compile(r'\/\*%s\*\/(.*?)\/\*%s\*\/'%(copy_start,copy_end), re.DOTALL)
#         hd_new_content = new_string + aaa.findall(content)[0]
#
#     with open(outcontent, 'r',encoding='utf-8') as oldfile:
#         content = oldfile.read()
#         new_content = content.replace(old_string,hd_new_content)
#         with open(outcontent,'w',encoding='utf-8') as newfile:
#             newfile.write(new_content)
#
#
# #content_blank_replace(r'E:\bulidpackage\CDZsystemParams.js',r'E:\bulidpackage\HDsystemParams(1).js',
#  #                     'EVENTSTART_SRC','EVENTEND_SRC','/*EVENTSTART_DEST*/')
#
#
#
# content_blank_replace(r'E:\bulidpackage\CDZsystemParams.js', r'E:\bulidpackage\HDsystemParams(1).js',
#                       'INITSTART_SRC', 'INITEND_SRC','/*INITSTART_DEST*/')

# content_blank_replace(r'E:\bulidpackage\CDZsystemParams.js', r'E:\bulidpackage\HDsystemParams(1).js', 'BUSINESSSTART_SRC', 'BUSINESSEND_SRC',
#                                    '/*BUSINESSSTART_DEST*/')

# new_content = ''
# with open(r'E:\bulidpackage\CDZsystemParams.js','r',encoding='utf-8') as f1:
#     content = f1.read()
#     aaa = re.compile(r'\/\*DEFINIESTART_SRC\*\/(.*?)\/\*DEFINEEND_SRC\*\/' ,re.DOTALL)
#     #aaa = re.compile(r'\/\*EVENTSTART_SRC\*\/(.*?)\/\*EVENTEND_SRC\*\/',re.DOTALL)
#     new_content = aaa.findall(content)[0] + new_content
# print(new_content,type(new_content))
#
# old_content = ''
# with open(r'E:\bulidpackage\HDsystemParams(1).js','r',encoding='utf-8') as f2:
#     content1 = f2.read()
#     a1 = re.compile(r'\/\*DEFINESTART_DEST\*\/(.*?)\/\*DEFINEEND_DEST\*\/',re.DOTALL)
#     old_content = a1.findall(content1)[0] +old_content
#     print(old_content)
#     new_content1 = content1.replace(old_content,new_content)
#     with open(r'E:\bulidpackage\HDsystemParams(1).js','w',encoding='utf-8') as f3:
#         f3.write(new_content1)

import os, tarfile,re






#package_path = os.path.abspath(os.path.dirname(__file__))+'\outpath'


# with open('wrapper.conf', "r", encoding="utf-8") as f1, open("wrapper1.conf", "w",encoding="utf-8") as f2:
#     n=1
#     for line in f1.readlines():
#         if 'wrapper.java.classpath' in line:
#             n = n + 1
#             if "jasypt-1.9.4.jar"  in line:
#                 f2.write(line+'%sxxxxxx'%n+"\n" )
#             else:
#                 f2.write(line)
#         else:
#             f2.write(line)
# os.remove('wrapper.conf')
# os.rename("wrapper1.conf", 'wrapper.conf')

# with open('wrapper.conf', "r", encoding="utf-8") as f1, open("wrapper1.conf", "w",encoding="utf-8") as f2:
#     n=1
#     for line in f1.readlines():
#         if 'wrapper.java.classpath' in line:
#             n = n + 1
#             f2.write(line)
#         elif "# Java Library Path (location of Wrapper.DLL or libwrapper.so)"  in line:
#             f2.write(line+'%sxxxxxx'%n+"\n" )
#         else:
#             f2.write(line)
# os.remove('wrapper.conf')
# os.rename("wrapper1.conf", 'wrapper.conf')

# with open('wrapper.conf', "r", encoding="utf-8")as f1:
#     for line in f1.readlines():
#         if 'wrapper.java.classpath' in line:
#             n = n + 1
# file = open('wrapper.conf', "r", encoding="utf-8")
# content = file.read()
# add_content = 'wrapper.java.classpath.' + str(n) + '=%REPO_DIR%/' + file_zip_name
# pos = content.find("# Java Library Path (location of Wrapper.DLL or libwrapper.so)")
# if pos != -1:
#     content = content[:pos] + add_content + content[pos:]
#     file = open("wrapper.conf", "w")
#     file.write(content)
#     file.close()




# os.system('rmdir /s /q .git')

package_path = os.path.abspath(os.path.dirname(__file__)) + '\outpath'

# def untar(fname, zip_dirs):
#     """
#     :param fname: 解压文件路径
#     :param zip_dirs: 解压后存放路径
#     :return:
#     """
#     t = tarfile.open(fname)
#     t.extractall(path = zip_dirs)
#     files = file_name(zip_dirs)
#     print(files)
#     file_zip_name = ''
#     print(package_path+'\%s\lib' % files)
#     for root, dirs, files in os.walk(package_path+'\%s\lib' % files):
#         for fileName in files:
#             if 'mastersmeetingsystem' in fileName:
#                 file_zip_name = fileName
#     print(file_zip_name)
#     os.chdir(r'%s\%s\conf' %(zip_dirs,files))
#     n = 1
#     with open('wrapper.conf', "r", encoding="utf-8")as f1:
#         for line in f1.readlines():
#             if 'wrapper.java.classpath' in line:
#                  n = n + 1
#     file = open('wrapper.conf', "r", encoding="utf-8")
#     content = file.read()
#     add_content = 'wrapper.java.classpath.'+str(n)+'=%REPO_DIR%/'+file_zip_name
#     pos = content.find("# Java Library Path (location of Wrapper.DLL or libwrapper.so)")
#     if pos != -1:
#         content = content[:pos] + add_content + content[pos:]
#         file = open("wrapper.conf", "w")
#         file.write(content)
#         file.close()
# def file_name(file_dir):
#     for root,dirs,files in os.walk(file_dir):
#         for file_names in dirs:
#             if 'mastersmeetingsystem' in file_names:
#                 name = file_names
#     return name
# def preDelPic(path):
#   for root, dirs, files in os.walk(path):
#     for name in files:
#       if name.endswith(".tar.gz"):
#         os.remove(os.path.join(root, name))
# def make_targz(output_filename, source_dir):
#   with tarfile.open(output_filename, "w:gz") as tar:
#     tar.add(source_dir, arcname=os.path.basename(source_dir))



def untar(fname, zip_dirs):
    """
    :param fname: 解压文件路径
    :param zip_dirs: 解压后存放路径
    :return:
    """
    t = tarfile.open(fname)
    t.extractall(path=zip_dirs)
    file_zip_name = ''
    Files = file_name(zip_dirs)
    for root, dirs, files in os.walk(package_path+'\%s\lib' %Files):
        for fileName in files:
            if 'mastersmeetingsystem' in fileName:
                file_zip_name = fileName
    os.chdir(r'%s\%s\conf' % (zip_dirs, Files))
    n = 1
    with open('wrapper.conf', "r", encoding="utf-8") as f1, open("wrapper1.conf", "w", encoding="utf-8") as f2:
        for line in f1.readlines():
            if 'wrapper.java.classpath' in line:
                n = n + 1
                f2.write(line)
            elif "# Java Library Path (location of Wrapper.DLL or libwrapper.so)" in line:
                f2.write(line + 'wrapper.java.classpath.' + str(n) + '=%REPO_DIR%/' + file_zip_name + "\n")
            else:
                f2.write(line)
    os.remove('wrapper.conf')
    os.rename("wrapper1.conf", 'wrapper.conf')

#获取文件夹名
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file_names in dirs:
            if 'mastersmeetingsystem' in file_names:
                name = file_names
    return name
#untar(r'E:\bulidpackage\CDSZF\outpath\mastersmeetingsystem-cdszf-2.6.2-20201204141739-distribution.tar.gz',r'E:\bulidpackage\CDSZF\outpath')
#preDelPic(r'E:\bulidpackage\CDSZF\outpath')
#make_targz(r'E:\bulidpackage\CDSZF\outpath\mastersmeetingsystem-cdszf-2.6.2-20201201134715-distribution.tar.gz',r'E:\bulidpackage\CDSZF\outpath\mastersmeetingsystem-cdszf-2.6.2-20201201134715')

# list = os.listdir(r'D:\cdszfserver\CDSZF-smeetingsystem-server\target')
# os.chdir(r'D:\cdszfserver\CDSZF-smeetingsystem-server\target')
# for file_name in list:
#     if file_name.endswith('.jar') or file_name.endswith('.gz'):
#         os.remove(file_name)



