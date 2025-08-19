# What is Module?
# Consider a module to be as same as a code library like a file containing  a set of functions you want to include in an application.

# Create  a module.
import mymodule
mymodule.greeting("Durgesh")     #Output:Hello, Durgesh

# Variables in Module 
# A Module can contain functions but also variables of all types.
import mymodule1 
a = mymodule1.person1["age"]
print(a)     #Output:   38

# Naming and Re-naming a Module with as keyword
import mymodule1 as mx 
a = mx.person1["age"]
print(a)      #Output:   38
 
import platform
x = platform.system()
print(x)     #Output:    Windows

# Using the dir() function
import platform
x = dir(platform)     
print(x)     #Output:   ['AndroidVer', 'IOSVersionInfo', '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_java_getprop', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates', '_parse_os_release', '_platform', '_platform_cache', '_sys_version', '_sys_version_cache', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_stages', '_win32_ver', '_wmi', '_wmi_query', 'android_ver', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'ios_ver', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']

# Import from Module - You can choose to import only parts of a module of a module by from keyword 
from mymodule2 import person1 
print(person1["age"])     #Output:   34

# Do not write like    =>  x = mymodule.person1["age"]
