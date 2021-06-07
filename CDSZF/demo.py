# encoding=gbk
from common import out_style
import os,sys,yaml,time,zipfile,re,shutil,tarfile
from shutil import copyfile
package_path = os.path.abspath(os.path.dirname(__file__))+'\outpath'


def file_name(file_dir):
    name = ''
    for root, dirs, files in os.walk(file_dir):
        for file_names in dirs:
            if 'mastersmeetingsystem' in file_names:
            #if 'AO-ULT-FSsmeetingsystem' in file_names:
                name = file_names
    return name
def untar(fname, zip_dirs,commid):
    """
    :param fname: 解压文件路径
    :param zip_dirs: 解压后存放路径
    :return:
    """
    t = tarfile.open(fname)
    t.extractall(path=zip_dirs)
    file_zip_name = ''
    Files = file_name(zip_dirs)
    for root, dirs, files in os.walk(package_path + '\%s\lib' % Files):
        for fileName in files:
            #if 'AO-ULT-FSsmeetingsystem' in fileName:
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
    if commid == 'devServerCluster':
        os.chdir(r'%s\%s\conf' % (zip_dirs, Files))
        with open('application.properties', "r", encoding="utf-8") as f1, open("application1.properties", "w",
                                                                               encoding="utf-8") as f2:
            for line in f1.readlines():
                if 'meeting.cluster=false' in line:
                    f2.write(re.sub('meeting.cluster=false', 'meeting.cluster=True', line))
                else:
                    f2.write(line)
        os.remove('application.properties')
        os.rename("application1.properties", 'application.properties')


untar(package_path+r'\%s'%'mastersmeetingsystem-cdszf-2.6.2-20210114144028-distribution.tar.gz',package_path,'devServerCluster')