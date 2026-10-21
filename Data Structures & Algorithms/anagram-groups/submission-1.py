class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings: Dict[tuple, List[str]] = {}
        for string in strs:
            sorted_tuple = tuple(sorted(string))
            if sorted_tuple in groupings:
                groupings[sorted_tuple].append(string)
            else:
                groupings[sorted_tuple] = [string]
        
        return [groupings[group] for group in groupings]
        
             