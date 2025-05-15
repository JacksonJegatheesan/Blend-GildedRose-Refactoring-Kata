from oputils.opertationutils import Operation
from constants import (
    BACKSTAGE_PASSES,
)

class AgedBrie(object):
    @staticmethod
    def UpdateAgedBrie(item):
        Operation.increase_quality(item,2 if item.sell_in < 0 else 1)

class BackstagePasses(object):
    @staticmethod
    def UpdateBackstagePasses(item):
        check_value = lambda x: 1 if x >= 10 else 3 if x <= 6 else 2
        Operation.increase_quality(item, check_value(item.sell_in))

class AnythingElse(object):
    @staticmethod
    def UpdateAnythingElse(item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.name == BACKSTAGE_PASSES:
            BackstagePasses.UpdateBackstagePasses(item)
        else:
            Operation.increase_quality(item, -2 if item.sell_in < 0 else -1)