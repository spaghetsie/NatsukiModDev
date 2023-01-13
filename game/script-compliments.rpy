default persistent._compliment_database = dict()

init 0 python in jn_compliments:
    import random
    import store

    COMPLIMENT_MAP = dict()

    # Compliment types
    TYPE_AMAZING = 0
    TYPE_BEAUTIFUL = 1
    TYPE_CONFIDENT = 2
    TYPE_CUTE = 3
    TYPE_HILARIOUS = 4
    TYPE_INSPIRATIONAL = 5
    TYPE_STYLE = 6
    TYPE_THOUGHTFUL = 7

    # The last compliment the player gave to Natsuki
    last_compliment_type = None

    def get_all_compliments():
        """
        Gets all compliment topics which are available

        OUT:
            List<Topic> of compliments which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            COMPLIMENT_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_compliments_start:
    python:
        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in jn_compliments.get_all_compliments()
        ]
        compliment_menu_items.sort()

    call screen scrollable_choice_menu(compliment_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're amazing!",
            label="compliment_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_amazing").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_AMAZING:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 4uskemfesh "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}" 
            extend 1fcsemfsbr " Honestly!{w=0.75}{nw}" 
            extend 4kwmemfsbr " Again?!{w=1}{nw}" 
            extend 4kslpofsbr " Jeez..."
            n 2nslsllsbr "..."
            n 2nslpulsbr "But...{w=0.75}{nw}" 
            extend 1ksqcalsbr " thanks.{w=0.5} It really...{w=0.75}{nw}" 
            extend 4ksrcalsbr " means a lot to me."
            n 4ksqajlsbr "...And [player]?"
            n 1kslbolsbr "..."
            n 2fcstrl "...You're pretty amazing too." 
            n 2fcspol "A-{w=0.2}and you better remember that."

            if Natsuki.isLove(higher=True):
                n 2kchssleaf "L-{w=0.2}love you,{w=0.2} [player]!"

        else:
            n 1nslsslsbr "Jeez,{w=0.2} [player]...{w=0.5}{nw}"
            extend 1klrbolsbr " you...{w=0.5} really are doling out the compliments today,{w=0.5}{nw}" 
            extend 4ksrsslsbr " huh?"
            n 2fcsajl "D-{w=0.2}don't get me wrong though!{w=0.5}{nw}" 
            extend 2fcsbglsbl " I'm not complaining!"
            extend 2fcssmlsbl " I-{w=0.2}it's good to know we {i}both{/i} agree!"
            extend 4nslsslsbr " Just..."
            n 1ksqbolsbr "Make sure you don't leave yourself out though,{w=0.2} 'kay?"
            n 4kllsslsbr "You're {i}almost{/i} as amazing,{w=0.2} a-{w=0.2}after all."
            n 3fsqdvlsbr "...{i}Almost{/i}."
            extend 3fchbllsbr " Ehehe."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1kwmpul "...Y{w=0.2}-you really think so,{w=0.5}{nw}" 
            extend 1kllpul " [player]?"
            n 4kllsrl "..."
            n 1ncsssl "Heh."
            n 2fslpolsbl "It's always super embarrassing to say it,{w=0.2} you know."
            n 2kslbol "..."
            n 2ncspul "But...{w=0.75}{nw}"
            extend 2kwmbol " thanks."
            n 4fcsajlsbr "It means...{w=0.75}{nw}" 
            extend 1ksrsllsbr " a lot to me,{w=0.5} [player]."
            n 1ksqsllsbr "Really.{w=0.75}{nw}" 
            extend 4ksqbol " Thank you.{w=0.75}{nw}" 
            extend 4kcspul " You're honestly...{w=1}{nw}" 
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            extend 1ksrcal " [chosen_descriptor],{w=0.3} [player]."
            n 1ksrfsl "..."

            if Natsuki.isLove(higher=True):
                n 4kchssf "L-{w=0.2}love you."

        else:
            n 1uskgslesh "O-{w=0.2}oh!{w=0.5}{nw}" 
            extend 4fllbglesssbr " A-{w=0.2}aha!{w=0.5}{nw}" 
            extend 2fcsbglsbr " Well,{w=0.2} I knew you'd {i}have{/i} to admit it {i}eventually{/i}!"
            n 2fcssmlsbl "I'm just glad to hear {i}both{/i} of us agree on that.{w=0.75}{nw}"
            extend 1fsldvlsbl " Ehehe."

            if Natsuki.isAffectionate(higher=True):
                n 3fcsssl "J-{w=0.2}just remember though,{w=0.2} [player]..."
                n 3fchbll "You're at {i}least{/i} second best!"

            else:
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchgnlsbr "Thanks,{w=0.2} [chosen_tease]!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_AMAZING
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're beautiful!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_beautiful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_BEAUTIFUL:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 1fcsanlesssbl "Uuuuuu-!"
            n 4kwdgslesssbl "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 1kbkwrless " You already told me thaaaaat!"
            n 4ksqemlsbr "You really gotta do it {i}again{/i}?!"
            n 2ksrbolsbr "..."
            n 2ncsemlesisbr "..."
            n 1ncsbolsbr "...Fine.{w=0.75}{nw}"
            extend 4kslbolsbl " I'll take it."
            n 2fcscalsbl "The compliment,{w=0.2} I mean.{w=0.75}{nw}"
            extend 2fcstrlsbl " Just..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1ksrcal "..."
            n 4ncsssl "...Heh.{w=1}{nw}"
            extend 4nslfsl " Nevermind."
            
            if Natsuki.isLove(higher=True):
                n 2kslbol "T-{w=0.2}thanks again,{w=0.2} [chosen_tease]."
                n 1kslfsfeaf "...Y-{w=0.2}you always make me feel prettier."

            else:
                n 2kslbol "T-{w=0.2}thanks again,{w=0.2} [chosen_tease]."
                n 1kslcaf "..."

        else:
            n 4fskgslesh "E-{w=0.2}excuse me?!"
            n 1fwmgslsbl "[player]!{w=0.5}{nw}" 
            extend 4fbkwrlsbl " What did {i}literally{/i} just I tell you?!"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcsgsl "Are you {i}trying{/i} to give me a heart attack or something?!{w=0.75}{nw}"
            extend 2fsleml " Sheesh..."
            n 2fslpol "..."
            n 4fcsajl "I-{w=0.2}I mean,{w=0.75}{nw}"
            extend 3fcspol " I know I already look great!{w=1}{nw}"
            extend 3fsrdvlsbl " I {i}always{/i} look top-{w=0.2}notch, o-{w=0.2}of course."
            n 2fcsemlsbl "But you {i}really{/i} don't have to..."
            n 2fslunlsbl "T-{w=0.2}to keep...!"
            n 1fcsunlsbl "..."
            n 4fcsemlsbr "Oh,{w=0.5}{nw}"
            extend 2flrbolsbr " forget it!"

            if Natsuki.isAffectionate(higher=True):
                n 2fcscalsbr "You know what I mean,{w=0.2} a-{w=0.2}anyway..."

            n 2ksrbolsbr "..."

    else:
        if Natsuki.isEnamored(higher=True):
            n 4uskemlesh "H-{w=0.2}huh?!"
            n 1fcseml "Wait..."
            n 1kllemlsbl "Y-{w=0.2}you really think I'm..."
            n 1fslunfsbl "I-{w=0.3}I'm..."
            n 4fcsunfesssbr "..."
            n 2kcsbolsbr "..."
            n 2ksqbolsbr "[player]..."
            n 1kllbolsbr "You {w=0.2}{i}do{/i}{w=0.2} know you're not meant to just say things like that..."
            n 4kwmslfsbl "Unless you really mean them?"

            if Natsuki.isLove(higher=True):
                n 1knmajlsbl "I-{w=0.2}it's not that I don't believe you!{w=1}{nw}"
                extend 2klrsslsbl " O-{w=0.2}of course not!"
                n 4ksrbolsbl "...You should know that by now."
                n 2ksrpulsbl "But..."
                n 4ksrsll "..."
                n 1ksrfsl "...Thanks,{w=0.2} [player].{w=1}{nw}"
                extend 1ksrssl " Really{w=0.2}, heh."
                n 4ksqfsl "Thank you."
                n 3fcssmless "...Just don't forget {i}who{/i} helps me feel that way.{w=0.75}{nw}"
                extend 3fsqbll " You goof."
                n 4fchsmleaf "Ehehe."

            else:
                n 1kslcafsbl "..."
                n 2fcstrlesssbr  "I-{w=0.2}I mean...!"
                n 2nsrsllsbr "...{w=0.75}{nw}"
                extend 2ksrbolsbr "Really."
                n 2ksrfslsbr "T-{w=0.2}thanks, [player]."

        else:
            n 1uskemlesh "W{w=0.2}-w{w=0.2}-what?"
            n 1fskeml "W-{w=0.2}what did you say?!"
            n 4fcsanfsbr "Nnnnnnnnnn-!"
            n 4fbkwrfsbr "Y-{w=0.2}you can't just {i}say{/i} things like that so suddenly!"
            n 2fllemlsbl "Sheesh...{w=0.75}{nw}"
            extend 2fslpolsbl " come on,{w=0.2} [player]..."
            n 1fcsbolsbr "..."
            n 1fcsemlsbr "I-{w=0.2}I mean,{w=0.75}{nw}" 
            extend 3fsrbglsbr " I'm glad we both agree,{w=0.75}{nw}" 
            extend 4fsrunlsbr " but..."
            n 1fcsunlesssbl "Uuuuuu...!"
            n 1fcsemlsbl "Just..." 
            n 1kslcal "..."
            n 2ksqsllsbr "...Think a little before you just blurt stuff out like that.{w=0.75}{nw}"
            extend 2fsrsllsbr " I-{w=0.2}it just makes everything all awkward."
            n 1fsrsslsbr "...Heh.{w=0.75}{nw}"
            extend 4fcsajlsbr " A-{w=0.2}and besides,{w=0.75}{nw}"
            n 3fcsbglsbl " I {i}always{/i} look stunning anyway!{w=0.75}{nw}"
            extend 3nslsslsbl " So...{w=0.5}{nw}" 
            extend 3nslbol " yeah."
            n 3kslsllsbr "..."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_BEAUTIFUL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how confident you are!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_confident").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CONFIDENT:
        n 1fcssmleme "Ehehe.{w=0.5}{nw}"
        extend 2fcsbg " Well,{w=0.2} I'm glad you still agree,{w=0.2} [player]!"
        n 2fllsm "Besides,{w=0.5}{nw}"
        extend 2fcssm " it's only natural."
        
        if Natsuki.isEnamoured(higher=True):
            n 4nslssl "E-{w=0.2}especially with you around,"
            extend 3fchbll " you goof."

        else:
            n 2fcsbg "Full of confidence,{w=0.5}{nw}"
            extend 2flrbs " always unfazed..."
            n 3uchgnl "...That's just what it means to be a pro,{w=0.2} right?"
    
    else:
        n "Oho?{w=1}{nw}"
        extend " I do,{w=0.2} do I?"
        n "Now that's {i}just{/i} what I like to hear!"
        n "After all,{w=0.5}{nw}"
        extend " don't I just radiate confidence?"
        n " Come on,{w=0.2} [player]!{w=0.75}{nw}"
        extend " No need to be shy!{w=0.5}{nw}"
        extend " Is it the eyes?"
        n "The smile?"
        n "The {i}killer{/i} personality?"
        n "Ehehe."
        n "Whatever it is..."
        
        if Natsuki.isLove(higher=True):
            n "..."
            n "I-{w=0.2}I hope I inspire you just as much as you inspire me."
            extend " Ehehe."
            n "L-{w=0.2}love you,{w=0.2} [player]!"

        if Natsuki.isEnamored(higher=True):
            n "I hope I inspire some confidence in you too!"
            n "N-{w=0.2}not that you need it {i}too{/i} much,{w=0.2} a-{w=0.2}anyway."
            n "Y-{w=0.2}you're welcome,{w=0.2} [player]!"

        else:
            n "I hope I inspire some confidence in you too."
            n "You're welcome,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're cute!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_cute").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CUTE:
        if Natsuki.isEnamored(higher=True):
            n 1fskwrl "..."
            n 1fcsanl "..."
            n 1fcsful "..."
            n 1fcsfuf "Urgh!"
            n 1fbkwrf "Alright,{w=0.2} fine!{w=0.2} Fine!{w=0.2} You win,{w=0.2} okay?!"
            n 1fcsemf  "I'm kinda...{w=0.3} maybe...{w=0.3} sorta...{w=0.3} somehow..."
            n 1fsqemf "In an abstract way..."
            n 1fsqpuf "...{w=0.3}'cute.'"
            n 1fsqslf "..."
            n 1fcsemf "There.{w=0.3} I said it, [player].{w=0.3} I said it.{w=0.3} {i}Hooray{/i} for you."
            n 1fsqpof "Are we done?{w=0.3} Are you happy?{w=0.3} Are you {i}pleased{/i} with yourself now?"
            n 1flrpof "Jeez..."
            n 1fnmpof "I swear,{w=0.2} you're such a goofball sometimes..."

            if Natsuki.isLove(higher=True):
                n 1fcsbgf "Besides,{w=0.2} I'm not even the cutest here,{w=0.2} a-{w=0.2}anyhow..."
                $ chosen_tease = jn_utils.getRandomTease()
                n 1fcssmf "I guess I'll let you figure out the rest,{w=0.2} [chosen_tease].{w=0.2} Ehehe."

        else:
            n 1fcsanf "Nnnnnnn-!"
            n 1fcsfuf "How many times do I have to say this,{w=0.2} [player]?!"
            n 1fbkwrf "{i}I'm not cute!!{/i}"
            n 1flremf "Jeez..."
            n 1fsqemf "Now I {i}know{/i} you just wanted me to say that,{w=0.2} didn't you?"
            n 1flrpof "Really now...{w=0.3} you're such a jerk sometimes,{w=0.2} [player]."

            if Natsuki.isAffectionate(higher=True):
                n 1fsqpol "You're just lucky you're in my good books."
                n 1fsqbgl "O-{w=0.2}or I wouldn't be nearly this patient.{w=0.2} Ehehe."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fsqbsl "A-{w=0.2}Aha!{w=0.2} Nope!"
            n 1fcsbgl "Nice try,{w=0.2} [player]!"
            n 1fchgnl "You're not gonna get me to say it that easily!{w=0.2} Ehehe."

        else:
            n 1uskemf "W-{w=0.2}what?{w=0.2} What did you just say?!"
            n 1nllemf "..."
            n 1nlrpuf "..."
            n 1flrbgl "I...{w=0.3} must have misheard you."
            n 1fcsbgl "Y-{w=0.2}yeah.{w=0.2} Yeah!{w=0.2} I totally misheard you.{w=0.2} One hundred percent."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_CUTE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of humour!",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_hilarious").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_HILARIOUS:
        if Natsuki.isEnamored(higher=True):
            n 1uchgn "Ehehe. Thanks, [player]!{w=0.2} I pride myself on that,{w=0.2} you know."
            n 1fnmbg "You aren't too shabby yourself,{w=0.2} you know!"
            n 1fwlts "But anyway{w=0.2} -{w=0.2} I'll keep it up,{w=0.2} juuust for you.{w=0.2} Ehehe."

        else:
            n 1uchgn "Ehehe.{w=0.2} I'm glad you're still having fun listening to me,{w=0.2} [player]."
            n 1fwlts "Thanks!{w=0.2} I'll keep it up!"

    else:
        if Natsuki.isEnamored(higher=True):
            n 1unmpu "Huh?{w=0.2} You do?"
            n 1nllpu "...{w=0.3}To tell you the truth,{w=0.2} [player]?"
            n 1kllaj "I'm honestly...{w=0.3} really glad to hear that."
            n 1kllsl "It's probably dumb,{w=0.2} but I always kinda worry about how much fun you're having here."
            n 1klrsl "I...{w=0.3} don't want you to get all bored..."
            n 1flrssl "That'd be super lame."
            n 1kllbol "So...{w=0.3} thanks for telling me that,{w=0.2} [player].{w=0.2} Truly."
            n 1klrssl "It means a lot."

        else:
            n 1fcsbgl "O-{w=0.2}Oh?{w=0.2} Aha!{w=0.2} Well,{w=0.2} I'm glad to hear it!"
            n 1fsqsm "You know what that means,{w=0.2} right?"
            n 1fchgn "It means you have great taste,{w=0.2} [player]!"
            n 1uchbselg "Ahaha!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_HILARIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="You're an inspiration to me!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_inspirational").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_INSPIRATIONAL:
        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Ahaha.{w=0.2} Thanks again for that,{w=0.2} [player]."
            n 1nllss "You're not half-bad an inspiration either,{w=0.2} you know!"

        else:
            n 1nchgn "Ehehe.{w=0.2} What can I say?{w=0.2} I'm a pro,{w=0.2} after all!"
            n 1nnmbg "But thanks,{w=0.2} [player]!"
            n 1fchsm "I'm glad you still find inspiration in yours truly!"

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fskeml "H-{w=0.2}huh?{w=0.2} I'm inspirational to you?"
            n 1fllbgl "Ahaha...{w=0.3} well...{w=0.3} of course I am!"
            n 1kllsr "..."
            n 1kllssl "Though I'm glad to hear it,{w=0.2} all the same."

        else:
            n 1fskeml "H-{w=0.2}huh?{w=0.2} I'm an inspiration to you?"
            n 1fcsbgl "Well...{w=0.3} o-{w=0.2}of course you'd think that!"
            n 1fllbgl "I mean,{w=0.2} role models don't come much better than me,{w=0.2} after all."
            n 1uchgn "Why,{w=0.2} I'm practically an idol,{w=0.2} right?{w=0.2} Ahaha!"
            n 1nllss "..."
            n 1knmss "...Right?"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_INSPIRATIONAL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of style!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_style").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_STYLE:
        if not Natsuki.isWearingOutfit("jn_school_uniform"):

            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1fchgn "Ehehe.{w=0.2} Still awestruck by my sense of fashion,{w=0.2} [player]?"
                n 1fwlbg "You can't deny I'm a snappy dresser!"

                if Natsuki.isLove(higher=True):
                    $ chosen_tease = jn_utils.getRandomTease()
                    n 1fllbgl "D-{w=0.2}don't think I just dress for me though,{w=0.2} [chosen_tease]~."
                    n 1nchsmleaf "Ahaha!"

            else:
                n 1tsgssl "Oh?{w=0.2} Someone could stand to take a few points,{w=0.2} huh?"
                n 1fsgsm "Ehehe."
                n 1fchbg "Relax,{w=0.2} relax!{w=0.2} I'm kidding,{w=0.2} [player].{w=0.2} Don't worry."
                n 1fwrsm "But thanks again!"

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1flleml "I mean...{w=0.3} thanks again,{w=0.2} [player]..."
                n 1fllpol "But it isn't like I picked out these clothes myself,{w=0.2} you know!"
                n 1flrsml "I guess a confidence boost is always welcome though..."

            else:
                n 1tlrpul "Uh...{w=0.3} well...{w=0.3} thanks again,{w=0.2} ...I think?"
                $ chosen_tease = jn_utils.getRandomTease()
                n 1fllpol "You could at least save the compliments for my own clothes though,{w=0.2} [chosen_tease]..."
                n 1nlrbg "But...{w=0.3} I guess I appreciate the sentiment.{w=0.2} Ahaha."

    else:

        if not Natsuki.isWearingOutfit("jn_school_uniform"):

            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1nchsml "Ehehe.{w=0.2} I'm just happy you like this outfit,{w=0.2} [player]!"
                n 1usqsml "But then...{w=0.3} should I really be surprised?"
                n 1fllssl "I-{w=0.2}I {i}am{/i} the one wearing it,{w=0.2} a-{w=0.2}after all!"

            else:
                n 1fchbgl "H-{w=0.2}ha!{w=0.2} I'm glad you agree!"
                n 1fcsbgl "It's only natural though,{w=0.2} right?{w=0.2} I like to pride myself on my sense of style!"
                n 1fchbg "Good job for noticing,{w=0.2} [player]!"

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1tskeml "H-{w=0.2}huh?{w=0.2} You like my sense of style?"
                n 1fllpol "I mean,{w=0.2} it's not like I can do much styling in this sort of getup..."
                n 1flrpol "But thanks,{w=0.2} [player]."

            else:
                n 1tskeml "W-{w=0.2}what?{w=0.2} My sense of style?"
                n 1fbkeml "But [player]!{w=0.2} It isn't like I came up with this look myself!"
                n 1fsqpol "..."
                n 1fllpul "Unless..."
                n 1tnmaj "A-{w=0.2}are you saying I look good in {i}uniform{/i}?"
                n 1fskemf "..."
                n 1fbkwrf "A-{w=0.2}ah!{w=0.2} Gross!{w=0.2} I don't like where this is going at all!{w=0.2} That's enough!"
                $ chosen_tease = jn_utils.getRandomTease()
                n 1flremf "Jeez,{w=0.2} [chosen_tease]..."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_STYLE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how thoughtful you are!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_thoughtful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_THOUGHTFUL:
        if Natsuki.isEnamored(higher=True):
            n 1fcsanl "Nnnnn-!{w=0.2} what did I tell you,{w=0.2} [player]?"
            n 1kllpol "I'm just...{w=0.3} giving as good as I get,{w=0.2} alright?"
            n 1knmpol "Jeez...{w=0.3} are you trying to put me on the spot or what?"
            $ chosen_tease = jn_utils.getRandomTease().capitalize()
            n 1klrpo "[chosen_tease]..."
            n 1klrpu "But...{w=0.3} I'm just really glad you appreciate it,{w=0.2} [player]."

            if Natsuki.isLove(higher=True):
                n 1knmsml "You're totally worth the effort."

        else:
            n 1fcsanl "Uuuuu...{w=0.3} jeez,{w=0.2} [player]..."
            n 1fbkeml "I already said it was nothing!{w=0.2} Are you trying to put me on the spot?"
            n 1fllpol "It's fine,{w=0.2} so...{w=0.3} don't worry about it,{w=0.2} alright?"
            $ chosen_tease = jn_utils.getRandomTease().capitalize()
            n 1flrpol "[chosen_tease]..."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1klrpol "Honestly,{w=0.2} [player]?{w=0.2} Don't worry about it,{w=0.2} 'kay?"
            n 1knmpol "You've done...{w=0.3} a lot for me already..."
            n 1klrnvl "So...{w=0.3} I'm just returning the favour,{w=0.2} that's all."
            n 1klrssl "Ahaha..."

        else:
            n 1fcsssl "Ah,{w=0.2} jeez,{w=0.2} [player]..."
            n 1fllssl "It's nothing,{w=0.2} honestly!"
            n 1knmpol "I-{w=0.2}I'm just trying to be friendly,{w=0.2} you know?"
            n 1fcsbgl "Yeah!{w=0.2} Totally no special treatment going on here.{w=0.2} Nope!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_THOUGHTFUL
    return
