class Article:
    link_to_download = ""
    issue = ""
    volume = ""
    Abstract = ""
    title = ""
    Authors = []
    number = ""
    code = ""

    def __init__(self, ltd, v, i, c, auts):
        self.link_to_download = ltd
        self.volume = v
        self.issue = i
        self.number = c
        self.Authors = auts


class Author:
    Affiliation = ""
    FirstName = ""
    LastName = ""
    def __init__(self, f, l, a):
        self.FirstName = f
        self.LastName = l
        self.Affiliation = a
