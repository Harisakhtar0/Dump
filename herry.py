import os, platform
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dump1 import herry_main
    herry_main()

elif bit == '32bit':
    from dump import herry_main
    herry_main()
