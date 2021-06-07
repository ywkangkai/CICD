# encoding=gbk
from common import out_style
import os,sys,yaml,time,zipfile,re,shutil,tarfile
from shutil import copyfile
curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, "CDSZF.yaml")
f = open(yamlPath, 'r', encoding='ISO-8859-1')
cfg = f.read()
version = yaml.load(cfg, Loader=yaml.FullLoader)
server_commid_Id = version['server_commid_Id']
web_commid_id = version['web_commid_id']
Server_Web_commid_id = version['Server_Web_commid_id']
CDSZF_Server_commid_id = version['CDSZF_Server_commid_id']
admin_tool_commid_Id = version['admin_tool_commid_Id']
config_tool_commid = version['config_tool_commid']
cluster_tool_commid = version['cluster_tool_commid']
client_commid_Id = version['client_commid']
Server = version['Server']
CDSZF_Web = version['CDSZF_Web']
Server_Web = version['Server_Web']
CDSZF_Server = version['CDSZF_Server']
admintool = version['admintool']
client = version['client']
clustertool = version['clustertool']
configtool = version['configtool']
package_path = os.path.abspath(os.path.dirname(__file__))+'\outpath'


class westone_CDSZF_server():
    def __init__(self,path,commid,Version_type,server_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir

    def build_server(self):
        out_style.printGreen('开始构建项目：成都市定制服务端......！')
        server_smsManage_path = r'%s\smeetingsystem-server-web\scripts\views\container\systemManage' %self.path
        web_smsManage_path = r'%s\CDSZF-smeetingsystem-server-web\scripts\views\container\systemManage' %self.path
        web_systemParams_html_path = r'%s\CDSZF-smeetingsystem-server-web\scripts\views\container\systemManage\templates' %self.path
        server_systemParams_html_path = r'%s\smeetingsystem-server\src\main\resources\static\scripts\views\container\systemManage\templates' %self.path
        web_smsManage_path_js = web_smsManage_path+r'\systemParams.js'
        server_smsManage_path_js = server_smsManage_path+r'\systemParams.js'
        cdszf_server_web_sider = r'%s\CDSZF-smeetingsystem-server-web\scripts\views\layout' %self.path
        server_web_sider = r'%s\smeetingsystem-server-web\scripts\views\layout'%self.path
        cdszf_server_web_sider_html = r'%s\CDSZF-smeetingsystem-server-web\scripts\views\layout\templates'%self.path
        server_web_sider_html = r'%s\smeetingsystem-server-web\scripts\views\layout\templates' %self.path
        cdszf_web_login_html = r'%s\CDSZF-smeetingsystem-server-web'%self.path
        server_web_login_html = r'%s\smeetingsystem-server-web' %self.path
        cdszf_server_web_businessclient_js = r'%s\CDSZF-smeetingsystem-server-web\scripts\business'%self.path
        server_web_businessclient_js = r'%s\smeetingsystem-server-web\scripts\business'%self.path
        if os.path.exists(r'%s\smeetingsystem-server' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-server' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %server_commid_Id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.makedirs(r'%s' % self.path)
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(Server)
            elif self.commid == 'head':
                os.system(Server)
                os.system('git checkout %s' % server_commid_Id)
                os.system('git pull')
            else:
                os.system(Server)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\CDSZF-smeetingsystem-server-web' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\CDSZF-smeetingsystem-server-web' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %web_commid_id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(CDSZF_Web)
            elif self.commid == 'head':
                os.system(CDSZF_Web)
                os.system('git checkout %s' % web_commid_id)
                os.system('git pull')
            else:
                os.system(CDSZF_Web)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-server-web.git' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-server-web.git' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %Server_Web_commid_id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(Server_Web)
            elif self.commid == 'head':
                os.system(Server_Web)
                os.system('git checkout %s' % Server_Web_commid_id)
                os.system('git pull')
            else:
                os.system(Server_Web)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\CDSZF-smeetingsystem-server.git' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\CDSZF-smeetingsystem-server.git' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %CDSZF_Server_commid_id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(CDSZF_Server)
            elif self.commid == 'head':
                os.system(CDSZF_Server)
                os.system('git checkout %s' % CDSZF_Server_commid_id)
                os.system('git pull')
            else:
                os.system(CDSZF_Server)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        copyfile(cdszf_web_login_html + '\%s' % 'login.html', server_web_login_html + '\%s'% 'login.html')
        copyfile(cdszf_server_web_businessclient_js + '\%s' % 'businessClient.js', server_web_businessclient_js + '\%s' % 'businessClient.js')
        copyfile(cdszf_server_web_sider+'\%s'%'sider.js',server_web_sider+'\%s'%'sider.js')
        copyfile(cdszf_server_web_sider_html+'\%s'%'sider.html',server_web_sider_html+'\%s'%'sider.html')
        self.copy_file(web_smsManage_path,server_smsManage_path)
        if os.path.exists(r'%s\CDSZF-smeetingsystem-server\src\main\resources\static'%self.path):
            self.copy_file(r'%s\smeetingsystem-server-web' % self.path,
                           r'%s\CDSZF-smeetingsystem-server\src\main\resources\static' % self.path)
        else:
            os.makedirs(r'%s\CDSZF-smeetingsystem-server\src\main\resources\static'%self.path)
            self.copy_file(r'%s\smeetingsystem-server-web' % self.path,
                           r'%s\CDSZF-smeetingsystem-server\src\main\resources\static' % self.path)
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

        os.chdir(r'%s\CDSZF-smeetingsystem-server' %self.path)
        os.system('mvn clear package -Ptest')

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
                if 'mastersmeetingsystem-cdszf' in file:
                    zip_name = file
        self.untar(package_path+r'\%s'%zip_name,package_path)
        self.preDelPic(package_path)
        self.make_targz(package_path+r'\%s'%zip_name,package_path+r'\%s' %(self.file_name(package_path)))
        os.chdir(r'%s\CDSZF-smeetingsystem-server\src\main\resources\static'%self.path)
        #删除非空文件夹不需要提示
        os.system('rmdir /s /q .git')
        os.chdir(package_path)
        os.system('rmdir /s /q %s'%self.file_name(package_path))
        out_style.printGreen('成都市定制服务包构建完成')

    # 正在表达式替换无空白的内容
    def content_replace(self,copycontent, outcontent, copy_satrt_lable, copy_end_lable, out_start_lable, out_end_lable):
        new_content = ''
        with open(copycontent, 'r', encoding='utf-8') as f1:
            content = f1.read()
            new_string = re.compile(r'\/\*%s_SRC\*\/(.*?)\/\*%s_SRC\*\/' % (copy_satrt_lable, copy_end_lable), re.DOTALL)
            new_content = new_string.findall(content)[0] + new_content
        old_content = ''
        with open(outcontent, 'r', encoding='utf-8') as f2:
            content1 = f2.read()
            old_string = re.compile(r'\/\*%s_DEST\*\/(.*?)\/\*%s_DEST\*\/' % (out_start_lable, out_end_lable), re.DOTALL)
            old_content = old_string.findall(content1)[0] + old_content
            new_content1 = content1.replace(old_content, new_content)
            with open(outcontent, 'w', encoding='utf-8') as f3:
                f3.write(new_content1)

    #正在表达式替换有空白的内容
    def content_blank_replace(self,copycontent, outcontent, copy_start, copy_end, out_string):
        old_string = out_string
        new_string = out_string
        with open(copycontent, 'r', encoding='utf-8') as f1:
            content = f1.read()
            aaa = re.compile(r'\/\*%s\*\/(.*?)\/\*%s\*\/' % (copy_start, copy_end), re.DOTALL)
            hd_new_content = new_string + aaa.findall(content)[0]
        with open(outcontent, 'r', encoding='utf-8') as oldfile:
            content = oldfile.read()
            new_content = content.replace(old_string, hd_new_content)
            with open(outcontent, 'w', encoding='utf-8') as newfile:
                newfile.write(new_content)

    #将某一个文件下的所有文件复制到另一个文件下
    def copy_file(self, copy_in_path, copy_out_path):
        for files in os.listdir(copy_in_path):
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
                self.copy_file(name, back_name)

    #解压tar.gz格式的压缩包
    def untar(self,fname, zip_dirs):
        """
        :param fname: 解压文件路径
        :param zip_dirs: 解压后存放路径
        :return:
        """
        t = tarfile.open(fname)
        t.extractall(path=zip_dirs)
        file_zip_name = ''
        Files = self.file_name(zip_dirs)
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
    def file_name(self,file_dir):
        for root, dirs, files in os.walk(file_dir):
            for file_names in dirs:
                if 'mastersmeetingsystem' in file_names:
                    name = file_names
        return name

     #删除指定文件
    def preDelPic(self,path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".tar.gz"):
                    os.remove(os.path.join(root, name))

    #将文件压缩为tar格式
    def make_targz(self,output_filename, source_dir):
        """
        :param output_filename: 自己取一个压缩文件名
        :param source_dir: 压缩后存放的路径
        :return:
        """
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

class Westone_CDSZF_tools():
    def __init__(self, path, commid, Version_type, tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.tool_dir = tool_dir

    def build_tools(self):
        globals()['res_path'] = r'%s\smeeting-admin-tool\dist' % self.path
        globals()['config_res_path'] = r'%s\smeeting-server-config\dist' % self.path
        globals()['cluster_res_path'] = r'%s\smeeting-server-config-cluster\dist' % self.path
        config_res_path = globals()['config_res_path'] + r'\res'
        res_path = globals()['res_path'] + r'\res'
        cluster_res_path = globals()['cluster_res_path'] + r'\res'
        src_res_path = r'%s\smeeting-admin-tool\src\res' % self.path
        config_src_res_path = r'%s\smeeting-server-config\src\res' % self.path
        cluster_src_res_path = r'%s\smeeting-server-config-cluster\src\res' % self.path
        out_style.printGreen('正在进行项目：构建会议系统辅助工具.......！')
        zip_name = package_path + '\会议系统辅助工具.zip'
        if os.path.exists(r'%s\smeeting-admin-tool' % self.path) and os.path.exists(r'%s' % self.path):
            os.chdir('%s\smeeting-admin-tool' % self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' % admin_tool_commid_Id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            if self.Version_type == '-tall':
                os.chdir(r'%s' % self.path)
                if self.commid == 'master':
                    try:
                        os.system(admintool)
                    except:
                        print('未拉代码')
                elif self.commid == 'head':
                    os.system(admintool)
                    os.system('git checkout %s' % admin_tool_commid_Id)
                    os.system('git pull')
                else:
                    os.system(admintool)
                    os.system('git checkout %s' % self.commid)
            else:
                os.makedirs(r'%s' % self.path)
                os.chdir(r'%s' % self.path)
                if self.commid == 'master':
                    try:
                        os.system(admintool)
                    except:
                        print('未拉代码')
                elif self.commid == 'head':
                    os.system(admintool)
                    os.system('git checkout %s' % admin_tool_commid_Id)
                    os.system('git pull')
                else:
                    os.system(admintool)
                    os.system('git checkout %s' % self.commid)

        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\会议系统辅助工具.pyw')
        out_style.printGreen('会议系统辅助工具构建完成，进行工具压缩.......！')
        time.sleep(3)
        self.get_admintool_zip(globals()['res_path'], src_res_path, res_path, zip_name)
        self.del_file(globals()['res_path'])
        out_style.printGreen('会议系统辅助工具压缩完成，进行会议系统管理工具项目构建......！')
        time.sleep(3)

        zip_name1 = package_path + '\会议系统管理工具.zip'
        zip_name2 = package_path + '\文件驿站管理工具.zip'
        if os.path.exists(r'%s\smeeting-server-config' % self.path) and os.path.exists(r'%s' % self.path):
            os.chdir('%s\smeeting-server-config' % self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' % config_tool_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(configtool)
            elif self.commid == 'head':
                os.system(configtool)
                os.system('git checkout %s' % config_tool_commid)
                os.system('git pull')
            else:
                os.system(configtool)
                os.system('git checkout %s' % self.commid)
        os.chdir('%s\smeeting-server-config' % self.path)

        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\会议系统管理工具.pyw')
        self.get_serverconfig_zip(globals()['config_res_path'], config_src_res_path, config_res_path, zip_name1)
        self.del_file(globals()['config_res_path'])
        out_style.printGreen('会议系统管理工具工具项目构建完成......！')
        time.sleep(2)

        os.system(
            'venv\\Scripts\\python venv\\Scripts\\pyinstaller.exe -F -w -i src\\res\\image\\app.ico src\\文件驿站管理工具.pyw')
        self.get_serverconfig_zip(globals()['config_res_path'], config_src_res_path, config_res_path, zip_name2)
        self.del_file(globals()['config_res_path'])
        out_style.printGreen('文件驿站管理工具项目构建完成,开始构建集群工具项目工程......！')
        time.sleep(2)

        zip_path1 = package_path + '\smeetingserver管理工具与emqx管理工具.zip'
        if os.path.exists(r'%s\smeeting-server-config-cluster' % self.path) and os.path.exists(r'%s' % self.path):
            os.chdir('%s\smeeting-server-config-cluster' % self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' % cluster_tool_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(clustertool)
            elif self.commid == 'head':
                os.system(clustertool)
                os.system('git checkout %s' % cluster_tool_commid)
                os.system('git pull')
            else:
                os.system(clustertool)
                os.system('git checkout %s' % self.commid)
        os.chdir('%s\smeeting-server-config-cluster' % self.path)

        out_style.printGreen('smeetingserver管理工具与emqx管理工具构建完成，正在进行文件压缩......！')
        time.sleep(2)
        self.get_clusterconfig_zip(globals()['cluster_res_path'], cluster_src_res_path, cluster_res_path, zip_path1)
        self.del_file(globals()['cluster_res_path'])
        out_style.printGreen('smeetingserver管理工具压缩完成,开始构建工具：emqx管理工具......！')
        time.sleep(2)

        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-nginxRedis-config.tar src\res\ src\meetingutils_linux.py src\nginxAndRedisFrame.py src\nginxRedis安装管理工具.pyw')
        out_style.printGreen('nginxRedis安装管理工具构建完成，开始构建工具：MYSQL-config安装管理工具')
        time.sleep(2)

        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL安装管理工具.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-config安装管理工具构建完成，开始构建工具：MYSQL-master-config安装管理工具')
        time.sleep(2)

        os.system(
            r'venv\7-Zip\7z a -ttar build\Smeeting-mysql-master-config.tar src\res\ src\meetingutils_linux.py src\mysqlInstallFrame.py src\MYSQL安装管理工具.pyw src\SpaceService.py')
        out_style.printGreen('MYSQL-master-config安装管理工具构建完成，正在将工具移动至指定目录......！')
        time.sleep(2)

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

    def get_admintool_zip(self, dir, copy_in_path, copy_out_path, outFullName):
        """
        :param dir: 需要传一个路径，判断dist目录下是否有res文件夹
        :param copy_in_path: 传src的路径，目的是拿到该目录下的res文件进行复制
        :param copy_out_path:将复制的res文件，粘贴到dist目录下
        :param outFullName:将压缩的文件存放的路径
        :return:
        """
        os.makedirs(globals()['res_path'] + r'\res')
        self.copy_file(copy_in_path, copy_out_path)
        zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dir):
            this_path = os.path.abspath('.')
            fpath = path.replace(this_path, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

    def get_serverconfig_zip(self, dir, copy_in_path, copy_out_path, outFullName):
        os.makedirs(globals()['config_res_path'] + r'\res')
        self.copy_file(copy_in_path, copy_out_path)
        zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dir):
            this_path = os.path.abspath('.')
            fpath = path.replace(this_path, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

    def get_clusterconfig_zip(self, dir, copy_in_path, copy_out_path, outFullName):
        os.makedirs(globals()['cluster_res_path'] + r'\res')
        self.copy_file(copy_in_path, copy_out_path)
        zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dir):
            this_path = os.path.abspath('.')
            fpath = path.replace(this_path, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

    def copy_file(self, copy_in_path, copy_out_path):
        for files in os.listdir(copy_in_path):
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
                self.copy_file(name, back_name)

    def del_file(self, filepath):
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

class Westone_CDSZF_client():
    def __init__(self, path, commid,Version_type):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type


    def builed_client(self):
        if os.path.exists(r'%s\smeetingsystem-client' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-client' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' % client_commid_Id)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            if self.Version_type == '-tall':
                os.chdir(r'%s' % self.path)
                if self.commid == 'master':
                    os.system(client)
                elif self.commid == 'head':
                    os.system(client)
                    os.system('git checkout %s' % client_commid_Id)
                    os.system('git pull')
                else:
                    os.system(client)
                    os.system('git checkout %s' %self.commid)
            else:
                os.makedirs(r'%s' % self.path)
                os.chdir(r'%s' % self.path)
                if self.commid == 'master':
                    os.system(client)
                elif self.commid == 'head':
                    os.system(client)
                    os.system('git checkout %s' % client_commid_Id)
                    os.system('git pull')
                else:
                    os.system(client)
                    os.system('git checkout %s' %self.commid)
        for i in range(1,3):
            if i == 1:
                out_style.printGreen('正在构建项目：客户端带T卡APK版本......！')
                time.sleep(2)
            else:
                out_style.printGreen('正在构建项目：客户端不带T卡APK版本......！')
                time.sleep(2)
            committee_path = r'%s\smeetingsystem-client\app\build\outputs\apk\committee\release' % self.path
            gov_path = r'%s\smeetingsystem-client\app\build\outputs\apk\gov\release' % self.path
            paperfree_path = r'%s\smeetingsystem-client\app\build\outputs\apk\paperfree\release' % self.path
            committeeFile = []
            govFile = []
            paperfreeFile = []
            os.chdir('%s\smeetingsystem-client' % self.path)
            with open('gradle.properties', "r", encoding="utf-8") as f1, open("gradle1.properties", "w",
                                                                              encoding="utf-8") as f2:
                for line in f1.readlines():
                    if "need_tfcard=false" in line:
                        f2.write(re.sub('need_tfcard=false', 'need_tfcard=true', line))
                    elif "need_tfcard=true" in line:
                        f2.write(re.sub('need_tfcard=true', 'need_tfcard=false', line))
                    else:
                        f2.write(line)
            os.remove('gradle.properties')
            os.rename("gradle1.properties", 'gradle.properties')
            os.system('gradle --daemon --parallel --max-workers 10 assembleRelease')
            for root, dirs, files in os.walk(committee_path):
                committeeFile.append(files[0])
            for root, dirs, files in os.walk(gov_path):
                govFile.append(files[0])
            for root, dirs, files in os.walk(paperfree_path):
                paperfreeFile.append(files[1])
            committee_zip_file = package_path + '\%s.zip' % committeeFile[0]
            govFile_zip_file = package_path + '\%s.zip' % govFile[0]
            paperfree_zip_file = package_path + '\%s.zip' % paperfreeFile[0]

            self.test_2_get_zip(committee_path, committeeFile, committee_zip_file)
            self.test_2_get_zip(gov_path, govFile, govFile_zip_file)
            self.test_2_get_zip(paperfree_path, paperfreeFile, paperfree_zip_file)

    def test_2_get_zip(self,path, files, zip_name):
        os.chdir(path)
        zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for file in files:
            zp.write(file)
        zp.close()
        time.sleep(5)
        out_style.printGreen('压缩完成已存在至指定目录......！')

class Westone_all():
    def __init__(self,path,commid,Version_type,server_dir,tool_dir):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type
        self.server_dir = server_dir
        self.tool_dir = tool_dir


    def build_all_package(self):
        westone_CDSZF_server(self.path,self.commid,self.Version_type,self.server_dir).build_server()
        Westone_CDSZF_tools(self.path, self.commid,self.Version_type,self.tool_dir).build_tools()
        Westone_CDSZF_client(self.path, self.commid,self.Version_type).builed_client()








