
import re
def validate(str):
    pat=r'\d+'
    print(pat)
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
    
print(validate("asdsab@!@234"))    