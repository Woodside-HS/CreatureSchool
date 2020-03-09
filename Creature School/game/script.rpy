# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("...")
define player = Character("[pfn]")
define lea = Character("Léa")
define doe = Character("Ms. Doeman")
define ire = Character("Irene")

#character images

image lea_def = "lea_default.png"
image lea_hap = "lea_happy.png"
image doe_def = "ms.doeman.png"
image ire_def = "irene_def.png"
image ire_sigh = "irene_sigh.png"

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
image classroom = "classroom.png"
image kitch = "kitchen.png"
image lt_pizza = "lt_pizza.png"
image lt_miso = "lt_miso.png"
image lt_cereal = "lt_cereal.png"
image lt_toast = "lt_toast.png"

#money and skills
default money = 400
default cooking = 0
default repair = 0
default gaming = 0
default art = 0
default writing = 0
default strength = 0

#creative stats
default found_site = False
default poems_written = 0
default poems_published = 0
default ss_written = 0
default ss_published = 0
default art_made = 0
default art_published = 0

#character relationship level
default lea_lev = 1
default irene_lev = 1

#cellphone
default lea_num = False
default irene_num = False
default texted_lea = False

#special booleans
default beento_sde = False

#time and day
default time = "morning"
default day = "Monday"

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
#screen phone():
    #imagebutton:
        #idle "phone.png"
        #hover "phone.png"
        #xpos 100 ypos 100
        #action Jump("test")
image phone = "phone.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #introduction

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
            player "{i}I decided to leave my dorm room to explore the campus some more.{/i}"
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
            $ss_written += 1
            narrator "{i}You increased your writing skill!{/i}"

        "Draw something":
            player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
            $art += 1
            $art_made +=1
            narrator "{i}You increased your art skill!{/i}"

        "Play a computer game.":
            player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
            $gaming += 1
            narrator "{i}You increased your gaming skill!{/i}"

    scene dorm_night_off

    player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"

    show screen control()

    scene dorm_day

    narrator "{i}First day of school - Monday.{/i}"

    player "{i}I looked at the clock, and realized I had five minutes before my first class started! I didn't want to be late so I got dressed quickly and left the building without eating anything.{/i}"

    scene class_welc

    player "{i}I managed to get to class and sit down in the one empty seat in the front row in the nick of time{/i}."

    show doe_def

    doe "Welcome to Creature Literature I! I'm Ms. Doeman and my favorite book is {i}Human-Half{/i} by Giras Meese."

    player "{i}She made no haste lecturing us away about her expectations of us and what we are expected to accomplish this school year.{/i}"

    player "{i}She leisurely passed out the class syllabus, all the while still speaking to us.{/i}"

    player "{i}In perfect sync, Ms. Doeman said her last word just as she handed the last piece of sheet to the student right next to the window in the very back.{/i}"

    hide doe_def
    show ire_sigh

    player "{i}She sighed, seeming unhappy to be in class to say the least.{/i}"

    hide ire_sigh
    show doe_def

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

    player "And [fb] is my favorite book."

    doe "Thank you, [pfn]. And welcome to the class! The student next to [pfn], it's your turn!"

    player "{i}Just about every student went around introudcing themselves. Then it was that student in the back's turn.{/i}"

    hide doe_def
    show ire_def

    player "{i}She was looking out of the window, not paying any mind to what was going on at all.{/i}"

    hide ire_def
    show doe_def

    doe "Hello? Are you there? Please introduce yourself!"

    hide doe_def
    show ire_def

    ire "..."

    hide ire_def
    show ire_sigh

    player "She sighed once more. Reluctantly giving in to unethustiastically respond."

    ire "Irene. She/her. Don't have a favorite book."

    hide ire_sigh
    show doe_def

    player "{i}Ms. Doeman stared blankly at Irene for a moment, probably a little taken aback at her response so laced with upset as compared to the other students.{/i}"

    player "{i}She looked at the clock across the room. It read as 10:59.{/i}"

    doe "Well, we got to everyone! That's all for today, I'll see you again on Wednesday. I hope the rest of your classes go well!"

    menu:
        "{i}It's lunch time (a pretty early lunch time too), what should I do?{/i}"

        "Buy lunch from the cafeteria. {i}This action will cost $10{/i}":
            menu:
                "{i}What should I get?{/i}"

                "Pizza":
                    scene lt_pizza
                    player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                    player "{i}To be honest, it was pretty delicious!{/i}"

                "Miso soup":
                    scene lt_miso
                    player "{i}Today, it was miso soup for me!{/i}"
                    player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

            $money -= 10
            jump afternoon_class

        "Cook something in the dorm building kitchen.":
            scene kitch


    menu:
        "{i}What shall I cook?{/i}"

        "Make instant ramen":
            player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
            player "{i}Once they were done, I poured everything into a bowl.{/i}"
            player "{i}It was pretty tasty.{/i}"
            $cooking += 1
            narrator "{i}You increased your cooking skill!{/i}"

        "Get cereal with milk":
            player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
            player "{i}This made my breakfast quick and easy.{/i}"
            narrator "{i}You did not increase your cooking skill.{/i}"

        "Make spaghetti and meatballs" if cooking >= 1:
            player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
            player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
            $cooking += 2
            narrator "{i}You increased your cooking skill!{/i}"


    player "{i}After lunch, it was time to head to my afternoon classes.{/i}"
    scene classroom
    player "{i}They went on as classes usually do.{/i}"

label to_do:
    menu:
        "{i}What shall I do?{/i}"

        "Go for a run.":
            player "{i}I decided to jog a bit around campus.{/i}"
            scene wp
            player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
            player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

            menu:
                "{i}Do I go back to my dorm or go down this path?{/i}"

                "Go back to the dorms":
                    player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                    $strength += 2
                    narrator "{i}You increased your strength skill!{/i}"

                "Take the other path" if beento_sde == False:
                    player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                    scene sde
                    player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                    player "{i}The path still goes over this hill so I continued walking.{/i}"
                    player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                    player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                    player "{i}Any star-gazer would be really happy to find this place.{/i}"
                    player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                    $beento_sde = True
                    $strength += 5

                "Go up to the hill again" if beento_sde == True:
                    player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                    player "{i}So I just had to go.{/i}"
                    scene sde
                    player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                    player "{i}After some time, I headed back to my dorm.{/i}"
                    $strength += 5

        "Read a cookbook.":
            scene dorm_day
            player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
            $cooking += 1
            narrator "{i}You increased your cooking skill!{/i}"

        "Write a short story.":
            scene dorm_day
            player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
            $writing += 1
            $ss_written += 1
            narrator "{i}You increased your writing skill!{/i}"

        "Draw something":
            scene dorm_day
            player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
            $art += 1
            $art_made += 1
            narrator "{i}You increased your art skill!{/i}"

        "Play a computer game.":
            scene dorm_day
            player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
            $gaming += 1
            narrator "{i}You increased your gaming skill!{/i}"

        "Text Léa." if texted_lea == False:
            show phone
            if lea_lev == 1:
                player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                lea "Hi!"
                player "{i}Wow, that was fast!{/i}"
                lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                lea "Take your time to decide!"
                $texted_lea = True
                jump to_do

    player "{i}Dinner time was approaching.{/i}"
    menu:
        "{i}What shall I do for dinner?{/i}"

        "Buy dinner from the cafeteria. {i}This action will cost $10{/i}":
            menu:
                "{i}What should I get?{/i}"

                "Pizza":
                    scene lt_pizza
                    player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                    player "{i}To be honest, it was pretty delicious!{/i}"

                "Miso soup":
                    scene lt_miso
                    player "{i}Today, it was miso soup for me!{/i}"
                    player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

            $money -= 10
            jump evening_activity

        "Cook something in the dorm building kitchen.":
            scene kitch


    menu:
        "{i}What shall I cook?{/i}"

        "Make instant ramen":
            player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
            player "{i}Once they were done, I poured everything into a bowl.{/i}"
            player "{i}It was pretty tasty.{/i}"
            $cooking += 1
            narrator "{i}You increased your cooking skill!{/i}"

        "Get cereal with milk":
            player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
            player "{i}This made my breakfast quick and easy.{/i}"
            narrator "{i}You did not increase your cooking skill.{/i}"

        "Make spaghetti and meatballs" if cooking >= 1:
            player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
            player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
            $cooking += 2
            narrator "{i}You increased your cooking skill!{/i}"

label evening_activity:
    menu:
        "{i}What shall I do?{/i}"

        "Go for a run.":
            player "{i}I decided to jog a bit around campus.{/i}"
            scene wp
            player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
            player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

            menu:
                "{i}Do I go back to my dorm or go down this path?{/i}"

                "Go back to the dorms":
                    player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                    $strength += 2
                    narrator "{i}You increased your strength skill!{/i}"

                "Take the other path" if beento_sde == False:
                    player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                    scene sde
                    player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                    player "{i}The path still goes over this hill so I continued walking.{/i}"
                    player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                    player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                    player "{i}Any star-gazer would be really happy to find this place.{/i}"
                    player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                    $beento_sde = True
                    $strength += 5

                "Go up to the hill again" if beento_sde == True:
                    player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                    player "{i}So I just had to go.{/i}"
                    scene sde
                    player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                    player "{i}After some time, I headed back to my dorm.{/i}"
                    $strength += 5

        "Read a cookbook.":
            scene dorm_day
            player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
            $cooking += 1
            narrator "{i}You increased your cooking skill!{/i}"

        "Write a short story.":
            scene dorm_day
            player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
            $writing += 1
            $ss_written += 1
            narrator "{i}You increased your writing skill!{/i}"

        "Draw something":
            scene dorm_day
            player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
            $art += 1
            $art_made += 1
            narrator "{i}You increased your art skill!{/i}"

        "Play a computer game.":
            scene dorm_day
            player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
            $gaming += 1
            narrator "{i}You increased your gaming skill!{/i}"

        "Text Léa." if texted_lea == False:
            show phone
            if lea_lev == 1:
                player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                lea "Hi!"
                player "{i}Wow, that was fast!{/i}"
                lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                lea "Take your time to decide!"
                $texted_lea = True


    scene dorm_night_off

    player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"

    jump Tuesday


    #Monday

    label Tuesday:
        $ day = "Tuesday"
        scene dorm_day

        menu:
            "{i}Should I wake up now or sleep some more?{/i}"

            "Wake up":
                menu:
                    "{i}What should I do?{/i}"

                    "Cook":
                        scene kitch
                        menu:
                            "{i}What shall I cook?{/i}"

                            "Make instant ramen":
                                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                                player "{i}It was pretty tasty.{/i}"
                                $cooking += 1
                                narrator "{i}You increased your cooking skill!{/i}"

                            "Get cereal with milk":
                                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                                player "{i}This made my breakfast quick and easy.{/i}"
                                narrator "{i}You did not increase your cooking skill.{/i}"

                            "Make spaghetti and meatballs" if cooking >= 1:
                                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                                $cooking += 2
                                narrator "{i}You increased your cooking skill!{/i}"

                    "Buy breakfast from the cafeteria {i}(This action will cost $5){/i}":
                        menu:
                            "{i}What should I get?{/i}"

                            "Cereal with milk":
                                scene lt_cereal
                                player "{i}I decided to buy a cereal bowl with milk in it.{/i}"
                                player "{i}It's high quality so it tastes a lot better than your generic boxed-cereal!{/i}"

                            "Egg on Toast":
                                scene lt_toast
                                player "{i}Egg on toast, today!{/i}"
                                player "{i}It was a really nice dish, the egg and the bread mixed really well together.{/i}"
                        $money -= 5



                    "Write a poem":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                                player "{i}I'm not sure what to make of this poem but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                                player "{i}This poem was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                                player "{i}My writing has been progressing and those efforts were reflected in my poem. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my poem was out there, ready for the world to see.{/i}"

                                    $poems_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"

                        $poems_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Write a short story":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                            player "{i}I'm not sure what to make of this little story but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                            player "{i}This story was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                            player "{i}My writing has been progressing and those efforts were reflected in my short story. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my short story was out there, ready for the world to see.{/i}"

                                        $ss_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $ss_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Draw something":
                        player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"

                        if art == 0:
                            player "{i}The drawing itself may have not been that great, but that didn't really matter because I had fun.{/i}"

                        if art == 1:
                            player "{i}This was all right.{/i}"

                        if art == 2:
                            player "{i}It seemed as thougth every time I picked up the canvas, I got better.{/i}"

                        else:
                            player "{i}This was a delight to look at and I found it very meaningful.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers looked at my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my piece onto the site and with the press of a couple of buttons, my art was out there, ready for the world to see.{/i}"

                                        $art_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $art_made += 1
                        $art += 1
                        narrator "{i}You increased your art skill!{/i}"

                    "Play a computer game.":
                        player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                        $gaming += 1
                        narrator "{i}You increased your gaming skill!{/i}"

            "Sleep some more":
                player "{i}I decided that it wasn't time for me to get up quite yet so I slept for probably another hour or so before finally waking up and getting out of bed.{/i}"

        player "{i}It was time to head to class.{/i}"

        scene classroom
        player "{i}Class went on as classes usually do.{/i}"

        menu:
            "{i}It's lunch time (a pretty early lunch time too), what should I do?{/i}"

            "Buy lunch from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump afternoon_class

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"


        player "{i}After lunch, it was time to head to my afternoon classes.{/i}"
        scene classroom
        player "{i}They went on as classes usually do.{/i}"

    label to_do_tuesday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True
                    jump to_do_tuesday

        player "{i}Dinner time was approaching.{/i}"
        menu:
            "{i}What shall I do for dinner?{/i}"

            "Buy dinner from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump evening_activity

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"

    label evening_activity_tuesday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True


        scene dorm_night_off

        player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"


    label Wednesday:
        $ day = "Wednesday"
        scene dorm_day

        menu:
            "{i}Should I wake up now or sleep some more?{/i}"

            "Wake up":
                menu:
                    "{i}What should I do?{/i}"

                    "Cook":
                        scene kitch
                        menu:
                            "{i}What shall I cook?{/i}"

                            "Make instant ramen":
                                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                                player "{i}It was pretty tasty.{/i}"
                                $cooking += 1
                                narrator "{i}You increased your cooking skill!{/i}"

                            "Get cereal with milk":
                                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                                player "{i}This made my breakfast quick and easy.{/i}"
                                narrator "{i}You did not increase your cooking skill.{/i}"

                            "Make spaghetti and meatballs" if cooking >= 1:
                                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                                $cooking += 2
                                narrator "{i}You increased your cooking skill!{/i}"

                    "Buy breakfast from the cafeteria {i}(This action will cost $5){/i}":
                        menu:
                            "{i}What should I get?{/i}"

                            "Cereal with milk":
                                scene lt_cereal
                                player "{i}I decided to buy a cereal bowl with milk in it.{/i}"
                                player "{i}It's high quality so it tastes a lot better than your generic boxed-cereal!{/i}"

                            "Egg on Toast":
                                scene lt_toast
                                player "{i}Egg on toast, today!{/i}"
                                player "{i}It was a really nice dish, the egg and the bread mixed really well together.{/i}"
                        $money -= 5



                    "Write a poem":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                                player "{i}I'm not sure what to make of this poem but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                                player "{i}This poem was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                                player "{i}My writing has been progressing and those efforts were reflected in my poem. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my poem was out there, ready for the world to see.{/i}"

                                    $poems_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"

                        $poems_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Write a short story":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                            player "{i}I'm not sure what to make of this little story but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                            player "{i}This story was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                            player "{i}My writing has been progressing and those efforts were reflected in my short story. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my short story was out there, ready for the world to see.{/i}"

                                        $ss_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $ss_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Draw something":
                        player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"

                        if art == 0:
                            player "{i}The drawing itself may have not been that great, but that didn't really matter because I had fun.{/i}"

                        if art == 1:
                            player "{i}This was all right.{/i}"

                        if art == 2:
                            player "{i}It seemed as thougth every time I picked up the canvas, I got better.{/i}"

                        else:
                            player "{i}This was a delight to look at and I found it very meaningful.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers looked at my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my piece onto the site and with the press of a couple of buttons, my art was out there, ready for the world to see.{/i}"

                                        $art_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $art_made += 1
                        $art += 1
                        narrator "{i}You increased your art skill!{/i}"

                    "Play a computer game.":
                        player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                        $gaming += 1
                        narrator "{i}You increased your gaming skill!{/i}"

            "Sleep some more":
                player "{i}I decided that it wasn't time for me to get up quite yet so I slept for probably another hour or so before finally waking up and getting out of bed.{/i}"

        player "{i}It was time to head to class.{/i}"

        scene classroom
        player "{i}Class went on as classes usually do.{/i}"

        menu:
            "{i}It's lunch time (a pretty early lunch time too), what should I do?{/i}"

            "Buy lunch from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump afternoon_class

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"


        player "{i}After lunch, it was time to head to my afternoon classes.{/i}"
        scene classroom
        player "{i}They went on as classes usually do.{/i}"

    label to_do_wednesday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True
                    jump to_do_wednesday

        player "{i}Dinner time was approaching.{/i}"
        menu:
            "{i}What shall I do for dinner?{/i}"

            "Buy dinner from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump evening_activity

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"

    label evening_activity_wednesday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True


        scene dorm_night_off

        player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"

    label Thursday:
        $ day = "Thursday"
        scene dorm_day

        menu:
            "{i}Should I wake up now or sleep some more?{/i}"

            "Wake up":
                menu:
                    "{i}What should I do?{/i}"

                    "Cook":
                        scene kitch
                        menu:
                            "{i}What shall I cook?{/i}"

                            "Make instant ramen":
                                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                                player "{i}It was pretty tasty.{/i}"
                                $cooking += 1
                                narrator "{i}You increased your cooking skill!{/i}"

                            "Get cereal with milk":
                                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                                player "{i}This made my breakfast quick and easy.{/i}"
                                narrator "{i}You did not increase your cooking skill.{/i}"

                            "Make spaghetti and meatballs" if cooking >= 1:
                                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                                $cooking += 2
                                narrator "{i}You increased your cooking skill!{/i}"

                    "Buy breakfast from the cafeteria {i}(This action will cost $5){/i}":
                        menu:
                            "{i}What should I get?{/i}"

                            "Cereal with milk":
                                scene lt_cereal
                                player "{i}I decided to buy a cereal bowl with milk in it.{/i}"
                                player "{i}It's high quality so it tastes a lot better than your generic boxed-cereal!{/i}"

                            "Egg on Toast":
                                scene lt_toast
                                player "{i}Egg on toast, today!{/i}"
                                player "{i}It was a really nice dish, the egg and the bread mixed really well together.{/i}"
                        $money -= 5



                    "Write a poem":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                                player "{i}I'm not sure what to make of this poem but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                                player "{i}This poem was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                                player "{i}My writing has been progressing and those efforts were reflected in my poem. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my poem was out there, ready for the world to see.{/i}"

                                    $poems_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"

                        $poems_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Write a short story":
                        player "{i}I brought out all of my writing supplies and pondered what I should write about.{/i}"
                        player "{i}Soon after, the idea came into mind and I started writing away.{/i}"

                        if writing == 0:
                            player "{i}I'm not sure what to make of this little story but I couldn't unwrite now, could I? I had fun during the process which was I guess what always mattered most.{/i}"

                        if writing == 1:
                            player "{i}This story was pretty fun to write. It didn't turn out too bad I don't think.{/i}"

                        if writing == 2:
                            player "{i}My writing has been progressing and those efforts were reflected in my short story. Maybe I could be a published writer one day.{/i}"

                        else:
                            player "{i}This poem was pleasing to read and the sentences were rhymatic and flowed really well.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers read my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my writing onto the site and with the press of a couple of buttons, my short story was out there, ready for the world to see.{/i}"

                                        $ss_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $ss_written += 1
                        $writing +=1
                        narrator "{i}You increased your writing skill.{/i}"

                    "Draw something":
                        player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"

                        if art == 0:
                            player "{i}The drawing itself may have not been that great, but that didn't really matter because I had fun.{/i}"

                        if art == 1:
                            player "{i}This was all right.{/i}"

                        if art == 2:
                            player "{i}It seemed as thougth every time I picked up the canvas, I got better.{/i}"

                        else:
                            player "{i}This was a delight to look at and I found it very meaningful.{/i}"
                            menu:
                                "Publish it?"

                                "Yes":
                                    if found_site = False:
                                        player "{i}A quick internet search led me to a website where I could publish my work{/i}"
                                        player "{i}and if I connected my Art is Working account to this site, then I would be recieving weekly paymet depending on how many viewers looked at my stuff.{/i}"
                                        $found_site = True


                                    if found_site = True:
                                        player "{i}I logged onto the publishing site.{/i}"
                                        player "{i}I uploaded my piece onto the site and with the press of a couple of buttons, my art was out there, ready for the world to see.{/i}"

                                        $art_published += 1

                                "No":
                                    player "{i}Eh. I wasn't sure I was ready for the world to see my work yet.{/i}"
                        $art_made += 1
                        $art += 1
                        narrator "{i}You increased your art skill!{/i}"

                    "Play a computer game.":
                        player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                        $gaming += 1
                        narrator "{i}You increased your gaming skill!{/i}"

            "Sleep some more":
                player "{i}I decided that it wasn't time for me to get up quite yet so I slept for probably another hour or so before finally waking up and getting out of bed.{/i}"

        player "{i}It was time to head to class.{/i}"

        scene classroom
        player "{i}Class went on as classes usually do.{/i}"

        menu:
            "{i}It's lunch time (a pretty early lunch time too), what should I do?{/i}"

            "Buy lunch from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump afternoon_class

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"


        player "{i}After lunch, it was time to head to my afternoon classes.{/i}"
        scene classroom
        player "{i}They went on as classes usually do.{/i}"

    label to_do_thursday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True
                    jump to_do_thursday

        player "{i}Dinner time was approaching.{/i}"
        menu:
            "{i}What shall I do for dinner?{/i}"

            "Buy dinner from the cafeteria. {i}This action will cost $10{/i}":
                menu:
                    "{i}What should I get?{/i}"

                    "Pizza":
                        scene lt_pizza
                        player "{i}I decided to buy a slice of pizza and it came with a drink.{/i}"
                        player "{i}To be honest, it was pretty delicious!{/i}"

                    "Miso soup":
                        scene lt_miso
                        player "{i}Today, it was miso soup for me!{/i}"
                        player "{i}I didn't have much else to say other than that the soup was very tasty!{/i}"

                $money -= 10
                jump evening_activity

            "Cook something in the dorm building kitchen.":
                scene kitch


        menu:
            "{i}What shall I cook?{/i}"

            "Make instant ramen":
                player "{i}I boiled a couple of cups of water then plopped the noodles in.{/i}"
                player "{i}Once they were done, I poured everything into a bowl.{/i}"
                player "{i}It was pretty tasty.{/i}"
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Get cereal with milk":
                player "{i}The task of getting cereal and pouring milk on it was easy.{/i}"
                player "{i}This made my breakfast quick and easy.{/i}"
                narrator "{i}You did not increase your cooking skill.{/i}"

            "Make spaghetti and meatballs" if cooking >= 1:
                player "{i}I laid out all the ingredients I found from the various cupbords and set to work.{/i}"
                player "{i}The result was a delicious and nutritious bunch of noodles topped with rich marinara sauce and savory meatballs.{/i}"
                $cooking += 2
                narrator "{i}You increased your cooking skill!{/i}"

    label evening_activity_thursday:
        menu:
            "{i}What shall I do?{/i}"

            "Go for a run.":
                player "{i}I decided to jog a bit around campus.{/i}"
                scene wp
                player "{i}Running around at my own pace has felt fantastic and I couldn't be gladder to get the exercise.{/i}"
                player "{i}On my way back from the library to the dorms, I came across a curious split in the path.{/i}"

                menu:
                    "{i}Do I go back to my dorm or go down this path?{/i}"

                    "Go back to the dorms":
                        player "{i}I decided that I've had enough walking around for today, so I headed back to my room.{/i}"
                        $strength += 2
                        narrator "{i}You increased your strength skill!{/i}"

                    "Take the other path" if beento_sde == False:
                        player "{i}I was feeling adventurous, so I thought taking this unfamilar path was a good idea.{/i}"
                        scene sde
                        player "{i}After what seemed to be a long walk on a flat, level path, I came across a hill.{/i}"
                        player "{i}The path still goes over this hill so I continued walking.{/i}"
                        player "{i}To my surprise, the path stopped on the very top of the hill.{/i}"
                        player "{i}However, I looked up and saw that the skies were clearer than I've ever seen before.{/i}"
                        player "{i}Any star-gazer would be really happy to find this place.{/i}"
                        player "{i}Realizing how dark it had gotten, I turned around to head back to my dorm.{/i}"
                        $beento_sde = True
                        $strength += 5

                    "Go up to the hill again" if beento_sde == True:
                        player "{i}I could feel that mountain where I could see thousands of stars clearly call to me.{/i}"
                        player "{i}So I just had to go.{/i}"
                        scene sde
                        player "{i}I walked up to the hill's peak, taking in the gorgeous scene on the night sky.{/i}"
                        player "{i}After some time, I headed back to my dorm.{/i}"
                        $strength += 5

            "Read a cookbook.":
                scene dorm_day
                player "{i}I spent a few hours looking through a variety of different recipes. Maybe I should try making all of these sooner or later."
                $cooking += 1
                narrator "{i}You increased your cooking skill!{/i}"

            "Write a short story.":
                scene dorm_day
                player "{i}I pulled out all my writing materials and got busy writing a short story. I don't know whether it turned out okay or not but that was fun!{/i}"
                $writing += 1
                $ss_written += 1
                narrator "{i}You increased your writing skill!{/i}"

            "Draw something":
                scene dorm_day
                player "{i}I got all my art tools out and started drawing. After what seemed to be hours, I'm finally finished with my latest piece. Whew!{/i}"
                $art += 1
                $art_made += 1
                narrator "{i}You increased your art skill!{/i}"

            "Play a computer game.":
                scene dorm_day
                player "{i}I booted up my computer and the game of my choice. The moment I clicked the play button, everything else was a blur, kind of."
                $gaming += 1
                narrator "{i}You increased your gaming skill!{/i}"

            "Text Léa." if texted_lea == False:
                show phone
                if lea_lev == 1:
                    player "{i}I had her number so I thought to shoot her a quick text greeting her and letting her know it was me.{/i}"
                    lea "Hi!"
                    player "{i}Wow, that was fast!{/i}"
                    lea "If you're still down to go shopping with me, let's meet up after class on Friday?"
                    lea "Take your time to decide!"
                    $texted_lea = True


        scene dorm_night_off

        player "{i}Before I knew it, the sky got darker and I had gotten very sleepy.{/i}"


        #Friday

        #Saturday

        #Sunday





    # This ends the game.

    return
