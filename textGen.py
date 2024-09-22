import time
def textgen(txt):
    gen=""
    arr="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm9876543210 !@#$%&*<>?/"
    for i in range(len(txt)):
        for j in range(len(arr)):
            print(gen+arr[j])
            if arr[j]==txt[i]:
                gen+=txt[i]
                break
            time.sleep(0.009)

txt=input(">> ")
textgen(txt)