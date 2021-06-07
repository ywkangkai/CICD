# encoding=gbk
import sys,time,os
from STA import STA_build
from CDSZF import CDSZF_dev
from CDSZF import CDSZF_release
from common import out_style
from all_clone import allClone
parameter1 = sys.argv[1]
parameter2 = sys.argv[2]
parameter3 = sys.argv[3]
parameter4 = sys.argv[4]

list = [parameter1,parameter2,parameter3,parameter4]
print(list)
product_type = ''
Version_type = ''
path = ''
commid = ''

for type in list:
    print(type[0:2])
    if type[0:2] == '-t':
        if type == '-tall':
            Version_type = type
        elif type == '-tserver':
            Version_type = type
        elif type == '-tclient':
            Version_type = type
        elif type == '-tdevClient':
            Version_type = type
        elif type == '-treleaseClient':
            Version_type = type
        elif type == '-ttools':
            Version_type = type
        elif type == '-tallclone':
            Version_type = type
        elif type == '-tdevServer':
            Version_type = type
        elif type == '-tdevServerCluster':
            Version_type = type
        elif type == '-treleaseServer':
            Version_type = type
        elif type == '-releaseServerCluster':
            Version_type = type
        else:
            out_style.printRed('-t��ѡ����Ϊ[all,server,client,tools,allclone,dev,release,tdevServerCluster,releaseServerCluster]')
    elif type[0:2] == '-p':
        if type == '-psta':
            product_type = type
        elif type == '-pcdszf':
            product_type = type
        elif type == '-pNone':
            product_type = type
        else:
            out_style.printRed('-p��ѡ����Ϊ[sta,cdszf,None]')
    elif type[0:2] == '-o':
        path = type[2:]
    if type[0:2] == '-c':
        commid = type[2:]
server_target = r'%s\smeetingsystem-server\target' %path
cdszf_server_target =r'%s\CDSZF-smeetingsystem-server' %path
file_target = r'%s\smeetingsystem-netdisk\target'  %path
tool_dir = r'%s\smeeting-server-config-cluster\build' %path

if Version_type == '-tallclone'and product_type == '-pNone':
    out_style.printRed('׼����ʼ��ȡ���вֿ����......��')
    time.sleep(3)
    Wesone = allClone.westone_Get_clone(path, commid,Version_type)
    Wesone.get_clone()

if Version_type == '-tall' and product_type == '-psta':
    out_style.printRed('������ʼ�������б�׼��Ʒ����:����ˣ��ͻ��ˣ�����Ա����......��')
    time.sleep(3)
    Wesone = STA_build.Westone_all(path,commid,Version_type,server_target,file_target,tool_dir)
    Wesone.build_all_package()

if Version_type == '-tserver' and product_type == '-psta':
    out_style.printRed('׼����ʼ������׼��Ʒ���ͣ�����˰����ļ���վ�����......��')
    time.sleep(3)
    Wesone = STA_build.Westone_server(path,commid,Version_type,server_target,file_target)
    Wesone.build_server()

if Version_type == '-tclient' and product_type == '-psta':
    out_style.printRed('׼����ʼ������׼��Ʒ���ͣ��ͻ��˴�T��APK�벻��T��APK......��')
    Wesone = STA_build.Westone_client(path,commid,Version_type)
    Wesone.builed_client()

if Version_type == '-ttools' and product_type == '-psta':
    out_style.printRed('׼����ʼ������׼��Ʒ���ͣ�������[����ϵͳ��������,����ϵͳ�����ߣ��ļ���վ�����ߣ���Ⱥ������]......��')
    time.sleep(3)
    Wesone = STA_build.Westone_tools(path,commid,Version_type,tool_dir)
    Wesone.build_tools()

if Version_type == '-tdevServer' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�����-����')
    time.sleep(3)
    Westone = CDSZF_dev.westone_CDSZF_server(path, commid, Version_type, cdszf_server_target)
    Westone.build_server()

if Version_type == '-tdevServerCluster' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�����-��Ⱥ')
    time.sleep(3)
    Westone = CDSZF_dev.westone_CDSZF_server(path, commid, Version_type, cdszf_server_target)
    Westone.build_server()


if Version_type == '-treleaseServer' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�����-����')
    time.sleep(3)
    Westone = CDSZF_release.westone_CDSZF_server(path, commid, Version_type, cdszf_server_target)
    Westone.build_server()

if Version_type == '-releaseServerCluster' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�����-��Ⱥ')
    time.sleep(3)
    Westone = CDSZF_release.westone_CDSZF_server(path, commid, Version_type, cdszf_server_target)
    Westone.build_server()

if Version_type == '-tdevClient' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�ͻ���')
    time.sleep(3)
    Westone = CDSZF_dev.Westone_CDSZF_client(path, commid, Version_type)
    Westone.builed_client()

if Version_type == '-treleaseClient' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ������׶�-�ͻ���')
    time.sleep(3)
    Westone = CDSZF_release.Westone_CDSZF_client(path, commid, Version_type)
    Westone.builed_client()

if Version_type == '-ttools' and product_type == '-pcdszf':
    out_style.printRed('׼����ʼ�����ɶ���������Ʒ���ͣ�������')
    time.sleep(3)
    Westone = CDSZF_dev.Westone_CDSZF_tools(path, commid, Version_type, tool_dir)
    Westone.build_tools()

if Version_type == '-tall' and product_type == '-pcdszf':
    out_style.printRed('������ʼ�����ɶ���������Ʒ����:����ˣ��ͻ��ˣ�����Ա����')
    time.sleep(3)
    Westone = CDSZF_dev.Westone_all(path, commid, Version_type, server_target, tool_dir)
    Westone.build_all_package()
