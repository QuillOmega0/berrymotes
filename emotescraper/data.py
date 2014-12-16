nsfw_subreddits = [
    # Subreddits which when scraped will automatically have any emotes tagged as nsfw.
    "mylittlensfw",
    "clopmotes"
]

image_blacklist = [
    # Prevent any of the stylesheets from ever being emoted.
    "http://a.thumbs.redditmedia.com/4BIUyA0SW1OkC5ON.png",
    "http://f.thumbs.redditmedia.com/0Fr3gH0gBwtd9okw.png",
    "http://b.thumbs.redditmedia.com/GUrfNHIaMEoN29eC.jpg",
    "http://c.thumbs.redditmedia.com/5N6wrRpkfXoAv5lP.png",
    "http://e.thumbs.redditmedia.com/5ndsCluVaPSIsPOR.png",
    "http://b.thumbs.redditmedia.com/9KPIZR5eNlWAev7m.png",
    "http://e.thumbs.redditmedia.com/5ndsCluVaPSIsPOR.png"
]

image_blacklist_android = image_blacklist + [
    # Android ignore; mostly because they are too large.
    "http://d.thumbs.redditmedia.com/6vnl2z58K-37e-du.png",
    "http://e.thumbs.redditmedia.com/m48Mt-C5OajCRvXp.png",
    "http://d.thumbs.redditmedia.com/jbMarIOi-_cCQIRW.png",
]

subreddits = [
    # Subreddits to scrape for emotes
    "marmemotes",
    "marmemotes2",
    "mlpaprilfools2014",
    "btcanimotes",
    "jericksvector",
    "mylittlepony",
    "mylittlevagrant",
    "abunchofemotes",
    "abunchmoreemotes",
    "abunchmoreofemotes",
    "ademotes",
    "adery",
    "aderytunes",
    "adviceponies",
    "afterplounge",
    "ainbowdash",
    "anotherponymotessub",
    "applebloom",
    "appledashquisition",
    "applefritter",
    "applejack",
    "arborus",
    "asmatteringofemotes",
    "babsquisition",
    "batquisition",
    "beautybrass",
    "berrytrain",
    "berrytubelounge",
    "berrytubeball",
    "berrytubetf2",
    "bigmacintosh",
    "bonquisition",
    "braeburnquisition",
    "BronyGaming",
    "BTLoungeLoungeLounge",
    "BTdoesntevenknow",
    "btmodminmotes",
    "BTMoonlit",
    "BTpatron",
    "cadance",
    "chakolateemotes",
    "cheesesandwichmlp",
    "cianimotes",
    "clopclop",
    "clopmotes",
    "cloudchasermotes",
    "comeinside",
    "commabombing",
    "cuttershy",
    "dashiemotes",
    "daxterionfanclub",
    "daylightemotes",
    "desktopponies",
    "dumbrock",
    "dumbtoxin",
    "EquestriaGirls",
    "falloutequestria",
    "findauseforthesemotes",
    "flait111",
    "flitter",
    "Flutquisition",
    "flutterlounge",
    "futemotes",
    "gallopfrey",
    "himntor",
    "hugemotes",
    "idliketobeatree",
    "ilovedashie",
    "isthisananimoteyet",
    "isthisanemoteyet",
    "jacksanimotes",
    "littlecolt",
    "littlemissbloomotes",
    "lyra",
    "lyraquisition",
    "malsententia",
    "maudpie",
    "meatemotes",
    "minuette",
    "mlas1animotes",
    "mlas1emotes",
    "mlas1emotes2",
    "mlas1imagedump",
    "mlas1party",
    "mlhfis",
    "mlpdrawingschool",
    "mlplounge",
    "mlploungesteamgroup",
    "mlpvectors",
    "molestia",
    "mortdoesreddit",
    "multihoofdrinking",
    "mylittleadventuretime",
    "mylittlealicorn",
    "mylittlealcoholic",
    "mylittleandysonic1",
    "mylittleanhero23",
    "mylittleanime",
    "mylittleaprilfools",
    "mylittleayrl",
    "mylittlebannertest",
    "mylittlecelestias",
    "mylittlechaos",
    "mylittlecirclejerk",
    "mylittlecombiners",
    "mylittleconspiracy",
    "mylittledamon",
    "mylittledaww",
    "mylittledota",
    "mylittledramaticstory",
    "mylittledraders",
    "mylittledurian",
    "mylittledusty",
    "mylittlefalloutdiary",
    "mylittlefistfight",
    "mylittlefoodmanes",
    "mylittlefortress",
    "mylittlefriends",
    "mylittleglittermotes",
    "mylittlegooglyeyes",
    "mylittleicons",
    "mylittlekindle",
    "mylittlekitchen",
    "mylittlekurtis",
    "mylittleleague",
    "mylittlelistentothis",
    "mylittlelivestream",
    "mylittlemango",
    "mylittlemilkyway",
    "mylittlemotorhead",
    "mylittlemusician",
    "mylittlenanners",
    "mylittlenopenopenope",
    "mylittlenosleep",
    "mylittlensfw",
    "mylittleonions",
    "mylittlepeanutgallery",
    "mylittlepugnippets",
    "mylittlescreamotes",
    "mylittleserver",
    "mylittlesh",
    "mylittlesketchheart",
    "MyLittleSlamJam",
    "mylittlesports",
    "mylittlesquidward",
    "mylittlestartrek",
    "mylittlesupportgroup",
    "mylittletacos",
    "mylittletwist",
    "mylittlevagrancy",
    "mylittlewarhammer",
    "mylittlewelcomewagon",
    "mylittlewtf",
    "nolifemotes",
    "octavia",
    "onetrueprincess",
    "pankakke",
    "pinkiepie",
    "pinkquisition",
    "ploungeafterdark",
    "ploungefootballleague",
    "ploungemafia",
    "ponyanarchism",
    "ponyloungerts",
    "ponymotes",
    "ponymotesextra",
    "pwettypwinkpwincesses",
    "Rainbowjackemotes",
    "rarity",
    "redtoxinemotes",
    "roseluck",
    "rubypinch",
    "ryumotes",
    "sapphirestone",
    "scratchquisition",
    "seriouslyluna",
    "sexyconfederatereddit",
    "shadeschatlounge",
    "shittyemotes",
    "spaceclop",
    "spanishmeerkat",
    "speedingturtle",
    "spitquisition",
    "stalliongrad",
    "sunsetshimmer",
    "surprise",
    "sweetie_belle",
    "tacoshy",
    "taviquisition",
    "tbpimagedump",
    "tbpimagedump2",
    "thanksblueshift",
    "thanksberrytube",
    "thebestpony",
    "thecane",
    "thepleasurehub",
    "trixquisition",
    "themirishponies",
    "tiltemotes",
    "twidashmotes",
    "twilightsparkle",
    "twiquisition",
    "vinylscratch",
    "yaxim3",
    "zponymotes",
    "adagiodazzle",
    "ariablaze",
    "sonatadusk",
]

emote_info = [
    # Add meta data to emotes; usually used to tag emotes as nsfw. Please add only one alias of an emote.
    {'name': 'thesafewordistoast', 'com': 'bt'},
    {'name': 'toastdeib', 'com': 'bt'},
    {'name': 'gtoastdeib', 'com': 'bt'},
    {'name': 'beardtoastdeib', 'com': 'bt'},
    {'name': 'toastdd', 'com': 'bt'},
    {'name': 'toastbusters2', 'com': 'bt'},
    {'name': 'fuckthepolice', 'com': 'bt'},
    {'name': 'cadesxsugargrapeotp', 'com': 'bt'},
    {'name': 'nerfed', 'com': 'bt'},
    {'name': 'thesafewordistoast', 'com': 'bt'},
    {'name': 'ajsbanana', 'nsfw': True},
    {'name': 'ajshake', 'nsfw': True},
    {'name': 'andy', 'nsfw': True},
    {'name': 'andy', 'nsfw': True},
    {'name': 'bestcentaur', 'nsfw': True},
    {'name': 'bigenough', 'nsfw': True},
    {'name': 'books', 'nsfw': True},
    {'name': 'books', 'nsfw': True},
    {'name': 'buzzkillturtle', 'nsfw': True},
    {'name': 'coggler', 'nsfw': True},
    {'name': 'derpyshake', 'nsfw': True},
    {'name': 'derpypussy', 'nsfw': True},
    {'name': 'fluttershake', 'nsfw': True},
    {'name': 'fruitamad', 'nsfw': True},
    {'name': 'fut1', 'nsfw': True},
    {'name': 'fut4', 'nsfw': True},
    {'name': 'fut1', 'nsfw': True},
    {'name': 'fut4', 'nsfw': True},
    {'name': 'futacute', 'nsfw': True},
    {'name': 'futaplot', 'nsfw': True},
    {'name': 'futapomf', 'nsfw': True},
    {'name': 'futashy', 'nsfw': True},
    {'name': 'rfutashy', 'nsfw': True},
    {'name': 'goddamnitmango', 'nsfw': True},
    {'name': 'hcstare', 'nsfw': True},
    {'name': 'hom3rbutt', 'nsfw': True},
    {'name': 'horsecock', 'nsfw': True},
    {'name': 'horsedick', 'nsfw': True},
    {'name': 'hugehorsedick', 'nsfw': True},
    {'name': 'jizz', 'nsfw': True},
    {'name': 'kitty', 'nsfw': True},
    {'name': 'konapenis', 'nsfw': True},
    {'name': 'milkymic', 'nsfw': True},
    {'name': 'orschemote', 'nsfw': True},
    {'name': 'pinkieshake', 'nsfw': True},
    {'name': 'pone', 'nsfw': True},
    {'name': 'rainbowponysemen', 'nsfw': True},
    {'name': 'rainbowshake', 'nsfw': True},
    {'name': 'rarshake', 'nsfw': True},
    {'name': 'rockhard', 'nsfw': True},
    {'name': 'rvinylshake', 'nsfw': True},
    {'name': 'sandwich', 'nsfw': True},
    {'name': 'selfsuck', 'nsfw': True},
    {'name': 'sphlyrafun', 'nsfw': True},
    {'name': 'sweetiebellesvirginmarshmallowpussy', 'nsfw': True},
    {'name': 'twishake', 'nsfw': True},
    {'name': 'twna', 'nsfw': True},
    {'name': 'vinylshake', 'nsfw': True},
    {'name': 'ponykoreaisbestkorea', 'nsfw': True},
    {'name': 'opdelivers', 'nsfw': True},
    {'name': 'googlykoreaisbestkorea', 'nsfw': True},
    {'name': 'lyrapenisdoubt', 'nsfw': True},
    {'name': 'twilightstrapkle', 'nsfw': True},
    {'name': 'shakedatassmatt', 'nsfw': True},
    {'name': 'braetavia', 'nsfw': True},
    {'name': 'thesaddestboner', 'nsfw': True},
    {'name': 'breakitin', 'nsfw': True},
    {'name': 'uwotm8', 'nsfw': True},
    {'name': 'iwilldildoyou', 'nsfw': True},
    {'name': 'twisockbutt', 'nsfw': True},
    {'name': 'futashyaj', 'nsfw': True},
    {'name': 'blueshaft', 'nsfw': True},
    {'name': 'noponyhere', 'nsfw': True},
    {'name': 'chryshininglick', 'nsfw': True},
    {'name': 'braerainbowsocks', 'nsfw': True},
    {'name': 'bukkakebrae', 'nsfw': True},
    {'name': 'milkydance', 'nsfw': True},
    {'name': 'laughingcock', 'nsfw': True},
    {'name': 'futatwishy', 'nsfw': True},
    {'name': 'futajhelp', 'nsfw': True},
    {'name': 'vinylbutt', 'nsfw': True},
    {'name': 'doublebutts', 'nsfw': True},
    {'name': 'futhelp', 'nsfw': True},
    {'name': 'PonisEnvy', 'nsfw': True},
    {'name': 'CanisEnvy', 'nsfw': True},
    {'name': 'cane', 'nsfw': True},
    {'name': 'nudity', 'nsfw': True},
    {'name': 'kissit', 'nsfw': True},
    {'name': 'mwno', 'nsfw': True},
    {'name': 'toxinclop', 'nsfw': True},
    {'name': 'dickchaser', 'nsfw': True},
    {'name': 'chaserdance', 'nsfw': True},
    {'name': 'dustypugfuckdoodle', 'nsfw': True},
    {'name': 'rdfuriousclopping', 'nsfw': True},
    {'name': 'moonlitguard', 'nsfw': True},
    {'name': 'octaviaprotection', 'nsfw': True}
]
