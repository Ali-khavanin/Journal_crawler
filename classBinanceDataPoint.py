class DataPoint:
    symbol = ''
    time_stamp = None
    # sel_or_buy = None  # true for sale and false for buy
    order_amount = 0
    price = 0
    rank = 0

    def __init__(self, s, t, oa, pr, ran):
        self.symbol = s
        self.time_stamp = t
        # self.sel_or_buy = sob
        self.order_amount = oa
        self.price = pr
        self.rank = ran
