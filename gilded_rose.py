# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemStrategy:
    #DO NOT CHANGE THIS ATTRIBUTE!
    def __init__(self, item):
        self.item = item

    def update(self):
        """Default update behavior for normal items"""
        self.item.sell_in -= 1
        self.decrease_quality()
        if self.item.sell_in < 0:
            self.decrease_quality()

    def increase_quality(self, amount=1):
        """Helper function to increase quality with max cap of 50"""
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        """Helper function to decrease quality with min cap of 0"""
        if self.item.quality > 0:
            self.item.quality -= amount


class NormalItem(ItemStrategy):
    """Regular item with normal degradation"""
    pass


class AgedBrie(ItemStrategy):
    """Aged Brie increases in quality as time passes"""
    def update(self):
        self.item.sell_in -= 1
        self.increase_quality()
        if self.item.sell_in < 0:
            self.increase_quality()


class BackstagePass(ItemStrategy):
    """Backstage passes increase in quality as concert nears, then drop to 0 after the event"""
    def update(self):
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.increase_quality(3)
        elif self.item.sell_in < 10:
            self.increase_quality(2)
        else:
            self.increase_quality()


class Sulfuras(ItemStrategy):
    """Sulfuras, a legendary item, never decreases in quality or sell_in"""
    def update(self):
        pass  # Sulfuras never changes


class ConjuredItem(ItemStrategy):
    """Conjured items degrade twice as fast"""
    def update(self):
        self.item.sell_in -= 1
        self.decrease_quality(2)
        if self.item.sell_in < 0:
            self.decrease_quality(2)


class GildedRose:
    """Main class for updating inventory items"""
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Updates quality of all items using appropriate strategy"""
        strategy_map = {
            "Aged Brie": AgedBrie,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePass,
            "Sulfuras, Hand of Ragnaros": Sulfuras,
            "Conjured Mana Cake": ConjuredItem
        }

        for item in self.items:
            strategy = strategy_map.get(item.name, NormalItem)
            strategy(item).update()

    def get_items(self):
        return [item.name for item in self.items]