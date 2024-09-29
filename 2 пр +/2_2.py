import re
from playsound import playsound
def funct(tlfn):
    result = re.match(r'00\d\d\d\d\d\d\d\d$', tlfn) #'0034567891'
    if result is not None:
        tlfn = '++' + tlfn[2:]
        print(tlfn)
    else:
        playsound('C:\errorsound.mp3')

funct('0034567891')
funct('0934567891')
funct('0012345891')