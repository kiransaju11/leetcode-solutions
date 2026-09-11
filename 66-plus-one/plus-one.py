class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=""
        L1=[]
        for i in digits:
            str1=str1+str(i)
        int1=int(str1)
        int1=int1+1
        for i in str(int1):
            L1.append(int(i))
        return L1