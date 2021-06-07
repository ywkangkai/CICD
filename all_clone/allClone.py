# encoding=gbk
import os,yaml
from common import out_style
curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, "all_clone.yaml")
f = open(yamlPath, 'r', encoding='ISO-8859-1')
cfg = f.read()
version = yaml.load(cfg, Loader=yaml.FullLoader)

CDSZF_smeetingsystem_client = version['CDSZF-smeetingsystem-client']
CDSZF_smeetingsystem_server = version['CDSZF-smeetingsystem-server']
CDSZF_smeetingsystem_server_web = version['CDSZF-smeetingsystem-server-web']
smeeting_admin_tool = version['smeeting-admin-tool']
smeeting_maintenance = version['smeeting-maintenance']
smeeting_server_config = version['smeeting-server-config']
smeeting_server_config_cluster = version['smeeting-server-config-cluster']
smeetingsystem_client = version['smeetingsystem-client']
smeetingsystem_client_picviewer = version['smeetingsystem-client-picviewer']
smeetingsystem_client_plugins = version['smeetingsystem-client-plugins']
smeetingsystem_client_videoplayer = version['smeetingsystem-client-videoplayer']
smeetingsystem_netdisk = version['smeetingsystem-netdisk']
smeetingsystem_pcreader = version['smeetingsystem-pcreader']
smeetingsystem_server = version['smeetingsystem-server']
smeetingsystem_server_web = version['smeetingsystem-server-web']
smeetingsystem_whiteboard_server = version['smeetingsystem-whiteboard-server']

CDSZF_smeetingsystem_client_commid = version['CDSZF_smeetingsystem_client_commid']
CDSZF_smeetingsystem_server_commid = version['CDSZF_smeetingsystem_server_commid']
CDSZF_smeetingsystem_server_web_commid = version['CDSZF_smeetingsystem_server_web_commid']
smeeting_admin_tool_commid = version['smeeting_admin_tool_commid']
smeeting_maintenance_commid = version['smeeting_maintenance_commid']
smeeting_server_config_commid = version['smeeting_server_config_commid']
smeeting_server_config_cluster_commid = version['smeeting_server_config_cluster_commid']
smeetingsystem_client_commid = version['smeetingsystem_client_commid']
smeetingsystem_client_picviewer_commid = version['smeetingsystem_client_picviewer_commid']
smeetingsystem_client_plugins_commid = version['smeetingsystem_client_plugins_commid']
smeetingsystem_client_videoplayer_commid = version['smeetingsystem_client_videoplayer_commid']
smeetingsystem_netdisk_commid = version['smeetingsystem_netdisk_commid']
smeetingsystem_pcreader_commid = version['smeetingsystem_pcreader_commid']
smeetingsystem_server_commid = version['smeetingsystem_server_commid']
smeetingsystem_server_web_commid = version['smeetingsystem_server_web_commid']
smeetingsystem_whiteboard_server_commid = version['smeetingsystem_whiteboard_server_commid']




class westone_Get_clone():
    def __init__(self,path,commid,Version_type,):
        self.path = path
        self.commid = commid
        self.Version_type = Version_type


    def get_clone(self):

        if os.path.exists(r'%s\CDSZF-smeetingsystem-client' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\CDSZF-smeetingsystem-client' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %CDSZF_smeetingsystem_client_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.makedirs(r'%s' % self.path)
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(CDSZF_smeetingsystem_client)
            elif self.commid == 'head':
                os.system(CDSZF_smeetingsystem_client)
                os.system('git checkout %s' % CDSZF_smeetingsystem_client_commid)
                os.system('git pull')
            else:
                os.system(CDSZF_smeetingsystem_client)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')


        if os.path.exists(r'%s\CDSZF-smeetingsystem-server' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\CDSZF-smeetingsystem-server' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %CDSZF_smeetingsystem_server_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(CDSZF_smeetingsystem_server)
            elif self.commid == 'head':
                os.system(CDSZF_smeetingsystem_server)
                os.system('git checkout %s' % CDSZF_smeetingsystem_server_commid)
                os.system('git pull')
            else:
                os.system(CDSZF_smeetingsystem_server)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\CDSZF-smeetingsystem-server-web' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\CDSZF-smeetingsystem-server-web' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %CDSZF_smeetingsystem_server_web_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(CDSZF_smeetingsystem_server_web)
            elif self.commid == 'head':
                os.system(CDSZF_smeetingsystem_server_web)
                os.system('git checkout %s' % CDSZF_smeetingsystem_server_web_commid)
                os.system('git pull')
            else:
                os.system(CDSZF_smeetingsystem_server_web)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeeting-admin-tool' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeeting-admin-tool' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeeting_admin_tool_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeeting_admin_tool)
            elif self.commid == 'head':
                os.system(smeeting_admin_tool)
                os.system('git checkout %s' % smeeting_admin_tool_commid)
                os.system('git pull')
            else:
                os.system(smeeting_admin_tool)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeeting-maintenance' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeeting-maintenance' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeeting_maintenance_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeeting_maintenance)
            elif self.commid == 'head':
                os.system(smeeting_maintenance)
                os.system('git checkout %s' % smeeting_maintenance_commid)
                os.system('git pull')
            else:
                os.system(smeeting_maintenance)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeeting-server-config' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeeting-server-config' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeeting_server_config_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeeting_server_config)
            elif self.commid == 'head':
                os.system(smeeting_server_config)
                os.system('git checkout %s' % smeeting_server_config_commid)
                os.system('git pull')
            else:
                os.system(smeeting_server_config)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeeting-server-config-cluster' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeeting-server-config-cluster' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeeting_server_config_cluster_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeeting_server_config_cluster)
            elif self.commid == 'head':
                os.system(smeeting_server_config_cluster)
                os.system('git checkout %s' % smeeting_server_config_cluster_commid)
                os.system('git pull')
            else:
                os.system(smeeting_server_config_cluster)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-client' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-client' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_client_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_client)
            elif self.commid == 'head':
                os.system(smeetingsystem_client)
                os.system('git checkout %s' % smeetingsystem_client_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_client)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-client-picviewer' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-client-picviewer' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_client_picviewer_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_client_picviewer)
            elif self.commid == 'head':
                os.system(smeetingsystem_client_picviewer)
                os.system('git checkout %s' % smeetingsystem_client_picviewer_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_client_picviewer)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-client-plugins' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-client-plugins' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_client_plugins_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_client_plugins)
            elif self.commid == 'head':
                os.system(smeetingsystem_client_plugins)
                os.system('git checkout %s' % smeetingsystem_client_plugins_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_client_plugins)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-client-videoplayer' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-client-videoplayer' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_client_videoplayer_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_client_videoplayer)
            elif self.commid == 'head':
                os.system(smeetingsystem_client_videoplayer)
                os.system('git checkout %s' % smeetingsystem_client_videoplayer_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_client_videoplayer)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-netdisk' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-netdisk' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_netdisk_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_netdisk)
            elif self.commid == 'head':
                os.system(smeetingsystem_netdisk)
                os.system('git checkout %s' % smeetingsystem_netdisk_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_netdisk)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-pcreader' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-pcreader' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_pcreader_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_pcreader)
            elif self.commid == 'head':
                os.system(smeetingsystem_pcreader)
                os.system('git checkout %s' % smeetingsystem_pcreader_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_pcreader)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-server' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-server' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_server_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_server)
            elif self.commid == 'head':
                os.system(smeetingsystem_server)
                os.system('git checkout %s' % smeetingsystem_server_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_server)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-server-web' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-server-web' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_server_web_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_server_web)
            elif self.commid == 'head':
                os.system(smeetingsystem_server_web)
                os.system('git checkout %s' % smeetingsystem_server_web_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_server_web)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')

        if os.path.exists(r'%s\smeetingsystem-whiteboard-server' %self.path) and os.path.exists(r'%s'%self.path):
            os.chdir('%s\smeetingsystem-whiteboard-server' %self.path)
            if self.commid == 'master':
                os.system('git checkout master')
                os.system('git pull')
            elif self.commid == 'head':
                os.system('git checkout %s' %smeetingsystem_whiteboard_server_commid)
                os.system('git pull')
            else:
                os.system('git checkout %s' % self.commid)
                os.system('git pull')
        else:
            os.chdir(r'%s' % self.path)
            if self.commid == 'master':
                os.system(smeetingsystem_whiteboard_server)
            elif self.commid == 'head':
                os.system(smeetingsystem_whiteboard_server)
                os.system('git checkout %s' % smeetingsystem_whiteboard_server_commid)
                os.system('git pull')
            else:
                os.system(smeetingsystem_whiteboard_server)
                os.system('git checkout %s' %self.commid)
                os.system('git pull')