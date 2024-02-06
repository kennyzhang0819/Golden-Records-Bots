import discord
import random
from discord.ext import commands

TOKEN = ''
intents = discord.Intents(messages=True, reactions=True, guilds=True, members=True, message_content=True)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)



genres = [
    'Pop', 'Hip-Hop', 'Jazz', 'Electronic', 'Ambient', 'Rock', 'Classical', 'Funk', 'Reggae', 'Soul',
    'House', 'Trance', 'Dubstep', 'Drum and Bass', 'Techno', 'Electro House', 'Progressive House', 'Trap', 'Breakbeat', 'Neurofunk', 'Hardcore', 
    'Psytrance', 'Glitch Hop', 'Moombahton', 'Tropical House', 'Chillstep', 'Liquid DnB', 'Artcore', 'Dariacore'
    'Blues', 'Country', 'Folk', 'Gospel', 'Opera', 'Ska', 'Swing', 'Metal', 'Punk', 'Disco',
    'Lo-fi', 'Glitch', 'Hardstyle', 'Jungle', 'Garage', 'Grime', 'Chillwave', 'Vaporwave', 'Synthwave', 'Eurodance',
    'Afrobeat', 'Bossa Nova', 'Cumbia', 'Flamenco', 'Reggaeton', 'Salsa', 'Samba', 'Tango', 'Zouk', 'Bachata',
    'Acid Jazz', 'Afro Punk', 'Chamber Pop', 'Darkwave', 'Ethno Jazz', 'Folktronica', 'Gypsy Jazz', 'Hip Hopera', 'Math Rock', 'Neo Soul',
    'Psybient', 'Shoegaze', 'Trip Hop', 'Worldbeat', 'Zydeco', 'Nu Disco', 'Electro Swing', 'Future Bass', 'Gqom', 'Jersey Club', 'Kawaii Future Bass',
    'K-Pop', 'J-Pop', 'C-Pop', 'Qawwali', 'Ghazal', 'Bhangra', 'Dangdut', 'Filmi', 'Arabesque', 'Fado'
]
bpms = [str(i) for i in range(60, 201, 5)]
styles = ['Minimalist', 'Experimental', 'Cinematic', 'Retro', 'Psychedelic', 'Acoustic', 'Heavy', 'Groovy', 'Chill', 'Uplifting']
samples = ['Piano', 'Violin', 'Synth', 'Bass', 'Guitar', 'Drums', 'Flute', 'Saxophone', 'Vocal Chops', 'Harp', "Bed Squeak", "Ducks Quacking", 
           "Baby Crying", "Raindrops", "Wind Chimes", "Clock Ticking", "Train Horn", "Thunderclap", "Cat Meowing", "Dog Barking",
           "Typewriter Clicks", "Glass Breaking", "Waves Crashing", "Leaves Rustling", "Campfire Crackling",
           "Footsteps on Gravel", "Birds Chirping", "Soda Can Opening", "Bubble Wrap Popping", "Car Engine Starting",
           "Doorbell Ringing", "Police Siren", "Horse Neighing", "Sheep Baaing", "Cuckoo Clock",
           "Keyboard Typing", "Helicopter Blades", "Bicycle Bell", "Cash Register", "Chains Rattling",
           "Fireworks Exploding", "Golf Swing", "Skateboard Tricks", "Basketball Bounce", "Bowling Strike",
           "Slot Machine", "Spray Paint Can", "Air Horn", "Electric Drill", "Hammer Hits",
           "Pigeons Cooing", "Balloon Popping", "Water Dripping", "Snapping Fingers", "Crickets Chirping",
           "Zipper Zipping", "Gong Strike", "Harp Glissando", "Zither Strum", "Applause",
           "Heartbeat", "Clock Alarm", "Electric Buzz", "Phone Vibration", "Cash Drawer",
           "Skateboard on Pavement", "Subway Train", "Beach Volleyball", "Marbles Rolling", "Ice Cubes Clinking",
           "Velcro Rip", "Vacuum Cleaner", "Sewing Machine", "Video Game Console Startup", "Record Scratch",
           "Laser Gun", "Spaceship Launch", "Robot Movements", "UFO Landing", "Magic Wand Sparkle",
           "Dragon Roaring", "Ghostly Whispers", "Wizard Spells", "Sword Clash", "Medieval Battle",
           "Pirate Ship Creaks", "Monster Growl", "Wolf Howling", "Eagle Screech", "Jungle Ambience",
           "Volcano Eruption", "Avalanche", "Tornado Winds", "Digital Glitch", "Morse Code",
           "Old Film Projector", "Radio Tuning", "Vinyl Record Hiss", "Light Saber", "Dripping Faucet",
           "Frying Bacon", "Scissors Cutting", "Paper Folding", "Velcro Fastening", "Horse Galloping",
           "Bubbles Blowing", "Woodpecker Pecking", "Old Clock Ticking", "Creaky Door Opening", "Whistle Blowing", "Old Movie",
           "Sleigh Bells", "Bicycle Bell", "Car Horn", "Police Siren", "Fire Truck Siren", "Ambulance Siren", "Acapella", "Reverse Effect",
           "Lo-fi textures", "808", "Brass", "Neuro Bass", "Percussion", "String", "Moaning", "Screaming", "Laughing", "Crying", "Sighing"
]
time_signatures = ['4/4', '3/4', '6/8', '5/4', '7/8']
plugins = [
    "Serum", "Vital", "FabFilter Pro-Q 3", "OTT", "Sylenth1", "Massive", "Nexus", "Ableton Live's Operator",
    "FL Studio's Harmor", "Logic Pro's Alchemy", "Arturia Pigments", "Omnisphere", "Kontakt", "Spire", 
    "Zebra2", "Diva", "Hive", "Rob Papen Predator", "Xfer Records Cthulhu", "Izotope Ozone",
    "Valhalla VintageVerb", "Soundtoys EchoBoy", "Waves SSL G-Master Buss Compressor", "Cableguys ShaperBox",
    "LFO Tool", "FabFilter Saturn", "CamelCrusher", "Decapitator", "RC-20 Retro Color", "FabFilter Timeless",
    "Kickstart", "Native Instruments Reaktor", "Guitar Rig", "U-He Bazille", "ElectraX", "Absynth", 
    "Arturia V Collection", "Spectrasonics Keyscape", "Output Arcade", "UAD Shadow Hills Mastering Compressor",
    "Waves H-Delay", "Soundtoys Little AlterBoy", "Sausage Fattener", "FabFilter Twin", "Gross Beat", 
    "Native Instruments Guitar Rig", "Waves CLA Vocals", "iZotope Trash", "Reveal Sound Spire", "D16 Group Decimort",
    "Lexicon PCM Native Reverb", "Native Instruments The Giant", "Xfer Records SerumFX", "Celemony Melodyne", 
    "Waves Renaissance Reverb", "U-He Repro", "FabFilter One", "Roland Cloud Jupiter-8", "Softube Saturation Knob", 
    "Waves L2 Ultramaximizer", "Klanghelm MJUC", "MeldaProduction MTotalBundle", "Sonnox Oxford Inflator", 
    "Tone2 Gladiator", "Eventide Blackhole", "Soundtoys PrimalTap", "Brainworx bx_digital V3", "PSP VintageWarmer2", 
    "Izotope Vinyl", "Arturia CS-80 V", "Waves Bass Rider", "Antares Auto-Tune", "Sugar Bytes Effectrix", 
    "Spectrasonics Trilian", "Xfer Nerve", "NI Battery", "Valhalla Room", "Sonnox Oxford EQ", "Soundtoys Crystalizer", 
    "Boz Digital Labs Little Foot", "Output Portal", "TAL-U-NO-LX", "McDSP FutzBox", "FabFilter Volcano", 
    "Waves Torque", "Plugin Alliance Brainworx bx_console", "Waves CLA-76 Compressor", "Tokyo Dawn TDR Kotelnikov", 
    "D16 Group Toraverb", "Plugin Boutique Scaler", "Cytomic The Glue", "Native Instruments Massive X", 
    "Audio Damage EOS", "Plugin Alliance Maag EQ4", "iZotope Nectar", "Softube Tube-Tech CL 1B", 
    "Waves Aphex Vintage Aural Exciter", "HoRNet SongKey MK3", "FabFilter Simplon", "U-He ColourCopy", 
]
themes = [
    "Spring", "Water", "Evil", "Cute", "Space", "Mystery", "Love", "Adventure", "Dream", "Chaos",
    "Sunset", "Forest", "Urban Jungle", "Retro Future", "Mythology", "Underwater", "Desert", "Winter",
    "Vintage", "Cyberpunk", "Steampunk", "Alien Invasion", "Ancient Civilizations", "Haunted", "Festival",
    "Journey", "Celebration", "Solitude", "Revolution", "Fantasy", "War", "Peace", "Joy", "Sorrow",
    "Hope", "Melancholy", "Euphoria", "Zen", "Nostalgia", "Futuristic", "Industrial", "Tropical",
    "Meditation", "Chillout", "Rage", "Fear", "Courage", "Mystery", "Discovery", "Enigma", "Illusion",
    "Whimsical", "Epic", "Minimal", "Complex", "Organic", "Mechanical", "Digital", "Analog", "Noir",
    "Sunrise", "Nightfall", "Dystopia", "Utopia", "Rebirth", "Extinction", "Innovation", "Tradition",
    "Harmony", "Discord", "Silence", "Loudness", "Movement", "Stillness", "Chaos", "Order", "Primitive",
    "Sophisticated", "Rural", "Metropolitan", "Heaven", "Hell", "Purgatory", "Ascension", "Decline",
    "Birth", "Death", "Eternity", "Moment", "Time Travel", "Parallel Universe", "Dreamscape", "Nightmare",
    "Memory", "Forgetfulness", "Reality", "Fantasy", "Virtual", "Authentic", "Synthetic", "Natural",
    "East", "West", "North", "South", "Earth", "Fire", "Air", "Water", "Spirit", "Matter"
]


# Probabilities
include_genre = 0.80
include_bpm = 0.60
include_style = 0.30
include_sample = 0.80
include_time_signature = 0.20
include_plugins = 0.60
include_theme = 0.50

def generate_challenge():
    challenge_parts = []

    if random.random() < include_genre:
        genre = random.choice(genres)
        challenge_parts.append(f"a {genre} track")
        if random.random() < 0.5:
            additional_genre = random.choice(genres)
            challenge_parts.append(f"blending with {additional_genre}")
    else:
        challenge_parts.append("a track")

    if random.random() < include_bpm:
        bpm = random.choice(bpms)
        challenge_parts.append(f"with a BPM of {bpm}")

    if random.random() < include_style:
        style = random.choice(styles)
        challenge_parts.append(f"in {style} style")

    if random.random() < include_sample:
        num_samples = random.randint(1, 3)
        selected_samples = random.sample(samples, num_samples)
        sample_text = "using samples of " + ", ".join(selected_samples)
        challenge_parts.append(sample_text)

    if random.random() < include_time_signature:
        time_signature = random.choice(time_signatures)
        challenge_parts.append(f"in {time_signature} time")

    if random.random() < include_plugins:
        random_plugin = random.choice(plugins)
        challenge_parts.append(f"using the '{random_plugin}' plugin")

    if random.random() < include_theme:
        theme = random.choice(themes)
        challenge_parts.append(f"with a '{theme}' theme")

    if len(challenge_parts) > 1:
        last_part = challenge_parts.pop()
        return "Create " + ", ".join(challenge_parts) + ", and " + last_part + "."
    else:
        return "Create " + "".join(challenge_parts) + "."


@bot.command(name='challenge')
async def challenge(ctx):
    challenge_text = generate_challenge()
    await ctx.send(challenge_text)

bot.run(TOKEN)