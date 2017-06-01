# coding: utf-8
# Here your code !

inp=input().split(" ")

table={0,1,"b"}
q=[]
for i in range(5):
    for j in table:
         x=input().split(" ")
         q.append(x)

count = 1
qq = "0"

while (qq!="Y")&(qq!="N"):

    if(qq==0):
        if(inp[count]==0):
            qq=q[0][2]
            inp[count]=q[0][3]
            count +=q[0][4]
        elif(inp[count]==1):
            qq=q[1][2]
            inp[count]=q[1][3]
            count +=q[1][4]
        elif(inp[count]=="b"):
            qq=q[2][2]
            inp[count]=q[2][3]
            count +=q[2][4]
    elif(qq==1):
        if(inp[count]==0):
            qq=q[3][2]
            inp[count]=q[3][3]
            count +=q[3][4]
        elif(inp[count]==1):
            qq=q[4][2]
            inp[count]=q[4][3]
            count +=q[4][4]
        elif(inp[count]=="b"):
            qq=q[5][2]
            inp[count]=q[5][3]
            count +=q[5][4]
    elif(qq==2):
        if(inp[count]==0):
            qq=q[6][2]
            inp[count]=q[6][3]
            count +=q[6][4]
        elif(inp[count]==1):
            qq=q[7][2]
            inp[count]=q[7][3]
            count +=q[7][4]
        elif(inp[count]=="b"):
            qq=q[8][2]
            inp[count]=q[8][3]
            count +=q[8][4]
    elif(qq==3):
        if(inp[count]==0):
            qq=q[9][2]
            inp[count]=q[9][3]
            count +=q[9][4]
        elif(inp[count]==1):
            qq=q[10][2]
            inp[count]=q[10][3]
            count +=q[1][4]
        elif(inp[count]=="b"):
            qq=q[11][2]
            inp[count]=q[11][3]
            count +=q[11][4]
    elif(qq==4):
        if(inp[count]==0):
            qq=q[12][2]
            inp[count]=q[12][3]
            count +=q[12][4]
        elif(inp[count]==1):
            qq=q[13][2]
            inp[count]=q[13][3]
            count +=q[13][4]
        elif(inp[count]=="b"):
            qq=q[14][2]
            inp[count]=q[14][3]
            count +=q[14][4]
    elif(qq==5):
        if(inp[count]==0):
            qq=q[14][2]
            inp[count]=q[14][3]
            count +=q[14][4]
        elif(inp[count]==1):
            qq=q[14][2]
            inp[count]=q[14][3]
            count +=q[14][4]
        elif(inp[count]=="b"):
            qq=q[15][2]
            inp[count]=q[15][3]
            count +=q[15][4]

if qq=="Y":
    print("Yes")
elif qq=="N":
    print("NO")
