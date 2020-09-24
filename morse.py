import sys
import morse2
import morse3

version = sys.version_info[0]
if(version == 3):
    morse3.main()
elif(version == 2):
    morse2.main()