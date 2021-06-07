# encoding=gbk
from common import out_style, function
import os, sys, yaml, time, zipfile, re, shutil, tarfile
from shutil import copyfile

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

        # 把成都市政府web中的所有文件复制到标准版本的static文件中
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

        # 修改标准版本中pom.xml文件，把混淆关闭
        os.chdir(r'%s\smeetingsystem-server' % self.path)
        with open('pom.xml', "r", encoding="utf-8") as f1, open("pom1.xml", "w", encoding="utf-8") as f2:
            for line in f1.readlines():
                if "<obfuscate>true</obfuscate>" in line:
                    f2.write(re.sub('<obfuscate>true</obfuscate>', '<obfuscate>false</obfuscate>', line))
                else:
                    f2.write(line)
        os.remove('pom.xml')
        os.rename("pom1.xml", 'pom.xml')

        # 把标准版本中的Application.java文件中的相应内容删除
        function.blank_to_content(
            r'%s\smeetingsystem-server\src\main\java\com\westone\meeting\%s' % (self.path, 'Application.java'),
            'StartDelete', 'EndDelete')
        function.blank_to_content(
            r'%s\smeetingsystem-server\src\main\java\com\westone\meeting\%s' % (self.path, 'Application.java'),
            'StartComment', 'EndComment')

        # 构建标准产品包,注意需要对应打成都市的配置
        os.chdir(r'%s\smeetingsystem-server' % self.path)
        os.system('mvn clean package -Ptest -Dplugin.name=%s' % 'AO-ULT-FS')

        # 删除成都市后端相应路径下的jar包
        os.chdir(r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib' % self.path)
        list = os.listdir(r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib' % self.path)
        os.remove(list[0])

        # 把打好的标准版本中的jar包复制到成都市定制版本中的相应路径中去
        file_list = []
        for root, dirs, files in os.walk(r'%s\smeetingsystem-server\target' % self.path):
            for file in files:
                if file.endswith('.jar'):
                    file_list.append(file)
        copyfile(r'%s\smeetingsystem-server\target\%s' % (self.path, file_list[0]),
                 r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib\%s' % (self.path, file_list[0]))

        # 修改成都市后端中的pom.xml文件中相应内容
        os.chdir(r'%s\CDSZF-smeetingsystem-server' % self.path)
        tar_name = '<systemPath>${basedir}/src/main/resources/lib/%s</systemPath>' % file_list[0]
        with open('pom.xml', "r", encoding="utf-8") as f1, open("pom1.xml", "w", encoding="utf-8") as f2:
            for line in f1.readlines():
                if "{basedir}/src/main/resources/lib" in line:
                    f2.write('            ' + tar_name + "\n")
                else:
                    f2.write(line)
        os.remove('pom.xml')
        os.rename("pom1.xml", 'pom.xml')

        # 构建成都市定制包，并将其复制到bulidpackage\cdszf\outpath路径中
        os.chdir(r'%s\CDSZF-smeetingsystem-server' % self.path)
        os.system('mvn package -Ptest -Dplugin.name=%s' % 'AO-ULT-FS')
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
        zip_name = ''
        for root, dirs, files in os.walk(package_path):
            for file in files:
                if 'AO-ULT-FSsmeetingsystem' in file:
                    zip_name = file
        # 判读是否是单机还是集群
        self.SC_untar(package_path + r'\%s' % zip_name, package_path)
        # 删除原打好的成都市压缩包
        function.preDelPic(package_path)
        # 将配置修改好的文件夹进行压缩
        function.make_targz(package_path + r'\%s' % zip_name, package_path + r'\%s' % (self.file_name(package_path)))
        os.chdir(package_path)
        # 删除jar包,保证每次jar都是最新的
        os.system('rmdir /s /q %s' % self.file_name(package_path))
        list = os.listdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        os.chdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        for file_name in list:
            if file_name.endswith('.jar') or file_name.endswith('.gz'):
                os.remove(file_name)
        out_style.printGreen('成都市定制服务包构建完成')
        time.sleep(5)
        # os.system('rmdir /s /q %s'%self.path)

    # 解压tar.gz格式的压缩包
    def SC_untar(self, fname, zip_dirs):
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
                if 'AO-ULT-FSsmeetingsystem' in fileName:
                    # if 'mastersmeetingsystem' in fileName:
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
        if self.commid == 'releaseServerCluster':
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
        if self.Version_type == '-treleaseServerCluster':
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

    # 获取文件夹名
    def file_name(self, file_dir):
        name = ''
        for root, dirs, files in os.walk(file_dir):
            for file_names in dirs:
                # if 'mastersmeetingsystem' in file_names:
                if 'AO-ULT-FSsmeetingsystem' in file_names:
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

        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'smeetingsystem-client-picviewer', self.commid, client_picviewer_commid, client_picviewer)

        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'smeetingsystem-client-videoplayer', self.commid, client_videoplayer_commid, client_videoplayer)

        # 创建代码的存放路径，判断此路径是否有，没有直接创建拉取代码，有直接更新代码
        function.get_code(self.path, 'wstreader', self.commid, client_wstreader_commid, client_wstreader)

        os.chdir(r'%s\smeetingsystem-client' % self.path)
        out_style.printGreen('开始生成meeting.aar文件')
        # 生成meeting.aar文件,并将其复制到指定路径中
        os.system('gradle :meeting:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['meeting_aar'], 'meeting-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'meeting-release.aar'))

        out_style.printGreen('开始生成common.aar文件')
        # 生成common.aar文件,并将其复制到指定路径中
        os.system('gradle :common:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['common_aar'], 'common-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'common-release.aar'))

        out_style.printGreen('开始生成tflibrary.aar文件')
        # 生成tflibrary.aar文件,并将其复制到指定路径中
        os.system('gradle :tflibrary:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['tflibrary_aar'], 'tflibrary-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'tflibrary-release.aar'))

        os.chdir(r'%s\smeetingsystem-client-videoplayer' % self.path)
        out_style.printGreen('开始生成videoplayerlib.aar文件')
        # 生成videoplayerlib.aar文件,并将其复制到指定路径中
        os.system('gradle :videoplayerlib:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['videoplayerlib_aar'], 'videoplayerlib-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'videoplayerlib-release.aar'))

        os.chdir(r'%s\smeetingsystem-client-picviewer' % self.path)
        out_style.printGreen('开始生成LargeImage.aar文件')
        # LargeImage.aar文件,并将其复制到指定路径中
        os.system('gradle :LargeImage:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['LargeImage_aar'], 'LargeImage-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'LargeImage-release.aar'))

        os.chdir(r'%s\wstreader' % self.path)
        out_style.printGreen('开始生成readerlib.aar文件')
        # readerlib.aar文件,并将其复制到指定路径中
        os.system('gradle :readerlib:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['readerlib_aar'], 'readerlib-release.aar'),
                 r'%s\CDSZF-smeetingsystem-client\app\libs\%s' % (self.path, 'readerlib-release.aar'))

        # 构建带T卡与不带T卡版本
        for i in range(1, 3):
            if i == 1:
                out_style.printGreen('正在构建项目：客户端带T卡APK版本......！')
                time.sleep(2)
            else:
                out_style.printGreen('正在构建项目：客户端不带T卡APK版本......！')
                time.sleep(2)
            committee_path = r'%s\%s' % (self.path, version['committee_path'])
            gov_path = r'%s\%s' % (self.path, version['gov_path'])
            committeeFile = []
            govFile = []
            os.chdir(r'%s\CDSZF-smeetingsystem-client' % self.path)
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
            os.system('gradle --daemon --parallel --max-workers 10 assembleRelease')

            for root, dirs, files in os.walk(committee_path):
                committeeFile.append(files[0])

            for root, dirs, files in os.walk(gov_path):
                govFile.append(files[0])
            committee_zip_file = package_path + '\%s.zip' % committeeFile[0]
            govFile_zip_file = package_path + '\%s.zip' % govFile[0]
            function.get_zip(committee_path, committeeFile, committee_zip_file)
            function.get_zip(gov_path, govFile, govFile_zip_file)


