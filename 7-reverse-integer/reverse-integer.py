class Solution:
    def reverse(self, x: int) -> int:
    
        m = str(x)
        lem = len(m)
        ans = x
        list_1 = []
        int_result = 0
        is_negative = False
        if ans<0:
            is_negative = True
            ans = abs(ans)
        for i in range(lem) :
    
          ans = ans/10
          ans2 = int(ans *10)
          ans3 = str(ans2)
          length = len(ans3)
          result = ans3[length -1]
          list_1.append(result)
          ans = int(ans)
        # for digit in list_1 :
        #     int_result = int_result *10 + int(digit)
        # return int_result
        reversed_str = ''.join(list_1)
        int_result = int(reversed_str)
        if is_negative :
            int_result*= -1
            int_result =int( int_result/10)
        if int_result > 2**31 -1 or int_result< - 2**31-1:
            return 0 

        return int_result


        


   
     
       
        