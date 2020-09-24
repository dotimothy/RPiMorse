import sys
import morse2
import morse3

version = sys.version_info[0]
if(version == 2):
    print("hi")
    #morse2.main()
elif(version == 3):
    print("bye")
    #morse3.main()