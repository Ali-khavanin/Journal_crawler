class Article:
    link_to_download = ""
    issue = ""
    volume = ""
    Abstract = ""
    title = ""
    Authors = []
    number = ""
    code = ""

    def __init__(self, ltd, v, i , c):
        self.link_to_download = ltd
        self.volume = v
        self.issue = i
        self.number = c
