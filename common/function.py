# encoding=gbk
from common import out_style
import time
import os
import zipfile
import re
import shutil
import tarfile


# 获取最新的代码(无需判断version_type是不是-tall)
def get_code(path, git, commid, yamlbranch, clone_code):
    '''

    :param path: 仓库代码存放到本地的地址
    :param git: 仓库地址
    :param commid: 用来判断是不是master分支
    :param yamlbranch: 其他分支
    :param clone_code: 拉取代码命令
    :return:
    '''
    if os.path.exists(r'%s\%s' % (path, git)) and os.path.exists(r'%s' % path):
        os.chdir('%s\\%s' % (path, git))
        print(commid)
        if commid == 'master':
            os.system('git checkout master')
            os.system('git status')
            os.system('git pull')
            time.sleep(5)
        else:
            os.system('git checkout %s' % yamlbranch)
            os.system('git status')
            os.system('git pull')
            time.sleep(5)
    else:
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
        os.chdir(path)
        print(os.getcwd())
        if commid == 'master':
            os.system(clone_code)
            time.sleep(5)
        else:
            os.system(clone_code)
            print(os.getcwd())
            os.chdir('%s\\%s' % (path, git))
            os.system('git checkout %s' % yamlbranch)
            os.system('git status')
            time.sleep(5)


# 获取最新的代码(需要判断version_type是不是-tall)
def get_allcode(path, git, commid, yamlbranch, version_type, clone_code):
    '''

    :param path: 仓库代码存放到本地的地址
    :param git: 仓库地址
    :param commid: 用来判断是不是master分支
    :param yamlbranch: 其他分支
    :param version_type: 判断是不是打所有的包
    :param clone_code: 拉取代码命令
    :return:
    '''
    if os.path.exists(r'%s\%s' % (path, git)) and os.path.exists(r'%s' % path):
        os.chdir('%s\\%s' % (path, git))
        print(os.getcwd())
        if commid == 'master':
            os.system('git checkout master')
            os.system('git status')
            os.system('git pull')
            time.sleep(5)
        else:
            os.system('git checkout %s' % yamlbranch)
            os.system('git status')
            os.system('git pull')
            time.sleep(5)
    else:
        if version_type == '-tall':
            os.chdir(r'%s' % path)
            if commid == 'master':
                os.system(clone_code)
            else:
                os.system(clone_code)
                os.chdir('%s\\%s' % (path, git))
                os.system('git checkout %s' % yamlbranch)
                os.system('git status')
                os.system('git pull')
                time.sleep(5)
        else:
            os.makedirs(r'%s' % path)
            os.chdir(r'%s' % path)
            if commid == 'master':
                os.system(clone_code)
            else:
                os.system(clone_code)
                os.chdir('%s\\%s' % (path, git))
                os.system('git checkout %s' % yamlbranch)
                os.system('git status')
                os.system('git pull')
                time.sleep(5)


# 将某个目录下的所有文件及文件夹复制到另一个目录
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


# 获取文件夹名
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file_names in dirs:
            if 'mastersmeetingsystem' in file_names:
                name = file_names
    return name


# 打包压缩
def get_zip(path, files, zip_name):
    os.chdir(path)
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        zp.write(file)
    zp.close()
    time.sleep(5)
    out_style.printGreen('压缩完成已存在至指定目录......！')


# 进行管理工具压缩
def get_admintool_zip(respath, dir, copy_in_path, copy_out_path, outFullName):
    """
    :param dir: 需要传一个路径，判断dist目录下是否有res文件夹
    :param copy_in_path: 传src的路径，目的是拿到该目录下的res文件进行复制
    :param copy_out_path:将复制的res文件，粘贴到dist目录下
    :param outFullName:将压缩的文件存放的路径
    :return:
    """
    os.makedirs(respath)
    copy_file(copy_in_path, copy_out_path)
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dir):
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(
                os.path.join(
                    path, filename), os.path.join(
                    fpath, filename))
    zip.close()


# 进行管理工具压缩
def get_serverconfig_zip(
        configrespath,
        dir,
        copy_in_path,
        copy_out_path,
        outFullName):
    """
       :param dir: 需要传一个路径，判断dist目录下是否有res文件夹
       :param copy_in_path: 传src的路径，目的是拿到该目录下的res文件进行复制
       :param copy_out_path:将复制的res文件，粘贴到dist目录下
       :param outFullName:将压缩的文件存放的路径
       :return:
    """
    os.makedirs(configrespath)
    copy_file(copy_in_path, copy_out_path)
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dir):
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(
                os.path.join(
                    path, filename), os.path.join(
                    fpath, filename))
    zip.close()


# 进行集群工具压缩
def get_clusterconfig_zip(
        clusterrespath,
        dir,
        copy_in_path,
        copy_out_path,
        outFullName):
    """
           :param dir: 需要传一个路径，判断dist目录下是否有res文件夹
           :param copy_in_path: 传src的路径，目的是拿到该目录下的res文件进行复制
           :param copy_out_path:将复制的res文件，粘贴到dist目录下
           :param outFullName:将压缩的文件存放的路径
           :return:
    """
    os.makedirs(clusterrespath)
    copy_file(copy_in_path, copy_out_path)
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dir):
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(
                os.path.join(
                    path, filename), os.path.join(
                    fpath, filename))
    zip.close()


# 删除文件
def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


# 正在表达式替换无空白的内容
def content_replace(
        copycontent,
        outcontent,
        copy_satrt_lable,
        copy_end_lable,
        out_start_lable,
        out_end_lable):
    new_content = ''
    with open(copycontent, 'r', encoding='utf-8') as f1:
        content = f1.read()
        new_string = re.compile(
            r'\/\*%s_SRC\*\/(.*?)\/\*%s_SRC\*\/' %
            (copy_satrt_lable, copy_end_lable), re.DOTALL)
        new_content = new_string.findall(content)[0] + new_content
    old_content = ''
    with open(outcontent, 'r', encoding='utf-8') as f2:
        content1 = f2.read()
        old_string = re.compile(
            r'\/\*%s_DEST\*\/(.*?)\/\*%s_DEST\*\/' %
            (out_start_lable, out_end_lable), re.DOTALL)
        old_content = old_string.findall(content1)[0] + old_content
        new_content1 = content1.replace(old_content, new_content)
        with open(outcontent, 'w', encoding='utf-8') as f3:
            f3.write(new_content1)


# 正在表达式替换有空白的内容
def content_blank_replace(
        copycontent,
        outcontent,
        copy_start,
        copy_end,
        out_string):
    old_string = out_string
    new_string = out_string
    with open(copycontent, 'r', encoding='utf-8') as f1:
        content = f1.read()
        aaa = re.compile(
            r'\/\*%s\*\/(.*?)\/\*%s\*\/' %
            (copy_start, copy_end), re.DOTALL)
        hd_new_content = new_string + aaa.findall(content)[0]
    with open(outcontent, 'r', encoding='utf-8') as oldfile:
        content = oldfile.read()
        new_content = content.replace(old_string, hd_new_content)
        with open(outcontent, 'w', encoding='utf-8') as newfile:
            newfile.write(new_content)


# 用空字符串去替换有内容的部分
def blank_to_content(text_dir, out_start_lable, out_end_lable):
    new_content = ''
    old_content = ''
    with open(text_dir, 'r', encoding='utf-8') as f2:
        content1 = f2.read()
        old_string = re.compile(
            r'\/\*%s_IfNotConfused\*\/(.*?)\/\*%s_IfNotConfused\*\/' %
            (out_start_lable, out_end_lable), re.DOTALL)
        old_content = old_string.findall(content1)[0] + old_content
        new_content1 = content1.replace(old_content, new_content)
        with open(text_dir, 'w', encoding='utf-8') as f3:
            f3.write(new_content1)


# 删除指定文件
def preDelPic(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".tar.gz"):
                os.remove(os.path.join(root, name))


# 将文件压缩为tar格式
def make_targz(output_filename, source_dir):
    """
    :param output_filename: 自己取一个压缩文件名
    :param source_dir: 压缩后存放的路径
    :return:
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


# 将客户端打好的包压缩并存放至outpath路径
def get_zip(path, files, zip_name):
    os.chdir(path)
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        zp.write(file)
    zp.close()
    time.sleep(5)
    out_style.printGreen('压缩完成已存在至指定目录......！')
