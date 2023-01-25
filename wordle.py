import random
from time import sleep
import os
from colorama import Fore, init
import enchant

possible_answers = ["CIGAR", "REBUT", "SISSY", "HUMPH", "AWAKE", "BLUSH", "FOCAL", "EVADE", "NAVAL", "SERVE", "HEATH", "DWARF", "MODEL", "KARMA", "STINK", "GRADE", "QUIET", "BENCH", "ABATE", "FEIGN", "MAJOR", "DEATH", "FRESH", "CRUST", "STOOL", "COLON", "ABASE", "MARRY", "REACT", "BATTY", "PRIDE", "FLOSS", "HELIX", "CROAK", "STAFF", "PAPER", "UNFED", "TRAWL", "TRAWL", "OUTDO", "ADOBE", "CRAZY", "SOWER", "REPAY", "DIGIT", "CRATE", "CLUCK", "SPIKE", "MIMIC", "POUND", "MAXIM", "LINEN", "UNMET", "FLESH", "BOOBY", "FORTH", "FIRST", "STAND", "BELLY", "IVORY", "SEEDY", "PRINT", "YEARN", "DRAIN", "BRIBE", "STOUT", "PANEL", "CRASS", "FLUME", "OFFAL", "AGREE", "ERROR", "SWIRL", "ARGUE", "BLEED", "DELTA", "FLICK", "TOTEM", "WOOER", "FRONT", "SHRUB", "PARRY", "BIOME", "LAPEL", "START", "GREET", "GONER", "GOLEM", "LUSTY", "LOOPY", "ROUND", "AUDIT", "LYING", "GAMMA", "LABOR", "ISLET", "CIVIC", "FORGE", "CORNY", "MOULT", "BASIC", "SALAD", "AGATE", "SPICY", "SPRAY", "ESSAY", "FJORD", "SPEND", "KEBAB", "GUILD", "ABACK", "MOTOR", "ALONE", "HATCH", "HYPER", "THUMB", "DOWRY", "OUGHT", "BELCH", "DUTCH", "PILOT", "TWEED", "COMET", "JAUNT", "ENEMA", "STEED", "ABYSS", "GROWL", "FLING", "DOZEN", "BOOZY", "ERODE", "WORLD", "GOUGE", "CLICK", "BRIAR", "GREAT", "ALTAR", "PULPY", "BLURT", "COAST", "DUCHY", "GROIN", "FIXER", "GROUP", "ROGUE", "BADLY", "SMART", "PITHY", "GAUDY", "CHILL", "HERON", "VODKA", "FINER", "SURER", "RADIO", "ROUGE", "PERCH", "RETCH", "WROTE", "CLOCK", "TILDE", "STORE", "PROVE", "BRING", "SOLVE", "CHEAT", "GRIME", "EXULT", "USHER", "EPOCH", "TRIAD", "BREAK", "RHINO", "VIRAL", "CONIC", "MASSE", "SONIC", "VITAL", "TRACE", "USING", "PEACH", "CHAMP", "BATON", "BRAKE", "PLUCK", "CRAZE", "GRIPE", "WEARY", "PICKY", "ACUTE", "FERRY", "ASIDE", "TAPIR", "TROLL", "UNIFY", "REBUS", "BOOST", "TRUSS", "SIEGE", "TIGER", "BANAL", "SLUMP", "CRANK", "GORGE", "QUERY", "DRINK", "FAVOR", "ABBEY", "TANGY", "PANIC", "SOLAR", "SHIRE", "PROXY", "POINT", "ROBOT", "PRICK", "WINCE", "CRIMP", "KNOLL", "SUGAR", "WHACK", "MOUNT", "PERKY", "COULD", "WRUNG", "LIGHT", "THOSE", "MOIST", "SHARD", "PLEAT", "ALOFT", "SKILL", "ELDER", "FRAME", "HUMOR", "PAUSE", "ULCER", "ULTRA", "ROBIN", "CYNIC", "CAULK", "SHAKE", "SWILL", "TACIT", "OTHER", "THORN", "TROVE", "BLOKE", "VIVID", "SPILL", "CHANT", "CHOKE", "RUPEE", "NASTY", "MOURN", "AHEAD", "BRINE", "CLOTH", "HOARD", "SWEET", "MONTH", "LAPSE", "WATCH", "TODAY", "FOCUS", "SMELT", "TEASE", "CATER", "MOVIE", "ALLOW", "RENEW", "THEIR", "SLOSH", "PURGE", "CHEST", "DEPOT", "EPOXY", "NYMPH", "FOUND", "SHALL", "STOVE", "LOWLY", "TROPE", "FEWER", "SHAWL", "NATAL", "COMMA", "FORAY", "SCARE", "STAIR", "BLACK", "SQUAD", "ROYAL", "CHUNK", "MINCE", "CHEEK", "AMPLE", "FLAIR", "FOYER", "CARGO", "OXIDE", "PLANT", "OLIVE", "INERT", "ASKEW", "HEIST", "SHOWN", "LARVA", "FORGO", "STORY", "HAIRY", "TRAIN", "HOMER", "BADGE", "MIDST", "CANNY", "FARCE", "SLUNG", "TIPSY", "METAL", "YIELD", "DELVE", "BEING", "SCOUR", "GLASS", "GAMER", "SCRAP", "MONEY", "HINGE", "ALBUM", "VOUCH", "ASSET", "TIARA", "CREPT", "BAYOU", "ATOLL", "MANOR", "CREAK", "SHOWY", "PHASE", "FROTH", "DEPTH", "GLOOM", "FLOOD", "TRAIT", "GIRTH", "PIETY", "FLOAT", "DONOR", "ATONE", "PRIMO", "APRON", "BLOWN", "CACAO", "LOSER", "INPUT", "GLOAT", "AWFUL", "BRINK", "SMITE", "BEADY", "RUSTY", "RETRO", "DROLL", "GAWKY", "HUTCH", "PINTO", "LILAC", "SEVER", "FIELD", "FLUFF", "VOICE", "STEAD", "MADAM", "NIGHT", "BLAND", "LIVER", "WEDGE", "WACKY", "FLOCK", "ANGRY", "APHID", "TRYST", "MIDGE", "POWER", "ELOPE", "CINCH", "MOTTO", "STOMP", "UPSET", "BLUFF", "CRAMP", "QUART", "COYLY", "YOUTH", "RHYME", "BUGGY", "ALIEN", "SMEAR", "UNFIT", "PATTY", "CLING", "GLEAN", "LABEL", "HUNKY", "KHAKI", "POKER", "GRUEL", "TWICE", "TWANG", "SHRUG", "TREAT", "MERIT", "WOVEN", "CLOWN", "RUDER", "GAUZE", "CHIEF", "ONSET", "PRIZE", "FUNGI", "CHARM", "GULLY", "INTER", "WHOOP", "TAUNT", "LEERY", "CLASS", "THEME", "LOFTY", "TIBIA", "BOOZE", "ALPHA", "THYME", "PARER", "CHUTE", "STICK", "TRICE", "ALIKE", "SAINT", "GRATE", "ADMIT", "BRISK", "SOGGY", "USURP", "SCALD", "SCORN", "LEAVE", "TWINE", "STING", "BOUGH", "MARSH", "SLOTH", "DANDY", "VIGOR", "HOWDY", "ENJOY", "VALID", "IONIC", "EQUAL", "CATCH", "SPADE", "STEIN", "EXIST", "QUIRK", "DENIM", "GROVE", "SPIEL", "MUMMY", "FAULT", "FOGGY", "FLOUT", "CARRY", "SNEAK", "LIBEL", "WALTZ", "APTLY", "PINEY", "INEPT", "ALOUD", "PHOTO", "DREAM", "BEGIN", "SPELL", "RAINY", "UNITE", "MEDAL", "VALET", "INANE", "MAPLE", "SNARL", "BAKER", "THERE", "GLYPH", "AVERT", "BRAVE", "AXIOM", "PRIME", "DRIVE", "FEAST", "ITCHY", "CLEAN", "HAPPY", "TEPID", "UNDUE", "STUDY", "EJECT", "CHAFE", "TORSO", "ADORE", "WOKEN", "AMBER", "JOUST", "INFER", "BRAID", "KNOCK", "NAIVE", "APPLY", "SPOKE", "USUAL", "RIVAL", "PROBE", "CHORD", "TAPER", "SLATE", "THIRD", "LUNAR", "EXCEL", "AORTA", "POISE", "EXTRA", "JUDGE", "CONDO", "IMPEL", "HAVOC", "MOLAR", "MANLY", "WHINE", "SKIRT", "ANTIC", "LAYER", "SLEEK", "BELIE", "LEMON", "OPERA", "PIXIE", "GRIMY", "SEDAN", "LEAPT", "HUMAN", "KOALA", "SPIRE", "FROCK", "ADOPT", "CHARD", "MUCKY", "ALTER", "BLURB", "MATEY", "ELUDE", "COUNT", "MAIZE", "BEEFY", "WORRY", "FLIRT", "FISHY", "CRAVE", "CROSS", "SCOLD", "SHIRK", "TASTY", "UNLIT"]


def reset():
    global tries
    global answer
    global unused_letters
    global correct_letters
    global misplaced_letters
    tries = 0
    answer = random.choice(possible_answers).strip()
    unused_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]
    correct_letters = []
    misplaced_letters = []
    sleep(1)
    os.system("cls")


unused_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
correct_letters = []
misplaced_letters = []
dictionary = enchant.Dict("en_US")
tries = 0
max_tries = 6
quit_options = ['quit', 'exit', 'q', 'e']
reset()
guess = input("Guess: ")
init()


def change_to_green(string):
    return Fore.GREEN + string + Fore.RESET


def change_to_gray(string):
    return Fore.LIGHTBLACK_EX + string + Fore.RESET


def change_to_yellow(string):
    return Fore.YELLOW + string + Fore.RESET


def print_wordle_guess(guess):
    if guess == answer:
        print(Fore.GREEN + "You Win!!" + Fore.RESET)
        reset()
        return

    for char in guess:
        if char in unused_letters:
            unused_letters.remove(char)

    answer_letters = {}
    for char in answer:
        if char not in answer_letters:
            answer_letters[char] = 1
        else:
            answer_letters[char] += 1

    status = [0, 0, 0, 0, 0]

    for i, char in enumerate(guess):
        if char == answer[i]:
            answer_letters[char] -= 1
            status[i] = 1
            if char not in correct_letters:
                correct_letters.append(char)
            if char in misplaced_letters:
                misplaced_letters.remove(char)

    for i, char in enumerate(guess):
        if char in answer and status[i] == 0 and answer_letters[char] > 0:
            answer_letters[char] -= 1
            status[i] = 2
            if char not in misplaced_letters and char not in correct_letters:
                misplaced_letters.append(char)
    return status


while guess.lower() not in quit_options:
    flush = False
    if guess == "restart":
        reset()
        guess = input("Guess: ")
        continue
    elif guess == "answer":
        print(answer)
    elif len(guess) != 5:
        print("Guess must only be five letters")
    elif not dictionary.check(guess):
        print("Not a real word")
    elif tries > max_tries - 2:
        print(f"You Lost :( answer was {answer}")
        reset()
        guess = input("Guess: ")
        continue
    else:
        status = print_wordle_guess(guess.upper())
        if not status:
            guess = input("Guess: ")
            continue
        if len(unused_letters) < 26:
            print("Unused letters: " + change_to_gray(" ".join(unused_letters)))
        if len(correct_letters) > 0:
            print("Correct letters: " + change_to_green(" ".join(correct_letters)))
        if len(misplaced_letters) > 0:
            print("Misplaced letters: " + change_to_yellow(" ".join(misplaced_letters)))
        for i, char in enumerate(guess):
            char_status = status[i]
            char = char.upper()
            match char_status:
                case 0:
                    print(change_to_gray(char), end="")
                case 1:
                    print(change_to_green(char), end="")
                case 2:
                    print(change_to_yellow(char), end="")

        print()
        tries += 1

    guess = input("Guess: ")
