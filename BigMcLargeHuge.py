#!/usr/bin/env python

from __future__ import print_function

import random
import string
import sys

# enable debugging
import cgitb
cgitb.enable( )


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
VERSION = "1.3.7"
PROGRAM_DESCRIPTION = "an action movie hero name generator"
COPYRIGHT_MESSAGE = "copyright (c) 2014,2018 Rick and Simon Gutleber (rickg@his.com, simon@zycha.com)"

DESCRIPTION = PROGRAM_NAME + " " + VERSION + ", " + PROGRAM_DESCRIPTION + ", " + COPYRIGHT_MESSAGE

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeoiuy"

nonRepeatThreshold = 20

# word types

noun      = 0
bodyPart  = 1     # specific type of noun
animal    = 2     # specific type of noun
meat      = 3     # specific type of noun
adjective = 4
verb      = 5
nounVerb  = 6     # noun and verb
modifier  = 7

# word lists

firstNameList = [
    "Abraham",
    "Ace",
    "Agamemnon",
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
    "Bob",
    "Bold",
    "Bolt",
    "Bomb",
    "Bone",
    "Boom",
    "Boot",
    "Boris",
    "Bort",
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
    "Cain",
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
    "George",
    "Gil",
    "Glock",
    "Gooch",
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
    "Guido",
    "Gulp",
    "Gun",
    "Gunner",
    "Gunther",
    "Gus",
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
    "Jed",
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
    "Leo",
    "Leon",
    "Leonardo",
    "Lex",
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
    "Maximus",
    "Maxwell",
    "Mel",
    "Meteor",
    "Mick",
    "Moe",
    "Moose",
    "Moses",
    "Mud",
    "Mug",
    "Napoleon",
    "Narc",
    "Nasty",
    "Nate",
    "Ned",
    "Nick",
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
    "Spunk",
    "Squint",
    "Stag",
    "Stan",
    "Stanley",
    "Steel",
    "Steve",
    "Stick",
    "Stomp",
    "Stone",
    "Strike",
    "Strong",
    "Stubby",
    "Stud",
    "Studly",
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
    "Volt",
    "Wallop",
    "Wally",
    "Walt",
    "Wayne",
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
    [ "Able",         2,      adjective ],
    [ "Angry",        2,      adjective ],
    [ "Ankle",        2,      bodyPart  ],
    [ "Anvil",        2,      noun      ],
    [ "Ape",          1,      animal    ],
    [ "Assault",      2,      verb      ],
    [ "Attack",       2,      verb      ],
    [ "Awful",        2,      adjective ],
    [ "Ax",           1,      noun      ],
    [ "Back",         1,      bodyPart  ],
    [ "Bacon",        2,      meat      ],
    [ "Bad",          1,      adjective ],
    [ "Badger",       2,      animal    ],
    [ "Bang",         1,      noun      ],
    [ "Barge",        1,      verb      ],
    [ "Barrage",      2,      noun      ],
    [ "Bash",         1,      verb      ],
    [ "Batch",        1,      noun      ],
    [ "Batter",       2,      verb      ],
    [ "Battle",       2,      nounVerb  ],
    [ "Bear",         1,      animal    ],
    [ "Beast",        1,      noun      ],
    [ "Beat",         1,      verb      ],
    [ "Beef",         1,      meat      ],
    [ "Bend",         1,      verb      ],
    [ "Bent",         1,      adjective ],
    [ "Berserk",      2,      adjective ],
    [ "Big",          1,      adjective ],
    [ "Bigger",       1,      adjective ],
    [ "Bison",        2,      animal    ],
    [ "Bite",         1,      verb      ],
    [ "Black",        1,      adjective ],
    [ "Blade",        1,      noun      ],
    [ "Blast",        1,      nounVerb  ],
    [ "Block",        1,      nounVerb  ],
    [ "Body",         2,      bodyPart  ],
    [ "Bold",         1,      adjective ],
    [ "Bolt",         1,      noun      ],
    [ "Bomb",         1,      noun      ],
    [ "Bone",         1,      bodyPart  ],
    [ "Boot",         1,      nounVerb  ],
    [ "Boulder",      2,      noun      ],
    [ "Box",          1,      noun      ],
    [ "Brave",        1,      adjective ],
    [ "Brawl",        1,      verb      ],
    [ "Break",        1,      verb      ],
    [ "Brick",        1,      noun      ],
    [ "Broke",        1,      adjective ],
    [ "Broken",       2,      adjective ],
    [ "Bruise",       1,      nounVerb  ],
    [ "Brutal",       2,      adjective ],
    [ "Brute",        1,      noun      ],
    [ "Buff",         1,      adjective ],
    [ "Bulge",        1,      bodyPart  ],
    [ "Bulk",         1,      adjective ],
    [ "Bull",         1,      animal    ],
    [ "Bullet",       2,      noun      ],
    [ "Burn",         1,      verb      ],
    [ "Burnt",        1,      adjective ],
    [ "Burst",        1,      verb      ],
    [ "Bust",         1,      verb      ],
    [ "Buster",       2,      noun      ],
    [ "Butt",         1,      bodyPart  ],
    [ "Cannon",       2,      noun      ],
    [ "Castle",       2,      noun      ],
    [ "Char",         1,      verb      ],
    [ "Chest",        1,      bodyPart  ],
    [ "Chew",         1,      verb      ],
    [ "Chin",         1,      bodyPart  ],
    [ "Chisel",       2,      nounVerb  ],
    [ "Choke",        1,      verb      ],
    [ "Chomp",        1,      verb      ],
    [ "Chop",         1,      verb      ],
    [ "Chunk",        1,      noun      ],
    [ "Clamp",        1,      verb      ],
    [ "Clobber",      3,      verb      ],
    [ "Conquer",      2,      verb      ],
    [ "Cougar",       2,      animal    ],
    [ "Crack",        1,      nounVerb  ],
    [ "Cracked",      1,      adjective ],
    [ "Cram",         1,      verb      ],
    [ "Crank",        1,      verb      ],
    [ "Crazy",        2,      adjective ],
    [ "Cripple",      2,      verb      ],
    [ "Crooked",      2,      adjective ],
    [ "Crumble",      2,      verb      ],
    [ "Crumple",      2,      verb      ],
    [ "Crunch",       1,      verb      ],
    [ "Crush",        1,      verb      ],
    [ "Crushed",      1,      adjective ],
    [ "Danger",       2,      noun      ],
    [ "Dark",         1,      adjective ],
    [ "de la ",       2,      modifier  ],
    [ "Dead",         1,      adjective ],
    [ "Dirt",         1,      noun      ],
    [ "Dog",          1,      animal    ],
    [ "Double",       2,      adjective ],
    [ "Drag",         1,      verb      ],
    [ "Dragon",       2,      animal    ],
    [ "Dread",        1,      verb      ],
    [ "Drop",         1,      verb      ],
    [ "Eat",          1,      verb      ],
    [ "Elbow",        2,      bodyPart  ],
    [ "Fear",         1,      noun      ],
    [ "Fight",        1,      nounVerb  ],
    [ "Fire",         2,      noun      ],
    [ "Fist",         1,      bodyPart  ],
    [ "Fizzle",       2,      verb      ],
    [ "Flame",        1,      noun      ],
    [ "Flank",        1,      noun      ],
    [ "Flat",         1,      adjective ],
    [ "Flog",         1,      verb      ],
    [ "Foot",         1,      bodyPart  ],
    [ "Frag",         1,      verb      ],
    [ "Franken",      2,      adjective ],   # we don't want it to work like the other modifiers
    [ "Fury",         2,      noun      ],
    [ "Gator",        2,      animal    ],
    [ "Giant",        2,      adjective ],
    [ "Goat",         1,      animal    ],
    [ "Gorilla",      3,      animal    ],
    [ "Gouge",        1,      nounVerb  ],
    [ "Grab",         1,      verb      ],
    [ "Granite",      2,      adjective ],
    [ "Gravel",       2,      adjective ],
    [ "Grease",       1,      noun      ],
    [ "Grim",         1,      adjective ],
    [ "Grime",        1,      noun      ],
    [ "Grind",        1,      verb      ],
    [ "Gristle",      2,      noun      ],
    [ "Grit",         1,      noun      ],
    [ "Grizzly",      2,      animal    ],
    [ "Ground",       1,      verb      ],
    [ "Growl",        1,      verb      ],
    [ "Grunt",        1,      nounVerb  ],
    [ "Gut",          1,      bodyPart  ],
    [ "Hack",         1,      verb      ],
    [ "Ham",          1,      meat      ],
    [ "Hammer",       2,      noun      ],
    [ "Hard",         1,      adjective ],
    [ "Harm",         1,      verb      ],
    [ "Hatchet",      2,      noun      ],
    [ "Hawk",         1,      animal    ],
    [ "Head",         1,      bodyPart  ],
    [ "Heart",        1,      bodyPart  ],
    [ "Heave",        1,      verb      ],
    [ "Heavy",        2,      adjective ],
    [ "Heel",         1,      bodyPart  ],
    [ "Hinder",       2,      bodyPart  ],
    [ "Hit",          1,      verb      ],
    [ "Hog",          1,      animal    ],
    [ "Horse",        1,      animal    ],
    [ "Hound",        1,      animal    ],
    [ "Huge",         1,      adjective ],
    [ "Hulk",         1,      noun      ],
    [ "Hunk",         1,      noun      ],
    [ "Hunt",         1,      verb      ],
    [ "Hurl",         1,      verb      ],
    [ "Hurt",         1,      verb      ],
    [ "Husky",        2,      adjective ],
    [ "Iron",         2,      adjective ],
    [ "Jab",          1,      verb      ],
    [ "Jagged",       2,      adjective ],
    [ "Jam",          1,      verb      ],
    [ "Jaw",          1,      bodyPart  ],
    [ "Jet",          1,      noun      ],
    [ "Jump",         1,      verb      ],
    [ "Kick",         1,      verb      ],
    [ "Kicking",      1,      adjective ],
    [ "Kill",         1,      verb      ],
    [ "Knee",         1,      bodyPart  ],
    [ "Knuckle",      2,      bodyPart  ],
    [ "Large",        1,      adjective ],
    [ "Lava",         2,      noun      ],
    [ "Leather",      2,      noun      ],
    [ "Leopard",      2,      animal    ],
    [ "Lion",         2,      animal    ],
    [ "Log",          1,      noun      ],
    [ "Loud",         1,      adjective ],
    [ "Lug",          1,      verb      ],
    [ "Lumber",       2,      nounVerb  ],
    [ "Mad",          1,      adjective ],
    [ "Mallet",       2,      noun      ],
    [ "Man",          1,      bodyPart  ],
    [ "Mangle",       2,      verb      ],
    [ "Mash",         1,      verb      ],
    [ "Master",       1,      noun      ],
    [ "Maul",         1,      verb      ],
    [ "Mean",         1,      adjective ],
    [ "Meat",         1,      meat      ],
    [ "Meaty",        2,      adjective ],
    [ "Mega",         2,      modifier  ],
    [ "Metal",        2,      noun      ],
    [ "Mighty",       2,      adjective ],
    [ "Monkey",       2,      animal    ],
    [ "Monster",      2,      animal    ],
    [ "Moose",        1,      animal    ],
    [ "Mountain",     2,      noun      ],
    [ "Mud",          1,      noun      ],
    [ "Mug",          1,      nounVerb  ],
    [ "Mule",         1,      animal    ],
    [ "Munch",        1,      verb      ],
    [ "Muscle",       2,      bodyPart  ],
    [ "Nasty",        2,      adjective ],
    [ "Neck",         1,      bodyPart  ],
    [ "Nitro",        2,      noun      ],
    [ "Nuke",         1,      nounVerb  ],
    [ "Ogre",         2,      noun      ],
    [ "Ox",           1,      animal    ],
    [ "Oxen",         2,      animal    ],
    [ "Pain",         1,      noun      ],
    [ "Pig",          1,      animal    ],
    [ "Pile",         2,      noun      ],
    [ "Pistol",       2,      noun      ],
    [ "Plank",        1,      noun      ],
    [ "Plug",         1,      nounVerb  ],
    [ "Pork",         1,      meat      ],
    [ "Pound",        1,      verb      ],
    [ "Power",        2,      noun      ],
    [ "Pummel",       2,      verb      ],
    [ "Punch",        1,      nounVerb  ],
    [ "Punching",     1,      adjective ],
    [ "Punk",         1,      noun      ],
    [ "Punt",         1,      verb      ],
    [ "Quarrel",      2,      verb      ],
    [ "Rage",         1,      noun      ],
    [ "Ram",          1,      nounVerb  ],
    [ "Ready",        2,      adjective ],
    [ "Red",          1,      adjective ],
    [ "Rib",          1,      bodyPart  ],
    [ "Rigid",        2,      adjective ],
    [ "Rip",          1,      verb      ],
    [ "Rivet",        2,      nounVerb  ],
    [ "Roar",         1,      verb      ],
    [ "Rock",         1,      noun      ],
    [ "Rocket",       2,      noun      ],
    [ "Rough",        1,      adjective ],
    [ "Rowdy",        2,      adjective ],
    [ "Rugged",       2,      adjective ],
    [ "Rumble",       2,      verb      ],
    [ "Rump",         1,      bodyPart  ],
    [ "Rust",         1,      noun      ],
    [ "Rusty",        2,      adjective ],
    [ "Scar",         1,      noun      ],
    [ "Scare",        1,      verb      ],
    [ "Scary",        2,      adjective ],
    [ "Scissor",      1,      verb      ],
    [ "Scorch",       1,      verb      ],
    [ "Scrape",       1,      verb      ],
    [ "Scream",       1,      nounVerb  ],
    [ "Shank",        1,      nounVerb  ],
    [ "Shark",        1,      noun      ],
    [ "Sharp",        1,      adjective ],
    [ "Shatter",      2,      verb      ],
    [ "Shoot",        1,      verb      ],
    [ "Shoulder",     2,      bodyPart  ],
    [ "Shout",        1,      verb      ],
    [ "Shove",        1,      verb      ],
    [ "Shovel",       1,      noun      ],
    [ "Shrapnel",     2,      noun      ],
    [ "Side",         1,      adjective ],
    [ "Singe",        1,      verb      ],
    [ "Sizzle",       2,      verb      ],
    [ "Skull",        1,      bodyPart  ],
    [ "Skunk",        1,      animal    ],
    [ "Slab",         1,      noun      ],
    [ "Slag",         1,      verb      ],
    [ "Slam",         1,      verb      ],
    [ "Slap",         1,      verb      ],
    [ "Slug",         1,      verb      ],
    [ "Smash",        1,      verb      ],
    [ "Smoke",        1,      noun      ],
    [ "Smug",         1,      adjective ],
    [ "Snake",        1,      animal    ],
    [ "Snap",         1,      verb      ],
    [ "Snarl",        1,      verb      ],
    [ "Solid",        2,      adjective ],
    [ "Spank",        1,      verb      ],
    [ "Speed",        1,      noun      ],
    [ "Spit",         1,      verb      ],
    [ "Spittle",      2,      noun      ],
    [ "Splinter",     2,      verb      ],
    [ "Split",        1,      verb      ],
    [ "Sprain",       1,      nounVerb  ],
    [ "Spud",         1,      noun      ],
    [ "Square",       1,      adjective ],
    [ "Squash",       1,      verb      ],
    [ "Squat",        1,      verb      ],
    [ "Squeeze",      1,      verb      ],
    [ "Stag",         1,      animal    ],
    [ "Stamp",        1,      verb      ],
    [ "Steak",        1,      meat      ],
    [ "Steel",        1,      adjective ],
    [ "Stick",        1,      noun      ],
    [ "Stomp",        1,      verb      ],
    [ "Stone",        1,      adjective ],
    [ "Storm",        1,      noun      ],
    [ "Strangle",     2,      verb      ],
    [ "Strike",       1,      verb      ],
    [ "Strong",       1,      adjective ],
    [ "Stud",         1,      noun      ],
    [ "Stump",        1,      noun      ],
    [ "Super",        1,      adjective ],
    [ "Sweat",        1,      nounVerb  ],
    [ "Sweaty",       1,      adjective ],
    [ "Swift",        1,      adjective ],
    [ "Tackle",       2,      verb      ],
    [ "Tank",         1,      noun      ],
    [ "Tear",         1,      verb      ],
    [ "Teeth",        1,      bodyPart  ],
    [ "Thick",        1,      adjective ],
    [ "Thrash",       1,      verb      ],
    [ "Throat",       1,      bodyPart  ],
    [ "Throw",        1,      verb      ],
    [ "Thud",         1,      noun      ],
    [ "Thump",        1,      verb      ],
    [ "Thunder",      2,      adjective ],
    [ "Tiger",        2,      animal    ],
    [ "Toad",         1,      animal    ],
    [ "Tooth",        1,      bodyPart  ],
    [ "Torch",        1,      noun      ],
    [ "Tough",        1,      adjective ],
    [ "Tower",        2,      noun      ],
    [ "Trample",      2,      verb      ],
    [ "Triple",       2,      adjective ],
    [ "Truck",        1,      noun      ],
    [ "Twist",        1,      verb      ],
    [ "Twister",      1,      noun      ],
    [ "Ugly",         2,      adjective ],
    [ "van der ",     2,      modifier  ],
    [ "Viper",        2,      animal    ],
    [ "Volt",         1,      noun      ],
    [ "von ",         1,      modifier  ],
    [ "Vulture",      2,      animal    ],
    [ "Wall",         1,      noun      ],
    [ "Wallop",       2,      verb      ],
    [ "War",          1,      noun      ],
    [ "Whip",         1,      nounVerb  ],
    [ "Widow",        2,      noun      ],
    [ "Wild",         1,      adjective ],
    [ "Wolf",         1,      animal    ],
    [ "Wound",        1,      verb      ],
    [ "Wrath",        1,      noun      ],
    [ "Wreck",        1,      verb      ],
    [ "Wrench",       1,      nounVerb  ],
    [ "Wrestle",      1,      verb      ],
    [ "Yak",          1,      animal    ],
    [ "Yank",         1,      verb      ],
]


lastNameTwoList = [
    [ "able",         2,      modifier  ],
    [ "alo",          2,      modifier  ],
    [ "alot",         2,      modifier  ],
    [ "amundo",       3,      modifier  ],
    [ "angry",        2,      adjective ],
    [ "ankle",        2,      bodyPart  ],
    [ "anvil",        2,      noun      ],
    [ "ape",          1,      animal    ],
    [ "arillo",       3,      modifier  ],
    [ "assault",      2,      verb      ],
    [ "attack",       2,      noun      ],
    [ "axe",          1,      noun      ],
    [ "back",         1,      bodyPart  ],
    [ "bacon",        2,      meat      ],
    [ "bad",          1,      adjective ],
    [ "badger",       2,      animal    ],
    [ "bang",         1,      noun      ],
    [ "banger",       2,      noun      ],
    [ "barrage",      2,      noun      ],
    [ "bash",         1,      verb      ],
    [ "basher",       2,      noun      ],
    [ "batch",        1,      noun      ],
    [ "batter",       2,      verb      ],
    [ "battle",       2,      nounVerb  ],
    [ "bear",         1,      animal    ],
    [ "beast",        1,      animal    ],
    [ "beef",         1,      meat      ],
    [ "bender",       2,      noun      ],
    [ "berg",         1,      modifier  ],
    [ "berserk",      1,      adjective ],
    [ "big",          1,      adjective ],
    [ "bison",        2,      animal    ],
    [ "bite",         1,      verb      ],
    [ "biter",        2,      noun      ],
    [ "blade",        1,      noun      ],
    [ "blast",        1,      nounVerb  ],
    [ "blaster",      2,      noun      ],
    [ "block",        1,      nounVerb  ],
    [ "body",         2,      bodyPart  ],
    [ "bold",         1,      adjective ],
    [ "bolt",         1,      noun      ],
    [ "bomb",         1,      verb      ],
    [ "bomber",       2,      noun      ],
    [ "bone",         1,      noun      ],
    [ "boot",         1,      nounVerb  ],
    [ "boulder",      2,      noun      ],
    [ "box",          1,      noun      ],
    [ "brave",        1,      adjective ],
    [ "brawl",        1,      nounVerb  ],
    [ "brawler",      2,      noun      ],
    [ "break",        1,      verb      ],
    [ "breaker",      2,      noun      ],
    [ "breath",       1,      bodyPart  ],
    [ "brick",        1,      noun      ],
    [ "bringer",      2,      noun      ],
    [ "bruise",       1,      verb      ],
    [ "bruiser",      2,      noun      ],
    [ "brutal",       1,      adjective ],
    [ "brute",        1,      noun      ],
    [ "bucket",       2,      noun      ],
    [ "bulge",        1,      noun      ],
    [ "bulk",         1,      noun      ],
    [ "bull",         1,      animal    ],
    [ "bullet",       2,      noun      ],
    [ "burger",       2,      modifier  ],
    [ "burn",         1,      verb      ],
    [ "burner",       2,      verb      ],
    [ "burst",        1,      verb      ],
    [ "buster",       2,      noun      ],
    [ "butt",         1,      bodyPart  ],
    [ "cage",         1,      noun      ],
    [ "cannon",       2,      noun      ],
    [ "castle",       2,      noun      ],
    [ "charger",      2,      noun      ],
    [ "cheese",       1,      noun      ],
    [ "chest",        1,      bodyPart  ],
    [ "chewer",       2,      noun      ],
    [ "chin",         1,      bodyPart  ],
    [ "chisel",       2,      nounVerb  ],
    [ "choke",        1,      verb      ],
    [ "chomp",        1,      verb      ],
    [ "chop",         1,      verb      ],
    [ "chump",        1,      noun      ],
    [ "chunk",        1,      noun      ],
    [ "churn",        1,      verb      ],
    [ "clamp",        1,      noun      ],
    [ "clobber",      2,      verb      ],
    [ "clump",        1,      noun      ],
    [ "cougar",       2,      animal    ],
    [ "crack",        1,      verb      ],
    [ "cracker",      2,      noun      ],
    [ "cram",         1,      verb      ],
    [ "cramp",        1,      noun      ],
    [ "crank",        1,      verb      ],
    [ "crash",        1,      verb      ],
    [ "crasher",      2,      noun      ],
    [ "crazy",        2,      adjective ],
    [ "cripple",      2,      verb      ],
    [ "crippler",     2,      noun      ],
    [ "crumble",      2,      verb      ],
    [ "crumple",      2,      verb      ],
    [ "crunch",       1,      verb      ],
    [ "cruncher",     2,      noun      ],
    [ "crush",        1,      verb      ],
    [ "crusher",      2,      noun      ],
    [ "cuda",         2,      modifier  ],
    [ "damage",       2,      noun      ],
    [ "danger",       2,      noun      ],
    [ "dead",         1,      adjective ],
    [ "dirt",         1,      noun      ],
    [ "dog",          1,      animal    ],
    [ "dozer",        2,      modifier  ],
    [ "dragon",       2,      animal    ],
    [ "dread",        1,      nounVerb  ],
    [ "driver",       2,      noun      ],
    [ "drop",         1,      verb      ],
    [ "eater",        2,      noun      ],
    [ "enheimer",     2,      modifier  ],
    [ "enstein",      2,      modifier  ],
    [ "erella",       3,      modifier  ],
    [ "erino",        3,      modifier  ],
    [ "face",         1,      bodyPart  ],
    [ "fall",         1,      verb      ],
    [ "fast",         1,      adjective ],
    [ "faster",       2,      adjective ],
    [ "feast",        1,      noun      ],
    [ "feet",         1,      bodyPart  ],
    [ "fierce",       1,      adjective ],
    [ "fight",        1,      verb      ],
    [ "fighter",      2,      noun      ],
    [ "fire",         2,      noun      ],
    [ "fist",         1,      bodyPart  ],
    [ "flank",        1,      noun      ],
    [ "flog",         1,      verb      ],
    [ "foot",         1,      bodyPart  ],
    [ "force",        1,      nounVerb  ],
    [ "fracture",     2,      nounVerb  ],
    [ "frag",         1,      verb      ],
    [ "fragger",      2,      noun      ],
    [ "fury",         2,      noun      ],
    [ "gator",        2,      animal    ],
    [ "goat",         1,      animal    ],
    [ "gouge",        1,      verb      ],
    [ "gouger",       2,      noun      ],
    [ "grab",         1,      verb      ],
    [ "grabber",      2,      noun      ],
    [ "granite",      2,      adjective ],
    [ "gravel",       2,      noun      ],
    [ "grease",       1,      noun      ],
    [ "grind",        1,      verb      ],
    [ "grinder",      2,      noun      ],
    [ "gristle",      2,      noun      ],
    [ "groin",        1,      bodyPart  ],
    [ "growl",        1,      verb      ],
    [ "grunt",        1,      verb      ],
    [ "gut",          1,      bodyPart  ],
    [ "guts",         1,      bodyPart  ],
    [ "hack",         1,      verb      ],
    [ "hair",         1,      bodyPart  ],
    [ "ham",          1,      meat      ],
    [ "hammer",       2,      nounVerb  ],
    [ "hard",         1,      adjective ],
    [ "harm",         1,      verb      ],
    [ "hatchet",      2,      noun      ],
    [ "hawk",         1,      animal    ],
    [ "head",         1,      bodyPart  ],
    [ "heap",         1,      noun      ],
    [ "heart",        1,      bodyPart  ],
    [ "heave",        1,      verb      ],
    [ "heavy",        1,      adjective ],
    [ "heel",         1,      bodyPart  ],
    [ "hinder",       2,      bodyPart  ],
    [ "hit",          1,      verb      ],
    [ "hog",          1,      animal    ],
    [ "horse",        1,      animal    ],
    [ "hound",        1,      animal    ],
    [ "huge",         1,      adjective ],
    [ "hulk",         1,      noun      ],
    [ "hunk",         1,      noun      ],
    [ "hunter",       2,      noun      ],
    [ "hurl",         1,      verb      ],
    [ "hurler",       2,      noun      ],
    [ "hurt",         1,      verb      ],
    [ "ilicious",     3,      modifier  ],
    [ "inator",       3,      modifier  ],
    [ "ington",       2,      modifier  ],
    [ "iron",         2,      adjective ],
    [ "jab",          1,      verb      ],
    [ "jam",          1,      verb      ],
    [ "jammer",       2,      noun      ],
    [ "jaw",          1,      bodyPart  ],
    [ "jet",          1,      noun      ],
    [ "jowls",        1,      bodyPart  ],
    [ "jump",         1,      verb      ],
    [ "kapow",        2,      noun      ],
    [ "kick",         1,      verb      ],
    [ "kicker",       2,      noun      ],
    [ "kill",         1,      verb      ],
    [ "knuckle",      2,      bodyPart  ],
    [ "knuckles",     2,      bodyPart  ],
    [ "large",        1,      adjective ],
    [ "leather",      2,      noun      ],
    [ "legs",         1,      bodyPart  ],
    [ "leopard",      2,      animal    ],
    [ "ley",          1,      modifier  ],
    [ "licious",      2,      modifier  ],
    [ "lightning",    2,      noun      ],
    [ "lion",         2,      animal    ],
    [ "lip",          1,      bodyPart  ],
    [ "lips",         1,      bodyPart  ],
    [ "load",         1,      noun      ],
    [ "log",          1,      noun      ],
    [ "lots",         1,      modifier  ],
    [ "loud",         1,      adjective ],
    [ "lumber",       2,      noun      ],
    [ "lump",         1,      noun      ],
    [ "ly",           1,      modifier  ],
    [ "maker",        1,      noun      ],
    [ "mallet",       2,      noun      ],
    [ "man",          1,      noun      ],
    [ "mangle",       1,      verb      ],
    [ "mangler",      2,      noun      ],
    [ "mash",         1,      verb      ],
    [ "masher",       2,      noun      ],
    [ "master",       2,      noun      ],
    [ "meal",         1,      noun      ],
    [ "meat",         1,      meat      ],
    [ "meister",      2,      noun      ],
    [ "metal",        2,      noun      ],
    [ "monger",       2,      noun      ],
    [ "monster",      2,      animal    ],
    [ "moose",        1,      animal    ],
    [ "mountain",     2,      noun      ],
    [ "mouth",        1,      bodyPart  ],
    [ "mower",        1,      modifier  ],
    [ "mud",          1,      noun      ],
    [ "mule",         1,      animal    ],
    [ "munch",        1,      verb      ],
    [ "muncher",      2,      noun      ],
    [ "muscle",       2,      bodyPart  ],
    [ "naut",         1,      modifier  ],
    [ "neck",         1,      bodyPart  ],
    [ "normous",      2,      modifier  ],
    [ "nuke",         1,      verb      ],
    [ "nuker",        2,      noun      ],
    [ "ogre",         2,      noun      ],
    [ "omatic",       3,      modifier  ],
    [ "orama",        3,      modifier  ],
    [ "pain",         1,      noun      ],
    [ "pants",        1,      noun      ],
    [ "pecs",         1,      bodyPart  ],
    [ "pile",         1,      noun      ],
    [ "plank",        1,      noun      ],
    [ "pork",         1,      meat      ],
    [ "pound",        1,      verb      ],
    [ "pounder",      2,      noun      ],
    [ "power",        2,      noun      ],
    [ "pummel",       2,      verb      ],
    [ "punch",        1,      verb      ],
    [ "puncher",      2,      noun      ],
    [ "puncture",     2,      nounVerb  ],
    [ "punk",         1,      noun      ],
    [ "punt",         1,      verb      ],
    [ "punter",       2,      noun      ],
    [ "quake",        1,      modifier  ],
    [ "rage",         1,      noun      ],
    [ "ram",          1,      verb      ],
    [ "ribs",         1,      bodyPart  ],
    [ "rilla",        1,      animal    ],
    [ "riot",         2,      noun      ],
    [ "rip",          1,      verb      ],
    [ "rivet",        2,      nounVerb  ],
    [ "roar",         1,      verb      ],
    [ "roast",        1,      nounVerb  ],
    [ "rock",         1,      noun      ],
    [ "rocket",       2,      noun      ],
    [ "rumble",       2,      nounVerb  ],
    [ "rump",         1,      bodyPart  ],
    [ "scar",         1,      adjective ],
    [ "scorch" ,      1,      verb      ],
    [ "shank",        1,      nounVerb  ],
    [ "shooter",      2,      noun      ],
    [ "shoulder",     2,      bodyPart  ],
    [ "shout",        1,      verb      ],
    [ "shovel",       2,      nounVerb  ],
    [ "shrapnel",     2,      noun      ],
    [ "shredder",     2,      noun      ],
    [ "skull",        1,      bodyPart  ],
    [ "slab",         1,      verb      ],
    [ "slag",         1,      verb      ],
    [ "slam",         1,      verb      ],
    [ "slammer",      2,      noun      ],
    [ "slap",         1,      verb      ],
    [ "slapper",      2,      noun      ],
    [ "slugger",      2,      noun      ],
    [ "smash",        1,      verb      ],
    [ "smasher",      2,      noun      ],
    [ "snag",         1,      verb      ],
    [ "snake",        1,      animal    ],
    [ "snap",         1,      verb      ],
    [ "snapper",      2,      noun      ],
    [ "snarl",        1,      verb      ],
    [ "socket",       2,      bodyPart  ],
    [ "spank",        1,      verb      ],
    [ "spanker",      2,      noun      ],
    [ "speed",        1,      noun      ],
    [ "spit",         1,      verb      ],
    [ "spittle",      2,      noun      ],
    [ "splinter",     2,      verb      ],
    [ "split",        1,      verb      ],
    [ "splode",       1,      nounVerb  ],
    [ "splosion",     2,      modifier  ],
    [ "sprain",       1,      verb      ],
    [ "squash",       1,      verb      ],
    [ "squasher",     2,      adjective ],
    [ "stack",        1,      noun      ],
    [ "stag",         1,      animal    ],
    [ "steak",        1,      meat      ],
    [ "steel",        1,      adjective ],
    [ "stein",        1,      modifier  ],
    [ "stick",        1,      noun      ],
    [ "stomp",        1,      verb      ],
    [ "stone",        1,      adjective ],
    [ "storm",        1,      noun      ],
    [ "strangle",     2,      verb      ],
    [ "strike",       1,      verb      ],
    [ "striker",      1,      noun      ],
    [ "strong",       1,      adjective ],
    [ "stud",         1,      noun      ],
    [ "stump",        1,      noun      ],
    [ "sweat",        1,      nounVerb  ],
    [ "swift",        1,      adjective ],
    [ "sword",        1,      noun      ],
    [ "tackle",       2,      verb      ],
    [ "tacular",      3,      modifier  ],
    [ "tank",         1,      noun      ],
    [ "tastic",       2,      modifier  ],
    [ "tastic",       2,      modifier  ],
    [ "teeth",        1,      bodyPart  ],
    [ "thick",        1,      adjective ],
    [ "thrash",       1,      verb      ],
    [ "throat",       1,      bodyPart  ],
    [ "thrust",       1,      verb      ],
    [ "thud",         1,      noun      ],
    [ "thump",        1,      verb      ],
    [ "thumper",      2,      noun      ],
    [ "thunder",      2,      noun      ],
    [ "tiger",        2,      animal    ],
    [ "toad",         1,      animal    ],
    [ "tooth",        1,      bodyPart  ],
    [ "torch",        1,      noun      ],
    [ "torn",         1,      adjective ],
    [ "tough",        1,      adjective ],
    [ "tower",        2,      noun      ],
    [ "trample",      2,      verb      ],
    [ "truck",        1,      noun      ],
    [ "twister",      2,      noun      ],
    [ "viper",        2,      animal    ],
    [ "volt",         1,      noun      ],
    [ "vulture",      2,      animal    ],
    [ "wall",         1,      noun      ],
    [ "wallop",       2,      verb      ],
    [ "war",          1,      noun      ],
    [ "welt",         1,      noun      ],
    [ "whip",         1,      nounVerb  ],
    [ "wolf",         1,      animal    ],
    [ "wood",         1,      noun      ],
    [ "wound",        1,      noun      ],
    [ "wrangler",     2,      noun      ],
    [ "wrath",        1,      noun      ],
    [ "wreck",        1,      verb      ],
    [ "wrecker",      2,      noun      ],
    [ "wrench",       1,      nounVerb  ],
    [ "wrestle",      2,      verb      ],
    [ "wrestler",     2,      noun      ],
    [ "yak",          1,      animal    ],
    [ "yank",         1,      verb      ],
    [ "yanker",       1,      noun      ],
    [ "zilla",        2,      modifier  ],
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

    # while firstName == lastNameOne[ 0 ]:
    #     lastNameOne = getLastNameOne( )

        # if firstName == lastNameOne[ 0 ]:
        #     print( "-->  " + firstName + " " + lastNameOne[ 0 ] )

    lastNameTwo = getLastNameTwo( )

    # lastNameTwo = [ "enheimer", 2, modifier ]

    # lastNameOne[ 0 ] in [ "Back", "Side" ] ) and ( lastNameTwo[ 2 ] in [ noun, bodyPart, animal, adjective, modifier ] ) ) or \

    while ( ( "ump" in lastNameOne[ 0 ] ) and ( "ump" in lastNameTwo[ 0 ] ) ) or \
          ( ( lastNameOne[ 0 ] == "Broke" ) and ( lastNameTwo[ 0 ] == "Back" ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Cracked", "Split", "Crushed", "Broke", "Broken", "Bent", "Heave" ] ) and ( lastNameTwo[ 2 ] in [ verb, adjective ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Cracked", "Crushed" ] ) and ( lastNameTwo[ 0 ][ 0 ] in [ "bcdgjkpst" ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Meaty", "Elbow" ] ) and ( lastNameTwo[ 2 ] in [ adjective ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Square" ] ) and ( lastNameTwo[ 2 ] not in [ noun, meat, bodyPart, animal ] ) ) or \
          ( ( lastNameOne[ 0 ] in [ "Wall" ] ) and ( lastNameTwo[ 2 ] not in [ nounVerb, verb ] ) ) or \
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
          ( ( lastNameOne[ 2 ] in [ bodyPart ]  ) and ( lastNameTwo[ 0 ] in [ "feast" ] ) ) or \
          ( ( lastNameOne[ 2 ] in [ adjective ] ) and ( lastNameOne[ 1 ] > 1 ) and ( lastNameTwo[ 0 ] in [ "normous" ] ) ) or \
          ( ( lastNameOne[ 2 ] in [ verb, adjective ] ) and ( lastNameTwo[ 0 ] in [ "heave", "torn" ] ) ) or \
          ( ( lastNameOne[ 2 ] not in [ bodyPart  ]  ) and ( lastNameTwo[ 0 ] in [ "damage" ] ) ) or \
          ( firstName.lower( ) == lastNameTwo[ 0 ] ) or \
          ( lastNameOne[ 0 ].lower( ) == lastNameTwo[ 0 ] ) or \
          ( lastNameOne[ 0 ][ -3 : ] == lastNameTwo[ 0 ][ -3 : ] ) or \
          ( lastNameOne[ 0 ][ : 4 ].lower( ) == lastNameTwo[ 0 ][ : 4 ] ) or \
          ( ( lastNameOne[ 2 ] not in [ verb, nounVerb  ] ) and  ( lastNameTwo[ 0 ] == "lots" ) ):
        # print( firstName + " " + lastNameOne[ 0 ] + " " + lastNameTwo[ 0 ] )
        lastNameTwo = getLastNameTwo( )

    # now we might need to modify the strings, so let's copy them
    lastNameFirstHalf = lastNameOne[ 0 ]
    lastNameLastHalf = lastNameTwo[ 0 ]

    # when consonant-vowel-consonant gets an 'e' or 'i' appended, double the final consonant
    if ( ( lastNameFirstHalf[ -1 ] in consonants ) and ( lastNameFirstHalf[ -2 ] in vowels ) and \
         ( lastNameFirstHalf[ -3 ] in consonants ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ) ):
        lastNameFirstHalf += lastNameFirstHalf[ -1 ]

    # when adding an 'e' or an 'i' to a trailing 'e', eat the trailing 'e' first
    if ( ( lastNameFirstHalf[ -1 ] == "e" ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ) ):
        lastNameFirstHalf = lastNameFirstHalf[ : -1 ]

    # double consonants with adding 'e' or 'i' makes a vowel-consonant-vowel combination
    if ( ( len( lastNameFirstHalf ) > 2 ) and ( lastNameFirstHalf[ -3 ] in vowels ) and ( lastNameFirstHalf[ -2 ] in consonants ) and
         ( lastNameFirstHalf[ -1 ] in vowels ) and ( lastNameLastHalf in [ "enstein", "enheimer", "erella", "erino", "inator" ] ) ):
        lastNameFirstHalf.Insert( -2, lastNameFirstHalf[ -2 ] )

    if ( ( lastNameFirstHalf[ -2 : ] == "le" ) and ( lastNameLastHalf in [ "ly", "ley" ] ) ):
        lastNameLastHalf = "y"

    middle = " "

    # if the first part is not a modifier then consider adding a middle name (which is basically just another modifier)
    if lastNameOne[ 2 ] == modifier:
        while True:
            lastNameTwo = getLastNameOne( )

            if lastNameTwo[ 2 ] == modifier:
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
            elif ( ( firstName in [ "Baron", "Count" ] ) and ( random.randint( 1, 12 ) ) ):
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
Coming soon to a theater near you: <a href="http://zycha.com/BMovie.py">B-Movies</a>!<br>
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

    webPage = "Content-Type: text/html\r\n\r\n"
    webPage += siteHeader( pageTitle )
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

