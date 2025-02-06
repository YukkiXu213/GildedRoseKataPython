# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

     # Logical Error: Aged Brie should increase in quality over time
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 10, "Aged Brie should increase in quality over time.")

    # Logical Error: Backstage passes should increase in quality but drop to 0 after the concert
    def test_backstage_passes_quality_behavior(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 15, "Forcing failure: Backstage passes should NOT be 15.")
        
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
        self.assertEquals(["Sulfuras"], all_items)

    # Syntax Error: GildedRose does not have a method called `update_all_items`
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        
        try:
            all_items = gilded_rose.get_items()
            exists = True
        except AttributeError:
            exists = False

        self.assertEquals(exists, True, "Forcing failure: get_items() should exist but doesn't")


if __name__ == '__main__':
    unittest.main()
