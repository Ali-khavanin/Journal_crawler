
from save_load_pickle import save_obj

journalPapers_code: dict = {}


# print("{:04d}".format(45))



coder: int = 1
coder_to_string: str = ''
url: str = ''
file = open('allSinaWebs.txt', 'r')
allURLS = file.readlines()
for url in allURLS:
    # print(url)
    coder_to_string = str(coder).zfill(8)
    journalPapers_code[coder_to_string] = url.rstrip('\n')
    coder += 1

print("going to save the dict ...")
save_obj(journalPapers_code, './journalPapersCode.pkl')
print("dict is saved")
# print(type(journalPapers_code))
# print(get_key('http://ma.iaumajlesi.ac.ir'))

# codes: dict = load_obj('./journalPapers.pkl')
#
# print(list(codes.items())[1200])

