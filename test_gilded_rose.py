# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras, Hand of Ragnaros", sulfuras_item.name)

     # Logical Error: Aged Brie should increase in quality over time
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 10, "Aged Brie should increase in quality over time.")

    # Logical Error: Backstage passes should increase in quality but drop to 0 after the concert
    def test_backstage_passes_quality_behavior(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 20),  # Increases by 1
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),  # Increases by 2
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),   # Increases by 3
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)    # Drops to 0
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
    
        self.assertEqual(items[0].quality, 21, "Backstage passes should increase by 1 when sell_in > 10.")
        self.assertEqual(items[1].quality, 22, "Backstage passes should increase by 2 when 10 >= sell_in > 5.")
        self.assertEqual(items[2].quality, 23, "Backstage passes should increase by 3 when 5 >= sell_in > 0.")
        self.assertEqual(items[3].quality, 0, "Backstage passes should drop to 0 after the concert.")

        
    # Logical Error: Conjured items should degrade in Quality twice as fast
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8, "Conjured items should degrade in quality twice as fast.")


    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # Syntax Error: GildedRose does not have a method called `update_all_items`
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        
        try:
            all_items = gilded_rose.get_items()
            exists = True
        except AttributeError:
            exists = False

        self.assertEqual(exists, True, "Forcing failure: get_items() should exist but doesn't")


if __name__ == '__main__':
    unittest.main()
