class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1 and strs[0] == "":
            return "exception!!!!"
        result = ":;".join(strs)
        return result
    def decode(self, s: str) -> List[str]:
        if s == "exception!!!!":
            return [""]
        elif not s:
            return []
        result = s.split(":;")
        return result