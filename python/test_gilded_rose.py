# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(0, items[0].sell_in)


    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(13, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(12, items[0].sell_in)

    def test_backstage_passes_less_than11(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(10, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        
    def test_backstage_passes_less_than6(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(26, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

    def test_backstage_passes_expired(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
