# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("...")
define player = Character("[pfn]")

#pronouns
#sfc = subject form with capital at beginning (She, He, They)
#sfl = subject form in all lowercase (she, he, they)
#pf = possessive form (her, his, their)
#verb (is, are)
#of = object form (her, him, them)

#background images
image monsters = "monsters.png"
image myana = "myana.png"
image deal = "deal.png"
image application = "application.png"
image schoolsign = "schoolsign.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene monsters

    # These display lines of dialogue.

    narrator "My mom always told me stories of encounters with creatures everyone else thought were just mere figments of millennia-old human imagination."

    narrator "I myself always oscillated between believing her and dismissing her stories as silly."

    scene myana

    narrator "But,"

    narrator "her stories are completely true."

    narrator "At age 10, I saw for myself that monsters are real when my parents turned on the TV for the latest scope by Unbelieveably Real News."

    narrator "Myana Aditi, a well-known celebrity dating Blyke Riley, suddenly grew whiskers,"

    narrator "her nose became that of a feline's, and she took off her hat to reveal two very soft-looking cat ears with a long tail to boot."

    narrator "My dad and I thought there was some film witchcraft going on behind the scenes but my mom was grinning at the TV screen."

    narrator "'I told you so,' she said."

    scene deal

    narrator "It turns out that the human government and the other-species government of our country made a deal a few centuries back."

    narrator "For the longest time, it was prohibited for an other-species to walk around in human areas wihtout first disgusing themself as a human."

    narrator "Other-species also had to hide their town and cities from human eyes with magic."

    narrator "If a human ending up encountering an other-species in their natural state or somehow walked into their town, they have two choices:"

    narrator "1) to be deported from the town and have their memory wiped"

    narrator "or in rare cases, 2) to make a legal contract with a local governor that allows the human to enter and leave other-species towns freely but anticipate severe punishment should they betray the secrets of other-species."

    narrator "Mom always thought these restrictions were silly because they didn't exist in her home country so the monsters and people could learn to live together in harmony."

    narrator "In any case, after Myana's rebellious show, the two authorities decided to abolish this deal once and for all and replace it with a new one."

    narrator "It is the Merger Act: Everyone is allowed to mingle and co-exist in each other's worlds and our leaders will work together to maintain peace and order between the various species."

    scene schoolsign

    narrator "I'm going to start high school soon and I've chosen to attend Florce Academy, a private school boasting over a century's worth of pride in teaching monster students and only monster students."

    narrator "However, since the passing of the Merger Act, human students were welcome to attend as well."

    narrator "The Florce student-body has been mostly other-species even in these recent years, so the headmaster reached out to my parents and offered me a scholarship with admission."

    scene application

    narrator "Dad is a bit apprehensive about me going to a school made of mostly monster students, but mom is ecstatic."

    narrator "I've made my decision and all I need to do now is fill out this application form."

    #asking player for name
    #pfn = player first name
    #pmn = player middle name
    #pln = player last name

    python:
        pfn = renpy.input("What is your first name?")
        pfn = pfn.strip()

        if not pfn:
            pfn = "Payton"

        pmn = renpy.input("What is your middle name?")
        pmn = pmn.strip()

        if not pmn:
            pmn = "Dace"

        pln = renpy.input("What is your last name?")
        pln = pln.strip()

        if not pln:
            pln = "Smith"

    menu:
        "What are your pronouns?"

        "They/them":
            $ sfc = "They"
            $ sfl = "they"
            $ verb = "are"
            $ pf = "their"
            $ of = "them"
        "She/her":
            $ sfc = "She"
            $ sfl = "she"
            $ verb = "is"
            $ pf = "her"
            $ of = "her"
        "He/him":
            $ sfc = "He"
            $ sfl = "he"
            $ verb = "is"
            $ pf = "his"
            $ of = "him"

    player "This is [pfn] [pmn] [pln]. [sfc] [verb] going to Florce Academy. Okay, now let's see what the rest of this application has to offer."

    # This ends the game.

    return
