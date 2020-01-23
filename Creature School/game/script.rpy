# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("...")
define player = Character("[pfn]")
define lea = Character("Léa")

#character images

image lea_def = "lea_default.png"
image lea_hap = "lea_happy.png"

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
image d_door = "dorm_door.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene monsters

    # These display lines of dialogue.

    narrator "{i}My mom always told me stories of encounters with creatures everyone else thought were just mere figments of millennia-old human imagination.{/i}"

    narrator "{i}I myself always oscillated between believing her and dismissing her stories as silly.{/i}"

    scene myana

    narrator "{i}But,{/i}"

    narrator "{i}her stories are completely true.{/i}"

    narrator "{i}At age 10, I saw for myself that monsters are real when my parents turned on the TV for the latest scope by Unbelieveably Real News.{/i}"

    narrator "{i}Myana Aditi, a well-known celebrity dating Blyke Riley, suddenly grew whiskers,{/i}"

    narrator "{i}her nose became that of a feline's, and she took off her hat to reveal two very soft-looking cat ears with a long tail to boot.{/i}"

    narrator "{i}My dad and I thought there was some film witchcraft going on behind the scenes but my mom was grinning at the TV screen.{/i}"

    narrator "{i}'I told you so,' she said.{/i}"

    scene deal

    narrator "{i}It turns out that the human government and the other-species government of our country made a deal a few centuries back.{/i}"

    narrator "{i}For the longest time, it was prohibited for an other-species to walk around in human areas wihtout first disgusing themself as a human.{/i}"

    narrator "{i}Other-species also had to hide their town and cities from human eyes with magic and news about them were to never mix with our own.{/i}"

    narrator "{i}If a human ending up encountering an other-species in their natural state or somehow walked into their town, they have two choices:{/i}"

    narrator "{i}1) to be deported from the town and have their memory wiped{/i}"

    narrator "{i}or in rare cases, 2) to make a legal contract with a local governor that allows the human to enter and leave other-species towns freely but anticipate severe punishment should they betray the secrets of other-species.{/i}"

    narrator "{i}Mom always thought these restrictions were silly because they didn't exist in her home country so the monsters and people could learn to live together in harmony.{/i}"

    narrator "{i}In any case, after Myana's rebellious show, the two authorities decided to abolish this deal once and for all and replace it with a new one.{/i}"

    narrator "{i}It is the Merger Act: Everyone is allowed to mingle and co-exist in each other's worlds and our leaders will work together to maintain peace and order between the various species.{/i}"

    scene schoolsign

    narrator "{i}I'm going to start high school soon and I've chosen to attend Florce Academy, a private school boasting over a century's worth of pride in teaching monster students and only monster students.{/i}"

    narrator "{i}However, since the passing of the Merger Act, human students were welcome to attend as well.{/i}"

    narrator "{i}The Florce student-body has been mostly other-species even in these recent years, so the headmaster reached out to my parents and offered me a scholarship with admission.{/i}"

    scene application

    narrator "{i}Dad is a bit apprehensive about me going to a school made of mostly monster students, but mom is ecstatic.{/i}"

    narrator "{i}I've made my decision and all I need to do now is fill out this application form.{/i}"

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

    player "{i}This is [pfn] [pmn] [pln]. [sfc] [verb] going to Florce Academy. Okay, now let's see what the rest of this application is asking me.{/i}"

    scene schoolsign

    narrator "{i}A week before school starts.{/i}"

    show lea_def

    player "{i}I'm stepping onto the really beautiful but kinda overwhelmingly large campus. Hey, there's a girl standing by the sign! Perhaps she can help.{/i}"

    lea "Hi there! Are you a freshman?"

    player "Yeah. I'm a bit lost. Any chance you can show me around?"

    hide lea_def
    show lea_hap

    lea "Totally!"

    hide lea_hap
    show lea_def

    lea "We should stop by your dorm first to take off that heavy load you're carrying. What's your dorm number?"

    player "8."

    lea "I know exactly where that is. Follow me!"

    player "{i}I follow the girl to a building several hundred feet away from the school entrance. We step inside.{/i}"

    scene d_door

    player "{i}The carpetted floor is colored like grass and I'm sure it feels like it, too. The walls are painted a pleasing mix of blue and white to look like a cloudy sky.{/i}"

    player "{i}It feels like I'm walking through a plains field on a warm day.{/i}"

    hide lea_def

    show lea_hap

    lea "Here we are! Your very own dorm room!"

    lea "No roomates to share it with, but don't worry, if you get lonely you can always talk to your neighbors or come and find me!"

    hide lea_hap
    show lea_def

    lea "Speaking of me, I forgot to properly introduce myself didn't I?"

    player "Well, I'm [pfn]. Pleasure to meet you!"

    lea "Likewise! I'm Léa!"

    # This ends the game.

    return
