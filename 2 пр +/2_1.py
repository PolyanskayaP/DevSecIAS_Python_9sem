import datetime
import time

def decor(func_na_modif):
    
    def modified():
        start_time = time.time()
        print(datetime.datetime.now()) #tek data
        func_na_modif()
        print("%s seconds " % (time.time() - start_time)) #vrem vip funk 
    return modified

@decor
def print_text():
    time.sleep(2)
    print("It's KB-2!!!!")
    
print_text()