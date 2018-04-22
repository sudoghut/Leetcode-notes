def ceil(num):
    if int(num)<float(num):
        return int(num+1)
    else:
        return int(num)

def locXPos(i, numRows):
    s_num = i+1
    blocks = ceil(s_num/(2*numRows-2))-1
    left = s_num - blocks*(2*numRows-2)
    if left>numRows:
        return blocks*(numRows-1)+1+left-numRows
    else:
        return blocks*(numRows-1)+1

def locYPos(i, numRows):
    s_num = i+1
    pos_summary = s_num%(2*numRows-2)
    if pos_summary==0:
        pos_summary = 2*numRows-2
    if pos_summary<=numRows:
        return pos_summary
    else:
        return numRows-(pos_summary-numRows)

class Solution:
    def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #print(s)
        if(len(s)<=(numRows) or numRows==1):
            return s
        arr = [["" for i in range(ceil(len(s)/2))] for j in range(numRows)]
        output = ""
        for i in range(len(s)):
            xPos = locXPos(i, numRows)
            yPos = locYPos(i, numRows)
            #print([xPos, yPos])
            arr[yPos-1][xPos-1] = s[i]
        #print(arr)
        for i in arr:
            for j in i:               
                if j !="":
                    output+=j
        return output
