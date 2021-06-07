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

        out_style.printGreen('��ʼ������Ŀ���ɶ��ж��Ʒ����......��')
        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'smeetingsystem-server', self.commid, server_commid_Id, Server)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'CDSZF-smeetingsystem-server-web', self.commid, CDSZF_Server_Web_commid_id,
                          CDSZF_Web)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'smeetingsystem-server-web', self.commid, Server_Web_commid_id, Server_Web)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'CDSZF-smeetingsystem-server', self.commid, CDSZF_Server_commid_id, CDSZF_Server)

        # ���ɶ�������ǰ���е�header.js�ļ����Ƶ�������ǰ�˶�Ӧ��·����
        copyfile(self.path + version['cdszf_web_header_js'] + '\%s' % 'header.js',
                 self.path + version['server_web_header_js'] + '\%s' % 'header.js')

        # ���ɶ���ǰ���е�header.html�ļ����Ƶ�������ǰ�˶�Ӧ��·����
        copyfile(self.path + version['cdszf_web_header_html'] + '\%s' % 'header.html',
                 self.path + version['server_web_header_html'] + '\%s' % 'header.html')

        # ���ɶ���ǰ��unitsManage�ļ��µ������ļ����Ƶ������汾unitsManage��
        function.copy_file(self.path + version['cdszf_web_unitsManage'], self.path + version['server_web_unitsManage'])

        # ���ɶ���ǰ��BaseView.js�ļ����Ƶ������汾��
        copyfile(self.path + version['cdszf_web_BaseView_js'] + '\%s' % 'BaseView.js',
                 self.path + version['server_web_BaseView_js'] + '\%s' % 'BaseView.js')

        # �ѳɶ�������web�е�login.html�ļ����Ƶ���׼�汾��Ӧ��·����
        copyfile(self.path + version['cdszf_web_login_html'] + '\%s' % 'login.html',
                 self.path + version['server_web_login_html'] + '\%s' % 'login.html')

        # �ѳɶ�������web��businessClient.js�ļ����Ƶ���׼�汾��Ӧ��·����
        copyfile(self.path + version['cdszf_server_web_businessclient_js'] + '\%s' % 'businessClient.js',
                 self.path + version['server_web_businessclient_js'] + '\%s' % 'businessClient.js')

        # �ѳɶ�������web��sider.js�ļ����Ƶ���׼�汾��Ӧ��·����
        # copyfile(cdszf_server_web_sider+'\%s'%'sider.js',server_web_sider+'\%s'%'sider.js')

        # �ѳɶ�������web��sider.html�ļ����Ƶ���׼�汾��Ӧ��·����
        # copyfile(cdszf_server_web_sider_html+'\%s'%'sider.html',server_web_sider_html+'\%s'%'sider.html')

        # �ѳɶ�������web�е������ļ����Ƶ���׼�汾��static�ļ���
        # �ѳɶ�������web�г���.git�ļ���������ļ����Ƶ���׼�汾��static�ļ���ȥ,��Ҫ�жϻ����汾��Ӧ��·���Ƿ����static�ļ�
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

        # �޸ı�׼�汾��pom.xml�ļ����ѻ����ر�
        os.chdir(r'%s\smeetingsystem-server' % self.path)
        with open('pom.xml', "r", encoding="utf-8") as f1, open("pom1.xml", "w", encoding="utf-8") as f2:
            for line in f1.readlines():
                if "<obfuscate>true</obfuscate>" in line:
                    f2.write(re.sub('<obfuscate>true</obfuscate>', '<obfuscate>false</obfuscate>', line))
                else:
                    f2.write(line)
        os.remove('pom.xml')
        os.rename("pom1.xml", 'pom.xml')

        # �ѱ�׼�汾�е�Application.java�ļ��е���Ӧ����ɾ��
        function.blank_to_content(
            r'%s\smeetingsystem-server\src\main\java\com\westone\meeting\%s' % (self.path, 'Application.java'),
            'StartDelete', 'EndDelete')
        function.blank_to_content(
            r'%s\smeetingsystem-server\src\main\java\com\westone\meeting\%s' % (self.path, 'Application.java'),
            'StartComment', 'EndComment')

        # ������׼��Ʒ��,ע����Ҫ��Ӧ��ɶ��е�����
        os.chdir(r'%s\smeetingsystem-server' % self.path)
        os.system('mvn clean package -Ptest -Dplugin.name=%s' % 'AO-ULT-FS')

        # ɾ���ɶ��к����Ӧ·���µ�jar��
        os.chdir(r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib' % self.path)
        list = os.listdir(r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib' % self.path)
        os.remove(list[0])

        # �Ѵ�õı�׼�汾�е�jar�����Ƶ��ɶ��ж��ư汾�е���Ӧ·����ȥ
        file_list = []
        for root, dirs, files in os.walk(r'%s\smeetingsystem-server\target' % self.path):
            for file in files:
                if file.endswith('.jar'):
                    file_list.append(file)
        copyfile(r'%s\smeetingsystem-server\target\%s' % (self.path, file_list[0]),
                 r'%s\CDSZF-smeetingsystem-server\src\main\resources\lib\%s' % (self.path, file_list[0]))

        # �޸ĳɶ��к���е�pom.xml�ļ�����Ӧ����
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

        # �����ɶ��ж��ư��������临�Ƶ�bulidpackage\cdszf\outpath·����
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
        # �ж��Ƿ��ǵ������Ǽ�Ⱥ
        self.SC_untar(package_path + r'\%s' % zip_name, package_path)
        # ɾ��ԭ��õĳɶ���ѹ����
        function.preDelPic(package_path)
        # �������޸ĺõ��ļ��н���ѹ��
        function.make_targz(package_path + r'\%s' % zip_name, package_path + r'\%s' % (self.file_name(package_path)))
        os.chdir(package_path)
        # ɾ��jar��,��֤ÿ��jar�������µ�
        os.system('rmdir /s /q %s' % self.file_name(package_path))
        list = os.listdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        os.chdir(r'%s\CDSZF-smeetingsystem-server\target' % self.path)
        for file_name in list:
            if file_name.endswith('.jar') or file_name.endswith('.gz'):
                os.remove(file_name)
        out_style.printGreen('�ɶ��ж��Ʒ�����������')
        time.sleep(5)
        # os.system('rmdir /s /q %s'%self.path)

    # ��ѹtar.gz��ʽ��ѹ����
    def SC_untar(self, fname, zip_dirs):
        """
        :param fname: ��ѹ�ļ�·��
        :param zip_dirs: ��ѹ����·��
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

    # ��ȡ�ļ�����
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
        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'smeetingsystem-client', self.commid, client_commid_Id, client)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'CDSZF-smeetingsystem-client', self.commid, CDSZF_Client_commid, CDSZF_Client)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'smeetingsystem-client-picviewer', self.commid, client_picviewer_commid, client_picviewer)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'smeetingsystem-client-videoplayer', self.commid, client_videoplayer_commid, client_videoplayer)

        # ��������Ĵ��·�����жϴ�·���Ƿ��У�û��ֱ�Ӵ�����ȡ���룬��ֱ�Ӹ��´���
        function.get_code(self.path, 'wstreader', self.commid, client_wstreader_commid, client_wstreader)

        os.chdir(r'%s\smeetingsystem-client' % self.path)
        out_style.printGreen('��ʼ����meeting.aar�ļ�')
        # ����meeting.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :meeting:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['meeting_aar'], 'meeting-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'meeting-release.aar'))

        out_style.printGreen('��ʼ����common.aar�ļ�')
        # ����common.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :common:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['common_aar'], 'common-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'common-release.aar'))

        out_style.printGreen('��ʼ����tflibrary.aar�ļ�')
        # ����tflibrary.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :tflibrary:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['tflibrary_aar'], 'tflibrary-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'tflibrary-release.aar'))

        os.chdir(r'%s\smeetingsystem-client-videoplayer' % self.path)
        out_style.printGreen('��ʼ����videoplayerlib.aar�ļ�')
        # ����videoplayerlib.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :videoplayerlib:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['videoplayerlib_aar'], 'videoplayerlib-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'videoplayerlib-release.aar'))

        os.chdir(r'%s\smeetingsystem-client-picviewer' % self.path)
        out_style.printGreen('��ʼ����LargeImage.aar�ļ�')
        # LargeImage.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :LargeImage:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['LargeImage_aar'], 'LargeImage-release.aar'),
                 r'%s\%s\%s' % (self.path,version['cdszf_lib'], 'LargeImage-release.aar'))

        os.chdir(r'%s\wstreader' % self.path)
        out_style.printGreen('��ʼ����readerlib.aar�ļ�')
        # readerlib.aar�ļ�,�����临�Ƶ�ָ��·����
        os.system('gradle :readerlib:assembleRelease')
        copyfile(r'%s\%s\%s' % (self.path,version['readerlib_aar'], 'readerlib-release.aar'),
                 r'%s\CDSZF-smeetingsystem-client\app\libs\%s' % (self.path, 'readerlib-release.aar'))

        # ������T���벻��T���汾
        for i in range(1, 3):
            if i == 1:
                out_style.printGreen('���ڹ�����Ŀ���ͻ��˴�T��APK�汾......��')
                time.sleep(2)
            else:
                out_style.printGreen('���ڹ�����Ŀ���ͻ��˲���T��APK�汾......��')
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


