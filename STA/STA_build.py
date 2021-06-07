# encoding=gbk
from common import out_style
import os, sys, yaml, time, zipfile, re, shutil
from shutil import copyfile
from common import function

curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, "STA.yaml")
f = open(yamlPath, 'r', encoding='ISO-8859-1')
cfg = f.read()
version = yaml.load(cfg, Loader=yaml.FullLoader)
server_commid_Id = version['server_commid']
server_web_comm_Id = version['server_Web_commid']
client_commid_Id = version['client_commid']
admin_tool_commid_Id = version['admin_tool_commid']
config_tool_commid = version['config_tool_commid']
cluster_tool_commid = version['cluster_tool_commid']
file_commid = version['file_commid']
server = version['server']
server_web = version['Server_Web']
file_server = version['file_server']
configtool = version['configtool']
admintool = version['admintool']
client = version['client']
clustertool = version['clustertool']
package_path = os.path.abspath(os.path.dirname(__file__)) + '\outpath'


# ����������������Ͳ�Ʒ��������˺�ˣ��ļ���վ�����
class Westone_server():
    # ��gitԶ��cangk��ȡ����
    def __init__(self, path, commid, Version_type, server_dir, file_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.file_dir = file_dir

    def build_server(self):
        out_style.printGreen('���ڽ�����Ŀ����������˰�.......��')
        time.sleep(3)
        function.get_code(self.path, 'smeetingsystem-server-web', self.commid, server_web_comm_Id, server_web)
        function.get_code(self.path, 'smeetingsystem-server', self.commid, server_commid_Id, server)
        if os.path.exists(self.path + version['server_static']):
            function.copy_file(self.path + version['server_web_static'], self.path + version['server_static'])
        else:
            os.makedirs(self.path + version['server_static'])
            function.copy_file(self.path + version['server_web_static'], self.path + version['server_static'])

        Path = []
        File = []
        if self.Version_type == '-tserver' or self.Version_type == '-tall':
            for i in version['all_version']:
                os.chdir('%s\smeetingsystem-server' % self.path)
                os.system('mvn clean package -Ptest -Dplugin.name=%s' % version['all_version'][i])
                for root, dirs, files in os.walk(self.server_dir):
                    for file in files:
                        if os.path.splitext(file)[1] == '.gz':
                            Path.append(os.path.join(root, file))
                            File.append(file)
                print(r'%s\%s' % (package_path, File[0]))
                copyfile(Path[0], r'%s\%s' % (package_path, File[0]))
                del Path[0]
                del File[0]
        out_style.printGreen('����˰�������ɣ�׼�����й����ļ���վ�����......��')
        time.sleep(3)

        # Path = []
        # File = []
        # function.get_code(self.path, 'smeetingsystem-netdisk', self.commid, file_commid, file_server)
        # os.chdir('%s\smeetingsystem-netdisk' % self.path)
        # os.system('mvn install -DskipTests')
        # for root, dirs, files in os.walk(self.file_dir):
        #     for file in files:
        #         if os.path.splitext(file)[1] == '.gz':
        #             Path.append(os.path.join(root, file))
        #             File.append(file)
        # copyfile(Path[0], r'%s\%s' % (package_path, File[0]))
        # del Path[0]
        # del File[0]
        # out_style.printGreen('�ļ���վ������������......��')


# ���������������Ͳ�Ʒ��������ϵͳ�������ߣ�����ϵͳ�����ߣ��ļ���վ������
class Westone_tools():
    def __init__(self, path, commid, Version_type, tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.tool_dir = tool_dir

    def build_tools(self):
        globals()['res_path'] = r'%s\%s' % (self.path, version['res_path'])
        globals()['config_res_path'] = r'%s\%s' % (self.path, version['config_res_path'])
        globals()['cluster_res_path'] = r'%s\%s' % (self.path, version['cluster_res_path'])
        config_res_path = globals()['config_res_path'] + r'\res'
        res_path = globals()['res_path'] + r'\res'
        cluster_res_path = globals()['cluster_res_path'] + r'\res'
        src_res_path = r'%s\%s' % (self.path, version['src_res_path'])
        config_src_res_path = r'%s\%s' % (self.path, version['config_src_res_path'])
        cluster_src_res_path = r'%s\%s' % (self.path, version['cluster_src_res_path'])
        out_style.printGreen('���ڽ�����Ŀ����������ϵͳ��������.......��')
        zip_name = package_path + '\����ϵͳ��������.zip'
        # ��ȡ���߸��¹���Ա�������´��뵽����
        function.get_allcode(self.path, 'smeeting-admin-tool', self.commid, admin_tool_commid_Id, self.Version_type,
                             admintool)
        # �������߹��ߴ������
        os.chdir('%s\smeeting-admin-tool' % self.path)
        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\����ϵͳ��������.pyw')
        out_style.printGreen('����ϵͳ�������߹�����ɣ����й���ѹ��.......��')
        time.sleep(3)
        # �������ߴ������ѹ��
        function.get_admintool_zip(globals()['res_path'] + r'\res', globals()['res_path'], src_res_path, res_path,
                                   zip_name)
        # ��ð�����Ҫɾ��res�ļ�����res�ļ�ÿ�ζ������µ�
        function.del_file(globals()['res_path'])
        out_style.printGreen('����ϵͳ��������ѹ����ɣ����л���ϵͳ��������Ŀ����......��')
        time.sleep(3)

        zip_name = [package_path + '\����ϵͳ�����߲�������ƽ̨.zip', package_path + '\����ϵͳ�����ߴ�����ƽ̨.zip']
        zip_name2 = package_path + '\�ļ���վ������.zip'
        # ��ȡ���߸��°�װ�������´��뵽����
        function.get_code(self.path, 'smeeting-server-config', self.commid, config_tool_commid, configtool)
        # ѭ������,�ֿ��������ƽ̨�Ĺ����벻������ƽ̨�Ĺ���,��Ҫ�޸������ļ�
        for i in range(0, len(zip_name)):
            os.chdir('%s\smeeting-server-config\src' % self.path)
            with open('����ϵͳ������.pyw', "r", encoding="utf-8") as f1, open("����ϵͳ������1.pyw", "w", encoding="utf-8") as f2:
                for line in f1.readlines():
                    if "isCDSZF = True" in line:
                        f2.write(re.sub('isCDSZF = True', 'isCDSZF = False', line))
                    elif "isCDSZF = False" in line:
                        f2.write(re.sub('isCDSZF = False', 'isCDSZF = True', line))
                    else:
                        f2.write(line)
            os.remove('����ϵͳ������.pyw')
            os.rename("����ϵͳ������1.pyw", '����ϵͳ������.pyw')
            os.chdir('%s\smeeting-server-config' % self.path)
            # �����ߴ������
            os.system(
                'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\����ϵͳ������.pyw')
            # �������߰�����Ҫ��
            function.get_serverconfig_zip(globals()['config_res_path'] + r'\res', globals()['config_res_path'],
                                          config_src_res_path, config_res_path, zip_name[i])
            # ��ð�����Ҫɾ��res�ļ�����res�ļ�ÿ�ζ������µ�
            function.del_file(globals()['config_res_path'])
            out_style.printGreen('����ϵͳ�����߹�����Ŀ�������......��')
            time.sleep(2)
        # �ļ���վ�������
        os.chdir('%s\smeeting-server-config\src' % self.path)
        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\�ļ���վ������.pyw')
        # ���ļ���վ���߽��д��
        function.get_serverconfig_zip(globals()['config_res_path'] + r'\res', globals()['config_res_path'],
                                      config_src_res_path, config_res_path, zip_name2)
        # ��ð�����Ҫɾ��res�ļ�����res�ļ�ÿ�ζ������µ�
        function.del_file(globals()['config_res_path'])
        out_style.printGreen('�ļ���վ��������Ŀ�������,��ʼ������Ⱥ������Ŀ����......��')
        time.sleep(2)

        zip_path1 = package_path + '\smeetingserver��������emqx������.zip'
        # ��ȡ���߸��¼�Ⱥ���ߴ��뵽����
        function.get_code(self.path, 'smeeting-server-config-cluster', self.commid, cluster_tool_commid, clustertool)
        os.chdir('%s\smeeting-server-config-cluster' % self.path)
        out_style.printGreen('smeetingserver��������emqx�����߹�����ɣ����ڽ����ļ�ѹ��......��')
        time.sleep(2)
        # ѹ����Ⱥ����
        function.get_clusterconfig_zip(globals()['cluster_res_path'] + r'\res', globals()['cluster_res_path'],
                                       cluster_src_res_path, cluster_res_path, zip_path1)
        function.del_file(globals()['cluster_res_path'])
        out_style.printGreen('smeetingserver������ѹ�����,��ʼ�������ߣ�emqx������......��')
        time.sleep(2)
        # ���nginxRedis��װ����������
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-nginxRedis-config.tar src\res\ src\meetingutils_linux.py src\nginxAndRedisFrame.py src\nginxRedis��װ������.pyw')
        out_style.printGreen('nginxRedis��װ�����߹�����ɣ���ʼ�������ߣ�MYSQL-config��װ������')
        time.sleep(2)
        # ���MYSQL-config��װ����������
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL��װ������.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-config��װ�����߹�����ɣ���ʼ�������ߣ�MYSQL-master-config��װ������')
        time.sleep(2)
        # ���MYSQL-master-config��װ����������
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-master-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL��װ������.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-master-config��װ�����߹�����ɣ����ڽ������ƶ���ָ��Ŀ¼......��')
        time.sleep(2)

        # �����д�õĹ��߰��ƶ���outpathĿ¼��
        tool_path = []
        tool_file = []
        for root, dirs, files in os.walk(self.tool_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.tar':
                    tool_path.append(os.path.join(root, file))
                    tool_file.append(file)
                    copyfile(tool_path[0], r'%s\%s' % (package_path, tool_file[0]))
                    del tool_path[0]
                    del tool_file[0]

        out_style.printGreen('������Ŀ�����߹������......��')


# �����ͻ����������Ͳ�Ʒ������T��APK��committee,gov,paperfree��������T��APK��committee,gov,paperfree��
class Westone_client():
    def __init__(self, path, commid, Version_type):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type

    def builed_client(self):
        # ��ȡ���߸��¿ͻ��˴��뵽����
        function.get_allcode(self.path, 'smeetingsystem-client', self.commid, client_commid_Id, self.Version_type,
                             client)
        # ������T���汾�벻��T���汾
        for i in range(1, 3):
            if i == 1:
                out_style.printGreen('���ڹ�����Ŀ���ͻ��˴�T��APK�汾......��')
                time.sleep(2)
            else:
                out_style.printGreen('���ڹ�����Ŀ���ͻ��˲���T��APK�汾......��')
                time.sleep(2)
            '''
            # ���ڻ����汾��������ί�����������汾
            committee_path = r'%s\%s' % (self.path, version['committee_path'])
            gov_path = r'%s\%s' % (self.path, version['gov_path'])
            '''
            # �����汾��·��
            paperfree_path = r'%s\%s' % (self.path, version['paperfree_path'])
            # committeeFile = []
            # govFile = []
            paperfreeFile = []
            os.chdir('%s\smeetingsystem-client' % self.path)
            # �޸�����ѭ��������T���벻��T���İ汾
            with open('build.gradle', "r", encoding="utf-8") as f1, open("build1.gradle", "w",
                                                                         encoding="utf-8") as f2:
                for line in f1.readlines():
                    if 'need_tfcard = "false"' in line:
                        f2.write(re.sub('need_tfcard = "false"', 'need_tfcard = "true"', line))
                    elif 'need_tfcard = "true"' in line:
                        f2.write(re.sub('need_tfcard = "true"', 'need_tfcard = "false"', line))
                    else:
                        f2.write(line)
            os.remove('build.gradle')
            os.rename("build1.gradle", 'build.gradle')
            # �ͻ��˴������
            os.system('gradle --daemon --parallel --max-workers 10 assembleRelease')
            '''
            for root, dirs, files in os.walk(committee_path):
                committeeFile.append(files[0])
            for root, dirs, files in os.walk(gov_path):
                govFile.append(files[0])
            '''
            # ��ȡ�����汾����
            for root, dirs, files in os.walk(paperfree_path):
                paperfreeFile.append(files[1])
            '''
            committee_zip_file = package_path + '\%s.zip' % committeeFile[0]
            govFile_zip_file = package_path + '\%s.zip' % govFile[0]
            '''
            paperfree_zip_file = package_path + '\%s.zip' % paperfreeFile[0]
            '''
            function.get_zip(committee_path, committeeFile, committee_zip_file)
            function.get_zip(gov_path, govFile, govFile_zip_file)
            '''
            # ����õĿͻ��˰�����ѹ������ŵ�ָ��Ŀ¼
            function.get_zip(paperfree_path, paperfreeFile, paperfree_zip_file)


# ��ѡ�������Ͳ�Ʒ��������ˣ��ͻ��ˣ�����
class Westone_all():
    def __init__(self, path, commid, Version_type, server_dir, file_dir, tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.file_dir = file_dir
        self.tool_dir = tool_dir

    # һ���Թ����������Ͳ�Ʒ��
    def build_all_package(self):
        Westone_server(self.path, self.commid, self.Version_type, self.server_dir, self.file_dir).build_server()
        Westone_tools(self.path, self.commid, self.Version_type, self.tool_dir).build_tools()
        Westone_client(self.path, self.commid, self.Version_type).builed_client()
