# encoding=gbk
from common import out_style
import time
import os
import zipfile
import re
import shutil
import tarfile


# ��ȡ���µĴ���(�����ж�version_type�ǲ���-tall)
def get_code(path, git, commid, yamlbranch, clone_code):
    '''

    :param path: �ֿ�����ŵ����صĵ�ַ
    :param git: �ֿ��ַ
    :param commid: �����ж��ǲ���master��֧
    :param yamlbranch: ������֧
    :param clone_code: ��ȡ��������
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


# ��ȡ���µĴ���(��Ҫ�ж�version_type�ǲ���-tall)
def get_allcode(path, git, commid, yamlbranch, version_type, clone_code):
    '''

    :param path: �ֿ�����ŵ����صĵ�ַ
    :param git: �ֿ��ַ
    :param commid: �����ж��ǲ���master��֧
    :param yamlbranch: ������֧
    :param version_type: �ж��ǲ��Ǵ����еİ�
    :param clone_code: ��ȡ��������
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


# ��ĳ��Ŀ¼�µ������ļ����ļ��и��Ƶ���һ��Ŀ¼
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


# ��ȡ�ļ�����
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file_names in dirs:
            if 'mastersmeetingsystem' in file_names:
                name = file_names
    return name


# ���ѹ��
def get_zip(path, files, zip_name):
    os.chdir(path)
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        zp.write(file)
    zp.close()
    time.sleep(5)
    out_style.printGreen('ѹ������Ѵ�����ָ��Ŀ¼......��')


# ���й�����ѹ��
def get_admintool_zip(respath, dir, copy_in_path, copy_out_path, outFullName):
    """
    :param dir: ��Ҫ��һ��·�����ж�distĿ¼���Ƿ���res�ļ���
    :param copy_in_path: ��src��·����Ŀ�����õ���Ŀ¼�µ�res�ļ����и���
    :param copy_out_path:�����Ƶ�res�ļ���ճ����distĿ¼��
    :param outFullName:��ѹ�����ļ���ŵ�·��
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


# ���й�����ѹ��
def get_serverconfig_zip(
        configrespath,
        dir,
        copy_in_path,
        copy_out_path,
        outFullName):
    """
       :param dir: ��Ҫ��һ��·�����ж�distĿ¼���Ƿ���res�ļ���
       :param copy_in_path: ��src��·����Ŀ�����õ���Ŀ¼�µ�res�ļ����и���
       :param copy_out_path:�����Ƶ�res�ļ���ճ����distĿ¼��
       :param outFullName:��ѹ�����ļ���ŵ�·��
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


# ���м�Ⱥ����ѹ��
def get_clusterconfig_zip(
        clusterrespath,
        dir,
        copy_in_path,
        copy_out_path,
        outFullName):
    """
           :param dir: ��Ҫ��һ��·�����ж�distĿ¼���Ƿ���res�ļ���
           :param copy_in_path: ��src��·����Ŀ�����õ���Ŀ¼�µ�res�ļ����и���
           :param copy_out_path:�����Ƶ�res�ļ���ճ����distĿ¼��
           :param outFullName:��ѹ�����ļ���ŵ�·��
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


# ɾ���ļ�
def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


# ���ڱ��ʽ�滻�޿հ׵�����
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


# ���ڱ��ʽ�滻�пհ׵�����
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


# �ÿ��ַ���ȥ�滻�����ݵĲ���
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


# ɾ��ָ���ļ�
def preDelPic(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".tar.gz"):
                os.remove(os.path.join(root, name))


# ���ļ�ѹ��Ϊtar��ʽ
def make_targz(output_filename, source_dir):
    """
    :param output_filename: �Լ�ȡһ��ѹ���ļ���
    :param source_dir: ѹ�����ŵ�·��
    :return:
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


# ���ͻ��˴�õİ�ѹ���������outpath·��
def get_zip(path, files, zip_name):
    os.chdir(path)
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        zp.write(file)
    zp.close()
    time.sleep(5)
    out_style.printGreen('ѹ������Ѵ�����ָ��Ŀ¼......��')
