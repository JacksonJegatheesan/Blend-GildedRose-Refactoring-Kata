class Operation(object):

    @staticmethod
    def increase_quality(item, qty=1):
        if item.quality < 50:
            item.quality += qty

    @staticmethod
    def sell_in(item):
        item.sell_in -= 1
