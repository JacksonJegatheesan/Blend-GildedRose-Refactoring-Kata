# main.py
from constants import (
    AGED_BRIE,
    BACKSTAGE_PASSES,
    SULFURAS,
    ELIXIR_OF_THE_MONGOOSE
)

from gilded_rose import Item, GildedRose, GildedRoseV2

if __name__ == "__main__":
    items = [
        # Item(name=AGED_BRIE, sell_in=2, quality=0),
        Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=2, quality=5),
        # Item(name=SULFURAS, sell_in=-1, quality=-50),
        # Item(name=BACKSTAGE_PASSES, sell_in=15, quality=30),
        # Item("foo", 2, 5)
    ]

    app = GildedRose(items)

    days = 7
    for day in range(days):
        print(f"-------- day {day} --------")
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        app.update_quality()

    print("-------- GildedRoseV2 --------")
    items = [
        # Item(name=AGED_BRIE, sell_in=2, quality=0),
        # Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=3, quality=2),
        # Item(name=SULFURAS, sell_in=-1, quality=-50),
        # Item(name=BACKSTAGE_PASSES, sell_in=15, quality=30),
        Item("foo", 2, 5)
    ]

    app = GildedRoseV2(items)

    days = 7
    for day in range(days):
        print(f"-------- day {day} --------")
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        app.update_quality()
