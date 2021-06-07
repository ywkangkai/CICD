# encoding=gbk
from common import out_style
import os, sys, yaml, time, zipfile, re, shutil, tarfile
from shutil import copyfile
from common import function
from threading import Thread

curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, "CDSZF.yaml")
f = open(yamlPath, 'r', encoding='ISO-8859-1')
cfg = f.read()
version = yaml.load(cfg, Loader=yaml.FullLoader)
server_commid_Id = version['server_commid_Id']

Server_Web_commid_id = version['Server_Web_commid_id']
CDSZF_Server_Web_commid_id = version['CDSZF_Server_Web_commid_id']
CDSZF_Server_commid_id = version['CDSZF_Server_commid_id']
admin_tool_commid_Id = version['admin_tool_commid_Id']
config_tool_commid = version['config_tool_commid']
cluster_tool_commid = version['cluster_tool_commid']
client_commid_Id = version['client_commid']
client_picviewer_commid = version['client_picviewer_commid']
client_videoplayer_commid = version['client_videoplayer_commid']
client_wstreader_commid = version['client_wstreader_commid']
CDSZF_Client_commid = version['CDSZF_Client_commid']
Server = version['Server']
CDSZF_Web = version['CDSZF_Web']
Server_Web = version['Server_Web']
CDSZF_Server = version['CDSZF_Server']
admintool = version['admintool']
client = version['client']
client_picviewer = version['client_picviewer']
client_videoplayer = version['client_videoplayer']
client_wstreader = version['client_wstreader']
CDSZF_Client = version['CDSZF_Client']

clustertool = version['clustertool']
configtool = version['configtool']
package_path = os.path.abspath(os.path.dirname(__file__)) + '\outpath'


# 强制删除文件夹
def delete_file(path):
    os.system('rmdir /s /q %s' % path)


class westone_CDSZF_server():
    def __init__(self, path, commid, Version_type, server_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir

    def build_server(self):
        out_style.printGreen('开始构建项目：成都市定制服务端......！')
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'smeetingsystem-server', self.commid, server_commid_Id, Server)
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'CDSZF-smeetingsystem-server-web', self.commid, CDSZF_Server_Web_commid_id,
                          CDSZF_Web)
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'smeetingsystem-server-web', self.commid, Server_Web_commid_id, Server_Web)
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'CDSZF-smeetingsystem-server', self.commid, CDSZF_Server_commid_id, CDSZF_Server)

        # 将成都市政府前端中的header.js文件复制到基础版前端对应的路径中
        copyfile(self.path + version['cdszf_web_header_js'] + '\%s' % 'header.js',
                 self.path + version['server_web_header_js'] + '\%s' % 'header.js')

        # 将成都市前端中的header.html文件复制到基础版前端对应的路径中
        copyfile(self.path + version['cdszf_web_header_html'] + '\%s' % 'header.html',
                 self.path + version['server_web_header_html'] + '\%s' % 'header.html')

        # 将成都市前端unitsManage文件下的所有文件复制到基础版本unitsManage中
        function.copy_file(self.path + version['cdszf_web_unitsManage'], self.path + version['server_web_unitsManage'])

        # 将成都市前端BaseView.js文件复制到基础版本中
        copyfile(self.path + version['cdszf_web_BaseView_js'] + '\%s' % 'BaseView.js',
                 self.path + version['server_web_BaseView_js'] + '\%s' % 'BaseView.js')

        # 把成都市政府web中的login.html文件复制到标准版本相应的路径中
        copyfile(self.path + version['cdszf_web_login_html'] + '\%s' % 'login.html',
                 self.path + version['server_web_login_html'] + '\%s' % 'login.html')

        # 把成都市政府web中businessClient.js文件复制到标准版本相应的路径中
        copyfile(self.path + version['cdszf_server_web_businessclient_js'] + '\%s' % 'businessClient.js',
                 self.path + version['server_web_businessclient_js'] + '\%s' % 'businessClient.js')

        # 把成都市政府web中sider.js文件复制到标准版本相应的路径中
        # copyfile(cdszf_server_web_sider+'\%s'%'sider.js',server_web_sider+'\%s'%'sider.js')

        # 把成都市政府web中sider.html文件复制到标准版本相应的路径中
        # copyfile(cdszf_server_web_sider_html+'\%s'%'sider.html',server_web_sider_html+'\%s'%'sider.html')

        # 把成都市政府web中除开.git文件外的所有文件复制到标准版本的static文件中去,需要判断基础版本对应的路径是否存在static文件
        function.copy_file(self.path + version['web_smsManage_path'], self.path + version['server_smsManage_path'])
        if os.path.exists(r'%s\%s' % (self.path, version['cdszf_server_static'])):
            function.copy_file(r'%s\smeetingsystem-server-web' % self.path,
                               r'%s\%s' % (self.path, version['cdszf_server_static']))
        else:
            os.makedirs(r'%s\%s' % (self.path, version['cdszf_server_static']))
            function.copy_file(r'%s\smeetingsystem-server-web' % self.path,
                               r'%s\%s' % (self.path, version['cdszf_server_static']))
        '''
        # copyfile(web_systemParams_html_path+r'\systemParams.html',server_systemParams_html_path+r'\systemParams.html')
        #
        # copyfile(r'%s\CDSZF-smeetingsystem-server-web\login.html' %self.path,
        #          r'%s\smeetingsystem-server\src\main\resources\templates\login.html' %self.path)
        #
        # self.content_replace(web_smsManage_path_js,
        #         server_smsManage_path_js,'DEFINIESTART','DEFINEEND','DEFINESTART','DEFINEEND')
        #
        # self.content_blank_replace(web_smsManage_path_js,server_smsManage_path_js,'EVENTSTART_SRC','EVENTEND_SRC',
        #                            '/*EVENTSTART_DEST*/')
        #
        # self.content_blank_replace(web_smsManage_path_js, server_smsManage_path_js, 'INITSTART_SRC', 'INITEND_SRC',
        #                            '/*INITSTART_DEST*/')
        #
        # self.content_blank_replace(web_smsManage_path_js, server_smsManage_path_js, 'BUSINESSSTART_SRC', 'BUSINESSEND_SRC',
        #                            '/*BUSINESSSTART_DEST*/')
        '''

        # 构建成都市定制包，并将其复制到bulidpackage\cdszf\outpath路径中
        os.chdir(r'%s\CDSZF-smeetingsystem-server' % self.path)
        # 成都市定制包打包命令
        os.system('mvn package -Ptest')
        # 将打好后的包移动到outpath路径中
        Path = []
        File = []
        for root, dirs, files in os.walk(self.server_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.gz':
                    Path.append(os.path.join(root, file))
                    File.append(file)
        copyfile(Path[0], r'%s\%s' % (package_path, File[0]))
        del Path[0]
        del File[0]
        # 包移动到指定路径后,获取包名
        zip_name = ''
        for root, dirs, files in os.walk(package_path):
            for file in files:
                if 'mastersmeetingsystem-cdszf' in file:
                    zip_name = file
        # 判断打包,如果命令行参数输入的是-tdevServerCluster表明是打集群版本
        if self.Version_type == '-tdevServerCluster':
            self.untarCluster(package_path + r'\%s' % zip_name, package_path)
        # 否则打单机版本
        else:
            self.untar(package_path + r'\%s' % zip_name, package_path)
        # 删除压缩包,保留源文件
        function.preDelPic(package_path)
        # 配置修改完成后,对文件夹压缩
        function.make_targz(package_path + r'\%s' % zip_name, package_path + r'\%s' % (self.file_name(package_path)))
        os.chdir(package_path)
        # 删除文件夹,保留压缩文件
        os.system('rmdir /s /q %s' % self.file_name(package_path))
        # 需要删除放入的jar包,保证每一次打包时的jar包都是最新的
        list = os.listdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        os.chdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        for file_name in list:
            if file_name.endswith('.jar') or file_name.endswith('.gz'):
                os.remove(file_name)
        out_style.printGreen('成都市定制服务包构建完成')

        # p = Thread(target=delete_file(self.path))
        # p.start()

    # 解压tar.gz格式的压缩包并生成集群配置
    def untarCluster(self, fname, zip_dirs):
        """
        :param fname: 解压文件路径
        :param zip_dirs: 解压后存放路径
        :return:
        """
        t = tarfile.open(fname)
        t.extractall(path=zip_dirs)
        file_zip_name = ''
        Files = self.file_name(zip_dirs)
        for root, dirs, files in os.walk(package_path + '\%s\lib' % Files):
            for fileName in files:
                # if 'AO-ULT-FSsmeetingsystem' in fileName:
                if 'mastersmeetingsystem' in fileName:
                    file_zip_name = fileName

        os.chdir(r'%s\%s\conf' % (zip_dirs, Files))
        with open('application.properties', "r", encoding="utf-8") as f1, open("application1.properties", "w",
                                                                               encoding="utf-8") as f2:
            for line in f1.readlines():
                if 'meeting.cluster=false' in line:
                    f2.write(re.sub('meeting.cluster=false', 'meeting.cluster=true', line))
                else:
                    f2.write(line)
        os.remove('application.properties')
        os.rename("application1.properties", 'application.properties')
        time.sleep(5)

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

    # 解压tar.gz格式的压缩包并生成单机配置
    def untar(self, fname, zip_dirs):
        """
        :param fname: 解压文件路径
        :param zip_dirs: 解压后存放路径
        :return:
        """
        t = tarfile.open(fname)
        t.extractall(path=zip_dirs)
        file_zip_name = ''
        Files = self.file_name(zip_dirs)
        for root, dirs, files in os.walk(package_path + '\%s\lib' % Files):
            for fileName in files:
                # if 'AO-ULT-FSsmeetingsystem' in fileName:
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

    # 获取文件夹名
    def file_name(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            for file_names in dirs:
                if 'mastersmeetingsystem' in file_names:
                    name = file_names
        return name


class Westone_CDSZF_client():
    def __init__(self, path, commid, Version_type):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type

    def builed_client(self):
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'smeetingsystem-client', self.commid, client_commid_Id, client)
        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'CDSZF-smeetingsystem-client', self.commid, CDSZF_Client_commid, CDSZF_Client)

        # 构建带T卡版本与不带T卡版本的客户端
        for i in range(1, 3):
            if i == 1:
                out_style.printGreen('正在构建项目：客户端带T卡APK版本......！')
                time.sleep(2)
            else:
                out_style.printGreen('正在构建项目：客户端不带T卡APK版本......！')
                time.sleep(2)
            # 市委apk路径
            committee_path = r'%s\%s' % (self.path, version['committee_path'])
            # 市政府apk路径
            gov_path = r'%s\%s' % (self.path, version['gov_path'])
            committeeFile = []
            govFile = []
            os.chdir(r'%s\CDSZF-smeetingsystem-client' % self.path)
            # 修改打包配置文件同时打带T卡与不带T卡版本
            with open('build.gradle', "r", encoding="utf-8") as f1, open("build1.gradle", "w",
                                                                         encoding="utf-8") as f2:
                for line in f1.readlines():
                    if 'need_tfcard = "false"' in line:
                        print(line)
                        f2.write(re.sub('need_tfcard = "false"', 'need_tfcard = "true"', line))
                    elif 'need_tfcard = "true"' in line:
                        print(line)
                        f2.write(re.sub('need_tfcard = "true"', 'need_tfcard = "false"', line))
                    else:
                        f2.write(line)
            os.remove('build.gradle')
            os.rename("build1.gradle", 'build.gradle')
            # 客户端打包命令
            os.system('gradle --daemon --parallel --max-workers 10 assembleRelease')
            # 获取市委apk名称
            for root, dirs, files in os.walk(committee_path):
                committeeFile.append(files[0])
            # 获取市政府apk名称
            for root, dirs, files in os.walk(gov_path):
                govFile.append(files[0])
            # 拼接市委apk完整路径
            committee_zip_file = package_path + '\%s.zip' % committeeFile[0]
            # 拼接市政府apk完成路径
            govFile_zip_file = package_path + '\%s.zip' % govFile[0]

            function.get_zip(committee_path, committeeFile, committee_zip_file)
            function.get_zip(gov_path, govFile, govFile_zip_file)




class Westone_all():
    def __init__(self, path, commid, Version_type, server_dir, tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.tool_dir = tool_dir

    def build_all_package(self):
        westone_CDSZF_server(self.path, self.commid, self.Version_type, self.server_dir).build_server()
        #Westone_CDSZF_tools(self.path, self.commid, self.Version_type, self.tool_dir).build_tools()
        Westone_CDSZF_client(self.path, self.commid, self.Version_type).builed_client()
