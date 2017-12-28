import os
import pdb
fileList = [];
def rename(path):
	i = 0
	path = path
	fileList = os.listdir(path)#listdir 列出目录下所有文件
	for files in fileList:
		i = i + 1
		pdb.set_trace();#debugg;next;
		olddir = os.path.join(path,files);
		fileType = os.path.splitext(files)[1];
		newdir = os.path.join(path,str(i)+fileType)
		os.rename(olddir,newdir)
rename("E:\\test\python")