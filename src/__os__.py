#! /usr/bin/env python
# coding=utf-8

import os,sys,stat

tempdir = "d:/temp/"
tempfile = tempdir + "os_temp.txt"
tempfilecopy = tempdir + "os_temp_copy.txt"
tempfilerename = tempdir + "os.txt"
temppipe = tempdir + "os_temp_pipe"
templink = tempdir + "os_temp_link"
temppython = tempdir + "python/"
tempmakedirs = temppython + "makedirs"
tempmkdir = temppython + "mkdir"

print('\n----------------getcwd getcwdu chdir----------------')
python_work_directory = os.getcwd()
changed_directory = python_work_directory + "/.."
print("current directory:", changed_directory)
os.chdir(changed_directory)
print("current directory:", os.getcwd())
os.chdir(python_work_directory)
print("pardir:\t", os.pardir) #".." not callable 
#print("getcwu:", os.getcwdu())

print('\n----------------access----------------')
print("F_OK:", os.access(os.getcwd(), os.F_OK))
print("W_OK:", os.access(os.getcwd(), os.W_OK))
print("R_OK:", os.access(os.getcwd(), os.R_OK))
print("X_OK:", os.access(os.getcwd(), os.X_OK))

print('\n----------------file read write----------------')
fd = os.open(tempfile, os.O_RDWR | os.O_CREAT)
d_fd = os.dup(fd)
f = os.fdopen(fd)
print("type(f):", type(f))
with open(sys.argv[0], "r") as fi:
	print("type(fi):", type(fi))
	print("os.fdopen == open:", type(f) == type(fi))

writed_size = os.write(fd, sys.argv[0].encode("utf-8", "strict"))
os.write(fd, "\tsize:{0}".format(writed_size).encode("utf-8", "strict"))
#os.fdatasync(fd) #写入磁盘
os.fsync(fd)#写入磁盘
os.lseek(fd, 0, os.SEEK_SET) # os.SEEK_CUR os.SEEK_END
print("read:", os.read(d_fd, 256))

os.close(d_fd)
#os.close(fd) #OSError
fd_low = d_fd
fd_high = d_fd
os.closerange(fd_low, fd_high) #忽略错误


#os.dup2(fd, 1) #stdout:1 将stdout重定向到文件

print('\n----------------fstat----------------')
info = os.fstat(fd)
print("info:", info)
print(
	"dev:{dev}\n" 			#设备信息
	"ino:{ino}\n" 			#文件的i-node值
	"mode:{mode}\n" 		#文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
	"nlink:{nlink}\n" 		#硬连接数
	"uid:{uid}\n" 			#用户ID 
	"gid:{gid}\n" 			#用户组 ID
#	"rdev:{rdev}\n" 		#设备 ID (如果指定文件)
	"size:{size}\n" 		#文件大小，以byte为单位
#	"blksize:{blksize}\n" 	#系统 I/O 块大小
#	"blocks:{blocks\n}" 	#文件的是由多少个 512 byte 的块构成的
	"atime:{atime}\n" 		#文件最近的访问时间
	"mtime:{mtime}\n" 		#文件最近的修改时间
	"ctime:{ctime}\n"		#文件状态信息的修改时间（不是文件内容的修改时间）
	.format(dev=info.st_dev
	, ino=info.st_ino
	, mode=info.st_mode
	, nlink=info.st_nlink
	, uid=info.st_uid
	, gid=info.st_gid
#	, rdev=info.st_rdev
	, size=info.st_size
#	, blksize=info.st_blksize
#	, blocks=info.st_blocks
	, atime=info.st_atime
	, mtime=info.st_mtime
	, ctime=info.st_ctime)
	)
	
print("S_ISDIR:{isdir}\n"
	"S_ISFIFO:{isfifo}\n"
	"S_ISSOCK:{issock}\n"
	"S_ISREG:{isreg}\n"
	"S_ISLNK:{islink}\n"
	.format(isdir=stat.S_ISDIR(info.st_mode)
		, isfifo=stat.S_ISFIFO(info.st_mode)
		, issock=stat.S_ISSOCK(info.st_mode)
		, isreg=stat.S_ISREG(info.st_mode)
		, islink=stat.S_ISLNK(info.st_mode)
	))
	
#print("major:{0}\nminor:{1}".format(os.major(info.st_dev), os.minor(info.st_dev))) # has no attribute 'major'
major_num = 0
minor_num = 103
#dev = os.makedev(major_num, minor_num) # has no attribute "makedev"

print('\n----------------general----------------')

if False == os.path.exists(tempmakedirs):
	os.makedirs(tempmakedirs, 0o777) #如果已经存在，则抛出FileExistedError
if False == os.path.exists(tempmkdir):
	os.mkdir(tempmkdir, 0o777) #如果没有上级目录，则抛出FileNotFoundError;如果已经存在，则抛出FileExistedError
if False == os.path.exists(tempfilecopy):
	os.link(tempfile, tempfilecopy) #创建一个已存在文件的拷贝 如果已经存在，则抛出FileExistedError
	
os.rename(tempfilecopy, tempfilerename)
os.utime(tempfilerename, (1577808000,1577808000)) #atime, mtime
#if os.path.exists(tempfilerename):
#	os.remove(tempfilerename)
"""
if os.path.exists(tempfile):
	os.unlink(tempfile) #删除文件路径
"""
	
print("listdir:", os.listdir(tempdir))
print("lstat:\t", os.lstat(sys.argv[0])) #像stat(),但是没有软链接
print("stat:\t",os.stat(sys.argv[0]))
#print("stat_float_times:\t", os.stat_float_times()) #has no attribute "stat_float_times"
#print("statvfs:\t", os.statvfs(sys.argv[0])) #has no attribute "statvfs"
#print("tcgetpgrp:\t", os.tcgetpgrp(sys.argv[0])) #has no attribute "tcgetpgrp"
#print("ttyname:\t", os.ttyname(fd)) #has no attribute "ttyname"

#os.mkfifo(temppipe, 0o664) #has no attribute "mkfifo"
#os.mknod(temppipe, 0o664 | stat.S_IFIFO) #has no attribute "mkno"
#m, s = os.openpty() #has no attribute "openpty"


a = 'mkdir nwdir'
b = os.popen(a, "r", -1) #用于从一个命令打开一个管道
print("popen:", b) #读取命令的执行结果
#print("popen-read:", b.read())
b.close()

print('\n----------------link----------------')
if False == os.path.exists(templink):
	os.symlink(tempfile, templink)
print("file path from readlink:", os.readlink(templink))
os.remove(templink)
os.removedirs(tempmkdir)
os.rmdir(tempmakedirs)

print('\n----------------other----------------')
print("isatty:", os.isatty(fd)) 


fd_r, fd_w = os.pipe()
print("fd_r:{0},fd_w:{1}".format(fd_r,fd_w))
os.closerange(fd_r, fd_w+1)
'''
father_id = os.fork() #has no attribute "fork"
if father_id:
	os.close(fd_w) #父进程不需要写
	f = os.fdopen(fd_r, "r")
	print(f.read())
	f.close()
	sys.exit()
else:
	os.close(fd_r) #子进程不需要读
	f = os.fdopen(fd_w, "w")
	f.write("child process")
	f.close()
	sys.exit()
'''


print('\n----------------Unix----------------')
uid = 100
gid = -1
#print(os.chflags("/home/python", stat.UF_NODUMP))
#os.chmod("/home/python", stat.S_IXUSR) #返回None
#os.chown("/home/python", uid, gid) #返回None
#os.chroot("/home/python") #返回None
#os.fchdir(fd) #通过文件描述符改变当前工作目录
#os.fdatasync(fd) #写入磁盘
#os.fpathconf(fd, "PC_LINK_MAX") # 获取最大文件连接数
#os.fpathconf(fd, "PC_NAME_MAX") # 获取文件名最大长度
#info = os.fstatvfs(fd)
#os.ftruncate(fd, 10)
#print("getcwu:", os.getcwdu())
#ret = os.lchflags(path, os.UF_IMMUTABLE )
#os.lchmod("/tmp/foo.txt", stat.S_IWOTH)
#os.lchown( path, -1, 500)

os.close(fd)
if os.path.exists(tempfile):
	os.unlink(tempfile)