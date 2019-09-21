
# coding: utf-8

# In[27]:


import sys
from itertools import permutations
def onecompliment(one):
    for i in range(len(one)):
        if(one[i]=='0'):
            one[i]='1'
        else:
            one[i]='0'
    ones=''
    for i in one:
        ones+=i
    return(ones)
def samecheck(n):
    ans=[]
    s=''
    j=0
    if(len(n)%2!=0):
        for i in range(0,len(n)-1,2):
            ans.append(n[i:i+2])
            p=permutations(ans)
        print("Strings with same checksum are")
        for i in list(p):
            j+=1
            print(s.join(i)+n[len(n)-1])
            if(j==5):
                break;
    else:
        for i in range(0,len(n),2):
            ans.append(n[i:i+2])
        p=permutations(ans)
        print("Strings with same checksum are")
        for i in list(p):
            j+=1
            print(s.join(i))
            if(j==5):
                break;
s_ip=list(map(int,sys.argv[1].split('.')))#source ip
d_ip=list(map(int,sys.argv[3].split('.')))#destination ip
s_port=int(sys.argv[2])#source port
d_port=int(sys.argv[4])#destination port
data=sys.argv[5]#data
samecheck(data)#function that prints strings having same checksum as that of the data
length=8+len(data)#length
proto=17#prototype
hexa_s_ip=[]#hexadecimal value of source ip in two halfs
hexa_d_ip=[]#hexadecimal value of destination ip in two halfs
temp1=[]#holds hexadecimal value of each 8 bits in source ip after dropping 0x
temp2=[]#holds hexadecimal value of each 8 bits in destination ip after dropping 0x
j=0
for i in range(4):
    temp1.append(hex(s_ip[i])[2:])
    if((len(temp1[j]))<2):
        temp1[j]='0'+temp1[j]
    temp2.append(hex(d_ip[i])[2:])
    if(len(temp2[j])<2):
        temp2[j]='0'+temp2[j]
    j+=1
for i in range(0,4,2):
    hexa_s_ip.append(hex(int(temp1[i]+temp1[i+1],16)))#combines two 8 bits of temp1
    hexa_d_ip.append(hex(int(temp2[i]+temp2[i+1],16)))#combines two 8 bits of temp2
if(len(data)%2!=0):
    data+=chr(0)#padding
temp_hexa_data=[]#holds hexadecimal value of each 8 bits in data after dropping 0x
hexa_data=[]#holds hexadecimal value of each 16 bits in data after dropping 0x
for i in data:
    temp_hexa_data.append(hex(ord(i))[2:])
for i in range(0,len(temp_hexa_data),2):
    hexa_data.append(hex(int(temp_hexa_data[i]+temp_hexa_data[i+1],16)))
z=hexa_d_ip+hexa_data+hexa_s_ip
checksum=s_port+d_port+length+length+proto
for i in z:
    checksum+=int(str(i),0)
checksum=hex(checksum)[2:]
if(len(checksum)>4):
    checksum=hex(int(checksum[1:],16)+int(checksum[0],16))
checksum=hex(int(onecompliment(list(bin(int(checksum,16))[2:])),2))
print("The Checksum is ",checksum)

