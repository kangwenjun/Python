#! /usr/bin/env python
# coding=utf-8
# author:justin
# site:www.kangwenjun.com

import os,sys

print("environ:\n", os.environ)
print("")

print('\n----------------file path----------------')
print("supports_unicode_filenames:\t", os.path.supports_unicode_filenames) #is not callable
filename = sys.argv[0]
curdir = os.getcwd()
currentabspath = curdir + "/" + filename
print("normcase:\t", os.path.normcase("jJJjdf/df.tXt")) #在不区分大小写的文件系统上, 它把路径转换为小写字母。在Windows上, 它把正斜杠转换为反斜杠
print("normpath:\t", os.path.normpath(currentabspath)) #将“/”规范为“\“
filepath = os.path.join(curdir, filename) #使用了一致的反斜杠"\"
print("join:\t", filepath)
if currentabspath != filepath:
	currentabspath = filepath
	
print("exists:\t", os.path.exists(currentabspath)) #如果检查的文件是一个软制链接，但这个软连接指向的文件被删除了，会返回False
print("lexists:\t", os.path.lexists(currentabspath)) #只要软连接存在，即使它指向的文件不存在，也返回True
print("getcwd:\t", curdir)
print("currentabspath:\t", currentabspath)
print("relpath:\t", os.path.relpath(currentabspath)) #将绝对路径转为相对路径
print("relpath-existedpath:\t", os.path.relpath("d:/temp")) #存在”d:/temp"正确返回当前目录到“d：/temp”的相对目录
print("relpath-notexistedpath:\t", os.path.relpath("d:/notexistedpath")) #不存在”d:/notexistedpath"也正确返回当前目录到“d：/notexistedpath”的相对目录
print("relpath-notexistedpath-currentabspath:\t", os.path.relpath("d:/notexistedpath", currentabspath))#错误--必须使用目录路径，否则文件名会当作目录名，从而多向上跳转一次
print("relpath-existedpath-currentabspath:\t", os.path.relpath("d:/temp", currentabspath))#错误--必须使用目录路径，否则文件名会当作目录名，从而多向上跳转一次
print("relpath-start:\t", os.path.relpath("d:/temp", os.path.dirname(currentabspath))) #正确

print('\n----------------expanduser expandvars----------------')
print("expanduser:\t", os.path.expanduser("~")) #"~"表示当前用户
print("expanduser:\t", os.path.expanduser("~kangwenjun")) #”~"表示c:\user\
print("USERNAME:\t", os.path.expandvars("$USERNAME"))
print("USERNAME:\t", os.path.expandvars("${USERNAME}"))

print('\n----------------file time----------------')
print("getatime:\t", os.path.getatime(currentabspath))
print("getmtime:\t", os.path.getmtime(currentabspath))
print("getctime:\t", os.path.getctime(currentabspath))
print("getsize:\t", os.path.getsize(currentabspath))

print('\n----------------file type----------------')
print("isabs:\t", os.path.isabs(currentabspath))
print("isabs:\t", os.path.isabs("."))
print("isfile:\t", os.path.isfile(currentabspath))
print("isdir:\t", os.path.isdir(currentabspath))
print("islink:\t", os.path.islink(currentabspath))
print("ismount:\t", os.path.ismount(currentabspath))

print('\n----------------abspath realpath----------------')
print('abspath(""):\t', os.path.abspath("")) #等同于getcwd
print('realpath(""):\t', os.path.realpath(""))#等同于getcwd
print('abspath-notexistedfile:\t', os.path.abspath("notesistedfile"))#等同于getcwd+"notesistedfile"
print('realpath-notesistedfile:\t', os.path.realpath("notesistedfile"))#等同于getcwd+"notesistedfile"

linkfile = filename + ".link"
if False == os.path.exists(linkfile):
	os.symlink(filename, linkfile) #以管理员身份运行
print("abspath-link:\t", os.path.abspath(linkfile))
print("realpath-link:\t", os.path.realpath(linkfile))
print("samefile:\t", os.path.samefile(filename, linkfile)) #win:True 判断目录或文件是否相同
print("samestat:\t", os.path.samestat(os.stat(filename), os.stat(linkfile)))#判断stat tuple stat1和stat2是否指向同一个文件

fd = os.open(filename, os.O_RDONLY)
fd_link = os.open(linkfile, os.O_RDONLY)
print("sameopenfile:\t", os.path.sameopenfile(fd, fd_link)) #判断fp1和fp2是否指向同一文件
os.close(fd)
os.close(fd_link)

print('\n----------------split----------------')
print("split-currentabspath:\t", os.path.split(currentabspath)) #把路径分割成 dirname 和 basename，返回一个元组
print("split-curdir:\t", os.path.split(curdir)) #类似dirname 将最后一个节点视作文件名
print("splitdrive:\t", os.path.splitdrive(currentabspath)) #一般用在 windows 下，返回驱动器名和路径组成的元组
print("splitext-currentabspath:\t", os.path.splitext(currentabspath)) #分割路径中的文件名(及其路径)与拓展名
print("splitext-curdir:\t", os.path.splitext(curdir)) #仅按"."分割成两部分，此处后缀为空""
print("splitext-basename:\t", os.path.splitext(os.path.basename(currentabspath))) #完全正确
#print("splitunc:\t", os.path.splitunc(currentabspath)) #has no attribute "splitunc"

print('\n----------------other----------------')
print("abspaht:\t", os.path.abspath("./"))
print("basename-currentabspath:\t", os.path.basename(currentabspath)) #取最后一个节点 返回文件名,含后缀
print("basename-curdir:\t", os.path.basename(curdir)) #取最后一个节点
print("dirname-using-filepath:\t", os.path.dirname(currentabspath)) #仅将最后一个节点（此处为文件名）去掉
print("dirname-using-dirpath:\t", os.path.dirname(curdir))#仅将最后一个节点（此处为目录名）去掉
print("commonprefix:\t", os.path.commonprefix([curdir, currentabspath])) #返回list(多个路径)中，所有path共有的最长的路径
