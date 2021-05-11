
def write(filename):
    if filename != "sample.text":
        raise Exception("this is an error")
    f = open(filename,'w')
    f.write("this is my test program")
    f.close()

try:
    f = open("test.txt",'w')
    f.write("this is my test program")
except Exception:
    print("Error has occured")
else:
    print("success")
    f.close()

write("sample.text")
