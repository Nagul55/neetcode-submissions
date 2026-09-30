class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        length=""
        while j<len(abbr):
            if abbr[j].isdigit():
                if length == "" and abbr[j]=="0":
                    return False
                length += abbr[j]
                j +=1

            else:
                if length:
                    i += int(length)
                    length = ""
                if i>=len(word) or word[i]!= abbr[j]:
                    return False
                        
                i +=1
                j +=1
        if length:
            i += int(length)
            
            
        return i==len(word)

    