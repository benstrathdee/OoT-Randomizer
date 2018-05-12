import logging

from BaseClasses import Item


def ItemFactory(items):
    ret = []
    singleton = False
    if isinstance(items, str):
        items = [items]
        singleton = True
    for item in items:
        if item in item_table:
            advancement, priority, type, code, index = item_table[item]
            ret.append(Item(item, advancement, priority, type, code, index))
        else:
            logging.getLogger('').warning('Unknown Item: %s', item)
            return None

    if singleton:
        return ret[0]
    return ret


# Format: Name: (Advancement, Priority, Type, ItemCode, Index)
item_table = {'Bow': (True, False, None, 0x0620, 0x31),
              'Progressive Hookshot': (True, False, None, 0x0120, 0x09),
              'Hammer': (True, False, None, 0x01A0, 0x0D),
              'Slingshot': (True, False, None, 0x0F60, 0x7B),
              'Boomerang': (True, False, None, 0x00C0, 0x06),
              'Bomb Bag': (True, False, None, 0x0680, 0x34),
              'Lens of Truth': (True, False, None, 0x0140, 0x0A),
              'Dins Fire': (True, False, None, 0x0B80, 0x5C),
              'Farores Wind': (True, False, None, 0x0BA0, 0x5D),
              'Nayrus Love': (True, False, None, 0x0BC0, 0x5E),
              'Fire Arrows': (True, False, None, 0x0B00, 0x58),
              'Ice Arrows': (True, False, None, 0x0B20, 0x59),
              'Light Arrows': (True, False, None, 0x0B40, 0x5A),
              'Fairy Ocarina': (True, False, None, 0x0760, 0x3B),
              'Ocarina of Time': (True, False, None, 0x0180, 0x0C),
              'Bottle': (True, False, None, 0x01E0, 0x0F),
              'Bottle with Letter': (True, False, None, 0x02A0, 0x15),
              'Bottle with Milk': (True, False, None, 0x0280, 0x14),
              'Pocket Egg': (True, False, None, 0x03A0, 0x1D),
              'Pocket Cucco': (True, False, None, 0x03C0, 0x1E),
              'Cojiro': (True, False, None, 0x01C0, 0x0E),
              'Odd Mushroom': (True, False, None, 0x03E0, 0x1F),
              'Odd Potion': (True, False, None, 0x0400, 0x20),
              'Poachers Saw': (True, False, None, 0x0420, 0x21),
              'Broken Sword': (True, False, None, 0x0440, 0x22),
              'Prescription': (True, False, None, 0x0460, 0x23),
              'Eyeball Frog': (True, False, None, 0x0480, 0x24),
              'Eyedrops': (True, False, None, 0x04A0, 0x25),
              'Claim Check': (True, False, None, 0x04C0, 0x26),
              'Kokiri Sword': (True, False, None, 0x04E0, 0x27),
              'Master Sword': (True, False, None, None, None),
              'Biggoron Sword': (True, False, None, 0x0100, 0x08),
              'Deku Shield': (False, True, None, 0x0520, 0x29),
              'Hylian Shield': (False, True, None, 0x0540, 0x2A),
              'Mirror Shield': (True, False, None, 0x0560, 0x2B),
              'Goron Tunic': (True, False, None, 0x0580, 0x2C),
              'Zora Tunic': (True, False, None, 0x05A0, 0x2D),
              'Iron Boots': (True, False, None, 0x05C0, 0x2E),
              'Hover Boots': (True, False, None, 0x05E0, 0x2F),
              'Progressive Strength Upgrade': (True, False, None, 0x06C0, 0x36),
              'Progressive Scale': (True, False, None, 0x0700, 0x38),
              'Progressive Wallet': (True, False, None, 0x08C0, 0x46),
              'Deku Stick Capacity': (False, True, None, 0x0EE0, 0x77),
              'Deku Nut Capacity': (False, True, None, 0x0F20, 0x79),
              'Stone of Agony': (True, False, None, 0x0720, 0x39),
              'Piece of Heart': (False, False, None, 0x07C0, 0x3E),
              'Recovery Heart': (False, True, None, 0x0900, 0x48),
              'Arrows (5)': (False, True, None, 0x0920, 0x49),
              'Arrows (10)': (False, True, None, 0x0940, 0x4A),
              'Arrows (30)': (False, True, None, 0x0960, 0x4B),
              'Bombs (5)': (False, True, None, 0x0020, 0x01),
              'Bombs (10)': (False, True, None, 0x0CC0, 0x66),
              'Bombs (20)': (False, True, None, 0x0CE0, 0x67),
              'Bombchus (5)': (False, False, None, 0x0D40, 0x6A),
              'Bombchus (10)': (False, False, None, 0x0060, 0x03),
              'Bombchus (20)': (False, False, None, 0x0D60, 0x6B),
              'Deku Nuts (5)': (False, True, None, 0x0040, 0x02),
              'Deku Nuts (10)': (False, True, None, 0x0C80, 0x64),
              'Rupee (1)': (False, False, None, 0x0980, 0x4C),
              'Rupees (5)': (False, False, None, 0x09A0, 0x4D),
              'Rupees (20)': (False, False, None, 0x09C0, 0x4E),
              'Rupees (50)': (False, False, None, 0x0AA0, 0x55),
              'Rupees (200)': (False, False, None, 0x0AC0, 0x56),
              'Ice Trap': (False, True, None, 0x0F80, 0x7C),
              'Magic Bean': (True, False, None, 0x02C0, 0x16),
              'Map': (False, False, 'Map', 0x0820, 0x41),
              'Compass': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Deku Tree)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Deku Tree)': (False, False, 'Compass', 0x0800, 0x40),
              'Map (Dodongos Cavern)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Dodongos Cavern)': (False, False, 'Compass', 0x0800, 0x40),
              'Map (Jabu Jabus Belly)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Jabu Jabus Belly)': (False, False, 'Compass', 0x0800, 0x40),
              'Map (Forest Temple)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Forest Temple)': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key (Forest Temple)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Forest Temple)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Bottom of the Well)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Bottom of the Well)': (False, False, 'Compass', 0x0800, 0x40),
              'Small Key (Bottom of the Well)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Fire Temple)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Fire Temple)': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key (Fire Temple)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Fire Temple)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Ice Cavern)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Ice Cavern)': (False, False, 'Compass', 0x0800, 0x40),
              'Map (Water Temple)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Water Temple)': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key (Water Temple)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Water Temple)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Shadow Temple)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Shadow Temple)': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key (Shadow Temple)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Shadow Temple)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Small Key (Gerudo Training Grounds)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Map (Spirit Temple)': (False, False, 'Map', 0x0820, 0x41),
              'Compass (Spirit Temple)': (False, False, 'Compass', 0x0800, 0x40),
              'Boss Key (Spirit Temple)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Spirit Temple)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Boss Key (Ganons Castle)': (False, False, 'BossKey', 0x07E0, 0x3F),
              'Small Key (Ganons Castle)': (False, False, 'SmallKey', 0x0840, 0x42),
              'Zeldas Letter': (True, False, None, None, None),
              'Zeldas Lullaby': (True, False, 'Song', 0x0A, 0x5),
              'Eponas Song': (True, False, 'Song', 0x09, 0x4),
              'Suns Song': (True, False, 'Song', 0x0B, 0x2),
              'Sarias Song': (True, False, 'Song', 0x08, 0x3),
              'Song of Time': (True, False, 'Song', 0x0C, 0x1),
              'Song of Storms': (True, False, 'Song', 0x0D, 0x0),
              'Minuet of Forest': (True, False, 'Song', 0x02, 0xB),
              'Prelude of Light': (True, False, 'Song', 0x07, 0x6),
              'Bolero of Fire': (True, False, 'Song', 0x03, 0xA),
              'Serenade of Water': (True, False, 'Song', 0x04, 0x9),
              'Nocturne of Shadow': (True, False, 'Song', 0x06, 0x7),
              'Requiem of Spirit': (True, False, 'Song', 0x05, 0x8),
              'Magic Meter': (True, False, 'Event', None, None),
              'Epona': (True, False, 'Event', None, None),
              'Gerudo Membership Card': (True, False, 'Event', 0x0740, 0x3A),
              'Gold Skulltulla Token': (True, False, 'Event', None, None),
              'Kokiri Emerald': (True, False, 'Event', None, None),
              'Goron Ruby': (True, False, 'Event', None, None),
              'Zora Sapphire': (True, False, 'Event', None, None),
              'Forest Medallion': (True, False, 'Event', None, None),
              'Fire Medallion': (True, False, 'Event', None, None),
              'Water Medallion': (True, False, 'Event', None, None),
              'Shadow Medallion': (True, False, 'Event', None, None),
              'Spirit Medallion': (True, False, 'Event', None, None),
              'Light Medallion': (True, False, 'Event', None, None),
              'Forest Trial Clear': (True, False, 'Event', None, None),
              'Fire Trial Clear': (True, False, 'Event', None, None),
              'Water Trial Clear': (True, False, 'Event', None, None),
              'Shadow Trial Clear': (True, False, 'Event', None, None),
              'Spirit Trial Clear': (True, False, 'Event', None, None),
              'Light Trial Clear': (True, False, 'Event', None, None),
              'Triforce': (True, False, 'Event', None, None)}

item_data = {'Bow': [0x4C, 0x80, 0x17, 0x57, 0x00, 0xBE],
              'Progressive Hookshot': [0x0B, 0x80, 0x2E, 0x4F, 0x00, 0xDD],
              'Hammer': [0x11, 0x80, 0x41, 0x38, 0x00, 0xF6],
              'Slingshot': [0x49, 0x80, 0x73, 0x6C, 0x01, 0x7B],
              'Boomerang': [0x0E, 0x80, 0x34, 0x35, 0x00, 0xE8],
              'Bomb Bag': [0x4F, 0x80, 0x1A, 0x5A, 0x00, 0xBF],
              'Lens of Truth': [0x0F, 0x80, 0x36, 0x39, 0x00, 0xEA],
              'Dins Fire': [0x05, 0x80, 0x64, 0xAD, 0x01, 0x5D],
              'Farores Wind': [0x0D, 0x80, 0x65, 0xAE, 0x01, 0x5D],
              'Nayrus Love': [0x13, 0x80, 0x66, 0xAF, 0x01, 0x5D],
              'Fire Arrows': [0x04, 0x80, 0x60, 0x70, 0x01, 0x58],
              'Ice Arrows': [0x0C, 0x80, 0x61, 0x71, 0x01, 0x58],
              'Light Arrows': [0x12, 0x80, 0x62, 0x72, 0x01, 0x58],
              'Bottle': [0x14, 0x80, 0x01, 0x42, 0x00, 0xC6],
              'Bottle with Letter': [0x1B, 0x80, 0x45, 0x99, 0x01, 0x0B],
              'Bottle with Milk': [0x1A, 0x80, 0x30, 0x98, 0x00, 0xDF],
              'Pocket Egg': [0x2D, 0x80, 0x29, 0x01, 0x00, 0xDA],
              'Pocket Cucco': [0x2E, 0x80, 0x44, 0x01, 0x01, 0x09],
              'Cojiro': [0x2F, 0x80, 0x5E, 0x02, 0x01, 0x09],
              'Odd Mushroom': [0x30, 0x80, 0x54, 0x03, 0x01, 0x41],
              'Odd Potion': [0x31, 0x80, 0x53, 0x04, 0x01, 0x40],
              'Poachers Saw': [0x32, 0x80, 0x40, 0x05, 0x00, 0xF5],
              'Broken Sword': [0x33, 0x80, 0x56, 0x08, 0x01, 0x43],
              'Prescription': [0x34, 0x80, 0x57, 0x09, 0x01, 0x46],
              'Eyeball Frog': [0x35, 0x80, 0x5A, 0x0D, 0x01, 0x49],
              'Eyedrops': [0x36, 0x80, 0x52, 0x0E, 0x01, 0x3F],
              'Claim Check': [0x37, 0x80, 0x55, 0xA4, 0x01, 0x8D],
              'Kokiri Sword': [0x3B, 0x80, 0x74, 0xA4, 0x01, 0x8D],
              'Biggoron Sword': [0x3D, 0x80, 0x43, 0x0B, 0x00, 0xF8],
              'Deku Shield': [0x3E, 0xA0, 0xE3, 0x4C, 0x00, 0xCB],
              'Hylian Shield': [0x3F, 0xA0, 0xD4, 0x4D, 0x00, 0xDC],
              'Mirror Shield': [0x40, 0x80, 0x3A, 0x4E, 0x00, 0xEE],
              'Goron Tunic': [0x42, 0xA0, 0x3C, 0x50, 0x00, 0xF2],
              'Zora Tunic': [0x43, 0xA0, 0x3D, 0x51, 0x00, 0xF2],
              'Iron Boots': [0x45, 0x80, 0x47, 0x53, 0x01, 0x18],
              'Hover Boots': [0x46, 0x80, 0x5F, 0x54, 0x01, 0x57],
              'Progressive Strength Upgrade': [0x52, 0x80, 0x4A, 0x5C, 0x01, 0x2D],
              'Progressive Scale': [0x54, 0x80, 0x2B, 0xCE, 0x00, 0xDB],
              'Progressive Wallet': [0x57, 0x80, 0x23, 0x5F, 0x00, 0xD1],
              'Deku Stick Capacity': [0x98, 0x80, 0xE5, 0x90, 0x00, 0xC7],
              'Deku Nut Capacity': [0x9A, 0x80, 0xEE, 0xA7, 0x00, 0xBB],
              'Stone of Agony': [0x6F, 0x80, 0x21, 0x68, 0x00, 0xC8],
              'Piece of Heart': [0x7A, 0x80, 0x14, 0xC2, 0x00, 0xBD],
              'Recovery Heart': [0x83, 0x80, 0x09, 0x55, 0x00, 0xB7],
              'Arrows (5)': [0x92, 0x48, 0xDB, 0xE6, 0x00, 0xD8],
              'Arrows (10)': [0x93, 0x4A, 0xDA, 0xE6, 0x00, 0xD8],
              'Arrows (30)': [0x94, 0x4A, 0xD9, 0xE6, 0x00, 0xD8],
              'Bombs (5)': [0x8E, 0x59, 0xE0, 0x32, 0x00, 0xCE],
              'Bombs (10)': [0x8F, 0x59, 0xE0, 0x32, 0x00, 0xCE],
              'Bombs (20)': [0x90, 0x59, 0xE0, 0x32, 0x00, 0xCE],
              'Bombchus (5)': [0x96, 0x80, 0xD8, 0x33, 0x00, 0xD9],
              'Bombchus (10)': [0x09, 0x80, 0xD8, 0x33, 0x00, 0xD9],
              'Bombchus (20)': [0x97, 0x80, 0xD8, 0x33, 0x00, 0xD9],
              'Deku Nuts (5)': [0x8C, 0x0C, 0xEE, 0x34, 0x00, 0xBB],
              'Deku Nuts (10)': [0x8D, 0x0C, 0xEE, 0x34, 0x00, 0xBB],
              'Rupee (1)': [0x84, 0x00, 0x93, 0x6F, 0x01, 0x7F],
              'Rupees (5)': [0x85, 0x01, 0x92, 0xCC, 0x01, 0x7F],
              'Rupees (20)': [0x86, 0x02, 0x91, 0xF0, 0x01, 0x7F],
              'Rupees (50)': [0x87, 0x14, 0x8F, 0xF1, 0x01, 0x7F],
              'Rupees (200)': [0x88, 0x13, 0x8E, 0xF2, 0x01, 0x7F],
              'Ice Trap': [0x85, 0x01, 0x92, 0xCC, 0x01, 0x7F], # Ice Trap in special spots will become a blue rupee.
              'Zeldas Lullaby': 0xD4,
              'Eponas Song': 0xD2,
              'Suns Song': 0xD3,
              'Sarias Song': 0xD1,
              'Song of Time': 0xD5,
              'Song of Storms': 0xD6,
              'Minuet of Forest': 0x73,
              'Bolero of Fire': 0x74,
              'Serenade of Water': 0x75,
              'Nocturne of Shadow': 0x77,
              'Requiem of Spirit': 0x76,
              'Prelude of Light': 0x78}