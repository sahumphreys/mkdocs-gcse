# rle.py
# SAH Sept 2023
# -------------------------------------------------------------------
# Take a string and compress using run length encoding
# ===================================================================

def Compress(str):
    result = ""
    i = 0
    
    while i < len(str):
        count = 1
        ch = str[i]
        while i + 1 < len(str) and str[i] == str[i + 1]:
            count += 1
            i += 1
        result += f"{ch}{count} "
        i += 1
    return result


#phrase = input("Enter phrase to compress: ")
phrase = "AAAAABBBBBCCCDDEFFFFF"
rle_phrase = Compress(phrase)
print(f"{phrase} compressed is {rle_phrase}")