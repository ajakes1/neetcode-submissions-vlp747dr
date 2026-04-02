class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = {}
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string in out_dict:
                out_dict[sorted_string].append(string)
            else:
                out_dict[sorted_string] = [string]
        return list(out_dict.values())