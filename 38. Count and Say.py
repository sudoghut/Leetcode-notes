def countNum(data):
    data = str(data)
    print("data:"+data)
    output = ""
    temp = ""
    isFirst = 1
    if len(data)==1:
        return "1"+data
    while len(data)>0:
        if isFirst == 1:
            print(1)
            temp = data[0]
            isFirst = 0
            if data[0]!=data[1]:
                output = "1"+data[0]
            data = data[1:]
            continue
        if data[0] == temp[0]:
            temp+=data[0]
            data = data[1:]
            if data=="":
                output+=(str(len(temp))+temp[0])
        else:
            if len(temp)>1:
                output+=(str(len(temp))+temp[0])
            if len(data)==1:
                output+=("1"+data[0])
            elif data[0]!= data[1]:                
                output+=("1"+data[0])                
            temp = data[0]
            
            data = data[1:]
    return output


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = 1
        data = 1
        lastData = 1
        while (count < n):
            data = countNum(lastData)
            lastData = data
            count+=1
        return str(data)
