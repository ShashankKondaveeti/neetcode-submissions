class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for val in s:
            if val in s_dict:
                s_dict[val] += 1
            else:
                s_dict[val] = 1
        for val in t:
            if val in t_dict:
                t_dict[val] += 1
            else:
                t_dict[val] = 1
        if len(s_dict.keys()) == len(t_dict.keys()):
            for key in s_dict.keys():
                if key in t_dict:
                    if s_dict[key] == t_dict[key]:
                        continue
                    return False
                else: 
                    return False
        else:
            return False
        return True
