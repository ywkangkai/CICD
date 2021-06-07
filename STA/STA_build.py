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


# 构建服务端所有类型产品包：服务端后端，文件驿站服务端
class Westone_server():
    # 向git远程cangk拉取代码
    def __init__(self, path, commid, Version_type, server_dir, file_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.file_dir = file_dir

    def build_server(self):
        out_style.printGreen('正在进行项目：构建服务端包.......！')
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
        out_style.printGreen('服务端包构建完成，准备进行构建文件驿站服务包......！')
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
        # out_style.printGreen('文件驿站服务包构建完成......！')


# 构建工具所有类型产品包：会议系统辅助工具，会议系统管理工具，文件驿站管理工具
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
        out_style.printGreen('正在进行项目：构建会议系统辅助工具.......！')
        zip_name = package_path + '\会议系统辅助工具.zip'
        # 拉取或者更新管理员工具最新代码到本地
        function.get_allcode(self.path, 'smeeting-admin-tool', self.commid, admin_tool_commid_Id, self.Version_type,
                             admintool)
        # 辅助工具工具打包命令
        os.chdir('%s\smeeting-admin-tool' % self.path)
        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\会议系统辅助工具.pyw')
        out_style.printGreen('会议系统辅助工具构建完成，进行工具压缩.......！')
        time.sleep(3)
        # 将管理工具打包进行压缩
        function.get_admintool_zip(globals()['res_path'] + r'\res', globals()['res_path'], src_res_path, res_path,
                                   zip_name)
        # 打好包后需要删除res文件保持res文件每次都是最新的
        function.del_file(globals()['res_path'])
        out_style.printGreen('会议系统辅助工具压缩完成，进行会议系统管理工具项目构建......！')
        time.sleep(3)

        zip_name = [package_path + '\会议系统管理工具不带短信平台.zip', package_path + '\会议系统管理工具带短信平台.zip']
        zip_name2 = package_path + '\文件驿站管理工具.zip'
        # 拉取或者更新安装工具最新代码到本地
        function.get_code(self.path, 'smeeting-server-config', self.commid, config_tool_commid, configtool)
        # 循环出包,分开打带短信平台的工具与不带短信平台的工具,需要修改配置文件
        for i in range(0, len(zip_name)):
            os.chdir('%s\smeeting-server-config\src' % self.path)
            with open('会议系统管理工具.pyw', "r", encoding="utf-8") as f1, open("会议系统管理工具1.pyw", "w", encoding="utf-8") as f2:
                for line in f1.readlines():
                    if "isCDSZF = True" in line:
                        f2.write(re.sub('isCDSZF = True', 'isCDSZF = False', line))
                    elif "isCDSZF = False" in line:
                        f2.write(re.sub('isCDSZF = False', 'isCDSZF = True', line))
                    else:
                        f2.write(line)
            os.remove('会议系统管理工具.pyw')
            os.rename("会议系统管理工具1.pyw", '会议系统管理工具.pyw')
            os.chdir('%s\smeeting-server-config' % self.path)
            # 管理工具打包命令
            os.system(
                'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\会议系统管理工具.pyw')
            # 将管理工具包进行要锁
            function.get_serverconfig_zip(globals()['config_res_path'] + r'\res', globals()['config_res_path'],
                                          config_src_res_path, config_res_path, zip_name[i])
            # 打好包后需要删除res文件保持res文件每次都是最新的
            function.del_file(globals()['config_res_path'])
            out_style.printGreen('会议系统管理工具工具项目构建完成......！')
            time.sleep(2)
        # 文件驿站打包命令
        os.chdir('%s\smeeting-server-config\src' % self.path)
        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\文件驿站管理工具.pyw')
        # 对文件驿站工具进行打包
        function.get_serverconfig_zip(globals()['config_res_path'] + r'\res', globals()['config_res_path'],
                                      config_src_res_path, config_res_path, zip_name2)
        # 打好包后需要删除res文件保持res文件每次都是最新的
        function.del_file(globals()['config_res_path'])
        out_style.printGreen('文件驿站管理工具项目构建完成,开始构建集群工具项目工程......！')
        time.sleep(2)

        zip_path1 = package_path + '\smeetingserver管理工具与emqx管理工具.zip'
        # 拉取或者更新集群工具代码到本地
        function.get_code(self.path, 'smeeting-server-config-cluster', self.commid, cluster_tool_commid, clustertool)
        os.chdir('%s\smeeting-server-config-cluster' % self.path)
        out_style.printGreen('smeetingserver管理工具与emqx管理工具构建完成，正在进行文件压缩......！')
        time.sleep(2)
        # 压缩集群工具
        function.get_clusterconfig_zip(globals()['cluster_res_path'] + r'\res', globals()['cluster_res_path'],
                                       cluster_src_res_path, cluster_res_path, zip_path1)
        function.del_file(globals()['cluster_res_path'])
        out_style.printGreen('smeetingserver管理工具压缩完成,开始构建工具：emqx管理工具......！')
        time.sleep(2)
        # 打包nginxRedis安装管理工具命令
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-nginxRedis-config.tar src\res\ src\meetingutils_linux.py src\nginxAndRedisFrame.py src\nginxRedis安装管理工具.pyw')
        out_style.printGreen('nginxRedis安装管理工具构建完成，开始构建工具：MYSQL-config安装管理工具')
        time.sleep(2)
        # 打包MYSQL-config安装管理工具命令
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL安装管理工具.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-config安装管理工具构建完成，开始构建工具：MYSQL-master-config安装管理工具')
        time.sleep(2)
        # 打包MYSQL-master-config安装管理工具命令
        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-master-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL安装管理工具.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-master-config安装管理工具构建完成，正在将工具移动至指定目录......！')
        time.sleep(2)

        # 将所有打好的工具包移动至outpath目录中
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

        out_style.printGreen('所有项目管理工具构建完成......！')


# 构建客户端所有类型产品包：带T卡APK（committee,gov,paperfree），不带T卡APK（committee,gov,paperfree）
class Westone_client():
    def __init__(self, path, commid, Version_type):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type

    def builed_client(self):
        # 拉取或者更新客户端代码到本地
        function.get_allcode(self.path, 'smeetingsystem-client', self.commid, client_commid_Id, self.Version_type,
                             client)
        # 构建带T卡版本与不带T卡版本
        for i in range(1, 3):
            if i == 1:
                out_style.printGreen('正在构建项目：客户端带T卡APK版本......！')
                time.sleep(2)
            else:
                out_style.printGreen('正在构建项目：客户端不带T卡APK版本......！')
                time.sleep(2)
            '''
            # 现在基础版本无需打包市委版与市政府版本
            committee_path = r'%s\%s' % (self.path, version['committee_path'])
            gov_path = r'%s\%s' % (self.path, version['gov_path'])
            '''
            # 基础版本包路径
            paperfree_path = r'%s\%s' % (self.path, version['paperfree_path'])
            # committeeFile = []
            # govFile = []
            paperfreeFile = []
            os.chdir('%s\smeetingsystem-client' % self.path)
            # 修改配置循环出包带T卡与不带T卡的版本
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
            # 客户端打包命令
            os.system('gradle --daemon --parallel --max-workers 10 assembleRelease')
            '''
            for root, dirs, files in os.walk(committee_path):
                committeeFile.append(files[0])
            for root, dirs, files in os.walk(gov_path):
                govFile.append(files[0])
            '''
            # 获取基础版本包名
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
            # 将打好的客户端包进行压缩并存放到指定目录
            function.get_zip(paperfree_path, paperfreeFile, paperfree_zip_file)


# 勾选所有类型产品包：服务端，客户端，工具
class Westone_all():
    def __init__(self, path, commid, Version_type, server_dir, file_dir, tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.file_dir = file_dir
        self.tool_dir = tool_dir

    # 一次性构建所有类型产品包
    def build_all_package(self):
        Westone_server(self.path, self.commid, self.Version_type, self.server_dir, self.file_dir).build_server()
        Westone_tools(self.path, self.commid, self.Version_type, self.tool_dir).build_tools()
        Westone_client(self.path, self.commid, self.Version_type).builed_client()
