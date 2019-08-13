class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Roman = [["", "I","II","III","IV","V","VI","VII","VIII","IX"],
                ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                 ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                ["","M","MM","MMM"]]
        res = []
        res.append(Roman[3][num/1000])
        res.append(Roman[2][num/100 % 10])
        res.append(Roman[1][num/10 %10])
        res.append(Roman[0][num % 10])
        return "".join(res)
        
            