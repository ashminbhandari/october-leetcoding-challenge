class Solution(object):
    def maximum69Number (self, num):
        arr = []
        while (num != 0):
            arr.insert(0, num % 10)
            num = num / 10
        for i in range(len(arr)):
            if arr[i] != 9:
                arr[i] = 9
                break
        strng = ''.join([str(elem) for elem in arr])
        return int(strng)