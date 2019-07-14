#!/usr/bin/env python

from __future__ import print_function

import random
import string
import sys

from enum import Enum

# enable debugging
#import cgitb
#cgitb.enable( )


#//**********************************************************************
#//
#//  BigMcLargeHuge name guidelines:
#//
#//  1.  The Rule of Tough always trumps the Rule of Funny.
#//  2.  Keep it PG.  I avoid words which imply graphic, personal
#//      injuries.  "Punch" is OK, but "Sword" or "Sever" is not.
#//  3.  If something in here appears to break rule #1 or #2, blame
#//      my artistic vision and/or poor judgement.
#//
#//  Rick Gutleber
#//
#//**********************************************************************

#//**********************************************************************
#//
#//  constants
#//
#//**********************************************************************

PROGRAM_NAME = "BigMcLargeHuge"
VERSION = "1.3.10"
PROGRAM_DESCRIPTION = "an action movie hero name generator"
COPYRIGHT_MESSAGE = "copyright (c) 2019 (2014), Rick and Simon Gutleber (rickg@his.com, simon@zycha.com)"

DESCRIPTION = PROGRAM_NAME + " " + VERSION + ", " + PROGRAM_DESCRIPTION 

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeoiuy"

nonRepeatThreshold = 20

# word types

class WordType( Enum ):
    noun      = 0,
    bodyPart  = 1,     # specific type of noun
    animal    = 2,     # specific type of noun
    meat      = 3,     # specific type of noun
    adjective = 4,
    verb      = 5,
    nounVerb  = 6,     # noun and verb
    modifier  = 7

# word lists

firstNameList = [
    "Abel",
    "Abraham",
    "Ace",
    "Agamemnon",
    "Ajax",
    "Al",
    "Angry",
    "Antonio",
    "Anvil",
    "Ape",
    "Ares",
    "Aristotle",
    "Ash",
    "Attila",
    "Augustus",
    "Axe",
    "Bad",
    "Badge",
    "Baltazar",
    "Bang",
    "Barge",
    "Barney",
    "Baron",
    "Barrage",
    "Bart",
    "Bash",
    "Batch",
    "Beat",
    "Beef",
    "Belt",
    "Bend",
    "Bert",
    "Biff",
    "Big",
    "Bilge",
    "Bill",
    "Billy",
    "Bjorn",
    "Black",
    "Blade",
    "Blam",
    "Blast",
    "Blunt",
    "Bob",
    "Bold",
    "Bolt",
    "Bomb",
    "Bone",
    "Boom",
    "Boot",
    "Boris",
    "Bort",
    "Bortus",
    "Boss",
    "Brad",
    "Brag",
    "Brawl",
    "Break",
    "Brick",
    "Brock",
    "Bruce",
    "Bruno",
    "Brunt",
    "Brute",
    "Brutus",
    "Bubba",
    "Buck",
    "Bud",
    "Buff",
    "Bug",
    "Bulge",
    "Bulk",
    "Bull",
    "Burn",
    "Burst",
    "Buster",
    "Butch",
    "Cable",
    "Cage",
    "Cain",
    "Captain",
    "Carl",
    "Cassius",
    "Chad",
    "Chap",
    "Char",
    "Charles",
    "Charleton",
    "Chaz",
    "Chester",
    "Chip",
    "Choke",
    "Chuck",
    "Chud",
    "Chunk",
    "Clamp",
    "Clank",
    "Claude",
    "Clayton",
    "Cliff",
    "Clint",
    "Clutch",
    "Clyde",
    "Colonel",
    "Commander",
    "Connor",
    "Count",
    "Crack",
    "Cram",
    "Crank",
    "Crash",
    "Crud",
    "Crunch",
    "Crush",
    "Crutch",
    "Dag",
    "Danger",
    "Dash",
    "Dave",
    "Dawg",
    "Dean",
    "Death",
    "Dennis",
    "Dice",
    "Dig",
    "Dirk",
    "Dirt",
    "Doc",
    "Doctor",
    "Dog",
    "Dolph",
    "Doug",
    "Drag",
    "Dread",
    "Duke",
    "Dwight",
    "Earl",
    "Ed",
    "Edward",
    "Elmer",
    "Eric",
    "Ernest",
    "Errol",
    "Fight",
    "Fist",
    "Flag",
    "Flank",
    "Flex",
    "Flint",
    "Flip",
    "Flog",
    "Force",
    "Fork",
    "Frag",
    "Francis",
    "Frank",
    "Fred",
    "Frederick",
    "Fridge",
    "Fry",
    "Fudd",
    "Funk",
    "Garth",
    "Gator",
    "General",
    "George",
    "Gil",
    "Glock",
    "Gold",
    "Goliath",
    "Gooch",
    "Gort",
    "Gouge",
    "Granite",
    "Gravel",
    "Grease",
    "Greasy",
    "Griff",
    "Grim",
    "Grind",
    "Gristle",
    "Grit",
    "Grizzly",
    "Grouch",
    "Grouchy",
    "Growl",
    "Grunt",
    "Guido",
    "Gulp",
    "Gun",
    "Gunner",
    "Gunther",
    "Gus",
    "Gusset",
    "Gut",
    "Guy",
    "Hack",
    "Ham",
    "Hank",
    "Hannibal",
    "Harm",
    "Harry",
    "Hawk",
    "Heavy",
    "Hector",
    "Heel",
    "Herman",
    "Hog",
    "Holt",
    "Horse",
    "Hound",
    "Howl",
    "Huge",
    "Hugo",
    "Hulk",
    "Hunk",
    "Hunter",
    "Hurl",
    "Hurt",
    "Husky",
    "Ignatius",
    "Ignatz",
    "Ike",
    "Ivan",
    "Jab",
    "Jack",
    "Jag",
    "Jam",
    "Jeb",
    "Jebediah",
    "Jed",
    "Jedediah",
    "Jeep",
    "Jet",
    "Jib",
    "Jim",
    "Jimbo",
    "Jock",
    "Joe",
    "John",
    "Jolt",
    "Kane",
    "Karl",
    "Kick",
    "Kid",
    "Killer",
    "King",
    "Kirk",
    "Knob",
    "Knuckles",
    "Kurt",
    "Lance",
    "Large",
    "Lars",
    "Lee",
    "Leif",
    "Leo",
    "Leon",
    "Leonardo",
    "Lex",
    "Lieutenant",
    "Lightning",
    "Lord",
    "Loud",
    "Lucas",
    "Lug",
    "Lugnut",
    "Lump",
    "Mace",
    "Mack",
    "Mad",
    "Major",
    "Malachi",
    "Mallet",
    "Manly",
    "Mario",
    "Marlon",
    "Mars",
    "Matt",
    "Max",
    "Maximilian",
    "Maximus",
    "Maxwell",
    "Mel",
    "Melchior",
    "Meteor",
    "Mick",
    "Moe",
    "Moose",
    "Mose",
    "Moses",
    "Mud",
    "Mug",
    "Napoleon",
    "Narc",
    "Nasty",
    "Nate",
    "Ned",
    "Nick",
    "Obidiah",
    "Ogre",
    "Otis",
    "Ox",
    "Pete",
    "Phil",
    "Pierce",
    "Pitch",
    "Plug",
    "Pound",
    "Pug",
    "Punch",
    "Punchy",
    "Punt",
    "Race",
    "Rage",
    "Rake",
    "Ralph",
    "Ram",
    "Reb",
    "Red",
    "Reef",
    "Rex",
    "Rhett",
    "Rib",
    "Ricardo",
    "Rick",
    "Rip",
    "Rock",
    "Rocket",
    "Rocko",
    "Rocky",
    "Rod",
    "Roll",
    "Rough",
    "Ruff",
    "Rugged",
    "Russell",
    "Rust",
    "Sal",
    "Sam",
    "Samson",
    "Sarge",
    "Saw",
    "Scorch",
    "Sergeant",
    "Shaft",
    "Shane",
    "Shark",
    "Sharp",
    "Shiv",
    "Shove",
    "Shrapnel",
    "Sid",
    "Sidney",
    "Simon",
    "Singe",
    "Sizzle",
    "Skip",
    "Skunk",
    "Slab",
    "Slag",
    "Slam",
    "Slap",
    "Slate",
    "Sledge",
    "Slog",
    "Slug",
    "Slump",
    "Smash",
    "Smoke",
    "Smudge",
    "Snag",
    "Snap",
    "Snarl",
    "Solid",
    "Solomon",
    "Spank",
    "Spanky",
    "Spartacus",
    "Speed",
    "Spiff",
    "Spit",
    "Splat",
    "Splint",
    "Split",
    "Splot",
    "Spode",
    "Spork",
    "Sport",
    "Spud",
    "Spuds",
    "Spunk",
    "Squid",
    "Squint",
    "Stag",
    "Stan",
    "Stanley",
    "Steel",
    "Steve",
    "Stick",
    "Stomp",
    "Stone",
    "Stretch",
    "Strike",
    "Strong",
    "Stubby",
    "Stud",
    "Studly",
    "Studs",
    "Stump",
    "Stumpy",
    "Surly",
    "Tank",
    "Ted",
    "Tex",
    "Thad",
    "Thaddeus",
    "Thick",
    "Thor",
    "Throb",
    "Thud",
    "Thug",
    "Thump",
    "Thunder",
    "Tiberius",
    "Tim",
    "Tom",
    "Tony",
    "Tor",
    "Torch",
    "Torgo",
    "Touch",
    "Tough",
    "Trip",
    "Troy",
    "Truck",
    "Trunk",
    "Tuff",
    "Tug",
    "Tyrone",
    "Tyson",
    "Vic",
    "Victor",
    "Vince",
    "Volt",
    "Wallop",
    "Wally",
    "Walt",
    "Wayne",
    "Whack",
    "Wolf",
    "Worf",
    "Wrack",
    "Wrath",
    "Wreck",
    "Wrench",
    "Yak",
    "Yancy",
    "Yank",
    "Zack",
    "Zane",
    "Zapp",
    "Zeb",
    "Zebulon",
    "Zed",
    "Zeke",
    "Zeus",
    "Zit",
]

lastNameOneList = [
      # name      # syllables # word type
    [ "Able",         2,      WordType.adjective ],
    [ "Angry",        2,      WordType.adjective ],
    [ "Ankle",        2,      WordType.bodyPart  ],
    [ "Anvil",        2,      WordType.noun      ],
    [ "Ape",          1,      WordType.animal    ],
    [ "Assault",      2,      WordType.verb      ],
    [ "Attack",       2,      WordType.verb      ],
    [ "Awful",        2,      WordType.adjective ],
    [ "Ax",           1,      WordType.noun      ],
    [ "Back",         1,      WordType.bodyPart  ],
    [ "Bacon",        2,      WordType.meat      ],
    [ "Bad",          1,      WordType.adjective ],
    [ "Badger",       2,      WordType.animal    ],
    [ "Bang",         1,      WordType.noun      ],
    [ "Barge",        1,      WordType.verb      ],
    [ "Barrage",      2,      WordType.noun      ],
    [ "Bash",         1,      WordType.verb      ],
    [ "Batch",        1,      WordType.noun      ],
    [ "Batter",       2,      WordType.verb      ],
    [ "Battle",       2,      WordType.nounVerb  ],
    [ "Bear",         1,      WordType.animal    ],
    [ "Beast",        1,      WordType.noun      ],
    [ "Beat",         1,      WordType.verb      ],
    [ "Beef",         1,      WordType.meat      ],
    [ "Bend",         1,      WordType.verb      ],
    [ "Bent",         1,      WordType.adjective ],
    [ "Berserk",      2,      WordType.adjective ],
    [ "Big",          1,      WordType.adjective ],
    [ "Bigger",       1,      WordType.adjective ],
    [ "Bison",        2,      WordType.animal    ],
    [ "Bite",         1,      WordType.verb      ],
    [ "Black",        1,      WordType.adjective ],
    [ "Blade",        1,      WordType.noun      ],
    [ "Blast",        1,      WordType.nounVerb  ],
    [ "Block",        1,      WordType.nounVerb  ],
    [ "Blunt",        1,      WordType.adjective ],
    [ "Body",         2,      WordType.bodyPart  ],
    [ "Bold",         1,      WordType.adjective ],
    [ "Bolt",         1,      WordType.noun      ],
    [ "Bomb",         1,      WordType.noun      ],
    [ "Bone",         1,      WordType.bodyPart  ],
    [ "Boot",         1,      WordType.nounVerb  ],
    [ "Boulder",      2,      WordType.noun      ],
    [ "Box",          1,      WordType.noun      ],
    [ "Brave",        1,      WordType.adjective ],
    [ "Brawl",        1,      WordType.verb      ],
    [ "Break",        1,      WordType.verb      ],
    [ "Brick",        1,      WordType.noun      ],
    [ "Broke",        1,      WordType.adjective ],
    [ "Broken",       2,      WordType.adjective ],
    [ "Bruise",       1,      WordType.nounVerb  ],
    [ "Brutal",       2,      WordType.adjective ],
    [ "Brute",        1,      WordType.noun      ],
    [ "Buff",         1,      WordType.adjective ],
    [ "Bulge",        1,      WordType.bodyPart  ],
    [ "Bulk",         1,      WordType.adjective ],
    [ "Bull",         1,      WordType.animal    ],
    [ "Bullet",       2,      WordType.noun      ],
    [ "Burn",         1,      WordType.verb      ],
    [ "Burnt",        1,      WordType.adjective ],
    [ "Burst",        1,      WordType.verb      ],
    [ "Bust",         1,      WordType.verb      ],
    [ "Buster",       2,      WordType.noun      ],
    [ "Butt",         1,      WordType.bodyPart  ],
    [ "Cannon",       2,      WordType.noun      ],
    [ "Castle",       2,      WordType.noun      ],
    [ "Char",         1,      WordType.verb      ],
    [ "Chest",        1,      WordType.bodyPart  ],
    [ "Chew",         1,      WordType.verb      ],
    [ "Chin",         1,      WordType.bodyPart  ],
    [ "Chisel",       2,      WordType.nounVerb  ],
    [ "Choke",        1,      WordType.verb      ],
    [ "Chomp",        1,      WordType.verb      ],
    [ "Chop",         1,      WordType.verb      ],
    [ "Chunk",        1,      WordType.noun      ],
    [ "Chrome",       1,      WordType.adjective ],
    [ "Clamp",        1,      WordType.verb      ],
    [ "Clobber",      3,      WordType.verb      ],
    [ "Conquer",      2,      WordType.verb      ],
    [ "Cougar",       2,      WordType.animal    ],
    [ "Crack",        1,      WordType.nounVerb  ],
    [ "Cracked",      1,      WordType.adjective ],
    [ "Cram",         1,      WordType.verb      ],
    [ "Crank",        1,      WordType.verb      ],
    [ "Crazy",        2,      WordType.adjective ],
    [ "Cripple",      2,      WordType.verb      ],
    [ "Crooked",      2,      WordType.adjective ],
    [ "Crumble",      2,      WordType.verb      ],
    [ "Crumple",      2,      WordType.verb      ],
    [ "Crunch",       1,      WordType.verb      ],
    [ "Crush",        1,      WordType.verb      ],
    [ "Crushed",      1,      WordType.adjective ],
    [ "Danger",       2,      WordType.noun      ],
    [ "Dark",         1,      WordType.adjective ],
    [ "de la ",       2,      WordType.modifier  ],
    [ "Dead",         1,      WordType.adjective ],
    [ "Dirt",         1,      WordType.noun      ],
    [ "Dog",          1,      WordType.animal    ],
    [ "Double",       2,      WordType.adjective ],
    [ "Drag",         1,      WordType.verb      ],
    [ "Dragon",       2,      WordType.animal    ],
    [ "Dread",        1,      WordType.verb      ],
    [ "Drop",         1,      WordType.verb      ],
    [ "Eat",          1,      WordType.verb      ],
    [ "Elbow",        2,      WordType.bodyPart  ],
    [ "Fear",         1,      WordType.noun      ],
    [ "Fight",        1,      WordType.nounVerb  ],
    [ "Fire",         2,      WordType.noun      ],
    [ "Fist",         1,      WordType.bodyPart  ],
    [ "Fizzle",       2,      WordType.verb      ],
    [ "Flame",        1,      WordType.noun      ],
    [ "Flank",        1,      WordType.noun      ],
    [ "Flat",         1,      WordType.adjective ],
    [ "Flog",         1,      WordType.verb      ],
    [ "Foot",         1,      WordType.bodyPart  ],
    [ "Frag",         1,      WordType.verb      ],
    [ "Franken",      2,      WordType.adjective ],   # we don't want it to work like the other modifiers
    [ "Fury",         2,      WordType.noun      ],
    [ "Gator",        2,      WordType.animal    ],
    [ "Giant",        2,      WordType.adjective ],
    [ "Goat",         1,      WordType.animal    ],
    [ "Gold",         1,      WordType.adjective ],
    [ "Gorilla",      3,      WordType.animal    ],
    [ "Gouge",        1,      WordType.nounVerb  ],
    [ "Grab",         1,      WordType.verb      ],
    [ "Granite",      2,      WordType.adjective ],
    [ "Gravel",       2,      WordType.adjective ],
    [ "Grease",       1,      WordType.noun      ],
    [ "Grim",         1,      WordType.adjective ],
    [ "Grime",        1,      WordType.noun      ],
    [ "Grind",        1,      WordType.verb      ],
    [ "Gristle",      2,      WordType.noun      ],
    [ "Grit",         1,      WordType.noun      ],
    [ "Grizzly",      2,      WordType.animal    ],
    [ "Ground",       1,      WordType.verb      ],
    [ "Growl",        1,      WordType.verb      ],
    [ "Grunt",        1,      WordType.nounVerb  ],
    [ "Gut",          1,      WordType.bodyPart  ],
    [ "Hack",         1,      WordType.verb      ],
    [ "Ham",          1,      WordType.meat      ],
    [ "Hammer",       2,      WordType.noun      ],
    [ "Hard",         1,      WordType.adjective ],
    [ "Harm",         1,      WordType.verb      ],
    [ "Hatchet",      2,      WordType.noun      ],
    [ "Hawk",         1,      WordType.animal    ],
    [ "Head",         1,      WordType.bodyPart  ],
    [ "Heart",        1,      WordType.bodyPart  ],
    [ "Heave",        1,      WordType.verb      ],
    [ "Heavy",        2,      WordType.adjective ],
    [ "Heel",         1,      WordType.bodyPart  ],
    [ "High",         1,      WordType.adjective ],
    [ "Hinder",       2,      WordType.bodyPart  ],
    [ "Hit",          1,      WordType.verb      ],
    [ "Hog",          1,      WordType.animal    ],
    [ "Horse",        1,      WordType.animal    ],
    [ "Hound",        1,      WordType.animal    ],
    [ "Huge",         1,      WordType.adjective ],
    [ "Hulk",         1,      WordType.noun      ],
    [ "Hunk",         1,      WordType.noun      ],
    [ "Hunt",         1,      WordType.verb      ],
    [ "Hurl",         1,      WordType.verb      ],
    [ "Hurt",         1,      WordType.verb      ],
    [ "Husky",        2,      WordType.adjective ],
    [ "Iron",         2,      WordType.adjective ],
    [ "Jab",          1,      WordType.verb      ],
    [ "Jagged",       2,      WordType.adjective ],
    [ "Jam",          1,      WordType.verb      ],
    [ "Jaw",          1,      WordType.bodyPart  ],
    [ "Jet",          1,      WordType.noun      ],
    [ "Jump",         1,      WordType.verb      ],
    [ "Kick",         1,      WordType.verb      ],
    [ "Kicking",      1,      WordType.adjective ],
    [ "Kill",         1,      WordType.verb      ],
    [ "Knee",         1,      WordType.bodyPart  ],
    [ "Knuckle",      2,      WordType.bodyPart  ],
    [ "Large",        1,      WordType.adjective ],
    [ "Lava",         2,      WordType.noun      ],
    [ "Leather",      2,      WordType.noun      ],
    [ "Leopard",      2,      WordType.animal    ],
    [ "Lion",         2,      WordType.animal    ],
    [ "Log",          1,      WordType.noun      ],
    [ "Loud",         1,      WordType.adjective ],
    [ "Lug",          1,      WordType.verb      ],
    [ "Lumber",       2,      WordType.nounVerb  ],
    [ "Mad",          1,      WordType.adjective ],
    [ "Mallet",       2,      WordType.noun      ],
    [ "Man",          1,      WordType.bodyPart  ],
    [ "Mangle",       2,      WordType.verb      ],
    [ "Mash",         1,      WordType.verb      ],
    [ "Master",       1,      WordType.noun      ],
    [ "Maul",         1,      WordType.verb      ],
    [ "Mean",         1,      WordType.adjective ],
    [ "Meat",         1,      WordType.meat      ],
    [ "Meaty",        2,      WordType.adjective ],
    [ "Mega",         2,      WordType.modifier  ],
    [ "Metal",        2,      WordType.noun      ],
    [ "Mighty",       2,      WordType.adjective ],
    [ "Million",      2,      WordType.adjective ],
    [ "Monkey",       2,      WordType.animal    ],
    [ "Monster",      2,      WordType.animal    ],
    [ "Moose",        1,      WordType.animal    ],
    [ "Mountain",     2,      WordType.noun      ],
    [ "Mud",          1,      WordType.noun      ],
    [ "Mug",          1,      WordType.nounVerb  ],
    [ "Mule",         1,      WordType.animal    ],
    [ "Munch",        1,      WordType.verb      ],
    [ "Muscle",       2,      WordType.bodyPart  ],
    [ "Nasty",        2,      WordType.adjective ],
    [ "Neck",         1,      WordType.bodyPart  ],
    [ "Nitro",        2,      WordType.noun      ],
    [ "Noisy",        2,      WordType.adjective ],
    [ "Nuke",         1,      WordType.nounVerb  ],
    [ "Octo",         2,      WordType.adjective ],
    [ "Ogre",         2,      WordType.noun      ],
    [ "Ox",           1,      WordType.animal    ],
    [ "Oxen",         2,      WordType.animal    ],
    [ "Pain",         1,      WordType.noun      ],
    [ "Pig",          1,      WordType.animal    ],
    [ "Pile",         2,      WordType.noun      ],
    [ "Pistol",       2,      WordType.noun      ],
    [ "Plank",        1,      WordType.noun      ],
    [ "Plug",         1,      WordType.nounVerb  ],
    [ "Pork",         1,      WordType.meat      ],
    [ "Pound",        1,      WordType.verb      ],
    [ "Power",        2,      WordType.noun      ],
    [ "Pummel",       2,      WordType.verb      ],
    [ "Punch",        1,      WordType.nounVerb  ],
    [ "Punching",     1,      WordType.adjective ],
    [ "Punk",         1,      WordType.noun      ],
    [ "Punt",         1,      WordType.verb      ],
    [ "Quarrel",      2,      WordType.verb      ],
    [ "Quadra",       2,      WordType.adjective ],
    [ "Quick",        1,      WordType.adjective ],
    [ "Rage",         1,      WordType.noun      ],
    [ "Ram",          1,      WordType.nounVerb  ],
    [ "Ready",        2,      WordType.adjective ],
    [ "Red",          1,      WordType.adjective ],
    [ "Rhino",        2,      WordType.animal    ],
    [ "Rib",          1,      WordType.bodyPart  ],
    [ "Rigid",        2,      WordType.adjective ],
    [ "Rip",          1,      WordType.verb      ],
    [ "Rivet",        2,      WordType.nounVerb  ],
    [ "Roar",         1,      WordType.verb      ],
    [ "Rock",         1,      WordType.noun      ],
    [ "Rocket",       2,      WordType.noun      ],
    [ "Rough",        1,      WordType.adjective ],
    [ "Rowdy",        2,      WordType.adjective ],
    [ "Rugged",       2,      WordType.adjective ],
    [ "Rumble",       2,      WordType.verb      ],
    [ "Rump",         1,      WordType.bodyPart  ],
    [ "Rust",         1,      WordType.noun      ],
    [ "Rusty",        2,      WordType.adjective ],
    [ "Scar",         1,      WordType.noun      ],
    [ "Scare",        1,      WordType.verb      ],
    [ "Scary",        2,      WordType.adjective ],
    [ "Scissor",      1,      WordType.verb      ],
    [ "Scorch",       1,      WordType.verb      ],
    [ "Scrape",       1,      WordType.verb      ],
    [ "Scream",       1,      WordType.nounVerb  ],
    [ "Schwarz",      1,      WordType.adjective ],
    [ "Shank",        1,      WordType.nounVerb  ],
    [ "Shark",        1,      WordType.noun      ],
    [ "Sharp",        1,      WordType.adjective ],
    [ "Shatter",      2,      WordType.verb      ],
    [ "Shoot",        1,      WordType.verb      ],
    [ "Shoulder",     2,      WordType.bodyPart  ],
    [ "Shout",        1,      WordType.verb      ],
    [ "Shove",        1,      WordType.verb      ],
    [ "Shovel",       1,      WordType.noun      ],
    [ "Shrapnel",     2,      WordType.noun      ],
    [ "Side",         1,      WordType.adjective ],
    [ "Singe",        1,      WordType.verb      ],
    [ "Sizzle",       2,      WordType.verb      ],
    [ "Skull",        1,      WordType.bodyPart  ],
    [ "Skunk",        1,      WordType.animal    ],
    [ "Slab",         1,      WordType.noun      ],
    [ "Slag",         1,      WordType.verb      ],
    [ "Slam",         1,      WordType.verb      ],
    [ "Slap",         1,      WordType.verb      ],
    [ "Slug",         1,      WordType.verb      ],
    [ "Smash",        1,      WordType.verb      ],
    [ "Smoke",        1,      WordType.noun      ],
    [ "Smug",         1,      WordType.adjective ],
    [ "Snake",        1,      WordType.animal    ],
    [ "Snap",         1,      WordType.verb      ],
    [ "Snarl",        1,      WordType.verb      ],
    [ "Solid",        2,      WordType.adjective ],
    [ "Spank",        1,      WordType.verb      ],
    [ "Speed",        1,      WordType.noun      ],
    [ "Spit",         1,      WordType.verb      ],
    [ "Spittle",      2,      WordType.noun      ],
    [ "Splinter",     2,      WordType.verb      ],
    [ "Split",        1,      WordType.verb      ],
    [ "Sprain",       1,      WordType.nounVerb  ],
    [ "Spud",         1,      WordType.noun      ],
    [ "Square",       1,      WordType.adjective ],
    [ "Squash",       1,      WordType.verb      ],
    [ "Squat",        1,      WordType.verb      ],
    [ "Squeeze",      1,      WordType.verb      ],
    [ "Stag",         1,      WordType.animal    ],
    [ "Stamp",        1,      WordType.verb      ],
    [ "Steak",        1,      WordType.meat      ],
    [ "Steel",        1,      WordType.adjective ],
    [ "Stick",        1,      WordType.noun      ],
    [ "Stomp",        1,      WordType.verb      ],
    [ "Stone",        1,      WordType.adjective ],
    [ "Storm",        1,      WordType.noun      ],
    [ "Strangle",     2,      WordType.verb      ],
    [ "Stretch",      1,      WordType.verb      ],
    [ "Strike",       1,      WordType.verb      ],
    [ "Strong",       1,      WordType.adjective ],
    [ "Stud",         1,      WordType.noun      ],
    [ "Stump",        1,      WordType.noun      ],
    [ "Super",        1,      WordType.adjective ],
    [ "Sweat",        1,      WordType.nounVerb  ],
    [ "Sweaty",       1,      WordType.adjective ],
    [ "Swift",        1,      WordType.adjective ],
    [ "Tackle",       2,      WordType.verb      ],
    [ "Tank",         1,      WordType.noun      ],
    [ "Tear",         1,      WordType.verb      ],
    [ "Teeth",        1,      WordType.bodyPart  ],
    [ "Thick",        1,      WordType.adjective ],
    [ "Thrash",       1,      WordType.verb      ],
    [ "Throat",       1,      WordType.bodyPart  ],
    [ "Throw",        1,      WordType.verb      ],
    [ "Thud",         1,      WordType.noun      ],
    [ "Thump",        1,      WordType.verb      ],
    [ "Thousand",     2,      WordType.adjective ],
    [ "Thunder",      2,      WordType.adjective ],
    [ "Tiger",        2,      WordType.animal    ],
    [ "Toad",         1,      WordType.animal    ],
    [ "Tooth",        1,      WordType.bodyPart  ],
    [ "Torch",        1,      WordType.noun      ],
    [ "Tough",        1,      WordType.adjective ],
    [ "Tower",        2,      WordType.noun      ],
    [ "Trample",      2,      WordType.verb      ],
    [ "Triple",       2,      WordType.adjective ],
    [ "Truck",        1,      WordType.noun      ],
    [ "Twist",        1,      WordType.verb      ],
    [ "Twister",      1,      WordType.noun      ],
    [ "Ugly",         2,      WordType.adjective ],
    [ "van der ",     2,      WordType.modifier  ],
    [ "Viper",        2,      WordType.animal    ],
    [ "Volt",         1,      WordType.noun      ],
    [ "von ",         1,      WordType.modifier  ],
    [ "Vulture",      2,      WordType.animal    ],
    [ "Wall",         1,      WordType.noun      ],
    [ "Wallop",       2,      WordType.verb      ],
    [ "War",          1,      WordType.noun      ],
    [ "Whip",         1,      WordType.nounVerb  ],
    [ "Widow",        2,      WordType.noun      ],
    [ "Wild",         1,      WordType.adjective ],
    [ "Wolf",         1,      WordType.animal    ],
    [ "Wood",         1,      WordType.noun      ],
    [ "Wound",        1,      WordType.verb      ],
    [ "Wrath",        1,      WordType.noun      ],
    [ "Wreck",        1,      WordType.verb      ],
    [ "Wrench",       1,      WordType.nounVerb  ],
    [ "Wrestle",      1,      WordType.verb      ],
    [ "Yak",          1,      WordType.animal    ],
    [ "Yank",         1,      WordType.verb      ],
]


lastNameTwoList = [
      # name      # syllables # word type
    [ "able",         2,      WordType.modifier  ],
    [ "alo",          2,      WordType.modifier  ],
    [ "alot",         2,      WordType.modifier  ],
    [ "amundo",       3,      WordType.modifier  ],
    [ "angry",        2,      WordType.adjective ],
    [ "ankle",        2,      WordType.bodyPart  ],
    [ "anvil",        2,      WordType.noun      ],
    [ "ape",          1,      WordType.animal    ],
    [ "arillo",       3,      WordType.modifier  ],
    [ "assault",      2,      WordType.verb      ],
    [ "attack",       2,      WordType.noun      ],
    [ "axe",          1,      WordType.noun      ],
    [ "back",         1,      WordType.bodyPart  ],
    [ "bacon",        2,      WordType.meat      ],
    [ "bad",          1,      WordType.adjective ],
    [ "badger",       2,      WordType.animal    ],
    [ "bang",         1,      WordType.noun      ],
    [ "banger",       2,      WordType.noun      ],
    [ "barrage",      2,      WordType.noun      ],
    [ "bash",         1,      WordType.verb      ],
    [ "basher",       2,      WordType.noun      ],
    [ "batch",        1,      WordType.noun      ],
    [ "batter",       2,      WordType.verb      ],
    [ "battle",       2,      WordType.nounVerb  ],
    [ "bear",         1,      WordType.animal    ],
    [ "beast",        1,      WordType.animal    ],
    [ "beef",         1,      WordType.meat      ],
    [ "bender",       2,      WordType.noun      ],
    [ "berg",         1,      WordType.modifier  ],
    [ "berserk",      1,      WordType.adjective ],
    [ "big",          1,      WordType.adjective ],
    [ "bison",        2,      WordType.animal    ],
    [ "bite",         1,      WordType.verb      ],
    [ "biter",        2,      WordType.noun      ],
    [ "blade",        1,      WordType.noun      ],
    [ "blast",        1,      WordType.nounVerb  ],
    [ "blaster",      2,      WordType.noun      ],
    [ "block",        1,      WordType.nounVerb  ],
    [ "body",         2,      WordType.bodyPart  ],
    [ "bold",         1,      WordType.adjective ],
    [ "bolt",         1,      WordType.noun      ],
    [ "bomb",         1,      WordType.verb      ],
    [ "bomber",       2,      WordType.noun      ],
    [ "bone",         1,      WordType.noun      ],
    [ "boot",         1,      WordType.nounVerb  ],
    [ "boulder",      2,      WordType.noun      ],
    [ "box",          1,      WordType.noun      ],
    [ "brave",        1,      WordType.adjective ],
    [ "brawl",        1,      WordType.nounVerb  ],
    [ "brawler",      2,      WordType.noun      ],
    [ "break",        1,      WordType.verb      ],
    [ "breaker",      2,      WordType.noun      ],
    [ "breath",       1,      WordType.bodyPart  ],
    [ "brick",        1,      WordType.noun      ],
    [ "bringer",      2,      WordType.noun      ],
    [ "bruise",       1,      WordType.verb      ],
    [ "bruiser",      2,      WordType.noun      ],
    [ "brutal",       1,      WordType.adjective ],
    [ "brute",        1,      WordType.noun      ],
    [ "bucket",       2,      WordType.noun      ],
    [ "bulge",        1,      WordType.noun      ],
    [ "bulk",         1,      WordType.noun      ],
    [ "bull",         1,      WordType.animal    ],
    [ "bullet",       2,      WordType.noun      ],
    [ "burger",       2,      WordType.modifier  ],
    [ "burn",         1,      WordType.verb      ],
    [ "burner",       2,      WordType.verb      ],
    [ "burst",        1,      WordType.verb      ],
    [ "buster",       2,      WordType.noun      ],
    [ "butt",         1,      WordType.bodyPart  ],
    [ "cage",         1,      WordType.noun      ],
    [ "cannon",       2,      WordType.noun      ],
    [ "castle",       2,      WordType.noun      ],
    [ "charger",      2,      WordType.noun      ],
    [ "cheese",       1,      WordType.noun      ],
    [ "chest",        1,      WordType.bodyPart  ],
    [ "chewer",       2,      WordType.noun      ],
    [ "chin",         1,      WordType.bodyPart  ],
    [ "chisel",       2,      WordType.nounVerb  ],
    [ "choke",        1,      WordType.verb      ],
    [ "chomp",        1,      WordType.verb      ],
    [ "chop",         1,      WordType.verb      ],
    [ "chump",        1,      WordType.noun      ],
    [ "chunk",        1,      WordType.noun      ],
    [ "churn",        1,      WordType.verb      ],
    [ "clamp",        1,      WordType.noun      ],
    [ "clobber",      2,      WordType.verb      ],
    [ "clump",        1,      WordType.noun      ],
    [ "cougar",       2,      WordType.animal    ],
    [ "crack",        1,      WordType.verb      ],
    [ "cracker",      2,      WordType.noun      ],
    [ "cram",         1,      WordType.verb      ],
    [ "cramp",        1,      WordType.noun      ],
    [ "crank",        1,      WordType.verb      ],
    [ "crash",        1,      WordType.verb      ],
    [ "crasher",      2,      WordType.noun      ],
    [ "crazy",        2,      WordType.adjective ],
    [ "cripple",      2,      WordType.verb      ],
    [ "crippler",     2,      WordType.noun      ],
    [ "crumble",      2,      WordType.verb      ],
    [ "crumple",      2,      WordType.verb      ],
    [ "crunch",       1,      WordType.verb      ],
    [ "cruncher",     2,      WordType.noun      ],
    [ "crush",        1,      WordType.verb      ],
    [ "crusher",      2,      WordType.noun      ],
    [ "cuda",         2,      WordType.modifier  ],
    [ "damage",       2,      WordType.noun      ],
    [ "danger",       2,      WordType.noun      ],
    [ "dead",         1,      WordType.adjective ],
    [ "dirt",         1,      WordType.noun      ],
    [ "dog",          1,      WordType.animal    ],
    [ "dozer",        2,      WordType.modifier  ],
    [ "dragon",       2,      WordType.animal    ],
    [ "dread",        1,      WordType.nounVerb  ],
    [ "driver",       2,      WordType.noun      ],
    [ "drop",         1,      WordType.verb      ],
    [ "eater",        2,      WordType.noun      ],
    [ "enheimer",     2,      WordType.modifier  ],
    [ "enstein",      2,      WordType.modifier  ],
    [ "erella",       3,      WordType.modifier  ],
    [ "erino",        3,      WordType.modifier  ],
    [ "face",         1,      WordType.bodyPart  ],
    [ "fall",         1,      WordType.verb      ],
    [ "fast",         1,      WordType.adjective ],
    [ "faster",       2,      WordType.adjective ],
    [ "feast",        1,      WordType.noun      ],
    [ "feet",         1,      WordType.bodyPart  ],
    [ "fierce",       1,      WordType.adjective ],
    [ "fight",        1,      WordType.verb      ],
    [ "fighter",      2,      WordType.noun      ],
    [ "fire",         2,      WordType.noun      ],
    [ "fist",         1,      WordType.bodyPart  ],
    [ "flank",        1,      WordType.noun      ],
    [ "flog",         1,      WordType.verb      ],
    [ "foot",         1,      WordType.bodyPart  ],
    [ "force",        1,      WordType.nounVerb  ],
    [ "fracture",     2,      WordType.nounVerb  ],
    [ "frag",         1,      WordType.verb      ],
    [ "fragger",      2,      WordType.noun      ],
    [ "fury",         2,      WordType.noun      ],
    [ "gator",        2,      WordType.animal    ],
    [ "goat",         1,      WordType.animal    ],
    [ "gouge",        1,      WordType.verb      ],
    [ "gouger",       2,      WordType.noun      ],
    [ "grab",         1,      WordType.verb      ],
    [ "grabber",      2,      WordType.noun      ],
    [ "granite",      2,      WordType.adjective ],
    [ "gravel",       2,      WordType.noun      ],
    [ "grease",       1,      WordType.noun      ],
    [ "grind",        1,      WordType.verb      ],
    [ "grinder",      2,      WordType.noun      ],
    [ "gristle",      2,      WordType.noun      ],
    [ "groin",        1,      WordType.bodyPart  ],
    [ "growl",        1,      WordType.verb      ],
    [ "grunt",        1,      WordType.verb      ],
    [ "gut",          1,      WordType.bodyPart  ],
    [ "guts",         1,      WordType.bodyPart  ],
    [ "hack",         1,      WordType.verb      ],
    [ "hair",         1,      WordType.bodyPart  ],
    [ "ham",          1,      WordType.meat      ],
    [ "hammer",       2,      WordType.nounVerb  ],
    [ "hard",         1,      WordType.adjective ],
    [ "harm",         1,      WordType.verb      ],
    [ "hatchet",      2,      WordType.noun      ],
    [ "hawk",         1,      WordType.animal    ],
    [ "head",         1,      WordType.bodyPart  ],
    [ "heap",         1,      WordType.noun      ],
    [ "heart",        1,      WordType.bodyPart  ],
    [ "heave",        1,      WordType.verb      ],
    [ "heavy",        1,      WordType.adjective ],
    [ "heel",         1,      WordType.bodyPart  ],
    [ "hinder",       2,      WordType.bodyPart  ],
    [ "hit",          1,      WordType.verb      ],
    [ "hog",          1,      WordType.animal    ],
    [ "horse",        1,      WordType.animal    ],
    [ "hound",        1,      WordType.animal    ],
    [ "house",        1,      WordType.noun      ],
    [ "huge",         1,      WordType.adjective ],
    [ "hulk",         1,      WordType.noun      ],
    [ "hunk",         1,      WordType.noun      ],
    [ "hunter",       2,      WordType.noun      ],
    [ "hurl",         1,      WordType.verb      ],
    [ "hurler",       2,      WordType.noun      ],
    [ "hurt",         1,      WordType.verb      ],
    [ "ilicious",     3,      WordType.modifier  ],
    [ "inator",       3,      WordType.modifier  ],
    [ "ington",       2,      WordType.modifier  ],
    [ "iron",         2,      WordType.adjective ],
    [ "jab",          1,      WordType.verb      ],
    [ "jam",          1,      WordType.verb      ],
    [ "jammer",       2,      WordType.noun      ],
    [ "jaw",          1,      WordType.bodyPart  ],
    [ "jet",          1,      WordType.noun      ],
    [ "jowls",        1,      WordType.bodyPart  ],
    [ "jump",         1,      WordType.verb      ],
    [ "kapow",        2,      WordType.noun      ],
    [ "kick",         1,      WordType.verb      ],
    [ "kicker",       2,      WordType.noun      ],
    [ "kill",         1,      WordType.verb      ],
    [ "knuckle",      2,      WordType.bodyPart  ],
    [ "knuckles",     2,      WordType.bodyPart  ],
    [ "large",        1,      WordType.adjective ],
    [ "leather",      2,      WordType.noun      ],
    [ "legs",         1,      WordType.bodyPart  ],
    [ "leopard",      2,      WordType.animal    ],
    [ "ley",          1,      WordType.modifier  ],
    [ "licious",      2,      WordType.modifier  ],
    [ "lightning",    2,      WordType.noun      ],
    [ "lion",         2,      WordType.animal    ],
    [ "lip",          1,      WordType.bodyPart  ],
    [ "lips",         1,      WordType.bodyPart  ],
    [ "load",         1,      WordType.noun      ],
    [ "log",          1,      WordType.noun      ],
    [ "lots",         1,      WordType.modifier  ],
    [ "loud",         1,      WordType.adjective ],
    [ "lumber",       2,      WordType.noun      ],
    [ "lump",         1,      WordType.noun      ],
    [ "ly",           1,      WordType.modifier  ],
    [ "maker",        1,      WordType.noun      ],
    [ "mallet",       2,      WordType.noun      ],
    [ "man",          1,      WordType.noun      ],
    [ "mangle",       1,      WordType.verb      ],
    [ "mangler",      2,      WordType.noun      ],
    [ "mash",         1,      WordType.verb      ],
    [ "masher",       2,      WordType.noun      ],
    [ "master",       2,      WordType.noun      ],
    [ "meal",         1,      WordType.noun      ],
    [ "meat",         1,      WordType.meat      ],
    [ "meister",      2,      WordType.noun      ],
    [ "metal",        2,      WordType.noun      ],
    [ "monger",       2,      WordType.noun      ],
    [ "monster",      2,      WordType.animal    ],
    [ "moose",        1,      WordType.animal    ],
    [ "mountain",     2,      WordType.noun      ],
    [ "mouth",        1,      WordType.bodyPart  ],
    [ "mower",        1,      WordType.modifier  ],
    [ "mud",          1,      WordType.noun      ],
    [ "mule",         1,      WordType.animal    ],
    [ "munch",        1,      WordType.verb      ],
    [ "muncher",      2,      WordType.noun      ],
    [ "muscle",       2,      WordType.bodyPart  ],
    [ "naut",         1,      WordType.modifier  ],
    [ "neck",         1,      WordType.bodyPart  ],
    [ "normous",      2,      WordType.modifier  ],
    [ "nuke",         1,      WordType.verb      ],
    [ "nuker",        2,      WordType.noun      ],
    [ "oceros",       3,      WordType.modifier  ],
    [ "ogre",         2,      WordType.noun      ],
    [ "omatic",       3,      WordType.modifier  ],
    [ "orama",        3,      WordType.modifier  ],
    [ "pain",         1,      WordType.noun      ],
    [ "pants",        1,      WordType.noun      ],
    [ "pecs",         1,      WordType.bodyPart  ],
    [ "pile",         1,      WordType.noun      ],
    [ "plank",        1,      WordType.noun      ],
    [ "pork",         1,      WordType.meat      ],
    [ "pound",        1,      WordType.verb      ],
    [ "pounder",      2,      WordType.noun      ],
    [ "power",        2,      WordType.noun      ],
    [ "pummel",       2,      WordType.verb      ],
    [ "punch",        1,      WordType.verb      ],
    [ "puncher",      2,      WordType.noun      ],
    [ "puncture",     2,      WordType.nounVerb  ],
    [ "punk",         1,      WordType.noun      ],
    [ "punt",         1,      WordType.verb      ],
    [ "punter",       2,      WordType.noun      ],
    [ "quake",        1,      WordType.modifier  ],
    [ "rage",         1,      WordType.noun      ],
    [ "ram",          1,      WordType.verb      ],
    [ "ribs",         1,      WordType.bodyPart  ],
    [ "rilla",        1,      WordType.animal    ],
    [ "riot",         2,      WordType.noun      ],
    [ "rip",          1,      WordType.verb      ],
    [ "rivet",        2,      WordType.nounVerb  ],
    [ "roar",         1,      WordType.verb      ],
    [ "roast",        1,      WordType.nounVerb  ],
    [ "rock",         1,      WordType.noun      ],
    [ "rocket",       2,      WordType.noun      ],
    [ "roid",         1,      WordType.modifier  ],
    [ "rumble",       2,      WordType.nounVerb  ],
    [ "rump",         1,      WordType.bodyPart  ],
    [ "scar",         1,      WordType.adjective ],
    [ "scorch" ,      1,      WordType.verb      ],
    [ "shank",        1,      WordType.nounVerb  ],
    [ "shooter",      2,      WordType.noun      ],
    [ "shoulder",     2,      WordType.bodyPart  ],
    [ "shout",        1,      WordType.verb      ],
    [ "shovel",       2,      WordType.nounVerb  ],
    [ "shrapnel",     2,      WordType.noun      ],
    [ "shredder",     2,      WordType.noun      ],
    [ "skjold",       1,      WordType.noun      ],  # Danish for shield
    [ "skull",        1,      WordType.bodyPart  ],
    [ "slab",         1,      WordType.verb      ],
    [ "slag",         1,      WordType.verb      ],
    [ "slam",         1,      WordType.verb      ],
    [ "slammer",      2,      WordType.noun      ],
    [ "slap",         1,      WordType.verb      ],
    [ "slapper",      2,      WordType.noun      ],
    [ "slugger",      2,      WordType.noun      ],
    [ "smash",        1,      WordType.verb      ],
    [ "smasher",      2,      WordType.noun      ],
    [ "smith",        2,      WordType.noun      ],
    [ "snag",         1,      WordType.verb      ],
    [ "snake",        1,      WordType.animal    ],
    [ "snap",         1,      WordType.verb      ],
    [ "snapper",      2,      WordType.noun      ],
    [ "snarl",        1,      WordType.verb      ],
    [ "socket",       2,      WordType.bodyPart  ],
    [ "spank",        1,      WordType.verb      ],
    [ "spanker",      2,      WordType.noun      ],
    [ "speed",        1,      WordType.noun      ],
    [ "spit",         1,      WordType.verb      ],
    [ "spittle",      2,      WordType.noun      ],
    [ "splinter",     2,      WordType.verb      ],
    [ "split",        1,      WordType.verb      ],
    [ "splode",       1,      WordType.nounVerb  ],
    [ "splosion",     2,      WordType.modifier  ],
    [ "sprain",       1,      WordType.verb      ],
    [ "squash",       1,      WordType.verb      ],
    [ "squasher",     2,      WordType.adjective ],
    [ "stack",        1,      WordType.noun      ],
    [ "stag",         1,      WordType.animal    ],
    [ "steak",        1,      WordType.meat      ],
    [ "steel",        1,      WordType.adjective ],
    [ "stein",        1,      WordType.modifier  ],
    [ "stick",        1,      WordType.noun      ],
    [ "stomp",        1,      WordType.verb      ],
    [ "stone",        1,      WordType.adjective ],
    [ "storm",        1,      WordType.noun      ],
    [ "strangle",     2,      WordType.verb      ],
    [ "strike",       1,      WordType.verb      ],
    [ "striker",      1,      WordType.noun      ],
    [ "strong",       1,      WordType.adjective ],
    [ "stud",         1,      WordType.noun      ],
    [ "stump",        1,      WordType.noun      ],
    [ "sweat",        1,      WordType.nounVerb  ],
    [ "swift",        1,      WordType.adjective ],
    [ "sword",        1,      WordType.noun      ],
    [ "tackle",       2,      WordType.verb      ],
    [ "tacular",      3,      WordType.modifier  ],
    [ "tank",         1,      WordType.noun      ],
    [ "tastic",       2,      WordType.modifier  ],
    [ "teeth",        1,      WordType.bodyPart  ],
    [ "thick",        1,      WordType.adjective ],
    [ "thrash",       1,      WordType.verb      ],
    [ "throat",       1,      WordType.bodyPart  ],
    [ "thrust",       1,      WordType.verb      ],
    [ "thud",         1,      WordType.noun      ],
    [ "thump",        1,      WordType.verb      ],
    [ "thumper",      2,      WordType.noun      ],
    [ "thunder",      2,      WordType.noun      ],
    [ "tiger",        2,      WordType.animal    ],
    [ "toad",         1,      WordType.animal    ],
    [ "tooth",        1,      WordType.bodyPart  ],
    [ "torch",        1,      WordType.noun      ],
    [ "torn",         1,      WordType.adjective ],
    [ "tough",        1,      WordType.adjective ],
    [ "tower",        2,      WordType.noun      ],
    [ "trample",      2,      WordType.verb      ],
    [ "truck",        1,      WordType.noun      ],
    [ "twister",      2,      WordType.noun      ],
    [ "viper",        2,      WordType.animal    ],
    [ "volt",         1,      WordType.noun      ],
    [ "vulture",      2,      WordType.animal    ],
    [ "wall",         1,      WordType.noun      ],
    [ "wallop",       2,      WordType.verb      ],
    [ "war",          1,      WordType.noun      ],
    [ "welt",         1,      WordType.noun      ],
    [ "whip",         1,      WordType.nounVerb  ],
    [ "wolf",         1,      WordType.animal    ],
    [ "wood",         1,      WordType.noun      ],
    [ "wound",        1,      WordType.noun      ],
    [ "wrangler",     2,      WordType.noun      ],
    [ "wrath",        1,      WordType.noun      ],
    [ "wreck",        1,      WordType.verb      ],
    [ "wrecker",      2,      WordType.noun      ],
    [ "wrench",       1,      WordType.nounVerb  ],
    [ "wrestle",      2,      WordType.verb      ],
    [ "wrestler",     2,      WordType.noun      ],
    [ "yak",          1,      WordType.animal    ],
    [ "yank",         1,      WordType.verb      ],
    [ "yanker",       1,      WordType.noun      ],
    [ "zilla",        2,      WordType.modifier  ],
]


specialList = [
    "Ace Rimmer",
    "Adam Chance",
    "Aram Fingle",
    "Beef Wellington",
    "Bill Corbett",
    "Bob Johnson",
    "Carlo Lombardi",
    "Charles B. Pierce",
    "Charles Poindexter",
    "Chuck Norris"
    "Craig Breedlove",
    "Crow T. Robot",
    "D. P. Gumby",
    "Forrest Tucker",
    "Francine Gutleber",
    "Frank Conniff",
    "Htom Sirveaux",
    "Hugh Beaumont",
    "Ian Gutleber",
    "J. Elvis Weinstein",
    "Jean-Claude Gosh Darn",
    "Jennifer Gutleber",
    "Jeremy Gutleber",
    "Jet Jaguar",
    "Joel Hodgson",
    "John Agar",
    "Jonas Grumby",
    "Kevin Murphy",
    "Lloyd Bridges",
    "Lyle Waggoner",
    "Mary Jo Pehl",
    "Michael J. Nelson",
    "Rick Gutleber",
    "Simon Gutleber",
    "Sledge Hammer"
    "Tom Servo",
    "Tommy Kirk",
    "Torgo",
    "Trace Beaulieu",
    "Twinkle McFuzzykittens",
    "William Shatner",
    "Zapp Rowsdower",
]


firstNameListSize = len( firstNameList )
lastNameOneListSize = len( lastNameOneList )
lastNameTwoListSize = len( lastNameTwoList )
specialSize = len( specialList )

firstNameUsedIndices = list( )
lastNameOneUsedIndices = list( )
lastNameTwoUsedIndices = list( )


#//**********************************************************************
#//
#//  getFirstName
#//
#//**********************************************************************

def getFirstName( ):
    global firstNameUsedIndices

    while True:
        index = random.randint( 0, firstNameListSize - 1 )

        if index not in firstNameUsedIndices:
            break

    firstNameUsedIndices.append( index )

    if len( firstNameUsedIndices ) > nonRepeatThreshold:
        firstNameUsedIndices = firstNameUsedIndices[ 1 : ]

    return firstNameList[ index ]


#//**********************************************************************
#//
#//  getLastNameOne
#//
#//**********************************************************************

def getLastNameOne( ):
    global lastNameOneUsedIndices

    while True:
        index = random.randint( 0, lastNameOneListSize - 1 )

        if index not in lastNameOneUsedIndices:
            break

    lastNameOneUsedIndices.append( index )

    if len( lastNameOneUsedIndices ) > nonRepeatThreshold:
        lastNameOneUsedIndices = lastNameOneUsedIndices[ 1 : ]

    return lastNameOneList[ index ]


#//**********************************************************************
#//
#//  getLastNameTwo
#//
#//**********************************************************************

def getLastNameTwo( ):
    global lastNameTwoUsedIndices

    while True:
        index = random.randint( 0, lastNameTwoListSize - 1 )

        if index not in lastNameTwoUsedIndices:
            break

    lastNameTwoUsedIndices.append( index )

    if len( lastNameTwoUsedIndices ) > nonRepeatThreshold:
        lastNameTwoUsedIndices = lastNameTwoUsedIndices[ 1 : ]

    return lastNameTwoList[ index ]


#//**********************************************************************
#//
#//  getSpecial
#//
#//**********************************************************************

def getSpecial( ):
    return specialList[ random.randint( 0, specialSize - 1 ) ]


#//**********************************************************************
#//
#//  buildName
#//
#//**********************************************************************

def buildName( ):
    if ( random.randint( 1, 500 ) == 1 ):
        return getSpecial( )

    firstName = getFirstName( )

    lastNameOne = getLastNameOne( )
    lastNameTwo = getLastNameTwo( )

    # lastNameOne[ 0 ] in [ "Back", "Side" ] ) and ( lastNameTwo[ 2 ] in [ noun, bodyPart, animal, adjective, modifier ] ) ) or \

    while ( ( "ump" in lastNameOne[ 0 ] ) and ( "ump" in lastNameTwo[ 0 ] ) ) or \
          ( ( lastNameOne[ 0 ] == "Broke" ) and ( lastNameTwo[ 0 ] == "Back" ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Cracked", "Split", "Crushed", "Broke", "Broken", "Bent", "Heave" ] ) and ( lastNameTwo[ 2 ] in [ WordType.verb, WordType.adjective ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Cracked", "Crushed" ] ) and ( lastNameTwo[ 0 ][ 0 ] in [ "bcdgjkpst" ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Meaty", "Elbow" ] ) and ( lastNameTwo[ 2 ] in [ WordType.adjective ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Square" ] ) and ( lastNameTwo[ 2 ] not in [ WordType.noun, WordType.meat, WordType.bodyPart, WordType.animal ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Wall" ] ) and ( lastNameTwo[ 2 ] not in [ WordType.nounVerb, WordType.verb ] ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "a" ) and ( lastNameTwo[ 0 ][ 0 ] == "a" ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "a" ) and ( lastNameTwo[ 0 ][ 0 ] == "o" ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "e" ) and ( lastNameTwo[ 0 ] in [ "eater", "splode" ] ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "l" ) and ( lastNameTwo[ 0 ] in ( "alo" ) ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "y" ) and ( lastNameTwo[ 0 ] == "ley" ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] == "y" ) and ( lastNameTwo[ 0 ] == "ly" ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] in "aeiouy" ) and ( lastNameTwo[ 0 ] in ( "alo", "ington" ) ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] in "aiouy" ) and ( lastNameTwo[ 0 ] in [ "alot", "amundo", "inator", "omatic", "orama" ] ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] not in "aeiouy" ) and ( lastNameOne[ 0 ][ -2 : ] not in [ "ar", "er", "ir", "or", "ur" ] ) and ( lastNameTwo[ 0 ] in [ "naut" ] ) ) or \
          ( ( lastNameOne[ 0 ][ -1 ] not in vowels ) and ( lastNameOne[ 0 ][ -2 : ] not in [ "an", "en", "in", "on", "un" ] ) and ( lastNameOne[ 0 ][ -2 : ] not in [ "ar", "er", "ir", "or", "ur" ] ) and ( lastNameTwo[ 0 ] == "cuda" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ch" ) and ( lastNameTwo[ 0 ][ 0 : 2 ] == "ch" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ee" ) and ( lastNameTwo[ 0 ] in [ "alot", "enstein", "enheimer", "erella", "erino", "inator", "omatic", "orama" ] ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "er" ) and ( lastNameTwo[ 0 ] in ( "alo" ) ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ff" ) and ( lastNameTwo[ 0 ][ 0 ] == "f" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ll" ) and ( lastNameTwo[ 0 ] == "ley" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ll" ) and ( lastNameTwo[ 0 ] == "ly" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ll" ) and ( lastNameTwo[ 0 ][ 0 ] == "l" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "sh" ) and ( lastNameTwo[ 0 ][ : 2 ] == "sl" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "ss" ) and ( lastNameTwo[ 0 ][ 0 ] == "s" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "st" ) and ( lastNameTwo[ 0 ][ 0 ] == "s" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "st" ) and ( lastNameTwo[ 0 ][ 0 ] == "s" ) ) or \
          ( ( lastNameOne[ 0 ][ -2 : ] == "th" ) and ( lastNameTwo[ 0 ][ : 2 ] == "th" ) ) or \
          ( ( lastNameOne[ 0 ][ -3 : ] == "ash" ) and ( lastNameTwo[ 0 ][ -3 : ] == "ash" ) ) or \
          ( ( lastNameOne[ 0 ][ -3 : ] == "ple" ) and ( lastNameTwo[ 0 ][ -3 : ] == "ple" ) ) or \
          ( ( lastNameOne[ 0 ][ -3 : ] == "ump" ) and ( lastNameTwo[ 0 ][ -3 : ] == "ump" ) ) or \
          ( ( lastNameOne[ 0 ][ -3 : ] == "unk" ) and ( lastNameTwo[ 0 ][ -3 : ] == "unk" ) ) or \
          ( ( lastNameOne[ 0 ][ -4 : ] == "mble" ) and ( lastNameTwo[ 0 ][ -4 : ] == "mple" ) ) or \
          ( ( lastNameOne[ 0 ][ -4 : ] == "mple" ) and ( lastNameTwo[ 0 ][ -4 : ] == "mble" ) ) or \
          ( ( lastNameOne[ 1 ] > 1 ) and ( lastNameTwo[ 0 ] in [ "alo", "alot", "arillo", "enstein", "enheimer", "ilicious", "inator", "ington", "tacular", "tastic" ] ) ) or \
          ( ( lastNameOne[ 1 ] < 2 ) and ( lastNameTwo[ 0 ] in [ "licious", "naut" ] ) ) or \
          ( ( lastNameOne[ 2 ] in [ WordType.bodyPart ]  ) and ( lastNameTwo[ 0 ] in [ "feast" ] ) ) or \
          ( ( lastNameOne[ 2 ] in [ WordType.adjective ] ) and ( lastNameOne[ 1 ] > 1 ) and ( lastNameTwo[ 0 ] in [ "normous" ] ) ) or \
          ( ( lastNameOne[ 2 ] in [ WordType.verb, WordType.adjective ] ) and ( lastNameTwo[ 0 ] in [ "heave", "torn" ] ) ) or \
          ( ( lastNameOne[ 2 ] not in [ WordType.bodyPart ]  ) and ( lastNameTwo[ 0 ] in [ "damage" ] ) ) or \
          ( firstName.lower( ) == lastNameOne[ 0 ] ) or \
          ( firstName.lower( ) == lastNameTwo[ 0 ] ) or \
          ( lastNameOne[ 0 ].lower( ) == lastNameTwo[ 0 ] ) or \
          ( lastNameOne[ 0 ][ -3 : ] == lastNameTwo[ 0 ][ -3 : ] ) or \
          ( lastNameOne[ 0 ][ : 4 ].lower( ) == lastNameTwo[ 0 ][ : 4 ] ) or \
          ( ( lastNameOne[ 2 ] not in [ WordType.verb, WordType.nounVerb  ] ) and  ( lastNameTwo[ 0 ] == "lots" ) ):
        # print( firstName + " " + lastNameOne[ 0 ] + " " + lastNameTwo[ 0 ] )
        lastNameTwo = getLastNameTwo( )

    # now we might need to modify the strings, so let's copy them
    lastNameFirstHalf = lastNameOne[ 0 ]
    lastNameLastHalf = lastNameTwo[ 0 ]

    # when consonant-vowel-consonant gets an 'e' or 'i' appended, double the final consonant
    if ( lastNameFirstHalf[ -1 ] in consonants ) and ( lastNameFirstHalf[ -2 ] in vowels ) and \
       ( lastNameFirstHalf[ -3 ] in consonants ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ):
        lastNameFirstHalf += lastNameFirstHalf[ -1 ]

    # when adding a 'y' to a trailing 'y', eat the trailing 'y' first
    if ( lastNameFirstHalf[ -1 ] == "y" ) and ( lastNameLastHalf[ 0 ] == "y" ):
        lastNameFirstHalf = lastNameFirstHalf[ : -1 ]

    # when adding an 'e' or an 'i' to a trailing 'e', eat the trailing 'e' first
    if ( lastNameFirstHalf[ -1 ] == "e" ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ):
        lastNameFirstHalf = lastNameFirstHalf[ : -1 ]

    # double consonants with adding 'e' or 'i' makes a vowel-consonant-vowel combination
    if ( len( lastNameFirstHalf ) > 2 ) and ( lastNameFirstHalf[ -3 ] in vowels ) and ( lastNameFirstHalf[ -2 ] in consonants ) and \
       ( lastNameFirstHalf[ -1 ] in vowels ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ):
        lastNameFirstHalf.Insert( -2, lastNameFirstHalf[ -2 ] )

    if ( lastNameFirstHalf[ -2 : ] == "le" ) and ( lastNameLastHalf in [ "ly", "ley" ] ):
        lastNameLastHalf = "y"

    middle = " "

    # if the first part is not a modifier then consider adding a middle name (which is basically just another modifier)
    if lastNameOne[ 2 ] == WordType.modifier:
        while True:
            lastNameTwo = getLastNameOne( )

            if lastNameTwo[ 2 ] == WordType.modifier:
                break

            lastNameLastHalf = lastNameTwo[ 0 ]
    else:
        done = False

        # a few validation rules for modifiers (e.g., McGorilla just doesn't work for me)
        while ( not done ):
            if ( random.randint( 1, 100 ) == 1 ):
                middle = random.choice( [ " Mc", " von ", " van der ", " del ", " La ", " de la " ] )

                if ( middle == " Mc" ) and ( lastNameFirstHalf in [ "Gorilla" ] ) and \
                   ( lastNameTwo[ 0 ] not in [ "enstein", "enheimer" ] ):
                    done = True

                if ( middle in [ " del ", " de la " ] ) and ( lastNameTwo[ 0 ] not in [ "enstein", "enheimer" ] ):
                    done = True

                if middle in [ " von ", " van der ", " La " ]:
                    done = True
            elif ( firstName in [ "Baron", "Count" ] ) and ( random.randint( 1, 12 ) ):
                middle = " von "
                done = True
            else:
                done = True

    return firstName + middle + lastNameFirstHalf + lastNameLastHalf


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    import argparse

    parser = argparse.ArgumentParser( prog=PROGRAM_NAME, description=DESCRIPTION )

    parser.add_argument( '-n', '--count', type=int, action='store', default=1 )
    parser.add_argument( '-s', '--stats', action='store_true' )

    args = parser.parse_args( )

    count = args.count

    for i in range( 0, count ):
        print( buildName( ) )

    if args.stats:
        print( )
        print( "first names:    " + format( firstNameListSize ) )
        print( "last names one: " + format( lastNameOneListSize ) )
        print( "last names two: " + format( lastNameTwoListSize ) )


#//**********************************************************************
#//
#//  siteHeader
#//
#//**********************************************************************

def siteHeader( title ):
    string = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><title>
""" + "\n" + title + "\n</title></head><body>\n"
    return string


#//**********************************************************************
#//
#//  siteBody
#//
#//**********************************************************************

def siteBody( title ):
    string = "<h2>" + title + "</h2>" + '\n'
    string += COPYRIGHT_MESSAGE + '<br><br>\n'
    string += "Inspired by Mystery Science Theater 3000, episode #820, 'Space Mutiny'<br>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += "<h2>" + buildName( ) + "</h2>" + '\n'
    string += """Hit 'Refresh' for more names.  Props to Reb Brown!<br>
Thanks for many additional suggestions from Ian, Francine and Jeremy.<br>
Now with over <i>one hundred million</i> possible combinations and support for semantic rules so there are fewer lame names!<br><br>
Send suggestions, complaints or meandering stories about your goiter to <a href="mailto:rickg@his.com?subject=BigMcLargeHuge">rickg@his.com</a><br>
<a href="https://github.com/ConceptJunkie/BigMcLargeHuge">Source Code</a><br><br><br>
""" + '\n'
    string += "Stats:<ul>" + '\n'
    string += "<li>First Names: " + str( firstNameListSize ) + "</li>" + '\n'
    string += "<li>Last Names (first half): " + str( lastNameOneListSize ) + "</li>" + '\n'
    string += "<li>Last Names (second half): " + str( lastNameTwoListSize ) + "</li>" + '\n'
    string += "<li>plus name modifiers and other <a href=\"https://github.com/ConceptJunkie/BigMcLargeHuge\">secret sauce</a></li></ul>" + '\n'

    return string


#//**********************************************************************
#//
#//  siteFooter
#//
#//**********************************************************************

def siteFooter( ):
    return "\n</body></html>"


#//**********************************************************************
#//
#//  buildWebPage
#//
#//**********************************************************************

def buildWebPage( ):
    pageTitle = DESCRIPTION

    webPage = siteHeader( pageTitle )
    webPage += siteBody( pageTitle )
    webPage += siteFooter( )
    return webPage


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    main( )
else:
    print( buildWebPage( ) )

# The original list from MST3K

#    Slab Bulkhead
#  Fridge Largemeat
#    Punt Speedchunk
#   Butch Deadlift
#    Bold Bigflank
#  Splint Chesthair
#   Flint Ironstag
#    Bolt Vanderhuge
#   Thick McRunfast
#   Blast Hardcheese
#    Buff Drinklots
#   Trunk Slamchest
#    Fist Rockbone
#   Stump Beefgnaw
#   Smash Lampjaw
#   Punch Rockgroin
#    Buck Plankchest
#   Stump Chunkman
#    Dirk Hardpeck
#     Rip Steakface
#   Slate Slabrock
#    Crud Bonemeal
#   Brick Hardmeat
#     Rip Sidecheek
#   Punch Sideiron
# Gristle McThornBody
#   Slake Fistcrunch
#    Buff Hardback
#     Bob Johnson
#   Blast Thickneck
#  Crunch Buttsteak
#    Slab Squatthrust
#    Lump Beefrock
#   Touch Rustrod
#    Reef Blastbody
#     Big McLargeHuge
#   Smoke Manmuscle
#    Beat Punchbeef
#    Pack Blowfist
#    Roll Fizzlebeef

