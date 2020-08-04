journalPapers_code: dict = {}
# print("{:04d}".format(45))

coder: int = 1
coder_to_string: str = ''
url: str = ''
file = open('allSinaWebs.txt', 'r')
allURLS = file.readlines()
for url in allURLS:
    print(url)
    coder_to_string = str(coder).zfill(4)
    journalPapers_code[coder_to_string] = url.rstrip('\n')
    coder += 1

print(journalPapers_code)
