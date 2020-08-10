from set_journlPaper_code import journalPapers_code


class Article:
    year = ""
    link_to_download = ""
    issue = ""
    volume = ""
    Abstract = ""
    title = ""
    Authors = []
    number = ""
    code = ""
    JournalCode = ""
    SorY = ""

    def __init__(self, ltd, jc, v, i, c, auts, abs, ti, y):
        self.link_to_download = ltd
        self.JournalCode = jc
        self.volume = v
        self.issue = i
        self.number = c
        self.Authors = auts
        self.Abstract = abs
        self.title = ti
        self.year = y
        self.SorY = '0'
        self.code = self.SorY.join('1700').join(self.volume).join(self.number)


class Author:
    Affiliation = ""
    FirstName = ""
    LastName = ""

    def __init__(self, f, l, a):
        self.FirstName = f
        self.LastName = l
        self.Affiliation = a
