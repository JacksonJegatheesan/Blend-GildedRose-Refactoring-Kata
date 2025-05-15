# -*- coding: utf-8 -*-
from constants import (
    AGED_BRIE,
    SULFURAS,
)

from bl.logic import (
    AgedBrie,
    AnythingElse,
)
from oputils.opertationutils import Operation

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            Operation.sell_in(item)
            if item.name == AGED_BRIE:
                AgedBrie.UpdateAgedBrie(item)
            elif item.name == SULFURAS:
                pass
            else:
                AnythingElse.UpdateAnythingElse(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
