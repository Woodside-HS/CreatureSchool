# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("...")
define player = Character("[pfn]")
define lea = Character("Léa")
define doe = Character("Ms. Doeman")

#character images

image lea_def = "lea_default.png"
image lea_hap = "lea_happy.png"
image doe_def = "ms.doeman.png"

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
image dorm_day = "dorm_d.png"
image dorm_night_on = "dorm_n_lon.png"
image dorm_night_off = "dorm_n_loff.png"
image wp = "walking_path.png"
image sde = "starry_dead_end.png"
image class_welc = "classroom_welc.png"

#money and skills
default money = 400
default cooking = 0
default repair = 0
default gaming = 0
default art = 0
default writing = 0
default strength = 0

#character relationship level
default lea_lev = 1
default irene_lev = 2

#cellphone
default lea_num = False
default irene_num = False

#special booleans
default beento_sde = False

#This is your control screen that will allow you to show/hide the stat screen
screen control():
    frame:
        xalign 0.95
        yalign 2
        textbutton "Stats" action If(renpy.get_screen("stat_box"), Hide("stat_box"), Show("stat_box"))

#This is your stat_box Screen
screen stat_box():
    frame:
        align (0.5,0.5)
        vbox:
            text "Money: [money]"
            text "Cooking: [cooking]"
            text "Repair: [repair]"
            text "Gaming: [gaming]"
            text "Art: [art]"
            text "Writing: [writing]"
            text "Strength: [strength]"

#phone
screen phone():
    imagebutton:
        idle "phone.png"
        hover "phone.png"
        xpos 100 ypos 100
        action Jump("test")


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

    player "{i}The two of us stand awkwardly for a moment.{/i}"

    lea "Well, what are you waiting for, come inside!"

    hide lea_def
    show lea_hap

    lea "I'll even help you with your stuff!"

    scene dorm_day

    show lea_def

    lea "Here we are! This will be your home for the school year. What do you think?"

    menu:
        "Do you like your new dorm?"

        "Really simple and the colors are great. I like it!":
            hide lea_def
            show lea_hap
            lea "That's awesome! I'm sure you'll feel right at home very soon."

            hide lea_hap
            show lea_def

            lea "Still, if you want to decorate your room some more, I'd be happy to go shopping with you sometime."

        "Honestly this dorm could have more decor, but the colors aren't bad.":
            lea "Good thing students can decorate their dorms."

            lea "Ooooooh! We can go shopping for room decor sometime!"

        "I like the more minamilist style going on here, but the colors, dear lord, the colors! Could they get any more plain and somber?.":
            hide lea_def
            show lea_hap

            lea "I know just the solution to balance out these plain and somber colors: decor shopping!!!"

            hide lea_hap
            show lea_def

            lea "Consider going shopping with me sometime, will you?"

        "Is decorating your dorms allowed here?":
            hide lea_def
            show lea_hap

            lea "Totally!! If you don't like the way your room looks right now, you can totally come shopping with me sometime!"

    hide lea_hap
    show lea_def

    lea "Anyway, let me help you with all that!"

    player "{i}Léa helps me put down and put away all of my stuff into the closet and various drawers. The job was done very quickly.{/i}"

    player "Wow! That was fast! Thank you so much for helping me out!"

    hide lea_def
    show lea_hap

    lea "No problem, [pfn]!"

    hide lea_hap
    show lea_def

    lea "Oh! One more thing before you go. Let me give you my number. Your phone please?"

    player "{i} I pull out my phone and give it to Léa. She types in several digits then hands it back to me.{/i}"

    hide lea_def
    show lea_hap

    lea "I'm usually free after school most days and available most weekends! Feel free to call or text me if you need anything and don't be afraid to say hi if we see each other in school!"

    hide lea_hap
    show lea_def

    lea "Well, anyway, I got to go. I'll see you around?"

    player "Totally! See you later, Léa!"

    hide lea_def

    player "{i} Léa left my dorm room. It's still pretty bright out, I could go outside or I could stay inside. Maybe I can read a book or play a video game."

    menu:
        "{i}What should I do?{/i}"

        "Explore the campus some more.":
            player "{i}I decided to leave my dorm room to explore the campus some more{/i}"
            scene wp
            player "{i}I managed to locate the locate my classroom buildings, the cafeteria, and the library along with most of the various restrooms across campus on my walk.{/i}"
            player "{i}On my way back from the library to the dorms, I noticed a curious split in the path.{/i}"

            menu:
                "{i}Do I go back to my dorm or see where this other path takes me?{/i}"

                "Go back to the dorms":
                    player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                    $strength += 1
                    narrator "{i}You increased your strength skill!{/i}"

                "Take the other path":
                    player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                    scene sde
                    player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                    player "{i}The path still goes over this hill so I continued walking.{/i}"
                    player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                    player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                    player "{i}Any star-gazer would be really happy to find this place.{/i}"
                    player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                    $beento_sde = True
                    $strength += 3

        "Read a cookbook.":
            player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
            $cooking += 1
            narrator "{i}You increased your cooking skill!{/i}"

        "Write a short story.":
            player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
            $writing += 1
            narrator "{i}You increased your writing skill!{/i}"

        "Draw something":
            player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
            $art += 1
            narrator "{i}You increased your art skill!{/i}"

        "Play a computer game.":
            player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
            $gaming += 1
            narrator "{i}You increased your gaming skill!{/i}"

    scene dorm_night_off

    player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"

    show screen control()

    #show screen phone()

    scene dorm_day

    narrator "{i}First day of school - Monday.{/i}"

    player "{i}I looked at the clock, and realized I had five minutes before my first class started! I didn't want to be late so I got dressed quickly and left the building without eating anything.{/i}"

    scene class_welc

    player "{i}I managed to get to class and sit down in the one empty seat in the front row in the nick of time{/i}."

    show doe_def

    doe "Welcome to Creature Literature I! I'm Ms. Doe and my favorite book is {i}Human-Half{/i} by Giras Meese."

    doe "Let's introduce ourselves, shall we? State your name, pronouns, and favorite book. You there are going to start."

    player "{i}She points to me.{/i}"

    menu:
        "{i}What's my favorite book?{/i}"

        "{i}Bake with Me{/i} - a book full of recipes and ideas for baking at home.":
            $ fb = "{i}Bake with Me{/i}"

        "{i}2 Strangers, 1 Heart{/i} - a kinda cheesy, kinda trashy romance novel.":
            $ fb = "{i}2 Strangers, 1 Heart{/i}"

        "{i}Shut Down{/i} - a very tragic sci-fi novel.":
            $ fb = "{i}Shut Down{/i}"

    player "Oh, um. Hi, I'm [pfn]. My pronouns are [sfc]/[of]."


    # This ends the game.

    return
