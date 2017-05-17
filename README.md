# OS-Module

os.uname()  - gives system-dependent version information

os.environ - mapping object representing the string environment

os.chdir(path), os.getcwd(), os.fchdir(fd)

os.getenv(varname[,value]) - return the value of the environment variable varname if it exists or value if it doesn't, value defautls to NONE

os.putenv(varname[,value]) - set environment variable varname to string value

os.unsetenv(varname) - unset(delete) the environment variable varname

os.access(path, mode) - returns True if mode exists for the given path otherwise False
mode : OS.F_OK - existence of path
       OS.R_OK - existence of readibility
       OS.W_OK - existence of writability
       OS.X_OK - existence of executability
       
os.listdir(path) - returns the list of containing the names of entries in directory given by path. It doesn't include special entries '.' and '..' even if they are present in the path

os.mkdir(path[,mode]) - create a directory names path with numeric mode mode. The default mode is 0777 (octal). If directory already exists, OSError is raised.
