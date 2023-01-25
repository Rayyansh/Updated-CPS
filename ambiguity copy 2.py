def ambi(msg):
    msgs = msg.lower()
    qtns = []
    anss = []
    msgs = msgs.split(". ")

    print(f"----------{msgs}")
    msgs = msgs[0]
    msgs = msgs[:-1]
    msgs = msgs + " "
    print(msgs)
    """
    for i in range(0, len(words)):
        flag = 0

        # msgs[i]=msgs[i].split()
        abc=""
        print(abc)
     
        print(words)
    """

    if " more " in msgs:
        qtns.append(" more ")
        anss.append("How much / how many is more?  ")
        flag = 1
    elif " too many " in msgs:
        qtns.append(" too many ")
        anss.append("too many means how many? ")
        flag = 1
    elif " many " in msgs:
        qtns.append(" many ")
        anss.append("many means how many? ")
        flag = 1
    if " greater than " in msgs:
        qtns.append(" greater than ")
        anss.append("greater than is vague. Specify it ")
        flag = 1
    if " lesser than " in msgs:
        qtns.append(" greater than ")
        anss.append("lesser than is vague. Specify it ")
        flag = 1
    if " hardly any " in msgs:
        qtns.append(" hardly any ")
        anss.append("hardly any is vague. Specify it ")
        flag = 1
    if " monthly expenses " in msgs:
        qtns.append(" monthly expenses ")
        anss.append("Specifically, which expenses? ")
        flag = 1
    if " tried hard " in msgs:
        qtns.append(" tried hard ")
        anss.append("What exactly was done in trying hard? ")
        flag = 1
    if " Holiday is a good thing " in msgs:
        qtns.append(" Holiday is a good thing. ")
        anss.append("How is holiday a good thing? ")
        flag = 1
    if " The Boss is crazy " in msgs:
        qtns.append(" The Boss is crazy ")
        anss.append("What leads you to believe that the Boss is crazy? ")
        flag = 1
    if " some " in msgs:
        qtns.append(" some ")
        anss.append("Some means whom? ")
        flag = 1
    if " more effective " in msgs:
        qtns.append(" more effective ")
        anss.append("How more effective and than whom? ")
        flag = 1
    if " should " in msgs:
        qtns.append(" should ")
        anss.append("What would happen if not done? ")
        flag = 1
    if " should not " in msgs:
        print("What would happen if not done? ")
        qtns.append(" should not ")
        anss.append()
        flag = 1
    if " must not " in msgs:
        qtns.append(" must not ")
        anss.append("What would happen if not done? ")
        flag = 1
    elif " must " in msgs:
        qtns.append(" must ")
        anss.append("What would happen if not done? ")
        flag = 1
    if " need to " in msgs:
        qtns.append(" need to ")
        anss.append("What would happen if not done? ")
        flag = 1
    if " it is necessary " in msgs:
        qtns.append(" it is necessary ")
        anss.append("What would happen if not done? ")
        flag = 1
    if " never " in msgs:
        qtns.append(" never ")
        anss.append("Never? What is preventing? ")
        flag = 1
    if " under a staff " in msgs:
        qtns.append(" under a staff ")
        anss.append("which staff? ")
        flag = 1
    if " clueless " in msgs:
        qtns.append(" clueless ")
        anss.append("What do you mean by clueless? ")
        flag = 1
    if " quitting in their papers " in msgs:
        qtns.append(" quitting in their papers ")
        anss.append("What do you mean by quitting in their papers? ")
        flag = 1
    if " killing our business " in msgs:
        qtns.append(" killing our business ")
        anss.append("What do you mean by killing our business? ")
        flag = 1
    if " out the door " in msgs:
        qtns.append(" out the door ")
        anss.append("What do you mean by out the door? ")
        flag = 1
    if " keeps up " in msgs:
        qtns.append(" keeps up ")
        anss.append("What do you mean by keeps up? ")
        flag = 1
    if " out of business " in msgs:
        qtns.append(" out of business ")
        anss.append("What do you mean by out of business? ")
        flag = 1
    if " on time " in msgs:
        qtns.append(" on time ")
        anss.append("What is meant by 'on time'? Can you be more specific? ")
        flag = 1
    if " over time " in msgs:
        qtns.append(" over time ")
        anss.append("How much more time is over time? ")
        flag = 1
    # if " we " in msgs:
    #    qtns.append(" we ")
    #    anss.append("What do you mean by we? A group of people or a company or what? ")
    #    flag=1
    if " high " in msgs:
        qtns.append(" high ")
        anss.append("What is meant by high? Can you be more specific? ")
        flag = 1
    if " low " in msgs:
        qtns.append(" low ")
        anss.append("What is meant by low? Can you be more specific? ")
        flag = 1
    if " lots " in msgs:
        qtns.append(" lots ")
        anss.append("What is meant by lots? Can you be more specific? ")
        flag = 1
    if " Lots " in msgs:
        qtns.append(" Lots ")
        anss.append("What is meant by Lots? Can you be more specific? ")
        flag = 1
    if " this " in msgs:
        qtns.append(" this ")
        anss.append("What do you mean by this? Can you be more specific? ")
        flag = 1
    if " that " in msgs:
        print("What is meant by that? Can you be more specific? ")
        qtns.append(" that ")
        anss.append(" ")
        flag = 1
    if " these " in msgs:
        print("What is meant by these? Can you be more specific? ")
        qtns.append(" these ")
        anss.append(" ")
        flag = 1
    if " new " in msgs:
        qtns.append(" new ")
        anss.append("How new? ")
        flag = 1
    if " good " in msgs:
        qtns.append(" good ")
        anss.append("How can you say good? ")
        flag = 1
    if " best " in msgs:
        qtns.append(" best ")
        anss.append("How can you say best? ")
        flag = 1
    if " better " in msgs:
        qtns.append(" better ")
        anss.append("How can you say better? ")
        flag = 1
    if " great " in msgs:
        qtns.append(" great ")
        anss.append("How can you say great? ")
        flag = 1
    if " greater " in msgs:
        qtns.append(" greater ")
        anss.append("How can you say greater? ")
        flag = 1
    if " greatest " in msgs:
        qtns.append(" greatest ")
        anss.append("How can you say greatest? ")
        flag = 1
    if " bad " in msgs:
        qtns.append(" bad ")
        anss.append("How can you say bad? ")
        flag = 1
    if " worse " in msgs:
        qtns.append(" worse ")
        anss.append("How can you say worse? ")
        flag = 1
    if " worst " in msgs:
        qtns.append(" worst ")
        anss.append("How can you say worst? ")
        flag = 1
    if " impossible " in msgs:
        qtns.append(" impossible ")
        anss.append("How can you say impossible? ")
        flag = 1
    if " less " in msgs:
        qtns.append(" less ")
        anss.append("less means how many? ")
        flag = 1
    if " few " in msgs:
        qtns.append(" few ")
        anss.append("few means how many? ")
        flag = 1
    if " most " in msgs:
        qtns.append(" most ")
        anss.append("most means how many? ")
        flag = 1
    if " least " in msgs:
        qtns.append(" least ")
        anss.append("least means how many? ")
        flag = 1
    if " sometimes " in msgs:
        qtns.append(" sometimes ")
        anss.append("sometimes is vague. Specify it ")
        flag = 1
    if " usually " in msgs:
        qtns.append(" most ")
        anss.append("usually is vague. Specify it ")
        flag = 1
    if " seldom " in msgs:
        qtns.append(" seldom ")
        anss.append("seldom is vague. Specify it ")
        flag = 1
    if " frequently " in msgs:
        qtns.append(" frequently ")
        anss.append("frequently is vague. Specify it ")
        flag = 1
    if " him " in msgs:
        qtns.append(" him ")
        anss.append("him is vague. Specify 'him' ")
        flag = 1
    if " a bit " in msgs:
        qtns.append(" a bit ")
        anss.append("What is meant by 'a bit'? ")
        flag = 1
    if " empoyees " in msgs:
        qtns.append(" employees ")
        anss.append("employees means? Which employees? ")
        flag = 1
    if " when " in msgs:
        qtns.append(" when ")
        anss.append("How often is 'when'? ")
        flag = 1
    if " workers " in msgs:
        qtns.append(" workers ")
        anss.append("Workers means? Which workers? ")
        flag = 1
    if " loud " in msgs:
        qtns.append(" loud ")
        anss.append("'Loud' compared to what?  ")
        flag = 1
    if " scary " in msgs:
        qtns.append(" scary ")
        anss.append("'Scary' compared to what? ")
        flag = 1
    if " Overall " in msgs:
        qtns.append(" Overall ")
        anss.append("'Overall' or only sometime? ")
        flag = 1
    if " as clean as " in msgs:
        qtns.append(" as clean as ")
        anss.append("'as clean as' compared to what?  ")
        flag = 1
    if " ordinary " in msgs:
        qtns.append(" ordinary ")
        anss.append("how ordinary? ")
        flag = 1
    if " overwhelmed " in msgs:
        qtns.append(" overwhelmed ")
        anss.append("how specifically are you overwhelemed? ")
        flag = 1
    if " satisfy " in msgs:
        qtns.append(" satisfy ")
        anss.append("How do you want to satisfy? ")
        flag = 1
    if " all " in msgs:
        qtns.append(" all ")
        anss.append("All means how many? ")
        flag = 1
    if " much " in msgs:
        qtns.append(" much ")
        anss.append("Can you quantify 'much'? ")
        flag = 1
    if " terrible " in msgs:
        qtns.append(" terrible ")
        anss.append("How terrible? ")
        flag = 1
    if " slow " in msgs:
        qtns.append(" slow ")
        anss.append("How slow? ")
        flag = 1
    if " organisation " in msgs:
        qtns.append(" organisation ")
        anss.append("Which organisation? ")
        flag = 1
    if " ahead " in msgs:
        qtns.append(" ahead ")
        anss.append("ahead? How much ahead? ")
        flag = 1
    if " higly " in msgs:
        qtns.append(" highly ")
        anss.append("How high? ")
        flag = 1
    if " may " in msgs:
        qtns.append(" may ")
        anss.append("may? or definitely need? ")
        flag = 1
    if " maybe " in msgs:
        qtns.append(" maybe ")
        anss.append("What can we do differently to find out? ")
        flag = 1
    if " targeted goal. " in msgs:
        qtns.append(" targeted goal. ")
        anss.append("What is your targeted goal specificly? ")
        flag = 1
    if " competitions " in msgs:
        qtns.append(" competitions ")
        anss.append("Who is your competitors? ")
        flag = 1
    if " almost " in msgs:
        qtns.append(" almost ")
        anss.append("Almost? How many or how much? ")
        flag = 1
    if " adjustments " in msgs:
        qtns.append(" adjustments ")
        anss.append("What adjustments exactly? ")
        flag = 1
    if " skilled " in msgs:
        qtns.append(" skilled ")
        anss.append("skilled in what? ")
        flag = 1
    if " right people " in msgs:
        qtns.append(" right people ")
        anss.append("Who specifically are the right people? ")
        flag = 1
    if " not matching " in msgs:
        qtns.append(" not matching ")
        anss.append("What can you do differently to match? ")
        flag = 1
    if " not sure " in msgs:
        qtns.append(" not sure ")
        anss.append("What can you do differently to become sure? ")
        flag = 1
    if " clients " in msgs:
        qtns.append(" clients ")
        anss.append("who are you clients? ")
        flag = 1
    if " top management " in msgs:
        qtns.append(" top management ")
        anss.append("Who in top management? ")
        flag = 1
    if " perhaps " in msgs:
        qtns.append(" perhaps ")
        anss.append("perhaps? Can you be more specific? ")
        flag = 1
    if " new recruits " in msgs:
        qtns.append(" new recruits ")
        anss.append("how many new recruits? ")
        flag = 1
    if " attrition " in msgs:
        qtns.append(" attrition ")
        anss.append("how much attrition is happening ? ")
        flag = 1
    if " procrastination " in msgs:
        qtns.append(" procrastination ")
        anss.append("how specifically do you procrastinate? ")
        flag = 1
    if " technically " in msgs:
        qtns.append(" technically ")
        anss.append("how technically? What technology? ")
        flag = 1
    if " bitter " in msgs:
        qtns.append(" bitter ")
        anss.append("How bitter is the problem when it exists? Does it always exist? ")
        flag = 1
    if " billion dollar " in msgs:
        qtns.append(" billion dollar ")
        anss.append("in what? Turn over? Profit? Or market capitalisation? Please specify ")
        flag = 1
    if " train the sales team " in msgs:
        qtns.append(" train the sales team ")
        anss.append("Train in what? ")
        flag = 1
    if " deliver " in msgs:
        qtns.append(" deliver ")
        anss.append("What do you mean by deliver? ")
        flag = 1
    if " bulk " in msgs:
        qtns.append(" bulk ")
        anss.append("How much / how many is bulk? ")
        flag = 1
    if " most abactinal " in msgs:
        qtns.append(" most abactinal ")
        anss.append("What do you mean by most abactinal? Please specify. ")
        flag = 1
    if " least abactinal " in msgs:
        qtns.append(" least abactinal ")
        anss.append("What do you mean by least abactinal? Please specify. ")
        flag = 1
    if " very abactinal " in msgs:
        qtns.append(" very abactinal ")
        anss.append("What do you mean by very abactinal? Please specify. ")
        flag = 1
    if " extremely abactinal " in msgs:
        qtns.append(" extremely abactinal ")
        anss.append("What do you mean by extremely abactinal? Please specify. ")
        flag = 1
    if " especially abactinal " in msgs:
        qtns.append(" especially abactinal ")
        anss.append("What do you mean by especially abactinal? Please specify. ")
        flag = 1
    if " absolutely abactinal " in msgs:
        qtns.append(" absolutely abactinal ")
        anss.append("What do you mean by absolutely abactinal? Please specify. ")
        flag = 1
    if " most abandoned " in msgs:
        qtns.append(" most abandoned ")
        anss.append("What do you mean by most abandoned? Please specify. ")
        flag = 1
    if " least abandoned " in msgs:
        qtns.append(" least abandoned ")
        anss.append("What do you mean by least abandoned? Please specify. ")
        flag = 1
    if " very abandoned " in msgs:
        qtns.append(" very abandoned ")
        anss.append("What do you mean by very abandoned? Please specify. ")
        flag = 1
    if " extremely abandoned " in msgs:
        qtns.append(" extremely abandoned ")
        anss.append("What do you mean by extremely abandoned? Please specify. ")
        flag = 1
    if " especially abandoned " in msgs:
        qtns.append(" especially abandoned ")
        anss.append("What do you mean by especially abandoned? Please specify. ")
        flag = 1
    if " absolutely abandoned " in msgs:
        qtns.append(" absolutely abandoned ")
        anss.append("What do you mean by absolutely abandoned? Please specify. ")
        flag = 1
    if " most abashed " in msgs:
        qtns.append(" most abashed ")
        anss.append("What do you mean by most abashed? Please specify. ")
        flag = 1
    if " least abashed " in msgs:
        qtns.append(" least abashed ")
        anss.append("What do you mean by least abashed? Please specify. ")
        flag = 1
    if " very abashed " in msgs:
        qtns.append(" very abashed ")
        anss.append("What do you mean by very abashed? Please specify. ")
        flag = 1
    if " extremely abashed " in msgs:
        qtns.append(" extremely abashed ")
        anss.append("What do you mean by extremely abashed? Please specify. ")
        flag = 1
    if " especially abashed " in msgs:
        qtns.append(" especially abashed ")
        anss.append("What do you mean by especially abashed? Please specify. ")
        flag = 1
    if " absolutely abashed " in msgs:
        qtns.append(" absolutely abashed ")
        anss.append("What do you mean by absolutely abashed? Please specify. ")
        flag = 1
    if " most abatable " in msgs:
        qtns.append(" most abatable ")
        anss.append("What do you mean by most abatable? Please specify. ")
        flag = 1
    if " least abatable " in msgs:
        qtns.append(" least abatable ")
        anss.append("What do you mean by least abatable? Please specify. ")
        flag = 1
    if " very abatable " in msgs:
        qtns.append(" very abatable ")
        anss.append("What do you mean by very abatable? Please specify. ")
        flag = 1
    if " extremely abatable " in msgs:
        qtns.append(" extremely abatable ")
        anss.append("What do you mean by extremely abatable? Please specify. ")
        flag = 1
    if " especially abatable " in msgs:
        qtns.append(" especially abatable ")
        anss.append("What do you mean by especially abatable? Please specify. ")
        flag = 1
    if " absolutely abatable " in msgs:
        qtns.append(" absolutely abatable ")
        anss.append("What do you mean by absolutely abatable? Please specify. ")
        flag = 1
    if " most abatic " in msgs:
        qtns.append(" most abatic ")
        anss.append("What do you mean by most abatic? Please specify. ")
        flag = 1
    if " least abatic " in msgs:
        qtns.append(" least abatic ")
        anss.append("What do you mean by least abatic? Please specify. ")
        flag = 1
    if " very abatic " in msgs:
        qtns.append(" very abatic ")
        anss.append("What do you mean by very abatic? Please specify. ")
        flag = 1
    if " extremely abatic " in msgs:
        qtns.append(" extremely abatic ")
        anss.append("What do you mean by extremely abatic? Please specify. ")
        flag = 1
    if " especially abatic " in msgs:
        qtns.append(" especially abatic ")
        anss.append("What do you mean by especially abatic? Please specify. ")
        flag = 1
    if " absolutely abatic " in msgs:
        qtns.append(" absolutely abatic ")
        anss.append("What do you mean by absolutely abatic? Please specify. ")
        flag = 1
    if " most abaxial " in msgs:
        qtns.append(" most abaxial ")
        anss.append("What do you mean by most abaxial? Please specify. ")
        flag = 1
    if " least abaxial " in msgs:
        qtns.append(" least abaxial ")
        anss.append("What do you mean by least abaxial? Please specify. ")
        flag = 1
    if " very abaxial " in msgs:
        qtns.append(" very abaxial ")
        anss.append("What do you mean by very abaxial? Please specify. ")
        flag = 1
    if " extremely abaxial " in msgs:
        qtns.append(" extremely abaxial ")
        anss.append("What do you mean by extremely abaxial? Please specify. ")
        flag = 1
    if " especially abaxial " in msgs:
        qtns.append(" especially abaxial ")
        anss.append("What do you mean by especially abaxial? Please specify. ")
        flag = 1
    if " absolutely abaxial " in msgs:
        qtns.append(" absolutely abaxial ")
        anss.append("What do you mean by absolutely abaxial? Please specify. ")
        flag = 1
    if " most abbatial " in msgs:
        qtns.append(" most abbatial ")
        anss.append("What do you mean by most abbatial? Please specify. ")
        flag = 1
    if " least abbatial " in msgs:
        qtns.append(" least abbatial ")
        anss.append("What do you mean by least abbatial? Please specify. ")
        flag = 1
    if " very abbatial " in msgs:
        qtns.append(" very abbatial ")
        anss.append("What do you mean by very abbatial? Please specify. ")
        flag = 1
    if " extremely abbatial " in msgs:
        qtns.append(" extremely abbatial ")
        anss.append("What do you mean by extremely abbatial? Please specify. ")
        flag = 1
    if " especially abbatial " in msgs:
        qtns.append(" especially abbatial ")
        anss.append("What do you mean by especially abbatial? Please specify. ")
        flag = 1
    if " absolutely abbatial " in msgs:
        qtns.append(" absolutely abbatial ")
        anss.append("What do you mean by absolutely abbatial? Please specify. ")
        flag = 1
    if " most abbreviated " in msgs:
        qtns.append(" most abbreviated ")
        anss.append("What do you mean by most abbreviated? Please specify. ")
        flag = 1
    if " least abbreviated " in msgs:
        qtns.append(" least abbreviated ")
        anss.append("What do you mean by least abbreviated? Please specify. ")
        flag = 1
    if " very abbreviated " in msgs:
        qtns.append(" very abbreviated ")
        anss.append("What do you mean by very abbreviated? Please specify. ")
        flag = 1
    if " extremely abbreviated " in msgs:
        qtns.append(" extremely abbreviated ")
        anss.append("What do you mean by extremely abbreviated? Please specify. ")
        flag = 1
    if " especially abbreviated " in msgs:
        qtns.append(" especially abbreviated ")
        anss.append("What do you mean by especially abbreviated? Please specify. ")
        flag = 1
    if " absolutely abbreviated " in msgs:
        qtns.append(" absolutely abbreviated ")
        anss.append("What do you mean by absolutely abbreviated? Please specify. ")
        flag = 1
    if " most abducent " in msgs:
        qtns.append(" most abducent ")
        anss.append("What do you mean by most abducent? Please specify. ")
        flag = 1
    if " least abducent " in msgs:
        qtns.append(" least abducent ")
        anss.append("What do you mean by least abducent? Please specify. ")
        flag = 1
    if " very abducent " in msgs:
        qtns.append(" very abducent ")
        anss.append("What do you mean by very abducent? Please specify. ")
        flag = 1
    if " extremely abducent " in msgs:
        qtns.append(" extremely abducent ")
        anss.append("What do you mean by extremely abducent? Please specify. ")
        flag = 1
    if " especially abducent " in msgs:
        qtns.append(" especially abducent ")
        anss.append("What do you mean by especially abducent? Please specify. ")
        flag = 1
    if " absolutely abducent " in msgs:
        qtns.append(" absolutely abducent ")
        anss.append("What do you mean by absolutely abducent? Please specify. ")
        flag = 1
    if " most abducting " in msgs:
        qtns.append(" most abducting ")
        anss.append("What do you mean by most abducting? Please specify. ")
        flag = 1
    if " least abducting " in msgs:
        qtns.append(" least abducting ")
        anss.append("What do you mean by least abducting? Please specify. ")
        flag = 1
    if " very abducting " in msgs:
        qtns.append(" very abducting ")
        anss.append("What do you mean by very abducting? Please specify. ")
        flag = 1
    if " extremely abducting " in msgs:
        qtns.append(" extremely abducting ")
        anss.append("What do you mean by extremely abducting? Please specify. ")
        flag = 1
    if " especially abducting " in msgs:
        qtns.append(" especially abducting ")
        anss.append("What do you mean by especially abducting? Please specify. ")
        flag = 1
    if " absolutely abducting " in msgs:
        qtns.append(" absolutely abducting ")
        anss.append("What do you mean by absolutely abducting? Please specify. ")
        flag = 1
    if " most aberrant " in msgs:
        qtns.append(" most aberrant ")
        anss.append("What do you mean by most aberrant? Please specify. ")
        flag = 1
    if " least aberrant " in msgs:
        qtns.append(" least aberrant ")
        anss.append("What do you mean by least aberrant? Please specify. ")
        flag = 1
    if " very aberrant " in msgs:
        qtns.append(" very aberrant ")
        anss.append("What do you mean by very aberrant? Please specify. ")
        flag = 1
    if " extremely aberrant " in msgs:
        qtns.append(" extremely aberrant ")
        anss.append("What do you mean by extremely aberrant? Please specify. ")
        flag = 1
    if " especially aberrant " in msgs:
        qtns.append(" especially aberrant ")
        anss.append("What do you mean by especially aberrant? Please specify. ")
        flag = 1
    if " absolutely aberrant " in msgs:
        qtns.append(" absolutely aberrant ")
        anss.append("What do you mean by absolutely aberrant? Please specify. ")
        flag = 1
    if " most abeyant " in msgs:
        qtns.append(" most abeyant ")
        anss.append("What do you mean by most abeyant? Please specify. ")
        flag = 1
    if " least abeyant " in msgs:
        qtns.append(" least abeyant ")
        anss.append("What do you mean by least abeyant? Please specify. ")
        flag = 1
    if " very abeyant " in msgs:
        qtns.append(" very abeyant ")
        anss.append("What do you mean by very abeyant? Please specify. ")
        flag = 1
    if " extremely abeyant " in msgs:
        qtns.append(" extremely abeyant ")
        anss.append("What do you mean by extremely abeyant? Please specify. ")
        flag = 1
    if " especially abeyant " in msgs:
        qtns.append(" especially abeyant ")
        anss.append("What do you mean by especially abeyant? Please specify. ")
        flag = 1
    if " absolutely abeyant " in msgs:
        qtns.append(" absolutely abeyant ")
        anss.append("What do you mean by absolutely abeyant? Please specify. ")
        flag = 1
    if " most abhorrent " in msgs:
        qtns.append(" most abhorrent ")
        anss.append("What do you mean by most abhorrent? Please specify. ")
        flag = 1
    if " least abhorrent " in msgs:
        qtns.append(" least abhorrent ")
        anss.append("What do you mean by least abhorrent? Please specify. ")
        flag = 1
    if " very abhorrent " in msgs:
        qtns.append(" very abhorrent ")
        anss.append("What do you mean by very abhorrent? Please specify. ")
        flag = 1
    if " extremely abhorrent " in msgs:
        qtns.append(" extremely abhorrent ")
        anss.append("What do you mean by extremely abhorrent? Please specify. ")
        flag = 1
    if " especially abhorrent " in msgs:
        qtns.append(" especially abhorrent ")
        anss.append("What do you mean by especially abhorrent? Please specify. ")
        flag = 1
    if " absolutely abhorrent " in msgs:
        qtns.append(" absolutely abhorrent ")
        anss.append("What do you mean by absolutely abhorrent? Please specify. ")
        flag = 1
    if " most abiding " in msgs:
        qtns.append(" most abiding ")
        anss.append("What do you mean by most abiding? Please specify. ")
        flag = 1
    if " least abiding " in msgs:
        qtns.append(" least abiding ")
        anss.append("What do you mean by least abiding? Please specify. ")
        flag = 1
    if " very abiding " in msgs:
        qtns.append(" very abiding ")
        anss.append("What do you mean by very abiding? Please specify. ")
        flag = 1
    if " extremely abiding " in msgs:
        qtns.append(" extremely abiding ")
        anss.append("What do you mean by extremely abiding? Please specify. ")
        flag = 1
    if " especially abiding " in msgs:
        qtns.append(" especially abiding ")
        anss.append("What do you mean by especially abiding? Please specify. ")
        flag = 1
    if " absolutely abiding " in msgs:
        qtns.append(" absolutely abiding ")
        anss.append("What do you mean by absolutely abiding? Please specify. ")
        flag = 1
    if " most abient " in msgs:
        qtns.append(" most abient ")
        anss.append("What do you mean by most abient? Please specify. ")
        flag = 1
    if " least abient " in msgs:
        qtns.append(" least abient ")
        anss.append("What do you mean by least abient? Please specify. ")
        flag = 1
    if " very abient " in msgs:
        qtns.append(" very abient ")
        anss.append("What do you mean by very abient? Please specify. ")
        flag = 1
    if " extremely abient " in msgs:
        qtns.append(" extremely abient ")
        anss.append("What do you mean by extremely abient? Please specify. ")
        flag = 1
    if " especially abient " in msgs:
        qtns.append(" especially abient ")
        anss.append("What do you mean by especially abient? Please specify. ")
        flag = 1
    if " absolutely abient " in msgs:
        qtns.append(" absolutely abient ")
        anss.append("What do you mean by absolutely abient? Please specify. ")
        flag = 1
    if " most abundant " in msgs:
        qtns.append(" most abundant ")
        anss.append("What do you mean by most abundant? Please specify. ")
        flag = 1
    if " least abundant " in msgs:
        qtns.append(" least abundant ")
        anss.append("What do you mean by least abundant? Please specify. ")
        flag = 1
    if " very abundant " in msgs:
        qtns.append(" very abundant ")
        anss.append("What do you mean by very abundant? Please specify. ")
        flag = 1
    if " extremely abundant " in msgs:
        qtns.append(" extremely abundant ")
        anss.append("What do you mean by extremely abundant? Please specify. ")
        flag = 1
    if " especially abundant " in msgs:
        qtns.append(" especially abundant ")
        anss.append("What do you mean by especially abundant? Please specify. ")
        flag = 1
    if " absolutely abundant " in msgs:
        qtns.append(" absolutely abundant ")
        anss.append("What do you mean by absolutely abundant? Please specify. ")
        flag = 1
    if " most accurate " in msgs:
        qtns.append(" most accurate ")
        anss.append("What do you mean by most accurate? Please specify. ")
        flag = 1
    if " least accurate " in msgs:
        qtns.append(" least accurate ")
        anss.append("What do you mean by least accurate? Please specify. ")
        flag = 1
    if " very accurate " in msgs:
        qtns.append(" very accurate ")
        anss.append("What do you mean by very accurate? Please specify. ")
        flag = 1
    if " extremely accurate " in msgs:
        qtns.append(" extremely accurate ")
        anss.append("What do you mean by extremely accurate? Please specify. ")
        flag = 1
    if " especially accurate " in msgs:
        qtns.append(" especially accurate ")
        anss.append("What do you mean by especially accurate? Please specify. ")
        flag = 1
    if " absolutely accurate " in msgs:
        qtns.append(" absolutely accurate ")
        anss.append("What do you mean by absolutely accurate? Please specify. ")
        flag = 1
    if " most addicted " in msgs:
        qtns.append(" most addicted ")
        anss.append("What do you mean by most addicted? Please specify. ")
        flag = 1
    if " least addicted " in msgs:
        qtns.append(" least addicted ")
        anss.append("What do you mean by least addicted? Please specify. ")
        flag = 1
    if " very addicted " in msgs:
        qtns.append(" very addicted ")
        anss.append("What do you mean by very addicted? Please specify. ")
        flag = 1
    if " extremely addicted " in msgs:
        qtns.append(" extremely addicted ")
        anss.append("What do you mean by extremely addicted? Please specify. ")
        flag = 1
    if " especially addicted " in msgs:
        qtns.append(" especially addicted ")
        anss.append("What do you mean by especially addicted? Please specify. ")
        flag = 1
    if " absolutely addicted " in msgs:
        qtns.append(" absolutely addicted ")
        anss.append("What do you mean by absolutely addicted? Please specify. ")
        flag = 1
    if " most adorable " in msgs:
        qtns.append(" most adorable ")
        anss.append("What do you mean by most adorable? Please specify. ")
        flag = 1
    if " least adorable " in msgs:
        qtns.append(" least adorable ")
        anss.append("What do you mean by least adorable? Please specify. ")
        flag = 1
    if " very adorable " in msgs:
        qtns.append(" very adorable ")
        anss.append("What do you mean by very adorable? Please specify. ")
        flag = 1
    if " extremely adorable " in msgs:
        qtns.append(" extremely adorable ")
        anss.append("What do you mean by extremely adorable? Please specify. ")
        flag = 1
    if " especially adorable " in msgs:
        qtns.append(" especially adorable ")
        anss.append("What do you mean by especially adorable? Please specify. ")
        flag = 1
    if " absolutely adorable " in msgs:
        qtns.append(" absolutely adorable ")
        anss.append("What do you mean by absolutely adorable? Please specify. ")
        flag = 1
    if " most adventurous " in msgs:
        qtns.append(" most adventurous ")
        anss.append("What do you mean by most adventurous? Please specify. ")
        flag = 1
    if " least adventurous " in msgs:
        qtns.append(" least adventurous ")
        anss.append("What do you mean by least adventurous? Please specify. ")
        flag = 1
    if " very adventurous " in msgs:
        qtns.append(" very adventurous ")
        anss.append("What do you mean by very adventurous? Please specify. ")
        flag = 1
    if " extremely adventurous " in msgs:
        qtns.append(" extremely adventurous ")
        anss.append("What do you mean by extremely adventurous? Please specify. ")
        flag = 1
    if " especially adventurous " in msgs:
        qtns.append(" especially adventurous ")
        anss.append("What do you mean by especially adventurous? Please specify. ")
        flag = 1
    if " absolutely adventurous " in msgs:
        qtns.append(" absolutely adventurous ")
        anss.append("What do you mean by absolutely adventurous? Please specify. ")
        flag = 1
    if " most afraid " in msgs:
        qtns.append(" most afraid ")
        anss.append("What do you mean by most afraid? Please specify. ")
        flag = 1
    if " least afraid " in msgs:
        qtns.append(" least afraid ")
        anss.append("What do you mean by least afraid? Please specify. ")
        flag = 1
    if " very afraid " in msgs:
        qtns.append(" very afraid ")
        anss.append("What do you mean by very afraid? Please specify. ")
        flag = 1
    if " extremely afraid " in msgs:
        qtns.append(" extremely afraid ")
        anss.append("What do you mean by extremely afraid? Please specify. ")
        flag = 1
    if " especially afraid " in msgs:
        qtns.append(" especially afraid ")
        anss.append("What do you mean by especially afraid? Please specify. ")
        flag = 1
    if " absolutely afraid " in msgs:
        qtns.append(" absolutely afraid ")
        anss.append("What do you mean by absolutely afraid? Please specify. ")
        flag = 1
    if " most aggressive " in msgs:
        qtns.append(" most aggressive ")
        anss.append("What do you mean by most aggressive? Please specify. ")
        flag = 1
    if " least aggressive " in msgs:
        qtns.append(" least aggressive ")
        anss.append("What do you mean by least aggressive? Please specify. ")
        flag = 1
    if " very aggressive " in msgs:
        qtns.append(" very aggressive ")
        anss.append("What do you mean by very aggressive? Please specify. ")
        flag = 1
    if " extremely aggressive " in msgs:
        qtns.append(" extremely aggressive ")
        anss.append("What do you mean by extremely aggressive? Please specify. ")
        flag = 1
    if " especially aggressive " in msgs:
        qtns.append(" especially aggressive ")
        anss.append("What do you mean by especially aggressive? Please specify. ")
        flag = 1
    if " absolutely aggressive " in msgs:
        qtns.append(" absolutely aggressive ")
        anss.append("What do you mean by absolutely aggressive? Please specify. ")
        flag = 1
    if " most alcoholic " in msgs:
        qtns.append(" most alcoholic ")
        anss.append("What do you mean by most alcoholic? Please specify. ")
        flag = 1
    if " least alcoholic " in msgs:
        qtns.append(" least alcoholic ")
        anss.append("What do you mean by least alcoholic? Please specify. ")
        flag = 1
    if " very alcoholic " in msgs:
        qtns.append(" very alcoholic ")
        anss.append("What do you mean by very alcoholic? Please specify. ")
        flag = 1
    if " extremely alcoholic " in msgs:
        qtns.append(" extremely alcoholic ")
        anss.append("What do you mean by extremely alcoholic? Please specify. ")
        flag = 1
    if " especially alcoholic " in msgs:
        qtns.append(" especially alcoholic ")
        anss.append("What do you mean by especially alcoholic? Please specify. ")
        flag = 1
    if " absolutely alcoholic " in msgs:
        qtns.append(" absolutely alcoholic ")
        anss.append("What do you mean by absolutely alcoholic? Please specify. ")
        flag = 1
    if " most alert " in msgs:
        qtns.append(" most alert ")
        anss.append("What do you mean by most alert? Please specify. ")
        flag = 1
    if " least alert " in msgs:
        qtns.append(" least alert ")
        anss.append("What do you mean by least alert? Please specify. ")
        flag = 1
    if " very alert " in msgs:
        qtns.append(" very alert ")
        anss.append("What do you mean by very alert? Please specify. ")
        flag = 1
    if " extremely alert " in msgs:
        qtns.append(" extremely alert ")
        anss.append("What do you mean by extremely alert? Please specify. ")
        flag = 1
    if " especially alert " in msgs:
        qtns.append(" especially alert ")
        anss.append("What do you mean by especially alert? Please specify. ")
        flag = 1
    if " absolutely alert " in msgs:
        qtns.append(" absolutely alert ")
        anss.append("What do you mean by absolutely alert? Please specify. ")
        flag = 1
    if " most aloof " in msgs:
        qtns.append(" most aloof ")
        anss.append("What do you mean by most aloof? Please specify. ")
        flag = 1
    if " least aloof " in msgs:
        qtns.append(" least aloof ")
        anss.append("What do you mean by least aloof? Please specify. ")
        flag = 1
    if " very aloof " in msgs:
        qtns.append(" very aloof ")
        anss.append("What do you mean by very aloof? Please specify. ")
        flag = 1
    if " extremely aloof " in msgs:
        qtns.append(" extremely aloof ")
        anss.append("What do you mean by extremely aloof? Please specify. ")
        flag = 1
    if " especially aloof " in msgs:
        qtns.append(" especially aloof ")
        anss.append("What do you mean by especially aloof? Please specify. ")
        flag = 1
    if " absolutely aloof " in msgs:
        qtns.append(" absolutely aloof ")
        anss.append("What do you mean by absolutely aloof? Please specify. ")
        flag = 1
    if " most ambitious " in msgs:
        qtns.append(" most ambitious ")
        anss.append("What do you mean by most ambitious? Please specify. ")
        flag = 1
    if " least ambitious " in msgs:
        qtns.append(" least ambitious ")
        anss.append("What do you mean by least ambitious? Please specify. ")
        flag = 1
    if " very ambitious " in msgs:
        qtns.append(" very ambitious ")
        anss.append("What do you mean by very ambitious? Please specify. ")
        flag = 1
    if " extremely ambitious " in msgs:
        qtns.append(" extremely ambitious ")
        anss.append("What do you mean by extremely ambitious? Please specify. ")
        flag = 1
    if " especially ambitious " in msgs:
        qtns.append(" especially ambitious ")
        anss.append("What do you mean by especially ambitious? Please specify. ")
        flag = 1
    if " absolutely ambitious " in msgs:
        qtns.append(" absolutely ambitious ")
        anss.append("What do you mean by absolutely ambitious? Please specify. ")
        flag = 1
    if " most ancient " in msgs:
        qtns.append(" most ancient ")
        anss.append("What do you mean by most ancient? Please specify. ")
        flag = 1
    if " least ancient " in msgs:
        qtns.append(" least ancient ")
        anss.append("What do you mean by least ancient? Please specify. ")
        flag = 1
    if " very ancient " in msgs:
        qtns.append(" very ancient ")
        anss.append("What do you mean by very ancient? Please specify. ")
        flag = 1
    if " extremely ancient " in msgs:
        qtns.append(" extremely ancient ")
        anss.append("What do you mean by extremely ancient? Please specify. ")
        flag = 1
    if " especially ancient " in msgs:
        qtns.append(" especially ancient ")
        anss.append("What do you mean by especially ancient? Please specify. ")
        flag = 1
    if " absolutely ancient " in msgs:
        qtns.append(" absolutely ancient ")
        anss.append("What do you mean by absolutely ancient? Please specify. ")
        flag = 1
    if " most angry " in msgs:
        qtns.append(" most angry ")
        anss.append("What do you mean by most angry? Please specify. ")
        flag = 1
    if " least angry " in msgs:
        qtns.append(" least angry ")
        anss.append("What do you mean by least angry? Please specify. ")
        flag = 1
    if " very angry " in msgs:
        qtns.append(" very angry ")
        anss.append("What do you mean by very angry? Please specify. ")
        flag = 1
    if " extremely angry " in msgs:
        qtns.append(" extremely angry ")
        anss.append("What do you mean by extremely angry? Please specify. ")
        flag = 1
    if " especially angry " in msgs:
        qtns.append(" especially angry ")
        anss.append("What do you mean by especially angry? Please specify. ")
        flag = 1
    if " absolutely angry " in msgs:
        qtns.append(" absolutely angry ")
        anss.append("What do you mean by absolutely angry? Please specify. ")
        flag = 1
    if " most animated " in msgs:
        qtns.append(" most animated ")
        anss.append("What do you mean by most animated? Please specify. ")
        flag = 1
    if " least animated " in msgs:
        qtns.append(" least animated ")
        anss.append("What do you mean by least animated? Please specify. ")
        flag = 1
    if " very animated " in msgs:
        qtns.append(" very animated ")
        anss.append("What do you mean by very animated? Please specify. ")
        flag = 1
    if " extremely animated " in msgs:
        qtns.append(" extremely animated ")
        anss.append("What do you mean by extremely animated? Please specify. ")
        flag = 1
    if " especially animated " in msgs:
        qtns.append(" especially animated ")
        anss.append("What do you mean by especially animated? Please specify. ")
        flag = 1
    if " absolutely animated " in msgs:
        qtns.append(" absolutely animated ")
        anss.append("What do you mean by absolutely animated? Please specify. ")
        flag = 1
    if " most annoying " in msgs:
        qtns.append(" most annoying ")
        anss.append("What do you mean by most annoying? Please specify. ")
        flag = 1
    if " least annoying " in msgs:
        qtns.append(" least annoying ")
        anss.append("What do you mean by least annoying? Please specify. ")
        flag = 1
    if " very annoying " in msgs:
        qtns.append(" very annoying ")
        anss.append("What do you mean by very annoying? Please specify. ")
        flag = 1
    if " extremely annoying " in msgs:
        qtns.append(" extremely annoying ")
        anss.append("What do you mean by extremely annoying? Please specify. ")
        flag = 1
    if " especially annoying " in msgs:
        qtns.append(" especially annoying ")
        anss.append("What do you mean by especially annoying? Please specify. ")
        flag = 1
    if " absolutely annoying " in msgs:
        qtns.append(" absolutely annoying ")
        anss.append("What do you mean by absolutely annoying? Please specify. ")
        flag = 1
    if " most anxious " in msgs:
        qtns.append(" most anxious ")
        anss.append("What do you mean by most anxious? Please specify. ")
        flag = 1
    if " least anxious " in msgs:
        qtns.append(" least anxious ")
        anss.append("What do you mean by least anxious? Please specify. ")
        flag = 1
    if " very anxious " in msgs:
        qtns.append(" very anxious ")
        anss.append("What do you mean by very anxious? Please specify. ")
        flag = 1
    if " extremely anxious " in msgs:
        qtns.append(" extremely anxious ")
        anss.append("What do you mean by extremely anxious? Please specify. ")
        flag = 1
    if " especially anxious " in msgs:
        qtns.append(" especially anxious ")
        anss.append("What do you mean by especially anxious? Please specify. ")
        flag = 1
    if " absolutely anxious " in msgs:
        qtns.append(" absolutely anxious ")
        anss.append("What do you mean by absolutely anxious? Please specify. ")
        flag = 1
    if " most arrogant " in msgs:
        qtns.append(" most arrogant ")
        anss.append("What do you mean by most arrogant? Please specify. ")
        flag = 1
    if " least arrogant " in msgs:
        qtns.append(" least arrogant ")
        anss.append("What do you mean by least arrogant? Please specify. ")
        flag = 1
    if " very arrogant " in msgs:
        qtns.append(" very arrogant ")
        anss.append("What do you mean by very arrogant? Please specify. ")
        flag = 1
    if " extremely arrogant " in msgs:
        qtns.append(" extremely arrogant ")
        anss.append("What do you mean by extremely arrogant? Please specify. ")
        flag = 1
    if " especially arrogant " in msgs:
        qtns.append(" especially arrogant ")
        anss.append("What do you mean by especially arrogant? Please specify. ")
        flag = 1
    if " absolutely arrogant " in msgs:
        qtns.append(" absolutely arrogant ")
        anss.append("What do you mean by absolutely arrogant? Please specify. ")
        flag = 1
    if " most ashamed " in msgs:
        qtns.append(" most ashamed ")
        anss.append("What do you mean by most ashamed? Please specify. ")
        flag = 1
    if " least ashamed " in msgs:
        qtns.append(" least ashamed ")
        anss.append("What do you mean by least ashamed? Please specify. ")
        flag = 1
    if " very ashamed " in msgs:
        qtns.append(" very ashamed ")
        anss.append("What do you mean by very ashamed? Please specify. ")
        flag = 1
    if " extremely ashamed " in msgs:
        qtns.append(" extremely ashamed ")
        anss.append("What do you mean by extremely ashamed? Please specify. ")
        flag = 1
    if " especially ashamed " in msgs:
        qtns.append(" especially ashamed ")
        anss.append("What do you mean by especially ashamed? Please specify. ")
        flag = 1
    if " absolutely ashamed " in msgs:
        qtns.append(" absolutely ashamed ")
        anss.append("What do you mean by absolutely ashamed? Please specify. ")
        flag = 1
    if " most attractive " in msgs:
        qtns.append(" most attractive ")
        anss.append("What do you mean by most attractive? Please specify. ")
        flag = 1
    if " least attractive " in msgs:
        qtns.append(" least attractive ")
        anss.append("What do you mean by least attractive? Please specify. ")
        flag = 1
    if " very attractive " in msgs:
        qtns.append(" very attractive ")
        anss.append("What do you mean by very attractive? Please specify. ")
        flag = 1
    if " extremely attractive " in msgs:
        qtns.append(" extremely attractive ")
        anss.append("What do you mean by extremely attractive? Please specify. ")
        flag = 1
    if " especially attractive " in msgs:
        qtns.append(" especially attractive ")
        anss.append("What do you mean by especially attractive? Please specify. ")
        flag = 1
    if " absolutely attractive " in msgs:
        qtns.append(" absolutely attractive ")
        anss.append("What do you mean by absolutely attractive? Please specify. ")
        flag = 1
    if " most auspicious " in msgs:
        qtns.append(" most auspicious ")
        anss.append("What do you mean by most auspicious? Please specify. ")
        flag = 1
    if " least auspicious " in msgs:
        qtns.append(" least auspicious ")
        anss.append("What do you mean by least auspicious? Please specify. ")
        flag = 1
    if " very auspicious " in msgs:
        qtns.append(" very auspicious ")
        anss.append("What do you mean by very auspicious? Please specify. ")
        flag = 1
    if " extremely auspicious " in msgs:
        qtns.append(" extremely auspicious ")
        anss.append("What do you mean by extremely auspicious? Please specify. ")
        flag = 1
    if " especially auspicious " in msgs:
        qtns.append(" especially auspicious ")
        anss.append("What do you mean by especially auspicious? Please specify. ")
        flag = 1
    if " absolutely auspicious " in msgs:
        qtns.append(" absolutely auspicious ")
        anss.append("What do you mean by absolutely auspicious? Please specify. ")
        flag = 1
    if " most awesome " in msgs:
        qtns.append(" most awesome ")
        anss.append("What do you mean by most awesome? Please specify. ")
        flag = 1
    if " least awesome " in msgs:
        qtns.append(" least awesome ")
        anss.append("What do you mean by least awesome? Please specify. ")
        flag = 1
    if " very awesome " in msgs:
        qtns.append(" very awesome ")
        anss.append("What do you mean by very awesome? Please specify. ")
        flag = 1
    if " extremely awesome " in msgs:
        qtns.append(" extremely awesome ")
        anss.append("What do you mean by extremely awesome? Please specify. ")
        flag = 1
    if " especially awesome " in msgs:
        qtns.append(" especially awesome ")
        anss.append("What do you mean by especially awesome? Please specify. ")
        flag = 1
    if " absolutely awesome " in msgs:
        qtns.append(" absolutely awesome ")
        anss.append("What do you mean by absolutely awesome? Please specify. ")
        flag = 1
    if " most awful " in msgs:
        qtns.append(" most awful ")
        anss.append("What do you mean by most awful? Please specify. ")
        flag = 1
    if " least awful " in msgs:
        qtns.append(" least awful ")
        anss.append("What do you mean by least awful? Please specify. ")
        flag = 1
    if " very awful " in msgs:
        qtns.append(" very awful ")
        anss.append("What do you mean by very awful? Please specify. ")
        flag = 1
    if " extremely awful " in msgs:
        qtns.append(" extremely awful ")
        anss.append("What do you mean by extremely awful? Please specify. ")
        flag = 1
    if " especially awful " in msgs:
        qtns.append(" especially awful ")
        anss.append("What do you mean by especially awful? Please specify. ")
        flag = 1
    if " absolutely awful " in msgs:
        qtns.append(" absolutely awful ")
        anss.append("What do you mean by absolutely awful? Please specify. ")
        flag = 1
    if " most bad " in msgs:
        qtns.append(" most bad ")
        anss.append("What do you mean by most bad? Please specify. ")
        flag = 1
    if " least bad " in msgs:
        qtns.append(" least bad ")
        anss.append("What do you mean by least bad? Please specify. ")
        flag = 1
    if " very bad " in msgs:
        qtns.append(" very bad ")
        anss.append("What do you mean by very bad? Please specify. ")
        flag = 1
    if " extremely bad " in msgs:
        qtns.append(" extremely bad ")
        anss.append("What do you mean by extremely bad? Please specify. ")
        flag = 1
    if " especially bad " in msgs:
        qtns.append(" especially bad ")
        anss.append("What do you mean by especially bad? Please specify. ")
        flag = 1
    if " absolutely bad " in msgs:
        qtns.append(" absolutely bad ")
        anss.append("What do you mean by absolutely bad? Please specify. ")
        flag = 1
    if " most bad " in msgs:
        qtns.append(" most bad ")
        anss.append("What do you mean by most bad? Please specify. ")
        flag = 1
    if " least bad " in msgs:
        qtns.append(" least bad ")
        anss.append("What do you mean by least bad? Please specify. ")
        flag = 1
    if " very bad " in msgs:
        qtns.append(" very bad ")
        anss.append("What do you mean by very bad? Please specify. ")
        flag = 1
    if " extremely bad " in msgs:
        qtns.append(" extremely bad ")
        anss.append("What do you mean by extremely bad? Please specify. ")
        flag = 1
    if " especially bad " in msgs:
        qtns.append(" especially bad ")
        anss.append("What do you mean by especially bad? Please specify. ")
        flag = 1
    if " absolutely bad " in msgs:
        qtns.append(" absolutely bad ")
        anss.append("What do you mean by absolutely bad? Please specify. ")
        flag = 1
    if " most barren " in msgs:
        qtns.append(" most barren ")
        anss.append("What do you mean by most barren? Please specify. ")
        flag = 1
    if " least barren " in msgs:
        qtns.append(" least barren ")
        anss.append("What do you mean by least barren? Please specify. ")
        flag = 1
    if " very barren " in msgs:
        qtns.append(" very barren ")
        anss.append("What do you mean by very barren? Please specify. ")
        flag = 1
    if " extremely barren " in msgs:
        qtns.append(" extremely barren ")
        anss.append("What do you mean by extremely barren? Please specify. ")
        flag = 1
    if " especially barren " in msgs:
        qtns.append(" especially barren ")
        anss.append("What do you mean by especially barren? Please specify. ")
        flag = 1
    if " absolutely barren " in msgs:
        qtns.append(" absolutely barren ")
        anss.append("What do you mean by absolutely barren? Please specify. ")
        flag = 1
    if " most barricaded " in msgs:
        qtns.append(" most barricaded ")
        anss.append("What do you mean by most barricaded? Please specify. ")
        flag = 1
    if " least barricaded " in msgs:
        qtns.append(" least barricaded ")
        anss.append("What do you mean by least barricaded? Please specify. ")
        flag = 1
    if " very barricaded " in msgs:
        qtns.append(" very barricaded ")
        anss.append("What do you mean by very barricaded? Please specify. ")
        flag = 1
    if " extremely barricaded " in msgs:
        qtns.append(" extremely barricaded ")
        anss.append("What do you mean by extremely barricaded? Please specify. ")
        flag = 1
    if " especially barricaded " in msgs:
        qtns.append(" especially barricaded ")
        anss.append("What do you mean by especially barricaded? Please specify. ")
        flag = 1
    if " absolutely barricaded " in msgs:
        qtns.append(" absolutely barricaded ")
        anss.append("What do you mean by absolutely barricaded? Please specify. ")
        flag = 1
    if " most barytic " in msgs:
        qtns.append(" most barytic ")
        anss.append("What do you mean by most barytic? Please specify. ")
        flag = 1
    if " least barytic " in msgs:
        qtns.append(" least barytic ")
        anss.append("What do you mean by least barytic? Please specify. ")
        flag = 1
    if " very barytic " in msgs:
        qtns.append(" very barytic ")
        anss.append("What do you mean by very barytic? Please specify. ")
        flag = 1
    if " extremely barytic " in msgs:
        qtns.append(" extremely barytic ")
        anss.append("What do you mean by extremely barytic? Please specify. ")
        flag = 1
    if " especially barytic " in msgs:
        qtns.append(" especially barytic ")
        anss.append("What do you mean by especially barytic? Please specify. ")
        flag = 1
    if " absolutely barytic " in msgs:
        qtns.append(" absolutely barytic ")
        anss.append("What do you mean by absolutely barytic? Please specify. ")
        flag = 1
    if " most basal " in msgs:
        qtns.append(" most basal ")
        anss.append("What do you mean by most basal? Please specify. ")
        flag = 1
    if " least basal " in msgs:
        qtns.append(" least basal ")
        anss.append("What do you mean by least basal? Please specify. ")
        flag = 1
    if " very basal " in msgs:
        qtns.append(" very basal ")
        anss.append("What do you mean by very basal? Please specify. ")
        flag = 1
    if " extremely basal " in msgs:
        qtns.append(" extremely basal ")
        anss.append("What do you mean by extremely basal? Please specify. ")
        flag = 1
    if " especially basal " in msgs:
        qtns.append(" especially basal ")
        anss.append("What do you mean by especially basal? Please specify. ")
        flag = 1
    if " absolutely basal " in msgs:
        qtns.append(" absolutely basal ")
        anss.append("What do you mean by absolutely basal? Please specify. ")
        flag = 1
    if " most basaltic " in msgs:
        qtns.append(" most basaltic ")
        anss.append("What do you mean by most basaltic? Please specify. ")
        flag = 1
    if " least basaltic " in msgs:
        qtns.append(" least basaltic ")
        anss.append("What do you mean by least basaltic? Please specify. ")
        flag = 1
    if " very basaltic " in msgs:
        qtns.append(" very basaltic ")
        anss.append("What do you mean by very basaltic? Please specify. ")
        flag = 1
    if " extremely basaltic " in msgs:
        qtns.append(" extremely basaltic ")
        anss.append("What do you mean by extremely basaltic? Please specify. ")
        flag = 1
    if " especially basaltic " in msgs:
        qtns.append(" especially basaltic ")
        anss.append("What do you mean by especially basaltic? Please specify. ")
        flag = 1
    if " absolutely basaltic " in msgs:
        qtns.append(" absolutely basaltic ")
        anss.append("What do you mean by absolutely basaltic? Please specify. ")
        flag = 1
    if " most baseborn " in msgs:
        qtns.append(" most baseborn ")
        anss.append("What do you mean by most baseborn? Please specify. ")
        flag = 1
    if " least baseborn " in msgs:
        qtns.append(" least baseborn ")
        anss.append("What do you mean by least baseborn? Please specify. ")
        flag = 1
    if " very baseborn " in msgs:
        qtns.append(" very baseborn ")
        anss.append("What do you mean by very baseborn? Please specify. ")
        flag = 1
    if " extremely baseborn " in msgs:
        qtns.append(" extremely baseborn ")
        anss.append("What do you mean by extremely baseborn? Please specify. ")
        flag = 1
    if " especially baseborn " in msgs:
        qtns.append(" especially baseborn ")
        anss.append("What do you mean by especially baseborn? Please specify. ")
        flag = 1
    if " absolutely baseborn " in msgs:
        qtns.append(" absolutely baseborn ")
        anss.append("What do you mean by absolutely baseborn? Please specify. ")
        flag = 1
    if " most based " in msgs:
        qtns.append(" most based ")
        anss.append("What do you mean by most based? Please specify. ")
        flag = 1
    if " least based " in msgs:
        qtns.append(" least based ")
        anss.append("What do you mean by least based? Please specify. ")
        flag = 1
    if " very based " in msgs:
        qtns.append(" very based ")
        anss.append("What do you mean by very based? Please specify. ")
        flag = 1
    if " extremely based " in msgs:
        qtns.append(" extremely based ")
        anss.append("What do you mean by extremely based? Please specify. ")
        flag = 1
    if " especially based " in msgs:
        qtns.append(" especially based ")
        anss.append("What do you mean by especially based? Please specify. ")
        flag = 1
    if " absolutely based " in msgs:
        qtns.append(" absolutely based ")
        anss.append("What do you mean by absolutely based? Please specify. ")
        flag = 1
    if " most baseless " in msgs:
        qtns.append(" most baseless ")
        anss.append("What do you mean by most baseless? Please specify. ")
        flag = 1
    if " least baseless " in msgs:
        qtns.append(" least baseless ")
        anss.append("What do you mean by least baseless? Please specify. ")
        flag = 1
    if " very baseless " in msgs:
        qtns.append(" very baseless ")
        anss.append("What do you mean by very baseless? Please specify. ")
        flag = 1
    if " extremely baseless " in msgs:
        qtns.append(" extremely baseless ")
        anss.append("What do you mean by extremely baseless? Please specify. ")
        flag = 1
    if " especially baseless " in msgs:
        qtns.append(" especially baseless ")
        anss.append("What do you mean by especially baseless? Please specify. ")
        flag = 1
    if " absolutely baseless " in msgs:
        qtns.append(" absolutely baseless ")
        anss.append("What do you mean by absolutely baseless? Please specify. ")
        flag = 1
    if " most bashful " in msgs:
        qtns.append(" most bashful ")
        anss.append("What do you mean by most bashful? Please specify. ")
        flag = 1
    if " least bashful " in msgs:
        qtns.append(" least bashful ")
        anss.append("What do you mean by least bashful? Please specify. ")
        flag = 1
    if " very bashful " in msgs:
        qtns.append(" very bashful ")
        anss.append("What do you mean by very bashful? Please specify. ")
        flag = 1
    if " extremely bashful " in msgs:
        qtns.append(" extremely bashful ")
        anss.append("What do you mean by extremely bashful? Please specify. ")
        flag = 1
    if " especially bashful " in msgs:
        qtns.append(" especially bashful ")
        anss.append("What do you mean by especially bashful? Please specify. ")
        flag = 1
    if " absolutely bashful " in msgs:
        qtns.append(" absolutely bashful ")
        anss.append("What do you mean by absolutely bashful? Please specify. ")
        flag = 1
    if " most basic " in msgs:
        qtns.append(" most basic ")
        anss.append("What do you mean by most basic? Please specify. ")
        flag = 1
    if " least basic " in msgs:
        qtns.append(" least basic ")
        anss.append("What do you mean by least basic? Please specify. ")
        flag = 1
    if " very basic " in msgs:
        qtns.append(" very basic ")
        anss.append("What do you mean by very basic? Please specify. ")
        flag = 1
    if " extremely basic " in msgs:
        qtns.append(" extremely basic ")
        anss.append("What do you mean by extremely basic? Please specify. ")
        flag = 1
    if " especially basic " in msgs:
        qtns.append(" especially basic ")
        anss.append("What do you mean by especially basic? Please specify. ")
        flag = 1
    if " absolutely basic " in msgs:
        qtns.append(" absolutely basic ")
        anss.append("What do you mean by absolutely basic? Please specify. ")
        flag = 1
    if " most bathyal " in msgs:
        qtns.append(" most bathyal ")
        anss.append("What do you mean by most bathyal? Please specify. ")
        flag = 1
    if " least bathyal " in msgs:
        qtns.append(" least bathyal ")
        anss.append("What do you mean by least bathyal? Please specify. ")
        flag = 1
    if " very bathyal " in msgs:
        qtns.append(" very bathyal ")
        anss.append("What do you mean by very bathyal? Please specify. ")
        flag = 1
    if " extremely bathyal " in msgs:
        qtns.append(" extremely bathyal ")
        anss.append("What do you mean by extremely bathyal? Please specify. ")
        flag = 1
    if " especially bathyal " in msgs:
        qtns.append(" especially bathyal ")
        anss.append("What do you mean by especially bathyal? Please specify. ")
        flag = 1
    if " absolutely bathyal " in msgs:
        qtns.append(" absolutely bathyal ")
        anss.append("What do you mean by absolutely bathyal? Please specify. ")
        flag = 1
    if " most battleful " in msgs:
        qtns.append(" most battleful ")
        anss.append("What do you mean by most battleful? Please specify. ")
        flag = 1
    if " least battleful " in msgs:
        qtns.append(" least battleful ")
        anss.append("What do you mean by least battleful? Please specify. ")
        flag = 1
    if " very battleful " in msgs:
        qtns.append(" very battleful ")
        anss.append("What do you mean by very battleful? Please specify. ")
        flag = 1
    if " extremely battleful " in msgs:
        qtns.append(" extremely battleful ")
        anss.append("What do you mean by extremely battleful? Please specify. ")
        flag = 1
    if " especially battleful " in msgs:
        qtns.append(" especially battleful ")
        anss.append("What do you mean by especially battleful? Please specify. ")
        flag = 1
    if " absolutely battleful " in msgs:
        qtns.append(" absolutely battleful ")
        anss.append("What do you mean by absolutely battleful? Please specify. ")
        flag = 1
    if " most battlemented " in msgs:
        qtns.append(" most battlemented ")
        anss.append("What do you mean by most battlemented? Please specify. ")
        flag = 1
    if " least battlemented " in msgs:
        qtns.append(" least battlemented ")
        anss.append("What do you mean by least battlemented? Please specify. ")
        flag = 1
    if " very battlemented " in msgs:
        qtns.append(" very battlemented ")
        anss.append("What do you mean by very battlemented? Please specify. ")
        flag = 1
    if " extremely battlemented " in msgs:
        qtns.append(" extremely battlemented ")
        anss.append("What do you mean by extremely battlemented? Please specify. ")
        flag = 1
    if " especially battlemented " in msgs:
        qtns.append(" especially battlemented ")
        anss.append("What do you mean by especially battlemented? Please specify. ")
        flag = 1
    if " absolutely battlemented " in msgs:
        qtns.append(" absolutely battlemented ")
        anss.append("What do you mean by absolutely battlemented? Please specify. ")
        flag = 1
    if " most batty " in msgs:
        qtns.append(" most batty ")
        anss.append("What do you mean by most batty? Please specify. ")
        flag = 1
    if " least batty " in msgs:
        qtns.append(" least batty ")
        anss.append("What do you mean by least batty? Please specify. ")
        flag = 1
    if " very batty " in msgs:
        qtns.append(" very batty ")
        anss.append("What do you mean by very batty? Please specify. ")
        flag = 1
    if " extremely batty " in msgs:
        qtns.append(" extremely batty ")
        anss.append("What do you mean by extremely batty? Please specify. ")
        flag = 1
    if " especially batty " in msgs:
        qtns.append(" especially batty ")
        anss.append("What do you mean by especially batty? Please specify. ")
        flag = 1
    if " absolutely batty " in msgs:
        qtns.append(" absolutely batty ")
        anss.append("What do you mean by absolutely batty? Please specify. ")
        flag = 1
    if " most batwing " in msgs:
        qtns.append(" most batwing ")
        anss.append("What do you mean by most batwing? Please specify. ")
        flag = 1
    if " least batwing " in msgs:
        qtns.append(" least batwing ")
        anss.append("What do you mean by least batwing? Please specify. ")
        flag = 1
    if " very batwing " in msgs:
        qtns.append(" very batwing ")
        anss.append("What do you mean by very batwing? Please specify. ")
        flag = 1
    if " extremely batwing " in msgs:
        qtns.append(" extremely batwing ")
        anss.append("What do you mean by extremely batwing? Please specify. ")
        flag = 1
    if " especially batwing " in msgs:
        qtns.append(" especially batwing ")
        anss.append("What do you mean by especially batwing? Please specify. ")
        flag = 1
    if " absolutely batwing " in msgs:
        qtns.append(" absolutely batwing ")
        anss.append("What do you mean by absolutely batwing? Please specify. ")
        flag = 1
    if " most beautiful " in msgs:
        qtns.append(" most beautiful ")
        anss.append("What do you mean by most beautiful? Please specify. ")
        flag = 1
    if " least beautiful " in msgs:
        qtns.append(" least beautiful ")
        anss.append("What do you mean by least beautiful? Please specify. ")
        flag = 1
    if " very beautiful " in msgs:
        qtns.append(" very beautiful ")
        anss.append("What do you mean by very beautiful? Please specify. ")
        flag = 1
    if " extremely beautiful " in msgs:
        qtns.append(" extremely beautiful ")
        anss.append("What do you mean by extremely beautiful? Please specify. ")
        flag = 1
    if " especially beautiful " in msgs:
        qtns.append(" especially beautiful ")
        anss.append("What do you mean by especially beautiful? Please specify. ")
        flag = 1
    if " absolutely beautiful " in msgs:
        qtns.append(" absolutely beautiful ")
        anss.append("What do you mean by absolutely beautiful? Please specify. ")
        flag = 1
    if " most belligerent " in msgs:
        qtns.append(" most belligerent ")
        anss.append("What do you mean by most belligerent? Please specify. ")
        flag = 1
    if " least belligerent " in msgs:
        qtns.append(" least belligerent ")
        anss.append("What do you mean by least belligerent? Please specify. ")
        flag = 1
    if " very belligerent " in msgs:
        qtns.append(" very belligerent ")
        anss.append("What do you mean by very belligerent? Please specify. ")
        flag = 1
    if " extremely belligerent " in msgs:
        qtns.append(" extremely belligerent ")
        anss.append("What do you mean by extremely belligerent? Please specify. ")
        flag = 1
    if " especially belligerent " in msgs:
        qtns.append(" especially belligerent ")
        anss.append("What do you mean by especially belligerent? Please specify. ")
        flag = 1
    if " absolutely belligerent " in msgs:
        qtns.append(" absolutely belligerent ")
        anss.append("What do you mean by absolutely belligerent? Please specify. ")
        flag = 1
    if " most beneficial " in msgs:
        qtns.append(" most beneficial ")
        anss.append("What do you mean by most beneficial? Please specify. ")
        flag = 1
    if " least beneficial " in msgs:
        qtns.append(" least beneficial ")
        anss.append("What do you mean by least beneficial? Please specify. ")
        flag = 1
    if " very beneficial " in msgs:
        qtns.append(" very beneficial ")
        anss.append("What do you mean by very beneficial? Please specify. ")
        flag = 1
    if " extremely beneficial " in msgs:
        qtns.append(" extremely beneficial ")
        anss.append("What do you mean by extremely beneficial? Please specify. ")
        flag = 1
    if " especially beneficial " in msgs:
        qtns.append(" especially beneficial ")
        anss.append("What do you mean by especially beneficial? Please specify. ")
        flag = 1
    if " absolutely beneficial " in msgs:
        qtns.append(" absolutely beneficial ")
        anss.append("What do you mean by absolutely beneficial? Please specify. ")
        flag = 1
    if " most biased " in msgs:
        qtns.append(" most biased ")
        anss.append("What do you mean by most biased? Please specify. ")
        flag = 1
    if " least biased " in msgs:
        qtns.append(" least biased ")
        anss.append("What do you mean by least biased? Please specify. ")
        flag = 1
    if " very biased " in msgs:
        qtns.append(" very biased ")
        anss.append("What do you mean by very biased? Please specify. ")
        flag = 1
    if " extremely biased " in msgs:
        qtns.append(" extremely biased ")
        anss.append("What do you mean by extremely biased? Please specify. ")
        flag = 1
    if " especially biased " in msgs:
        qtns.append(" especially biased ")
        anss.append("What do you mean by especially biased? Please specify. ")
        flag = 1
    if " absolutely biased " in msgs:
        qtns.append(" absolutely biased ")
        anss.append("What do you mean by absolutely biased? Please specify. ")
        flag = 1
    if " most big " in msgs:
        qtns.append(" most big ")
        anss.append("What do you mean by most big? Please specify. ")
        flag = 1
    if " least big " in msgs:
        qtns.append(" least big ")
        anss.append("What do you mean by least big? Please specify. ")
        flag = 1
    if " very big " in msgs:
        qtns.append(" very big ")
        anss.append("What do you mean by very big? Please specify. ")
        flag = 1
    if " extremely big " in msgs:
        qtns.append(" extremely big ")
        anss.append("What do you mean by extremely big? Please specify. ")
        flag = 1
    if " especially big " in msgs:
        qtns.append(" especially big ")
        anss.append("What do you mean by especially big? Please specify. ")
        flag = 1
    if " absolutely big " in msgs:
        qtns.append(" absolutely big ")
        anss.append("What do you mean by absolutely big? Please specify. ")
        flag = 1
    if " most bitter " in msgs:
        qtns.append(" most bitter ")
        anss.append("What do you mean by most bitter? Please specify. ")
        flag = 1
    if " least bitter " in msgs:
        qtns.append(" least bitter ")
        anss.append("What do you mean by least bitter? Please specify. ")
        flag = 1
    if " very bitter " in msgs:
        qtns.append(" very bitter ")
        anss.append("What do you mean by very bitter? Please specify. ")
        flag = 1
    if " extremely bitter " in msgs:
        qtns.append(" extremely bitter ")
        anss.append("What do you mean by extremely bitter? Please specify. ")
        flag = 1
    if " especially bitter " in msgs:
        qtns.append(" especially bitter ")
        anss.append("What do you mean by especially bitter? Please specify. ")
        flag = 1
    if " absolutely bitter " in msgs:
        qtns.append(" absolutely bitter ")
        anss.append("What do you mean by absolutely bitter? Please specify. ")
        flag = 1
    if " most bitter " in msgs:
        qtns.append(" most bitter ")
        anss.append("What do you mean by most bitter? Please specify. ")
        flag = 1
    if " least bitter " in msgs:
        qtns.append(" least bitter ")
        anss.append("What do you mean by least bitter? Please specify. ")
        flag = 1
    if " very bitter " in msgs:
        qtns.append(" very bitter ")
        anss.append("What do you mean by very bitter? Please specify. ")
        flag = 1
    if " extremely bitter " in msgs:
        qtns.append(" extremely bitter ")
        anss.append("What do you mean by extremely bitter? Please specify. ")
        flag = 1
    if " especially bitter " in msgs:
        qtns.append(" especially bitter ")
        anss.append("What do you mean by especially bitter? Please specify. ")
        flag = 1
    if " absolutely bitter " in msgs:
        qtns.append(" absolutely bitter ")
        anss.append("What do you mean by absolutely bitter? Please specify. ")
        flag = 1
    if " most bizarre " in msgs:
        qtns.append(" most bizarre ")
        anss.append("What do you mean by most bizarre? Please specify. ")
        flag = 1
    if " least bizarre " in msgs:
        qtns.append(" least bizarre ")
        anss.append("What do you mean by least bizarre? Please specify. ")
        flag = 1
    if " very bizarre " in msgs:
        qtns.append(" very bizarre ")
        anss.append("What do you mean by very bizarre? Please specify. ")
        flag = 1
    if " extremely bizarre " in msgs:
        qtns.append(" extremely bizarre ")
        anss.append("What do you mean by extremely bizarre? Please specify. ")
        flag = 1
    if " especially bizarre " in msgs:
        qtns.append(" especially bizarre ")
        anss.append("What do you mean by especially bizarre? Please specify. ")
        flag = 1
    if " absolutely bizarre " in msgs:
        qtns.append(" absolutely bizarre ")
        anss.append("What do you mean by absolutely bizarre? Please specify. ")
        flag = 1
    if " most black " in msgs:
        qtns.append(" most black ")
        anss.append("What do you mean by most black? Please specify. ")
        flag = 1
    if " least black " in msgs:
        qtns.append(" least black ")
        anss.append("What do you mean by least black? Please specify. ")
        flag = 1
    if " very black " in msgs:
        qtns.append(" very black ")
        anss.append("What do you mean by very black? Please specify. ")
        flag = 1
    if " extremely black " in msgs:
        qtns.append(" extremely black ")
        anss.append("What do you mean by extremely black? Please specify. ")
        flag = 1
    if " especially black " in msgs:
        qtns.append(" especially black ")
        anss.append("What do you mean by especially black? Please specify. ")
        flag = 1
    if " absolutely black " in msgs:
        qtns.append(" absolutely black ")
        anss.append("What do you mean by absolutely black? Please specify. ")
        flag = 1
    if " most bland " in msgs:
        qtns.append(" most bland ")
        anss.append("What do you mean by most bland? Please specify. ")
        flag = 1
    if " least bland " in msgs:
        qtns.append(" least bland ")
        anss.append("What do you mean by least bland? Please specify. ")
        flag = 1
    if " very bland " in msgs:
        qtns.append(" very bland ")
        anss.append("What do you mean by very bland? Please specify. ")
        flag = 1
    if " extremely bland " in msgs:
        qtns.append(" extremely bland ")
        anss.append("What do you mean by extremely bland? Please specify. ")
        flag = 1
    if " especially bland " in msgs:
        qtns.append(" especially bland ")
        anss.append("What do you mean by especially bland? Please specify. ")
        flag = 1
    if " absolutely bland " in msgs:
        qtns.append(" absolutely bland ")
        anss.append("What do you mean by absolutely bland? Please specify. ")
        flag = 1
    if " most bloody " in msgs:
        qtns.append(" most bloody ")
        anss.append("What do you mean by most bloody? Please specify. ")
        flag = 1
    if " least bloody " in msgs:
        qtns.append(" least bloody ")
        anss.append("What do you mean by least bloody? Please specify. ")
        flag = 1
    if " very bloody " in msgs:
        qtns.append(" very bloody ")
        anss.append("What do you mean by very bloody? Please specify. ")
        flag = 1
    if " extremely bloody " in msgs:
        qtns.append(" extremely bloody ")
        anss.append("What do you mean by extremely bloody? Please specify. ")
        flag = 1
    if " especially bloody " in msgs:
        qtns.append(" especially bloody ")
        anss.append("What do you mean by especially bloody? Please specify. ")
        flag = 1
    if " absolutely bloody " in msgs:
        qtns.append(" absolutely bloody ")
        anss.append("What do you mean by absolutely bloody? Please specify. ")
        flag = 1
    if " most blue " in msgs:
        qtns.append(" most blue ")
        anss.append("What do you mean by most blue? Please specify. ")
        flag = 1
    if " least blue " in msgs:
        qtns.append(" least blue ")
        anss.append("What do you mean by least blue? Please specify. ")
        flag = 1
    if " very blue " in msgs:
        qtns.append(" very blue ")
        anss.append("What do you mean by very blue? Please specify. ")
        flag = 1
    if " extremely blue " in msgs:
        qtns.append(" extremely blue ")
        anss.append("What do you mean by extremely blue? Please specify. ")
        flag = 1
    if " especially blue " in msgs:
        qtns.append(" especially blue ")
        anss.append("What do you mean by especially blue? Please specify. ")
        flag = 1
    if " absolutely blue " in msgs:
        qtns.append(" absolutely blue ")
        anss.append("What do you mean by absolutely blue? Please specify. ")
        flag = 1
    if " most bold " in msgs:
        qtns.append(" most bold ")
        anss.append("What do you mean by most bold? Please specify. ")
        flag = 1
    if " least bold " in msgs:
        qtns.append(" least bold ")
        anss.append("What do you mean by least bold? Please specify. ")
        flag = 1
    if " very bold " in msgs:
        qtns.append(" very bold ")
        anss.append("What do you mean by very bold? Please specify. ")
        flag = 1
    if " extremely bold " in msgs:
        qtns.append(" extremely bold ")
        anss.append("What do you mean by extremely bold? Please specify. ")
        flag = 1
    if " especially bold " in msgs:
        qtns.append(" especially bold ")
        anss.append("What do you mean by especially bold? Please specify. ")
        flag = 1
    if " absolutely bold " in msgs:
        qtns.append(" absolutely bold ")
        anss.append("What do you mean by absolutely bold? Please specify. ")
        flag = 1
    if " most boring " in msgs:
        qtns.append(" most boring ")
        anss.append("What do you mean by most boring? Please specify. ")
        flag = 1
    if " least boring " in msgs:
        qtns.append(" least boring ")
        anss.append("What do you mean by least boring? Please specify. ")
        flag = 1
    if " very boring " in msgs:
        qtns.append(" very boring ")
        anss.append("What do you mean by very boring? Please specify. ")
        flag = 1
    if " extremely boring " in msgs:
        qtns.append(" extremely boring ")
        anss.append("What do you mean by extremely boring? Please specify. ")
        flag = 1
    if " especially boring " in msgs:
        qtns.append(" especially boring ")
        anss.append("What do you mean by especially boring? Please specify. ")
        flag = 1
    if " absolutely boring " in msgs:
        qtns.append(" absolutely boring ")
        anss.append("What do you mean by absolutely boring? Please specify. ")
        flag = 1
    if " most bossy " in msgs:
        qtns.append(" most bossy ")
        anss.append("What do you mean by most bossy? Please specify. ")
        flag = 1
    if " least bossy " in msgs:
        qtns.append(" least bossy ")
        anss.append("What do you mean by least bossy? Please specify. ")
        flag = 1
    if " very bossy " in msgs:
        qtns.append(" very bossy ")
        anss.append("What do you mean by very bossy? Please specify. ")
        flag = 1
    if " extremely bossy " in msgs:
        qtns.append(" extremely bossy ")
        anss.append("What do you mean by extremely bossy? Please specify. ")
        flag = 1
    if " especially bossy " in msgs:
        qtns.append(" especially bossy ")
        anss.append("What do you mean by especially bossy? Please specify. ")
        flag = 1
    if " absolutely bossy " in msgs:
        qtns.append(" absolutely bossy ")
        anss.append("What do you mean by absolutely bossy? Please specify. ")
        flag = 1
    if " most brainy " in msgs:
        qtns.append(" most brainy ")
        anss.append("What do you mean by most brainy? Please specify. ")
        flag = 1
    if " least brainy " in msgs:
        qtns.append(" least brainy ")
        anss.append("What do you mean by least brainy? Please specify. ")
        flag = 1
    if " very brainy " in msgs:
        qtns.append(" very brainy ")
        anss.append("What do you mean by very brainy? Please specify. ")
        flag = 1
    if " extremely brainy " in msgs:
        qtns.append(" extremely brainy ")
        anss.append("What do you mean by extremely brainy? Please specify. ")
        flag = 1
    if " especially brainy " in msgs:
        qtns.append(" especially brainy ")
        anss.append("What do you mean by especially brainy? Please specify. ")
        flag = 1
    if " absolutely brainy " in msgs:
        qtns.append(" absolutely brainy ")
        anss.append("What do you mean by absolutely brainy? Please specify. ")
        flag = 1
    if " most brainy " in msgs:
        qtns.append(" most brainy ")
        anss.append("What do you mean by most brainy? Please specify. ")
        flag = 1
    if " least brainy " in msgs:
        qtns.append(" least brainy ")
        anss.append("What do you mean by least brainy? Please specify. ")
        flag = 1
    if " very brainy " in msgs:
        qtns.append(" very brainy ")
        anss.append("What do you mean by very brainy? Please specify. ")
        flag = 1
    if " extremely brainy " in msgs:
        qtns.append(" extremely brainy ")
        anss.append("What do you mean by extremely brainy? Please specify. ")
        flag = 1
    if " especially brainy " in msgs:
        qtns.append(" especially brainy ")
        anss.append("What do you mean by especially brainy? Please specify. ")
        flag = 1
    if " absolutely brainy " in msgs:
        qtns.append(" absolutely brainy ")
        anss.append("What do you mean by absolutely brainy? Please specify. ")
        flag = 1
    if " most brave " in msgs:
        qtns.append(" most brave ")
        anss.append("What do you mean by most brave? Please specify. ")
        flag = 1
    if " least brave " in msgs:
        qtns.append(" least brave ")
        anss.append("What do you mean by least brave? Please specify. ")
        flag = 1
    if " very brave " in msgs:
        qtns.append(" very brave ")
        anss.append("What do you mean by very brave? Please specify. ")
        flag = 1
    if " extremely brave " in msgs:
        qtns.append(" extremely brave ")
        anss.append("What do you mean by extremely brave? Please specify. ")
        flag = 1
    if " especially brave " in msgs:
        qtns.append(" especially brave ")
        anss.append("What do you mean by especially brave? Please specify. ")
        flag = 1
    if " absolutely brave " in msgs:
        qtns.append(" absolutely brave ")
        anss.append("What do you mean by absolutely brave? Please specify. ")
        flag = 1
    if " most brief " in msgs:
        qtns.append(" most brief ")
        anss.append("What do you mean by most brief? Please specify. ")
        flag = 1
    if " least brief " in msgs:
        qtns.append(" least brief ")
        anss.append("What do you mean by least brief? Please specify. ")
        flag = 1
    if " very brief " in msgs:
        qtns.append(" very brief ")
        anss.append("What do you mean by very brief? Please specify. ")
        flag = 1
    if " extremely brief " in msgs:
        qtns.append(" extremely brief ")
        anss.append("What do you mean by extremely brief? Please specify. ")
        flag = 1
    if " especially brief " in msgs:
        qtns.append(" especially brief ")
        anss.append("What do you mean by especially brief? Please specify. ")
        flag = 1
    if " absolutely brief " in msgs:
        qtns.append(" absolutely brief ")
        anss.append("What do you mean by absolutely brief? Please specify. ")
        flag = 1
    if " most bright " in msgs:
        qtns.append(" most bright ")
        anss.append("What do you mean by most bright? Please specify. ")
        flag = 1
    if " least bright " in msgs:
        qtns.append(" least bright ")
        anss.append("What do you mean by least bright? Please specify. ")
        flag = 1
    if " very bright " in msgs:
        qtns.append(" very bright ")
        anss.append("What do you mean by very bright? Please specify. ")
        flag = 1
    if " extremely bright " in msgs:
        qtns.append(" extremely bright ")
        anss.append("What do you mean by extremely bright? Please specify. ")
        flag = 1
    if " especially bright " in msgs:
        qtns.append(" especially bright ")
        anss.append("What do you mean by especially bright? Please specify. ")
        flag = 1
    if " absolutely bright " in msgs:
        qtns.append(" absolutely bright ")
        anss.append("What do you mean by absolutely bright? Please specify. ")
        flag = 1
    if " most broad " in msgs:
        qtns.append(" most broad ")
        anss.append("What do you mean by most broad? Please specify. ")
        flag = 1
    if " least broad " in msgs:
        qtns.append(" least broad ")
        anss.append("What do you mean by least broad? Please specify. ")
        flag = 1
    if " very broad " in msgs:
        qtns.append(" very broad ")
        anss.append("What do you mean by very broad? Please specify. ")
        flag = 1
    if " extremely broad " in msgs:
        qtns.append(" extremely broad ")
        anss.append("What do you mean by extremely broad? Please specify. ")
        flag = 1
    if " especially broad " in msgs:
        qtns.append(" especially broad ")
        anss.append("What do you mean by especially broad? Please specify. ")
        flag = 1
    if " absolutely broad " in msgs:
        qtns.append(" absolutely broad ")
        anss.append("What do you mean by absolutely broad? Please specify. ")
        flag = 1
    if " most broken " in msgs:
        qtns.append(" most broken ")
        anss.append("What do you mean by most broken? Please specify. ")
        flag = 1
    if " least broken " in msgs:
        qtns.append(" least broken ")
        anss.append("What do you mean by least broken? Please specify. ")
        flag = 1
    if " very broken " in msgs:
        qtns.append(" very broken ")
        anss.append("What do you mean by very broken? Please specify. ")
        flag = 1
    if " extremely broken " in msgs:
        qtns.append(" extremely broken ")
        anss.append("What do you mean by extremely broken? Please specify. ")
        flag = 1
    if " especially broken " in msgs:
        qtns.append(" especially broken ")
        anss.append("What do you mean by especially broken? Please specify. ")
        flag = 1
    if " absolutely broken " in msgs:
        qtns.append(" absolutely broken ")
        anss.append("What do you mean by absolutely broken? Please specify. ")
        flag = 1
    if " most busy " in msgs:
        qtns.append(" most busy ")
        anss.append("What do you mean by most busy? Please specify. ")
        flag = 1
    if " least busy " in msgs:
        qtns.append(" least busy ")
        anss.append("What do you mean by least busy? Please specify. ")
        flag = 1
    if " very busy " in msgs:
        qtns.append(" very busy ")
        anss.append("What do you mean by very busy? Please specify. ")
        flag = 1
    if " extremely busy " in msgs:
        qtns.append(" extremely busy ")
        anss.append("What do you mean by extremely busy? Please specify. ")
        flag = 1
    if " especially busy " in msgs:
        qtns.append(" especially busy ")
        anss.append("What do you mean by especially busy? Please specify. ")
        flag = 1
    if " absolutely busy " in msgs:
        qtns.append(" absolutely busy ")
        anss.append("What do you mean by absolutely busy? Please specify. ")
        flag = 1
    if " most calm " in msgs:
        qtns.append(" most calm ")
        anss.append("What do you mean by most calm? Please specify. ")
        flag = 1
    if " least calm " in msgs:
        qtns.append(" least calm ")
        anss.append("What do you mean by least calm? Please specify. ")
        flag = 1
    if " very calm " in msgs:
        qtns.append(" very calm ")
        anss.append("What do you mean by very calm? Please specify. ")
        flag = 1
    if " extremely calm " in msgs:
        qtns.append(" extremely calm ")
        anss.append("What do you mean by extremely calm? Please specify. ")
        flag = 1
    if " especially calm " in msgs:
        qtns.append(" especially calm ")
        anss.append("What do you mean by especially calm? Please specify. ")
        flag = 1
    if " absolutely calm " in msgs:
        qtns.append(" absolutely calm ")
        anss.append("What do you mean by absolutely calm? Please specify. ")
        flag = 1
    if " most capable " in msgs:
        qtns.append(" most capable ")
        anss.append("What do you mean by most capable? Please specify. ")
        flag = 1
    if " least capable " in msgs:
        qtns.append(" least capable ")
        anss.append("What do you mean by least capable? Please specify. ")
        flag = 1
    if " very capable " in msgs:
        qtns.append(" very capable ")
        anss.append("What do you mean by very capable? Please specify. ")
        flag = 1
    if " extremely capable " in msgs:
        qtns.append(" extremely capable ")
        anss.append("What do you mean by extremely capable? Please specify. ")
        flag = 1
    if " especially capable " in msgs:
        qtns.append(" especially capable ")
        anss.append("What do you mean by especially capable? Please specify. ")
        flag = 1
    if " absolutely capable " in msgs:
        qtns.append(" absolutely capable ")
        anss.append("What do you mean by absolutely capable? Please specify. ")
        flag = 1
    if " most careful " in msgs:
        qtns.append(" most careful ")
        anss.append("What do you mean by most careful? Please specify. ")
        flag = 1
    if " least careful " in msgs:
        qtns.append(" least careful ")
        anss.append("What do you mean by least careful? Please specify. ")
        flag = 1
    if " very careful " in msgs:
        qtns.append(" very careful ")
        anss.append("What do you mean by very careful? Please specify. ")
        flag = 1
    if " extremely careful " in msgs:
        qtns.append(" extremely careful ")
        anss.append("What do you mean by extremely careful? Please specify. ")
        flag = 1
    if " especially careful " in msgs:
        qtns.append(" especially careful ")
        anss.append("What do you mean by especially careful? Please specify. ")
        flag = 1
    if " absolutely careful " in msgs:
        qtns.append(" absolutely careful ")
        anss.append("What do you mean by absolutely careful? Please specify. ")
        flag = 1
    if " most careless " in msgs:
        qtns.append(" most careless ")
        anss.append("What do you mean by most careless? Please specify. ")
        flag = 1
    if " least careless " in msgs:
        qtns.append(" least careless ")
        anss.append("What do you mean by least careless? Please specify. ")
        flag = 1
    if " very careless " in msgs:
        qtns.append(" very careless ")
        anss.append("What do you mean by very careless? Please specify. ")
        flag = 1
    if " extremely careless " in msgs:
        qtns.append(" extremely careless ")
        anss.append("What do you mean by extremely careless? Please specify. ")
        flag = 1
    if " especially careless " in msgs:
        qtns.append(" especially careless ")
        anss.append("What do you mean by especially careless? Please specify. ")
        flag = 1
    if " absolutely careless " in msgs:
        qtns.append(" absolutely careless ")
        anss.append("What do you mean by absolutely careless? Please specify. ")
        flag = 1
    if " most caring " in msgs:
        qtns.append(" most caring ")
        anss.append("What do you mean by most caring? Please specify. ")
        flag = 1
    if " least caring " in msgs:
        qtns.append(" least caring ")
        anss.append("What do you mean by least caring? Please specify. ")
        flag = 1
    if " very caring " in msgs:
        qtns.append(" very caring ")
        anss.append("What do you mean by very caring? Please specify. ")
        flag = 1
    if " extremely caring " in msgs:
        qtns.append(" extremely caring ")
        anss.append("What do you mean by extremely caring? Please specify. ")
        flag = 1
    if " especially caring " in msgs:
        qtns.append(" especially caring ")
        anss.append("What do you mean by especially caring? Please specify. ")
        flag = 1
    if " absolutely caring " in msgs:
        qtns.append(" absolutely caring ")
        anss.append("What do you mean by absolutely caring? Please specify. ")
        flag = 1
    if " most cautious " in msgs:
        qtns.append(" most cautious ")
        anss.append("What do you mean by most cautious? Please specify. ")
        flag = 1
    if " least cautious " in msgs:
        qtns.append(" least cautious ")
        anss.append("What do you mean by least cautious? Please specify. ")
        flag = 1
    if " very cautious " in msgs:
        qtns.append(" very cautious ")
        anss.append("What do you mean by very cautious? Please specify. ")
        flag = 1
    if " extremely cautious " in msgs:
        qtns.append(" extremely cautious ")
        anss.append("What do you mean by extremely cautious? Please specify. ")
        flag = 1
    if " especially cautious " in msgs:
        qtns.append(" especially cautious ")
        anss.append("What do you mean by especially cautious? Please specify. ")
        flag = 1
    if " absolutely cautious " in msgs:
        qtns.append(" absolutely cautious ")
        anss.append("What do you mean by absolutely cautious? Please specify. ")
        flag = 1
    if " most charming " in msgs:
        qtns.append(" most charming ")
        anss.append("What do you mean by most charming? Please specify. ")
        flag = 1
    if " least charming " in msgs:
        qtns.append(" least charming ")
        anss.append("What do you mean by least charming? Please specify. ")
        flag = 1
    if " very charming " in msgs:
        qtns.append(" very charming ")
        anss.append("What do you mean by very charming? Please specify. ")
        flag = 1
    if " extremely charming " in msgs:
        qtns.append(" extremely charming ")
        anss.append("What do you mean by extremely charming? Please specify. ")
        flag = 1
    if " especially charming " in msgs:
        qtns.append(" especially charming ")
        anss.append("What do you mean by especially charming? Please specify. ")
        flag = 1
    if " absolutely charming " in msgs:
        qtns.append(" absolutely charming ")
        anss.append("What do you mean by absolutely charming? Please specify. ")
        flag = 1
    if " most cheap " in msgs:
        qtns.append(" most cheap ")
        anss.append("What do you mean by most cheap? Please specify. ")
        flag = 1
    if " least cheap " in msgs:
        qtns.append(" least cheap ")
        anss.append("What do you mean by least cheap? Please specify. ")
        flag = 1
    if " very cheap " in msgs:
        qtns.append(" very cheap ")
        anss.append("What do you mean by very cheap? Please specify. ")
        flag = 1
    if " extremely cheap " in msgs:
        qtns.append(" extremely cheap ")
        anss.append("What do you mean by extremely cheap? Please specify. ")
        flag = 1
    if " especially cheap " in msgs:
        qtns.append(" especially cheap ")
        anss.append("What do you mean by especially cheap? Please specify. ")
        flag = 1
    if " absolutely cheap " in msgs:
        qtns.append(" absolutely cheap ")
        anss.append("What do you mean by absolutely cheap? Please specify. ")
        flag = 1
    if " most cheerful " in msgs:
        qtns.append(" most cheerful ")
        anss.append("What do you mean by most cheerful? Please specify. ")
        flag = 1
    if " least cheerful " in msgs:
        qtns.append(" least cheerful ")
        anss.append("What do you mean by least cheerful? Please specify. ")
        flag = 1
    if " very cheerful " in msgs:
        qtns.append(" very cheerful ")
        anss.append("What do you mean by very cheerful? Please specify. ")
        flag = 1
    if " extremely cheerful " in msgs:
        qtns.append(" extremely cheerful ")
        anss.append("What do you mean by extremely cheerful? Please specify. ")
        flag = 1
    if " especially cheerful " in msgs:
        qtns.append(" especially cheerful ")
        anss.append("What do you mean by especially cheerful? Please specify. ")
        flag = 1
    if " absolutely cheerful " in msgs:
        qtns.append(" absolutely cheerful ")
        anss.append("What do you mean by absolutely cheerful? Please specify. ")
        flag = 1
    if " most chewy " in msgs:
        qtns.append(" most chewy ")
        anss.append("What do you mean by most chewy? Please specify. ")
        flag = 1
    if " least chewy " in msgs:
        qtns.append(" least chewy ")
        anss.append("What do you mean by least chewy? Please specify. ")
        flag = 1
    if " very chewy " in msgs:
        qtns.append(" very chewy ")
        anss.append("What do you mean by very chewy? Please specify. ")
        flag = 1
    if " extremely chewy " in msgs:
        qtns.append(" extremely chewy ")
        anss.append("What do you mean by extremely chewy? Please specify. ")
        flag = 1
    if " especially chewy " in msgs:
        qtns.append(" especially chewy ")
        anss.append("What do you mean by especially chewy? Please specify. ")
        flag = 1
    if " absolutely chewy " in msgs:
        qtns.append(" absolutely chewy ")
        anss.append("What do you mean by absolutely chewy? Please specify. ")
        flag = 1
    if " most chubby " in msgs:
        qtns.append(" most chubby ")
        anss.append("What do you mean by most chubby? Please specify. ")
        flag = 1
    if " least chubby " in msgs:
        qtns.append(" least chubby ")
        anss.append("What do you mean by least chubby? Please specify. ")
        flag = 1
    if " very chubby " in msgs:
        qtns.append(" very chubby ")
        anss.append("What do you mean by very chubby? Please specify. ")
        flag = 1
    if " extremely chubby " in msgs:
        qtns.append(" extremely chubby ")
        anss.append("What do you mean by extremely chubby? Please specify. ")
        flag = 1
    if " especially chubby " in msgs:
        qtns.append(" especially chubby ")
        anss.append("What do you mean by especially chubby? Please specify. ")
        flag = 1
    if " absolutely chubby " in msgs:
        qtns.append(" absolutely chubby ")
        anss.append("What do you mean by absolutely chubby? Please specify. ")
        flag = 1
    if " most classy " in msgs:
        qtns.append(" most classy ")
        anss.append("What do you mean by most classy? Please specify. ")
        flag = 1
    if " least classy " in msgs:
        qtns.append(" least classy ")
        anss.append("What do you mean by least classy? Please specify. ")
        flag = 1
    if " very classy " in msgs:
        qtns.append(" very classy ")
        anss.append("What do you mean by very classy? Please specify. ")
        flag = 1
    if " extremely classy " in msgs:
        qtns.append(" extremely classy ")
        anss.append("What do you mean by extremely classy? Please specify. ")
        flag = 1
    if " especially classy " in msgs:
        qtns.append(" especially classy ")
        anss.append("What do you mean by especially classy? Please specify. ")
        flag = 1
    if " absolutely classy " in msgs:
        qtns.append(" absolutely classy ")
        anss.append("What do you mean by absolutely classy? Please specify. ")
        flag = 1
    if " most clean " in msgs:
        qtns.append(" most clean ")
        anss.append("What do you mean by most clean? Please specify. ")
        flag = 1
    if " least clean " in msgs:
        qtns.append(" least clean ")
        anss.append("What do you mean by least clean? Please specify. ")
        flag = 1
    if " very clean " in msgs:
        qtns.append(" very clean ")
        anss.append("What do you mean by very clean? Please specify. ")
        flag = 1
    if " extremely clean " in msgs:
        qtns.append(" extremely clean ")
        anss.append("What do you mean by extremely clean? Please specify. ")
        flag = 1
    if " especially clean " in msgs:
        qtns.append(" especially clean ")
        anss.append("What do you mean by especially clean? Please specify. ")
        flag = 1
    if " absolutely clean " in msgs:
        qtns.append(" absolutely clean ")
        anss.append("What do you mean by absolutely clean? Please specify. ")
        flag = 1
    if " most clear " in msgs:
        qtns.append(" most clear ")
        anss.append("What do you mean by most clear? Please specify. ")
        flag = 1
    if " least clear " in msgs:
        qtns.append(" least clear ")
        anss.append("What do you mean by least clear? Please specify. ")
        flag = 1
    if " very clear " in msgs:
        qtns.append(" very clear ")
        anss.append("What do you mean by very clear? Please specify. ")
        flag = 1
    if " extremely clear " in msgs:
        qtns.append(" extremely clear ")
        anss.append("What do you mean by extremely clear? Please specify. ")
        flag = 1
    if " especially clear " in msgs:
        qtns.append(" especially clear ")
        anss.append("What do you mean by especially clear? Please specify. ")
        flag = 1
    if " absolutely clear " in msgs:
        qtns.append(" absolutely clear ")
        anss.append("What do you mean by absolutely clear? Please specify. ")
        flag = 1
    if " most clever " in msgs:
        qtns.append(" most clever ")
        anss.append("What do you mean by most clever? Please specify. ")
        flag = 1
    if " least clever " in msgs:
        qtns.append(" least clever ")
        anss.append("What do you mean by least clever? Please specify. ")
        flag = 1
    if " very clever " in msgs:
        qtns.append(" very clever ")
        anss.append("What do you mean by very clever? Please specify. ")
        flag = 1
    if " extremely clever " in msgs:
        qtns.append(" extremely clever ")
        anss.append("What do you mean by extremely clever? Please specify. ")
        flag = 1
    if " especially clever " in msgs:
        qtns.append(" especially clever ")
        anss.append("What do you mean by especially clever? Please specify. ")
        flag = 1
    if " absolutely clever " in msgs:
        qtns.append(" absolutely clever ")
        anss.append("What do you mean by absolutely clever? Please specify. ")
        flag = 1
    if " most close " in msgs:
        qtns.append(" most close ")
        anss.append("What do you mean by most close? Please specify. ")
        flag = 1
    if " least close " in msgs:
        qtns.append(" least close ")
        anss.append("What do you mean by least close? Please specify. ")
        flag = 1
    if " very close " in msgs:
        qtns.append(" very close ")
        anss.append("What do you mean by very close? Please specify. ")
        flag = 1
    if " extremely close " in msgs:
        qtns.append(" extremely close ")
        anss.append("What do you mean by extremely close? Please specify. ")
        flag = 1
    if " especially close " in msgs:
        qtns.append(" especially close ")
        anss.append("What do you mean by especially close? Please specify. ")
        flag = 1
    if " absolutely close " in msgs:
        qtns.append(" absolutely close ")
        anss.append("What do you mean by absolutely close? Please specify. ")
        flag = 1
    if " most cloudy " in msgs:
        qtns.append(" most cloudy ")
        anss.append("What do you mean by most cloudy? Please specify. ")
        flag = 1
    if " least cloudy " in msgs:
        qtns.append(" least cloudy ")
        anss.append("What do you mean by least cloudy? Please specify. ")
        flag = 1
    if " very cloudy " in msgs:
        qtns.append(" very cloudy ")
        anss.append("What do you mean by very cloudy? Please specify. ")
        flag = 1
    if " extremely cloudy " in msgs:
        qtns.append(" extremely cloudy ")
        anss.append("What do you mean by extremely cloudy? Please specify. ")
        flag = 1
    if " especially cloudy " in msgs:
        qtns.append(" especially cloudy ")
        anss.append("What do you mean by especially cloudy? Please specify. ")
        flag = 1
    if " absolutely cloudy " in msgs:
        qtns.append(" absolutely cloudy ")
        anss.append("What do you mean by absolutely cloudy? Please specify. ")
        flag = 1
    if " most clumsy " in msgs:
        qtns.append(" most clumsy ")
        anss.append("What do you mean by most clumsy? Please specify. ")
        flag = 1
    if " least clumsy " in msgs:
        qtns.append(" least clumsy ")
        anss.append("What do you mean by least clumsy? Please specify. ")
        flag = 1
    if " very clumsy " in msgs:
        qtns.append(" very clumsy ")
        anss.append("What do you mean by very clumsy? Please specify. ")
        flag = 1
    if " extremely clumsy " in msgs:
        qtns.append(" extremely clumsy ")
        anss.append("What do you mean by extremely clumsy? Please specify. ")
        flag = 1
    if " especially clumsy " in msgs:
        qtns.append(" especially clumsy ")
        anss.append("What do you mean by especially clumsy? Please specify. ")
        flag = 1
    if " absolutely clumsy " in msgs:
        qtns.append(" absolutely clumsy ")
        anss.append("What do you mean by absolutely clumsy? Please specify. ")
        flag = 1
    if " most coarse " in msgs:
        qtns.append(" most coarse ")
        anss.append("What do you mean by most coarse? Please specify. ")
        flag = 1
    if " least coarse " in msgs:
        qtns.append(" least coarse ")
        anss.append("What do you mean by least coarse? Please specify. ")
        flag = 1
    if " very coarse " in msgs:
        qtns.append(" very coarse ")
        anss.append("What do you mean by very coarse? Please specify. ")
        flag = 1
    if " extremely coarse " in msgs:
        qtns.append(" extremely coarse ")
        anss.append("What do you mean by extremely coarse? Please specify. ")
        flag = 1
    if " especially coarse " in msgs:
        qtns.append(" especially coarse ")
        anss.append("What do you mean by especially coarse? Please specify. ")
        flag = 1
    if " absolutely coarse " in msgs:
        qtns.append(" absolutely coarse ")
        anss.append("What do you mean by absolutely coarse? Please specify. ")
        flag = 1
    if " most cold " in msgs:
        qtns.append(" most cold ")
        anss.append("What do you mean by most cold? Please specify. ")
        flag = 1
    if " least cold " in msgs:
        qtns.append(" least cold ")
        anss.append("What do you mean by least cold? Please specify. ")
        flag = 1
    if " very cold " in msgs:
        qtns.append(" very cold ")
        anss.append("What do you mean by very cold? Please specify. ")
        flag = 1
    if " extremely cold " in msgs:
        qtns.append(" extremely cold ")
        anss.append("What do you mean by extremely cold? Please specify. ")
        flag = 1
    if " especially cold " in msgs:
        qtns.append(" especially cold ")
        anss.append("What do you mean by especially cold? Please specify. ")
        flag = 1
    if " absolutely cold " in msgs:
        qtns.append(" absolutely cold ")
        anss.append("What do you mean by absolutely cold? Please specify. ")
        flag = 1
    if " most colorful " in msgs:
        qtns.append(" most colorful ")
        anss.append("What do you mean by most colorful? Please specify. ")
        flag = 1
    if " least colorful " in msgs:
        qtns.append(" least colorful ")
        anss.append("What do you mean by least colorful? Please specify. ")
        flag = 1
    if " very colorful " in msgs:
        qtns.append(" very colorful ")
        anss.append("What do you mean by very colorful? Please specify. ")
        flag = 1
    if " extremely colorful " in msgs:
        qtns.append(" extremely colorful ")
        anss.append("What do you mean by extremely colorful? Please specify. ")
        flag = 1
    if " especially colorful " in msgs:
        qtns.append(" especially colorful ")
        anss.append("What do you mean by especially colorful? Please specify. ")
        flag = 1
    if " absolutely colorful " in msgs:
        qtns.append(" absolutely colorful ")
        anss.append("What do you mean by absolutely colorful? Please specify. ")
        flag = 1
    if " most comfortable " in msgs:
        qtns.append(" most comfortable ")
        anss.append("What do you mean by most comfortable? Please specify. ")
        flag = 1
    if " least comfortable " in msgs:
        qtns.append(" least comfortable ")
        anss.append("What do you mean by least comfortable? Please specify. ")
        flag = 1
    if " very comfortable " in msgs:
        qtns.append(" very comfortable ")
        anss.append("What do you mean by very comfortable? Please specify. ")
        flag = 1
    if " extremely comfortable " in msgs:
        qtns.append(" extremely comfortable ")
        anss.append("What do you mean by extremely comfortable? Please specify. ")
        flag = 1
    if " especially comfortable " in msgs:
        qtns.append(" especially comfortable ")
        anss.append("What do you mean by especially comfortable? Please specify. ")
        flag = 1
    if " absolutely comfortable " in msgs:
        qtns.append(" absolutely comfortable ")
        anss.append("What do you mean by absolutely comfortable? Please specify. ")
        flag = 1
    if " most concerned " in msgs:
        qtns.append(" most concerned ")
        anss.append("What do you mean by most concerned? Please specify. ")
        flag = 1
    if " least concerned " in msgs:
        qtns.append(" least concerned ")
        anss.append("What do you mean by least concerned? Please specify. ")
        flag = 1
    if " very concerned " in msgs:
        qtns.append(" very concerned ")
        anss.append("What do you mean by very concerned? Please specify. ")
        flag = 1
    if " extremely concerned " in msgs:
        qtns.append(" extremely concerned ")
        anss.append("What do you mean by extremely concerned? Please specify. ")
        flag = 1
    if " especially concerned " in msgs:
        qtns.append(" especially concerned ")
        anss.append("What do you mean by especially concerned? Please specify. ")
        flag = 1
    if " absolutely concerned " in msgs:
        qtns.append(" absolutely concerned ")
        anss.append("What do you mean by absolutely concerned? Please specify. ")
        flag = 1
    if " most confused " in msgs:
        qtns.append(" most confused ")
        anss.append("What do you mean by most confused? Please specify. ")
        flag = 1
    if " least confused " in msgs:
        qtns.append(" least confused ")
        anss.append("What do you mean by least confused? Please specify. ")
        flag = 1
    if " very confused " in msgs:
        qtns.append(" very confused ")
        anss.append("What do you mean by very confused? Please specify. ")
        flag = 1
    if " extremely confused " in msgs:
        qtns.append(" extremely confused ")
        anss.append("What do you mean by extremely confused? Please specify. ")
        flag = 1
    if " especially confused " in msgs:
        qtns.append(" especially confused ")
        anss.append("What do you mean by especially confused? Please specify. ")
        flag = 1
    if " absolutely confused " in msgs:
        qtns.append(" absolutely confused ")
        anss.append("What do you mean by absolutely confused? Please specify. ")
        flag = 1
    if " most consistent " in msgs:
        qtns.append(" most consistent ")
        anss.append("What do you mean by most consistent? Please specify. ")
        flag = 1
    if " least consistent " in msgs:
        qtns.append(" least consistent ")
        anss.append("What do you mean by least consistent? Please specify. ")
        flag = 1
    if " very consistent " in msgs:
        qtns.append(" very consistent ")
        anss.append("What do you mean by very consistent? Please specify. ")
        flag = 1
    if " extremely consistent " in msgs:
        qtns.append(" extremely consistent ")
        anss.append("What do you mean by extremely consistent? Please specify. ")
        flag = 1
    if " especially consistent " in msgs:
        qtns.append(" especially consistent ")
        anss.append("What do you mean by especially consistent? Please specify. ")
        flag = 1
    if " absolutely consistent " in msgs:
        qtns.append(" absolutely consistent ")
        anss.append("What do you mean by absolutely consistent? Please specify. ")
        flag = 1
    if " most cool " in msgs:
        qtns.append(" most cool ")
        anss.append("What do you mean by most cool? Please specify. ")
        flag = 1
    if " least cool " in msgs:
        qtns.append(" least cool ")
        anss.append("What do you mean by least cool? Please specify. ")
        flag = 1
    if " very cool " in msgs:
        qtns.append(" very cool ")
        anss.append("What do you mean by very cool? Please specify. ")
        flag = 1
    if " extremely cool " in msgs:
        qtns.append(" extremely cool ")
        anss.append("What do you mean by extremely cool? Please specify. ")
        flag = 1
    if " especially cool " in msgs:
        qtns.append(" especially cool ")
        anss.append("What do you mean by especially cool? Please specify. ")
        flag = 1
    if " absolutely cool " in msgs:
        qtns.append(" absolutely cool ")
        anss.append("What do you mean by absolutely cool? Please specify. ")
        flag = 1
    if " most crazy " in msgs:
        qtns.append(" most crazy ")
        anss.append("What do you mean by most crazy? Please specify. ")
        flag = 1
    if " least crazy " in msgs:
        qtns.append(" least crazy ")
        anss.append("What do you mean by least crazy? Please specify. ")
        flag = 1
    if " very crazy " in msgs:
        qtns.append(" very crazy ")
        anss.append("What do you mean by very crazy? Please specify. ")
        flag = 1
    if " extremely crazy " in msgs:
        qtns.append(" extremely crazy ")
        anss.append("What do you mean by extremely crazy? Please specify. ")
        flag = 1
    if " especially crazy " in msgs:
        qtns.append(" especially crazy ")
        anss.append("What do you mean by especially crazy? Please specify. ")
        flag = 1
    if " absolutely crazy " in msgs:
        qtns.append(" absolutely crazy ")
        anss.append("What do you mean by absolutely crazy? Please specify. ")
        flag = 1
    if " most creamy " in msgs:
        qtns.append(" most creamy ")
        anss.append("What do you mean by most creamy? Please specify. ")
        flag = 1
    if " least creamy " in msgs:
        qtns.append(" least creamy ")
        anss.append("What do you mean by least creamy? Please specify. ")
        flag = 1
    if " very creamy " in msgs:
        qtns.append(" very creamy ")
        anss.append("What do you mean by very creamy? Please specify. ")
        flag = 1
    if " extremely creamy " in msgs:
        qtns.append(" extremely creamy ")
        anss.append("What do you mean by extremely creamy? Please specify. ")
        flag = 1
    if " especially creamy " in msgs:
        qtns.append(" especially creamy ")
        anss.append("What do you mean by especially creamy? Please specify. ")
        flag = 1
    if " absolutely creamy " in msgs:
        qtns.append(" absolutely creamy ")
        anss.append("What do you mean by absolutely creamy? Please specify. ")
        flag = 1
    if " most creepy " in msgs:
        qtns.append(" most creepy ")
        anss.append("What do you mean by most creepy? Please specify. ")
        flag = 1
    if " least creepy " in msgs:
        qtns.append(" least creepy ")
        anss.append("What do you mean by least creepy? Please specify. ")
        flag = 1
    if " very creepy " in msgs:
        qtns.append(" very creepy ")
        anss.append("What do you mean by very creepy? Please specify. ")
        flag = 1
    if " extremely creepy " in msgs:
        qtns.append(" extremely creepy ")
        anss.append("What do you mean by extremely creepy? Please specify. ")
        flag = 1
    if " especially creepy " in msgs:
        qtns.append(" especially creepy ")
        anss.append("What do you mean by especially creepy? Please specify. ")
        flag = 1
    if " absolutely creepy " in msgs:
        qtns.append(" absolutely creepy ")
        anss.append("What do you mean by absolutely creepy? Please specify. ")
        flag = 1
    if " most crispy " in msgs:
        qtns.append(" most crispy ")
        anss.append("What do you mean by most crispy? Please specify. ")
        flag = 1
    if " least crispy " in msgs:
        qtns.append(" least crispy ")
        anss.append("What do you mean by least crispy? Please specify. ")
        flag = 1
    if " very crispy " in msgs:
        qtns.append(" very crispy ")
        anss.append("What do you mean by very crispy? Please specify. ")
        flag = 1
    if " extremely crispy " in msgs:
        qtns.append(" extremely crispy ")
        anss.append("What do you mean by extremely crispy? Please specify. ")
        flag = 1
    if " especially crispy " in msgs:
        qtns.append(" especially crispy ")
        anss.append("What do you mean by especially crispy? Please specify. ")
        flag = 1
    if " absolutely crispy " in msgs:
        qtns.append(" absolutely crispy ")
        anss.append("What do you mean by absolutely crispy? Please specify. ")
        flag = 1
    if " most crowded " in msgs:
        qtns.append(" most crowded ")
        anss.append("What do you mean by most crowded? Please specify. ")
        flag = 1
    if " least crowded " in msgs:
        qtns.append(" least crowded ")
        anss.append("What do you mean by least crowded? Please specify. ")
        flag = 1
    if " very crowded " in msgs:
        qtns.append(" very crowded ")
        anss.append("What do you mean by very crowded? Please specify. ")
        flag = 1
    if " extremely crowded " in msgs:
        qtns.append(" extremely crowded ")
        anss.append("What do you mean by extremely crowded? Please specify. ")
        flag = 1
    if " especially crowded " in msgs:
        qtns.append(" especially crowded ")
        anss.append("What do you mean by especially crowded? Please specify. ")
        flag = 1
    if " absolutely crowded " in msgs:
        qtns.append(" absolutely crowded ")
        anss.append("What do you mean by absolutely crowded? Please specify. ")
        flag = 1
    if " most cruel " in msgs:
        qtns.append(" most cruel ")
        anss.append("What do you mean by most cruel? Please specify. ")
        flag = 1
    if " least cruel " in msgs:
        qtns.append(" least cruel ")
        anss.append("What do you mean by least cruel? Please specify. ")
        flag = 1
    if " very cruel " in msgs:
        qtns.append(" very cruel ")
        anss.append("What do you mean by very cruel? Please specify. ")
        flag = 1
    if " extremely cruel " in msgs:
        qtns.append(" extremely cruel ")
        anss.append("What do you mean by extremely cruel? Please specify. ")
        flag = 1
    if " especially cruel " in msgs:
        qtns.append(" especially cruel ")
        anss.append("What do you mean by especially cruel? Please specify. ")
        flag = 1
    if " absolutely cruel " in msgs:
        qtns.append(" absolutely cruel ")
        anss.append("What do you mean by absolutely cruel? Please specify. ")
        flag = 1
    if " most crunchy " in msgs:
        qtns.append(" most crunchy ")
        anss.append("What do you mean by most crunchy? Please specify. ")
        flag = 1
    if " least crunchy " in msgs:
        qtns.append(" least crunchy ")
        anss.append("What do you mean by least crunchy? Please specify. ")
        flag = 1
    if " very crunchy " in msgs:
        qtns.append(" very crunchy ")
        anss.append("What do you mean by very crunchy? Please specify. ")
        flag = 1
    if " extremely crunchy " in msgs:
        qtns.append(" extremely crunchy ")
        anss.append("What do you mean by extremely crunchy? Please specify. ")
        flag = 1
    if " especially crunchy " in msgs:
        qtns.append(" especially crunchy ")
        anss.append("What do you mean by especially crunchy? Please specify. ")
        flag = 1
    if " absolutely crunchy " in msgs:
        qtns.append(" absolutely crunchy ")
        anss.append("What do you mean by absolutely crunchy? Please specify. ")
        flag = 1
    if " most curious " in msgs:
        qtns.append(" most curious ")
        anss.append("What do you mean by most curious? Please specify. ")
        flag = 1
    if " least curious " in msgs:
        qtns.append(" least curious ")
        anss.append("What do you mean by least curious? Please specify. ")
        flag = 1
    if " very curious " in msgs:
        qtns.append(" very curious ")
        anss.append("What do you mean by very curious? Please specify. ")
        flag = 1
    if " extremely curious " in msgs:
        qtns.append(" extremely curious ")
        anss.append("What do you mean by extremely curious? Please specify. ")
        flag = 1
    if " especially curious " in msgs:
        qtns.append(" especially curious ")
        anss.append("What do you mean by especially curious? Please specify. ")
        flag = 1
    if " absolutely curious " in msgs:
        qtns.append(" absolutely curious ")
        anss.append("What do you mean by absolutely curious? Please specify. ")
        flag = 1
    if " most curly " in msgs:
        qtns.append(" most curly ")
        anss.append("What do you mean by most curly? Please specify. ")
        flag = 1
    if " least curly " in msgs:
        qtns.append(" least curly ")
        anss.append("What do you mean by least curly? Please specify. ")
        flag = 1
    if " very curly " in msgs:
        qtns.append(" very curly ")
        anss.append("What do you mean by very curly? Please specify. ")
        flag = 1
    if " extremely curly " in msgs:
        qtns.append(" extremely curly ")
        anss.append("What do you mean by extremely curly? Please specify. ")
        flag = 1
    if " especially curly " in msgs:
        qtns.append(" especially curly ")
        anss.append("What do you mean by especially curly? Please specify. ")
        flag = 1
    if " absolutely curly " in msgs:
        qtns.append(" absolutely curly ")
        anss.append("What do you mean by absolutely curly? Please specify. ")
        flag = 1
    if " most curvy " in msgs:
        qtns.append(" most curvy ")
        anss.append("What do you mean by most curvy? Please specify. ")
        flag = 1
    if " least curvy " in msgs:
        qtns.append(" least curvy ")
        anss.append("What do you mean by least curvy? Please specify. ")
        flag = 1
    if " very curvy " in msgs:
        qtns.append(" very curvy ")
        anss.append("What do you mean by very curvy? Please specify. ")
        flag = 1
    if " extremely curvy " in msgs:
        qtns.append(" extremely curvy ")
        anss.append("What do you mean by extremely curvy? Please specify. ")
        flag = 1
    if " especially curvy " in msgs:
        qtns.append(" especially curvy ")
        anss.append("What do you mean by especially curvy? Please specify. ")
        flag = 1
    if " absolutely curvy " in msgs:
        qtns.append(" absolutely curvy ")
        anss.append("What do you mean by absolutely curvy? Please specify. ")
        flag = 1
    if " most cute " in msgs:
        qtns.append(" most cute ")
        anss.append("What do you mean by most cute? Please specify. ")
        flag = 1
    if " least cute " in msgs:
        qtns.append(" least cute ")
        anss.append("What do you mean by least cute? Please specify. ")
        flag = 1
    if " very cute " in msgs:
        qtns.append(" very cute ")
        anss.append("What do you mean by very cute? Please specify. ")
        flag = 1
    if " extremely cute " in msgs:
        qtns.append(" extremely cute ")
        anss.append("What do you mean by extremely cute? Please specify. ")
        flag = 1
    if " especially cute " in msgs:
        qtns.append(" especially cute ")
        anss.append("What do you mean by especially cute? Please specify. ")
        flag = 1
    if " absolutely cute " in msgs:
        qtns.append(" absolutely cute ")
        anss.append("What do you mean by absolutely cute? Please specify. ")
        flag = 1
    if " most daft " in msgs:
        qtns.append(" most daft ")
        anss.append("What do you mean by most daft? Please specify. ")
        flag = 1
    if " least daft " in msgs:
        qtns.append(" least daft ")
        anss.append("What do you mean by least daft? Please specify. ")
        flag = 1
    if " very daft " in msgs:
        qtns.append(" very daft ")
        anss.append("What do you mean by very daft? Please specify. ")
        flag = 1
    if " extremely daft " in msgs:
        qtns.append(" extremely daft ")
        anss.append("What do you mean by extremely daft? Please specify. ")
        flag = 1
    if " especially daft " in msgs:
        qtns.append(" especially daft ")
        anss.append("What do you mean by especially daft? Please specify. ")
        flag = 1
    if " absolutely daft " in msgs:
        qtns.append(" absolutely daft ")
        anss.append("What do you mean by absolutely daft? Please specify. ")
        flag = 1
    if " most daily " in msgs:
        qtns.append(" most daily ")
        anss.append("What do you mean by most daily? Please specify. ")
        flag = 1
    if " least daily " in msgs:
        qtns.append(" least daily ")
        anss.append("What do you mean by least daily? Please specify. ")
        flag = 1
    if " very daily " in msgs:
        qtns.append(" very daily ")
        anss.append("What do you mean by very daily? Please specify. ")
        flag = 1
    if " extremely daily " in msgs:
        qtns.append(" extremely daily ")
        anss.append("What do you mean by extremely daily? Please specify. ")
        flag = 1
    if " especially daily " in msgs:
        qtns.append(" especially daily ")
        anss.append("What do you mean by especially daily? Please specify. ")
        flag = 1
    if " absolutely daily " in msgs:
        qtns.append(" absolutely daily ")
        anss.append("What do you mean by absolutely daily? Please specify. ")
        flag = 1
    if " most dainty " in msgs:
        qtns.append(" most dainty ")
        anss.append("What do you mean by most dainty? Please specify. ")
        flag = 1
    if " least dainty " in msgs:
        qtns.append(" least dainty ")
        anss.append("What do you mean by least dainty? Please specify. ")
        flag = 1
    if " very dainty " in msgs:
        qtns.append(" very dainty ")
        anss.append("What do you mean by very dainty? Please specify. ")
        flag = 1
    if " extremely dainty " in msgs:
        qtns.append(" extremely dainty ")
        anss.append("What do you mean by extremely dainty? Please specify. ")
        flag = 1
    if " especially dainty " in msgs:
        qtns.append(" especially dainty ")
        anss.append("What do you mean by especially dainty? Please specify. ")
        flag = 1
    if " absolutely dainty " in msgs:
        qtns.append(" absolutely dainty ")
        anss.append("What do you mean by absolutely dainty? Please specify. ")
        flag = 1
    if " most damaged " in msgs:
        qtns.append(" most damaged ")
        anss.append("What do you mean by most damaged? Please specify. ")
        flag = 1
    if " least damaged " in msgs:
        qtns.append(" least damaged ")
        anss.append("What do you mean by least damaged? Please specify. ")
        flag = 1
    if " very damaged " in msgs:
        qtns.append(" very damaged ")
        anss.append("What do you mean by very damaged? Please specify. ")
        flag = 1
    if " extremely damaged " in msgs:
        qtns.append(" extremely damaged ")
        anss.append("What do you mean by extremely damaged? Please specify. ")
        flag = 1
    if " especially damaged " in msgs:
        qtns.append(" especially damaged ")
        anss.append("What do you mean by especially damaged? Please specify. ")
        flag = 1
    if " absolutely damaged " in msgs:
        qtns.append(" absolutely damaged ")
        anss.append("What do you mean by absolutely damaged? Please specify. ")
        flag = 1
    if " most damn " in msgs:
        qtns.append(" most damn ")
        anss.append("What do you mean by most damn? Please specify. ")
        flag = 1
    if " least damn " in msgs:
        qtns.append(" least damn ")
        anss.append("What do you mean by least damn? Please specify. ")
        flag = 1
    if " very damn " in msgs:
        qtns.append(" very damn ")
        anss.append("What do you mean by very damn? Please specify. ")
        flag = 1
    if " extremely damn " in msgs:
        qtns.append(" extremely damn ")
        anss.append("What do you mean by extremely damn? Please specify. ")
        flag = 1
    if " especially damn " in msgs:
        qtns.append(" especially damn ")
        anss.append("What do you mean by especially damn? Please specify. ")
        flag = 1
    if " absolutely damn " in msgs:
        qtns.append(" absolutely damn ")
        anss.append("What do you mean by absolutely damn? Please specify. ")
        flag = 1
    if " most damning " in msgs:
        qtns.append(" most damning ")
        anss.append("What do you mean by most damning? Please specify. ")
        flag = 1
    if " least damning " in msgs:
        qtns.append(" least damning ")
        anss.append("What do you mean by least damning? Please specify. ")
        flag = 1
    if " very damning " in msgs:
        qtns.append(" very damning ")
        anss.append("What do you mean by very damning? Please specify. ")
        flag = 1
    if " extremely damning " in msgs:
        qtns.append(" extremely damning ")
        anss.append("What do you mean by extremely damning? Please specify. ")
        flag = 1
    if " especially damning " in msgs:
        qtns.append(" especially damning ")
        anss.append("What do you mean by especially damning? Please specify. ")
        flag = 1
    if " absolutely damning " in msgs:
        qtns.append(" absolutely damning ")
        anss.append("What do you mean by absolutely damning? Please specify. ")
        flag = 1
    if " most damp " in msgs:
        qtns.append(" most damp ")
        anss.append("What do you mean by most damp? Please specify. ")
        flag = 1
    if " least damp " in msgs:
        qtns.append(" least damp ")
        anss.append("What do you mean by least damp? Please specify. ")
        flag = 1
    if " very damp " in msgs:
        qtns.append(" very damp ")
        anss.append("What do you mean by very damp? Please specify. ")
        flag = 1
    if " extremely damp " in msgs:
        qtns.append(" extremely damp ")
        anss.append("What do you mean by extremely damp? Please specify. ")
        flag = 1
    if " especially damp " in msgs:
        qtns.append(" especially damp ")
        anss.append("What do you mean by especially damp? Please specify. ")
        flag = 1
    if " absolutely damp " in msgs:
        qtns.append(" absolutely damp ")
        anss.append("What do you mean by absolutely damp? Please specify. ")
        flag = 1
    if " most dampish " in msgs:
        qtns.append(" most dampish ")
        anss.append("What do you mean by most dampish? Please specify. ")
        flag = 1
    if " least dampish " in msgs:
        qtns.append(" least dampish ")
        anss.append("What do you mean by least dampish? Please specify. ")
        flag = 1
    if " very dampish " in msgs:
        qtns.append(" very dampish ")
        anss.append("What do you mean by very dampish? Please specify. ")
        flag = 1
    if " extremely dampish " in msgs:
        qtns.append(" extremely dampish ")
        anss.append("What do you mean by extremely dampish? Please specify. ")
        flag = 1
    if " especially dampish " in msgs:
        qtns.append(" especially dampish ")
        anss.append("What do you mean by especially dampish? Please specify. ")
        flag = 1
    if " absolutely dampish " in msgs:
        qtns.append(" absolutely dampish ")
        anss.append("What do you mean by absolutely dampish? Please specify. ")
        flag = 1
    if " most dangerous " in msgs:
        qtns.append(" most dangerous ")
        anss.append("What do you mean by most dangerous? Please specify. ")
        flag = 1
    if " least dangerous " in msgs:
        qtns.append(" least dangerous ")
        anss.append("What do you mean by least dangerous? Please specify. ")
        flag = 1
    if " very dangerous " in msgs:
        qtns.append(" very dangerous ")
        anss.append("What do you mean by very dangerous? Please specify. ")
        flag = 1
    if " extremely dangerous " in msgs:
        qtns.append(" extremely dangerous ")
        anss.append("What do you mean by extremely dangerous? Please specify. ")
        flag = 1
    if " especially dangerous " in msgs:
        qtns.append(" especially dangerous ")
        anss.append("What do you mean by especially dangerous? Please specify. ")
        flag = 1
    if " absolutely dangerous " in msgs:
        qtns.append(" absolutely dangerous ")
        anss.append("What do you mean by absolutely dangerous? Please specify. ")
        flag = 1
    if " most dark " in msgs:
        qtns.append(" most dark ")
        anss.append("What do you mean by most dark? Please specify. ")
        flag = 1
    if " least dark " in msgs:
        qtns.append(" least dark ")
        anss.append("What do you mean by least dark? Please specify. ")
        flag = 1
    if " very dark " in msgs:
        qtns.append(" very dark ")
        anss.append("What do you mean by very dark? Please specify. ")
        flag = 1
    if " extremely dark " in msgs:
        qtns.append(" extremely dark ")
        anss.append("What do you mean by extremely dark? Please specify. ")
        flag = 1
    if " especially dark " in msgs:
        qtns.append(" especially dark ")
        anss.append("What do you mean by especially dark? Please specify. ")
        flag = 1
    if " absolutely dark " in msgs:
        qtns.append(" absolutely dark ")
        anss.append("What do you mean by absolutely dark? Please specify. ")
        flag = 1
    if " most darkling " in msgs:
        qtns.append(" most darkling ")
        anss.append("What do you mean by most darkling? Please specify. ")
        flag = 1
    if " least darkling " in msgs:
        qtns.append(" least darkling ")
        anss.append("What do you mean by least darkling? Please specify. ")
        flag = 1
    if " very darkling " in msgs:
        qtns.append(" very darkling ")
        anss.append("What do you mean by very darkling? Please specify. ")
        flag = 1
    if " extremely darkling " in msgs:
        qtns.append(" extremely darkling ")
        anss.append("What do you mean by extremely darkling? Please specify. ")
        flag = 1
    if " especially darkling " in msgs:
        qtns.append(" especially darkling ")
        anss.append("What do you mean by especially darkling? Please specify. ")
        flag = 1
    if " absolutely darkling " in msgs:
        qtns.append(" absolutely darkling ")
        anss.append("What do you mean by absolutely darkling? Please specify. ")
        flag = 1
    if " most darned " in msgs:
        qtns.append(" most darned ")
        anss.append("What do you mean by most darned? Please specify. ")
        flag = 1
    if " least darned " in msgs:
        qtns.append(" least darned ")
        anss.append("What do you mean by least darned? Please specify. ")
        flag = 1
    if " very darned " in msgs:
        qtns.append(" very darned ")
        anss.append("What do you mean by very darned? Please specify. ")
        flag = 1
    if " extremely darned " in msgs:
        qtns.append(" extremely darned ")
        anss.append("What do you mean by extremely darned? Please specify. ")
        flag = 1
    if " especially darned " in msgs:
        qtns.append(" especially darned ")
        anss.append("What do you mean by especially darned? Please specify. ")
        flag = 1
    if " absolutely darned " in msgs:
        qtns.append(" absolutely darned ")
        anss.append("What do you mean by absolutely darned? Please specify. ")
        flag = 1
    if " most dauntless " in msgs:
        qtns.append(" most dauntless ")
        anss.append("What do you mean by most dauntless? Please specify. ")
        flag = 1
    if " least dauntless " in msgs:
        qtns.append(" least dauntless ")
        anss.append("What do you mean by least dauntless? Please specify. ")
        flag = 1
    if " very dauntless " in msgs:
        qtns.append(" very dauntless ")
        anss.append("What do you mean by very dauntless? Please specify. ")
        flag = 1
    if " extremely dauntless " in msgs:
        qtns.append(" extremely dauntless ")
        anss.append("What do you mean by extremely dauntless? Please specify. ")
        flag = 1
    if " especially dauntless " in msgs:
        qtns.append(" especially dauntless ")
        anss.append("What do you mean by especially dauntless? Please specify. ")
        flag = 1
    if " absolutely dauntless " in msgs:
        qtns.append(" absolutely dauntless ")
        anss.append("What do you mean by absolutely dauntless? Please specify. ")
        flag = 1
    if " most daylong " in msgs:
        qtns.append(" most daylong ")
        anss.append("What do you mean by most daylong? Please specify. ")
        flag = 1
    if " least daylong " in msgs:
        qtns.append(" least daylong ")
        anss.append("What do you mean by least daylong? Please specify. ")
        flag = 1
    if " very daylong " in msgs:
        qtns.append(" very daylong ")
        anss.append("What do you mean by very daylong? Please specify. ")
        flag = 1
    if " extremely daylong " in msgs:
        qtns.append(" extremely daylong ")
        anss.append("What do you mean by extremely daylong? Please specify. ")
        flag = 1
    if " especially daylong " in msgs:
        qtns.append(" especially daylong ")
        anss.append("What do you mean by especially daylong? Please specify. ")
        flag = 1
    if " absolutely daylong " in msgs:
        qtns.append(" absolutely daylong ")
        anss.append("What do you mean by absolutely daylong? Please specify. ")
        flag = 1
    if " most deadly " in msgs:
        qtns.append(" most deadly ")
        anss.append("What do you mean by most deadly? Please specify. ")
        flag = 1
    if " least deadly " in msgs:
        qtns.append(" least deadly ")
        anss.append("What do you mean by least deadly? Please specify. ")
        flag = 1
    if " very deadly " in msgs:
        qtns.append(" very deadly ")
        anss.append("What do you mean by very deadly? Please specify. ")
        flag = 1
    if " extremely deadly " in msgs:
        qtns.append(" extremely deadly ")
        anss.append("What do you mean by extremely deadly? Please specify. ")
        flag = 1
    if " especially deadly " in msgs:
        qtns.append(" especially deadly ")
        anss.append("What do you mean by especially deadly? Please specify. ")
        flag = 1
    if " absolutely deadly " in msgs:
        qtns.append(" absolutely deadly ")
        anss.append("What do you mean by absolutely deadly? Please specify. ")
        flag = 1
    if " most deep " in msgs:
        qtns.append(" most deep ")
        anss.append("What do you mean by most deep? Please specify. ")
        flag = 1
    if " least deep " in msgs:
        qtns.append(" least deep ")
        anss.append("What do you mean by least deep? Please specify. ")
        flag = 1
    if " very deep " in msgs:
        qtns.append(" very deep ")
        anss.append("What do you mean by very deep? Please specify. ")
        flag = 1
    if " extremely deep " in msgs:
        qtns.append(" extremely deep ")
        anss.append("What do you mean by extremely deep? Please specify. ")
        flag = 1
    if " especially deep " in msgs:
        qtns.append(" especially deep ")
        anss.append("What do you mean by especially deep? Please specify. ")
        flag = 1
    if " absolutely deep " in msgs:
        qtns.append(" absolutely deep ")
        anss.append("What do you mean by absolutely deep? Please specify. ")
        flag = 1
    if " most defective " in msgs:
        qtns.append(" most defective ")
        anss.append("What do you mean by most defective? Please specify. ")
        flag = 1
    if " least defective " in msgs:
        qtns.append(" least defective ")
        anss.append("What do you mean by least defective? Please specify. ")
        flag = 1
    if " very defective " in msgs:
        qtns.append(" very defective ")
        anss.append("What do you mean by very defective? Please specify. ")
        flag = 1
    if " extremely defective " in msgs:
        qtns.append(" extremely defective ")
        anss.append("What do you mean by extremely defective? Please specify. ")
        flag = 1
    if " especially defective " in msgs:
        qtns.append(" especially defective ")
        anss.append("What do you mean by especially defective? Please specify. ")
        flag = 1
    if " absolutely defective " in msgs:
        qtns.append(" absolutely defective ")
        anss.append("What do you mean by absolutely defective? Please specify. ")
        flag = 1
    if " most delicate " in msgs:
        qtns.append(" most delicate ")
        anss.append("What do you mean by most delicate? Please specify. ")
        flag = 1
    if " least delicate " in msgs:
        qtns.append(" least delicate ")
        anss.append("What do you mean by least delicate? Please specify. ")
        flag = 1
    if " very delicate " in msgs:
        qtns.append(" very delicate ")
        anss.append("What do you mean by very delicate? Please specify. ")
        flag = 1
    if " extremely delicate " in msgs:
        qtns.append(" extremely delicate ")
        anss.append("What do you mean by extremely delicate? Please specify. ")
        flag = 1
    if " especially delicate " in msgs:
        qtns.append(" especially delicate ")
        anss.append("What do you mean by especially delicate? Please specify. ")
        flag = 1
    if " absolutely delicate " in msgs:
        qtns.append(" absolutely delicate ")
        anss.append("What do you mean by absolutely delicate? Please specify. ")
        flag = 1
    if " most delicious " in msgs:
        qtns.append(" most delicious ")
        anss.append("What do you mean by most delicious? Please specify. ")
        flag = 1
    if " least delicious " in msgs:
        qtns.append(" least delicious ")
        anss.append("What do you mean by least delicious? Please specify. ")
        flag = 1
    if " very delicious " in msgs:
        qtns.append(" very delicious ")
        anss.append("What do you mean by very delicious? Please specify. ")
        flag = 1
    if " extremely delicious " in msgs:
        qtns.append(" extremely delicious ")
        anss.append("What do you mean by extremely delicious? Please specify. ")
        flag = 1
    if " especially delicious " in msgs:
        qtns.append(" especially delicious ")
        anss.append("What do you mean by especially delicious? Please specify. ")
        flag = 1
    if " absolutely delicious " in msgs:
        qtns.append(" absolutely delicious ")
        anss.append("What do you mean by absolutely delicious? Please specify. ")
        flag = 1
    if " most dense " in msgs:
        qtns.append(" most dense ")
        anss.append("What do you mean by most dense? Please specify. ")
        flag = 1
    if " least dense " in msgs:
        qtns.append(" least dense ")
        anss.append("What do you mean by least dense? Please specify. ")
        flag = 1
    if " very dense " in msgs:
        qtns.append(" very dense ")
        anss.append("What do you mean by very dense? Please specify. ")
        flag = 1
    if " extremely dense " in msgs:
        qtns.append(" extremely dense ")
        anss.append("What do you mean by extremely dense? Please specify. ")
        flag = 1
    if " especially dense " in msgs:
        qtns.append(" especially dense ")
        anss.append("What do you mean by especially dense? Please specify. ")
        flag = 1
    if " absolutely dense " in msgs:
        qtns.append(" absolutely dense ")
        anss.append("What do you mean by absolutely dense? Please specify. ")
        flag = 1
    if " most depressed " in msgs:
        qtns.append(" most depressed ")
        anss.append("What do you mean by most depressed? Please specify. ")
        flag = 1
    if " least depressed " in msgs:
        qtns.append(" least depressed ")
        anss.append("What do you mean by least depressed? Please specify. ")
        flag = 1
    if " very depressed " in msgs:
        qtns.append(" very depressed ")
        anss.append("What do you mean by very depressed? Please specify. ")
        flag = 1
    if " extremely depressed " in msgs:
        qtns.append(" extremely depressed ")
        anss.append("What do you mean by extremely depressed? Please specify. ")
        flag = 1
    if " especially depressed " in msgs:
        qtns.append(" especially depressed ")
        anss.append("What do you mean by especially depressed? Please specify. ")
        flag = 1
    if " absolutely depressed " in msgs:
        qtns.append(" absolutely depressed ")
        anss.append("What do you mean by absolutely depressed? Please specify. ")
        flag = 1
    if " most determined " in msgs:
        qtns.append(" most determined ")
        anss.append("What do you mean by most determined? Please specify. ")
        flag = 1
    if " least determined " in msgs:
        qtns.append(" least determined ")
        anss.append("What do you mean by least determined? Please specify. ")
        flag = 1
    if " very determined " in msgs:
        qtns.append(" very determined ")
        anss.append("What do you mean by very determined? Please specify. ")
        flag = 1
    if " extremely determined " in msgs:
        qtns.append(" extremely determined ")
        anss.append("What do you mean by extremely determined? Please specify. ")
        flag = 1
    if " especially determined " in msgs:
        qtns.append(" especially determined ")
        anss.append("What do you mean by especially determined? Please specify. ")
        flag = 1
    if " absolutely determined " in msgs:
        qtns.append(" absolutely determined ")
        anss.append("What do you mean by absolutely determined? Please specify. ")
        flag = 1
    if " most different " in msgs:
        qtns.append(" most different ")
        anss.append("What do you mean by most different? Please specify. ")
        flag = 1
    if " least different " in msgs:
        qtns.append(" least different ")
        anss.append("What do you mean by least different? Please specify. ")
        flag = 1
    if " very different " in msgs:
        qtns.append(" very different ")
        anss.append("What do you mean by very different? Please specify. ")
        flag = 1
    if " extremely different " in msgs:
        qtns.append(" extremely different ")
        anss.append("What do you mean by extremely different? Please specify. ")
        flag = 1
    if " especially different " in msgs:
        qtns.append(" especially different ")
        anss.append("What do you mean by especially different? Please specify. ")
        flag = 1
    if " absolutely different " in msgs:
        qtns.append(" absolutely different ")
        anss.append("What do you mean by absolutely different? Please specify. ")
        flag = 1
    if " most difficult " in msgs:
        qtns.append(" most difficult ")
        anss.append("What do you mean by most difficult? Please specify. ")
        flag = 1
    if " least difficult " in msgs:
        qtns.append(" least difficult ")
        anss.append("What do you mean by least difficult? Please specify. ")
        flag = 1
    if " very difficult " in msgs:
        qtns.append(" very difficult ")
        anss.append("What do you mean by very difficult? Please specify. ")
        flag = 1
    if " extremely difficult " in msgs:
        qtns.append(" extremely difficult ")
        anss.append("What do you mean by extremely difficult? Please specify. ")
        flag = 1
    if " especially difficult " in msgs:
        qtns.append(" especially difficult ")
        anss.append("What do you mean by especially difficult? Please specify. ")
        flag = 1
    if " absolutely difficult " in msgs:
        qtns.append(" absolutely difficult ")
        anss.append("What do you mean by absolutely difficult? Please specify. ")
        flag = 1
    if " most dirty " in msgs:
        qtns.append(" most dirty ")
        anss.append("What do you mean by most dirty? Please specify. ")
        flag = 1
    if " least dirty " in msgs:
        qtns.append(" least dirty ")
        anss.append("What do you mean by least dirty? Please specify. ")
        flag = 1
    if " very dirty " in msgs:
        qtns.append(" very dirty ")
        anss.append("What do you mean by very dirty? Please specify. ")
        flag = 1
    if " extremely dirty " in msgs:
        qtns.append(" extremely dirty ")
        anss.append("What do you mean by extremely dirty? Please specify. ")
        flag = 1
    if " especially dirty " in msgs:
        qtns.append(" especially dirty ")
        anss.append("What do you mean by especially dirty? Please specify. ")
        flag = 1
    if " absolutely dirty " in msgs:
        qtns.append(" absolutely dirty ")
        anss.append("What do you mean by absolutely dirty? Please specify. ")
        flag = 1
    if " most disgusting " in msgs:
        qtns.append(" most disgusting ")
        anss.append("What do you mean by most disgusting? Please specify. ")
        flag = 1
    if " least disgusting " in msgs:
        qtns.append(" least disgusting ")
        anss.append("What do you mean by least disgusting? Please specify. ")
        flag = 1
    if " very disgusting " in msgs:
        qtns.append(" very disgusting ")
        anss.append("What do you mean by very disgusting? Please specify. ")
        flag = 1
    if " extremely disgusting " in msgs:
        qtns.append(" extremely disgusting ")
        anss.append("What do you mean by extremely disgusting? Please specify. ")
        flag = 1
    if " especially disgusting " in msgs:
        qtns.append(" especially disgusting ")
        anss.append("What do you mean by especially disgusting? Please specify. ")
        flag = 1
    if " absolutely disgusting " in msgs:
        qtns.append(" absolutely disgusting ")
        anss.append("What do you mean by absolutely disgusting? Please specify. ")
        flag = 1
    if " most dry " in msgs:
        qtns.append(" most dry ")
        anss.append("What do you mean by most dry? Please specify. ")
        flag = 1
    if " least dry " in msgs:
        qtns.append(" least dry ")
        anss.append("What do you mean by least dry? Please specify. ")
        flag = 1
    if " very dry " in msgs:
        qtns.append(" very dry ")
        anss.append("What do you mean by very dry? Please specify. ")
        flag = 1
    if " extremely dry " in msgs:
        qtns.append(" extremely dry ")
        anss.append("What do you mean by extremely dry? Please specify. ")
        flag = 1
    if " especially dry " in msgs:
        qtns.append(" especially dry ")
        anss.append("What do you mean by especially dry? Please specify. ")
        flag = 1
    if " absolutely dry " in msgs:
        qtns.append(" absolutely dry ")
        anss.append("What do you mean by absolutely dry? Please specify. ")
        flag = 1
    if " most dull " in msgs:
        qtns.append(" most dull ")
        anss.append("What do you mean by most dull? Please specify. ")
        flag = 1
    if " least dull " in msgs:
        qtns.append(" least dull ")
        anss.append("What do you mean by least dull? Please specify. ")
        flag = 1
    if " very dull " in msgs:
        qtns.append(" very dull ")
        anss.append("What do you mean by very dull? Please specify. ")
        flag = 1
    if " extremely dull " in msgs:
        qtns.append(" extremely dull ")
        anss.append("What do you mean by extremely dull? Please specify. ")
        flag = 1
    if " especially dull " in msgs:
        qtns.append(" especially dull ")
        anss.append("What do you mean by especially dull? Please specify. ")
        flag = 1
    if " absolutely dull " in msgs:
        qtns.append(" absolutely dull ")
        anss.append("What do you mean by absolutely dull? Please specify. ")
        flag = 1
    if " most dumb " in msgs:
        qtns.append(" most dumb ")
        anss.append("What do you mean by most dumb? Please specify. ")
        flag = 1
    if " least dumb " in msgs:
        qtns.append(" least dumb ")
        anss.append("What do you mean by least dumb? Please specify. ")
        flag = 1
    if " very dumb " in msgs:
        qtns.append(" very dumb ")
        anss.append("What do you mean by very dumb? Please specify. ")
        flag = 1
    if " extremely dumb " in msgs:
        qtns.append(" extremely dumb ")
        anss.append("What do you mean by extremely dumb? Please specify. ")
        flag = 1
    if " especially dumb " in msgs:
        qtns.append(" especially dumb ")
        anss.append("What do you mean by especially dumb? Please specify. ")
        flag = 1
    if " absolutely dumb " in msgs:
        qtns.append(" absolutely dumb ")
        anss.append("What do you mean by absolutely dumb? Please specify. ")
        flag = 1
    if " most dusty " in msgs:
        qtns.append(" most dusty ")
        anss.append("What do you mean by most dusty? Please specify. ")
        flag = 1
    if " least dusty " in msgs:
        qtns.append(" least dusty ")
        anss.append("What do you mean by least dusty? Please specify. ")
        flag = 1
    if " very dusty " in msgs:
        qtns.append(" very dusty ")
        anss.append("What do you mean by very dusty? Please specify. ")
        flag = 1
    if " extremely dusty " in msgs:
        qtns.append(" extremely dusty ")
        anss.append("What do you mean by extremely dusty? Please specify. ")
        flag = 1
    if " especially dusty " in msgs:
        qtns.append(" especially dusty ")
        anss.append("What do you mean by especially dusty? Please specify. ")
        flag = 1
    if " absolutely dusty " in msgs:
        qtns.append(" absolutely dusty ")
        anss.append("What do you mean by absolutely dusty? Please specify. ")
        flag = 1
    if " most early " in msgs:
        qtns.append(" most early ")
        anss.append("What do you mean by most early? Please specify. ")
        flag = 1
    if " least early " in msgs:
        qtns.append(" least early ")
        anss.append("What do you mean by least early? Please specify. ")
        flag = 1
    if " very early " in msgs:
        qtns.append(" very early ")
        anss.append("What do you mean by very early? Please specify. ")
        flag = 1
    if " extremely early " in msgs:
        qtns.append(" extremely early ")
        anss.append("What do you mean by extremely early? Please specify. ")
        flag = 1
    if " especially early " in msgs:
        qtns.append(" especially early ")
        anss.append("What do you mean by especially early? Please specify. ")
        flag = 1
    if " absolutely early " in msgs:
        qtns.append(" absolutely early ")
        anss.append("What do you mean by absolutely early? Please specify. ")
        flag = 1
    if " most easy " in msgs:
        qtns.append(" most easy ")
        anss.append("What do you mean by most easy? Please specify. ")
        flag = 1
    if " least easy " in msgs:
        qtns.append(" least easy ")
        anss.append("What do you mean by least easy? Please specify. ")
        flag = 1
    if " very easy " in msgs:
        qtns.append(" very easy ")
        anss.append("What do you mean by very easy? Please specify. ")
        flag = 1
    if " extremely easy " in msgs:
        qtns.append(" extremely easy ")
        anss.append("What do you mean by extremely easy? Please specify. ")
        flag = 1
    if " especially easy " in msgs:
        qtns.append(" especially easy ")
        anss.append("What do you mean by especially easy? Please specify. ")
        flag = 1
    if " absolutely easy " in msgs:
        qtns.append(" absolutely easy ")
        anss.append("What do you mean by absolutely easy? Please specify. ")
        flag = 1
    if " most educated " in msgs:
        qtns.append(" most educated ")
        anss.append("What do you mean by most educated? Please specify. ")
        flag = 1
    if " least educated " in msgs:
        qtns.append(" least educated ")
        anss.append("What do you mean by least educated? Please specify. ")
        flag = 1
    if " very educated " in msgs:
        qtns.append(" very educated ")
        anss.append("What do you mean by very educated? Please specify. ")
        flag = 1
    if " extremely educated " in msgs:
        qtns.append(" extremely educated ")
        anss.append("What do you mean by extremely educated? Please specify. ")
        flag = 1
    if " especially educated " in msgs:
        qtns.append(" especially educated ")
        anss.append("What do you mean by especially educated? Please specify. ")
        flag = 1
    if " absolutely educated " in msgs:
        qtns.append(" absolutely educated ")
        anss.append("What do you mean by absolutely educated? Please specify. ")
        flag = 1
    if " most efficient " in msgs:
        qtns.append(" most efficient ")
        anss.append("What do you mean by most efficient? Please specify. ")
        flag = 1
    if " least efficient " in msgs:
        qtns.append(" least efficient ")
        anss.append("What do you mean by least efficient? Please specify. ")
        flag = 1
    if " very efficient " in msgs:
        qtns.append(" very efficient ")
        anss.append("What do you mean by very efficient? Please specify. ")
        flag = 1
    if " extremely efficient " in msgs:
        qtns.append(" extremely efficient ")
        anss.append("What do you mean by extremely efficient? Please specify. ")
        flag = 1
    if " especially efficient " in msgs:
        qtns.append(" especially efficient ")
        anss.append("What do you mean by especially efficient? Please specify. ")
        flag = 1
    if " absolutely efficient " in msgs:
        qtns.append(" absolutely efficient ")
        anss.append("What do you mean by absolutely efficient? Please specify. ")
        flag = 1
    if " most elderly " in msgs:
        qtns.append(" most elderly ")
        anss.append("What do you mean by most elderly? Please specify. ")
        flag = 1
    if " least elderly " in msgs:
        qtns.append(" least elderly ")
        anss.append("What do you mean by least elderly? Please specify. ")
        flag = 1
    if " very elderly " in msgs:
        qtns.append(" very elderly ")
        anss.append("What do you mean by very elderly? Please specify. ")
        flag = 1
    if " extremely elderly " in msgs:
        qtns.append(" extremely elderly ")
        anss.append("What do you mean by extremely elderly? Please specify. ")
        flag = 1
    if " especially elderly " in msgs:
        qtns.append(" especially elderly ")
        anss.append("What do you mean by especially elderly? Please specify. ")
        flag = 1
    if " absolutely elderly " in msgs:
        qtns.append(" absolutely elderly ")
        anss.append("What do you mean by absolutely elderly? Please specify. ")
        flag = 1
    if " most elegant " in msgs:
        qtns.append(" most elegant ")
        anss.append("What do you mean by most elegant? Please specify. ")
        flag = 1
    if " least elegant " in msgs:
        qtns.append(" least elegant ")
        anss.append("What do you mean by least elegant? Please specify. ")
        flag = 1
    if " very elegant " in msgs:
        qtns.append(" very elegant ")
        anss.append("What do you mean by very elegant? Please specify. ")
        flag = 1
    if " extremely elegant " in msgs:
        qtns.append(" extremely elegant ")
        anss.append("What do you mean by extremely elegant? Please specify. ")
        flag = 1
    if " especially elegant " in msgs:
        qtns.append(" especially elegant ")
        anss.append("What do you mean by especially elegant? Please specify. ")
        flag = 1
    if " absolutely elegant " in msgs:
        qtns.append(" absolutely elegant ")
        anss.append("What do you mean by absolutely elegant? Please specify. ")
        flag = 1
    if " most embarrassed " in msgs:
        qtns.append(" most embarrassed ")
        anss.append("What do you mean by most embarrassed? Please specify. ")
        flag = 1
    if " least embarrassed " in msgs:
        qtns.append(" least embarrassed ")
        anss.append("What do you mean by least embarrassed? Please specify. ")
        flag = 1
    if " very embarrassed " in msgs:
        qtns.append(" very embarrassed ")
        anss.append("What do you mean by very embarrassed? Please specify. ")
        flag = 1
    if " extremely embarrassed " in msgs:
        qtns.append(" extremely embarrassed ")
        anss.append("What do you mean by extremely embarrassed? Please specify. ")
        flag = 1
    if " especially embarrassed " in msgs:
        qtns.append(" especially embarrassed ")
        anss.append("What do you mean by especially embarrassed? Please specify. ")
        flag = 1
    if " absolutely embarrassed " in msgs:
        qtns.append(" absolutely embarrassed ")
        anss.append("What do you mean by absolutely embarrassed? Please specify. ")
        flag = 1
    if " most empty " in msgs:
        qtns.append(" most empty ")
        anss.append("What do you mean by most empty? Please specify. ")
        flag = 1
    if " least empty " in msgs:
        qtns.append(" least empty ")
        anss.append("What do you mean by least empty? Please specify. ")
        flag = 1
    if " very empty " in msgs:
        qtns.append(" very empty ")
        anss.append("What do you mean by very empty? Please specify. ")
        flag = 1
    if " extremely empty " in msgs:
        qtns.append(" extremely empty ")
        anss.append("What do you mean by extremely empty? Please specify. ")
        flag = 1
    if " especially empty " in msgs:
        qtns.append(" especially empty ")
        anss.append("What do you mean by especially empty? Please specify. ")
        flag = 1
    if " absolutely empty " in msgs:
        qtns.append(" absolutely empty ")
        anss.append("What do you mean by absolutely empty? Please specify. ")
        flag = 1
    if " most encouraging " in msgs:
        qtns.append(" most encouraging ")
        anss.append("What do you mean by most encouraging? Please specify. ")
        flag = 1
    if " least encouraging " in msgs:
        qtns.append(" least encouraging ")
        anss.append("What do you mean by least encouraging? Please specify. ")
        flag = 1
    if " very encouraging " in msgs:
        qtns.append(" very encouraging ")
        anss.append("What do you mean by very encouraging? Please specify. ")
        flag = 1
    if " extremely encouraging " in msgs:
        qtns.append(" extremely encouraging ")
        anss.append("What do you mean by extremely encouraging? Please specify. ")
        flag = 1
    if " especially encouraging " in msgs:
        qtns.append(" especially encouraging ")
        anss.append("What do you mean by especially encouraging? Please specify. ")
        flag = 1
    if " absolutely encouraging " in msgs:
        qtns.append(" absolutely encouraging ")
        anss.append("What do you mean by absolutely encouraging? Please specify. ")
        flag = 1
    if " most enthusiastic " in msgs:
        qtns.append(" most enthusiastic ")
        anss.append("What do you mean by most enthusiastic? Please specify. ")
        flag = 1
    if " least enthusiastic " in msgs:
        qtns.append(" least enthusiastic ")
        anss.append("What do you mean by least enthusiastic? Please specify. ")
        flag = 1
    if " very enthusiastic " in msgs:
        qtns.append(" very enthusiastic ")
        anss.append("What do you mean by very enthusiastic? Please specify. ")
        flag = 1
    if " extremely enthusiastic " in msgs:
        qtns.append(" extremely enthusiastic ")
        anss.append("What do you mean by extremely enthusiastic? Please specify. ")
        flag = 1
    if " especially enthusiastic " in msgs:
        qtns.append(" especially enthusiastic ")
        anss.append("What do you mean by especially enthusiastic? Please specify. ")
        flag = 1
    if " absolutely enthusiastic " in msgs:
        qtns.append(" absolutely enthusiastic ")
        anss.append("What do you mean by absolutely enthusiastic? Please specify. ")
        flag = 1
    if " most excellent " in msgs:
        qtns.append(" most excellent ")
        anss.append("What do you mean by most excellent? Please specify. ")
        flag = 1
    if " least excellent " in msgs:
        qtns.append(" least excellent ")
        anss.append("What do you mean by least excellent? Please specify. ")
        flag = 1
    if " very excellent " in msgs:
        qtns.append(" very excellent ")
        anss.append("What do you mean by very excellent? Please specify. ")
        flag = 1
    if " extremely excellent " in msgs:
        qtns.append(" extremely excellent ")
        anss.append("What do you mean by extremely excellent? Please specify. ")
        flag = 1
    if " especially excellent " in msgs:
        qtns.append(" especially excellent ")
        anss.append("What do you mean by especially excellent? Please specify. ")
        flag = 1
    if " absolutely excellent " in msgs:
        qtns.append(" absolutely excellent ")
        anss.append("What do you mean by absolutely excellent? Please specify. ")
        flag = 1
    if " most exciting " in msgs:
        qtns.append(" most exciting ")
        anss.append("What do you mean by most exciting? Please specify. ")
        flag = 1
    if " least exciting " in msgs:
        qtns.append(" least exciting ")
        anss.append("What do you mean by least exciting? Please specify. ")
        flag = 1
    if " very exciting " in msgs:
        qtns.append(" very exciting ")
        anss.append("What do you mean by very exciting? Please specify. ")
        flag = 1
    if " extremely exciting " in msgs:
        qtns.append(" extremely exciting ")
        anss.append("What do you mean by extremely exciting? Please specify. ")
        flag = 1
    if " especially exciting " in msgs:
        qtns.append(" especially exciting ")
        anss.append("What do you mean by especially exciting? Please specify. ")
        flag = 1
    if " absolutely exciting " in msgs:
        qtns.append(" absolutely exciting ")
        anss.append("What do you mean by absolutely exciting? Please specify. ")
        flag = 1
    if " most expensive " in msgs:
        qtns.append(" most expensive ")
        anss.append("What do you mean by most expensive? Please specify. ")
        flag = 1
    if " least expensive " in msgs:
        qtns.append(" least expensive ")
        anss.append("What do you mean by least expensive? Please specify. ")
        flag = 1
    if " very expensive " in msgs:
        qtns.append(" very expensive ")
        anss.append("What do you mean by very expensive? Please specify. ")
        flag = 1
    if " extremely expensive " in msgs:
        qtns.append(" extremely expensive ")
        anss.append("What do you mean by extremely expensive? Please specify. ")
        flag = 1
    if " especially expensive " in msgs:
        qtns.append(" especially expensive ")
        anss.append("What do you mean by especially expensive? Please specify. ")
        flag = 1
    if " absolutely expensive " in msgs:
        qtns.append(" absolutely expensive ")
        anss.append("What do you mean by absolutely expensive? Please specify. ")
        flag = 1
    if " most fabulous " in msgs:
        qtns.append(" most fabulous ")
        anss.append("What do you mean by most fabulous? Please specify. ")
        flag = 1
    if " least fabulous " in msgs:
        qtns.append(" least fabulous ")
        anss.append("What do you mean by least fabulous? Please specify. ")
        flag = 1
    if " very fabulous " in msgs:
        qtns.append(" very fabulous ")
        anss.append("What do you mean by very fabulous? Please specify. ")
        flag = 1
    if " extremely fabulous " in msgs:
        qtns.append(" extremely fabulous ")
        anss.append("What do you mean by extremely fabulous? Please specify. ")
        flag = 1
    if " especially fabulous " in msgs:
        qtns.append(" especially fabulous ")
        anss.append("What do you mean by especially fabulous? Please specify. ")
        flag = 1
    if " absolutely fabulous " in msgs:
        qtns.append(" absolutely fabulous ")
        anss.append("What do you mean by absolutely fabulous? Please specify. ")
        flag = 1
    if " most faint " in msgs:
        qtns.append(" most faint ")
        anss.append("What do you mean by most faint? Please specify. ")
        flag = 1
    if " least faint " in msgs:
        qtns.append(" least faint ")
        anss.append("What do you mean by least faint? Please specify. ")
        flag = 1
    if " very faint " in msgs:
        qtns.append(" very faint ")
        anss.append("What do you mean by very faint? Please specify. ")
        flag = 1
    if " extremely faint " in msgs:
        qtns.append(" extremely faint ")
        anss.append("What do you mean by extremely faint? Please specify. ")
        flag = 1
    if " especially faint " in msgs:
        qtns.append(" especially faint ")
        anss.append("What do you mean by especially faint? Please specify. ")
        flag = 1
    if " absolutely faint " in msgs:
        qtns.append(" absolutely faint ")
        anss.append("What do you mean by absolutely faint? Please specify. ")
        flag = 1
    if " most fair " in msgs:
        qtns.append(" most fair ")
        anss.append("What do you mean by most fair? Please specify. ")
        flag = 1
    if " least fair " in msgs:
        qtns.append(" least fair ")
        anss.append("What do you mean by least fair? Please specify. ")
        flag = 1
    if " very fair " in msgs:
        qtns.append(" very fair ")
        anss.append("What do you mean by very fair? Please specify. ")
        flag = 1
    if " extremely fair " in msgs:
        qtns.append(" extremely fair ")
        anss.append("What do you mean by extremely fair? Please specify. ")
        flag = 1
    if " especially fair " in msgs:
        qtns.append(" especially fair ")
        anss.append("What do you mean by especially fair? Please specify. ")
        flag = 1
    if " absolutely fair " in msgs:
        qtns.append(" absolutely fair ")
        anss.append("What do you mean by absolutely fair? Please specify. ")
        flag = 1
    if " most faithful " in msgs:
        qtns.append(" most faithful ")
        anss.append("What do you mean by most faithful? Please specify. ")
        flag = 1
    if " least faithful " in msgs:
        qtns.append(" least faithful ")
        anss.append("What do you mean by least faithful? Please specify. ")
        flag = 1
    if " very faithful " in msgs:
        qtns.append(" very faithful ")
        anss.append("What do you mean by very faithful? Please specify. ")
        flag = 1
    if " extremely faithful " in msgs:
        qtns.append(" extremely faithful ")
        anss.append("What do you mean by extremely faithful? Please specify. ")
        flag = 1
    if " especially faithful " in msgs:
        qtns.append(" especially faithful ")
        anss.append("What do you mean by especially faithful? Please specify. ")
        flag = 1
    if " absolutely faithful " in msgs:
        qtns.append(" absolutely faithful ")
        anss.append("What do you mean by absolutely faithful? Please specify. ")
        flag = 1
    if " most famous " in msgs:
        qtns.append(" most famous ")
        anss.append("What do you mean by most famous? Please specify. ")
        flag = 1
    if " least famous " in msgs:
        qtns.append(" least famous ")
        anss.append("What do you mean by least famous? Please specify. ")
        flag = 1
    if " very famous " in msgs:
        qtns.append(" very famous ")
        anss.append("What do you mean by very famous? Please specify. ")
        flag = 1
    if " extremely famous " in msgs:
        qtns.append(" extremely famous ")
        anss.append("What do you mean by extremely famous? Please specify. ")
        flag = 1
    if " especially famous " in msgs:
        qtns.append(" especially famous ")
        anss.append("What do you mean by especially famous? Please specify. ")
        flag = 1
    if " absolutely famous " in msgs:
        qtns.append(" absolutely famous ")
        anss.append("What do you mean by absolutely famous? Please specify. ")
        flag = 1
    if " most fancy " in msgs:
        qtns.append(" most fancy ")
        anss.append("What do you mean by most fancy? Please specify. ")
        flag = 1
    if " least fancy " in msgs:
        qtns.append(" least fancy ")
        anss.append("What do you mean by least fancy? Please specify. ")
        flag = 1
    if " very fancy " in msgs:
        qtns.append(" very fancy ")
        anss.append("What do you mean by very fancy? Please specify. ")
        flag = 1
    if " extremely fancy " in msgs:
        qtns.append(" extremely fancy ")
        anss.append("What do you mean by extremely fancy? Please specify. ")
        flag = 1
    if " especially fancy " in msgs:
        qtns.append(" especially fancy ")
        anss.append("What do you mean by especially fancy? Please specify. ")
        flag = 1
    if " absolutely fancy " in msgs:
        qtns.append(" absolutely fancy ")
        anss.append("What do you mean by absolutely fancy? Please specify. ")
        flag = 1
    if " most fantastic " in msgs:
        qtns.append(" most fantastic ")
        anss.append("What do you mean by most fantastic? Please specify. ")
        flag = 1
    if " least fantastic " in msgs:
        qtns.append(" least fantastic ")
        anss.append("What do you mean by least fantastic? Please specify. ")
        flag = 1
    if " very fantastic " in msgs:
        qtns.append(" very fantastic ")
        anss.append("What do you mean by very fantastic? Please specify. ")
        flag = 1
    if " extremely fantastic " in msgs:
        qtns.append(" extremely fantastic ")
        anss.append("What do you mean by extremely fantastic? Please specify. ")
        flag = 1
    if " especially fantastic " in msgs:
        qtns.append(" especially fantastic ")
        anss.append("What do you mean by especially fantastic? Please specify. ")
        flag = 1
    if " absolutely fantastic " in msgs:
        qtns.append(" absolutely fantastic ")
        anss.append("What do you mean by absolutely fantastic? Please specify. ")
        flag = 1
    if " most far " in msgs:
        qtns.append(" most far ")
        anss.append("What do you mean by most far? Please specify. ")
        flag = 1
    if " least far " in msgs:
        qtns.append(" least far ")
        anss.append("What do you mean by least far? Please specify. ")
        flag = 1
    if " very far " in msgs:
        qtns.append(" very far ")
        anss.append("What do you mean by very far? Please specify. ")
        flag = 1
    if " extremely far " in msgs:
        qtns.append(" extremely far ")
        anss.append("What do you mean by extremely far? Please specify. ")
        flag = 1
    if " especially far " in msgs:
        qtns.append(" especially far ")
        anss.append("What do you mean by especially far? Please specify. ")
        flag = 1
    if " absolutely far " in msgs:
        qtns.append(" absolutely far ")
        anss.append("What do you mean by absolutely far? Please specify. ")
        flag = 1
    if " most fast " in msgs:
        qtns.append(" most fast ")
        anss.append("What do you mean by most fast? Please specify. ")
        flag = 1
    if " least fast " in msgs:
        qtns.append(" least fast ")
        anss.append("What do you mean by least fast? Please specify. ")
        flag = 1
    if " very fast " in msgs:
        qtns.append(" very fast ")
        anss.append("What do you mean by very fast? Please specify. ")
        flag = 1
    if " extremely fast " in msgs:
        qtns.append(" extremely fast ")
        anss.append("What do you mean by extremely fast? Please specify. ")
        flag = 1
    if " especially fast " in msgs:
        qtns.append(" especially fast ")
        anss.append("What do you mean by especially fast? Please specify. ")
        flag = 1
    if " absolutely fast " in msgs:
        qtns.append(" absolutely fast ")
        anss.append("What do you mean by absolutely fast? Please specify. ")
        flag = 1
    if " most fat " in msgs:
        qtns.append(" most fat ")
        anss.append("What do you mean by most fat? Please specify. ")
        flag = 1
    if " least fat " in msgs:
        qtns.append(" least fat ")
        anss.append("What do you mean by least fat? Please specify. ")
        flag = 1
    if " very fat " in msgs:
        qtns.append(" very fat ")
        anss.append("What do you mean by very fat? Please specify. ")
        flag = 1
    if " extremely fat " in msgs:
        qtns.append(" extremely fat ")
        anss.append("What do you mean by extremely fat? Please specify. ")
        flag = 1
    if " especially fat " in msgs:
        qtns.append(" especially fat ")
        anss.append("What do you mean by especially fat? Please specify. ")
        flag = 1
    if " absolutely fat " in msgs:
        qtns.append(" absolutely fat ")
        anss.append("What do you mean by absolutely fat? Please specify. ")
        flag = 1
    if " most fearful " in msgs:
        qtns.append(" most fearful ")
        anss.append("What do you mean by most fearful? Please specify. ")
        flag = 1
    if " least fearful " in msgs:
        qtns.append(" least fearful ")
        anss.append("What do you mean by least fearful? Please specify. ")
        flag = 1
    if " very fearful " in msgs:
        qtns.append(" very fearful ")
        anss.append("What do you mean by very fearful? Please specify. ")
        flag = 1
    if " extremely fearful " in msgs:
        qtns.append(" extremely fearful ")
        anss.append("What do you mean by extremely fearful? Please specify. ")
        flag = 1
    if " especially fearful " in msgs:
        qtns.append(" especially fearful ")
        anss.append("What do you mean by especially fearful? Please specify. ")
        flag = 1
    if " absolutely fearful " in msgs:
        qtns.append(" absolutely fearful ")
        anss.append("What do you mean by absolutely fearful? Please specify. ")
        flag = 1
    if " most fearless " in msgs:
        qtns.append(" most fearless ")
        anss.append("What do you mean by most fearless? Please specify. ")
        flag = 1
    if " least fearless " in msgs:
        qtns.append(" least fearless ")
        anss.append("What do you mean by least fearless? Please specify. ")
        flag = 1
    if " very fearless " in msgs:
        qtns.append(" very fearless ")
        anss.append("What do you mean by very fearless? Please specify. ")
        flag = 1
    if " extremely fearless " in msgs:
        qtns.append(" extremely fearless ")
        anss.append("What do you mean by extremely fearless? Please specify. ")
        flag = 1
    if " especially fearless " in msgs:
        qtns.append(" especially fearless ")
        anss.append("What do you mean by especially fearless? Please specify. ")
        flag = 1
    if " absolutely fearless " in msgs:
        qtns.append(" absolutely fearless ")
        anss.append("What do you mean by absolutely fearless? Please specify. ")
        flag = 1
    if " most fertile " in msgs:
        qtns.append(" most fertile ")
        anss.append("What do you mean by most fertile? Please specify. ")
        flag = 1
    if " least fertile " in msgs:
        qtns.append(" least fertile ")
        anss.append("What do you mean by least fertile? Please specify. ")
        flag = 1
    if " very fertile " in msgs:
        qtns.append(" very fertile ")
        anss.append("What do you mean by very fertile? Please specify. ")
        flag = 1
    if " extremely fertile " in msgs:
        qtns.append(" extremely fertile ")
        anss.append("What do you mean by extremely fertile? Please specify. ")
        flag = 1
    if " especially fertile " in msgs:
        qtns.append(" especially fertile ")
        anss.append("What do you mean by especially fertile? Please specify. ")
        flag = 1
    if " absolutely fertile " in msgs:
        qtns.append(" absolutely fertile ")
        anss.append("What do you mean by absolutely fertile? Please specify. ")
        flag = 1
    if " most few " in msgs:
        qtns.append(" most few ")
        anss.append("What do you mean by most few? Please specify. ")
        flag = 1
    if " least few " in msgs:
        qtns.append(" least few ")
        anss.append("What do you mean by least few? Please specify. ")
        flag = 1
    if " very few " in msgs:
        qtns.append(" very few ")
        anss.append("What do you mean by very few? Please specify. ")
        flag = 1
    if " extremely few " in msgs:
        qtns.append(" extremely few ")
        anss.append("What do you mean by extremely few? Please specify. ")
        flag = 1
    if " especially few " in msgs:
        qtns.append(" especially few ")
        anss.append("What do you mean by especially few? Please specify. ")
        flag = 1
    if " absolutely few " in msgs:
        qtns.append(" absolutely few ")
        anss.append("What do you mean by absolutely few? Please specify. ")
        flag = 1
    if " most fierce " in msgs:
        qtns.append(" most fierce ")
        anss.append("What do you mean by most fierce? Please specify. ")
        flag = 1
    if " least fierce " in msgs:
        qtns.append(" least fierce ")
        anss.append("What do you mean by least fierce? Please specify. ")
        flag = 1
    if " very fierce " in msgs:
        qtns.append(" very fierce ")
        anss.append("What do you mean by very fierce? Please specify. ")
        flag = 1
    if " extremely fierce " in msgs:
        qtns.append(" extremely fierce ")
        anss.append("What do you mean by extremely fierce? Please specify. ")
        flag = 1
    if " especially fierce " in msgs:
        qtns.append(" especially fierce ")
        anss.append("What do you mean by especially fierce? Please specify. ")
        flag = 1
    if " absolutely fierce " in msgs:
        qtns.append(" absolutely fierce ")
        anss.append("What do you mean by absolutely fierce? Please specify. ")
        flag = 1
    if " most filthy " in msgs:
        qtns.append(" most filthy ")
        anss.append("What do you mean by most filthy? Please specify. ")
        flag = 1
    if " least filthy " in msgs:
        qtns.append(" least filthy ")
        anss.append("What do you mean by least filthy? Please specify. ")
        flag = 1
    if " very filthy " in msgs:
        qtns.append(" very filthy ")
        anss.append("What do you mean by very filthy? Please specify. ")
        flag = 1
    if " extremely filthy " in msgs:
        qtns.append(" extremely filthy ")
        anss.append("What do you mean by extremely filthy? Please specify. ")
        flag = 1
    if " especially filthy " in msgs:
        qtns.append(" especially filthy ")
        anss.append("What do you mean by especially filthy? Please specify. ")
        flag = 1
    if " absolutely filthy " in msgs:
        qtns.append(" absolutely filthy ")
        anss.append("What do you mean by absolutely filthy? Please specify. ")
        flag = 1
    if " most fine " in msgs:
        qtns.append(" most fine ")
        anss.append("What do you mean by most fine? Please specify. ")
        flag = 1
    if " least fine " in msgs:
        qtns.append(" least fine ")
        anss.append("What do you mean by least fine? Please specify. ")
        flag = 1
    if " very fine " in msgs:
        qtns.append(" very fine ")
        anss.append("What do you mean by very fine? Please specify. ")
        flag = 1
    if " extremely fine " in msgs:
        qtns.append(" extremely fine ")
        anss.append("What do you mean by extremely fine? Please specify. ")
        flag = 1
    if " especially fine " in msgs:
        qtns.append(" especially fine ")
        anss.append("What do you mean by especially fine? Please specify. ")
        flag = 1
    if " absolutely fine " in msgs:
        qtns.append(" absolutely fine ")
        anss.append("What do you mean by absolutely fine? Please specify. ")
        flag = 1
    if " most firm " in msgs:
        qtns.append(" most firm ")
        anss.append("What do you mean by most firm? Please specify. ")
        flag = 1
    if " least firm " in msgs:
        qtns.append(" least firm ")
        anss.append("What do you mean by least firm? Please specify. ")
        flag = 1
    if " very firm " in msgs:
        qtns.append(" very firm ")
        anss.append("What do you mean by very firm? Please specify. ")
        flag = 1
    if " extremely firm " in msgs:
        qtns.append(" extremely firm ")
        anss.append("What do you mean by extremely firm? Please specify. ")
        flag = 1
    if " especially firm " in msgs:
        qtns.append(" especially firm ")
        anss.append("What do you mean by especially firm? Please specify. ")
        flag = 1
    if " absolutely firm " in msgs:
        qtns.append(" absolutely firm ")
        anss.append("What do you mean by absolutely firm? Please specify. ")
        flag = 1
    if " most fit " in msgs:
        qtns.append(" most fit ")
        anss.append("What do you mean by most fit? Please specify. ")
        flag = 1
    if " least fit " in msgs:
        qtns.append(" least fit ")
        anss.append("What do you mean by least fit? Please specify. ")
        flag = 1
    if " very fit " in msgs:
        qtns.append(" very fit ")
        anss.append("What do you mean by very fit? Please specify. ")
        flag = 1
    if " extremely fit " in msgs:
        qtns.append(" extremely fit ")
        anss.append("What do you mean by extremely fit? Please specify. ")
        flag = 1
    if " especially fit " in msgs:
        qtns.append(" especially fit ")
        anss.append("What do you mean by especially fit? Please specify. ")
        flag = 1
    if " absolutely fit " in msgs:
        qtns.append(" absolutely fit ")
        anss.append("What do you mean by absolutely fit? Please specify. ")
        flag = 1
    if " most flaky " in msgs:
        qtns.append(" most flaky ")
        anss.append("What do you mean by most flaky? Please specify. ")
        flag = 1
    if " least flaky " in msgs:
        qtns.append(" least flaky ")
        anss.append("What do you mean by least flaky? Please specify. ")
        flag = 1
    if " very flaky " in msgs:
        qtns.append(" very flaky ")
        anss.append("What do you mean by very flaky? Please specify. ")
        flag = 1
    if " extremely flaky " in msgs:
        qtns.append(" extremely flaky ")
        anss.append("What do you mean by extremely flaky? Please specify. ")
        flag = 1
    if " especially flaky " in msgs:
        qtns.append(" especially flaky ")
        anss.append("What do you mean by especially flaky? Please specify. ")
        flag = 1
    if " absolutely flaky " in msgs:
        qtns.append(" absolutely flaky ")
        anss.append("What do you mean by absolutely flaky? Please specify. ")
        flag = 1
    if " most flat " in msgs:
        qtns.append(" most flat ")
        anss.append("What do you mean by most flat? Please specify. ")
        flag = 1
    if " least flat " in msgs:
        qtns.append(" least flat ")
        anss.append("What do you mean by least flat? Please specify. ")
        flag = 1
    if " very flat " in msgs:
        qtns.append(" very flat ")
        anss.append("What do you mean by very flat? Please specify. ")
        flag = 1
    if " extremely flat " in msgs:
        qtns.append(" extremely flat ")
        anss.append("What do you mean by extremely flat? Please specify. ")
        flag = 1
    if " especially flat " in msgs:
        qtns.append(" especially flat ")
        anss.append("What do you mean by especially flat? Please specify. ")
        flag = 1
    if " absolutely flat " in msgs:
        qtns.append(" absolutely flat ")
        anss.append("What do you mean by absolutely flat? Please specify. ")
        flag = 1
    if " most foolish " in msgs:
        qtns.append(" most foolish ")
        anss.append("What do you mean by most foolish? Please specify. ")
        flag = 1
    if " least foolish " in msgs:
        qtns.append(" least foolish ")
        anss.append("What do you mean by least foolish? Please specify. ")
        flag = 1
    if " very foolish " in msgs:
        qtns.append(" very foolish ")
        anss.append("What do you mean by very foolish? Please specify. ")
        flag = 1
    if " extremely foolish " in msgs:
        qtns.append(" extremely foolish ")
        anss.append("What do you mean by extremely foolish? Please specify. ")
        flag = 1
    if " especially foolish " in msgs:
        qtns.append(" especially foolish ")
        anss.append("What do you mean by especially foolish? Please specify. ")
        flag = 1
    if " absolutely foolish " in msgs:
        qtns.append(" absolutely foolish ")
        anss.append("What do you mean by absolutely foolish? Please specify. ")
        flag = 1
    if " most forgetful " in msgs:
        qtns.append(" most forgetful ")
        anss.append("What do you mean by most forgetful? Please specify. ")
        flag = 1
    if " least forgetful " in msgs:
        qtns.append(" least forgetful ")
        anss.append("What do you mean by least forgetful? Please specify. ")
        flag = 1
    if " very forgetful " in msgs:
        qtns.append(" very forgetful ")
        anss.append("What do you mean by very forgetful? Please specify. ")
        flag = 1
    if " extremely forgetful " in msgs:
        qtns.append(" extremely forgetful ")
        anss.append("What do you mean by extremely forgetful? Please specify. ")
        flag = 1
    if " especially forgetful " in msgs:
        qtns.append(" especially forgetful ")
        anss.append("What do you mean by especially forgetful? Please specify. ")
        flag = 1
    if " absolutely forgetful " in msgs:
        qtns.append(" absolutely forgetful ")
        anss.append("What do you mean by absolutely forgetful? Please specify. ")
        flag = 1
    if " most fresh " in msgs:
        qtns.append(" most fresh ")
        anss.append("What do you mean by most fresh? Please specify. ")
        flag = 1
    if " least fresh " in msgs:
        qtns.append(" least fresh ")
        anss.append("What do you mean by least fresh? Please specify. ")
        flag = 1
    if " very fresh " in msgs:
        qtns.append(" very fresh ")
        anss.append("What do you mean by very fresh? Please specify. ")
        flag = 1
    if " extremely fresh " in msgs:
        qtns.append(" extremely fresh ")
        anss.append("What do you mean by extremely fresh? Please specify. ")
        flag = 1
    if " especially fresh " in msgs:
        qtns.append(" especially fresh ")
        anss.append("What do you mean by especially fresh? Please specify. ")
        flag = 1
    if " absolutely fresh " in msgs:
        qtns.append(" absolutely fresh ")
        anss.append("What do you mean by absolutely fresh? Please specify. ")
        flag = 1
    if " most friendly " in msgs:
        qtns.append(" most friendly ")
        anss.append("What do you mean by most friendly? Please specify. ")
        flag = 1
    if " least friendly " in msgs:
        qtns.append(" least friendly ")
        anss.append("What do you mean by least friendly? Please specify. ")
        flag = 1
    if " very friendly " in msgs:
        qtns.append(" very friendly ")
        anss.append("What do you mean by very friendly? Please specify. ")
        flag = 1
    if " extremely friendly " in msgs:
        qtns.append(" extremely friendly ")
        anss.append("What do you mean by extremely friendly? Please specify. ")
        flag = 1
    if " especially friendly " in msgs:
        qtns.append(" especially friendly ")
        anss.append("What do you mean by especially friendly? Please specify. ")
        flag = 1
    if " absolutely friendly " in msgs:
        qtns.append(" absolutely friendly ")
        anss.append("What do you mean by absolutely friendly? Please specify. ")
        flag = 1
    if " most full " in msgs:
        qtns.append(" most full ")
        anss.append("What do you mean by most full? Please specify. ")
        flag = 1
    if " least full " in msgs:
        qtns.append(" least full ")
        anss.append("What do you mean by least full? Please specify. ")
        flag = 1
    if " very full " in msgs:
        qtns.append(" very full ")
        anss.append("What do you mean by very full? Please specify. ")
        flag = 1
    if " extremely full " in msgs:
        qtns.append(" extremely full ")
        anss.append("What do you mean by extremely full? Please specify. ")
        flag = 1
    if " especially full " in msgs:
        qtns.append(" especially full ")
        anss.append("What do you mean by especially full? Please specify. ")
        flag = 1
    if " absolutely full " in msgs:
        qtns.append(" absolutely full ")
        anss.append("What do you mean by absolutely full? Please specify. ")
        flag = 1
    if " most funny " in msgs:
        qtns.append(" most funny ")
        anss.append("What do you mean by most funny? Please specify. ")
        flag = 1
    if " least funny " in msgs:
        qtns.append(" least funny ")
        anss.append("What do you mean by least funny? Please specify. ")
        flag = 1
    if " very funny " in msgs:
        qtns.append(" very funny ")
        anss.append("What do you mean by very funny? Please specify. ")
        flag = 1
    if " extremely funny " in msgs:
        qtns.append(" extremely funny ")
        anss.append("What do you mean by extremely funny? Please specify. ")
        flag = 1
    if " especially funny " in msgs:
        qtns.append(" especially funny ")
        anss.append("What do you mean by especially funny? Please specify. ")
        flag = 1
    if " absolutely funny " in msgs:
        qtns.append(" absolutely funny ")
        anss.append("What do you mean by absolutely funny? Please specify. ")
        flag = 1
    if " most gentle " in msgs:
        qtns.append(" most gentle ")
        anss.append("What do you mean by most gentle? Please specify. ")
        flag = 1
    if " least gentle " in msgs:
        qtns.append(" least gentle ")
        anss.append("What do you mean by least gentle? Please specify. ")
        flag = 1
    if " very gentle " in msgs:
        qtns.append(" very gentle ")
        anss.append("What do you mean by very gentle? Please specify. ")
        flag = 1
    if " extremely gentle " in msgs:
        qtns.append(" extremely gentle ")
        anss.append("What do you mean by extremely gentle? Please specify. ")
        flag = 1
    if " especially gentle " in msgs:
        qtns.append(" especially gentle ")
        anss.append("What do you mean by especially gentle? Please specify. ")
        flag = 1
    if " absolutely gentle " in msgs:
        qtns.append(" absolutely gentle ")
        anss.append("What do you mean by absolutely gentle? Please specify. ")
        flag = 1
    if " most glamorous " in msgs:
        qtns.append(" most glamorous ")
        anss.append("What do you mean by most glamorous? Please specify. ")
        flag = 1
    if " least glamorous " in msgs:
        qtns.append(" least glamorous ")
        anss.append("What do you mean by least glamorous? Please specify. ")
        flag = 1
    if " very glamorous " in msgs:
        qtns.append(" very glamorous ")
        anss.append("What do you mean by very glamorous? Please specify. ")
        flag = 1
    if " extremely glamorous " in msgs:
        qtns.append(" extremely glamorous ")
        anss.append("What do you mean by extremely glamorous? Please specify. ")
        flag = 1
    if " especially glamorous " in msgs:
        qtns.append(" especially glamorous ")
        anss.append("What do you mean by especially glamorous? Please specify. ")
        flag = 1
    if " absolutely glamorous " in msgs:
        qtns.append(" absolutely glamorous ")
        anss.append("What do you mean by absolutely glamorous? Please specify. ")
        flag = 1
    if " most gloomy " in msgs:
        qtns.append(" most gloomy ")
        anss.append("What do you mean by most gloomy? Please specify. ")
        flag = 1
    if " least gloomy " in msgs:
        qtns.append(" least gloomy ")
        anss.append("What do you mean by least gloomy? Please specify. ")
        flag = 1
    if " very gloomy " in msgs:
        qtns.append(" very gloomy ")
        anss.append("What do you mean by very gloomy? Please specify. ")
        flag = 1
    if " extremely gloomy " in msgs:
        qtns.append(" extremely gloomy ")
        anss.append("What do you mean by extremely gloomy? Please specify. ")
        flag = 1
    if " especially gloomy " in msgs:
        qtns.append(" especially gloomy ")
        anss.append("What do you mean by especially gloomy? Please specify. ")
        flag = 1
    if " absolutely gloomy " in msgs:
        qtns.append(" absolutely gloomy ")
        anss.append("What do you mean by absolutely gloomy? Please specify. ")
        flag = 1
    if " most glorious " in msgs:
        qtns.append(" most glorious ")
        anss.append("What do you mean by most glorious? Please specify. ")
        flag = 1
    if " least glorious " in msgs:
        qtns.append(" least glorious ")
        anss.append("What do you mean by least glorious? Please specify. ")
        flag = 1
    if " very glorious " in msgs:
        qtns.append(" very glorious ")
        anss.append("What do you mean by very glorious? Please specify. ")
        flag = 1
    if " extremely glorious " in msgs:
        qtns.append(" extremely glorious ")
        anss.append("What do you mean by extremely glorious? Please specify. ")
        flag = 1
    if " especially glorious " in msgs:
        qtns.append(" especially glorious ")
        anss.append("What do you mean by especially glorious? Please specify. ")
        flag = 1
    if " absolutely glorious " in msgs:
        qtns.append(" absolutely glorious ")
        anss.append("What do you mean by absolutely glorious? Please specify. ")
        flag = 1
    if " most good " in msgs:
        qtns.append(" most good ")
        anss.append("What do you mean by most good? Please specify. ")
        flag = 1
    if " least good " in msgs:
        qtns.append(" least good ")
        anss.append("What do you mean by least good? Please specify. ")
        flag = 1
    if " very good " in msgs:
        qtns.append(" very good ")
        anss.append("What do you mean by very good? Please specify. ")
        flag = 1
    if " extremely good " in msgs:
        qtns.append(" extremely good ")
        anss.append("What do you mean by extremely good? Please specify. ")
        flag = 1
    if " especially good " in msgs:
        qtns.append(" especially good ")
        anss.append("What do you mean by especially good? Please specify. ")
        flag = 1
    if " absolutely good " in msgs:
        qtns.append(" absolutely good ")
        anss.append("What do you mean by absolutely good? Please specify. ")
        flag = 1
    if " most gorgeous " in msgs:
        qtns.append(" most gorgeous ")
        anss.append("What do you mean by most gorgeous? Please specify. ")
        flag = 1
    if " least gorgeous " in msgs:
        qtns.append(" least gorgeous ")
        anss.append("What do you mean by least gorgeous? Please specify. ")
        flag = 1
    if " very gorgeous " in msgs:
        qtns.append(" very gorgeous ")
        anss.append("What do you mean by very gorgeous? Please specify. ")
        flag = 1
    if " extremely gorgeous " in msgs:
        qtns.append(" extremely gorgeous ")
        anss.append("What do you mean by extremely gorgeous? Please specify. ")
        flag = 1
    if " especially gorgeous " in msgs:
        qtns.append(" especially gorgeous ")
        anss.append("What do you mean by especially gorgeous? Please specify. ")
        flag = 1
    if " absolutely gorgeous " in msgs:
        qtns.append(" absolutely gorgeous ")
        anss.append("What do you mean by absolutely gorgeous? Please specify. ")
        flag = 1
    if " most graceful " in msgs:
        qtns.append(" most graceful ")
        anss.append("What do you mean by most graceful? Please specify. ")
        flag = 1
    if " least graceful " in msgs:
        qtns.append(" least graceful ")
        anss.append("What do you mean by least graceful? Please specify. ")
        flag = 1
    if " very graceful " in msgs:
        qtns.append(" very graceful ")
        anss.append("What do you mean by very graceful? Please specify. ")
        flag = 1
    if " extremely graceful " in msgs:
        qtns.append(" extremely graceful ")
        anss.append("What do you mean by extremely graceful? Please specify. ")
        flag = 1
    if " especially graceful " in msgs:
        qtns.append(" especially graceful ")
        anss.append("What do you mean by especially graceful? Please specify. ")
        flag = 1
    if " absolutely graceful " in msgs:
        qtns.append(" absolutely graceful ")
        anss.append("What do you mean by absolutely graceful? Please specify. ")
        flag = 1
    if " most grand " in msgs:
        qtns.append(" most grand ")
        anss.append("What do you mean by most grand? Please specify. ")
        flag = 1
    if " least grand " in msgs:
        qtns.append(" least grand ")
        anss.append("What do you mean by least grand? Please specify. ")
        flag = 1
    if " very grand " in msgs:
        qtns.append(" very grand ")
        anss.append("What do you mean by very grand? Please specify. ")
        flag = 1
    if " extremely grand " in msgs:
        qtns.append(" extremely grand ")
        anss.append("What do you mean by extremely grand? Please specify. ")
        flag = 1
    if " especially grand " in msgs:
        qtns.append(" especially grand ")
        anss.append("What do you mean by especially grand? Please specify. ")
        flag = 1
    if " absolutely grand " in msgs:
        qtns.append(" absolutely grand ")
        anss.append("What do you mean by absolutely grand? Please specify. ")
        flag = 1
    if " most grateful " in msgs:
        qtns.append(" most grateful ")
        anss.append("What do you mean by most grateful? Please specify. ")
        flag = 1
    if " least grateful " in msgs:
        qtns.append(" least grateful ")
        anss.append("What do you mean by least grateful? Please specify. ")
        flag = 1
    if " very grateful " in msgs:
        qtns.append(" very grateful ")
        anss.append("What do you mean by very grateful? Please specify. ")
        flag = 1
    if " extremely grateful " in msgs:
        qtns.append(" extremely grateful ")
        anss.append("What do you mean by extremely grateful? Please specify. ")
        flag = 1
    if " especially grateful " in msgs:
        qtns.append(" especially grateful ")
        anss.append("What do you mean by especially grateful? Please specify. ")
        flag = 1
    if " absolutely grateful " in msgs:
        qtns.append(" absolutely grateful ")
        anss.append("What do you mean by absolutely grateful? Please specify. ")
        flag = 1
    if " most grave " in msgs:
        qtns.append(" most grave ")
        anss.append("What do you mean by most grave? Please specify. ")
        flag = 1
    if " least grave " in msgs:
        qtns.append(" least grave ")
        anss.append("What do you mean by least grave? Please specify. ")
        flag = 1
    if " very grave " in msgs:
        qtns.append(" very grave ")
        anss.append("What do you mean by very grave? Please specify. ")
        flag = 1
    if " extremely grave " in msgs:
        qtns.append(" extremely grave ")
        anss.append("What do you mean by extremely grave? Please specify. ")
        flag = 1
    if " especially grave " in msgs:
        qtns.append(" especially grave ")
        anss.append("What do you mean by especially grave? Please specify. ")
        flag = 1
    if " absolutely grave " in msgs:
        qtns.append(" absolutely grave ")
        anss.append("What do you mean by absolutely grave? Please specify. ")
        flag = 1
    if " most greasy " in msgs:
        qtns.append(" most greasy ")
        anss.append("What do you mean by most greasy? Please specify. ")
        flag = 1
    if " least greasy " in msgs:
        qtns.append(" least greasy ")
        anss.append("What do you mean by least greasy? Please specify. ")
        flag = 1
    if " very greasy " in msgs:
        qtns.append(" very greasy ")
        anss.append("What do you mean by very greasy? Please specify. ")
        flag = 1
    if " extremely greasy " in msgs:
        qtns.append(" extremely greasy ")
        anss.append("What do you mean by extremely greasy? Please specify. ")
        flag = 1
    if " especially greasy " in msgs:
        qtns.append(" especially greasy ")
        anss.append("What do you mean by especially greasy? Please specify. ")
        flag = 1
    if " absolutely greasy " in msgs:
        qtns.append(" absolutely greasy ")
        anss.append("What do you mean by absolutely greasy? Please specify. ")
        flag = 1
    if " most great " in msgs:
        qtns.append(" most great ")
        anss.append("What do you mean by most great? Please specify. ")
        flag = 1
    if " least great " in msgs:
        qtns.append(" least great ")
        anss.append("What do you mean by least great? Please specify. ")
        flag = 1
    if " very great " in msgs:
        qtns.append(" very great ")
        anss.append("What do you mean by very great? Please specify. ")
        flag = 1
    if " extremely great " in msgs:
        qtns.append(" extremely great ")
        anss.append("What do you mean by extremely great? Please specify. ")
        flag = 1
    if " especially great " in msgs:
        qtns.append(" especially great ")
        anss.append("What do you mean by especially great? Please specify. ")
        flag = 1
    if " absolutely great " in msgs:
        qtns.append(" absolutely great ")
        anss.append("What do you mean by absolutely great? Please specify. ")
        flag = 1
    if " most greedy " in msgs:
        qtns.append(" most greedy ")
        anss.append("What do you mean by most greedy? Please specify. ")
        flag = 1
    if " least greedy " in msgs:
        qtns.append(" least greedy ")
        anss.append("What do you mean by least greedy? Please specify. ")
        flag = 1
    if " very greedy " in msgs:
        qtns.append(" very greedy ")
        anss.append("What do you mean by very greedy? Please specify. ")
        flag = 1
    if " extremely greedy " in msgs:
        qtns.append(" extremely greedy ")
        anss.append("What do you mean by extremely greedy? Please specify. ")
        flag = 1
    if " especially greedy " in msgs:
        qtns.append(" especially greedy ")
        anss.append("What do you mean by especially greedy? Please specify. ")
        flag = 1
    if " absolutely greedy " in msgs:
        qtns.append(" absolutely greedy ")
        anss.append("What do you mean by absolutely greedy? Please specify. ")
        flag = 1
    if " most green " in msgs:
        qtns.append(" most green ")
        anss.append("What do you mean by most green? Please specify. ")
        flag = 1
    if " least green " in msgs:
        qtns.append(" least green ")
        anss.append("What do you mean by least green? Please specify. ")
        flag = 1
    if " very green " in msgs:
        qtns.append(" very green ")
        anss.append("What do you mean by very green? Please specify. ")
        flag = 1
    if " extremely green " in msgs:
        qtns.append(" extremely green ")
        anss.append("What do you mean by extremely green? Please specify. ")
        flag = 1
    if " especially green " in msgs:
        qtns.append(" especially green ")
        anss.append("What do you mean by especially green? Please specify. ")
        flag = 1
    if " absolutely green " in msgs:
        qtns.append(" absolutely green ")
        anss.append("What do you mean by absolutely green? Please specify. ")
        flag = 1
    if " most gross " in msgs:
        qtns.append(" most gross ")
        anss.append("What do you mean by most gross? Please specify. ")
        flag = 1
    if " least gross " in msgs:
        qtns.append(" least gross ")
        anss.append("What do you mean by least gross? Please specify. ")
        flag = 1
    if " very gross " in msgs:
        qtns.append(" very gross ")
        anss.append("What do you mean by very gross? Please specify. ")
        flag = 1
    if " extremely gross " in msgs:
        qtns.append(" extremely gross ")
        anss.append("What do you mean by extremely gross? Please specify. ")
        flag = 1
    if " especially gross " in msgs:
        qtns.append(" especially gross ")
        anss.append("What do you mean by especially gross? Please specify. ")
        flag = 1
    if " absolutely gross " in msgs:
        qtns.append(" absolutely gross ")
        anss.append("What do you mean by absolutely gross? Please specify. ")
        flag = 1
    if " most guilty " in msgs:
        qtns.append(" most guilty ")
        anss.append("What do you mean by most guilty? Please specify. ")
        flag = 1
    if " least guilty " in msgs:
        qtns.append(" least guilty ")
        anss.append("What do you mean by least guilty? Please specify. ")
        flag = 1
    if " very guilty " in msgs:
        qtns.append(" very guilty ")
        anss.append("What do you mean by very guilty? Please specify. ")
        flag = 1
    if " extremely guilty " in msgs:
        qtns.append(" extremely guilty ")
        anss.append("What do you mean by extremely guilty? Please specify. ")
        flag = 1
    if " especially guilty " in msgs:
        qtns.append(" especially guilty ")
        anss.append("What do you mean by especially guilty? Please specify. ")
        flag = 1
    if " absolutely guilty " in msgs:
        qtns.append(" absolutely guilty ")
        anss.append("What do you mean by absolutely guilty? Please specify. ")
        flag = 1
    if " most hairy " in msgs:
        qtns.append(" most hairy ")
        anss.append("What do you mean by most hairy? Please specify. ")
        flag = 1
    if " least hairy " in msgs:
        qtns.append(" least hairy ")
        anss.append("What do you mean by least hairy? Please specify. ")
        flag = 1
    if " very hairy " in msgs:
        qtns.append(" very hairy ")
        anss.append("What do you mean by very hairy? Please specify. ")
        flag = 1
    if " extremely hairy " in msgs:
        qtns.append(" extremely hairy ")
        anss.append("What do you mean by extremely hairy? Please specify. ")
        flag = 1
    if " especially hairy " in msgs:
        qtns.append(" especially hairy ")
        anss.append("What do you mean by especially hairy? Please specify. ")
        flag = 1
    if " absolutely hairy " in msgs:
        qtns.append(" absolutely hairy ")
        anss.append("What do you mean by absolutely hairy? Please specify. ")
        flag = 1
    if " most handsome " in msgs:
        qtns.append(" most handsome ")
        anss.append("What do you mean by most handsome? Please specify. ")
        flag = 1
    if " least handsome " in msgs:
        qtns.append(" least handsome ")
        anss.append("What do you mean by least handsome? Please specify. ")
        flag = 1
    if " very handsome " in msgs:
        qtns.append(" very handsome ")
        anss.append("What do you mean by very handsome? Please specify. ")
        flag = 1
    if " extremely handsome " in msgs:
        qtns.append(" extremely handsome ")
        anss.append("What do you mean by extremely handsome? Please specify. ")
        flag = 1
    if " especially handsome " in msgs:
        qtns.append(" especially handsome ")
        anss.append("What do you mean by especially handsome? Please specify. ")
        flag = 1
    if " absolutely handsome " in msgs:
        qtns.append(" absolutely handsome ")
        anss.append("What do you mean by absolutely handsome? Please specify. ")
        flag = 1
    if " most handy " in msgs:
        qtns.append(" most handy ")
        anss.append("What do you mean by most handy? Please specify. ")
        flag = 1
    if " least handy " in msgs:
        qtns.append(" least handy ")
        anss.append("What do you mean by least handy? Please specify. ")
        flag = 1
    if " very handy " in msgs:
        qtns.append(" very handy ")
        anss.append("What do you mean by very handy? Please specify. ")
        flag = 1
    if " extremely handy " in msgs:
        qtns.append(" extremely handy ")
        anss.append("What do you mean by extremely handy? Please specify. ")
        flag = 1
    if " especially handy " in msgs:
        qtns.append(" especially handy ")
        anss.append("What do you mean by especially handy? Please specify. ")
        flag = 1
    if " absolutely handy " in msgs:
        qtns.append(" absolutely handy ")
        anss.append("What do you mean by absolutely handy? Please specify. ")
        flag = 1
    if " most happy " in msgs:
        qtns.append(" most happy ")
        anss.append("What do you mean by most happy? Please specify. ")
        flag = 1
    if " least happy " in msgs:
        qtns.append(" least happy ")
        anss.append("What do you mean by least happy? Please specify. ")
        flag = 1
    if " very happy " in msgs:
        qtns.append(" very happy ")
        anss.append("What do you mean by very happy? Please specify. ")
        flag = 1
    if " extremely happy " in msgs:
        qtns.append(" extremely happy ")
        anss.append("What do you mean by extremely happy? Please specify. ")
        flag = 1
    if " especially happy " in msgs:
        qtns.append(" especially happy ")
        anss.append("What do you mean by especially happy? Please specify. ")
        flag = 1
    if " absolutely happy " in msgs:
        qtns.append(" absolutely happy ")
        anss.append("What do you mean by absolutely happy? Please specify. ")
        flag = 1
    if " most hard " in msgs:
        qtns.append(" most hard ")
        anss.append("What do you mean by most hard? Please specify. ")
        flag = 1
    if " least hard " in msgs:
        qtns.append(" least hard ")
        anss.append("What do you mean by least hard? Please specify. ")
        flag = 1
    if " very hard " in msgs:
        qtns.append(" very hard ")
        anss.append("What do you mean by very hard? Please specify. ")
        flag = 1
    if " extremely hard " in msgs:
        qtns.append(" extremely hard ")
        anss.append("What do you mean by extremely hard? Please specify. ")
        flag = 1
    if " especially hard " in msgs:
        qtns.append(" especially hard ")
        anss.append("What do you mean by especially hard? Please specify. ")
        flag = 1
    if " absolutely hard " in msgs:
        qtns.append(" absolutely hard ")
        anss.append("What do you mean by absolutely hard? Please specify. ")
        flag = 1
    if " most harsh " in msgs:
        qtns.append(" most harsh ")
        anss.append("What do you mean by most harsh? Please specify. ")
        flag = 1
    if " least harsh " in msgs:
        qtns.append(" least harsh ")
        anss.append("What do you mean by least harsh? Please specify. ")
        flag = 1
    if " very harsh " in msgs:
        qtns.append(" very harsh ")
        anss.append("What do you mean by very harsh? Please specify. ")
        flag = 1
    if " extremely harsh " in msgs:
        qtns.append(" extremely harsh ")
        anss.append("What do you mean by extremely harsh? Please specify. ")
        flag = 1
    if " especially harsh " in msgs:
        qtns.append(" especially harsh ")
        anss.append("What do you mean by especially harsh? Please specify. ")
        flag = 1
    if " absolutely harsh " in msgs:
        qtns.append(" absolutely harsh ")
        anss.append("What do you mean by absolutely harsh? Please specify. ")
        flag = 1
    if " most healthy " in msgs:
        qtns.append(" most healthy ")
        anss.append("What do you mean by most healthy? Please specify. ")
        flag = 1
    if " least healthy " in msgs:
        qtns.append(" least healthy ")
        anss.append("What do you mean by least healthy? Please specify. ")
        flag = 1
    if " very healthy " in msgs:
        qtns.append(" very healthy ")
        anss.append("What do you mean by very healthy? Please specify. ")
        flag = 1
    if " extremely healthy " in msgs:
        qtns.append(" extremely healthy ")
        anss.append("What do you mean by extremely healthy? Please specify. ")
        flag = 1
    if " especially healthy " in msgs:
        qtns.append(" especially healthy ")
        anss.append("What do you mean by especially healthy? Please specify. ")
        flag = 1
    if " absolutely healthy " in msgs:
        qtns.append(" absolutely healthy ")
        anss.append("What do you mean by absolutely healthy? Please specify. ")
        flag = 1
    if " most heavy " in msgs:
        qtns.append(" most heavy ")
        anss.append("What do you mean by most heavy? Please specify. ")
        flag = 1
    if " least heavy " in msgs:
        qtns.append(" least heavy ")
        anss.append("What do you mean by least heavy? Please specify. ")
        flag = 1
    if " very heavy " in msgs:
        qtns.append(" very heavy ")
        anss.append("What do you mean by very heavy? Please specify. ")
        flag = 1
    if " extremely heavy " in msgs:
        qtns.append(" extremely heavy ")
        anss.append("What do you mean by extremely heavy? Please specify. ")
        flag = 1
    if " especially heavy " in msgs:
        qtns.append(" especially heavy ")
        anss.append("What do you mean by especially heavy? Please specify. ")
        flag = 1
    if " absolutely heavy " in msgs:
        qtns.append(" absolutely heavy ")
        anss.append("What do you mean by absolutely heavy? Please specify. ")
        flag = 1
    if " most helpful " in msgs:
        qtns.append(" most helpful ")
        anss.append("What do you mean by most helpful? Please specify. ")
        flag = 1
    if " least helpful " in msgs:
        qtns.append(" least helpful ")
        anss.append("What do you mean by least helpful? Please specify. ")
        flag = 1
    if " very helpful " in msgs:
        qtns.append(" very helpful ")
        anss.append("What do you mean by very helpful? Please specify. ")
        flag = 1
    if " extremely helpful " in msgs:
        qtns.append(" extremely helpful ")
        anss.append("What do you mean by extremely helpful? Please specify. ")
        flag = 1
    if " especially helpful " in msgs:
        qtns.append(" especially helpful ")
        anss.append("What do you mean by especially helpful? Please specify. ")
        flag = 1
    if " absolutely helpful " in msgs:
        qtns.append(" absolutely helpful ")
        anss.append("What do you mean by absolutely helpful? Please specify. ")
        flag = 1
    if " most high " in msgs:
        qtns.append(" most high ")
        anss.append("What do you mean by most high? Please specify. ")
        flag = 1
    if " least high " in msgs:
        qtns.append(" least high ")
        anss.append("What do you mean by least high? Please specify. ")
        flag = 1
    if " very high " in msgs:
        qtns.append(" very high ")
        anss.append("What do you mean by very high? Please specify. ")
        flag = 1
    if " extremely high " in msgs:
        qtns.append(" extremely high ")
        anss.append("What do you mean by extremely high? Please specify. ")
        flag = 1
    if " especially high " in msgs:
        qtns.append(" especially high ")
        anss.append("What do you mean by especially high? Please specify. ")
        flag = 1
    if " absolutely high " in msgs:
        qtns.append(" absolutely high ")
        anss.append("What do you mean by absolutely high? Please specify. ")
        flag = 1
    if " most hilarious " in msgs:
        qtns.append(" most hilarious ")
        anss.append("What do you mean by most hilarious? Please specify. ")
        flag = 1
    if " least hilarious " in msgs:
        qtns.append(" least hilarious ")
        anss.append("What do you mean by least hilarious? Please specify. ")
        flag = 1
    if " very hilarious " in msgs:
        qtns.append(" very hilarious ")
        anss.append("What do you mean by very hilarious? Please specify. ")
        flag = 1
    if " extremely hilarious " in msgs:
        qtns.append(" extremely hilarious ")
        anss.append("What do you mean by extremely hilarious? Please specify. ")
        flag = 1
    if " especially hilarious " in msgs:
        qtns.append(" especially hilarious ")
        anss.append("What do you mean by especially hilarious? Please specify. ")
        flag = 1
    if " absolutely hilarious " in msgs:
        qtns.append(" absolutely hilarious ")
        anss.append("What do you mean by absolutely hilarious? Please specify. ")
        flag = 1
    if " most hip " in msgs:
        qtns.append(" most hip ")
        anss.append("What do you mean by most hip? Please specify. ")
        flag = 1
    if " least hip " in msgs:
        qtns.append(" least hip ")
        anss.append("What do you mean by least hip? Please specify. ")
        flag = 1
    if " very hip " in msgs:
        qtns.append(" very hip ")
        anss.append("What do you mean by very hip? Please specify. ")
        flag = 1
    if " extremely hip " in msgs:
        qtns.append(" extremely hip ")
        anss.append("What do you mean by extremely hip? Please specify. ")
        flag = 1
    if " especially hip " in msgs:
        qtns.append(" especially hip ")
        anss.append("What do you mean by especially hip? Please specify. ")
        flag = 1
    if " absolutely hip " in msgs:
        qtns.append(" absolutely hip ")
        anss.append("What do you mean by absolutely hip? Please specify. ")
        flag = 1
    if " most historical " in msgs:
        qtns.append(" most historical ")
        anss.append("What do you mean by most historical? Please specify. ")
        flag = 1
    if " least historical " in msgs:
        qtns.append(" least historical ")
        anss.append("What do you mean by least historical? Please specify. ")
        flag = 1
    if " very historical " in msgs:
        qtns.append(" very historical ")
        anss.append("What do you mean by very historical? Please specify. ")
        flag = 1
    if " extremely historical " in msgs:
        qtns.append(" extremely historical ")
        anss.append("What do you mean by extremely historical? Please specify. ")
        flag = 1
    if " especially historical " in msgs:
        qtns.append(" especially historical ")
        anss.append("What do you mean by especially historical? Please specify. ")
        flag = 1
    if " absolutely historical " in msgs:
        qtns.append(" absolutely historical ")
        anss.append("What do you mean by absolutely historical? Please specify. ")
        flag = 1
    if " most horrible " in msgs:
        qtns.append(" most horrible ")
        anss.append("What do you mean by most horrible? Please specify. ")
        flag = 1
    if " least horrible " in msgs:
        qtns.append(" least horrible ")
        anss.append("What do you mean by least horrible? Please specify. ")
        flag = 1
    if " very horrible " in msgs:
        qtns.append(" very horrible ")
        anss.append("What do you mean by very horrible? Please specify. ")
        flag = 1
    if " extremely horrible " in msgs:
        qtns.append(" extremely horrible ")
        anss.append("What do you mean by extremely horrible? Please specify. ")
        flag = 1
    if " especially horrible " in msgs:
        qtns.append(" especially horrible ")
        anss.append("What do you mean by especially horrible? Please specify. ")
        flag = 1
    if " absolutely horrible " in msgs:
        qtns.append(" absolutely horrible ")
        anss.append("What do you mean by absolutely horrible? Please specify. ")
        flag = 1
    if " most hot " in msgs:
        qtns.append(" most hot ")
        anss.append("What do you mean by most hot? Please specify. ")
        flag = 1
    if " least hot " in msgs:
        qtns.append(" least hot ")
        anss.append("What do you mean by least hot? Please specify. ")
        flag = 1
    if " very hot " in msgs:
        qtns.append(" very hot ")
        anss.append("What do you mean by very hot? Please specify. ")
        flag = 1
    if " extremely hot " in msgs:
        qtns.append(" extremely hot ")
        anss.append("What do you mean by extremely hot? Please specify. ")
        flag = 1
    if " especially hot " in msgs:
        qtns.append(" especially hot ")
        anss.append("What do you mean by especially hot? Please specify. ")
        flag = 1
    if " absolutely hot " in msgs:
        qtns.append(" absolutely hot ")
        anss.append("What do you mean by absolutely hot? Please specify. ")
        flag = 1
    if " most huge " in msgs:
        qtns.append(" most huge ")
        anss.append("What do you mean by most huge? Please specify. ")
        flag = 1
    if " least huge " in msgs:
        qtns.append(" least huge ")
        anss.append("What do you mean by least huge? Please specify. ")
        flag = 1
    if " very huge " in msgs:
        qtns.append(" very huge ")
        anss.append("What do you mean by very huge? Please specify. ")
        flag = 1
    if " extremely huge " in msgs:
        qtns.append(" extremely huge ")
        anss.append("What do you mean by extremely huge? Please specify. ")
        flag = 1
    if " especially huge " in msgs:
        qtns.append(" especially huge ")
        anss.append("What do you mean by especially huge? Please specify. ")
        flag = 1
    if " absolutely huge " in msgs:
        qtns.append(" absolutely huge ")
        anss.append("What do you mean by absolutely huge? Please specify. ")
        flag = 1
    if " most humble " in msgs:
        qtns.append(" most humble ")
        anss.append("What do you mean by most humble? Please specify. ")
        flag = 1
    if " least humble " in msgs:
        qtns.append(" least humble ")
        anss.append("What do you mean by least humble? Please specify. ")
        flag = 1
    if " very humble " in msgs:
        qtns.append(" very humble ")
        anss.append("What do you mean by very humble? Please specify. ")
        flag = 1
    if " extremely humble " in msgs:
        qtns.append(" extremely humble ")
        anss.append("What do you mean by extremely humble? Please specify. ")
        flag = 1
    if " especially humble " in msgs:
        qtns.append(" especially humble ")
        anss.append("What do you mean by especially humble? Please specify. ")
        flag = 1
    if " absolutely humble " in msgs:
        qtns.append(" absolutely humble ")
        anss.append("What do you mean by absolutely humble? Please specify. ")
        flag = 1
    if " most humorous " in msgs:
        qtns.append(" most humorous ")
        anss.append("What do you mean by most humorous? Please specify. ")
        flag = 1
    if " least humorous " in msgs:
        qtns.append(" least humorous ")
        anss.append("What do you mean by least humorous? Please specify. ")
        flag = 1
    if " very humorous " in msgs:
        qtns.append(" very humorous ")
        anss.append("What do you mean by very humorous? Please specify. ")
        flag = 1
    if " extremely humorous " in msgs:
        qtns.append(" extremely humorous ")
        anss.append("What do you mean by extremely humorous? Please specify. ")
        flag = 1
    if " especially humorous " in msgs:
        qtns.append(" especially humorous ")
        anss.append("What do you mean by especially humorous? Please specify. ")
        flag = 1
    if " absolutely humorous " in msgs:
        qtns.append(" absolutely humorous ")
        anss.append("What do you mean by absolutely humorous? Please specify. ")
        flag = 1
    if " most hungry " in msgs:
        qtns.append(" most hungry ")
        anss.append("What do you mean by most hungry? Please specify. ")
        flag = 1
    if " least hungry " in msgs:
        qtns.append(" least hungry ")
        anss.append("What do you mean by least hungry? Please specify. ")
        flag = 1
    if " very hungry " in msgs:
        qtns.append(" very hungry ")
        anss.append("What do you mean by very hungry? Please specify. ")
        flag = 1
    if " extremely hungry " in msgs:
        qtns.append(" extremely hungry ")
        anss.append("What do you mean by extremely hungry? Please specify. ")
        flag = 1
    if " especially hungry " in msgs:
        qtns.append(" especially hungry ")
        anss.append("What do you mean by especially hungry? Please specify. ")
        flag = 1
    if " absolutely hungry " in msgs:
        qtns.append(" absolutely hungry ")
        anss.append("What do you mean by absolutely hungry? Please specify. ")
        flag = 1
    if " most icy " in msgs:
        qtns.append(" most icy ")
        anss.append("What do you mean by most icy? Please specify. ")
        flag = 1
    if " least icy " in msgs:
        qtns.append(" least icy ")
        anss.append("What do you mean by least icy? Please specify. ")
        flag = 1
    if " very icy " in msgs:
        qtns.append(" very icy ")
        anss.append("What do you mean by very icy? Please specify. ")
        flag = 1
    if " extremely icy " in msgs:
        qtns.append(" extremely icy ")
        anss.append("What do you mean by extremely icy? Please specify. ")
        flag = 1
    if " especially icy " in msgs:
        qtns.append(" especially icy ")
        anss.append("What do you mean by especially icy? Please specify. ")
        flag = 1
    if " absolutely icy " in msgs:
        qtns.append(" absolutely icy ")
        anss.append("What do you mean by absolutely icy? Please specify. ")
        flag = 1
    if " most ignorant " in msgs:
        qtns.append(" most ignorant ")
        anss.append("What do you mean by most ignorant? Please specify. ")
        flag = 1
    if " least ignorant " in msgs:
        qtns.append(" least ignorant ")
        anss.append("What do you mean by least ignorant? Please specify. ")
        flag = 1
    if " very ignorant " in msgs:
        qtns.append(" very ignorant ")
        anss.append("What do you mean by very ignorant? Please specify. ")
        flag = 1
    if " extremely ignorant " in msgs:
        qtns.append(" extremely ignorant ")
        anss.append("What do you mean by extremely ignorant? Please specify. ")
        flag = 1
    if " especially ignorant " in msgs:
        qtns.append(" especially ignorant ")
        anss.append("What do you mean by especially ignorant? Please specify. ")
        flag = 1
    if " absolutely ignorant " in msgs:
        qtns.append(" absolutely ignorant ")
        anss.append("What do you mean by absolutely ignorant? Please specify. ")
        flag = 1
    if " most illegal " in msgs:
        qtns.append(" most illegal ")
        anss.append("What do you mean by most illegal? Please specify. ")
        flag = 1
    if " least illegal " in msgs:
        qtns.append(" least illegal ")
        anss.append("What do you mean by least illegal? Please specify. ")
        flag = 1
    if " very illegal " in msgs:
        qtns.append(" very illegal ")
        anss.append("What do you mean by very illegal? Please specify. ")
        flag = 1
    if " extremely illegal " in msgs:
        qtns.append(" extremely illegal ")
        anss.append("What do you mean by extremely illegal? Please specify. ")
        flag = 1
    if " especially illegal " in msgs:
        qtns.append(" especially illegal ")
        anss.append("What do you mean by especially illegal? Please specify. ")
        flag = 1
    if " absolutely illegal " in msgs:
        qtns.append(" absolutely illegal ")
        anss.append("What do you mean by absolutely illegal? Please specify. ")
        flag = 1
    if " most imaginary " in msgs:
        qtns.append(" most imaginary ")
        anss.append("What do you mean by most imaginary? Please specify. ")
        flag = 1
    if " least imaginary " in msgs:
        qtns.append(" least imaginary ")
        anss.append("What do you mean by least imaginary? Please specify. ")
        flag = 1
    if " very imaginary " in msgs:
        qtns.append(" very imaginary ")
        anss.append("What do you mean by very imaginary? Please specify. ")
        flag = 1
    if " extremely imaginary " in msgs:
        qtns.append(" extremely imaginary ")
        anss.append("What do you mean by extremely imaginary? Please specify. ")
        flag = 1
    if " especially imaginary " in msgs:
        qtns.append(" especially imaginary ")
        anss.append("What do you mean by especially imaginary? Please specify. ")
        flag = 1
    if " absolutely imaginary " in msgs:
        qtns.append(" absolutely imaginary ")
        anss.append("What do you mean by absolutely imaginary? Please specify. ")
        flag = 1
    if " most impolite " in msgs:
        qtns.append(" most impolite ")
        anss.append("What do you mean by most impolite? Please specify. ")
        flag = 1
    if " least impolite " in msgs:
        qtns.append(" least impolite ")
        anss.append("What do you mean by least impolite? Please specify. ")
        flag = 1
    if " very impolite " in msgs:
        qtns.append(" very impolite ")
        anss.append("What do you mean by very impolite? Please specify. ")
        flag = 1
    if " extremely impolite " in msgs:
        qtns.append(" extremely impolite ")
        anss.append("What do you mean by extremely impolite? Please specify. ")
        flag = 1
    if " especially impolite " in msgs:
        qtns.append(" especially impolite ")
        anss.append("What do you mean by especially impolite? Please specify. ")
        flag = 1
    if " absolutely impolite " in msgs:
        qtns.append(" absolutely impolite ")
        anss.append("What do you mean by absolutely impolite? Please specify. ")
        flag = 1
    if " most important " in msgs:
        qtns.append(" most important ")
        anss.append("What do you mean by most important? Please specify. ")
        flag = 1
    if " least important " in msgs:
        qtns.append(" least important ")
        anss.append("What do you mean by least important? Please specify. ")
        flag = 1
    if " very important " in msgs:
        qtns.append(" very important ")
        anss.append("What do you mean by very important? Please specify. ")
        flag = 1
    if " extremely important " in msgs:
        qtns.append(" extremely important ")
        anss.append("What do you mean by extremely important? Please specify. ")
        flag = 1
    if " especially important " in msgs:
        qtns.append(" especially important ")
        anss.append("What do you mean by especially important? Please specify. ")
        flag = 1
    if " absolutely important " in msgs:
        qtns.append(" absolutely important ")
        anss.append("What do you mean by absolutely important? Please specify. ")
        flag = 1
    if " most impossible " in msgs:
        qtns.append(" most impossible ")
        anss.append("What do you mean by most impossible? Please specify. ")
        flag = 1
    if " least impossible " in msgs:
        qtns.append(" least impossible ")
        anss.append("What do you mean by least impossible? Please specify. ")
        flag = 1
    if " very impossible " in msgs:
        qtns.append(" very impossible ")
        anss.append("What do you mean by very impossible? Please specify. ")
        flag = 1
    if " extremely impossible " in msgs:
        qtns.append(" extremely impossible ")
        anss.append("What do you mean by extremely impossible? Please specify. ")
        flag = 1
    if " especially impossible " in msgs:
        qtns.append(" especially impossible ")
        anss.append("What do you mean by especially impossible? Please specify. ")
        flag = 1
    if " absolutely impossible " in msgs:
        qtns.append(" absolutely impossible ")
        anss.append("What do you mean by absolutely impossible? Please specify. ")
        flag = 1
    if " most innocent " in msgs:
        qtns.append(" most innocent ")
        anss.append("What do you mean by most innocent? Please specify. ")
        flag = 1
    if " least innocent " in msgs:
        qtns.append(" least innocent ")
        anss.append("What do you mean by least innocent? Please specify. ")
        flag = 1
    if " very innocent " in msgs:
        qtns.append(" very innocent ")
        anss.append("What do you mean by very innocent? Please specify. ")
        flag = 1
    if " extremely innocent " in msgs:
        qtns.append(" extremely innocent ")
        anss.append("What do you mean by extremely innocent? Please specify. ")
        flag = 1
    if " especially innocent " in msgs:
        qtns.append(" especially innocent ")
        anss.append("What do you mean by especially innocent? Please specify. ")
        flag = 1
    if " absolutely innocent " in msgs:
        qtns.append(" absolutely innocent ")
        anss.append("What do you mean by absolutely innocent? Please specify. ")
        flag = 1
    if " most intelligent " in msgs:
        qtns.append(" most intelligent ")
        anss.append("What do you mean by most intelligent? Please specify. ")
        flag = 1
    if " least intelligent " in msgs:
        qtns.append(" least intelligent ")
        anss.append("What do you mean by least intelligent? Please specify. ")
        flag = 1
    if " very intelligent " in msgs:
        qtns.append(" very intelligent ")
        anss.append("What do you mean by very intelligent? Please specify. ")
        flag = 1
    if " extremely intelligent " in msgs:
        qtns.append(" extremely intelligent ")
        anss.append("What do you mean by extremely intelligent? Please specify. ")
        flag = 1
    if " especially intelligent " in msgs:
        qtns.append(" especially intelligent ")
        anss.append("What do you mean by especially intelligent? Please specify. ")
        flag = 1
    if " absolutely intelligent " in msgs:
        qtns.append(" absolutely intelligent ")
        anss.append("What do you mean by absolutely intelligent? Please specify. ")
        flag = 1
    if " most interesting " in msgs:
        qtns.append(" most interesting ")
        anss.append("What do you mean by most interesting? Please specify. ")
        flag = 1
    if " least interesting " in msgs:
        qtns.append(" least interesting ")
        anss.append("What do you mean by least interesting? Please specify. ")
        flag = 1
    if " very interesting " in msgs:
        qtns.append(" very interesting ")
        anss.append("What do you mean by very interesting? Please specify. ")
        flag = 1
    if " extremely interesting " in msgs:
        qtns.append(" extremely interesting ")
        anss.append("What do you mean by extremely interesting? Please specify. ")
        flag = 1
    if " especially interesting " in msgs:
        qtns.append(" especially interesting ")
        anss.append("What do you mean by especially interesting? Please specify. ")
        flag = 1
    if " absolutely interesting " in msgs:
        qtns.append(" absolutely interesting ")
        anss.append("What do you mean by absolutely interesting? Please specify. ")
        flag = 1
    if " most itchy " in msgs:
        qtns.append(" most itchy ")
        anss.append("What do you mean by most itchy? Please specify. ")
        flag = 1
    if " least itchy " in msgs:
        qtns.append(" least itchy ")
        anss.append("What do you mean by least itchy? Please specify. ")
        flag = 1
    if " very itchy " in msgs:
        qtns.append(" very itchy ")
        anss.append("What do you mean by very itchy? Please specify. ")
        flag = 1
    if " extremely itchy " in msgs:
        qtns.append(" extremely itchy ")
        anss.append("What do you mean by extremely itchy? Please specify. ")
        flag = 1
    if " especially itchy " in msgs:
        qtns.append(" especially itchy ")
        anss.append("What do you mean by especially itchy? Please specify. ")
        flag = 1
    if " absolutely itchy " in msgs:
        qtns.append(" absolutely itchy ")
        anss.append("What do you mean by absolutely itchy? Please specify. ")
        flag = 1
    if " most jealous " in msgs:
        qtns.append(" most jealous ")
        anss.append("What do you mean by most jealous? Please specify. ")
        flag = 1
    if " least jealous " in msgs:
        qtns.append(" least jealous ")
        anss.append("What do you mean by least jealous? Please specify. ")
        flag = 1
    if " very jealous " in msgs:
        qtns.append(" very jealous ")
        anss.append("What do you mean by very jealous? Please specify. ")
        flag = 1
    if " extremely jealous " in msgs:
        qtns.append(" extremely jealous ")
        anss.append("What do you mean by extremely jealous? Please specify. ")
        flag = 1
    if " especially jealous " in msgs:
        qtns.append(" especially jealous ")
        anss.append("What do you mean by especially jealous? Please specify. ")
        flag = 1
    if " absolutely jealous " in msgs:
        qtns.append(" absolutely jealous ")
        anss.append("What do you mean by absolutely jealous? Please specify. ")
        flag = 1
    if " most jolly " in msgs:
        qtns.append(" most jolly ")
        anss.append("What do you mean by most jolly? Please specify. ")
        flag = 1
    if " least jolly " in msgs:
        qtns.append(" least jolly ")
        anss.append("What do you mean by least jolly? Please specify. ")
        flag = 1
    if " very jolly " in msgs:
        qtns.append(" very jolly ")
        anss.append("What do you mean by very jolly? Please specify. ")
        flag = 1
    if " extremely jolly " in msgs:
        qtns.append(" extremely jolly ")
        anss.append("What do you mean by extremely jolly? Please specify. ")
        flag = 1
    if " especially jolly " in msgs:
        qtns.append(" especially jolly ")
        anss.append("What do you mean by especially jolly? Please specify. ")
        flag = 1
    if " absolutely jolly " in msgs:
        qtns.append(" absolutely jolly ")
        anss.append("What do you mean by absolutely jolly? Please specify. ")
        flag = 1
    if " most juicy " in msgs:
        qtns.append(" most juicy ")
        anss.append("What do you mean by most juicy? Please specify. ")
        flag = 1
    if " least juicy " in msgs:
        qtns.append(" least juicy ")
        anss.append("What do you mean by least juicy? Please specify. ")
        flag = 1
    if " very juicy " in msgs:
        qtns.append(" very juicy ")
        anss.append("What do you mean by very juicy? Please specify. ")
        flag = 1
    if " extremely juicy " in msgs:
        qtns.append(" extremely juicy ")
        anss.append("What do you mean by extremely juicy? Please specify. ")
        flag = 1
    if " especially juicy " in msgs:
        qtns.append(" especially juicy ")
        anss.append("What do you mean by especially juicy? Please specify. ")
        flag = 1
    if " absolutely juicy " in msgs:
        qtns.append(" absolutely juicy ")
        anss.append("What do you mean by absolutely juicy? Please specify. ")
        flag = 1
    if " most juvenile " in msgs:
        qtns.append(" most juvenile ")
        anss.append("What do you mean by most juvenile? Please specify. ")
        flag = 1
    if " least juvenile " in msgs:
        qtns.append(" least juvenile ")
        anss.append("What do you mean by least juvenile? Please specify. ")
        flag = 1
    if " very juvenile " in msgs:
        qtns.append(" very juvenile ")
        anss.append("What do you mean by very juvenile? Please specify. ")
        flag = 1
    if " extremely juvenile " in msgs:
        qtns.append(" extremely juvenile ")
        anss.append("What do you mean by extremely juvenile? Please specify. ")
        flag = 1
    if " especially juvenile " in msgs:
        qtns.append(" especially juvenile ")
        anss.append("What do you mean by especially juvenile? Please specify. ")
        flag = 1
    if " absolutely juvenile " in msgs:
        qtns.append(" absolutely juvenile ")
        anss.append("What do you mean by absolutely juvenile? Please specify. ")
        flag = 1
    if " most kind " in msgs:
        qtns.append(" most kind ")
        anss.append("What do you mean by most kind? Please specify. ")
        flag = 1
    if " least kind " in msgs:
        qtns.append(" least kind ")
        anss.append("What do you mean by least kind? Please specify. ")
        flag = 1
    if " very kind " in msgs:
        qtns.append(" very kind ")
        anss.append("What do you mean by very kind? Please specify. ")
        flag = 1
    if " extremely kind " in msgs:
        qtns.append(" extremely kind ")
        anss.append("What do you mean by extremely kind? Please specify. ")
        flag = 1
    if " especially kind " in msgs:
        qtns.append(" especially kind ")
        anss.append("What do you mean by especially kind? Please specify. ")
        flag = 1
    if " absolutely kind " in msgs:
        qtns.append(" absolutely kind ")
        anss.append("What do you mean by absolutely kind? Please specify. ")
        flag = 1
    if " most large " in msgs:
        qtns.append(" most large ")
        anss.append("What do you mean by most large? Please specify. ")
        flag = 1
    if " least large " in msgs:
        qtns.append(" least large ")
        anss.append("What do you mean by least large? Please specify. ")
        flag = 1
    if " very large " in msgs:
        qtns.append(" very large ")
        anss.append("What do you mean by very large? Please specify. ")
        flag = 1
    if " extremely large " in msgs:
        qtns.append(" extremely large ")
        anss.append("What do you mean by extremely large? Please specify. ")
        flag = 1
    if " especially large " in msgs:
        qtns.append(" especially large ")
        anss.append("What do you mean by especially large? Please specify. ")
        flag = 1
    if " absolutely large " in msgs:
        qtns.append(" absolutely large ")
        anss.append("What do you mean by absolutely large? Please specify. ")
        flag = 1
    if " most late " in msgs:
        qtns.append(" most late ")
        anss.append("What do you mean by most late? Please specify. ")
        flag = 1
    if " least late " in msgs:
        qtns.append(" least late ")
        anss.append("What do you mean by least late? Please specify. ")
        flag = 1
    if " very late " in msgs:
        qtns.append(" very late ")
        anss.append("What do you mean by very late? Please specify. ")
        flag = 1
    if " extremely late " in msgs:
        qtns.append(" extremely late ")
        anss.append("What do you mean by extremely late? Please specify. ")
        flag = 1
    if " especially late " in msgs:
        qtns.append(" especially late ")
        anss.append("What do you mean by especially late? Please specify. ")
        flag = 1
    if " absolutely late " in msgs:
        qtns.append(" absolutely late ")
        anss.append("What do you mean by absolutely late? Please specify. ")
        flag = 1
    if " most lazy " in msgs:
        qtns.append(" most lazy ")
        anss.append("What do you mean by most lazy? Please specify. ")
        flag = 1
    if " least lazy " in msgs:
        qtns.append(" least lazy ")
        anss.append("What do you mean by least lazy? Please specify. ")
        flag = 1
    if " very lazy " in msgs:
        qtns.append(" very lazy ")
        anss.append("What do you mean by very lazy? Please specify. ")
        flag = 1
    if " extremely lazy " in msgs:
        qtns.append(" extremely lazy ")
        anss.append("What do you mean by extremely lazy? Please specify. ")
        flag = 1
    if " especially lazy " in msgs:
        qtns.append(" especially lazy ")
        anss.append("What do you mean by especially lazy? Please specify. ")
        flag = 1
    if " absolutely lazy " in msgs:
        qtns.append(" absolutely lazy ")
        anss.append("What do you mean by absolutely lazy? Please specify. ")
        flag = 1
    if " most legal " in msgs:
        qtns.append(" most legal ")
        anss.append("What do you mean by most legal? Please specify. ")
        flag = 1
    if " least legal " in msgs:
        qtns.append(" least legal ")
        anss.append("What do you mean by least legal? Please specify. ")
        flag = 1
    if " very legal " in msgs:
        qtns.append(" very legal ")
        anss.append("What do you mean by very legal? Please specify. ")
        flag = 1
    if " extremely legal " in msgs:
        qtns.append(" extremely legal ")
        anss.append("What do you mean by extremely legal? Please specify. ")
        flag = 1
    if " especially legal " in msgs:
        qtns.append(" especially legal ")
        anss.append("What do you mean by especially legal? Please specify. ")
        flag = 1
    if " absolutely legal " in msgs:
        qtns.append(" absolutely legal ")
        anss.append("What do you mean by absolutely legal? Please specify. ")
        flag = 1
    if " most light " in msgs:
        qtns.append(" most light ")
        anss.append("What do you mean by most light? Please specify. ")
        flag = 1
    if " least light " in msgs:
        qtns.append(" least light ")
        anss.append("What do you mean by least light? Please specify. ")
        flag = 1
    if " very light " in msgs:
        qtns.append(" very light ")
        anss.append("What do you mean by very light? Please specify. ")
        flag = 1
    if " extremely light " in msgs:
        qtns.append(" extremely light ")
        anss.append("What do you mean by extremely light? Please specify. ")
        flag = 1
    if " especially light " in msgs:
        qtns.append(" especially light ")
        anss.append("What do you mean by especially light? Please specify. ")
        flag = 1
    if " absolutely light " in msgs:
        qtns.append(" absolutely light ")
        anss.append("What do you mean by absolutely light? Please specify. ")
        flag = 1
    if " most likely " in msgs:
        qtns.append(" most likely ")
        anss.append("What do you mean by most likely? Please specify. ")
        flag = 1
    if " least likely " in msgs:
        qtns.append(" least likely ")
        anss.append("What do you mean by least likely? Please specify. ")
        flag = 1
    if " very likely " in msgs:
        qtns.append(" very likely ")
        anss.append("What do you mean by very likely? Please specify. ")
        flag = 1
    if " extremely likely " in msgs:
        qtns.append(" extremely likely ")
        anss.append("What do you mean by extremely likely? Please specify. ")
        flag = 1
    if " especially likely " in msgs:
        qtns.append(" especially likely ")
        anss.append("What do you mean by especially likely? Please specify. ")
        flag = 1
    if " absolutely likely " in msgs:
        qtns.append(" absolutely likely ")
        anss.append("What do you mean by absolutely likely? Please specify. ")
        flag = 1
    if " most literate " in msgs:
        qtns.append(" most literate ")
        anss.append("What do you mean by most literate? Please specify. ")
        flag = 1
    if " least literate " in msgs:
        qtns.append(" least literate ")
        anss.append("What do you mean by least literate? Please specify. ")
        flag = 1
    if " very literate " in msgs:
        qtns.append(" very literate ")
        anss.append("What do you mean by very literate? Please specify. ")
        flag = 1
    if " extremely literate " in msgs:
        qtns.append(" extremely literate ")
        anss.append("What do you mean by extremely literate? Please specify. ")
        flag = 1
    if " especially literate " in msgs:
        qtns.append(" especially literate ")
        anss.append("What do you mean by especially literate? Please specify. ")
        flag = 1
    if " absolutely literate " in msgs:
        qtns.append(" absolutely literate ")
        anss.append("What do you mean by absolutely literate? Please specify. ")
        flag = 1
    if " most little " in msgs:
        qtns.append(" most little ")
        anss.append("What do you mean by most little? Please specify. ")
        flag = 1
    if " least little " in msgs:
        qtns.append(" least little ")
        anss.append("What do you mean by least little? Please specify. ")
        flag = 1
    if " very little " in msgs:
        qtns.append(" very little ")
        anss.append("What do you mean by very little? Please specify. ")
        flag = 1
    if " extremely little " in msgs:
        qtns.append(" extremely little ")
        anss.append("What do you mean by extremely little? Please specify. ")
        flag = 1
    if " especially little " in msgs:
        qtns.append(" especially little ")
        anss.append("What do you mean by especially little? Please specify. ")
        flag = 1
    if " absolutely little " in msgs:
        qtns.append(" absolutely little ")
        anss.append("What do you mean by absolutely little? Please specify. ")
        flag = 1
    if " most little " in msgs:
        qtns.append(" most little ")
        anss.append("What do you mean by most little? Please specify. ")
        flag = 1
    if " least little " in msgs:
        qtns.append(" least little ")
        anss.append("What do you mean by least little? Please specify. ")
        flag = 1
    if " very little " in msgs:
        qtns.append(" very little ")
        anss.append("What do you mean by very little? Please specify. ")
        flag = 1
    if " extremely little " in msgs:
        qtns.append(" extremely little ")
        anss.append("What do you mean by extremely little? Please specify. ")
        flag = 1
    if " especially little " in msgs:
        qtns.append(" especially little ")
        anss.append("What do you mean by especially little? Please specify. ")
        flag = 1
    if " absolutely little " in msgs:
        qtns.append(" absolutely little ")
        anss.append("What do you mean by absolutely little? Please specify. ")
        flag = 1
    if " most lively " in msgs:
        qtns.append(" most lively ")
        anss.append("What do you mean by most lively? Please specify. ")
        flag = 1
    if " least lively " in msgs:
        qtns.append(" least lively ")
        anss.append("What do you mean by least lively? Please specify. ")
        flag = 1
    if " very lively " in msgs:
        qtns.append(" very lively ")
        anss.append("What do you mean by very lively? Please specify. ")
        flag = 1
    if " extremely lively " in msgs:
        qtns.append(" extremely lively ")
        anss.append("What do you mean by extremely lively? Please specify. ")
        flag = 1
    if " especially lively " in msgs:
        qtns.append(" especially lively ")
        anss.append("What do you mean by especially lively? Please specify. ")
        flag = 1
    if " absolutely lively " in msgs:
        qtns.append(" absolutely lively ")
        anss.append("What do you mean by absolutely lively? Please specify. ")
        flag = 1
    if " most lonely " in msgs:
        qtns.append(" most lonely ")
        anss.append("What do you mean by most lonely? Please specify. ")
        flag = 1
    if " least lonely " in msgs:
        qtns.append(" least lonely ")
        anss.append("What do you mean by least lonely? Please specify. ")
        flag = 1
    if " very lonely " in msgs:
        qtns.append(" very lonely ")
        anss.append("What do you mean by very lonely? Please specify. ")
        flag = 1
    if " extremely lonely " in msgs:
        qtns.append(" extremely lonely ")
        anss.append("What do you mean by extremely lonely? Please specify. ")
        flag = 1
    if " especially lonely " in msgs:
        qtns.append(" especially lonely ")
        anss.append("What do you mean by especially lonely? Please specify. ")
        flag = 1
    if " absolutely lonely " in msgs:
        qtns.append(" absolutely lonely ")
        anss.append("What do you mean by absolutely lonely? Please specify. ")
        flag = 1
    if " most long " in msgs:
        qtns.append(" most long ")
        anss.append("What do you mean by most long? Please specify. ")
        flag = 1
    if " least long " in msgs:
        qtns.append(" least long ")
        anss.append("What do you mean by least long? Please specify. ")
        flag = 1
    if " very long " in msgs:
        qtns.append(" very long ")
        anss.append("What do you mean by very long? Please specify. ")
        flag = 1
    if " extremely long " in msgs:
        qtns.append(" extremely long ")
        anss.append("What do you mean by extremely long? Please specify. ")
        flag = 1
    if " especially long " in msgs:
        qtns.append(" especially long ")
        anss.append("What do you mean by especially long? Please specify. ")
        flag = 1
    if " absolutely long " in msgs:
        qtns.append(" absolutely long ")
        anss.append("What do you mean by absolutely long? Please specify. ")
        flag = 1
    if " most loud " in msgs:
        qtns.append(" most loud ")
        anss.append("What do you mean by most loud? Please specify. ")
        flag = 1
    if " least loud " in msgs:
        qtns.append(" least loud ")
        anss.append("What do you mean by least loud? Please specify. ")
        flag = 1
    if " very loud " in msgs:
        qtns.append(" very loud ")
        anss.append("What do you mean by very loud? Please specify. ")
        flag = 1
    if " extremely loud " in msgs:
        qtns.append(" extremely loud ")
        anss.append("What do you mean by extremely loud? Please specify. ")
        flag = 1
    if " especially loud " in msgs:
        qtns.append(" especially loud ")
        anss.append("What do you mean by especially loud? Please specify. ")
        flag = 1
    if " absolutely loud " in msgs:
        qtns.append(" absolutely loud ")
        anss.append("What do you mean by absolutely loud? Please specify. ")
        flag = 1
    if " most lovely " in msgs:
        qtns.append(" most lovely ")
        anss.append("What do you mean by most lovely? Please specify. ")
        flag = 1
    if " least lovely " in msgs:
        qtns.append(" least lovely ")
        anss.append("What do you mean by least lovely? Please specify. ")
        flag = 1
    if " very lovely " in msgs:
        qtns.append(" very lovely ")
        anss.append("What do you mean by very lovely? Please specify. ")
        flag = 1
    if " extremely lovely " in msgs:
        qtns.append(" extremely lovely ")
        anss.append("What do you mean by extremely lovely? Please specify. ")
        flag = 1
    if " especially lovely " in msgs:
        qtns.append(" especially lovely ")
        anss.append("What do you mean by especially lovely? Please specify. ")
        flag = 1
    if " absolutely lovely " in msgs:
        qtns.append(" absolutely lovely ")
        anss.append("What do you mean by absolutely lovely? Please specify. ")
        flag = 1
    if " most low " in msgs:
        qtns.append(" most low ")
        anss.append("What do you mean by most low? Please specify. ")
        flag = 1
    if " least low " in msgs:
        qtns.append(" least low ")
        anss.append("What do you mean by least low? Please specify. ")
        flag = 1
    if " very low " in msgs:
        qtns.append(" very low ")
        anss.append("What do you mean by very low? Please specify. ")
        flag = 1
    if " extremely low " in msgs:
        qtns.append(" extremely low ")
        anss.append("What do you mean by extremely low? Please specify. ")
        flag = 1
    if " especially low " in msgs:
        qtns.append(" especially low ")
        anss.append("What do you mean by especially low? Please specify. ")
        flag = 1
    if " absolutely low " in msgs:
        qtns.append(" absolutely low ")
        anss.append("What do you mean by absolutely low? Please specify. ")
        flag = 1
    if " most lucky " in msgs:
        qtns.append(" most lucky ")
        anss.append("What do you mean by most lucky? Please specify. ")
        flag = 1
    if " least lucky " in msgs:
        qtns.append(" least lucky ")
        anss.append("What do you mean by least lucky? Please specify. ")
        flag = 1
    if " very lucky " in msgs:
        qtns.append(" very lucky ")
        anss.append("What do you mean by very lucky? Please specify. ")
        flag = 1
    if " extremely lucky " in msgs:
        qtns.append(" extremely lucky ")
        anss.append("What do you mean by extremely lucky? Please specify. ")
        flag = 1
    if " especially lucky " in msgs:
        qtns.append(" especially lucky ")
        anss.append("What do you mean by especially lucky? Please specify. ")
        flag = 1
    if " absolutely lucky " in msgs:
        qtns.append(" absolutely lucky ")
        anss.append("What do you mean by absolutely lucky? Please specify. ")
        flag = 1
    if " most macho " in msgs:
        qtns.append(" most macho ")
        anss.append("What do you mean by most macho? Please specify. ")
        flag = 1
    if " least macho " in msgs:
        qtns.append(" least macho ")
        anss.append("What do you mean by least macho? Please specify. ")
        flag = 1
    if " very macho " in msgs:
        qtns.append(" very macho ")
        anss.append("What do you mean by very macho? Please specify. ")
        flag = 1
    if " extremely macho " in msgs:
        qtns.append(" extremely macho ")
        anss.append("What do you mean by extremely macho? Please specify. ")
        flag = 1
    if " especially macho " in msgs:
        qtns.append(" especially macho ")
        anss.append("What do you mean by especially macho? Please specify. ")
        flag = 1
    if " absolutely macho " in msgs:
        qtns.append(" absolutely macho ")
        anss.append("What do you mean by absolutely macho? Please specify. ")
        flag = 1
    if " most mad " in msgs:
        qtns.append(" most mad ")
        anss.append("What do you mean by most mad? Please specify. ")
        flag = 1
    if " least mad " in msgs:
        qtns.append(" least mad ")
        anss.append("What do you mean by least mad? Please specify. ")
        flag = 1
    if " very mad " in msgs:
        qtns.append(" very mad ")
        anss.append("What do you mean by very mad? Please specify. ")
        flag = 1
    if " extremely mad " in msgs:
        qtns.append(" extremely mad ")
        anss.append("What do you mean by extremely mad? Please specify. ")
        flag = 1
    if " especially mad " in msgs:
        qtns.append(" especially mad ")
        anss.append("What do you mean by especially mad? Please specify. ")
        flag = 1
    if " absolutely mad " in msgs:
        qtns.append(" absolutely mad ")
        anss.append("What do you mean by absolutely mad? Please specify. ")
        flag = 1
    if " most magical " in msgs:
        qtns.append(" most magical ")
        anss.append("What do you mean by most magical? Please specify. ")
        flag = 1
    if " least magical " in msgs:
        qtns.append(" least magical ")
        anss.append("What do you mean by least magical? Please specify. ")
        flag = 1
    if " very magical " in msgs:
        qtns.append(" very magical ")
        anss.append("What do you mean by very magical? Please specify. ")
        flag = 1
    if " extremely magical " in msgs:
        qtns.append(" extremely magical ")
        anss.append("What do you mean by extremely magical? Please specify. ")
        flag = 1
    if " especially magical " in msgs:
        qtns.append(" especially magical ")
        anss.append("What do you mean by especially magical? Please specify. ")
        flag = 1
    if " absolutely magical " in msgs:
        qtns.append(" absolutely magical ")
        anss.append("What do you mean by absolutely magical? Please specify. ")
        flag = 1
    if " most magnificent " in msgs:
        qtns.append(" most magnificent ")
        anss.append("What do you mean by most magnificent? Please specify. ")
        flag = 1
    if " least magnificent " in msgs:
        qtns.append(" least magnificent ")
        anss.append("What do you mean by least magnificent? Please specify. ")
        flag = 1
    if " very magnificent " in msgs:
        qtns.append(" very magnificent ")
        anss.append("What do you mean by very magnificent? Please specify. ")
        flag = 1
    if " extremely magnificent " in msgs:
        qtns.append(" extremely magnificent ")
        anss.append("What do you mean by extremely magnificent? Please specify. ")
        flag = 1
    if " especially magnificent " in msgs:
        qtns.append(" especially magnificent ")
        anss.append("What do you mean by especially magnificent? Please specify. ")
        flag = 1
    if " absolutely magnificent " in msgs:
        qtns.append(" absolutely magnificent ")
        anss.append("What do you mean by absolutely magnificent? Please specify. ")
        flag = 1
    if " most many / much  " in msgs:
        qtns.append(" most many / much  ")
        anss.append("What do you mean by most many / much ? Please specify. ")
        flag = 1
    if " least many / much  " in msgs:
        qtns.append(" least many / much  ")
        anss.append("What do you mean by least many / much ? Please specify. ")
        flag = 1
    if " very many / much  " in msgs:
        qtns.append(" very many / much  ")
        anss.append("What do you mean by very many / much ? Please specify. ")
        flag = 1
    if " extremely many / much  " in msgs:
        qtns.append(" extremely many / much  ")
        anss.append("What do you mean by extremely many / much ? Please specify. ")
        flag = 1
    if " especially many / much  " in msgs:
        qtns.append(" especially many / much  ")
        anss.append("What do you mean by especially many / much ? Please specify. ")
        flag = 1
    if " absolutely many / much  " in msgs:
        qtns.append(" absolutely many / much  ")
        anss.append("What do you mean by absolutely many / much ? Please specify. ")
        flag = 1
    if " most massive " in msgs:
        qtns.append(" most massive ")
        anss.append("What do you mean by most massive? Please specify. ")
        flag = 1
    if " least massive " in msgs:
        qtns.append(" least massive ")
        anss.append("What do you mean by least massive? Please specify. ")
        flag = 1
    if " very massive " in msgs:
        qtns.append(" very massive ")
        anss.append("What do you mean by very massive? Please specify. ")
        flag = 1
    if " extremely massive " in msgs:
        qtns.append(" extremely massive ")
        anss.append("What do you mean by extremely massive? Please specify. ")
        flag = 1
    if " especially massive " in msgs:
        qtns.append(" especially massive ")
        anss.append("What do you mean by especially massive? Please specify. ")
        flag = 1
    if " absolutely massive " in msgs:
        qtns.append(" absolutely massive ")
        anss.append("What do you mean by absolutely massive? Please specify. ")
        flag = 1
    if " most mature " in msgs:
        qtns.append(" most mature ")
        anss.append("What do you mean by most mature? Please specify. ")
        flag = 1
    if " least mature " in msgs:
        qtns.append(" least mature ")
        anss.append("What do you mean by least mature? Please specify. ")
        flag = 1
    if " very mature " in msgs:
        qtns.append(" very mature ")
        anss.append("What do you mean by very mature? Please specify. ")
        flag = 1
    if " extremely mature " in msgs:
        qtns.append(" extremely mature ")
        anss.append("What do you mean by extremely mature? Please specify. ")
        flag = 1
    if " especially mature " in msgs:
        qtns.append(" especially mature ")
        anss.append("What do you mean by especially mature? Please specify. ")
        flag = 1
    if " absolutely mature " in msgs:
        qtns.append(" absolutely mature ")
        anss.append("What do you mean by absolutely mature? Please specify. ")
        flag = 1
    if " most mean " in msgs:
        qtns.append(" most mean ")
        anss.append("What do you mean by most mean? Please specify. ")
        flag = 1
    if " least mean " in msgs:
        qtns.append(" least mean ")
        anss.append("What do you mean by least mean? Please specify. ")
        flag = 1
    if " very mean " in msgs:
        qtns.append(" very mean ")
        anss.append("What do you mean by very mean? Please specify. ")
        flag = 1
    if " extremely mean " in msgs:
        qtns.append(" extremely mean ")
        anss.append("What do you mean by extremely mean? Please specify. ")
        flag = 1
    if " especially mean " in msgs:
        qtns.append(" especially mean ")
        anss.append("What do you mean by especially mean? Please specify. ")
        flag = 1
    if " absolutely mean " in msgs:
        qtns.append(" absolutely mean ")
        anss.append("What do you mean by absolutely mean? Please specify. ")
        flag = 1
    if " most messy " in msgs:
        qtns.append(" most messy ")
        anss.append("What do you mean by most messy? Please specify. ")
        flag = 1
    if " least messy " in msgs:
        qtns.append(" least messy ")
        anss.append("What do you mean by least messy? Please specify. ")
        flag = 1
    if " very messy " in msgs:
        qtns.append(" very messy ")
        anss.append("What do you mean by very messy? Please specify. ")
        flag = 1
    if " extremely messy " in msgs:
        qtns.append(" extremely messy ")
        anss.append("What do you mean by extremely messy? Please specify. ")
        flag = 1
    if " especially messy " in msgs:
        qtns.append(" especially messy ")
        anss.append("What do you mean by especially messy? Please specify. ")
        flag = 1
    if " absolutely messy " in msgs:
        qtns.append(" absolutely messy ")
        anss.append("What do you mean by absolutely messy? Please specify. ")
        flag = 1
    if " most mild " in msgs:
        qtns.append(" most mild ")
        anss.append("What do you mean by most mild? Please specify. ")
        flag = 1
    if " least mild " in msgs:
        qtns.append(" least mild ")
        anss.append("What do you mean by least mild? Please specify. ")
        flag = 1
    if " very mild " in msgs:
        qtns.append(" very mild ")
        anss.append("What do you mean by very mild? Please specify. ")
        flag = 1
    if " extremely mild " in msgs:
        qtns.append(" extremely mild ")
        anss.append("What do you mean by extremely mild? Please specify. ")
        flag = 1
    if " especially mild " in msgs:
        qtns.append(" especially mild ")
        anss.append("What do you mean by especially mild? Please specify. ")
        flag = 1
    if " absolutely mild " in msgs:
        qtns.append(" absolutely mild ")
        anss.append("What do you mean by absolutely mild? Please specify. ")
        flag = 1
    if " most modern " in msgs:
        qtns.append(" most modern ")
        anss.append("What do you mean by most modern? Please specify. ")
        flag = 1
    if " least modern " in msgs:
        qtns.append(" least modern ")
        anss.append("What do you mean by least modern? Please specify. ")
        flag = 1
    if " very modern " in msgs:
        qtns.append(" very modern ")
        anss.append("What do you mean by very modern? Please specify. ")
        flag = 1
    if " extremely modern " in msgs:
        qtns.append(" extremely modern ")
        anss.append("What do you mean by extremely modern? Please specify. ")
        flag = 1
    if " especially modern " in msgs:
        qtns.append(" especially modern ")
        anss.append("What do you mean by especially modern? Please specify. ")
        flag = 1
    if " absolutely modern " in msgs:
        qtns.append(" absolutely modern ")
        anss.append("What do you mean by absolutely modern? Please specify. ")
        flag = 1
    if " most moist " in msgs:
        qtns.append(" most moist ")
        anss.append("What do you mean by most moist? Please specify. ")
        flag = 1
    if " least moist " in msgs:
        qtns.append(" least moist ")
        anss.append("What do you mean by least moist? Please specify. ")
        flag = 1
    if " very moist " in msgs:
        qtns.append(" very moist ")
        anss.append("What do you mean by very moist? Please specify. ")
        flag = 1
    if " extremely moist " in msgs:
        qtns.append(" extremely moist ")
        anss.append("What do you mean by extremely moist? Please specify. ")
        flag = 1
    if " especially moist " in msgs:
        qtns.append(" especially moist ")
        anss.append("What do you mean by especially moist? Please specify. ")
        flag = 1
    if " absolutely moist " in msgs:
        qtns.append(" absolutely moist ")
        anss.append("What do you mean by absolutely moist? Please specify. ")
        flag = 1
    if " most narrow " in msgs:
        qtns.append(" most narrow ")
        anss.append("What do you mean by most narrow? Please specify. ")
        flag = 1
    if " least narrow " in msgs:
        qtns.append(" least narrow ")
        anss.append("What do you mean by least narrow? Please specify. ")
        flag = 1
    if " very narrow " in msgs:
        qtns.append(" very narrow ")
        anss.append("What do you mean by very narrow? Please specify. ")
        flag = 1
    if " extremely narrow " in msgs:
        qtns.append(" extremely narrow ")
        anss.append("What do you mean by extremely narrow? Please specify. ")
        flag = 1
    if " especially narrow " in msgs:
        qtns.append(" especially narrow ")
        anss.append("What do you mean by especially narrow? Please specify. ")
        flag = 1
    if " absolutely narrow " in msgs:
        qtns.append(" absolutely narrow ")
        anss.append("What do you mean by absolutely narrow? Please specify. ")
        flag = 1
    if " most nasty " in msgs:
        qtns.append(" most nasty ")
        anss.append("What do you mean by most nasty? Please specify. ")
        flag = 1
    if " least nasty " in msgs:
        qtns.append(" least nasty ")
        anss.append("What do you mean by least nasty? Please specify. ")
        flag = 1
    if " very nasty " in msgs:
        qtns.append(" very nasty ")
        anss.append("What do you mean by very nasty? Please specify. ")
        flag = 1
    if " extremely nasty " in msgs:
        qtns.append(" extremely nasty ")
        anss.append("What do you mean by extremely nasty? Please specify. ")
        flag = 1
    if " especially nasty " in msgs:
        qtns.append(" especially nasty ")
        anss.append("What do you mean by especially nasty? Please specify. ")
        flag = 1
    if " absolutely nasty " in msgs:
        qtns.append(" absolutely nasty ")
        anss.append("What do you mean by absolutely nasty? Please specify. ")
        flag = 1
    if " most naughty " in msgs:
        qtns.append(" most naughty ")
        anss.append("What do you mean by most naughty? Please specify. ")
        flag = 1
    if " least naughty " in msgs:
        qtns.append(" least naughty ")
        anss.append("What do you mean by least naughty? Please specify. ")
        flag = 1
    if " very naughty " in msgs:
        qtns.append(" very naughty ")
        anss.append("What do you mean by very naughty? Please specify. ")
        flag = 1
    if " extremely naughty " in msgs:
        qtns.append(" extremely naughty ")
        anss.append("What do you mean by extremely naughty? Please specify. ")
        flag = 1
    if " especially naughty " in msgs:
        qtns.append(" especially naughty ")
        anss.append("What do you mean by especially naughty? Please specify. ")
        flag = 1
    if " absolutely naughty " in msgs:
        qtns.append(" absolutely naughty ")
        anss.append("What do you mean by absolutely naughty? Please specify. ")
        flag = 1
    if " most near " in msgs:
        qtns.append(" most near ")
        anss.append("What do you mean by most near? Please specify. ")
        flag = 1
    if " least near " in msgs:
        qtns.append(" least near ")
        anss.append("What do you mean by least near? Please specify. ")
        flag = 1
    if " very near " in msgs:
        qtns.append(" very near ")
        anss.append("What do you mean by very near? Please specify. ")
        flag = 1
    if " extremely near " in msgs:
        qtns.append(" extremely near ")
        anss.append("What do you mean by extremely near? Please specify. ")
        flag = 1
    if " especially near " in msgs:
        qtns.append(" especially near ")
        anss.append("What do you mean by especially near? Please specify. ")
        flag = 1
    if " absolutely near " in msgs:
        qtns.append(" absolutely near ")
        anss.append("What do you mean by absolutely near? Please specify. ")
        flag = 1
    if " most neat " in msgs:
        qtns.append(" most neat ")
        anss.append("What do you mean by most neat? Please specify. ")
        flag = 1
    if " least neat " in msgs:
        qtns.append(" least neat ")
        anss.append("What do you mean by least neat? Please specify. ")
        flag = 1
    if " very neat " in msgs:
        qtns.append(" very neat ")
        anss.append("What do you mean by very neat? Please specify. ")
        flag = 1
    if " extremely neat " in msgs:
        qtns.append(" extremely neat ")
        anss.append("What do you mean by extremely neat? Please specify. ")
        flag = 1
    if " especially neat " in msgs:
        qtns.append(" especially neat ")
        anss.append("What do you mean by especially neat? Please specify. ")
        flag = 1
    if " absolutely neat " in msgs:
        qtns.append(" absolutely neat ")
        anss.append("What do you mean by absolutely neat? Please specify. ")
        flag = 1
    if " most needy " in msgs:
        qtns.append(" most needy ")
        anss.append("What do you mean by most needy? Please specify. ")
        flag = 1
    if " least needy " in msgs:
        qtns.append(" least needy ")
        anss.append("What do you mean by least needy? Please specify. ")
        flag = 1
    if " very needy " in msgs:
        qtns.append(" very needy ")
        anss.append("What do you mean by very needy? Please specify. ")
        flag = 1
    if " extremely needy " in msgs:
        qtns.append(" extremely needy ")
        anss.append("What do you mean by extremely needy? Please specify. ")
        flag = 1
    if " especially needy " in msgs:
        qtns.append(" especially needy ")
        anss.append("What do you mean by especially needy? Please specify. ")
        flag = 1
    if " absolutely needy " in msgs:
        qtns.append(" absolutely needy ")
        anss.append("What do you mean by absolutely needy? Please specify. ")
        flag = 1
    if " most nervous " in msgs:
        qtns.append(" most nervous ")
        anss.append("What do you mean by most nervous? Please specify. ")
        flag = 1
    if " least nervous " in msgs:
        qtns.append(" least nervous ")
        anss.append("What do you mean by least nervous? Please specify. ")
        flag = 1
    if " very nervous " in msgs:
        qtns.append(" very nervous ")
        anss.append("What do you mean by very nervous? Please specify. ")
        flag = 1
    if " extremely nervous " in msgs:
        qtns.append(" extremely nervous ")
        anss.append("What do you mean by extremely nervous? Please specify. ")
        flag = 1
    if " especially nervous " in msgs:
        qtns.append(" especially nervous ")
        anss.append("What do you mean by especially nervous? Please specify. ")
        flag = 1
    if " absolutely nervous " in msgs:
        qtns.append(" absolutely nervous ")
        anss.append("What do you mean by absolutely nervous? Please specify. ")
        flag = 1
    if " most new " in msgs:
        qtns.append(" most new ")
        anss.append("What do you mean by most new? Please specify. ")
        flag = 1
    if " least new " in msgs:
        qtns.append(" least new ")
        anss.append("What do you mean by least new? Please specify. ")
        flag = 1
    if " very new " in msgs:
        qtns.append(" very new ")
        anss.append("What do you mean by very new? Please specify. ")
        flag = 1
    if " extremely new " in msgs:
        qtns.append(" extremely new ")
        anss.append("What do you mean by extremely new? Please specify. ")
        flag = 1
    if " especially new " in msgs:
        qtns.append(" especially new ")
        anss.append("What do you mean by especially new? Please specify. ")
        flag = 1
    if " absolutely new " in msgs:
        qtns.append(" absolutely new ")
        anss.append("What do you mean by absolutely new? Please specify. ")
        flag = 1
    if " most nice " in msgs:
        qtns.append(" most nice ")
        anss.append("What do you mean by most nice? Please specify. ")
        flag = 1
    if " least nice " in msgs:
        qtns.append(" least nice ")
        anss.append("What do you mean by least nice? Please specify. ")
        flag = 1
    if " very nice " in msgs:
        qtns.append(" very nice ")
        anss.append("What do you mean by very nice? Please specify. ")
        flag = 1
    if " extremely nice " in msgs:
        qtns.append(" extremely nice ")
        anss.append("What do you mean by extremely nice? Please specify. ")
        flag = 1
    if " especially nice " in msgs:
        qtns.append(" especially nice ")
        anss.append("What do you mean by especially nice? Please specify. ")
        flag = 1
    if " absolutely nice " in msgs:
        qtns.append(" absolutely nice ")
        anss.append("What do you mean by absolutely nice? Please specify. ")
        flag = 1
    if " most noisy " in msgs:
        qtns.append(" most noisy ")
        anss.append("What do you mean by most noisy? Please specify. ")
        flag = 1
    if " least noisy " in msgs:
        qtns.append(" least noisy ")
        anss.append("What do you mean by least noisy? Please specify. ")
        flag = 1
    if " very noisy " in msgs:
        qtns.append(" very noisy ")
        anss.append("What do you mean by very noisy? Please specify. ")
        flag = 1
    if " extremely noisy " in msgs:
        qtns.append(" extremely noisy ")
        anss.append("What do you mean by extremely noisy? Please specify. ")
        flag = 1
    if " especially noisy " in msgs:
        qtns.append(" especially noisy ")
        anss.append("What do you mean by especially noisy? Please specify. ")
        flag = 1
    if " absolutely noisy " in msgs:
        qtns.append(" absolutely noisy ")
        anss.append("What do you mean by absolutely noisy? Please specify. ")
        flag = 1
    if " most nutritious " in msgs:
        qtns.append(" most nutritious ")
        anss.append("What do you mean by most nutritious? Please specify. ")
        flag = 1
    if " least nutritious " in msgs:
        qtns.append(" least nutritious ")
        anss.append("What do you mean by least nutritious? Please specify. ")
        flag = 1
    if " very nutritious " in msgs:
        qtns.append(" very nutritious ")
        anss.append("What do you mean by very nutritious? Please specify. ")
        flag = 1
    if " extremely nutritious " in msgs:
        qtns.append(" extremely nutritious ")
        anss.append("What do you mean by extremely nutritious? Please specify. ")
        flag = 1
    if " especially nutritious " in msgs:
        qtns.append(" especially nutritious ")
        anss.append("What do you mean by especially nutritious? Please specify. ")
        flag = 1
    if " absolutely nutritious " in msgs:
        qtns.append(" absolutely nutritious ")
        anss.append("What do you mean by absolutely nutritious? Please specify. ")
        flag = 1
    if " most obedient " in msgs:
        qtns.append(" most obedient ")
        anss.append("What do you mean by most obedient? Please specify. ")
        flag = 1
    if " least obedient " in msgs:
        qtns.append(" least obedient ")
        anss.append("What do you mean by least obedient? Please specify. ")
        flag = 1
    if " very obedient " in msgs:
        qtns.append(" very obedient ")
        anss.append("What do you mean by very obedient? Please specify. ")
        flag = 1
    if " extremely obedient " in msgs:
        qtns.append(" extremely obedient ")
        anss.append("What do you mean by extremely obedient? Please specify. ")
        flag = 1
    if " especially obedient " in msgs:
        qtns.append(" especially obedient ")
        anss.append("What do you mean by especially obedient? Please specify. ")
        flag = 1
    if " absolutely obedient " in msgs:
        qtns.append(" absolutely obedient ")
        anss.append("What do you mean by absolutely obedient? Please specify. ")
        flag = 1
    if " most obese " in msgs:
        qtns.append(" most obese ")
        anss.append("What do you mean by most obese? Please specify. ")
        flag = 1
    if " least obese " in msgs:
        qtns.append(" least obese ")
        anss.append("What do you mean by least obese? Please specify. ")
        flag = 1
    if " very obese " in msgs:
        qtns.append(" very obese ")
        anss.append("What do you mean by very obese? Please specify. ")
        flag = 1
    if " extremely obese " in msgs:
        qtns.append(" extremely obese ")
        anss.append("What do you mean by extremely obese? Please specify. ")
        flag = 1
    if " especially obese " in msgs:
        qtns.append(" especially obese ")
        anss.append("What do you mean by especially obese? Please specify. ")
        flag = 1
    if " absolutely obese " in msgs:
        qtns.append(" absolutely obese ")
        anss.append("What do you mean by absolutely obese? Please specify. ")
        flag = 1
    if " most obnoxious " in msgs:
        qtns.append(" most obnoxious ")
        anss.append("What do you mean by most obnoxious? Please specify. ")
        flag = 1
    if " least obnoxious " in msgs:
        qtns.append(" least obnoxious ")
        anss.append("What do you mean by least obnoxious? Please specify. ")
        flag = 1
    if " very obnoxious " in msgs:
        qtns.append(" very obnoxious ")
        anss.append("What do you mean by very obnoxious? Please specify. ")
        flag = 1
    if " extremely obnoxious " in msgs:
        qtns.append(" extremely obnoxious ")
        anss.append("What do you mean by extremely obnoxious? Please specify. ")
        flag = 1
    if " especially obnoxious " in msgs:
        qtns.append(" especially obnoxious ")
        anss.append("What do you mean by especially obnoxious? Please specify. ")
        flag = 1
    if " absolutely obnoxious " in msgs:
        qtns.append(" absolutely obnoxious ")
        anss.append("What do you mean by absolutely obnoxious? Please specify. ")
        flag = 1
    if " most odd " in msgs:
        qtns.append(" most odd ")
        anss.append("What do you mean by most odd? Please specify. ")
        flag = 1
    if " least odd " in msgs:
        qtns.append(" least odd ")
        anss.append("What do you mean by least odd? Please specify. ")
        flag = 1
    if " very odd " in msgs:
        qtns.append(" very odd ")
        anss.append("What do you mean by very odd? Please specify. ")
        flag = 1
    if " extremely odd " in msgs:
        qtns.append(" extremely odd ")
        anss.append("What do you mean by extremely odd? Please specify. ")
        flag = 1
    if " especially odd " in msgs:
        qtns.append(" especially odd ")
        anss.append("What do you mean by especially odd? Please specify. ")
        flag = 1
    if " absolutely odd " in msgs:
        qtns.append(" absolutely odd ")
        anss.append("What do you mean by absolutely odd? Please specify. ")
        flag = 1
    if " most oily " in msgs:
        qtns.append(" most oily ")
        anss.append("What do you mean by most oily? Please specify. ")
        flag = 1
    if " least oily " in msgs:
        qtns.append(" least oily ")
        anss.append("What do you mean by least oily? Please specify. ")
        flag = 1
    if " very oily " in msgs:
        qtns.append(" very oily ")
        anss.append("What do you mean by very oily? Please specify. ")
        flag = 1
    if " extremely oily " in msgs:
        qtns.append(" extremely oily ")
        anss.append("What do you mean by extremely oily? Please specify. ")
        flag = 1
    if " especially oily " in msgs:
        qtns.append(" especially oily ")
        anss.append("What do you mean by especially oily? Please specify. ")
        flag = 1
    if " absolutely oily " in msgs:
        qtns.append(" absolutely oily ")
        anss.append("What do you mean by absolutely oily? Please specify. ")
        flag = 1
    if " most old " in msgs:
        qtns.append(" most old ")
        anss.append("What do you mean by most old? Please specify. ")
        flag = 1
    if " least old " in msgs:
        qtns.append(" least old ")
        anss.append("What do you mean by least old? Please specify. ")
        flag = 1
    if " very old " in msgs:
        qtns.append(" very old ")
        anss.append("What do you mean by very old? Please specify. ")
        flag = 1
    if " extremely old " in msgs:
        qtns.append(" extremely old ")
        anss.append("What do you mean by extremely old? Please specify. ")
        flag = 1
    if " especially old " in msgs:
        qtns.append(" especially old ")
        anss.append("What do you mean by especially old? Please specify. ")
        flag = 1
    if " absolutely old " in msgs:
        qtns.append(" absolutely old ")
        anss.append("What do you mean by absolutely old? Please specify. ")
        flag = 1
    if " most old " in msgs:
        qtns.append(" most old ")
        anss.append("What do you mean by most old? Please specify. ")
        flag = 1
    if " least old " in msgs:
        qtns.append(" least old ")
        anss.append("What do you mean by least old? Please specify. ")
        flag = 1
    if " very old " in msgs:
        qtns.append(" very old ")
        anss.append("What do you mean by very old? Please specify. ")
        flag = 1
    if " extremely old " in msgs:
        qtns.append(" extremely old ")
        anss.append("What do you mean by extremely old? Please specify. ")
        flag = 1
    if " especially old " in msgs:
        qtns.append(" especially old ")
        anss.append("What do you mean by especially old? Please specify. ")
        flag = 1
    if " absolutely old " in msgs:
        qtns.append(" absolutely old ")
        anss.append("What do you mean by absolutely old? Please specify. ")
        flag = 1
    if " most overconfident " in msgs:
        qtns.append(" most overconfident ")
        anss.append("What do you mean by most overconfident? Please specify. ")
        flag = 1
    if " least overconfident " in msgs:
        qtns.append(" least overconfident ")
        anss.append("What do you mean by least overconfident? Please specify. ")
        flag = 1
    if " very overconfident " in msgs:
        qtns.append(" very overconfident ")
        anss.append("What do you mean by very overconfident? Please specify. ")
        flag = 1
    if " extremely overconfident " in msgs:
        qtns.append(" extremely overconfident ")
        anss.append("What do you mean by extremely overconfident? Please specify. ")
        flag = 1
    if " especially overconfident " in msgs:
        qtns.append(" especially overconfident ")
        anss.append("What do you mean by especially overconfident? Please specify. ")
        flag = 1
    if " absolutely overconfident " in msgs:
        qtns.append(" absolutely overconfident ")
        anss.append("What do you mean by absolutely overconfident? Please specify. ")
        flag = 1
    if " most peaceful " in msgs:
        qtns.append(" most peaceful ")
        anss.append("What do you mean by most peaceful? Please specify. ")
        flag = 1
    if " least peaceful " in msgs:
        qtns.append(" least peaceful ")
        anss.append("What do you mean by least peaceful? Please specify. ")
        flag = 1
    if " very peaceful " in msgs:
        qtns.append(" very peaceful ")
        anss.append("What do you mean by very peaceful? Please specify. ")
        flag = 1
    if " extremely peaceful " in msgs:
        qtns.append(" extremely peaceful ")
        anss.append("What do you mean by extremely peaceful? Please specify. ")
        flag = 1
    if " especially peaceful " in msgs:
        qtns.append(" especially peaceful ")
        anss.append("What do you mean by especially peaceful? Please specify. ")
        flag = 1
    if " absolutely peaceful " in msgs:
        qtns.append(" absolutely peaceful ")
        anss.append("What do you mean by absolutely peaceful? Please specify. ")
        flag = 1
    if " most perfect " in msgs:
        qtns.append(" most perfect ")
        anss.append("What do you mean by most perfect? Please specify. ")
        flag = 1
    if " least perfect " in msgs:
        qtns.append(" least perfect ")
        anss.append("What do you mean by least perfect? Please specify. ")
        flag = 1
    if " very perfect " in msgs:
        qtns.append(" very perfect ")
        anss.append("What do you mean by very perfect? Please specify. ")
        flag = 1
    if " extremely perfect " in msgs:
        qtns.append(" extremely perfect ")
        anss.append("What do you mean by extremely perfect? Please specify. ")
        flag = 1
    if " especially perfect " in msgs:
        qtns.append(" especially perfect ")
        anss.append("What do you mean by especially perfect? Please specify. ")
        flag = 1
    if " absolutely perfect " in msgs:
        qtns.append(" absolutely perfect ")
        anss.append("What do you mean by absolutely perfect? Please specify. ")
        flag = 1
    if " most pink " in msgs:
        qtns.append(" most pink ")
        anss.append("What do you mean by most pink? Please specify. ")
        flag = 1
    if " least pink " in msgs:
        qtns.append(" least pink ")
        anss.append("What do you mean by least pink? Please specify. ")
        flag = 1
    if " very pink " in msgs:
        qtns.append(" very pink ")
        anss.append("What do you mean by very pink? Please specify. ")
        flag = 1
    if " extremely pink " in msgs:
        qtns.append(" extremely pink ")
        anss.append("What do you mean by extremely pink? Please specify. ")
        flag = 1
    if " especially pink " in msgs:
        qtns.append(" especially pink ")
        anss.append("What do you mean by especially pink? Please specify. ")
        flag = 1
    if " absolutely pink " in msgs:
        qtns.append(" absolutely pink ")
        anss.append("What do you mean by absolutely pink? Please specify. ")
        flag = 1
    if " most plain " in msgs:
        qtns.append(" most plain ")
        anss.append("What do you mean by most plain? Please specify. ")
        flag = 1
    if " least plain " in msgs:
        qtns.append(" least plain ")
        anss.append("What do you mean by least plain? Please specify. ")
        flag = 1
    if " very plain " in msgs:
        qtns.append(" very plain ")
        anss.append("What do you mean by very plain? Please specify. ")
        flag = 1
    if " extremely plain " in msgs:
        qtns.append(" extremely plain ")
        anss.append("What do you mean by extremely plain? Please specify. ")
        flag = 1
    if " especially plain " in msgs:
        qtns.append(" especially plain ")
        anss.append("What do you mean by especially plain? Please specify. ")
        flag = 1
    if " absolutely plain " in msgs:
        qtns.append(" absolutely plain ")
        anss.append("What do you mean by absolutely plain? Please specify. ")
        flag = 1
    if " most polite " in msgs:
        qtns.append(" most polite ")
        anss.append("What do you mean by most polite? Please specify. ")
        flag = 1
    if " least polite " in msgs:
        qtns.append(" least polite ")
        anss.append("What do you mean by least polite? Please specify. ")
        flag = 1
    if " very polite " in msgs:
        qtns.append(" very polite ")
        anss.append("What do you mean by very polite? Please specify. ")
        flag = 1
    if " extremely polite " in msgs:
        qtns.append(" extremely polite ")
        anss.append("What do you mean by extremely polite? Please specify. ")
        flag = 1
    if " especially polite " in msgs:
        qtns.append(" especially polite ")
        anss.append("What do you mean by especially polite? Please specify. ")
        flag = 1
    if " absolutely polite " in msgs:
        qtns.append(" absolutely polite ")
        anss.append("What do you mean by absolutely polite? Please specify. ")
        flag = 1
    if " most poor " in msgs:
        qtns.append(" most poor ")
        anss.append("What do you mean by most poor? Please specify. ")
        flag = 1
    if " least poor " in msgs:
        qtns.append(" least poor ")
        anss.append("What do you mean by least poor? Please specify. ")
        flag = 1
    if " very poor " in msgs:
        qtns.append(" very poor ")
        anss.append("What do you mean by very poor? Please specify. ")
        flag = 1
    if " extremely poor " in msgs:
        qtns.append(" extremely poor ")
        anss.append("What do you mean by extremely poor? Please specify. ")
        flag = 1
    if " especially poor " in msgs:
        qtns.append(" especially poor ")
        anss.append("What do you mean by especially poor? Please specify. ")
        flag = 1
    if " absolutely poor " in msgs:
        qtns.append(" absolutely poor ")
        anss.append("What do you mean by absolutely poor? Please specify. ")
        flag = 1
    if " most popular " in msgs:
        qtns.append(" most popular ")
        anss.append("What do you mean by most popular? Please specify. ")
        flag = 1
    if " least popular " in msgs:
        qtns.append(" least popular ")
        anss.append("What do you mean by least popular? Please specify. ")
        flag = 1
    if " very popular " in msgs:
        qtns.append(" very popular ")
        anss.append("What do you mean by very popular? Please specify. ")
        flag = 1
    if " extremely popular " in msgs:
        qtns.append(" extremely popular ")
        anss.append("What do you mean by extremely popular? Please specify. ")
        flag = 1
    if " especially popular " in msgs:
        qtns.append(" especially popular ")
        anss.append("What do you mean by especially popular? Please specify. ")
        flag = 1
    if " absolutely popular " in msgs:
        qtns.append(" absolutely popular ")
        anss.append("What do you mean by absolutely popular? Please specify. ")
        flag = 1
    if " most powerful " in msgs:
        qtns.append(" most powerful ")
        anss.append("What do you mean by most powerful? Please specify. ")
        flag = 1
    if " least powerful " in msgs:
        qtns.append(" least powerful ")
        anss.append("What do you mean by least powerful? Please specify. ")
        flag = 1
    if " very powerful " in msgs:
        qtns.append(" very powerful ")
        anss.append("What do you mean by very powerful? Please specify. ")
        flag = 1
    if " extremely powerful " in msgs:
        qtns.append(" extremely powerful ")
        anss.append("What do you mean by extremely powerful? Please specify. ")
        flag = 1
    if " especially powerful " in msgs:
        qtns.append(" especially powerful ")
        anss.append("What do you mean by especially powerful? Please specify. ")
        flag = 1
    if " absolutely powerful " in msgs:
        qtns.append(" absolutely powerful ")
        anss.append("What do you mean by absolutely powerful? Please specify. ")
        flag = 1
    if " most precious " in msgs:
        qtns.append(" most precious ")
        anss.append("What do you mean by most precious? Please specify. ")
        flag = 1
    if " least precious " in msgs:
        qtns.append(" least precious ")
        anss.append("What do you mean by least precious? Please specify. ")
        flag = 1
    if " very precious " in msgs:
        qtns.append(" very precious ")
        anss.append("What do you mean by very precious? Please specify. ")
        flag = 1
    if " extremely precious " in msgs:
        qtns.append(" extremely precious ")
        anss.append("What do you mean by extremely precious? Please specify. ")
        flag = 1
    if " especially precious " in msgs:
        qtns.append(" especially precious ")
        anss.append("What do you mean by especially precious? Please specify. ")
        flag = 1
    if " absolutely precious " in msgs:
        qtns.append(" absolutely precious ")
        anss.append("What do you mean by absolutely precious? Please specify. ")
        flag = 1
    if " most pretty " in msgs:
        qtns.append(" most pretty ")
        anss.append("What do you mean by most pretty? Please specify. ")
        flag = 1
    if " least pretty " in msgs:
        qtns.append(" least pretty ")
        anss.append("What do you mean by least pretty? Please specify. ")
        flag = 1
    if " very pretty " in msgs:
        qtns.append(" very pretty ")
        anss.append("What do you mean by very pretty? Please specify. ")
        flag = 1
    if " extremely pretty " in msgs:
        qtns.append(" extremely pretty ")
        anss.append("What do you mean by extremely pretty? Please specify. ")
        flag = 1
    if " especially pretty " in msgs:
        qtns.append(" especially pretty ")
        anss.append("What do you mean by especially pretty? Please specify. ")
        flag = 1
    if " absolutely pretty " in msgs:
        qtns.append(" absolutely pretty ")
        anss.append("What do you mean by absolutely pretty? Please specify. ")
        flag = 1
    if " most proud " in msgs:
        qtns.append(" most proud ")
        anss.append("What do you mean by most proud? Please specify. ")
        flag = 1
    if " least proud " in msgs:
        qtns.append(" least proud ")
        anss.append("What do you mean by least proud? Please specify. ")
        flag = 1
    if " very proud " in msgs:
        qtns.append(" very proud ")
        anss.append("What do you mean by very proud? Please specify. ")
        flag = 1
    if " extremely proud " in msgs:
        qtns.append(" extremely proud ")
        anss.append("What do you mean by extremely proud? Please specify. ")
        flag = 1
    if " especially proud " in msgs:
        qtns.append(" especially proud ")
        anss.append("What do you mean by especially proud? Please specify. ")
        flag = 1
    if " absolutely proud " in msgs:
        qtns.append(" absolutely proud ")
        anss.append("What do you mean by absolutely proud? Please specify. ")
        flag = 1
    if " most pure " in msgs:
        qtns.append(" most pure ")
        anss.append("What do you mean by most pure? Please specify. ")
        flag = 1
    if " least pure " in msgs:
        qtns.append(" least pure ")
        anss.append("What do you mean by least pure? Please specify. ")
        flag = 1
    if " very pure " in msgs:
        qtns.append(" very pure ")
        anss.append("What do you mean by very pure? Please specify. ")
        flag = 1
    if " extremely pure " in msgs:
        qtns.append(" extremely pure ")
        anss.append("What do you mean by extremely pure? Please specify. ")
        flag = 1
    if " especially pure " in msgs:
        qtns.append(" especially pure ")
        anss.append("What do you mean by especially pure? Please specify. ")
        flag = 1
    if " absolutely pure " in msgs:
        qtns.append(" absolutely pure ")
        anss.append("What do you mean by absolutely pure? Please specify. ")
        flag = 1
    if " most quick " in msgs:
        qtns.append(" most quick ")
        anss.append("What do you mean by most quick? Please specify. ")
        flag = 1
    if " least quick " in msgs:
        qtns.append(" least quick ")
        anss.append("What do you mean by least quick? Please specify. ")
        flag = 1
    if " very quick " in msgs:
        qtns.append(" very quick ")
        anss.append("What do you mean by very quick? Please specify. ")
        flag = 1
    if " extremely quick " in msgs:
        qtns.append(" extremely quick ")
        anss.append("What do you mean by extremely quick? Please specify. ")
        flag = 1
    if " especially quick " in msgs:
        qtns.append(" especially quick ")
        anss.append("What do you mean by especially quick? Please specify. ")
        flag = 1
    if " absolutely quick " in msgs:
        qtns.append(" absolutely quick ")
        anss.append("What do you mean by absolutely quick? Please specify. ")
        flag = 1
    if " most quiet " in msgs:
        qtns.append(" most quiet ")
        anss.append("What do you mean by most quiet? Please specify. ")
        flag = 1
    if " least quiet " in msgs:
        qtns.append(" least quiet ")
        anss.append("What do you mean by least quiet? Please specify. ")
        flag = 1
    if " very quiet " in msgs:
        qtns.append(" very quiet ")
        anss.append("What do you mean by very quiet? Please specify. ")
        flag = 1
    if " extremely quiet " in msgs:
        qtns.append(" extremely quiet ")
        anss.append("What do you mean by extremely quiet? Please specify. ")
        flag = 1
    if " especially quiet " in msgs:
        qtns.append(" especially quiet ")
        anss.append("What do you mean by especially quiet? Please specify. ")
        flag = 1
    if " absolutely quiet " in msgs:
        qtns.append(" absolutely quiet ")
        anss.append("What do you mean by absolutely quiet? Please specify. ")
        flag = 1
    if " most rapid " in msgs:
        qtns.append(" most rapid ")
        anss.append("What do you mean by most rapid? Please specify. ")
        flag = 1
    if " least rapid " in msgs:
        qtns.append(" least rapid ")
        anss.append("What do you mean by least rapid? Please specify. ")
        flag = 1
    if " very rapid " in msgs:
        qtns.append(" very rapid ")
        anss.append("What do you mean by very rapid? Please specify. ")
        flag = 1
    if " extremely rapid " in msgs:
        qtns.append(" extremely rapid ")
        anss.append("What do you mean by extremely rapid? Please specify. ")
        flag = 1
    if " especially rapid " in msgs:
        qtns.append(" especially rapid ")
        anss.append("What do you mean by especially rapid? Please specify. ")
        flag = 1
    if " absolutely rapid " in msgs:
        qtns.append(" absolutely rapid ")
        anss.append("What do you mean by absolutely rapid? Please specify. ")
        flag = 1
    if " most rare " in msgs:
        qtns.append(" most rare ")
        anss.append("What do you mean by most rare? Please specify. ")
        flag = 1
    if " least rare " in msgs:
        qtns.append(" least rare ")
        anss.append("What do you mean by least rare? Please specify. ")
        flag = 1
    if " very rare " in msgs:
        qtns.append(" very rare ")
        anss.append("What do you mean by very rare? Please specify. ")
        flag = 1
    if " extremely rare " in msgs:
        qtns.append(" extremely rare ")
        anss.append("What do you mean by extremely rare? Please specify. ")
        flag = 1
    if " especially rare " in msgs:
        qtns.append(" especially rare ")
        anss.append("What do you mean by especially rare? Please specify. ")
        flag = 1
    if " absolutely rare " in msgs:
        qtns.append(" absolutely rare ")
        anss.append("What do you mean by absolutely rare? Please specify. ")
        flag = 1
    if " most raw " in msgs:
        qtns.append(" most raw ")
        anss.append("What do you mean by most raw? Please specify. ")
        flag = 1
    if " least raw " in msgs:
        qtns.append(" least raw ")
        anss.append("What do you mean by least raw? Please specify. ")
        flag = 1
    if " very raw " in msgs:
        qtns.append(" very raw ")
        anss.append("What do you mean by very raw? Please specify. ")
        flag = 1
    if " extremely raw " in msgs:
        qtns.append(" extremely raw ")
        anss.append("What do you mean by extremely raw? Please specify. ")
        flag = 1
    if " especially raw " in msgs:
        qtns.append(" especially raw ")
        anss.append("What do you mean by especially raw? Please specify. ")
        flag = 1
    if " absolutely raw " in msgs:
        qtns.append(" absolutely raw ")
        anss.append("What do you mean by absolutely raw? Please specify. ")
        flag = 1
    if " most red " in msgs:
        qtns.append(" most red ")
        anss.append("What do you mean by most red? Please specify. ")
        flag = 1
    if " least red " in msgs:
        qtns.append(" least red ")
        anss.append("What do you mean by least red? Please specify. ")
        flag = 1
    if " very red " in msgs:
        qtns.append(" very red ")
        anss.append("What do you mean by very red? Please specify. ")
        flag = 1
    if " extremely red " in msgs:
        qtns.append(" extremely red ")
        anss.append("What do you mean by extremely red? Please specify. ")
        flag = 1
    if " especially red " in msgs:
        qtns.append(" especially red ")
        anss.append("What do you mean by especially red? Please specify. ")
        flag = 1
    if " absolutely red " in msgs:
        qtns.append(" absolutely red ")
        anss.append("What do you mean by absolutely red? Please specify. ")
        flag = 1
    if " most remarkable " in msgs:
        qtns.append(" most remarkable ")
        anss.append("What do you mean by most remarkable? Please specify. ")
        flag = 1
    if " least remarkable " in msgs:
        qtns.append(" least remarkable ")
        anss.append("What do you mean by least remarkable? Please specify. ")
        flag = 1
    if " very remarkable " in msgs:
        qtns.append(" very remarkable ")
        anss.append("What do you mean by very remarkable? Please specify. ")
        flag = 1
    if " extremely remarkable " in msgs:
        qtns.append(" extremely remarkable ")
        anss.append("What do you mean by extremely remarkable? Please specify. ")
        flag = 1
    if " especially remarkable " in msgs:
        qtns.append(" especially remarkable ")
        anss.append("What do you mean by especially remarkable? Please specify. ")
        flag = 1
    if " absolutely remarkable " in msgs:
        qtns.append(" absolutely remarkable ")
        anss.append("What do you mean by absolutely remarkable? Please specify. ")
        flag = 1
    if " most responsible " in msgs:
        qtns.append(" most responsible ")
        anss.append("What do you mean by most responsible? Please specify. ")
        flag = 1
    if " least responsible " in msgs:
        qtns.append(" least responsible ")
        anss.append("What do you mean by least responsible? Please specify. ")
        flag = 1
    if " very responsible " in msgs:
        qtns.append(" very responsible ")
        anss.append("What do you mean by very responsible? Please specify. ")
        flag = 1
    if " extremely responsible " in msgs:
        qtns.append(" extremely responsible ")
        anss.append("What do you mean by extremely responsible? Please specify. ")
        flag = 1
    if " especially responsible " in msgs:
        qtns.append(" especially responsible ")
        anss.append("What do you mean by especially responsible? Please specify. ")
        flag = 1
    if " absolutely responsible " in msgs:
        qtns.append(" absolutely responsible ")
        anss.append("What do you mean by absolutely responsible? Please specify. ")
        flag = 1
    if " most rich " in msgs:
        qtns.append(" most rich ")
        anss.append("What do you mean by most rich? Please specify. ")
        flag = 1
    if " least rich " in msgs:
        qtns.append(" least rich ")
        anss.append("What do you mean by least rich? Please specify. ")
        flag = 1
    if " very rich " in msgs:
        qtns.append(" very rich ")
        anss.append("What do you mean by very rich? Please specify. ")
        flag = 1
    if " extremely rich " in msgs:
        qtns.append(" extremely rich ")
        anss.append("What do you mean by extremely rich? Please specify. ")
        flag = 1
    if " especially rich " in msgs:
        qtns.append(" especially rich ")
        anss.append("What do you mean by especially rich? Please specify. ")
        flag = 1
    if " absolutely rich " in msgs:
        qtns.append(" absolutely rich ")
        anss.append("What do you mean by absolutely rich? Please specify. ")
        flag = 1
    if " most ripe " in msgs:
        qtns.append(" most ripe ")
        anss.append("What do you mean by most ripe? Please specify. ")
        flag = 1
    if " least ripe " in msgs:
        qtns.append(" least ripe ")
        anss.append("What do you mean by least ripe? Please specify. ")
        flag = 1
    if " very ripe " in msgs:
        qtns.append(" very ripe ")
        anss.append("What do you mean by very ripe? Please specify. ")
        flag = 1
    if " extremely ripe " in msgs:
        qtns.append(" extremely ripe ")
        anss.append("What do you mean by extremely ripe? Please specify. ")
        flag = 1
    if " especially ripe " in msgs:
        qtns.append(" especially ripe ")
        anss.append("What do you mean by especially ripe? Please specify. ")
        flag = 1
    if " absolutely ripe " in msgs:
        qtns.append(" absolutely ripe ")
        anss.append("What do you mean by absolutely ripe? Please specify. ")
        flag = 1
    if " most risky " in msgs:
        qtns.append(" most risky ")
        anss.append("What do you mean by most risky? Please specify. ")
        flag = 1
    if " least risky " in msgs:
        qtns.append(" least risky ")
        anss.append("What do you mean by least risky? Please specify. ")
        flag = 1
    if " very risky " in msgs:
        qtns.append(" very risky ")
        anss.append("What do you mean by very risky? Please specify. ")
        flag = 1
    if " extremely risky " in msgs:
        qtns.append(" extremely risky ")
        anss.append("What do you mean by extremely risky? Please specify. ")
        flag = 1
    if " especially risky " in msgs:
        qtns.append(" especially risky ")
        anss.append("What do you mean by especially risky? Please specify. ")
        flag = 1
    if " absolutely risky " in msgs:
        qtns.append(" absolutely risky ")
        anss.append("What do you mean by absolutely risky? Please specify. ")
        flag = 1
    if " most romantic " in msgs:
        qtns.append(" most romantic ")
        anss.append("What do you mean by most romantic? Please specify. ")
        flag = 1
    if " least romantic " in msgs:
        qtns.append(" least romantic ")
        anss.append("What do you mean by least romantic? Please specify. ")
        flag = 1
    if " very romantic " in msgs:
        qtns.append(" very romantic ")
        anss.append("What do you mean by very romantic? Please specify. ")
        flag = 1
    if " extremely romantic " in msgs:
        qtns.append(" extremely romantic ")
        anss.append("What do you mean by extremely romantic? Please specify. ")
        flag = 1
    if " especially romantic " in msgs:
        qtns.append(" especially romantic ")
        anss.append("What do you mean by especially romantic? Please specify. ")
        flag = 1
    if " absolutely romantic " in msgs:
        qtns.append(" absolutely romantic ")
        anss.append("What do you mean by absolutely romantic? Please specify. ")
        flag = 1
    if " most roomy " in msgs:
        qtns.append(" most roomy ")
        anss.append("What do you mean by most roomy? Please specify. ")
        flag = 1
    if " least roomy " in msgs:
        qtns.append(" least roomy ")
        anss.append("What do you mean by least roomy? Please specify. ")
        flag = 1
    if " very roomy " in msgs:
        qtns.append(" very roomy ")
        anss.append("What do you mean by very roomy? Please specify. ")
        flag = 1
    if " extremely roomy " in msgs:
        qtns.append(" extremely roomy ")
        anss.append("What do you mean by extremely roomy? Please specify. ")
        flag = 1
    if " especially roomy " in msgs:
        qtns.append(" especially roomy ")
        anss.append("What do you mean by especially roomy? Please specify. ")
        flag = 1
    if " absolutely roomy " in msgs:
        qtns.append(" absolutely roomy ")
        anss.append("What do you mean by absolutely roomy? Please specify. ")
        flag = 1
    if " most rough " in msgs:
        qtns.append(" most rough ")
        anss.append("What do you mean by most rough? Please specify. ")
        flag = 1
    if " least rough " in msgs:
        qtns.append(" least rough ")
        anss.append("What do you mean by least rough? Please specify. ")
        flag = 1
    if " very rough " in msgs:
        qtns.append(" very rough ")
        anss.append("What do you mean by very rough? Please specify. ")
        flag = 1
    if " extremely rough " in msgs:
        qtns.append(" extremely rough ")
        anss.append("What do you mean by extremely rough? Please specify. ")
        flag = 1
    if " especially rough " in msgs:
        qtns.append(" especially rough ")
        anss.append("What do you mean by especially rough? Please specify. ")
        flag = 1
    if " absolutely rough " in msgs:
        qtns.append(" absolutely rough ")
        anss.append("What do you mean by absolutely rough? Please specify. ")
        flag = 1
    if " most royal " in msgs:
        qtns.append(" most royal ")
        anss.append("What do you mean by most royal? Please specify. ")
        flag = 1
    if " least royal " in msgs:
        qtns.append(" least royal ")
        anss.append("What do you mean by least royal? Please specify. ")
        flag = 1
    if " very royal " in msgs:
        qtns.append(" very royal ")
        anss.append("What do you mean by very royal? Please specify. ")
        flag = 1
    if " extremely royal " in msgs:
        qtns.append(" extremely royal ")
        anss.append("What do you mean by extremely royal? Please specify. ")
        flag = 1
    if " especially royal " in msgs:
        qtns.append(" especially royal ")
        anss.append("What do you mean by especially royal? Please specify. ")
        flag = 1
    if " absolutely royal " in msgs:
        qtns.append(" absolutely royal ")
        anss.append("What do you mean by absolutely royal? Please specify. ")
        flag = 1
    if " most rude " in msgs:
        qtns.append(" most rude ")
        anss.append("What do you mean by most rude? Please specify. ")
        flag = 1
    if " least rude " in msgs:
        qtns.append(" least rude ")
        anss.append("What do you mean by least rude? Please specify. ")
        flag = 1
    if " very rude " in msgs:
        qtns.append(" very rude ")
        anss.append("What do you mean by very rude? Please specify. ")
        flag = 1
    if " extremely rude " in msgs:
        qtns.append(" extremely rude ")
        anss.append("What do you mean by extremely rude? Please specify. ")
        flag = 1
    if " especially rude " in msgs:
        qtns.append(" especially rude ")
        anss.append("What do you mean by especially rude? Please specify. ")
        flag = 1
    if " absolutely rude " in msgs:
        qtns.append(" absolutely rude ")
        anss.append("What do you mean by absolutely rude? Please specify. ")
        flag = 1
    if " most rusty " in msgs:
        qtns.append(" most rusty ")
        anss.append("What do you mean by most rusty? Please specify. ")
        flag = 1
    if " least rusty " in msgs:
        qtns.append(" least rusty ")
        anss.append("What do you mean by least rusty? Please specify. ")
        flag = 1
    if " very rusty " in msgs:
        qtns.append(" very rusty ")
        anss.append("What do you mean by very rusty? Please specify. ")
        flag = 1
    if " extremely rusty " in msgs:
        qtns.append(" extremely rusty ")
        anss.append("What do you mean by extremely rusty? Please specify. ")
        flag = 1
    if " especially rusty " in msgs:
        qtns.append(" especially rusty ")
        anss.append("What do you mean by especially rusty? Please specify. ")
        flag = 1
    if " absolutely rusty " in msgs:
        qtns.append(" absolutely rusty ")
        anss.append("What do you mean by absolutely rusty? Please specify. ")
        flag = 1
    if " most sad " in msgs:
        qtns.append(" most sad ")
        anss.append("What do you mean by most sad? Please specify. ")
        flag = 1
    if " least sad " in msgs:
        qtns.append(" least sad ")
        anss.append("What do you mean by least sad? Please specify. ")
        flag = 1
    if " very sad " in msgs:
        qtns.append(" very sad ")
        anss.append("What do you mean by very sad? Please specify. ")
        flag = 1
    if " extremely sad " in msgs:
        qtns.append(" extremely sad ")
        anss.append("What do you mean by extremely sad? Please specify. ")
        flag = 1
    if " especially sad " in msgs:
        qtns.append(" especially sad ")
        anss.append("What do you mean by especially sad? Please specify. ")
        flag = 1
    if " absolutely sad " in msgs:
        qtns.append(" absolutely sad ")
        anss.append("What do you mean by absolutely sad? Please specify. ")
        flag = 1
    if " most safe " in msgs:
        qtns.append(" most safe ")
        anss.append("What do you mean by most safe? Please specify. ")
        flag = 1
    if " least safe " in msgs:
        qtns.append(" least safe ")
        anss.append("What do you mean by least safe? Please specify. ")
        flag = 1
    if " very safe " in msgs:
        qtns.append(" very safe ")
        anss.append("What do you mean by very safe? Please specify. ")
        flag = 1
    if " extremely safe " in msgs:
        qtns.append(" extremely safe ")
        anss.append("What do you mean by extremely safe? Please specify. ")
        flag = 1
    if " especially safe " in msgs:
        qtns.append(" especially safe ")
        anss.append("What do you mean by especially safe? Please specify. ")
        flag = 1
    if " absolutely safe " in msgs:
        qtns.append(" absolutely safe ")
        anss.append("What do you mean by absolutely safe? Please specify. ")
        flag = 1
    if " most salty " in msgs:
        qtns.append(" most salty ")
        anss.append("What do you mean by most salty? Please specify. ")
        flag = 1
    if " least salty " in msgs:
        qtns.append(" least salty ")
        anss.append("What do you mean by least salty? Please specify. ")
        flag = 1
    if " very salty " in msgs:
        qtns.append(" very salty ")
        anss.append("What do you mean by very salty? Please specify. ")
        flag = 1
    if " extremely salty " in msgs:
        qtns.append(" extremely salty ")
        anss.append("What do you mean by extremely salty? Please specify. ")
        flag = 1
    if " especially salty " in msgs:
        qtns.append(" especially salty ")
        anss.append("What do you mean by especially salty? Please specify. ")
        flag = 1
    if " absolutely salty " in msgs:
        qtns.append(" absolutely salty ")
        anss.append("What do you mean by absolutely salty? Please specify. ")
        flag = 1
    if " most sane " in msgs:
        qtns.append(" most sane ")
        anss.append("What do you mean by most sane? Please specify. ")
        flag = 1
    if " least sane " in msgs:
        qtns.append(" least sane ")
        anss.append("What do you mean by least sane? Please specify. ")
        flag = 1
    if " very sane " in msgs:
        qtns.append(" very sane ")
        anss.append("What do you mean by very sane? Please specify. ")
        flag = 1
    if " extremely sane " in msgs:
        qtns.append(" extremely sane ")
        anss.append("What do you mean by extremely sane? Please specify. ")
        flag = 1
    if " especially sane " in msgs:
        qtns.append(" especially sane ")
        anss.append("What do you mean by especially sane? Please specify. ")
        flag = 1
    if " absolutely sane " in msgs:
        qtns.append(" absolutely sane ")
        anss.append("What do you mean by absolutely sane? Please specify. ")
        flag = 1
    if " most scary " in msgs:
        qtns.append(" most scary ")
        anss.append("What do you mean by most scary? Please specify. ")
        flag = 1
    if " least scary " in msgs:
        qtns.append(" least scary ")
        anss.append("What do you mean by least scary? Please specify. ")
        flag = 1
    if " very scary " in msgs:
        qtns.append(" very scary ")
        anss.append("What do you mean by very scary? Please specify. ")
        flag = 1
    if " extremely scary " in msgs:
        qtns.append(" extremely scary ")
        anss.append("What do you mean by extremely scary? Please specify. ")
        flag = 1
    if " especially scary " in msgs:
        qtns.append(" especially scary ")
        anss.append("What do you mean by especially scary? Please specify. ")
        flag = 1
    if " absolutely scary " in msgs:
        qtns.append(" absolutely scary ")
        anss.append("What do you mean by absolutely scary? Please specify. ")
        flag = 1
    if " most scintillating " in msgs:
        qtns.append(" most scintillating ")
        anss.append("What do you mean by most scintillating? Please specify. ")
        flag = 1
    if " least scintillating " in msgs:
        qtns.append(" least scintillating ")
        anss.append("What do you mean by least scintillating? Please specify. ")
        flag = 1
    if " very scintillating " in msgs:
        qtns.append(" very scintillating ")
        anss.append("What do you mean by very scintillating? Please specify. ")
        flag = 1
    if " extremely scintillating " in msgs:
        qtns.append(" extremely scintillating ")
        anss.append("What do you mean by extremely scintillating? Please specify. ")
        flag = 1
    if " especially scintillating " in msgs:
        qtns.append(" especially scintillating ")
        anss.append("What do you mean by especially scintillating? Please specify. ")
        flag = 1
    if " absolutely scintillating " in msgs:
        qtns.append(" absolutely scintillating ")
        anss.append("What do you mean by absolutely scintillating? Please specify. ")
        flag = 1
    if " most secretive " in msgs:
        qtns.append(" most secretive ")
        anss.append("What do you mean by most secretive? Please specify. ")
        flag = 1
    if " least secretive " in msgs:
        qtns.append(" least secretive ")
        anss.append("What do you mean by least secretive? Please specify. ")
        flag = 1
    if " very secretive " in msgs:
        qtns.append(" very secretive ")
        anss.append("What do you mean by very secretive? Please specify. ")
        flag = 1
    if " extremely secretive " in msgs:
        qtns.append(" extremely secretive ")
        anss.append("What do you mean by extremely secretive? Please specify. ")
        flag = 1
    if " especially secretive " in msgs:
        qtns.append(" especially secretive ")
        anss.append("What do you mean by especially secretive? Please specify. ")
        flag = 1
    if " absolutely secretive " in msgs:
        qtns.append(" absolutely secretive ")
        anss.append("What do you mean by absolutely secretive? Please specify. ")
        flag = 1
    if " most selfish " in msgs:
        qtns.append(" most selfish ")
        anss.append("What do you mean by most selfish? Please specify. ")
        flag = 1
    if " least selfish " in msgs:
        qtns.append(" least selfish ")
        anss.append("What do you mean by least selfish? Please specify. ")
        flag = 1
    if " very selfish " in msgs:
        qtns.append(" very selfish ")
        anss.append("What do you mean by very selfish? Please specify. ")
        flag = 1
    if " extremely selfish " in msgs:
        qtns.append(" extremely selfish ")
        anss.append("What do you mean by extremely selfish? Please specify. ")
        flag = 1
    if " especially selfish " in msgs:
        qtns.append(" especially selfish ")
        anss.append("What do you mean by especially selfish? Please specify. ")
        flag = 1
    if " absolutely selfish " in msgs:
        qtns.append(" absolutely selfish ")
        anss.append("What do you mean by absolutely selfish? Please specify. ")
        flag = 1
    if " most serious " in msgs:
        qtns.append(" most serious ")
        anss.append("What do you mean by most serious? Please specify. ")
        flag = 1
    if " least serious " in msgs:
        qtns.append(" least serious ")
        anss.append("What do you mean by least serious? Please specify. ")
        flag = 1
    if " very serious " in msgs:
        qtns.append(" very serious ")
        anss.append("What do you mean by very serious? Please specify. ")
        flag = 1
    if " extremely serious " in msgs:
        qtns.append(" extremely serious ")
        anss.append("What do you mean by extremely serious? Please specify. ")
        flag = 1
    if " especially serious " in msgs:
        qtns.append(" especially serious ")
        anss.append("What do you mean by especially serious? Please specify. ")
        flag = 1
    if " absolutely serious " in msgs:
        qtns.append(" absolutely serious ")
        anss.append("What do you mean by absolutely serious? Please specify. ")
        flag = 1
    if " most shallow " in msgs:
        qtns.append(" most shallow ")
        anss.append("What do you mean by most shallow? Please specify. ")
        flag = 1
    if " least shallow " in msgs:
        qtns.append(" least shallow ")
        anss.append("What do you mean by least shallow? Please specify. ")
        flag = 1
    if " very shallow " in msgs:
        qtns.append(" very shallow ")
        anss.append("What do you mean by very shallow? Please specify. ")
        flag = 1
    if " extremely shallow " in msgs:
        qtns.append(" extremely shallow ")
        anss.append("What do you mean by extremely shallow? Please specify. ")
        flag = 1
    if " especially shallow " in msgs:
        qtns.append(" especially shallow ")
        anss.append("What do you mean by especially shallow? Please specify. ")
        flag = 1
    if " absolutely shallow " in msgs:
        qtns.append(" absolutely shallow ")
        anss.append("What do you mean by absolutely shallow? Please specify. ")
        flag = 1
    if " most sharp " in msgs:
        qtns.append(" most sharp ")
        anss.append("What do you mean by most sharp? Please specify. ")
        flag = 1
    if " least sharp " in msgs:
        qtns.append(" least sharp ")
        anss.append("What do you mean by least sharp? Please specify. ")
        flag = 1
    if " very sharp " in msgs:
        qtns.append(" very sharp ")
        anss.append("What do you mean by very sharp? Please specify. ")
        flag = 1
    if " extremely sharp " in msgs:
        qtns.append(" extremely sharp ")
        anss.append("What do you mean by extremely sharp? Please specify. ")
        flag = 1
    if " especially sharp " in msgs:
        qtns.append(" especially sharp ")
        anss.append("What do you mean by especially sharp? Please specify. ")
        flag = 1
    if " absolutely sharp " in msgs:
        qtns.append(" absolutely sharp ")
        anss.append("What do you mean by absolutely sharp? Please specify. ")
        flag = 1
    if " most shiny " in msgs:
        qtns.append(" most shiny ")
        anss.append("What do you mean by most shiny? Please specify. ")
        flag = 1
    if " least shiny " in msgs:
        qtns.append(" least shiny ")
        anss.append("What do you mean by least shiny? Please specify. ")
        flag = 1
    if " very shiny " in msgs:
        qtns.append(" very shiny ")
        anss.append("What do you mean by very shiny? Please specify. ")
        flag = 1
    if " extremely shiny " in msgs:
        qtns.append(" extremely shiny ")
        anss.append("What do you mean by extremely shiny? Please specify. ")
        flag = 1
    if " especially shiny " in msgs:
        qtns.append(" especially shiny ")
        anss.append("What do you mean by especially shiny? Please specify. ")
        flag = 1
    if " absolutely shiny " in msgs:
        qtns.append(" absolutely shiny ")
        anss.append("What do you mean by absolutely shiny? Please specify. ")
        flag = 1
    if " most shocking " in msgs:
        qtns.append(" most shocking ")
        anss.append("What do you mean by most shocking? Please specify. ")
        flag = 1
    if " least shocking " in msgs:
        qtns.append(" least shocking ")
        anss.append("What do you mean by least shocking? Please specify. ")
        flag = 1
    if " very shocking " in msgs:
        qtns.append(" very shocking ")
        anss.append("What do you mean by very shocking? Please specify. ")
        flag = 1
    if " extremely shocking " in msgs:
        qtns.append(" extremely shocking ")
        anss.append("What do you mean by extremely shocking? Please specify. ")
        flag = 1
    if " especially shocking " in msgs:
        qtns.append(" especially shocking ")
        anss.append("What do you mean by especially shocking? Please specify. ")
        flag = 1
    if " absolutely shocking " in msgs:
        qtns.append(" absolutely shocking ")
        anss.append("What do you mean by absolutely shocking? Please specify. ")
        flag = 1
    if " most short " in msgs:
        qtns.append(" most short ")
        anss.append("What do you mean by most short? Please specify. ")
        flag = 1
    if " least short " in msgs:
        qtns.append(" least short ")
        anss.append("What do you mean by least short? Please specify. ")
        flag = 1
    if " very short " in msgs:
        qtns.append(" very short ")
        anss.append("What do you mean by very short? Please specify. ")
        flag = 1
    if " extremely short " in msgs:
        qtns.append(" extremely short ")
        anss.append("What do you mean by extremely short? Please specify. ")
        flag = 1
    if " especially short " in msgs:
        qtns.append(" especially short ")
        anss.append("What do you mean by especially short? Please specify. ")
        flag = 1
    if " absolutely short " in msgs:
        qtns.append(" absolutely short ")
        anss.append("What do you mean by absolutely short? Please specify. ")
        flag = 1
    if " most shy " in msgs:
        qtns.append(" most shy ")
        anss.append("What do you mean by most shy? Please specify. ")
        flag = 1
    if " least shy " in msgs:
        qtns.append(" least shy ")
        anss.append("What do you mean by least shy? Please specify. ")
        flag = 1
    if " very shy " in msgs:
        qtns.append(" very shy ")
        anss.append("What do you mean by very shy? Please specify. ")
        flag = 1
    if " extremely shy " in msgs:
        qtns.append(" extremely shy ")
        anss.append("What do you mean by extremely shy? Please specify. ")
        flag = 1
    if " especially shy " in msgs:
        qtns.append(" especially shy ")
        anss.append("What do you mean by especially shy? Please specify. ")
        flag = 1
    if " absolutely shy " in msgs:
        qtns.append(" absolutely shy ")
        anss.append("What do you mean by absolutely shy? Please specify. ")
        flag = 1
    if " most silly " in msgs:
        qtns.append(" most silly ")
        anss.append("What do you mean by most silly? Please specify. ")
        flag = 1
    if " least silly " in msgs:
        qtns.append(" least silly ")
        anss.append("What do you mean by least silly? Please specify. ")
        flag = 1
    if " very silly " in msgs:
        qtns.append(" very silly ")
        anss.append("What do you mean by very silly? Please specify. ")
        flag = 1
    if " extremely silly " in msgs:
        qtns.append(" extremely silly ")
        anss.append("What do you mean by extremely silly? Please specify. ")
        flag = 1
    if " especially silly " in msgs:
        qtns.append(" especially silly ")
        anss.append("What do you mean by especially silly? Please specify. ")
        flag = 1
    if " absolutely silly " in msgs:
        qtns.append(" absolutely silly ")
        anss.append("What do you mean by absolutely silly? Please specify. ")
        flag = 1
    if " most simple " in msgs:
        qtns.append(" most simple ")
        anss.append("What do you mean by most simple? Please specify. ")
        flag = 1
    if " least simple " in msgs:
        qtns.append(" least simple ")
        anss.append("What do you mean by least simple? Please specify. ")
        flag = 1
    if " very simple " in msgs:
        qtns.append(" very simple ")
        anss.append("What do you mean by very simple? Please specify. ")
        flag = 1
    if " extremely simple " in msgs:
        qtns.append(" extremely simple ")
        anss.append("What do you mean by extremely simple? Please specify. ")
        flag = 1
    if " especially simple " in msgs:
        qtns.append(" especially simple ")
        anss.append("What do you mean by especially simple? Please specify. ")
        flag = 1
    if " absolutely simple " in msgs:
        qtns.append(" absolutely simple ")
        anss.append("What do you mean by absolutely simple? Please specify. ")
        flag = 1
    if " most sincere " in msgs:
        qtns.append(" most sincere ")
        anss.append("What do you mean by most sincere? Please specify. ")
        flag = 1
    if " least sincere " in msgs:
        qtns.append(" least sincere ")
        anss.append("What do you mean by least sincere? Please specify. ")
        flag = 1
    if " very sincere " in msgs:
        qtns.append(" very sincere ")
        anss.append("What do you mean by very sincere? Please specify. ")
        flag = 1
    if " extremely sincere " in msgs:
        qtns.append(" extremely sincere ")
        anss.append("What do you mean by extremely sincere? Please specify. ")
        flag = 1
    if " especially sincere " in msgs:
        qtns.append(" especially sincere ")
        anss.append("What do you mean by especially sincere? Please specify. ")
        flag = 1
    if " absolutely sincere " in msgs:
        qtns.append(" absolutely sincere ")
        anss.append("What do you mean by absolutely sincere? Please specify. ")
        flag = 1
    if " most sincere " in msgs:
        qtns.append(" most sincere ")
        anss.append("What do you mean by most sincere? Please specify. ")
        flag = 1
    if " least sincere " in msgs:
        qtns.append(" least sincere ")
        anss.append("What do you mean by least sincere? Please specify. ")
        flag = 1
    if " very sincere " in msgs:
        qtns.append(" very sincere ")
        anss.append("What do you mean by very sincere? Please specify. ")
        flag = 1
    if " extremely sincere " in msgs:
        qtns.append(" extremely sincere ")
        anss.append("What do you mean by extremely sincere? Please specify. ")
        flag = 1
    if " especially sincere " in msgs:
        qtns.append(" especially sincere ")
        anss.append("What do you mean by especially sincere? Please specify. ")
        flag = 1
    if " absolutely sincere " in msgs:
        qtns.append(" absolutely sincere ")
        anss.append("What do you mean by absolutely sincere? Please specify. ")
        flag = 1
    if " most skinny " in msgs:
        qtns.append(" most skinny ")
        anss.append("What do you mean by most skinny? Please specify. ")
        flag = 1
    if " least skinny " in msgs:
        qtns.append(" least skinny ")
        anss.append("What do you mean by least skinny? Please specify. ")
        flag = 1
    if " very skinny " in msgs:
        qtns.append(" very skinny ")
        anss.append("What do you mean by very skinny? Please specify. ")
        flag = 1
    if " extremely skinny " in msgs:
        qtns.append(" extremely skinny ")
        anss.append("What do you mean by extremely skinny? Please specify. ")
        flag = 1
    if " especially skinny " in msgs:
        qtns.append(" especially skinny ")
        anss.append("What do you mean by especially skinny? Please specify. ")
        flag = 1
    if " absolutely skinny " in msgs:
        qtns.append(" absolutely skinny ")
        anss.append("What do you mean by absolutely skinny? Please specify. ")
        flag = 1
    if " most sleepy " in msgs:
        qtns.append(" most sleepy ")
        anss.append("What do you mean by most sleepy? Please specify. ")
        flag = 1
    if " least sleepy " in msgs:
        qtns.append(" least sleepy ")
        anss.append("What do you mean by least sleepy? Please specify. ")
        flag = 1
    if " very sleepy " in msgs:
        qtns.append(" very sleepy ")
        anss.append("What do you mean by very sleepy? Please specify. ")
        flag = 1
    if " extremely sleepy " in msgs:
        qtns.append(" extremely sleepy ")
        anss.append("What do you mean by extremely sleepy? Please specify. ")
        flag = 1
    if " especially sleepy " in msgs:
        qtns.append(" especially sleepy ")
        anss.append("What do you mean by especially sleepy? Please specify. ")
        flag = 1
    if " absolutely sleepy " in msgs:
        qtns.append(" absolutely sleepy ")
        anss.append("What do you mean by absolutely sleepy? Please specify. ")
        flag = 1
    if " most slim " in msgs:
        qtns.append(" most slim ")
        anss.append("What do you mean by most slim? Please specify. ")
        flag = 1
    if " least slim " in msgs:
        qtns.append(" least slim ")
        anss.append("What do you mean by least slim? Please specify. ")
        flag = 1
    if " very slim " in msgs:
        qtns.append(" very slim ")
        anss.append("What do you mean by very slim? Please specify. ")
        flag = 1
    if " extremely slim " in msgs:
        qtns.append(" extremely slim ")
        anss.append("What do you mean by extremely slim? Please specify. ")
        flag = 1
    if " especially slim " in msgs:
        qtns.append(" especially slim ")
        anss.append("What do you mean by especially slim? Please specify. ")
        flag = 1
    if " absolutely slim " in msgs:
        qtns.append(" absolutely slim ")
        anss.append("What do you mean by absolutely slim? Please specify. ")
        flag = 1
    if " most slimy " in msgs:
        qtns.append(" most slimy ")
        anss.append("What do you mean by most slimy? Please specify. ")
        flag = 1
    if " least slimy " in msgs:
        qtns.append(" least slimy ")
        anss.append("What do you mean by least slimy? Please specify. ")
        flag = 1
    if " very slimy " in msgs:
        qtns.append(" very slimy ")
        anss.append("What do you mean by very slimy? Please specify. ")
        flag = 1
    if " extremely slimy " in msgs:
        qtns.append(" extremely slimy ")
        anss.append("What do you mean by extremely slimy? Please specify. ")
        flag = 1
    if " especially slimy " in msgs:
        qtns.append(" especially slimy ")
        anss.append("What do you mean by especially slimy? Please specify. ")
        flag = 1
    if " absolutely slimy " in msgs:
        qtns.append(" absolutely slimy ")
        anss.append("What do you mean by absolutely slimy? Please specify. ")
        flag = 1
    if " most slow " in msgs:
        qtns.append(" most slow ")
        anss.append("What do you mean by most slow? Please specify. ")
        flag = 1
    if " least slow " in msgs:
        qtns.append(" least slow ")
        anss.append("What do you mean by least slow? Please specify. ")
        flag = 1
    if " very slow " in msgs:
        qtns.append(" very slow ")
        anss.append("What do you mean by very slow? Please specify. ")
        flag = 1
    if " extremely slow " in msgs:
        qtns.append(" extremely slow ")
        anss.append("What do you mean by extremely slow? Please specify. ")
        flag = 1
    if " especially slow " in msgs:
        qtns.append(" especially slow ")
        anss.append("What do you mean by especially slow? Please specify. ")
        flag = 1
    if " absolutely slow " in msgs:
        qtns.append(" absolutely slow ")
        anss.append("What do you mean by absolutely slow? Please specify. ")
        flag = 1
    if " most small " in msgs:
        qtns.append(" most small ")
        anss.append("What do you mean by most small? Please specify. ")
        flag = 1
    if " least small " in msgs:
        qtns.append(" least small ")
        anss.append("What do you mean by least small? Please specify. ")
        flag = 1
    if " very small " in msgs:
        qtns.append(" very small ")
        anss.append("What do you mean by very small? Please specify. ")
        flag = 1
    if " extremely small " in msgs:
        qtns.append(" extremely small ")
        anss.append("What do you mean by extremely small? Please specify. ")
        flag = 1
    if " especially small " in msgs:
        qtns.append(" especially small ")
        anss.append("What do you mean by especially small? Please specify. ")
        flag = 1
    if " absolutely small " in msgs:
        qtns.append(" absolutely small ")
        anss.append("What do you mean by absolutely small? Please specify. ")
        flag = 1
    if " most smart " in msgs:
        qtns.append(" most smart ")
        anss.append("What do you mean by most smart? Please specify. ")
        flag = 1
    if " least smart " in msgs:
        qtns.append(" least smart ")
        anss.append("What do you mean by least smart? Please specify. ")
        flag = 1
    if " very smart " in msgs:
        qtns.append(" very smart ")
        anss.append("What do you mean by very smart? Please specify. ")
        flag = 1
    if " extremely smart " in msgs:
        qtns.append(" extremely smart ")
        anss.append("What do you mean by extremely smart? Please specify. ")
        flag = 1
    if " especially smart " in msgs:
        qtns.append(" especially smart ")
        anss.append("What do you mean by especially smart? Please specify. ")
        flag = 1
    if " absolutely smart " in msgs:
        qtns.append(" absolutely smart ")
        anss.append("What do you mean by absolutely smart? Please specify. ")
        flag = 1
    if " most smelly " in msgs:
        qtns.append(" most smelly ")
        anss.append("What do you mean by most smelly? Please specify. ")
        flag = 1
    if " least smelly " in msgs:
        qtns.append(" least smelly ")
        anss.append("What do you mean by least smelly? Please specify. ")
        flag = 1
    if " very smelly " in msgs:
        qtns.append(" very smelly ")
        anss.append("What do you mean by very smelly? Please specify. ")
        flag = 1
    if " extremely smelly " in msgs:
        qtns.append(" extremely smelly ")
        anss.append("What do you mean by extremely smelly? Please specify. ")
        flag = 1
    if " especially smelly " in msgs:
        qtns.append(" especially smelly ")
        anss.append("What do you mean by especially smelly? Please specify. ")
        flag = 1
    if " absolutely smelly " in msgs:
        qtns.append(" absolutely smelly ")
        anss.append("What do you mean by absolutely smelly? Please specify. ")
        flag = 1
    if " most smoky " in msgs:
        qtns.append(" most smoky ")
        anss.append("What do you mean by most smoky? Please specify. ")
        flag = 1
    if " least smoky " in msgs:
        qtns.append(" least smoky ")
        anss.append("What do you mean by least smoky? Please specify. ")
        flag = 1
    if " very smoky " in msgs:
        qtns.append(" very smoky ")
        anss.append("What do you mean by very smoky? Please specify. ")
        flag = 1
    if " extremely smoky " in msgs:
        qtns.append(" extremely smoky ")
        anss.append("What do you mean by extremely smoky? Please specify. ")
        flag = 1
    if " especially smoky " in msgs:
        qtns.append(" especially smoky ")
        anss.append("What do you mean by especially smoky? Please specify. ")
        flag = 1
    if " absolutely smoky " in msgs:
        qtns.append(" absolutely smoky ")
        anss.append("What do you mean by absolutely smoky? Please specify. ")
        flag = 1
    if " most smooth " in msgs:
        qtns.append(" most smooth ")
        anss.append("What do you mean by most smooth? Please specify. ")
        flag = 1
    if " least smooth " in msgs:
        qtns.append(" least smooth ")
        anss.append("What do you mean by least smooth? Please specify. ")
        flag = 1
    if " very smooth " in msgs:
        qtns.append(" very smooth ")
        anss.append("What do you mean by very smooth? Please specify. ")
        flag = 1
    if " extremely smooth " in msgs:
        qtns.append(" extremely smooth ")
        anss.append("What do you mean by extremely smooth? Please specify. ")
        flag = 1
    if " especially smooth " in msgs:
        qtns.append(" especially smooth ")
        anss.append("What do you mean by especially smooth? Please specify. ")
        flag = 1
    if " absolutely smooth " in msgs:
        qtns.append(" absolutely smooth ")
        anss.append("What do you mean by absolutely smooth? Please specify. ")
        flag = 1
    if " most soft " in msgs:
        qtns.append(" most soft ")
        anss.append("What do you mean by most soft? Please specify. ")
        flag = 1
    if " least soft " in msgs:
        qtns.append(" least soft ")
        anss.append("What do you mean by least soft? Please specify. ")
        flag = 1
    if " very soft " in msgs:
        qtns.append(" very soft ")
        anss.append("What do you mean by very soft? Please specify. ")
        flag = 1
    if " extremely soft " in msgs:
        qtns.append(" extremely soft ")
        anss.append("What do you mean by extremely soft? Please specify. ")
        flag = 1
    if " especially soft " in msgs:
        qtns.append(" especially soft ")
        anss.append("What do you mean by especially soft? Please specify. ")
        flag = 1
    if " absolutely soft " in msgs:
        qtns.append(" absolutely soft ")
        anss.append("What do you mean by absolutely soft? Please specify. ")
        flag = 1
    if " most soon " in msgs:
        qtns.append(" most soon ")
        anss.append("What do you mean by most soon? Please specify. ")
        flag = 1
    if " least soon " in msgs:
        qtns.append(" least soon ")
        anss.append("What do you mean by least soon? Please specify. ")
        flag = 1
    if " very soon " in msgs:
        qtns.append(" very soon ")
        anss.append("What do you mean by very soon? Please specify. ")
        flag = 1
    if " extremely soon " in msgs:
        qtns.append(" extremely soon ")
        anss.append("What do you mean by extremely soon? Please specify. ")
        flag = 1
    if " especially soon " in msgs:
        qtns.append(" especially soon ")
        anss.append("What do you mean by especially soon? Please specify. ")
        flag = 1
    if " absolutely soon " in msgs:
        qtns.append(" absolutely soon ")
        anss.append("What do you mean by absolutely soon? Please specify. ")
        flag = 1
    if " most sore " in msgs:
        qtns.append(" most sore ")
        anss.append("What do you mean by most sore? Please specify. ")
        flag = 1
    if " least sore " in msgs:
        qtns.append(" least sore ")
        anss.append("What do you mean by least sore? Please specify. ")
        flag = 1
    if " very sore " in msgs:
        qtns.append(" very sore ")
        anss.append("What do you mean by very sore? Please specify. ")
        flag = 1
    if " extremely sore " in msgs:
        qtns.append(" extremely sore ")
        anss.append("What do you mean by extremely sore? Please specify. ")
        flag = 1
    if " especially sore " in msgs:
        qtns.append(" especially sore ")
        anss.append("What do you mean by especially sore? Please specify. ")
        flag = 1
    if " absolutely sore " in msgs:
        qtns.append(" absolutely sore ")
        anss.append("What do you mean by absolutely sore? Please specify. ")
        flag = 1
    if " most sorry " in msgs:
        qtns.append(" most sorry ")
        anss.append("What do you mean by most sorry? Please specify. ")
        flag = 1
    if " least sorry " in msgs:
        qtns.append(" least sorry ")
        anss.append("What do you mean by least sorry? Please specify. ")
        flag = 1
    if " very sorry " in msgs:
        qtns.append(" very sorry ")
        anss.append("What do you mean by very sorry? Please specify. ")
        flag = 1
    if " extremely sorry " in msgs:
        qtns.append(" extremely sorry ")
        anss.append("What do you mean by extremely sorry? Please specify. ")
        flag = 1
    if " especially sorry " in msgs:
        qtns.append(" especially sorry ")
        anss.append("What do you mean by especially sorry? Please specify. ")
        flag = 1
    if " absolutely sorry " in msgs:
        qtns.append(" absolutely sorry ")
        anss.append("What do you mean by absolutely sorry? Please specify. ")
        flag = 1
    if " most sour " in msgs:
        qtns.append(" most sour ")
        anss.append("What do you mean by most sour? Please specify. ")
        flag = 1
    if " least sour " in msgs:
        qtns.append(" least sour ")
        anss.append("What do you mean by least sour? Please specify. ")
        flag = 1
    if " very sour " in msgs:
        qtns.append(" very sour ")
        anss.append("What do you mean by very sour? Please specify. ")
        flag = 1
    if " extremely sour " in msgs:
        qtns.append(" extremely sour ")
        anss.append("What do you mean by extremely sour? Please specify. ")
        flag = 1
    if " especially sour " in msgs:
        qtns.append(" especially sour ")
        anss.append("What do you mean by especially sour? Please specify. ")
        flag = 1
    if " absolutely sour " in msgs:
        qtns.append(" absolutely sour ")
        anss.append("What do you mean by absolutely sour? Please specify. ")
        flag = 1
    if " most spicy " in msgs:
        qtns.append(" most spicy ")
        anss.append("What do you mean by most spicy? Please specify. ")
        flag = 1
    if " least spicy " in msgs:
        qtns.append(" least spicy ")
        anss.append("What do you mean by least spicy? Please specify. ")
        flag = 1
    if " very spicy " in msgs:
        qtns.append(" very spicy ")
        anss.append("What do you mean by very spicy? Please specify. ")
        flag = 1
    if " extremely spicy " in msgs:
        qtns.append(" extremely spicy ")
        anss.append("What do you mean by extremely spicy? Please specify. ")
        flag = 1
    if " especially spicy " in msgs:
        qtns.append(" especially spicy ")
        anss.append("What do you mean by especially spicy? Please specify. ")
        flag = 1
    if " absolutely spicy " in msgs:
        qtns.append(" absolutely spicy ")
        anss.append("What do you mean by absolutely spicy? Please specify. ")
        flag = 1
    if " most spiritual " in msgs:
        qtns.append(" most spiritual ")
        anss.append("What do you mean by most spiritual? Please specify. ")
        flag = 1
    if " least spiritual " in msgs:
        qtns.append(" least spiritual ")
        anss.append("What do you mean by least spiritual? Please specify. ")
        flag = 1
    if " very spiritual " in msgs:
        qtns.append(" very spiritual ")
        anss.append("What do you mean by very spiritual? Please specify. ")
        flag = 1
    if " extremely spiritual " in msgs:
        qtns.append(" extremely spiritual ")
        anss.append("What do you mean by extremely spiritual? Please specify. ")
        flag = 1
    if " especially spiritual " in msgs:
        qtns.append(" especially spiritual ")
        anss.append("What do you mean by especially spiritual? Please specify. ")
        flag = 1
    if " absolutely spiritual " in msgs:
        qtns.append(" absolutely spiritual ")
        anss.append("What do you mean by absolutely spiritual? Please specify. ")
        flag = 1
    if " most splendid " in msgs:
        qtns.append(" most splendid ")
        anss.append("What do you mean by most splendid? Please specify. ")
        flag = 1
    if " least splendid " in msgs:
        qtns.append(" least splendid ")
        anss.append("What do you mean by least splendid? Please specify. ")
        flag = 1
    if " very splendid " in msgs:
        qtns.append(" very splendid ")
        anss.append("What do you mean by very splendid? Please specify. ")
        flag = 1
    if " extremely splendid " in msgs:
        qtns.append(" extremely splendid ")
        anss.append("What do you mean by extremely splendid? Please specify. ")
        flag = 1
    if " especially splendid " in msgs:
        qtns.append(" especially splendid ")
        anss.append("What do you mean by especially splendid? Please specify. ")
        flag = 1
    if " absolutely splendid " in msgs:
        qtns.append(" absolutely splendid ")
        anss.append("What do you mean by absolutely splendid? Please specify. ")
        flag = 1
    if " most steep " in msgs:
        qtns.append(" most steep ")
        anss.append("What do you mean by most steep? Please specify. ")
        flag = 1
    if " least steep " in msgs:
        qtns.append(" least steep ")
        anss.append("What do you mean by least steep? Please specify. ")
        flag = 1
    if " very steep " in msgs:
        qtns.append(" very steep ")
        anss.append("What do you mean by very steep? Please specify. ")
        flag = 1
    if " extremely steep " in msgs:
        qtns.append(" extremely steep ")
        anss.append("What do you mean by extremely steep? Please specify. ")
        flag = 1
    if " especially steep " in msgs:
        qtns.append(" especially steep ")
        anss.append("What do you mean by especially steep? Please specify. ")
        flag = 1
    if " absolutely steep " in msgs:
        qtns.append(" absolutely steep ")
        anss.append("What do you mean by absolutely steep? Please specify. ")
        flag = 1
    if " most stingy " in msgs:
        qtns.append(" most stingy ")
        anss.append("What do you mean by most stingy? Please specify. ")
        flag = 1
    if " least stingy " in msgs:
        qtns.append(" least stingy ")
        anss.append("What do you mean by least stingy? Please specify. ")
        flag = 1
    if " very stingy " in msgs:
        qtns.append(" very stingy ")
        anss.append("What do you mean by very stingy? Please specify. ")
        flag = 1
    if " extremely stingy " in msgs:
        qtns.append(" extremely stingy ")
        anss.append("What do you mean by extremely stingy? Please specify. ")
        flag = 1
    if " especially stingy " in msgs:
        qtns.append(" especially stingy ")
        anss.append("What do you mean by especially stingy? Please specify. ")
        flag = 1
    if " absolutely stingy " in msgs:
        qtns.append(" absolutely stingy ")
        anss.append("What do you mean by absolutely stingy? Please specify. ")
        flag = 1
    if " most strange " in msgs:
        qtns.append(" most strange ")
        anss.append("What do you mean by most strange? Please specify. ")
        flag = 1
    if " least strange " in msgs:
        qtns.append(" least strange ")
        anss.append("What do you mean by least strange? Please specify. ")
        flag = 1
    if " very strange " in msgs:
        qtns.append(" very strange ")
        anss.append("What do you mean by very strange? Please specify. ")
        flag = 1
    if " extremely strange " in msgs:
        qtns.append(" extremely strange ")
        anss.append("What do you mean by extremely strange? Please specify. ")
        flag = 1
    if " especially strange " in msgs:
        qtns.append(" especially strange ")
        anss.append("What do you mean by especially strange? Please specify. ")
        flag = 1
    if " absolutely strange " in msgs:
        qtns.append(" absolutely strange ")
        anss.append("What do you mean by absolutely strange? Please specify. ")
        flag = 1
    if " most strict " in msgs:
        qtns.append(" most strict ")
        anss.append("What do you mean by most strict? Please specify. ")
        flag = 1
    if " least strict " in msgs:
        qtns.append(" least strict ")
        anss.append("What do you mean by least strict? Please specify. ")
        flag = 1
    if " very strict " in msgs:
        qtns.append(" very strict ")
        anss.append("What do you mean by very strict? Please specify. ")
        flag = 1
    if " extremely strict " in msgs:
        qtns.append(" extremely strict ")
        anss.append("What do you mean by extremely strict? Please specify. ")
        flag = 1
    if " especially strict " in msgs:
        qtns.append(" especially strict ")
        anss.append("What do you mean by especially strict? Please specify. ")
        flag = 1
    if " absolutely strict " in msgs:
        qtns.append(" absolutely strict ")
        anss.append("What do you mean by absolutely strict? Please specify. ")
        flag = 1
    if " most strong " in msgs:
        qtns.append(" most strong ")
        anss.append("What do you mean by most strong? Please specify. ")
        flag = 1
    if " least strong " in msgs:
        qtns.append(" least strong ")
        anss.append("What do you mean by least strong? Please specify. ")
        flag = 1
    if " very strong " in msgs:
        qtns.append(" very strong ")
        anss.append("What do you mean by very strong? Please specify. ")
        flag = 1
    if " extremely strong " in msgs:
        qtns.append(" extremely strong ")
        anss.append("What do you mean by extremely strong? Please specify. ")
        flag = 1
    if " especially strong " in msgs:
        qtns.append(" especially strong ")
        anss.append("What do you mean by especially strong? Please specify. ")
        flag = 1
    if " absolutely strong " in msgs:
        qtns.append(" absolutely strong ")
        anss.append("What do you mean by absolutely strong? Please specify. ")
        flag = 1
    if " most successful " in msgs:
        qtns.append(" most successful ")
        anss.append("What do you mean by most successful? Please specify. ")
        flag = 1
    if " least successful " in msgs:
        qtns.append(" least successful ")
        anss.append("What do you mean by least successful? Please specify. ")
        flag = 1
    if " very successful " in msgs:
        qtns.append(" very successful ")
        anss.append("What do you mean by very successful? Please specify. ")
        flag = 1
    if " extremely successful " in msgs:
        qtns.append(" extremely successful ")
        anss.append("What do you mean by extremely successful? Please specify. ")
        flag = 1
    if " especially successful " in msgs:
        qtns.append(" especially successful ")
        anss.append("What do you mean by especially successful? Please specify. ")
        flag = 1
    if " absolutely successful " in msgs:
        qtns.append(" absolutely successful ")
        anss.append("What do you mean by absolutely successful? Please specify. ")
        flag = 1
    if " most sunny " in msgs:
        qtns.append(" most sunny ")
        anss.append("What do you mean by most sunny? Please specify. ")
        flag = 1
    if " least sunny " in msgs:
        qtns.append(" least sunny ")
        anss.append("What do you mean by least sunny? Please specify. ")
        flag = 1
    if " very sunny " in msgs:
        qtns.append(" very sunny ")
        anss.append("What do you mean by very sunny? Please specify. ")
        flag = 1
    if " extremely sunny " in msgs:
        qtns.append(" extremely sunny ")
        anss.append("What do you mean by extremely sunny? Please specify. ")
        flag = 1
    if " especially sunny " in msgs:
        qtns.append(" especially sunny ")
        anss.append("What do you mean by especially sunny? Please specify. ")
        flag = 1
    if " absolutely sunny " in msgs:
        qtns.append(" absolutely sunny ")
        anss.append("What do you mean by absolutely sunny? Please specify. ")
        flag = 1
    if " most sweaty " in msgs:
        qtns.append(" most sweaty ")
        anss.append("What do you mean by most sweaty? Please specify. ")
        flag = 1
    if " least sweaty " in msgs:
        qtns.append(" least sweaty ")
        anss.append("What do you mean by least sweaty? Please specify. ")
        flag = 1
    if " very sweaty " in msgs:
        qtns.append(" very sweaty ")
        anss.append("What do you mean by very sweaty? Please specify. ")
        flag = 1
    if " extremely sweaty " in msgs:
        qtns.append(" extremely sweaty ")
        anss.append("What do you mean by extremely sweaty? Please specify. ")
        flag = 1
    if " especially sweaty " in msgs:
        qtns.append(" especially sweaty ")
        anss.append("What do you mean by especially sweaty? Please specify. ")
        flag = 1
    if " absolutely sweaty " in msgs:
        qtns.append(" absolutely sweaty ")
        anss.append("What do you mean by absolutely sweaty? Please specify. ")
        flag = 1
    if " most sweet " in msgs:
        qtns.append(" most sweet ")
        anss.append("What do you mean by most sweet? Please specify. ")
        flag = 1
    if " least sweet " in msgs:
        qtns.append(" least sweet ")
        anss.append("What do you mean by least sweet? Please specify. ")
        flag = 1
    if " very sweet " in msgs:
        qtns.append(" very sweet ")
        anss.append("What do you mean by very sweet? Please specify. ")
        flag = 1
    if " extremely sweet " in msgs:
        qtns.append(" extremely sweet ")
        anss.append("What do you mean by extremely sweet? Please specify. ")
        flag = 1
    if " especially sweet " in msgs:
        qtns.append(" especially sweet ")
        anss.append("What do you mean by especially sweet? Please specify. ")
        flag = 1
    if " absolutely sweet " in msgs:
        qtns.append(" absolutely sweet ")
        anss.append("What do you mean by absolutely sweet? Please specify. ")
        flag = 1
    if " most tactful " in msgs:
        qtns.append(" most tactful ")
        anss.append("What do you mean by most tactful? Please specify. ")
        flag = 1
    if " least tactful " in msgs:
        qtns.append(" least tactful ")
        anss.append("What do you mean by least tactful? Please specify. ")
        flag = 1
    if " very tactful " in msgs:
        qtns.append(" very tactful ")
        anss.append("What do you mean by very tactful? Please specify. ")
        flag = 1
    if " extremely tactful " in msgs:
        qtns.append(" extremely tactful ")
        anss.append("What do you mean by extremely tactful? Please specify. ")
        flag = 1
    if " especially tactful " in msgs:
        qtns.append(" especially tactful ")
        anss.append("What do you mean by especially tactful? Please specify. ")
        flag = 1
    if " absolutely tactful " in msgs:
        qtns.append(" absolutely tactful ")
        anss.append("What do you mean by absolutely tactful? Please specify. ")
        flag = 1
    if " most tailor-made " in msgs:
        qtns.append(" most tailor-made ")
        anss.append("What do you mean by most tailor-made? Please specify. ")
        flag = 1
    if " least tailor-made " in msgs:
        qtns.append(" least tailor-made ")
        anss.append("What do you mean by least tailor-made? Please specify. ")
        flag = 1
    if " very tailor-made " in msgs:
        qtns.append(" very tailor-made ")
        anss.append("What do you mean by very tailor-made? Please specify. ")
        flag = 1
    if " extremely tailor-made " in msgs:
        qtns.append(" extremely tailor-made ")
        anss.append("What do you mean by extremely tailor-made? Please specify. ")
        flag = 1
    if " especially tailor-made " in msgs:
        qtns.append(" especially tailor-made ")
        anss.append("What do you mean by especially tailor-made? Please specify. ")
        flag = 1
    if " absolutely tailor-made " in msgs:
        qtns.append(" absolutely tailor-made ")
        anss.append("What do you mean by absolutely tailor-made? Please specify. ")
        flag = 1
    if " most take-charge " in msgs:
        qtns.append(" most take-charge ")
        anss.append("What do you mean by most take-charge? Please specify. ")
        flag = 1
    if " least take-charge " in msgs:
        qtns.append(" least take-charge ")
        anss.append("What do you mean by least take-charge? Please specify. ")
        flag = 1
    if " very take-charge " in msgs:
        qtns.append(" very take-charge ")
        anss.append("What do you mean by very take-charge? Please specify. ")
        flag = 1
    if " extremely take-charge " in msgs:
        qtns.append(" extremely take-charge ")
        anss.append("What do you mean by extremely take-charge? Please specify. ")
        flag = 1
    if " especially take-charge " in msgs:
        qtns.append(" especially take-charge ")
        anss.append("What do you mean by especially take-charge? Please specify. ")
        flag = 1
    if " absolutely take-charge " in msgs:
        qtns.append(" absolutely take-charge ")
        anss.append("What do you mean by absolutely take-charge? Please specify. ")
        flag = 1
    if " most talented " in msgs:
        qtns.append(" most talented ")
        anss.append("What do you mean by most talented? Please specify. ")
        flag = 1
    if " least talented " in msgs:
        qtns.append(" least talented ")
        anss.append("What do you mean by least talented? Please specify. ")
        flag = 1
    if " very talented " in msgs:
        qtns.append(" very talented ")
        anss.append("What do you mean by very talented? Please specify. ")
        flag = 1
    if " extremely talented " in msgs:
        qtns.append(" extremely talented ")
        anss.append("What do you mean by extremely talented? Please specify. ")
        flag = 1
    if " especially talented " in msgs:
        qtns.append(" especially talented ")
        anss.append("What do you mean by especially talented? Please specify. ")
        flag = 1
    if " absolutely talented " in msgs:
        qtns.append(" absolutely talented ")
        anss.append("What do you mean by absolutely talented? Please specify. ")
        flag = 1
    if " most tall " in msgs:
        qtns.append(" most tall ")
        anss.append("What do you mean by most tall? Please specify. ")
        flag = 1
    if " least tall " in msgs:
        qtns.append(" least tall ")
        anss.append("What do you mean by least tall? Please specify. ")
        flag = 1
    if " very tall " in msgs:
        qtns.append(" very tall ")
        anss.append("What do you mean by very tall? Please specify. ")
        flag = 1
    if " extremely tall " in msgs:
        qtns.append(" extremely tall ")
        anss.append("What do you mean by extremely tall? Please specify. ")
        flag = 1
    if " especially tall " in msgs:
        qtns.append(" especially tall ")
        anss.append("What do you mean by especially tall? Please specify. ")
        flag = 1
    if " absolutely tall " in msgs:
        qtns.append(" absolutely tall ")
        anss.append("What do you mean by absolutely tall? Please specify. ")
        flag = 1
    if " most tan " in msgs:
        qtns.append(" most tan ")
        anss.append("What do you mean by most tan? Please specify. ")
        flag = 1
    if " least tan " in msgs:
        qtns.append(" least tan ")
        anss.append("What do you mean by least tan? Please specify. ")
        flag = 1
    if " very tan " in msgs:
        qtns.append(" very tan ")
        anss.append("What do you mean by very tan? Please specify. ")
        flag = 1
    if " extremely tan " in msgs:
        qtns.append(" extremely tan ")
        anss.append("What do you mean by extremely tan? Please specify. ")
        flag = 1
    if " especially tan " in msgs:
        qtns.append(" especially tan ")
        anss.append("What do you mean by especially tan? Please specify. ")
        flag = 1
    if " absolutely tan " in msgs:
        qtns.append(" absolutely tan ")
        anss.append("What do you mean by absolutely tan? Please specify. ")
        flag = 1
    if " most tangible " in msgs:
        qtns.append(" most tangible ")
        anss.append("What do you mean by most tangible? Please specify. ")
        flag = 1
    if " least tangible " in msgs:
        qtns.append(" least tangible ")
        anss.append("What do you mean by least tangible? Please specify. ")
        flag = 1
    if " very tangible " in msgs:
        qtns.append(" very tangible ")
        anss.append("What do you mean by very tangible? Please specify. ")
        flag = 1
    if " extremely tangible " in msgs:
        qtns.append(" extremely tangible ")
        anss.append("What do you mean by extremely tangible? Please specify. ")
        flag = 1
    if " especially tangible " in msgs:
        qtns.append(" especially tangible ")
        anss.append("What do you mean by especially tangible? Please specify. ")
        flag = 1
    if " absolutely tangible " in msgs:
        qtns.append(" absolutely tangible ")
        anss.append("What do you mean by absolutely tangible? Please specify. ")
        flag = 1
    if " most tasteful " in msgs:
        qtns.append(" most tasteful ")
        anss.append("What do you mean by most tasteful? Please specify. ")
        flag = 1
    if " least tasteful " in msgs:
        qtns.append(" least tasteful ")
        anss.append("What do you mean by least tasteful? Please specify. ")
        flag = 1
    if " very tasteful " in msgs:
        qtns.append(" very tasteful ")
        anss.append("What do you mean by very tasteful? Please specify. ")
        flag = 1
    if " extremely tasteful " in msgs:
        qtns.append(" extremely tasteful ")
        anss.append("What do you mean by extremely tasteful? Please specify. ")
        flag = 1
    if " especially tasteful " in msgs:
        qtns.append(" especially tasteful ")
        anss.append("What do you mean by especially tasteful? Please specify. ")
        flag = 1
    if " absolutely tasteful " in msgs:
        qtns.append(" absolutely tasteful ")
        anss.append("What do you mean by absolutely tasteful? Please specify. ")
        flag = 1
    if " most tasty " in msgs:
        qtns.append(" most tasty ")
        anss.append("What do you mean by most tasty? Please specify. ")
        flag = 1
    if " least tasty " in msgs:
        qtns.append(" least tasty ")
        anss.append("What do you mean by least tasty? Please specify. ")
        flag = 1
    if " very tasty " in msgs:
        qtns.append(" very tasty ")
        anss.append("What do you mean by very tasty? Please specify. ")
        flag = 1
    if " extremely tasty " in msgs:
        qtns.append(" extremely tasty ")
        anss.append("What do you mean by extremely tasty? Please specify. ")
        flag = 1
    if " especially tasty " in msgs:
        qtns.append(" especially tasty ")
        anss.append("What do you mean by especially tasty? Please specify. ")
        flag = 1
    if " absolutely tasty " in msgs:
        qtns.append(" absolutely tasty ")
        anss.append("What do you mean by absolutely tasty? Please specify. ")
        flag = 1
    if " most tasty " in msgs:
        qtns.append(" most tasty ")
        anss.append("What do you mean by most tasty? Please specify. ")
        flag = 1
    if " least tasty " in msgs:
        qtns.append(" least tasty ")
        anss.append("What do you mean by least tasty? Please specify. ")
        flag = 1
    if " very tasty " in msgs:
        qtns.append(" very tasty ")
        anss.append("What do you mean by very tasty? Please specify. ")
        flag = 1
    if " extremely tasty " in msgs:
        qtns.append(" extremely tasty ")
        anss.append("What do you mean by extremely tasty? Please specify. ")
        flag = 1
    if " especially tasty " in msgs:
        qtns.append(" especially tasty ")
        anss.append("What do you mean by especially tasty? Please specify. ")
        flag = 1
    if " absolutely tasty " in msgs:
        qtns.append(" absolutely tasty ")
        anss.append("What do you mean by absolutely tasty? Please specify. ")
        flag = 1
    if " most teachable " in msgs:
        qtns.append(" most teachable ")
        anss.append("What do you mean by most teachable? Please specify. ")
        flag = 1
    if " least teachable " in msgs:
        qtns.append(" least teachable ")
        anss.append("What do you mean by least teachable? Please specify. ")
        flag = 1
    if " very teachable " in msgs:
        qtns.append(" very teachable ")
        anss.append("What do you mean by very teachable? Please specify. ")
        flag = 1
    if " extremely teachable " in msgs:
        qtns.append(" extremely teachable ")
        anss.append("What do you mean by extremely teachable? Please specify. ")
        flag = 1
    if " especially teachable " in msgs:
        qtns.append(" especially teachable ")
        anss.append("What do you mean by especially teachable? Please specify. ")
        flag = 1
    if " absolutely teachable " in msgs:
        qtns.append(" absolutely teachable ")
        anss.append("What do you mean by absolutely teachable? Please specify. ")
        flag = 1
    if " most teeming " in msgs:
        qtns.append(" most teeming ")
        anss.append("What do you mean by most teeming? Please specify. ")
        flag = 1
    if " least teeming " in msgs:
        qtns.append(" least teeming ")
        anss.append("What do you mean by least teeming? Please specify. ")
        flag = 1
    if " very teeming " in msgs:
        qtns.append(" very teeming ")
        anss.append("What do you mean by very teeming? Please specify. ")
        flag = 1
    if " extremely teeming " in msgs:
        qtns.append(" extremely teeming ")
        anss.append("What do you mean by extremely teeming? Please specify. ")
        flag = 1
    if " especially teeming " in msgs:
        qtns.append(" especially teeming ")
        anss.append("What do you mean by especially teeming? Please specify. ")
        flag = 1
    if " absolutely teeming " in msgs:
        qtns.append(" absolutely teeming ")
        anss.append("What do you mean by absolutely teeming? Please specify. ")
        flag = 1
    if " most tempean " in msgs:
        qtns.append(" most tempean ")
        anss.append("What do you mean by most tempean? Please specify. ")
        flag = 1
    if " least tempean " in msgs:
        qtns.append(" least tempean ")
        anss.append("What do you mean by least tempean? Please specify. ")
        flag = 1
    if " very tempean " in msgs:
        qtns.append(" very tempean ")
        anss.append("What do you mean by very tempean? Please specify. ")
        flag = 1
    if " extremely tempean " in msgs:
        qtns.append(" extremely tempean ")
        anss.append("What do you mean by extremely tempean? Please specify. ")
        flag = 1
    if " especially tempean " in msgs:
        qtns.append(" especially tempean ")
        anss.append("What do you mean by especially tempean? Please specify. ")
        flag = 1
    if " absolutely tempean " in msgs:
        qtns.append(" absolutely tempean ")
        anss.append("What do you mean by absolutely tempean? Please specify. ")
        flag = 1
    if " most temperate " in msgs:
        qtns.append(" most temperate ")
        anss.append("What do you mean by most temperate? Please specify. ")
        flag = 1
    if " least temperate " in msgs:
        qtns.append(" least temperate ")
        anss.append("What do you mean by least temperate? Please specify. ")
        flag = 1
    if " very temperate " in msgs:
        qtns.append(" very temperate ")
        anss.append("What do you mean by very temperate? Please specify. ")
        flag = 1
    if " extremely temperate " in msgs:
        qtns.append(" extremely temperate ")
        anss.append("What do you mean by extremely temperate? Please specify. ")
        flag = 1
    if " especially temperate " in msgs:
        qtns.append(" especially temperate ")
        anss.append("What do you mean by especially temperate? Please specify. ")
        flag = 1
    if " absolutely temperate " in msgs:
        qtns.append(" absolutely temperate ")
        anss.append("What do you mean by absolutely temperate? Please specify. ")
        flag = 1
    if " most tenable " in msgs:
        qtns.append(" most tenable ")
        anss.append("What do you mean by most tenable? Please specify. ")
        flag = 1
    if " least tenable " in msgs:
        qtns.append(" least tenable ")
        anss.append("What do you mean by least tenable? Please specify. ")
        flag = 1
    if " very tenable " in msgs:
        qtns.append(" very tenable ")
        anss.append("What do you mean by very tenable? Please specify. ")
        flag = 1
    if " extremely tenable " in msgs:
        qtns.append(" extremely tenable ")
        anss.append("What do you mean by extremely tenable? Please specify. ")
        flag = 1
    if " especially tenable " in msgs:
        qtns.append(" especially tenable ")
        anss.append("What do you mean by especially tenable? Please specify. ")
        flag = 1
    if " absolutely tenable " in msgs:
        qtns.append(" absolutely tenable ")
        anss.append("What do you mean by absolutely tenable? Please specify. ")
        flag = 1
    if " most tenacious " in msgs:
        qtns.append(" most tenacious ")
        anss.append("What do you mean by most tenacious? Please specify. ")
        flag = 1
    if " least tenacious " in msgs:
        qtns.append(" least tenacious ")
        anss.append("What do you mean by least tenacious? Please specify. ")
        flag = 1
    if " very tenacious " in msgs:
        qtns.append(" very tenacious ")
        anss.append("What do you mean by very tenacious? Please specify. ")
        flag = 1
    if " extremely tenacious " in msgs:
        qtns.append(" extremely tenacious ")
        anss.append("What do you mean by extremely tenacious? Please specify. ")
        flag = 1
    if " especially tenacious " in msgs:
        qtns.append(" especially tenacious ")
        anss.append("What do you mean by especially tenacious? Please specify. ")
        flag = 1
    if " absolutely tenacious " in msgs:
        qtns.append(" absolutely tenacious ")
        anss.append("What do you mean by absolutely tenacious? Please specify. ")
        flag = 1
    if " most tender-hearted " in msgs:
        qtns.append(" most tender-hearted ")
        anss.append("What do you mean by most tender-hearted? Please specify. ")
        flag = 1
    if " least tender-hearted " in msgs:
        qtns.append(" least tender-hearted ")
        anss.append("What do you mean by least tender-hearted? Please specify. ")
        flag = 1
    if " very tender-hearted " in msgs:
        qtns.append(" very tender-hearted ")
        anss.append("What do you mean by very tender-hearted? Please specify. ")
        flag = 1
    if " extremely tender-hearted " in msgs:
        qtns.append(" extremely tender-hearted ")
        anss.append("What do you mean by extremely tender-hearted? Please specify. ")
        flag = 1
    if " especially tender-hearted " in msgs:
        qtns.append(" especially tender-hearted ")
        anss.append("What do you mean by especially tender-hearted? Please specify. ")
        flag = 1
    if " absolutely tender-hearted " in msgs:
        qtns.append(" absolutely tender-hearted ")
        anss.append("What do you mean by absolutely tender-hearted? Please specify. ")
        flag = 1
    if " most tense " in msgs:
        qtns.append(" most tense ")
        anss.append("What do you mean by most tense? Please specify. ")
        flag = 1
    if " least tense " in msgs:
        qtns.append(" least tense ")
        anss.append("What do you mean by least tense? Please specify. ")
        flag = 1
    if " very tense " in msgs:
        qtns.append(" very tense ")
        anss.append("What do you mean by very tense? Please specify. ")
        flag = 1
    if " extremely tense " in msgs:
        qtns.append(" extremely tense ")
        anss.append("What do you mean by extremely tense? Please specify. ")
        flag = 1
    if " especially tense " in msgs:
        qtns.append(" especially tense ")
        anss.append("What do you mean by especially tense? Please specify. ")
        flag = 1
    if " absolutely tense " in msgs:
        qtns.append(" absolutely tense ")
        anss.append("What do you mean by absolutely tense? Please specify. ")
        flag = 1
    if " most terrible " in msgs:
        qtns.append(" most terrible ")
        anss.append("What do you mean by most terrible? Please specify. ")
        flag = 1
    if " least terrible " in msgs:
        qtns.append(" least terrible ")
        anss.append("What do you mean by least terrible? Please specify. ")
        flag = 1
    if " very terrible " in msgs:
        qtns.append(" very terrible ")
        anss.append("What do you mean by very terrible? Please specify. ")
        flag = 1
    if " extremely terrible " in msgs:
        qtns.append(" extremely terrible ")
        anss.append("What do you mean by extremely terrible? Please specify. ")
        flag = 1
    if " especially terrible " in msgs:
        qtns.append(" especially terrible ")
        anss.append("What do you mean by especially terrible? Please specify. ")
        flag = 1
    if " absolutely terrible " in msgs:
        qtns.append(" absolutely terrible ")
        anss.append("What do you mean by absolutely terrible? Please specify. ")
        flag = 1
    if " most terrific " in msgs:
        qtns.append(" most terrific ")
        anss.append("What do you mean by most terrific? Please specify. ")
        flag = 1
    if " least terrific " in msgs:
        qtns.append(" least terrific ")
        anss.append("What do you mean by least terrific? Please specify. ")
        flag = 1
    if " very terrific " in msgs:
        qtns.append(" very terrific ")
        anss.append("What do you mean by very terrific? Please specify. ")
        flag = 1
    if " extremely terrific " in msgs:
        qtns.append(" extremely terrific ")
        anss.append("What do you mean by extremely terrific? Please specify. ")
        flag = 1
    if " especially terrific " in msgs:
        qtns.append(" especially terrific ")
        anss.append("What do you mean by especially terrific? Please specify. ")
        flag = 1
    if " absolutely terrific " in msgs:
        qtns.append(" absolutely terrific ")
        anss.append("What do you mean by absolutely terrific? Please specify. ")
        flag = 1
    if " most testimonial " in msgs:
        qtns.append(" most testimonial ")
        anss.append("What do you mean by most testimonial? Please specify. ")
        flag = 1
    if " least testimonial " in msgs:
        qtns.append(" least testimonial ")
        anss.append("What do you mean by least testimonial? Please specify. ")
        flag = 1
    if " very testimonial " in msgs:
        qtns.append(" very testimonial ")
        anss.append("What do you mean by very testimonial? Please specify. ")
        flag = 1
    if " extremely testimonial " in msgs:
        qtns.append(" extremely testimonial ")
        anss.append("What do you mean by extremely testimonial? Please specify. ")
        flag = 1
    if " especially testimonial " in msgs:
        qtns.append(" especially testimonial ")
        anss.append("What do you mean by especially testimonial? Please specify. ")
        flag = 1
    if " absolutely testimonial " in msgs:
        qtns.append(" absolutely testimonial ")
        anss.append("What do you mean by absolutely testimonial? Please specify. ")
        flag = 1
    if " most thankful " in msgs:
        qtns.append(" most thankful ")
        anss.append("What do you mean by most thankful? Please specify. ")
        flag = 1
    if " least thankful " in msgs:
        qtns.append(" least thankful ")
        anss.append("What do you mean by least thankful? Please specify. ")
        flag = 1
    if " very thankful " in msgs:
        qtns.append(" very thankful ")
        anss.append("What do you mean by very thankful? Please specify. ")
        flag = 1
    if " extremely thankful " in msgs:
        qtns.append(" extremely thankful ")
        anss.append("What do you mean by extremely thankful? Please specify. ")
        flag = 1
    if " especially thankful " in msgs:
        qtns.append(" especially thankful ")
        anss.append("What do you mean by especially thankful? Please specify. ")
        flag = 1
    if " absolutely thankful " in msgs:
        qtns.append(" absolutely thankful ")
        anss.append("What do you mean by absolutely thankful? Please specify. ")
        flag = 1
    if " most thankworthy " in msgs:
        qtns.append(" most thankworthy ")
        anss.append("What do you mean by most thankworthy? Please specify. ")
        flag = 1
    if " least thankworthy " in msgs:
        qtns.append(" least thankworthy ")
        anss.append("What do you mean by least thankworthy? Please specify. ")
        flag = 1
    if " very thankworthy " in msgs:
        qtns.append(" very thankworthy ")
        anss.append("What do you mean by very thankworthy? Please specify. ")
        flag = 1
    if " extremely thankworthy " in msgs:
        qtns.append(" extremely thankworthy ")
        anss.append("What do you mean by extremely thankworthy? Please specify. ")
        flag = 1
    if " especially thankworthy " in msgs:
        qtns.append(" especially thankworthy ")
        anss.append("What do you mean by especially thankworthy? Please specify. ")
        flag = 1
    if " absolutely thankworthy " in msgs:
        qtns.append(" absolutely thankworthy ")
        anss.append("What do you mean by absolutely thankworthy? Please specify. ")
        flag = 1
    if " most therapeutic " in msgs:
        qtns.append(" most therapeutic ")
        anss.append("What do you mean by most therapeutic? Please specify. ")
        flag = 1
    if " least therapeutic " in msgs:
        qtns.append(" least therapeutic ")
        anss.append("What do you mean by least therapeutic? Please specify. ")
        flag = 1
    if " very therapeutic " in msgs:
        qtns.append(" very therapeutic ")
        anss.append("What do you mean by very therapeutic? Please specify. ")
        flag = 1
    if " extremely therapeutic " in msgs:
        qtns.append(" extremely therapeutic ")
        anss.append("What do you mean by extremely therapeutic? Please specify. ")
        flag = 1
    if " especially therapeutic " in msgs:
        qtns.append(" especially therapeutic ")
        anss.append("What do you mean by especially therapeutic? Please specify. ")
        flag = 1
    if " absolutely therapeutic " in msgs:
        qtns.append(" absolutely therapeutic ")
        anss.append("What do you mean by absolutely therapeutic? Please specify. ")
        flag = 1
    if " most thick " in msgs:
        qtns.append(" most thick ")
        anss.append("What do you mean by most thick? Please specify. ")
        flag = 1
    if " least thick " in msgs:
        qtns.append(" least thick ")
        anss.append("What do you mean by least thick? Please specify. ")
        flag = 1
    if " very thick " in msgs:
        qtns.append(" very thick ")
        anss.append("What do you mean by very thick? Please specify. ")
        flag = 1
    if " extremely thick " in msgs:
        qtns.append(" extremely thick ")
        anss.append("What do you mean by extremely thick? Please specify. ")
        flag = 1
    if " especially thick " in msgs:
        qtns.append(" especially thick ")
        anss.append("What do you mean by especially thick? Please specify. ")
        flag = 1
    if " absolutely thick " in msgs:
        qtns.append(" absolutely thick ")
        anss.append("What do you mean by absolutely thick? Please specify. ")
        flag = 1
    if " most thick " in msgs:
        qtns.append(" most thick ")
        anss.append("What do you mean by most thick? Please specify. ")
        flag = 1
    if " least thick " in msgs:
        qtns.append(" least thick ")
        anss.append("What do you mean by least thick? Please specify. ")
        flag = 1
    if " very thick " in msgs:
        qtns.append(" very thick ")
        anss.append("What do you mean by very thick? Please specify. ")
        flag = 1
    if " extremely thick " in msgs:
        qtns.append(" extremely thick ")
        anss.append("What do you mean by extremely thick? Please specify. ")
        flag = 1
    if " especially thick " in msgs:
        qtns.append(" especially thick ")
        anss.append("What do you mean by especially thick? Please specify. ")
        flag = 1
    if " absolutely thick " in msgs:
        qtns.append(" absolutely thick ")
        anss.append("What do you mean by absolutely thick? Please specify. ")
        flag = 1
    if " most thin " in msgs:
        qtns.append(" most thin ")
        anss.append("What do you mean by most thin? Please specify. ")
        flag = 1
    if " least thin " in msgs:
        qtns.append(" least thin ")
        anss.append("What do you mean by least thin? Please specify. ")
        flag = 1
    if " very thin " in msgs:
        qtns.append(" very thin ")
        anss.append("What do you mean by very thin? Please specify. ")
        flag = 1
    if " extremely thin " in msgs:
        qtns.append(" extremely thin ")
        anss.append("What do you mean by extremely thin? Please specify. ")
        flag = 1
    if " especially thin " in msgs:
        qtns.append(" especially thin ")
        anss.append("What do you mean by especially thin? Please specify. ")
        flag = 1
    if " absolutely thin " in msgs:
        qtns.append(" absolutely thin ")
        anss.append("What do you mean by absolutely thin? Please specify. ")
        flag = 1
    if " most thin " in msgs:
        qtns.append(" most thin ")
        anss.append("What do you mean by most thin? Please specify. ")
        flag = 1
    if " least thin " in msgs:
        qtns.append(" least thin ")
        anss.append("What do you mean by least thin? Please specify. ")
        flag = 1
    if " very thin " in msgs:
        qtns.append(" very thin ")
        anss.append("What do you mean by very thin? Please specify. ")
        flag = 1
    if " extremely thin " in msgs:
        qtns.append(" extremely thin ")
        anss.append("What do you mean by extremely thin? Please specify. ")
        flag = 1
    if " especially thin " in msgs:
        qtns.append(" especially thin ")
        anss.append("What do you mean by especially thin? Please specify. ")
        flag = 1
    if " absolutely thin " in msgs:
        qtns.append(" absolutely thin ")
        anss.append("What do you mean by absolutely thin? Please specify. ")
        flag = 1
    if " most thirsty " in msgs:
        qtns.append(" most thirsty ")
        anss.append("What do you mean by most thirsty? Please specify. ")
        flag = 1
    if " least thirsty " in msgs:
        qtns.append(" least thirsty ")
        anss.append("What do you mean by least thirsty? Please specify. ")
        flag = 1
    if " very thirsty " in msgs:
        qtns.append(" very thirsty ")
        anss.append("What do you mean by very thirsty? Please specify. ")
        flag = 1
    if " extremely thirsty " in msgs:
        qtns.append(" extremely thirsty ")
        anss.append("What do you mean by extremely thirsty? Please specify. ")
        flag = 1
    if " especially thirsty " in msgs:
        qtns.append(" especially thirsty ")
        anss.append("What do you mean by especially thirsty? Please specify. ")
        flag = 1
    if " absolutely thirsty " in msgs:
        qtns.append(" absolutely thirsty ")
        anss.append("What do you mean by absolutely thirsty? Please specify. ")
        flag = 1
    if " most thorough " in msgs:
        qtns.append(" most thorough ")
        anss.append("What do you mean by most thorough? Please specify. ")
        flag = 1
    if " least thorough " in msgs:
        qtns.append(" least thorough ")
        anss.append("What do you mean by least thorough? Please specify. ")
        flag = 1
    if " very thorough " in msgs:
        qtns.append(" very thorough ")
        anss.append("What do you mean by very thorough? Please specify. ")
        flag = 1
    if " extremely thorough " in msgs:
        qtns.append(" extremely thorough ")
        anss.append("What do you mean by extremely thorough? Please specify. ")
        flag = 1
    if " especially thorough " in msgs:
        qtns.append(" especially thorough ")
        anss.append("What do you mean by especially thorough? Please specify. ")
        flag = 1
    if " absolutely thorough " in msgs:
        qtns.append(" absolutely thorough ")
        anss.append("What do you mean by absolutely thorough? Please specify. ")
        flag = 1
    if " most thoughtful " in msgs:
        qtns.append(" most thoughtful ")
        anss.append("What do you mean by most thoughtful? Please specify. ")
        flag = 1
    if " least thoughtful " in msgs:
        qtns.append(" least thoughtful ")
        anss.append("What do you mean by least thoughtful? Please specify. ")
        flag = 1
    if " very thoughtful " in msgs:
        qtns.append(" very thoughtful ")
        anss.append("What do you mean by very thoughtful? Please specify. ")
        flag = 1
    if " extremely thoughtful " in msgs:
        qtns.append(" extremely thoughtful ")
        anss.append("What do you mean by extremely thoughtful? Please specify. ")
        flag = 1
    if " especially thoughtful " in msgs:
        qtns.append(" especially thoughtful ")
        anss.append("What do you mean by especially thoughtful? Please specify. ")
        flag = 1
    if " absolutely thoughtful " in msgs:
        qtns.append(" absolutely thoughtful ")
        anss.append("What do you mean by absolutely thoughtful? Please specify. ")
        flag = 1
    if " most tiny " in msgs:
        qtns.append(" most tiny ")
        anss.append("What do you mean by most tiny? Please specify. ")
        flag = 1
    if " least tiny " in msgs:
        qtns.append(" least tiny ")
        anss.append("What do you mean by least tiny? Please specify. ")
        flag = 1
    if " very tiny " in msgs:
        qtns.append(" very tiny ")
        anss.append("What do you mean by very tiny? Please specify. ")
        flag = 1
    if " extremely tiny " in msgs:
        qtns.append(" extremely tiny ")
        anss.append("What do you mean by extremely tiny? Please specify. ")
        flag = 1
    if " especially tiny " in msgs:
        qtns.append(" especially tiny ")
        anss.append("What do you mean by especially tiny? Please specify. ")
        flag = 1
    if " absolutely tiny " in msgs:
        qtns.append(" absolutely tiny ")
        anss.append("What do you mean by absolutely tiny? Please specify. ")
        flag = 1
    if " most tiny " in msgs:
        qtns.append(" most tiny ")
        anss.append("What do you mean by most tiny? Please specify. ")
        flag = 1
    if " least tiny " in msgs:
        qtns.append(" least tiny ")
        anss.append("What do you mean by least tiny? Please specify. ")
        flag = 1
    if " very tiny " in msgs:
        qtns.append(" very tiny ")
        anss.append("What do you mean by very tiny? Please specify. ")
        flag = 1
    if " extremely tiny " in msgs:
        qtns.append(" extremely tiny ")
        anss.append("What do you mean by extremely tiny? Please specify. ")
        flag = 1
    if " especially tiny " in msgs:
        qtns.append(" especially tiny ")
        anss.append("What do you mean by especially tiny? Please specify. ")
        flag = 1
    if " absolutely tiny " in msgs:
        qtns.append(" absolutely tiny ")
        anss.append("What do you mean by absolutely tiny? Please specify. ")
        flag = 1
    if " most tired " in msgs:
        qtns.append(" most tired ")
        anss.append("What do you mean by most tired? Please specify. ")
        flag = 1
    if " least tired " in msgs:
        qtns.append(" least tired ")
        anss.append("What do you mean by least tired? Please specify. ")
        flag = 1
    if " very tired " in msgs:
        qtns.append(" very tired ")
        anss.append("What do you mean by very tired? Please specify. ")
        flag = 1
    if " extremely tired " in msgs:
        qtns.append(" extremely tired ")
        anss.append("What do you mean by extremely tired? Please specify. ")
        flag = 1
    if " especially tired " in msgs:
        qtns.append(" especially tired ")
        anss.append("What do you mean by especially tired? Please specify. ")
        flag = 1
    if " absolutely tired " in msgs:
        qtns.append(" absolutely tired ")
        anss.append("What do you mean by absolutely tired? Please specify. ")
        flag = 1
    if " most tough " in msgs:
        qtns.append(" most tough ")
        anss.append("What do you mean by most tough? Please specify. ")
        flag = 1
    if " least tough " in msgs:
        qtns.append(" least tough ")
        anss.append("What do you mean by least tough? Please specify. ")
        flag = 1
    if " very tough " in msgs:
        qtns.append(" very tough ")
        anss.append("What do you mean by very tough? Please specify. ")
        flag = 1
    if " extremely tough " in msgs:
        qtns.append(" extremely tough ")
        anss.append("What do you mean by extremely tough? Please specify. ")
        flag = 1
    if " especially tough " in msgs:
        qtns.append(" especially tough ")
        anss.append("What do you mean by especially tough? Please specify. ")
        flag = 1
    if " absolutely tough " in msgs:
        qtns.append(" absolutely tough ")
        anss.append("What do you mean by absolutely tough? Please specify. ")
        flag = 1
    if " most true " in msgs:
        qtns.append(" most true ")
        anss.append("What do you mean by most true? Please specify. ")
        flag = 1
    if " least true " in msgs:
        qtns.append(" least true ")
        anss.append("What do you mean by least true? Please specify. ")
        flag = 1
    if " very true " in msgs:
        qtns.append(" very true ")
        anss.append("What do you mean by very true? Please specify. ")
        flag = 1
    if " extremely true " in msgs:
        qtns.append(" extremely true ")
        anss.append("What do you mean by extremely true? Please specify. ")
        flag = 1
    if " especially true " in msgs:
        qtns.append(" especially true ")
        anss.append("What do you mean by especially true? Please specify. ")
        flag = 1
    if " absolutely true " in msgs:
        qtns.append(" absolutely true ")
        anss.append("What do you mean by absolutely true? Please specify. ")
        flag = 1
    if " most ugly " in msgs:
        qtns.append(" most ugly ")
        anss.append("What do you mean by most ugly? Please specify. ")
        flag = 1
    if " least ugly " in msgs:
        qtns.append(" least ugly ")
        anss.append("What do you mean by least ugly? Please specify. ")
        flag = 1
    if " very ugly " in msgs:
        qtns.append(" very ugly ")
        anss.append("What do you mean by very ugly? Please specify. ")
        flag = 1
    if " extremely ugly " in msgs:
        qtns.append(" extremely ugly ")
        anss.append("What do you mean by extremely ugly? Please specify. ")
        flag = 1
    if " especially ugly " in msgs:
        qtns.append(" especially ugly ")
        anss.append("What do you mean by especially ugly? Please specify. ")
        flag = 1
    if " absolutely ugly " in msgs:
        qtns.append(" absolutely ugly ")
        anss.append("What do you mean by absolutely ugly? Please specify. ")
        flag = 1
    if " most unique " in msgs:
        qtns.append(" most unique ")
        anss.append("What do you mean by most unique? Please specify. ")
        flag = 1
    if " least unique " in msgs:
        qtns.append(" least unique ")
        anss.append("What do you mean by least unique? Please specify. ")
        flag = 1
    if " very unique " in msgs:
        qtns.append(" very unique ")
        anss.append("What do you mean by very unique? Please specify. ")
        flag = 1
    if " extremely unique " in msgs:
        qtns.append(" extremely unique ")
        anss.append("What do you mean by extremely unique? Please specify. ")
        flag = 1
    if " especially unique " in msgs:
        qtns.append(" especially unique ")
        anss.append("What do you mean by especially unique? Please specify. ")
        flag = 1
    if " absolutely unique " in msgs:
        qtns.append(" absolutely unique ")
        anss.append("What do you mean by absolutely unique? Please specify. ")
        flag = 1
    if " most untidy " in msgs:
        qtns.append(" most untidy ")
        anss.append("What do you mean by most untidy? Please specify. ")
        flag = 1
    if " least untidy " in msgs:
        qtns.append(" least untidy ")
        anss.append("What do you mean by least untidy? Please specify. ")
        flag = 1
    if " very untidy " in msgs:
        qtns.append(" very untidy ")
        anss.append("What do you mean by very untidy? Please specify. ")
        flag = 1
    if " extremely untidy " in msgs:
        qtns.append(" extremely untidy ")
        anss.append("What do you mean by extremely untidy? Please specify. ")
        flag = 1
    if " especially untidy " in msgs:
        qtns.append(" especially untidy ")
        anss.append("What do you mean by especially untidy? Please specify. ")
        flag = 1
    if " absolutely untidy " in msgs:
        qtns.append(" absolutely untidy ")
        anss.append("What do you mean by absolutely untidy? Please specify. ")
        flag = 1
    if " most upset " in msgs:
        qtns.append(" most upset ")
        anss.append("What do you mean by most upset? Please specify. ")
        flag = 1
    if " least upset " in msgs:
        qtns.append(" least upset ")
        anss.append("What do you mean by least upset? Please specify. ")
        flag = 1
    if " very upset " in msgs:
        qtns.append(" very upset ")
        anss.append("What do you mean by very upset? Please specify. ")
        flag = 1
    if " extremely upset " in msgs:
        qtns.append(" extremely upset ")
        anss.append("What do you mean by extremely upset? Please specify. ")
        flag = 1
    if " especially upset " in msgs:
        qtns.append(" especially upset ")
        anss.append("What do you mean by especially upset? Please specify. ")
        flag = 1
    if " absolutely upset " in msgs:
        qtns.append(" absolutely upset ")
        anss.append("What do you mean by absolutely upset? Please specify. ")
        flag = 1
    if " most victorious " in msgs:
        qtns.append(" most victorious ")
        anss.append("What do you mean by most victorious? Please specify. ")
        flag = 1
    if " least victorious " in msgs:
        qtns.append(" least victorious ")
        anss.append("What do you mean by least victorious? Please specify. ")
        flag = 1
    if " very victorious " in msgs:
        qtns.append(" very victorious ")
        anss.append("What do you mean by very victorious? Please specify. ")
        flag = 1
    if " extremely victorious " in msgs:
        qtns.append(" extremely victorious ")
        anss.append("What do you mean by extremely victorious? Please specify. ")
        flag = 1
    if " especially victorious " in msgs:
        qtns.append(" especially victorious ")
        anss.append("What do you mean by especially victorious? Please specify. ")
        flag = 1
    if " absolutely victorious " in msgs:
        qtns.append(" absolutely victorious ")
        anss.append("What do you mean by absolutely victorious? Please specify. ")
        flag = 1
    if " most violent " in msgs:
        qtns.append(" most violent ")
        anss.append("What do you mean by most violent? Please specify. ")
        flag = 1
    if " least violent " in msgs:
        qtns.append(" least violent ")
        anss.append("What do you mean by least violent? Please specify. ")
        flag = 1
    if " very violent " in msgs:
        qtns.append(" very violent ")
        anss.append("What do you mean by very violent? Please specify. ")
        flag = 1
    if " extremely violent " in msgs:
        qtns.append(" extremely violent ")
        anss.append("What do you mean by extremely violent? Please specify. ")
        flag = 1
    if " especially violent " in msgs:
        qtns.append(" especially violent ")
        anss.append("What do you mean by especially violent? Please specify. ")
        flag = 1
    if " absolutely violent " in msgs:
        qtns.append(" absolutely violent ")
        anss.append("What do you mean by absolutely violent? Please specify. ")
        flag = 1
    if " most vulgar " in msgs:
        qtns.append(" most vulgar ")
        anss.append("What do you mean by most vulgar? Please specify. ")
        flag = 1
    if " least vulgar " in msgs:
        qtns.append(" least vulgar ")
        anss.append("What do you mean by least vulgar? Please specify. ")
        flag = 1
    if " very vulgar " in msgs:
        qtns.append(" very vulgar ")
        anss.append("What do you mean by very vulgar? Please specify. ")
        flag = 1
    if " extremely vulgar " in msgs:
        qtns.append(" extremely vulgar ")
        anss.append("What do you mean by extremely vulgar? Please specify. ")
        flag = 1
    if " especially vulgar " in msgs:
        qtns.append(" especially vulgar ")
        anss.append("What do you mean by especially vulgar? Please specify. ")
        flag = 1
    if " absolutely vulgar " in msgs:
        qtns.append(" absolutely vulgar ")
        anss.append("What do you mean by absolutely vulgar? Please specify. ")
        flag = 1
    if " most warm " in msgs:
        qtns.append(" most warm ")
        anss.append("What do you mean by most warm? Please specify. ")
        flag = 1
    if " least warm " in msgs:
        qtns.append(" least warm ")
        anss.append("What do you mean by least warm? Please specify. ")
        flag = 1
    if " very warm " in msgs:
        qtns.append(" very warm ")
        anss.append("What do you mean by very warm? Please specify. ")
        flag = 1
    if " extremely warm " in msgs:
        qtns.append(" extremely warm ")
        anss.append("What do you mean by extremely warm? Please specify. ")
        flag = 1
    if " especially warm " in msgs:
        qtns.append(" especially warm ")
        anss.append("What do you mean by especially warm? Please specify. ")
        flag = 1
    if " absolutely warm " in msgs:
        qtns.append(" absolutely warm ")
        anss.append("What do you mean by absolutely warm? Please specify. ")
        flag = 1
    if " most weak " in msgs:
        qtns.append(" most weak ")
        anss.append("What do you mean by most weak? Please specify. ")
        flag = 1
    if " least weak " in msgs:
        qtns.append(" least weak ")
        anss.append("What do you mean by least weak? Please specify. ")
        flag = 1
    if " very weak " in msgs:
        qtns.append(" very weak ")
        anss.append("What do you mean by very weak? Please specify. ")
        flag = 1
    if " extremely weak " in msgs:
        qtns.append(" extremely weak ")
        anss.append("What do you mean by extremely weak? Please specify. ")
        flag = 1
    if " especially weak " in msgs:
        qtns.append(" especially weak ")
        anss.append("What do you mean by especially weak? Please specify. ")
        flag = 1
    if " absolutely weak " in msgs:
        qtns.append(" absolutely weak ")
        anss.append("What do you mean by absolutely weak? Please specify. ")
        flag = 1
    if " most wealthy " in msgs:
        qtns.append(" most wealthy ")
        anss.append("What do you mean by most wealthy? Please specify. ")
        flag = 1
    if " least wealthy " in msgs:
        qtns.append(" least wealthy ")
        anss.append("What do you mean by least wealthy? Please specify. ")
        flag = 1
    if " very wealthy " in msgs:
        qtns.append(" very wealthy ")
        anss.append("What do you mean by very wealthy? Please specify. ")
        flag = 1
    if " extremely wealthy " in msgs:
        qtns.append(" extremely wealthy ")
        anss.append("What do you mean by extremely wealthy? Please specify. ")
        flag = 1
    if " especially wealthy " in msgs:
        qtns.append(" especially wealthy ")
        anss.append("What do you mean by especially wealthy? Please specify. ")
        flag = 1
    if " absolutely wealthy " in msgs:
        qtns.append(" absolutely wealthy ")
        anss.append("What do you mean by absolutely wealthy? Please specify. ")
        flag = 1
    if " most weird " in msgs:
        qtns.append(" most weird ")
        anss.append("What do you mean by most weird? Please specify. ")
        flag = 1
    if " least weird " in msgs:
        qtns.append(" least weird ")
        anss.append("What do you mean by least weird? Please specify. ")
        flag = 1
    if " very weird " in msgs:
        qtns.append(" very weird ")
        anss.append("What do you mean by very weird? Please specify. ")
        flag = 1
    if " extremely weird " in msgs:
        qtns.append(" extremely weird ")
        anss.append("What do you mean by extremely weird? Please specify. ")
        flag = 1
    if " especially weird " in msgs:
        qtns.append(" especially weird ")
        anss.append("What do you mean by especially weird? Please specify. ")
        flag = 1
    if " absolutely weird " in msgs:
        qtns.append(" absolutely weird ")
        anss.append("What do you mean by absolutely weird? Please specify. ")
        flag = 1
    if " most wet " in msgs:
        qtns.append(" most wet ")
        anss.append("What do you mean by most wet? Please specify. ")
        flag = 1
    if " least wet " in msgs:
        qtns.append(" least wet ")
        anss.append("What do you mean by least wet? Please specify. ")
        flag = 1
    if " very wet " in msgs:
        qtns.append(" very wet ")
        anss.append("What do you mean by very wet? Please specify. ")
        flag = 1
    if " extremely wet " in msgs:
        qtns.append(" extremely wet ")
        anss.append("What do you mean by extremely wet? Please specify. ")
        flag = 1
    if " especially wet " in msgs:
        qtns.append(" especially wet ")
        anss.append("What do you mean by especially wet? Please specify. ")
        flag = 1
    if " absolutely wet " in msgs:
        qtns.append(" absolutely wet ")
        anss.append("What do you mean by absolutely wet? Please specify. ")
        flag = 1
    if " most wide " in msgs:
        qtns.append(" most wide ")
        anss.append("What do you mean by most wide? Please specify. ")
        flag = 1
    if " least wide " in msgs:
        qtns.append(" least wide ")
        anss.append("What do you mean by least wide? Please specify. ")
        flag = 1
    if " very wide " in msgs:
        qtns.append(" very wide ")
        anss.append("What do you mean by very wide? Please specify. ")
        flag = 1
    if " extremely wide " in msgs:
        qtns.append(" extremely wide ")
        anss.append("What do you mean by extremely wide? Please specify. ")
        flag = 1
    if " especially wide " in msgs:
        qtns.append(" especially wide ")
        anss.append("What do you mean by especially wide? Please specify. ")
        flag = 1
    if " absolutely wide " in msgs:
        qtns.append(" absolutely wide ")
        anss.append("What do you mean by absolutely wide? Please specify. ")
        flag = 1
    if " most wild " in msgs:
        qtns.append(" most wild ")
        anss.append("What do you mean by most wild? Please specify. ")
        flag = 1
    if " least wild " in msgs:
        qtns.append(" least wild ")
        anss.append("What do you mean by least wild? Please specify. ")
        flag = 1
    if " very wild " in msgs:
        qtns.append(" very wild ")
        anss.append("What do you mean by very wild? Please specify. ")
        flag = 1
    if " extremely wild " in msgs:
        qtns.append(" extremely wild ")
        anss.append("What do you mean by extremely wild? Please specify. ")
        flag = 1
    if " especially wild " in msgs:
        qtns.append(" especially wild ")
        anss.append("What do you mean by especially wild? Please specify. ")
        flag = 1
    if " absolutely wild " in msgs:
        qtns.append(" absolutely wild ")
        anss.append("What do you mean by absolutely wild? Please specify. ")
        flag = 1
    if " most windy " in msgs:
        qtns.append(" most windy ")
        anss.append("What do you mean by most windy? Please specify. ")
        flag = 1
    if " least windy " in msgs:
        qtns.append(" least windy ")
        anss.append("What do you mean by least windy? Please specify. ")
        flag = 1
    if " very windy " in msgs:
        qtns.append(" very windy ")
        anss.append("What do you mean by very windy? Please specify. ")
        flag = 1
    if " extremely windy " in msgs:
        qtns.append(" extremely windy ")
        anss.append("What do you mean by extremely windy? Please specify. ")
        flag = 1
    if " especially windy " in msgs:
        qtns.append(" especially windy ")
        anss.append("What do you mean by especially windy? Please specify. ")
        flag = 1
    if " absolutely windy " in msgs:
        qtns.append(" absolutely windy ")
        anss.append("What do you mean by absolutely windy? Please specify. ")
        flag = 1
    if " most wise " in msgs:
        qtns.append(" most wise ")
        anss.append("What do you mean by most wise? Please specify. ")
        flag = 1
    if " least wise " in msgs:
        qtns.append(" least wise ")
        anss.append("What do you mean by least wise? Please specify. ")
        flag = 1
    if " very wise " in msgs:
        qtns.append(" very wise ")
        anss.append("What do you mean by very wise? Please specify. ")
        flag = 1
    if " extremely wise " in msgs:
        qtns.append(" extremely wise ")
        anss.append("What do you mean by extremely wise? Please specify. ")
        flag = 1
    if " especially wise " in msgs:
        qtns.append(" especially wise ")
        anss.append("What do you mean by especially wise? Please specify. ")
        flag = 1
    if " absolutely wise " in msgs:
        qtns.append(" absolutely wise ")
        anss.append("What do you mean by absolutely wise? Please specify. ")
        flag = 1
    if " most witty " in msgs:
        qtns.append(" most witty ")
        anss.append("What do you mean by most witty? Please specify. ")
        flag = 1
    if " least witty " in msgs:
        qtns.append(" least witty ")
        anss.append("What do you mean by least witty? Please specify. ")
        flag = 1
    if " very witty " in msgs:
        qtns.append(" very witty ")
        anss.append("What do you mean by very witty? Please specify. ")
        flag = 1
    if " extremely witty " in msgs:
        qtns.append(" extremely witty ")
        anss.append("What do you mean by extremely witty? Please specify. ")
        flag = 1
    if " especially witty " in msgs:
        qtns.append(" especially witty ")
        anss.append("What do you mean by especially witty? Please specify. ")
        flag = 1
    if " absolutely witty " in msgs:
        qtns.append(" absolutely witty ")
        anss.append("What do you mean by absolutely witty? Please specify. ")
        flag = 1
    if " most wonderful " in msgs:
        qtns.append(" most wonderful ")
        anss.append("What do you mean by most wonderful? Please specify. ")
        flag = 1
    if " least wonderful " in msgs:
        qtns.append(" least wonderful ")
        anss.append("What do you mean by least wonderful? Please specify. ")
        flag = 1
    if " very wonderful " in msgs:
        qtns.append(" very wonderful ")
        anss.append("What do you mean by very wonderful? Please specify. ")
        flag = 1
    if " extremely wonderful " in msgs:
        qtns.append(" extremely wonderful ")
        anss.append("What do you mean by extremely wonderful? Please specify. ")
        flag = 1
    if " especially wonderful " in msgs:
        qtns.append(" especially wonderful ")
        anss.append("What do you mean by especially wonderful? Please specify. ")
        flag = 1
    if " absolutely wonderful " in msgs:
        qtns.append(" absolutely wonderful ")
        anss.append("What do you mean by absolutely wonderful? Please specify. ")
        flag = 1
    if " most worldly " in msgs:
        qtns.append(" most worldly ")
        anss.append("What do you mean by most worldly? Please specify. ")
        flag = 1
    if " least worldly " in msgs:
        qtns.append(" least worldly ")
        anss.append("What do you mean by least worldly? Please specify. ")
        flag = 1
    if " very worldly " in msgs:
        qtns.append(" very worldly ")
        anss.append("What do you mean by very worldly? Please specify. ")
        flag = 1
    if " extremely worldly " in msgs:
        qtns.append(" extremely worldly ")
        anss.append("What do you mean by extremely worldly? Please specify. ")
        flag = 1
    if " especially worldly " in msgs:
        qtns.append(" especially worldly ")
        anss.append("What do you mean by especially worldly? Please specify. ")
        flag = 1
    if " absolutely worldly " in msgs:
        qtns.append(" absolutely worldly ")
        anss.append("What do you mean by absolutely worldly? Please specify. ")
        flag = 1
    if " most worried " in msgs:
        qtns.append(" most worried ")
        anss.append("What do you mean by most worried? Please specify. ")
        flag = 1
    if " least worried " in msgs:
        qtns.append(" least worried ")
        anss.append("What do you mean by least worried? Please specify. ")
        flag = 1
    if " very worried " in msgs:
        qtns.append(" very worried ")
        anss.append("What do you mean by very worried? Please specify. ")
        flag = 1
    if " extremely worried " in msgs:
        qtns.append(" extremely worried ")
        anss.append("What do you mean by extremely worried? Please specify. ")
        flag = 1
    if " especially worried " in msgs:
        qtns.append(" especially worried ")
        anss.append("What do you mean by especially worried? Please specify. ")
        flag = 1
    if " absolutely worried " in msgs:
        qtns.append(" absolutely worried ")
        anss.append("What do you mean by absolutely worried? Please specify. ")
        flag = 1
    if " most worthy " in msgs:
        qtns.append(" most worthy ")
        anss.append("What do you mean by most worthy? Please specify. ")
        flag = 1
    if " least worthy " in msgs:
        qtns.append(" least worthy ")
        anss.append("What do you mean by least worthy? Please specify. ")
        flag = 1
    if " very worthy " in msgs:
        qtns.append(" very worthy ")
        anss.append("What do you mean by very worthy? Please specify. ")
        flag = 1
    if " extremely worthy " in msgs:
        qtns.append(" extremely worthy ")
        anss.append("What do you mean by extremely worthy? Please specify. ")
        flag = 1
    if " especially worthy " in msgs:
        qtns.append(" especially worthy ")
        anss.append("What do you mean by especially worthy? Please specify. ")
        flag = 1
    if " absolutely worthy " in msgs:
        qtns.append(" absolutely worthy ")
        anss.append("What do you mean by absolutely worthy? Please specify. ")
        flag = 1
    if " most young " in msgs:
        qtns.append(" most young ")
        anss.append("What do you mean by most young? Please specify. ")
        flag = 1
    if " least young " in msgs:
        qtns.append(" least young ")
        anss.append("What do you mean by least young? Please specify. ")
        flag = 1
    if " very young " in msgs:
        qtns.append(" very young ")
        anss.append("What do you mean by very young? Please specify. ")
        flag = 1
    if " extremely young " in msgs:
        qtns.append(" extremely young ")
        anss.append("What do you mean by extremely young? Please specify. ")
        flag = 1
    if " especially young " in msgs:
        qtns.append(" especially young ")
        anss.append("What do you mean by especially young? Please specify. ")
        flag = 1
    if " absolutely young " in msgs:
        qtns.append(" absolutely young ")
        anss.append("What do you mean by absolutely young? Please specify. ")
        flag = 1
    if " most youthful " in msgs:
        qtns.append(" most youthful ")
        anss.append("What do you mean by most youthful? Please specify. ")
        flag = 1
    if " least youthful " in msgs:
        qtns.append(" least youthful ")
        anss.append("What do you mean by least youthful? Please specify. ")
        flag = 1
    if " very youthful " in msgs:
        qtns.append(" very youthful ")
        anss.append("What do you mean by very youthful? Please specify. ")
        flag = 1
    if " extremely youthful " in msgs:
        qtns.append(" extremely youthful ")
        anss.append("What do you mean by extremely youthful? Please specify. ")
        flag = 1
    if " especially youthful " in msgs:
        qtns.append(" especially youthful ")
        anss.append("What do you mean by especially youthful? Please specify. ")
        flag = 1
    if " absolutely youthful " in msgs:
        qtns.append(" absolutely youthful ")
        anss.append("What do you mean by absolutely youthful? Please specify. ")
        flag = 1
    if " most zealous " in msgs:
        qtns.append(" most zealous ")
        anss.append("What do you mean by most zealous? Please specify. ")
        flag = 1
    if " least zealous " in msgs:
        qtns.append(" least zealous ")
        anss.append("What do you mean by least zealous? Please specify. ")
        flag = 1
    if " very zealous " in msgs:
        qtns.append(" very zealous ")
        anss.append("What do you mean by very zealous? Please specify. ")
        flag = 1
    if " extremely zealous " in msgs:
        qtns.append(" extremely zealous ")
        anss.append("What do you mean by extremely zealous? Please specify. ")
        flag = 1
    if " especially zealous " in msgs:
        qtns.append(" especially zealous ")
        anss.append("What do you mean by especially zealous? Please specify. ")
        flag = 1
    if " absolutely zealous " in msgs:
        qtns.append(" absolutely zealous ")
        anss.append("What do you mean by absolutely zealous? Please specify. ")
        flag = 1
    if " more abactinal " in msgs:
        qtns.append(" more abactinal ")
        anss.append("more abactinal than what/whom? more abactinal compared to what/whom? ")
        flag = 1
    if " less abactinal " in msgs:
        qtns.append(" less abactinal ")
        anss.append("less abactinal than what/whom? less abactinal compared to what/whom? ")
        flag = 1
    if " more abandoned " in msgs:
        qtns.append(" more abandoned ")
        anss.append("more abandoned than what/whom? more abandoned compared to what/whom? ")
        flag = 1
    if " less abandoned " in msgs:
        qtns.append(" less abandoned ")
        anss.append("less abandoned than what/whom? less abandoned compared to what/whom? ")
        flag = 1
    if " more abashed " in msgs:
        qtns.append(" more abashed ")
        anss.append("more abashed than what/whom? more abashed compared to what/whom? ")
        flag = 1
    if " less abashed " in msgs:
        qtns.append(" less abashed ")
        anss.append("less abashed than what/whom? less abashed compared to what/whom? ")
        flag = 1
    if " more abatable " in msgs:
        qtns.append(" more abatable ")
        anss.append("more abatable than what/whom? more abatable compared to what/whom? ")
        flag = 1
    if " less abatable " in msgs:
        qtns.append(" less abatable ")
        anss.append("less abatable than what/whom? less abatable compared to what/whom? ")
        flag = 1
    if " more abatic " in msgs:
        qtns.append(" more abatic ")
        anss.append("more abatic than what/whom? more abatic compared to what/whom? ")
        flag = 1
    if " less abatic " in msgs:
        qtns.append(" less abatic ")
        anss.append("less abatic than what/whom? less abatic compared to what/whom? ")
        flag = 1
    if " more abaxial " in msgs:
        qtns.append(" more abaxial ")
        anss.append("more abaxial than what/whom? more abaxial compared to what/whom? ")
        flag = 1
    if " less abaxial " in msgs:
        qtns.append(" less abaxial ")
        anss.append("less abaxial than what/whom? less abaxial compared to what/whom? ")
        flag = 1
    if " more abbatial " in msgs:
        qtns.append(" more abbatial ")
        anss.append("more abbatial than what/whom? more abbatial compared to what/whom? ")
        flag = 1
    if " less abbatial " in msgs:
        qtns.append(" less abbatial ")
        anss.append("less abbatial than what/whom? less abbatial compared to what/whom? ")
        flag = 1
    if " more abbreviated " in msgs:
        qtns.append(" more abbreviated ")
        anss.append("more abbreviated than what/whom? more abbreviated compared to what/whom? ")
        flag = 1
    if " less abbreviated " in msgs:
        qtns.append(" less abbreviated ")
        anss.append("less abbreviated than what/whom? less abbreviated compared to what/whom? ")
        flag = 1
    if " more abducent " in msgs:
        qtns.append(" more abducent ")
        anss.append("more abducent than what/whom? more abducent compared to what/whom? ")
        flag = 1
    if " less abducent " in msgs:
        qtns.append(" less abducent ")
        anss.append("less abducent than what/whom? less abducent compared to what/whom? ")
        flag = 1
    if " more abducting " in msgs:
        qtns.append(" more abducting ")
        anss.append("more abducting than what/whom? more abducting compared to what/whom? ")
        flag = 1
    if " less abducting " in msgs:
        qtns.append(" less abducting ")
        anss.append("less abducting than what/whom? less abducting compared to what/whom? ")
        flag = 1
    if " more aberrant " in msgs:
        qtns.append(" more aberrant ")
        anss.append("more aberrant than what/whom? more aberrant compared to what/whom? ")
        flag = 1
    if " less aberrant " in msgs:
        qtns.append(" less aberrant ")
        anss.append("less aberrant than what/whom? less aberrant compared to what/whom? ")
        flag = 1
    if " more abeyant " in msgs:
        qtns.append(" more abeyant ")
        anss.append("more abeyant than what/whom? more abeyant compared to what/whom? ")
        flag = 1
    if " less abeyant " in msgs:
        qtns.append(" less abeyant ")
        anss.append("less abeyant than what/whom? less abeyant compared to what/whom? ")
        flag = 1
    if " more abhorrent " in msgs:
        qtns.append(" more abhorrent ")
        anss.append("more abhorrent than what/whom? more abhorrent compared to what/whom? ")
        flag = 1
    if " less abhorrent " in msgs:
        qtns.append(" less abhorrent ")
        anss.append("less abhorrent than what/whom? less abhorrent compared to what/whom? ")
        flag = 1
    if " more abiding " in msgs:
        qtns.append(" more abiding ")
        anss.append("more abiding than what/whom? more abiding compared to what/whom? ")
        flag = 1
    if " less abiding " in msgs:
        qtns.append(" less abiding ")
        anss.append("less abiding than what/whom? less abiding compared to what/whom? ")
        flag = 1
    if " more abient " in msgs:
        qtns.append(" more abient ")
        anss.append("more abient than what/whom? more abient compared to what/whom? ")
        flag = 1
    if " less abient " in msgs:
        qtns.append(" less abient ")
        anss.append("less abient than what/whom? less abient compared to what/whom? ")
        flag = 1
    if " more abundant " in msgs:
        qtns.append(" more abundant ")
        anss.append("more abundant than what/whom? more abundant compared to what/whom? ")
        flag = 1
    if " less abundant " in msgs:
        qtns.append(" less abundant ")
        anss.append("less abundant than what/whom? less abundant compared to what/whom? ")
        flag = 1
    if " more accurate " in msgs:
        qtns.append(" more accurate ")
        anss.append("more accurate than what/whom? more accurate compared to what/whom? ")
        flag = 1
    if " less accurate " in msgs:
        qtns.append(" less accurate ")
        anss.append("less accurate than what/whom? less accurate compared to what/whom? ")
        flag = 1
    if " more addicted " in msgs:
        qtns.append(" more addicted ")
        anss.append("more addicted than what/whom? more addicted compared to what/whom? ")
        flag = 1
    if " less addicted " in msgs:
        qtns.append(" less addicted ")
        anss.append("less addicted than what/whom? less addicted compared to what/whom? ")
        flag = 1
    if " more adorable " in msgs:
        qtns.append(" more adorable ")
        anss.append("more adorable than what/whom? more adorable compared to what/whom? ")
        flag = 1
    if " less adorable " in msgs:
        qtns.append(" less adorable ")
        anss.append("less adorable than what/whom? less adorable compared to what/whom? ")
        flag = 1
    if " more adventurous " in msgs:
        qtns.append(" more adventurous ")
        anss.append("more adventurous than what/whom? more adventurous compared to what/whom? ")
        flag = 1
    if " less adventurous " in msgs:
        qtns.append(" less adventurous ")
        anss.append("less adventurous than what/whom? less adventurous compared to what/whom? ")
        flag = 1
    if " more afraid " in msgs:
        qtns.append(" more afraid ")
        anss.append("more afraid than what/whom? more afraid compared to what/whom? ")
        flag = 1
    if " less afraid " in msgs:
        qtns.append(" less afraid ")
        anss.append("less afraid than what/whom? less afraid compared to what/whom? ")
        flag = 1
    if " more aggressive " in msgs:
        qtns.append(" more aggressive ")
        anss.append("more aggressive than what/whom? more aggressive compared to what/whom? ")
        flag = 1
    if " less aggressive " in msgs:
        qtns.append(" less aggressive ")
        anss.append("less aggressive than what/whom? less aggressive compared to what/whom? ")
        flag = 1
    if " more alcoholic " in msgs:
        qtns.append(" more alcoholic ")
        anss.append("more alcoholic than what/whom? more alcoholic compared to what/whom? ")
        flag = 1
    if " less alcoholic " in msgs:
        qtns.append(" less alcoholic ")
        anss.append("less alcoholic than what/whom? less alcoholic compared to what/whom? ")
        flag = 1
    if " more alert " in msgs:
        qtns.append(" more alert ")
        anss.append("more alert than what/whom? more alert compared to what/whom? ")
        flag = 1
    if " less alert " in msgs:
        qtns.append(" less alert ")
        anss.append("less alert than what/whom? less alert compared to what/whom? ")
        flag = 1
    if " more aloof " in msgs:
        qtns.append(" more aloof ")
        anss.append("more aloof than what/whom? more aloof compared to what/whom? ")
        flag = 1
    if " less aloof " in msgs:
        qtns.append(" less aloof ")
        anss.append("less aloof than what/whom? less aloof compared to what/whom? ")
        flag = 1
    if " more ambitious " in msgs:
        qtns.append(" more ambitious ")
        anss.append("more ambitious than what/whom? more ambitious compared to what/whom? ")
        flag = 1
    if " less ambitious " in msgs:
        qtns.append(" less ambitious ")
        anss.append("less ambitious than what/whom? less ambitious compared to what/whom? ")
        flag = 1
    if " more ancient " in msgs:
        qtns.append(" more ancient ")
        anss.append("more ancient than what/whom? more ancient compared to what/whom? ")
        flag = 1
    if " less ancient " in msgs:
        qtns.append(" less ancient ")
        anss.append("less ancient than what/whom? less ancient compared to what/whom? ")
        flag = 1
    if " more angrier " in msgs:
        qtns.append(" more angrier ")
        anss.append("more angrier than what/whom? more angrier compared to what/whom? ")
        flag = 1
    if " less angrier " in msgs:
        qtns.append(" less angrier ")
        anss.append("less angrier than what/whom? less angrier compared to what/whom? ")
        flag = 1
    if " more animated " in msgs:
        qtns.append(" more animated ")
        anss.append("more animated than what/whom? more animated compared to what/whom? ")
        flag = 1
    if " less animated " in msgs:
        qtns.append(" less animated ")
        anss.append("less animated than what/whom? less animated compared to what/whom? ")
        flag = 1
    if " more annoying " in msgs:
        qtns.append(" more annoying ")
        anss.append("more annoying than what/whom? more annoying compared to what/whom? ")
        flag = 1
    if " less annoying " in msgs:
        qtns.append(" less annoying ")
        anss.append("less annoying than what/whom? less annoying compared to what/whom? ")
        flag = 1
    if " more anxious " in msgs:
        qtns.append(" more anxious ")
        anss.append("more anxious than what/whom? more anxious compared to what/whom? ")
        flag = 1
    if " less anxious " in msgs:
        qtns.append(" less anxious ")
        anss.append("less anxious than what/whom? less anxious compared to what/whom? ")
        flag = 1
    if " more arrogant " in msgs:
        qtns.append(" more arrogant ")
        anss.append("more arrogant than what/whom? more arrogant compared to what/whom? ")
        flag = 1
    if " less arrogant " in msgs:
        qtns.append(" less arrogant ")
        anss.append("less arrogant than what/whom? less arrogant compared to what/whom? ")
        flag = 1
    if " more ashamed " in msgs:
        qtns.append(" more ashamed ")
        anss.append("more ashamed than what/whom? more ashamed compared to what/whom? ")
        flag = 1
    if " less ashamed " in msgs:
        qtns.append(" less ashamed ")
        anss.append("less ashamed than what/whom? less ashamed compared to what/whom? ")
        flag = 1
    if " more attractive " in msgs:
        qtns.append(" more attractive ")
        anss.append("more attractive than what/whom? more attractive compared to what/whom? ")
        flag = 1
    if " less attractive " in msgs:
        qtns.append(" less attractive ")
        anss.append("less attractive than what/whom? less attractive compared to what/whom? ")
        flag = 1
    if " more auspicious " in msgs:
        qtns.append(" more auspicious ")
        anss.append("more auspicious than what/whom? more auspicious compared to what/whom? ")
        flag = 1
    if " less auspicious " in msgs:
        qtns.append(" less auspicious ")
        anss.append("less auspicious than what/whom? less auspicious compared to what/whom? ")
        flag = 1
    if " more awesome " in msgs:
        qtns.append(" more awesome ")
        anss.append("more awesome than what/whom? more awesome compared to what/whom? ")
        flag = 1
    if " less awesome " in msgs:
        qtns.append(" less awesome ")
        anss.append("less awesome than what/whom? less awesome compared to what/whom? ")
        flag = 1
    if " more awful " in msgs:
        qtns.append(" more awful ")
        anss.append("more awful than what/whom? more awful compared to what/whom? ")
        flag = 1
    if " less awful " in msgs:
        qtns.append(" less awful ")
        anss.append("less awful than what/whom? less awful compared to what/whom? ")
        flag = 1
    if " more badder " in msgs:
        qtns.append(" more badder ")
        anss.append("more badder than what/whom? more badder compared to what/whom? ")
        flag = 1
    if " less badder " in msgs:
        qtns.append(" less badder ")
        anss.append("less badder than what/whom? less badder compared to what/whom? ")
        flag = 1
    if " more worse " in msgs:
        qtns.append(" more worse ")
        anss.append("more worse than what/whom? more worse compared to what/whom? ")
        flag = 1
    if " less worse " in msgs:
        qtns.append(" less worse ")
        anss.append("less worse than what/whom? less worse compared to what/whom? ")
        flag = 1
    if " more barren " in msgs:
        qtns.append(" more barren ")
        anss.append("more barren than what/whom? more barren compared to what/whom? ")
        flag = 1
    if " less barren " in msgs:
        qtns.append(" less barren ")
        anss.append("less barren than what/whom? less barren compared to what/whom? ")
        flag = 1
    if " more barricaded " in msgs:
        qtns.append(" more barricaded ")
        anss.append("more barricaded than what/whom? more barricaded compared to what/whom? ")
        flag = 1
    if " less barricaded " in msgs:
        qtns.append(" less barricaded ")
        anss.append("less barricaded than what/whom? less barricaded compared to what/whom? ")
        flag = 1
    if " more barytic " in msgs:
        qtns.append(" more barytic ")
        anss.append("more barytic than what/whom? more barytic compared to what/whom? ")
        flag = 1
    if " less barytic " in msgs:
        qtns.append(" less barytic ")
        anss.append("less barytic than what/whom? less barytic compared to what/whom? ")
        flag = 1
    if " more basal " in msgs:
        qtns.append(" more basal ")
        anss.append("more basal than what/whom? more basal compared to what/whom? ")
        flag = 1
    if " less basal " in msgs:
        qtns.append(" less basal ")
        anss.append("less basal than what/whom? less basal compared to what/whom? ")
        flag = 1
    if " more basaltic " in msgs:
        qtns.append(" more basaltic ")
        anss.append("more basaltic than what/whom? more basaltic compared to what/whom? ")
        flag = 1
    if " less basaltic " in msgs:
        qtns.append(" less basaltic ")
        anss.append("less basaltic than what/whom? less basaltic compared to what/whom? ")
        flag = 1
    if " more baseborn " in msgs:
        qtns.append(" more baseborn ")
        anss.append("more baseborn than what/whom? more baseborn compared to what/whom? ")
        flag = 1
    if " less baseborn " in msgs:
        qtns.append(" less baseborn ")
        anss.append("less baseborn than what/whom? less baseborn compared to what/whom? ")
        flag = 1
    if " more based " in msgs:
        qtns.append(" more based ")
        anss.append("more based than what/whom? more based compared to what/whom? ")
        flag = 1
    if " less based " in msgs:
        qtns.append(" less based ")
        anss.append("less based than what/whom? less based compared to what/whom? ")
        flag = 1
    if " more baseless " in msgs:
        qtns.append(" more baseless ")
        anss.append("more baseless than what/whom? more baseless compared to what/whom? ")
        flag = 1
    if " less baseless " in msgs:
        qtns.append(" less baseless ")
        anss.append("less baseless than what/whom? less baseless compared to what/whom? ")
        flag = 1
    if " more bashful " in msgs:
        qtns.append(" more bashful ")
        anss.append("more bashful than what/whom? more bashful compared to what/whom? ")
        flag = 1
    if " less bashful " in msgs:
        qtns.append(" less bashful ")
        anss.append("less bashful than what/whom? less bashful compared to what/whom? ")
        flag = 1
    if " more basic " in msgs:
        qtns.append(" more basic ")
        anss.append("more basic than what/whom? more basic compared to what/whom? ")
        flag = 1
    if " less basic " in msgs:
        qtns.append(" less basic ")
        anss.append("less basic than what/whom? less basic compared to what/whom? ")
        flag = 1
    if " more bathyal " in msgs:
        qtns.append(" more bathyal ")
        anss.append("more bathyal than what/whom? more bathyal compared to what/whom? ")
        flag = 1
    if " less bathyal " in msgs:
        qtns.append(" less bathyal ")
        anss.append("less bathyal than what/whom? less bathyal compared to what/whom? ")
        flag = 1
    if " more battleful " in msgs:
        qtns.append(" more battleful ")
        anss.append("more battleful than what/whom? more battleful compared to what/whom? ")
        flag = 1
    if " less battleful " in msgs:
        qtns.append(" less battleful ")
        anss.append("less battleful than what/whom? less battleful compared to what/whom? ")
        flag = 1
    if " more battlemented " in msgs:
        qtns.append(" more battlemented ")
        anss.append("more battlemented than what/whom? more battlemented compared to what/whom? ")
        flag = 1
    if " less battlemented " in msgs:
        qtns.append(" less battlemented ")
        anss.append("less battlemented than what/whom? less battlemented compared to what/whom? ")
        flag = 1
    if " more batty " in msgs:
        qtns.append(" more batty ")
        anss.append("more batty than what/whom? more batty compared to what/whom? ")
        flag = 1
    if " less batty " in msgs:
        qtns.append(" less batty ")
        anss.append("less batty than what/whom? less batty compared to what/whom? ")
        flag = 1
    if " more batwing " in msgs:
        qtns.append(" more batwing ")
        anss.append("more batwing than what/whom? more batwing compared to what/whom? ")
        flag = 1
    if " less batwing " in msgs:
        qtns.append(" less batwing ")
        anss.append("less batwing than what/whom? less batwing compared to what/whom? ")
        flag = 1
    if " more beautiful " in msgs:
        qtns.append(" more beautiful ")
        anss.append("more beautiful than what/whom? more beautiful compared to what/whom? ")
        flag = 1
    if " less beautiful " in msgs:
        qtns.append(" less beautiful ")
        anss.append("less beautiful than what/whom? less beautiful compared to what/whom? ")
        flag = 1
    if " more belligerent " in msgs:
        qtns.append(" more belligerent ")
        anss.append("more belligerent than what/whom? more belligerent compared to what/whom? ")
        flag = 1
    if " less belligerent " in msgs:
        qtns.append(" less belligerent ")
        anss.append("less belligerent than what/whom? less belligerent compared to what/whom? ")
        flag = 1
    if " more beneficial " in msgs:
        qtns.append(" more beneficial ")
        anss.append("more beneficial than what/whom? more beneficial compared to what/whom? ")
        flag = 1
    if " less beneficial " in msgs:
        qtns.append(" less beneficial ")
        anss.append("less beneficial than what/whom? less beneficial compared to what/whom? ")
        flag = 1
    if " more biased " in msgs:
        qtns.append(" more biased ")
        anss.append("more biased than what/whom? more biased compared to what/whom? ")
        flag = 1
    if " less biased " in msgs:
        qtns.append(" less biased ")
        anss.append("less biased than what/whom? less biased compared to what/whom? ")
        flag = 1
    if " more bigger " in msgs:
        qtns.append(" more bigger ")
        anss.append("more bigger than what/whom? more bigger compared to what/whom? ")
        flag = 1
    if " less bigger " in msgs:
        qtns.append(" less bigger ")
        anss.append("less bigger than what/whom? less bigger compared to what/whom? ")
        flag = 1
    if " more bitter " in msgs:
        qtns.append(" more bitter ")
        anss.append("more bitter than what/whom? more bitter compared to what/whom? ")
        flag = 1
    if " less bitter " in msgs:
        qtns.append(" less bitter ")
        anss.append("less bitter than what/whom? less bitter compared to what/whom? ")
        flag = 1
    if " more bitterer " in msgs:
        qtns.append(" more bitterer ")
        anss.append("more bitterer than what/whom? more bitterer compared to what/whom? ")
        flag = 1
    if " less bitterer " in msgs:
        qtns.append(" less bitterer ")
        anss.append("less bitterer than what/whom? less bitterer compared to what/whom? ")
        flag = 1
    if " more bizarre " in msgs:
        qtns.append(" more bizarre ")
        anss.append("more bizarre than what/whom? more bizarre compared to what/whom? ")
        flag = 1
    if " less bizarre " in msgs:
        qtns.append(" less bizarre ")
        anss.append("less bizarre than what/whom? less bizarre compared to what/whom? ")
        flag = 1
    if " more blacker " in msgs:
        qtns.append(" more blacker ")
        anss.append("more blacker than what/whom? more blacker compared to what/whom? ")
        flag = 1
    if " less blacker " in msgs:
        qtns.append(" less blacker ")
        anss.append("less blacker than what/whom? less blacker compared to what/whom? ")
        flag = 1
    if " more blander " in msgs:
        qtns.append(" more blander ")
        anss.append("more blander than what/whom? more blander compared to what/whom? ")
        flag = 1
    if " less blander " in msgs:
        qtns.append(" less blander ")
        anss.append("less blander than what/whom? less blander compared to what/whom? ")
        flag = 1
    if " more bloodier " in msgs:
        qtns.append(" more bloodier ")
        anss.append("more bloodier than what/whom? more bloodier compared to what/whom? ")
        flag = 1
    if " less bloodier " in msgs:
        qtns.append(" less bloodier ")
        anss.append("less bloodier than what/whom? less bloodier compared to what/whom? ")
        flag = 1
    if " more bluer " in msgs:
        qtns.append(" more bluer ")
        anss.append("more bluer than what/whom? more bluer compared to what/whom? ")
        flag = 1
    if " less bluer " in msgs:
        qtns.append(" less bluer ")
        anss.append("less bluer than what/whom? less bluer compared to what/whom? ")
        flag = 1
    if " more bolder " in msgs:
        qtns.append(" more bolder ")
        anss.append("more bolder than what/whom? more bolder compared to what/whom? ")
        flag = 1
    if " less bolder " in msgs:
        qtns.append(" less bolder ")
        anss.append("less bolder than what/whom? less bolder compared to what/whom? ")
        flag = 1
    if " more boring " in msgs:
        qtns.append(" more boring ")
        anss.append("more boring than what/whom? more boring compared to what/whom? ")
        flag = 1
    if " less boring " in msgs:
        qtns.append(" less boring ")
        anss.append("less boring than what/whom? less boring compared to what/whom? ")
        flag = 1
    if " more bossier " in msgs:
        qtns.append(" more bossier ")
        anss.append("more bossier than what/whom? more bossier compared to what/whom? ")
        flag = 1
    if " less bossier " in msgs:
        qtns.append(" less bossier ")
        anss.append("less bossier than what/whom? less bossier compared to what/whom? ")
        flag = 1
    if " more brainy " in msgs:
        qtns.append(" more brainy ")
        anss.append("more brainy than what/whom? more brainy compared to what/whom? ")
        flag = 1
    if " less brainy " in msgs:
        qtns.append(" less brainy ")
        anss.append("less brainy than what/whom? less brainy compared to what/whom? ")
        flag = 1
    if " more brainier " in msgs:
        qtns.append(" more brainier ")
        anss.append("more brainier than what/whom? more brainier compared to what/whom? ")
        flag = 1
    if " less brainier " in msgs:
        qtns.append(" less brainier ")
        anss.append("less brainier than what/whom? less brainier compared to what/whom? ")
        flag = 1
    if " more braver " in msgs:
        qtns.append(" more braver ")
        anss.append("more braver than what/whom? more braver compared to what/whom? ")
        flag = 1
    if " less braver " in msgs:
        qtns.append(" less braver ")
        anss.append("less braver than what/whom? less braver compared to what/whom? ")
        flag = 1
    if " more briefer " in msgs:
        qtns.append(" more briefer ")
        anss.append("more briefer than what/whom? more briefer compared to what/whom? ")
        flag = 1
    if " less briefer " in msgs:
        qtns.append(" less briefer ")
        anss.append("less briefer than what/whom? less briefer compared to what/whom? ")
        flag = 1
    if " more brighter " in msgs:
        qtns.append(" more brighter ")
        anss.append("more brighter than what/whom? more brighter compared to what/whom? ")
        flag = 1
    if " less brighter " in msgs:
        qtns.append(" less brighter ")
        anss.append("less brighter than what/whom? less brighter compared to what/whom? ")
        flag = 1
    if " more broader " in msgs:
        qtns.append(" more broader ")
        anss.append("more broader than what/whom? more broader compared to what/whom? ")
        flag = 1
    if " less broader " in msgs:
        qtns.append(" less broader ")
        anss.append("less broader than what/whom? less broader compared to what/whom? ")
        flag = 1
    if " more broken " in msgs:
        qtns.append(" more broken ")
        anss.append("more broken than what/whom? more broken compared to what/whom? ")
        flag = 1
    if " less broken " in msgs:
        qtns.append(" less broken ")
        anss.append("less broken than what/whom? less broken compared to what/whom? ")
        flag = 1
    if " more busier " in msgs:
        qtns.append(" more busier ")
        anss.append("more busier than what/whom? more busier compared to what/whom? ")
        flag = 1
    if " less busier " in msgs:
        qtns.append(" less busier ")
        anss.append("less busier than what/whom? less busier compared to what/whom? ")
        flag = 1
    if " more calmer " in msgs:
        qtns.append(" more calmer ")
        anss.append("more calmer than what/whom? more calmer compared to what/whom? ")
        flag = 1
    if " less calmer " in msgs:
        qtns.append(" less calmer ")
        anss.append("less calmer than what/whom? less calmer compared to what/whom? ")
        flag = 1
    if " more capable " in msgs:
        qtns.append(" more capable ")
        anss.append("more capable than what/whom? more capable compared to what/whom? ")
        flag = 1
    if " less capable " in msgs:
        qtns.append(" less capable ")
        anss.append("less capable than what/whom? less capable compared to what/whom? ")
        flag = 1
    if " more careful " in msgs:
        qtns.append(" more careful ")
        anss.append("more careful than what/whom? more careful compared to what/whom? ")
        flag = 1
    if " less careful " in msgs:
        qtns.append(" less careful ")
        anss.append("less careful than what/whom? less careful compared to what/whom? ")
        flag = 1
    if " more careless " in msgs:
        qtns.append(" more careless ")
        anss.append("more careless than what/whom? more careless compared to what/whom? ")
        flag = 1
    if " less careless " in msgs:
        qtns.append(" less careless ")
        anss.append("less careless than what/whom? less careless compared to what/whom? ")
        flag = 1
    if " more caring " in msgs:
        qtns.append(" more caring ")
        anss.append("more caring than what/whom? more caring compared to what/whom? ")
        flag = 1
    if " less caring " in msgs:
        qtns.append(" less caring ")
        anss.append("less caring than what/whom? less caring compared to what/whom? ")
        flag = 1
    if " more cautious " in msgs:
        qtns.append(" more cautious ")
        anss.append("more cautious than what/whom? more cautious compared to what/whom? ")
        flag = 1
    if " less cautious " in msgs:
        qtns.append(" less cautious ")
        anss.append("less cautious than what/whom? less cautious compared to what/whom? ")
        flag = 1
    if " more charming " in msgs:
        qtns.append(" more charming ")
        anss.append("more charming than what/whom? more charming compared to what/whom? ")
        flag = 1
    if " less charming " in msgs:
        qtns.append(" less charming ")
        anss.append("less charming than what/whom? less charming compared to what/whom? ")
        flag = 1
    if " more cheaper " in msgs:
        qtns.append(" more cheaper ")
        anss.append("more cheaper than what/whom? more cheaper compared to what/whom? ")
        flag = 1
    if " less cheaper " in msgs:
        qtns.append(" less cheaper ")
        anss.append("less cheaper than what/whom? less cheaper compared to what/whom? ")
        flag = 1
    if " more cheerful " in msgs:
        qtns.append(" more cheerful ")
        anss.append("more cheerful than what/whom? more cheerful compared to what/whom? ")
        flag = 1
    if " less cheerful " in msgs:
        qtns.append(" less cheerful ")
        anss.append("less cheerful than what/whom? less cheerful compared to what/whom? ")
        flag = 1
    if " more chewier " in msgs:
        qtns.append(" more chewier ")
        anss.append("more chewier than what/whom? more chewier compared to what/whom? ")
        flag = 1
    if " less chewier " in msgs:
        qtns.append(" less chewier ")
        anss.append("less chewier than what/whom? less chewier compared to what/whom? ")
        flag = 1
    if " more chubbier " in msgs:
        qtns.append(" more chubbier ")
        anss.append("more chubbier than what/whom? more chubbier compared to what/whom? ")
        flag = 1
    if " less chubbier " in msgs:
        qtns.append(" less chubbier ")
        anss.append("less chubbier than what/whom? less chubbier compared to what/whom? ")
        flag = 1
    if " more classier " in msgs:
        qtns.append(" more classier ")
        anss.append("more classier than what/whom? more classier compared to what/whom? ")
        flag = 1
    if " less classier " in msgs:
        qtns.append(" less classier ")
        anss.append("less classier than what/whom? less classier compared to what/whom? ")
        flag = 1
    if " more cleaner " in msgs:
        qtns.append(" more cleaner ")
        anss.append("more cleaner than what/whom? more cleaner compared to what/whom? ")
        flag = 1
    if " less cleaner " in msgs:
        qtns.append(" less cleaner ")
        anss.append("less cleaner than what/whom? less cleaner compared to what/whom? ")
        flag = 1
    if " more clearer " in msgs:
        qtns.append(" more clearer ")
        anss.append("more clearer than what/whom? more clearer compared to what/whom? ")
        flag = 1
    if " less clearer " in msgs:
        qtns.append(" less clearer ")
        anss.append("less clearer than what/whom? less clearer compared to what/whom? ")
        flag = 1
    if " more cleverer " in msgs:
        qtns.append(" more cleverer ")
        anss.append("more cleverer than what/whom? more cleverer compared to what/whom? ")
        flag = 1
    if " less cleverer " in msgs:
        qtns.append(" less cleverer ")
        anss.append("less cleverer than what/whom? less cleverer compared to what/whom? ")
        flag = 1
    if " more closer " in msgs:
        qtns.append(" more closer ")
        anss.append("more closer than what/whom? more closer compared to what/whom? ")
        flag = 1
    if " less closer " in msgs:
        qtns.append(" less closer ")
        anss.append("less closer than what/whom? less closer compared to what/whom? ")
        flag = 1
    if " more cloudier " in msgs:
        qtns.append(" more cloudier ")
        anss.append("more cloudier than what/whom? more cloudier compared to what/whom? ")
        flag = 1
    if " less cloudier " in msgs:
        qtns.append(" less cloudier ")
        anss.append("less cloudier than what/whom? less cloudier compared to what/whom? ")
        flag = 1
    if " more clumsier " in msgs:
        qtns.append(" more clumsier ")
        anss.append("more clumsier than what/whom? more clumsier compared to what/whom? ")
        flag = 1
    if " less clumsier " in msgs:
        qtns.append(" less clumsier ")
        anss.append("less clumsier than what/whom? less clumsier compared to what/whom? ")
        flag = 1
    if " more coarser " in msgs:
        qtns.append(" more coarser ")
        anss.append("more coarser than what/whom? more coarser compared to what/whom? ")
        flag = 1
    if " less coarser " in msgs:
        qtns.append(" less coarser ")
        anss.append("less coarser than what/whom? less coarser compared to what/whom? ")
        flag = 1
    if " more colder " in msgs:
        qtns.append(" more colder ")
        anss.append("more colder than what/whom? more colder compared to what/whom? ")
        flag = 1
    if " less colder " in msgs:
        qtns.append(" less colder ")
        anss.append("less colder than what/whom? less colder compared to what/whom? ")
        flag = 1
    if " more colorful " in msgs:
        qtns.append(" more colorful ")
        anss.append("more colorful than what/whom? more colorful compared to what/whom? ")
        flag = 1
    if " less colorful " in msgs:
        qtns.append(" less colorful ")
        anss.append("less colorful than what/whom? less colorful compared to what/whom? ")
        flag = 1
    if " more comfortable " in msgs:
        qtns.append(" more comfortable ")
        anss.append("more comfortable than what/whom? more comfortable compared to what/whom? ")
        flag = 1
    if " less comfortable " in msgs:
        qtns.append(" less comfortable ")
        anss.append("less comfortable than what/whom? less comfortable compared to what/whom? ")
        flag = 1
    if " more concerned " in msgs:
        qtns.append(" more concerned ")
        anss.append("more concerned than what/whom? more concerned compared to what/whom? ")
        flag = 1
    if " less concerned " in msgs:
        qtns.append(" less concerned ")
        anss.append("less concerned than what/whom? less concerned compared to what/whom? ")
        flag = 1
    if " more confused " in msgs:
        qtns.append(" more confused ")
        anss.append("more confused than what/whom? more confused compared to what/whom? ")
        flag = 1
    if " less confused " in msgs:
        qtns.append(" less confused ")
        anss.append("less confused than what/whom? less confused compared to what/whom? ")
        flag = 1
    if " more consistent " in msgs:
        qtns.append(" more consistent ")
        anss.append("more consistent than what/whom? more consistent compared to what/whom? ")
        flag = 1
    if " less consistent " in msgs:
        qtns.append(" less consistent ")
        anss.append("less consistent than what/whom? less consistent compared to what/whom? ")
        flag = 1
    if " more cooler " in msgs:
        qtns.append(" more cooler ")
        anss.append("more cooler than what/whom? more cooler compared to what/whom? ")
        flag = 1
    if " less cooler " in msgs:
        qtns.append(" less cooler ")
        anss.append("less cooler than what/whom? less cooler compared to what/whom? ")
        flag = 1
    if " more crazier " in msgs:
        qtns.append(" more crazier ")
        anss.append("more crazier than what/whom? more crazier compared to what/whom? ")
        flag = 1
    if " less crazier " in msgs:
        qtns.append(" less crazier ")
        anss.append("less crazier than what/whom? less crazier compared to what/whom? ")
        flag = 1
    if " more creamier " in msgs:
        qtns.append(" more creamier ")
        anss.append("more creamier than what/whom? more creamier compared to what/whom? ")
        flag = 1
    if " less creamier " in msgs:
        qtns.append(" less creamier ")
        anss.append("less creamier than what/whom? less creamier compared to what/whom? ")
        flag = 1
    if " more creepier " in msgs:
        qtns.append(" more creepier ")
        anss.append("more creepier than what/whom? more creepier compared to what/whom? ")
        flag = 1
    if " less creepier " in msgs:
        qtns.append(" less creepier ")
        anss.append("less creepier than what/whom? less creepier compared to what/whom? ")
        flag = 1
    if " more crispier " in msgs:
        qtns.append(" more crispier ")
        anss.append("more crispier than what/whom? more crispier compared to what/whom? ")
        flag = 1
    if " less crispier " in msgs:
        qtns.append(" less crispier ")
        anss.append("less crispier than what/whom? less crispier compared to what/whom? ")
        flag = 1
    if " more crowded " in msgs:
        qtns.append(" more crowded ")
        anss.append("more crowded than what/whom? more crowded compared to what/whom? ")
        flag = 1
    if " less crowded " in msgs:
        qtns.append(" less crowded ")
        anss.append("less crowded than what/whom? less crowded compared to what/whom? ")
        flag = 1
    if " more crueler " in msgs:
        qtns.append(" more crueler ")
        anss.append("more crueler than what/whom? more crueler compared to what/whom? ")
        flag = 1
    if " less crueler " in msgs:
        qtns.append(" less crueler ")
        anss.append("less crueler than what/whom? less crueler compared to what/whom? ")
        flag = 1
    if " more crunchier " in msgs:
        qtns.append(" more crunchier ")
        anss.append("more crunchier than what/whom? more crunchier compared to what/whom? ")
        flag = 1
    if " less crunchier " in msgs:
        qtns.append(" less crunchier ")
        anss.append("less crunchier than what/whom? less crunchier compared to what/whom? ")
        flag = 1
    if " more curious " in msgs:
        qtns.append(" more curious ")
        anss.append("more curious than what/whom? more curious compared to what/whom? ")
        flag = 1
    if " less curious " in msgs:
        qtns.append(" less curious ")
        anss.append("less curious than what/whom? less curious compared to what/whom? ")
        flag = 1
    if " more curlier " in msgs:
        qtns.append(" more curlier ")
        anss.append("more curlier than what/whom? more curlier compared to what/whom? ")
        flag = 1
    if " less curlier " in msgs:
        qtns.append(" less curlier ")
        anss.append("less curlier than what/whom? less curlier compared to what/whom? ")
        flag = 1
    if " more curvier " in msgs:
        qtns.append(" more curvier ")
        anss.append("more curvier than what/whom? more curvier compared to what/whom? ")
        flag = 1
    if " less curvier " in msgs:
        qtns.append(" less curvier ")
        anss.append("less curvier than what/whom? less curvier compared to what/whom? ")
        flag = 1
    if " more cuter " in msgs:
        qtns.append(" more cuter ")
        anss.append("more cuter than what/whom? more cuter compared to what/whom? ")
        flag = 1
    if " less cuter " in msgs:
        qtns.append(" less cuter ")
        anss.append("less cuter than what/whom? less cuter compared to what/whom? ")
        flag = 1
    if " more dafter " in msgs:
        qtns.append(" more dafter ")
        anss.append("more dafter than what/whom? more dafter compared to what/whom? ")
        flag = 1
    if " less dafter " in msgs:
        qtns.append(" less dafter ")
        anss.append("less dafter than what/whom? less dafter compared to what/whom? ")
        flag = 1
    if " more daily " in msgs:
        qtns.append(" more daily ")
        anss.append("more daily than what/whom? more daily compared to what/whom? ")
        flag = 1
    if " less daily " in msgs:
        qtns.append(" less daily ")
        anss.append("less daily than what/whom? less daily compared to what/whom? ")
        flag = 1
    if " more dainty " in msgs:
        qtns.append(" more dainty ")
        anss.append("more dainty than what/whom? more dainty compared to what/whom? ")
        flag = 1
    if " less dainty " in msgs:
        qtns.append(" less dainty ")
        anss.append("less dainty than what/whom? less dainty compared to what/whom? ")
        flag = 1
    if " more damaged " in msgs:
        qtns.append(" more damaged ")
        anss.append("more damaged than what/whom? more damaged compared to what/whom? ")
        flag = 1
    if " less damaged " in msgs:
        qtns.append(" less damaged ")
        anss.append("less damaged than what/whom? less damaged compared to what/whom? ")
        flag = 1
    if " more damn " in msgs:
        qtns.append(" more damn ")
        anss.append("more damn than what/whom? more damn compared to what/whom? ")
        flag = 1
    if " less damn " in msgs:
        qtns.append(" less damn ")
        anss.append("less damn than what/whom? less damn compared to what/whom? ")
        flag = 1
    if " more damning " in msgs:
        qtns.append(" more damning ")
        anss.append("more damning than what/whom? more damning compared to what/whom? ")
        flag = 1
    if " less damning " in msgs:
        qtns.append(" less damning ")
        anss.append("less damning than what/whom? less damning compared to what/whom? ")
        flag = 1
    if " more damper " in msgs:
        qtns.append(" more damper ")
        anss.append("more damper than what/whom? more damper compared to what/whom? ")
        flag = 1
    if " less damper " in msgs:
        qtns.append(" less damper ")
        anss.append("less damper than what/whom? less damper compared to what/whom? ")
        flag = 1
    if " more dampish " in msgs:
        qtns.append(" more dampish ")
        anss.append("more dampish than what/whom? more dampish compared to what/whom? ")
        flag = 1
    if " less dampish " in msgs:
        qtns.append(" less dampish ")
        anss.append("less dampish than what/whom? less dampish compared to what/whom? ")
        flag = 1
    if " more dangerous " in msgs:
        qtns.append(" more dangerous ")
        anss.append("more dangerous than what/whom? more dangerous compared to what/whom? ")
        flag = 1
    if " less dangerous " in msgs:
        qtns.append(" less dangerous ")
        anss.append("less dangerous than what/whom? less dangerous compared to what/whom? ")
        flag = 1
    if " more darker " in msgs:
        qtns.append(" more darker ")
        anss.append("more darker than what/whom? more darker compared to what/whom? ")
        flag = 1
    if " less darker " in msgs:
        qtns.append(" less darker ")
        anss.append("less darker than what/whom? less darker compared to what/whom? ")
        flag = 1
    if " more darkling " in msgs:
        qtns.append(" more darkling ")
        anss.append("more darkling than what/whom? more darkling compared to what/whom? ")
        flag = 1
    if " less darkling " in msgs:
        qtns.append(" less darkling ")
        anss.append("less darkling than what/whom? less darkling compared to what/whom? ")
        flag = 1
    if " more darned " in msgs:
        qtns.append(" more darned ")
        anss.append("more darned than what/whom? more darned compared to what/whom? ")
        flag = 1
    if " less darned " in msgs:
        qtns.append(" less darned ")
        anss.append("less darned than what/whom? less darned compared to what/whom? ")
        flag = 1
    if " more dauntless " in msgs:
        qtns.append(" more dauntless ")
        anss.append("more dauntless than what/whom? more dauntless compared to what/whom? ")
        flag = 1
    if " less dauntless " in msgs:
        qtns.append(" less dauntless ")
        anss.append("less dauntless than what/whom? less dauntless compared to what/whom? ")
        flag = 1
    if " more daylong " in msgs:
        qtns.append(" more daylong ")
        anss.append("more daylong than what/whom? more daylong compared to what/whom? ")
        flag = 1
    if " less daylong " in msgs:
        qtns.append(" less daylong ")
        anss.append("less daylong than what/whom? less daylong compared to what/whom? ")
        flag = 1
    if " more deadlier " in msgs:
        qtns.append(" more deadlier ")
        anss.append("more deadlier than what/whom? more deadlier compared to what/whom? ")
        flag = 1
    if " less deadlier " in msgs:
        qtns.append(" less deadlier ")
        anss.append("less deadlier than what/whom? less deadlier compared to what/whom? ")
        flag = 1
    if " more deeper " in msgs:
        qtns.append(" more deeper ")
        anss.append("more deeper than what/whom? more deeper compared to what/whom? ")
        flag = 1
    if " less deeper " in msgs:
        qtns.append(" less deeper ")
        anss.append("less deeper than what/whom? less deeper compared to what/whom? ")
        flag = 1
    if " more defective " in msgs:
        qtns.append(" more defective ")
        anss.append("more defective than what/whom? more defective compared to what/whom? ")
        flag = 1
    if " less defective " in msgs:
        qtns.append(" less defective ")
        anss.append("less defective than what/whom? less defective compared to what/whom? ")
        flag = 1
    if " more delicate " in msgs:
        qtns.append(" more delicate ")
        anss.append("more delicate than what/whom? more delicate compared to what/whom? ")
        flag = 1
    if " less delicate " in msgs:
        qtns.append(" less delicate ")
        anss.append("less delicate than what/whom? less delicate compared to what/whom? ")
        flag = 1
    if " more delicious " in msgs:
        qtns.append(" more delicious ")
        anss.append("more delicious than what/whom? more delicious compared to what/whom? ")
        flag = 1
    if " less delicious " in msgs:
        qtns.append(" less delicious ")
        anss.append("less delicious than what/whom? less delicious compared to what/whom? ")
        flag = 1
    if " more denser " in msgs:
        qtns.append(" more denser ")
        anss.append("more denser than what/whom? more denser compared to what/whom? ")
        flag = 1
    if " less denser " in msgs:
        qtns.append(" less denser ")
        anss.append("less denser than what/whom? less denser compared to what/whom? ")
        flag = 1
    if " more depressed " in msgs:
        qtns.append(" more depressed ")
        anss.append("more depressed than what/whom? more depressed compared to what/whom? ")
        flag = 1
    if " less depressed " in msgs:
        qtns.append(" less depressed ")
        anss.append("less depressed than what/whom? less depressed compared to what/whom? ")
        flag = 1
    if " more determined " in msgs:
        qtns.append(" more determined ")
        anss.append("more determined than what/whom? more determined compared to what/whom? ")
        flag = 1
    if " less determined " in msgs:
        qtns.append(" less determined ")
        anss.append("less determined than what/whom? less determined compared to what/whom? ")
        flag = 1
    if " more different " in msgs:
        qtns.append(" more different ")
        anss.append("more different than what/whom? more different compared to what/whom? ")
        flag = 1
    if " less different " in msgs:
        qtns.append(" less different ")
        anss.append("less different than what/whom? less different compared to what/whom? ")
        flag = 1
    if " more difficult " in msgs:
        qtns.append(" more difficult ")
        anss.append("more difficult than what/whom? more difficult compared to what/whom? ")
        flag = 1
    if " less difficult " in msgs:
        qtns.append(" less difficult ")
        anss.append("less difficult than what/whom? less difficult compared to what/whom? ")
        flag = 1
    if " more dirtier " in msgs:
        qtns.append(" more dirtier ")
        anss.append("more dirtier than what/whom? more dirtier compared to what/whom? ")
        flag = 1
    if " less dirtier " in msgs:
        qtns.append(" less dirtier ")
        anss.append("less dirtier than what/whom? less dirtier compared to what/whom? ")
        flag = 1
    if " more disgusting " in msgs:
        qtns.append(" more disgusting ")
        anss.append("more disgusting than what/whom? more disgusting compared to what/whom? ")
        flag = 1
    if " less disgusting " in msgs:
        qtns.append(" less disgusting ")
        anss.append("less disgusting than what/whom? less disgusting compared to what/whom? ")
        flag = 1
    if " more drier " in msgs:
        qtns.append(" more drier ")
        anss.append("more drier than what/whom? more drier compared to what/whom? ")
        flag = 1
    if " less drier " in msgs:
        qtns.append(" less drier ")
        anss.append("less drier than what/whom? less drier compared to what/whom? ")
        flag = 1
    if " more duller " in msgs:
        qtns.append(" more duller ")
        anss.append("more duller than what/whom? more duller compared to what/whom? ")
        flag = 1
    if " less duller " in msgs:
        qtns.append(" less duller ")
        anss.append("less duller than what/whom? less duller compared to what/whom? ")
        flag = 1
    if " more dumber " in msgs:
        qtns.append(" more dumber ")
        anss.append("more dumber than what/whom? more dumber compared to what/whom? ")
        flag = 1
    if " less dumber " in msgs:
        qtns.append(" less dumber ")
        anss.append("less dumber than what/whom? less dumber compared to what/whom? ")
        flag = 1
    if " more dustier " in msgs:
        qtns.append(" more dustier ")
        anss.append("more dustier than what/whom? more dustier compared to what/whom? ")
        flag = 1
    if " less dustier " in msgs:
        qtns.append(" less dustier ")
        anss.append("less dustier than what/whom? less dustier compared to what/whom? ")
        flag = 1
    if " more earlier " in msgs:
        qtns.append(" more earlier ")
        anss.append("more earlier than what/whom? more earlier compared to what/whom? ")
        flag = 1
    if " less earlier " in msgs:
        qtns.append(" less earlier ")
        anss.append("less earlier than what/whom? less earlier compared to what/whom? ")
        flag = 1
    if " more easier " in msgs:
        qtns.append(" more easier ")
        anss.append("more easier than what/whom? more easier compared to what/whom? ")
        flag = 1
    if " less easier " in msgs:
        qtns.append(" less easier ")
        anss.append("less easier than what/whom? less easier compared to what/whom? ")
        flag = 1
    if " more educated " in msgs:
        qtns.append(" more educated ")
        anss.append("more educated than what/whom? more educated compared to what/whom? ")
        flag = 1
    if " less educated " in msgs:
        qtns.append(" less educated ")
        anss.append("less educated than what/whom? less educated compared to what/whom? ")
        flag = 1
    if " more efficient " in msgs:
        qtns.append(" more efficient ")
        anss.append("more efficient than what/whom? more efficient compared to what/whom? ")
        flag = 1
    if " less efficient " in msgs:
        qtns.append(" less efficient ")
        anss.append("less efficient than what/whom? less efficient compared to what/whom? ")
        flag = 1
    if " more elderly " in msgs:
        qtns.append(" more elderly ")
        anss.append("more elderly than what/whom? more elderly compared to what/whom? ")
        flag = 1
    if " less elderly " in msgs:
        qtns.append(" less elderly ")
        anss.append("less elderly than what/whom? less elderly compared to what/whom? ")
        flag = 1
    if " more elegant " in msgs:
        qtns.append(" more elegant ")
        anss.append("more elegant than what/whom? more elegant compared to what/whom? ")
        flag = 1
    if " less elegant " in msgs:
        qtns.append(" less elegant ")
        anss.append("less elegant than what/whom? less elegant compared to what/whom? ")
        flag = 1
    if " more embarrassed " in msgs:
        qtns.append(" more embarrassed ")
        anss.append("more embarrassed than what/whom? more embarrassed compared to what/whom? ")
        flag = 1
    if " less embarrassed " in msgs:
        qtns.append(" less embarrassed ")
        anss.append("less embarrassed than what/whom? less embarrassed compared to what/whom? ")
        flag = 1
    if " more emptier " in msgs:
        qtns.append(" more emptier ")
        anss.append("more emptier than what/whom? more emptier compared to what/whom? ")
        flag = 1
    if " less emptier " in msgs:
        qtns.append(" less emptier ")
        anss.append("less emptier than what/whom? less emptier compared to what/whom? ")
        flag = 1
    if " more encouraging " in msgs:
        qtns.append(" more encouraging ")
        anss.append("more encouraging than what/whom? more encouraging compared to what/whom? ")
        flag = 1
    if " less encouraging " in msgs:
        qtns.append(" less encouraging ")
        anss.append("less encouraging than what/whom? less encouraging compared to what/whom? ")
        flag = 1
    if " more enthusiastic " in msgs:
        qtns.append(" more enthusiastic ")
        anss.append("more enthusiastic than what/whom? more enthusiastic compared to what/whom? ")
        flag = 1
    if " less enthusiastic " in msgs:
        qtns.append(" less enthusiastic ")
        anss.append("less enthusiastic than what/whom? less enthusiastic compared to what/whom? ")
        flag = 1
    if " more excellent " in msgs:
        qtns.append(" more excellent ")
        anss.append("more excellent than what/whom? more excellent compared to what/whom? ")
        flag = 1
    if " less excellent " in msgs:
        qtns.append(" less excellent ")
        anss.append("less excellent than what/whom? less excellent compared to what/whom? ")
        flag = 1
    if " more exciting " in msgs:
        qtns.append(" more exciting ")
        anss.append("more exciting than what/whom? more exciting compared to what/whom? ")
        flag = 1
    if " less exciting " in msgs:
        qtns.append(" less exciting ")
        anss.append("less exciting than what/whom? less exciting compared to what/whom? ")
        flag = 1
    if " more expensive " in msgs:
        qtns.append(" more expensive ")
        anss.append("more expensive than what/whom? more expensive compared to what/whom? ")
        flag = 1
    if " less expensive " in msgs:
        qtns.append(" less expensive ")
        anss.append("less expensive than what/whom? less expensive compared to what/whom? ")
        flag = 1
    if " more fabulous " in msgs:
        qtns.append(" more fabulous ")
        anss.append("more fabulous than what/whom? more fabulous compared to what/whom? ")
        flag = 1
    if " less fabulous " in msgs:
        qtns.append(" less fabulous ")
        anss.append("less fabulous than what/whom? less fabulous compared to what/whom? ")
        flag = 1
    if " more fainter " in msgs:
        qtns.append(" more fainter ")
        anss.append("more fainter than what/whom? more fainter compared to what/whom? ")
        flag = 1
    if " less fainter " in msgs:
        qtns.append(" less fainter ")
        anss.append("less fainter than what/whom? less fainter compared to what/whom? ")
        flag = 1
    if " more fairer " in msgs:
        qtns.append(" more fairer ")
        anss.append("more fairer than what/whom? more fairer compared to what/whom? ")
        flag = 1
    if " less fairer " in msgs:
        qtns.append(" less fairer ")
        anss.append("less fairer than what/whom? less fairer compared to what/whom? ")
        flag = 1
    if " more faithful " in msgs:
        qtns.append(" more faithful ")
        anss.append("more faithful than what/whom? more faithful compared to what/whom? ")
        flag = 1
    if " less faithful " in msgs:
        qtns.append(" less faithful ")
        anss.append("less faithful than what/whom? less faithful compared to what/whom? ")
        flag = 1
    if " more famous " in msgs:
        qtns.append(" more famous ")
        anss.append("more famous than what/whom? more famous compared to what/whom? ")
        flag = 1
    if " less famous " in msgs:
        qtns.append(" less famous ")
        anss.append("less famous than what/whom? less famous compared to what/whom? ")
        flag = 1
    if " more fancier " in msgs:
        qtns.append(" more fancier ")
        anss.append("more fancier than what/whom? more fancier compared to what/whom? ")
        flag = 1
    if " less fancier " in msgs:
        qtns.append(" less fancier ")
        anss.append("less fancier than what/whom? less fancier compared to what/whom? ")
        flag = 1
    if " more fantastic " in msgs:
        qtns.append(" more fantastic ")
        anss.append("more fantastic than what/whom? more fantastic compared to what/whom? ")
        flag = 1
    if " less fantastic " in msgs:
        qtns.append(" less fantastic ")
        anss.append("less fantastic than what/whom? less fantastic compared to what/whom? ")
        flag = 1
    if " more farther " in msgs:
        qtns.append(" more farther ")
        anss.append("more farther than what/whom? more farther compared to what/whom? ")
        flag = 1
    if " less farther " in msgs:
        qtns.append(" less farther ")
        anss.append("less farther than what/whom? less farther compared to what/whom? ")
        flag = 1
    if " more faster " in msgs:
        qtns.append(" more faster ")
        anss.append("more faster than what/whom? more faster compared to what/whom? ")
        flag = 1
    if " less faster " in msgs:
        qtns.append(" less faster ")
        anss.append("less faster than what/whom? less faster compared to what/whom? ")
        flag = 1
    if " more fatter " in msgs:
        qtns.append(" more fatter ")
        anss.append("more fatter than what/whom? more fatter compared to what/whom? ")
        flag = 1
    if " less fatter " in msgs:
        qtns.append(" less fatter ")
        anss.append("less fatter than what/whom? less fatter compared to what/whom? ")
        flag = 1
    if " more fearful " in msgs:
        qtns.append(" more fearful ")
        anss.append("more fearful than what/whom? more fearful compared to what/whom? ")
        flag = 1
    if " less fearful " in msgs:
        qtns.append(" less fearful ")
        anss.append("less fearful than what/whom? less fearful compared to what/whom? ")
        flag = 1
    if " more fearless " in msgs:
        qtns.append(" more fearless ")
        anss.append("more fearless than what/whom? more fearless compared to what/whom? ")
        flag = 1
    if " less fearless " in msgs:
        qtns.append(" less fearless ")
        anss.append("less fearless than what/whom? less fearless compared to what/whom? ")
        flag = 1
    if " more fertile " in msgs:
        qtns.append(" more fertile ")
        anss.append("more fertile than what/whom? more fertile compared to what/whom? ")
        flag = 1
    if " less fertile " in msgs:
        qtns.append(" less fertile ")
        anss.append("less fertile than what/whom? less fertile compared to what/whom? ")
        flag = 1
    if " more fewer " in msgs:
        qtns.append(" more fewer ")
        anss.append("more fewer than what/whom? more fewer compared to what/whom? ")
        flag = 1
    if " less fewer " in msgs:
        qtns.append(" less fewer ")
        anss.append("less fewer than what/whom? less fewer compared to what/whom? ")
        flag = 1
    if " more fiercer " in msgs:
        qtns.append(" more fiercer ")
        anss.append("more fiercer than what/whom? more fiercer compared to what/whom? ")
        flag = 1
    if " less fiercer " in msgs:
        qtns.append(" less fiercer ")
        anss.append("less fiercer than what/whom? less fiercer compared to what/whom? ")
        flag = 1
    if " more filthier " in msgs:
        qtns.append(" more filthier ")
        anss.append("more filthier than what/whom? more filthier compared to what/whom? ")
        flag = 1
    if " less filthier " in msgs:
        qtns.append(" less filthier ")
        anss.append("less filthier than what/whom? less filthier compared to what/whom? ")
        flag = 1
    if " more finer " in msgs:
        qtns.append(" more finer ")
        anss.append("more finer than what/whom? more finer compared to what/whom? ")
        flag = 1
    if " less finer " in msgs:
        qtns.append(" less finer ")
        anss.append("less finer than what/whom? less finer compared to what/whom? ")
        flag = 1
    if " more firmer " in msgs:
        qtns.append(" more firmer ")
        anss.append("more firmer than what/whom? more firmer compared to what/whom? ")
        flag = 1
    if " less firmer " in msgs:
        qtns.append(" less firmer ")
        anss.append("less firmer than what/whom? less firmer compared to what/whom? ")
        flag = 1
    if " more fitter " in msgs:
        qtns.append(" more fitter ")
        anss.append("more fitter than what/whom? more fitter compared to what/whom? ")
        flag = 1
    if " less fitter " in msgs:
        qtns.append(" less fitter ")
        anss.append("less fitter than what/whom? less fitter compared to what/whom? ")
        flag = 1
    if " more flakier " in msgs:
        qtns.append(" more flakier ")
        anss.append("more flakier than what/whom? more flakier compared to what/whom? ")
        flag = 1
    if " less flakier " in msgs:
        qtns.append(" less flakier ")
        anss.append("less flakier than what/whom? less flakier compared to what/whom? ")
        flag = 1
    if " more flatter " in msgs:
        qtns.append(" more flatter ")
        anss.append("more flatter than what/whom? more flatter compared to what/whom? ")
        flag = 1
    if " less flatter " in msgs:
        qtns.append(" less flatter ")
        anss.append("less flatter than what/whom? less flatter compared to what/whom? ")
        flag = 1
    if " more foolish " in msgs:
        qtns.append(" more foolish ")
        anss.append("more foolish than what/whom? more foolish compared to what/whom? ")
        flag = 1
    if " less foolish " in msgs:
        qtns.append(" less foolish ")
        anss.append("less foolish than what/whom? less foolish compared to what/whom? ")
        flag = 1
    if " more forgetful " in msgs:
        qtns.append(" more forgetful ")
        anss.append("more forgetful than what/whom? more forgetful compared to what/whom? ")
        flag = 1
    if " less forgetful " in msgs:
        qtns.append(" less forgetful ")
        anss.append("less forgetful than what/whom? less forgetful compared to what/whom? ")
        flag = 1
    if " more fresher " in msgs:
        qtns.append(" more fresher ")
        anss.append("more fresher than what/whom? more fresher compared to what/whom? ")
        flag = 1
    if " less fresher " in msgs:
        qtns.append(" less fresher ")
        anss.append("less fresher than what/whom? less fresher compared to what/whom? ")
        flag = 1
    if " more friendlier " in msgs:
        qtns.append(" more friendlier ")
        anss.append("more friendlier than what/whom? more friendlier compared to what/whom? ")
        flag = 1
    if " less friendlier " in msgs:
        qtns.append(" less friendlier ")
        anss.append("less friendlier than what/whom? less friendlier compared to what/whom? ")
        flag = 1
    if " more fuller " in msgs:
        qtns.append(" more fuller ")
        anss.append("more fuller than what/whom? more fuller compared to what/whom? ")
        flag = 1
    if " less fuller " in msgs:
        qtns.append(" less fuller ")
        anss.append("less fuller than what/whom? less fuller compared to what/whom? ")
        flag = 1
    if " more funnier " in msgs:
        qtns.append(" more funnier ")
        anss.append("more funnier than what/whom? more funnier compared to what/whom? ")
        flag = 1
    if " less funnier " in msgs:
        qtns.append(" less funnier ")
        anss.append("less funnier than what/whom? less funnier compared to what/whom? ")
        flag = 1
    if " more gentler " in msgs:
        qtns.append(" more gentler ")
        anss.append("more gentler than what/whom? more gentler compared to what/whom? ")
        flag = 1
    if " less gentler " in msgs:
        qtns.append(" less gentler ")
        anss.append("less gentler than what/whom? less gentler compared to what/whom? ")
        flag = 1
    if " more glamorous " in msgs:
        qtns.append(" more glamorous ")
        anss.append("more glamorous than what/whom? more glamorous compared to what/whom? ")
        flag = 1
    if " less glamorous " in msgs:
        qtns.append(" less glamorous ")
        anss.append("less glamorous than what/whom? less glamorous compared to what/whom? ")
        flag = 1
    if " more gloomier " in msgs:
        qtns.append(" more gloomier ")
        anss.append("more gloomier than what/whom? more gloomier compared to what/whom? ")
        flag = 1
    if " less gloomier " in msgs:
        qtns.append(" less gloomier ")
        anss.append("less gloomier than what/whom? less gloomier compared to what/whom? ")
        flag = 1
    if " more glorious " in msgs:
        qtns.append(" more glorious ")
        anss.append("more glorious than what/whom? more glorious compared to what/whom? ")
        flag = 1
    if " less glorious " in msgs:
        qtns.append(" less glorious ")
        anss.append("less glorious than what/whom? less glorious compared to what/whom? ")
        flag = 1
    if " more better " in msgs:
        qtns.append(" more better ")
        anss.append("more better than what/whom? more better compared to what/whom? ")
        flag = 1
    if " less better " in msgs:
        qtns.append(" less better ")
        anss.append("less better than what/whom? less better compared to what/whom? ")
        flag = 1
    if " more gorgeous " in msgs:
        qtns.append(" more gorgeous ")
        anss.append("more gorgeous than what/whom? more gorgeous compared to what/whom? ")
        flag = 1
    if " less gorgeous " in msgs:
        qtns.append(" less gorgeous ")
        anss.append("less gorgeous than what/whom? less gorgeous compared to what/whom? ")
        flag = 1
    if " more graceful " in msgs:
        qtns.append(" more graceful ")
        anss.append("more graceful than what/whom? more graceful compared to what/whom? ")
        flag = 1
    if " less graceful " in msgs:
        qtns.append(" less graceful ")
        anss.append("less graceful than what/whom? less graceful compared to what/whom? ")
        flag = 1
    if " more grander " in msgs:
        qtns.append(" more grander ")
        anss.append("more grander than what/whom? more grander compared to what/whom? ")
        flag = 1
    if " less grander " in msgs:
        qtns.append(" less grander ")
        anss.append("less grander than what/whom? less grander compared to what/whom? ")
        flag = 1
    if " more grateful " in msgs:
        qtns.append(" more grateful ")
        anss.append("more grateful than what/whom? more grateful compared to what/whom? ")
        flag = 1
    if " less grateful " in msgs:
        qtns.append(" less grateful ")
        anss.append("less grateful than what/whom? less grateful compared to what/whom? ")
        flag = 1
    if " more graver " in msgs:
        qtns.append(" more graver ")
        anss.append("more graver than what/whom? more graver compared to what/whom? ")
        flag = 1
    if " less graver " in msgs:
        qtns.append(" less graver ")
        anss.append("less graver than what/whom? less graver compared to what/whom? ")
        flag = 1
    if " more greasier " in msgs:
        qtns.append(" more greasier ")
        anss.append("more greasier than what/whom? more greasier compared to what/whom? ")
        flag = 1
    if " less greasier " in msgs:
        qtns.append(" less greasier ")
        anss.append("less greasier than what/whom? less greasier compared to what/whom? ")
        flag = 1
    if " more greater " in msgs:
        qtns.append(" more greater ")
        anss.append("more greater than what/whom? more greater compared to what/whom? ")
        flag = 1
    if " less greater " in msgs:
        qtns.append(" less greater ")
        anss.append("less greater than what/whom? less greater compared to what/whom? ")
        flag = 1
    if " more greedier " in msgs:
        qtns.append(" more greedier ")
        anss.append("more greedier than what/whom? more greedier compared to what/whom? ")
        flag = 1
    if " less greedier " in msgs:
        qtns.append(" less greedier ")
        anss.append("less greedier than what/whom? less greedier compared to what/whom? ")
        flag = 1
    if " more greener " in msgs:
        qtns.append(" more greener ")
        anss.append("more greener than what/whom? more greener compared to what/whom? ")
        flag = 1
    if " less greener " in msgs:
        qtns.append(" less greener ")
        anss.append("less greener than what/whom? less greener compared to what/whom? ")
        flag = 1
    if " more grosser " in msgs:
        qtns.append(" more grosser ")
        anss.append("more grosser than what/whom? more grosser compared to what/whom? ")
        flag = 1
    if " less grosser " in msgs:
        qtns.append(" less grosser ")
        anss.append("less grosser than what/whom? less grosser compared to what/whom? ")
        flag = 1
    if " more guiltier " in msgs:
        qtns.append(" more guiltier ")
        anss.append("more guiltier than what/whom? more guiltier compared to what/whom? ")
        flag = 1
    if " less guiltier " in msgs:
        qtns.append(" less guiltier ")
        anss.append("less guiltier than what/whom? less guiltier compared to what/whom? ")
        flag = 1
    if " more hairier " in msgs:
        qtns.append(" more hairier ")
        anss.append("more hairier than what/whom? more hairier compared to what/whom? ")
        flag = 1
    if " less hairier " in msgs:
        qtns.append(" less hairier ")
        anss.append("less hairier than what/whom? less hairier compared to what/whom? ")
        flag = 1
    if " more handsome " in msgs:
        qtns.append(" more handsome ")
        anss.append("more handsome than what/whom? more handsome compared to what/whom? ")
        flag = 1
    if " less handsome " in msgs:
        qtns.append(" less handsome ")
        anss.append("less handsome than what/whom? less handsome compared to what/whom? ")
        flag = 1
    if " more handier " in msgs:
        qtns.append(" more handier ")
        anss.append("more handier than what/whom? more handier compared to what/whom? ")
        flag = 1
    if " less handier " in msgs:
        qtns.append(" less handier ")
        anss.append("less handier than what/whom? less handier compared to what/whom? ")
        flag = 1
    if " more happier " in msgs:
        qtns.append(" more happier ")
        anss.append("more happier than what/whom? more happier compared to what/whom? ")
        flag = 1
    if " less happier " in msgs:
        qtns.append(" less happier ")
        anss.append("less happier than what/whom? less happier compared to what/whom? ")
        flag = 1
    if " more harder " in msgs:
        qtns.append(" more harder ")
        anss.append("more harder than what/whom? more harder compared to what/whom? ")
        flag = 1
    if " less harder " in msgs:
        qtns.append(" less harder ")
        anss.append("less harder than what/whom? less harder compared to what/whom? ")
        flag = 1
    if " more harsher " in msgs:
        qtns.append(" more harsher ")
        anss.append("more harsher than what/whom? more harsher compared to what/whom? ")
        flag = 1
    if " less harsher " in msgs:
        qtns.append(" less harsher ")
        anss.append("less harsher than what/whom? less harsher compared to what/whom? ")
        flag = 1
    if " more healthier " in msgs:
        qtns.append(" more healthier ")
        anss.append("more healthier than what/whom? more healthier compared to what/whom? ")
        flag = 1
    if " less healthier " in msgs:
        qtns.append(" less healthier ")
        anss.append("less healthier than what/whom? less healthier compared to what/whom? ")
        flag = 1
    if " more heavier " in msgs:
        qtns.append(" more heavier ")
        anss.append("more heavier than what/whom? more heavier compared to what/whom? ")
        flag = 1
    if " less heavier " in msgs:
        qtns.append(" less heavier ")
        anss.append("less heavier than what/whom? less heavier compared to what/whom? ")
        flag = 1
    if " more helpful " in msgs:
        qtns.append(" more helpful ")
        anss.append("more helpful than what/whom? more helpful compared to what/whom? ")
        flag = 1
    if " less helpful " in msgs:
        qtns.append(" less helpful ")
        anss.append("less helpful than what/whom? less helpful compared to what/whom? ")
        flag = 1
    if " more higher " in msgs:
        qtns.append(" more higher ")
        anss.append("more higher than what/whom? more higher compared to what/whom? ")
        flag = 1
    if " less higher " in msgs:
        qtns.append(" less higher ")
        anss.append("less higher than what/whom? less higher compared to what/whom? ")
        flag = 1
    if " more hilarious " in msgs:
        qtns.append(" more hilarious ")
        anss.append("more hilarious than what/whom? more hilarious compared to what/whom? ")
        flag = 1
    if " less hilarious " in msgs:
        qtns.append(" less hilarious ")
        anss.append("less hilarious than what/whom? less hilarious compared to what/whom? ")
        flag = 1
    if " more hipper " in msgs:
        qtns.append(" more hipper ")
        anss.append("more hipper than what/whom? more hipper compared to what/whom? ")
        flag = 1
    if " less hipper " in msgs:
        qtns.append(" less hipper ")
        anss.append("less hipper than what/whom? less hipper compared to what/whom? ")
        flag = 1
    if " more historical " in msgs:
        qtns.append(" more historical ")
        anss.append("more historical than what/whom? more historical compared to what/whom? ")
        flag = 1
    if " less historical " in msgs:
        qtns.append(" less historical ")
        anss.append("less historical than what/whom? less historical compared to what/whom? ")
        flag = 1
    if " more horrible " in msgs:
        qtns.append(" more horrible ")
        anss.append("more horrible than what/whom? more horrible compared to what/whom? ")
        flag = 1
    if " less horrible " in msgs:
        qtns.append(" less horrible ")
        anss.append("less horrible than what/whom? less horrible compared to what/whom? ")
        flag = 1
    if " more hotter " in msgs:
        qtns.append(" more hotter ")
        anss.append("more hotter than what/whom? more hotter compared to what/whom? ")
        flag = 1
    if " less hotter " in msgs:
        qtns.append(" less hotter ")
        anss.append("less hotter than what/whom? less hotter compared to what/whom? ")
        flag = 1
    if " more huge " in msgs:
        qtns.append(" more huge ")
        anss.append("more huge than what/whom? more huge compared to what/whom? ")
        flag = 1
    if " less huge " in msgs:
        qtns.append(" less huge ")
        anss.append("less huge than what/whom? less huge compared to what/whom? ")
        flag = 1
    if " more humbler " in msgs:
        qtns.append(" more humbler ")
        anss.append("more humbler than what/whom? more humbler compared to what/whom? ")
        flag = 1
    if " less humbler " in msgs:
        qtns.append(" less humbler ")
        anss.append("less humbler than what/whom? less humbler compared to what/whom? ")
        flag = 1
    if " more humorous " in msgs:
        qtns.append(" more humorous ")
        anss.append("more humorous than what/whom? more humorous compared to what/whom? ")
        flag = 1
    if " less humorous " in msgs:
        qtns.append(" less humorous ")
        anss.append("less humorous than what/whom? less humorous compared to what/whom? ")
        flag = 1
    if " more hungrier " in msgs:
        qtns.append(" more hungrier ")
        anss.append("more hungrier than what/whom? more hungrier compared to what/whom? ")
        flag = 1
    if " less hungrier " in msgs:
        qtns.append(" less hungrier ")
        anss.append("less hungrier than what/whom? less hungrier compared to what/whom? ")
        flag = 1
    if " more icier " in msgs:
        qtns.append(" more icier ")
        anss.append("more icier than what/whom? more icier compared to what/whom? ")
        flag = 1
    if " less icier " in msgs:
        qtns.append(" less icier ")
        anss.append("less icier than what/whom? less icier compared to what/whom? ")
        flag = 1
    if " more ignorant " in msgs:
        qtns.append(" more ignorant ")
        anss.append("more ignorant than what/whom? more ignorant compared to what/whom? ")
        flag = 1
    if " less ignorant " in msgs:
        qtns.append(" less ignorant ")
        anss.append("less ignorant than what/whom? less ignorant compared to what/whom? ")
        flag = 1
    if " more illegal " in msgs:
        qtns.append(" more illegal ")
        anss.append("more illegal than what/whom? more illegal compared to what/whom? ")
        flag = 1
    if " less illegal " in msgs:
        qtns.append(" less illegal ")
        anss.append("less illegal than what/whom? less illegal compared to what/whom? ")
        flag = 1
    if " more imaginary " in msgs:
        qtns.append(" more imaginary ")
        anss.append("more imaginary than what/whom? more imaginary compared to what/whom? ")
        flag = 1
    if " less imaginary " in msgs:
        qtns.append(" less imaginary ")
        anss.append("less imaginary than what/whom? less imaginary compared to what/whom? ")
        flag = 1
    if " more impolite " in msgs:
        qtns.append(" more impolite ")
        anss.append("more impolite than what/whom? more impolite compared to what/whom? ")
        flag = 1
    if " less impolite " in msgs:
        qtns.append(" less impolite ")
        anss.append("less impolite than what/whom? less impolite compared to what/whom? ")
        flag = 1
    if " more important " in msgs:
        qtns.append(" more important ")
        anss.append("more important than what/whom? more important compared to what/whom? ")
        flag = 1
    if " less important " in msgs:
        qtns.append(" less important ")
        anss.append("less important than what/whom? less important compared to what/whom? ")
        flag = 1
    if " more impossible " in msgs:
        qtns.append(" more impossible ")
        anss.append("more impossible than what/whom? more impossible compared to what/whom? ")
        flag = 1
    if " less impossible " in msgs:
        qtns.append(" less impossible ")
        anss.append("less impossible than what/whom? less impossible compared to what/whom? ")
        flag = 1
    if " more innocent " in msgs:
        qtns.append(" more innocent ")
        anss.append("more innocent than what/whom? more innocent compared to what/whom? ")
        flag = 1
    if " less innocent " in msgs:
        qtns.append(" less innocent ")
        anss.append("less innocent than what/whom? less innocent compared to what/whom? ")
        flag = 1
    if " more intelligent " in msgs:
        qtns.append(" more intelligent ")
        anss.append("more intelligent than what/whom? more intelligent compared to what/whom? ")
        flag = 1
    if " less intelligent " in msgs:
        qtns.append(" less intelligent ")
        anss.append("less intelligent than what/whom? less intelligent compared to what/whom? ")
        flag = 1
    if " more interesting " in msgs:
        qtns.append(" more interesting ")
        anss.append("more interesting than what/whom? more interesting compared to what/whom? ")
        flag = 1
    if " less interesting " in msgs:
        qtns.append(" less interesting ")
        anss.append("less interesting than what/whom? less interesting compared to what/whom? ")
        flag = 1
    if " more itchier " in msgs:
        qtns.append(" more itchier ")
        anss.append("more itchier than what/whom? more itchier compared to what/whom? ")
        flag = 1
    if " less itchier " in msgs:
        qtns.append(" less itchier ")
        anss.append("less itchier than what/whom? less itchier compared to what/whom? ")
        flag = 1
    if " more jealous " in msgs:
        qtns.append(" more jealous ")
        anss.append("more jealous than what/whom? more jealous compared to what/whom? ")
        flag = 1
    if " less jealous " in msgs:
        qtns.append(" less jealous ")
        anss.append("less jealous than what/whom? less jealous compared to what/whom? ")
        flag = 1
    if " more jollier " in msgs:
        qtns.append(" more jollier ")
        anss.append("more jollier than what/whom? more jollier compared to what/whom? ")
        flag = 1
    if " less jollier " in msgs:
        qtns.append(" less jollier ")
        anss.append("less jollier than what/whom? less jollier compared to what/whom? ")
        flag = 1
    if " more juicier " in msgs:
        qtns.append(" more juicier ")
        anss.append("more juicier than what/whom? more juicier compared to what/whom? ")
        flag = 1
    if " less juicier " in msgs:
        qtns.append(" less juicier ")
        anss.append("less juicier than what/whom? less juicier compared to what/whom? ")
        flag = 1
    if " more juvenile " in msgs:
        qtns.append(" more juvenile ")
        anss.append("more juvenile than what/whom? more juvenile compared to what/whom? ")
        flag = 1
    if " less juvenile " in msgs:
        qtns.append(" less juvenile ")
        anss.append("less juvenile than what/whom? less juvenile compared to what/whom? ")
        flag = 1
    if " more kinder " in msgs:
        qtns.append(" more kinder ")
        anss.append("more kinder than what/whom? more kinder compared to what/whom? ")
        flag = 1
    if " less kinder " in msgs:
        qtns.append(" less kinder ")
        anss.append("less kinder than what/whom? less kinder compared to what/whom? ")
        flag = 1
    if " more larger " in msgs:
        qtns.append(" more larger ")
        anss.append("more larger than what/whom? more larger compared to what/whom? ")
        flag = 1
    if " less larger " in msgs:
        qtns.append(" less larger ")
        anss.append("less larger than what/whom? less larger compared to what/whom? ")
        flag = 1
    if " more later " in msgs:
        qtns.append(" more later ")
        anss.append("more later than what/whom? more later compared to what/whom? ")
        flag = 1
    if " less later " in msgs:
        qtns.append(" less later ")
        anss.append("less later than what/whom? less later compared to what/whom? ")
        flag = 1
    if " more lazier " in msgs:
        qtns.append(" more lazier ")
        anss.append("more lazier than what/whom? more lazier compared to what/whom? ")
        flag = 1
    if " less lazier " in msgs:
        qtns.append(" less lazier ")
        anss.append("less lazier than what/whom? less lazier compared to what/whom? ")
        flag = 1
    if " more legal " in msgs:
        qtns.append(" more legal ")
        anss.append("more legal than what/whom? more legal compared to what/whom? ")
        flag = 1
    if " less legal " in msgs:
        qtns.append(" less legal ")
        anss.append("less legal than what/whom? less legal compared to what/whom? ")
        flag = 1
    if " more lighter " in msgs:
        qtns.append(" more lighter ")
        anss.append("more lighter than what/whom? more lighter compared to what/whom? ")
        flag = 1
    if " less lighter " in msgs:
        qtns.append(" less lighter ")
        anss.append("less lighter than what/whom? less lighter compared to what/whom? ")
        flag = 1
    if " more likelier " in msgs:
        qtns.append(" more likelier ")
        anss.append("more likelier than what/whom? more likelier compared to what/whom? ")
        flag = 1
    if " less likelier " in msgs:
        qtns.append(" less likelier ")
        anss.append("less likelier than what/whom? less likelier compared to what/whom? ")
        flag = 1
    if " more literate " in msgs:
        qtns.append(" more literate ")
        anss.append("more literate than what/whom? more literate compared to what/whom? ")
        flag = 1
    if " less literate " in msgs:
        qtns.append(" less literate ")
        anss.append("less literate than what/whom? less literate compared to what/whom? ")
        flag = 1
    if " more littler " in msgs:
        qtns.append(" more littler ")
        anss.append("more littler than what/whom? more littler compared to what/whom? ")
        flag = 1
    if " less littler " in msgs:
        qtns.append(" less littler ")
        anss.append("less littler than what/whom? less littler compared to what/whom? ")
        flag = 1
    if " more less " in msgs:
        qtns.append(" more less ")
        anss.append("more less than what/whom? more less compared to what/whom? ")
        flag = 1
    if " less less " in msgs:
        qtns.append(" less less ")
        anss.append("less less than what/whom? less less compared to what/whom? ")
        flag = 1
    if " more livelier " in msgs:
        qtns.append(" more livelier ")
        anss.append("more livelier than what/whom? more livelier compared to what/whom? ")
        flag = 1
    if " less livelier " in msgs:
        qtns.append(" less livelier ")
        anss.append("less livelier than what/whom? less livelier compared to what/whom? ")
        flag = 1
    if " more lonelier " in msgs:
        qtns.append(" more lonelier ")
        anss.append("more lonelier than what/whom? more lonelier compared to what/whom? ")
        flag = 1
    if " less lonelier " in msgs:
        qtns.append(" less lonelier ")
        anss.append("less lonelier than what/whom? less lonelier compared to what/whom? ")
        flag = 1
    if " more longer " in msgs:
        qtns.append(" more longer ")
        anss.append("more longer than what/whom? more longer compared to what/whom? ")
        flag = 1
    if " less longer " in msgs:
        qtns.append(" less longer ")
        anss.append("less longer than what/whom? less longer compared to what/whom? ")
        flag = 1
    if " more louder " in msgs:
        qtns.append(" more louder ")
        anss.append("more louder than what/whom? more louder compared to what/whom? ")
        flag = 1
    if " less louder " in msgs:
        qtns.append(" less louder ")
        anss.append("less louder than what/whom? less louder compared to what/whom? ")
        flag = 1
    if " more lovelier " in msgs:
        qtns.append(" more lovelier ")
        anss.append("more lovelier than what/whom? more lovelier compared to what/whom? ")
        flag = 1
    if " less lovelier " in msgs:
        qtns.append(" less lovelier ")
        anss.append("less lovelier than what/whom? less lovelier compared to what/whom? ")
        flag = 1
    if " more lower " in msgs:
        qtns.append(" more lower ")
        anss.append("more lower than what/whom? more lower compared to what/whom? ")
        flag = 1
    if " less lower " in msgs:
        qtns.append(" less lower ")
        anss.append("less lower than what/whom? less lower compared to what/whom? ")
        flag = 1
    if " more luckier " in msgs:
        qtns.append(" more luckier ")
        anss.append("more luckier than what/whom? more luckier compared to what/whom? ")
        flag = 1
    if " less luckier " in msgs:
        qtns.append(" less luckier ")
        anss.append("less luckier than what/whom? less luckier compared to what/whom? ")
        flag = 1
    if " more macho " in msgs:
        qtns.append(" more macho ")
        anss.append("more macho than what/whom? more macho compared to what/whom? ")
        flag = 1
    if " less macho " in msgs:
        qtns.append(" less macho ")
        anss.append("less macho than what/whom? less macho compared to what/whom? ")
        flag = 1
    if " more madder " in msgs:
        qtns.append(" more madder ")
        anss.append("more madder than what/whom? more madder compared to what/whom? ")
        flag = 1
    if " less madder " in msgs:
        qtns.append(" less madder ")
        anss.append("less madder than what/whom? less madder compared to what/whom? ")
        flag = 1
    if " more magical " in msgs:
        qtns.append(" more magical ")
        anss.append("more magical than what/whom? more magical compared to what/whom? ")
        flag = 1
    if " less magical " in msgs:
        qtns.append(" less magical ")
        anss.append("less magical than what/whom? less magical compared to what/whom? ")
        flag = 1
    if " more magnificent " in msgs:
        qtns.append(" more magnificent ")
        anss.append("more magnificent than what/whom? more magnificent compared to what/whom? ")
        flag = 1
    if " less magnificent " in msgs:
        qtns.append(" less magnificent ")
        anss.append("less magnificent than what/whom? less magnificent compared to what/whom? ")
        flag = 1
    if " more more " in msgs:
        qtns.append(" more more ")
        anss.append("more more than what/whom? more more compared to what/whom? ")
        flag = 1
    if " less more " in msgs:
        qtns.append(" less more ")
        anss.append("less more than what/whom? less more compared to what/whom? ")
        flag = 1
    if " more massive " in msgs:
        qtns.append(" more massive ")
        anss.append("more massive than what/whom? more massive compared to what/whom? ")
        flag = 1
    if " less massive " in msgs:
        qtns.append(" less massive ")
        anss.append("less massive than what/whom? less massive compared to what/whom? ")
        flag = 1
    if " more mature " in msgs:
        qtns.append(" more mature ")
        anss.append("more mature than what/whom? more mature compared to what/whom? ")
        flag = 1
    if " less mature " in msgs:
        qtns.append(" less mature ")
        anss.append("less mature than what/whom? less mature compared to what/whom? ")
        flag = 1
    if " more meaner " in msgs:
        qtns.append(" more meaner ")
        anss.append("more meaner than what/whom? more meaner compared to what/whom? ")
        flag = 1
    if " less meaner " in msgs:
        qtns.append(" less meaner ")
        anss.append("less meaner than what/whom? less meaner compared to what/whom? ")
        flag = 1
    if " more messier " in msgs:
        qtns.append(" more messier ")
        anss.append("more messier than what/whom? more messier compared to what/whom? ")
        flag = 1
    if " less messier " in msgs:
        qtns.append(" less messier ")
        anss.append("less messier than what/whom? less messier compared to what/whom? ")
        flag = 1
    if " more milder " in msgs:
        qtns.append(" more milder ")
        anss.append("more milder than what/whom? more milder compared to what/whom? ")
        flag = 1
    if " less milder " in msgs:
        qtns.append(" less milder ")
        anss.append("less milder than what/whom? less milder compared to what/whom? ")
        flag = 1
    if " more modern " in msgs:
        qtns.append(" more modern ")
        anss.append("more modern than what/whom? more modern compared to what/whom? ")
        flag = 1
    if " less modern " in msgs:
        qtns.append(" less modern ")
        anss.append("less modern than what/whom? less modern compared to what/whom? ")
        flag = 1
    if " more moister " in msgs:
        qtns.append(" more moister ")
        anss.append("more moister than what/whom? more moister compared to what/whom? ")
        flag = 1
    if " less moister " in msgs:
        qtns.append(" less moister ")
        anss.append("less moister than what/whom? less moister compared to what/whom? ")
        flag = 1
    if " more narrower " in msgs:
        qtns.append(" more narrower ")
        anss.append("more narrower than what/whom? more narrower compared to what/whom? ")
        flag = 1
    if " less narrower " in msgs:
        qtns.append(" less narrower ")
        anss.append("less narrower than what/whom? less narrower compared to what/whom? ")
        flag = 1
    if " more nastier " in msgs:
        qtns.append(" more nastier ")
        anss.append("more nastier than what/whom? more nastier compared to what/whom? ")
        flag = 1
    if " less nastier " in msgs:
        qtns.append(" less nastier ")
        anss.append("less nastier than what/whom? less nastier compared to what/whom? ")
        flag = 1
    if " more naughtier " in msgs:
        qtns.append(" more naughtier ")
        anss.append("more naughtier than what/whom? more naughtier compared to what/whom? ")
        flag = 1
    if " less naughtier " in msgs:
        qtns.append(" less naughtier ")
        anss.append("less naughtier than what/whom? less naughtier compared to what/whom? ")
        flag = 1
    if " more nearer " in msgs:
        qtns.append(" more nearer ")
        anss.append("more nearer than what/whom? more nearer compared to what/whom? ")
        flag = 1
    if " less nearer " in msgs:
        qtns.append(" less nearer ")
        anss.append("less nearer than what/whom? less nearer compared to what/whom? ")
        flag = 1
    if " more neater " in msgs:
        qtns.append(" more neater ")
        anss.append("more neater than what/whom? more neater compared to what/whom? ")
        flag = 1
    if " less neater " in msgs:
        qtns.append(" less neater ")
        anss.append("less neater than what/whom? less neater compared to what/whom? ")
        flag = 1
    if " more needier " in msgs:
        qtns.append(" more needier ")
        anss.append("more needier than what/whom? more needier compared to what/whom? ")
        flag = 1
    if " less needier " in msgs:
        qtns.append(" less needier ")
        anss.append("less needier than what/whom? less needier compared to what/whom? ")
        flag = 1
    if " more nervous " in msgs:
        qtns.append(" more nervous ")
        anss.append("more nervous than what/whom? more nervous compared to what/whom? ")
        flag = 1
    if " less nervous " in msgs:
        qtns.append(" less nervous ")
        anss.append("less nervous than what/whom? less nervous compared to what/whom? ")
        flag = 1
    if " more newer " in msgs:
        qtns.append(" more newer ")
        anss.append("more newer than what/whom? more newer compared to what/whom? ")
        flag = 1
    if " less newer " in msgs:
        qtns.append(" less newer ")
        anss.append("less newer than what/whom? less newer compared to what/whom? ")
        flag = 1
    if " more nicer " in msgs:
        qtns.append(" more nicer ")
        anss.append("more nicer than what/whom? more nicer compared to what/whom? ")
        flag = 1
    if " less nicer " in msgs:
        qtns.append(" less nicer ")
        anss.append("less nicer than what/whom? less nicer compared to what/whom? ")
        flag = 1
    if " more noisier " in msgs:
        qtns.append(" more noisier ")
        anss.append("more noisier than what/whom? more noisier compared to what/whom? ")
        flag = 1
    if " less noisier " in msgs:
        qtns.append(" less noisier ")
        anss.append("less noisier than what/whom? less noisier compared to what/whom? ")
        flag = 1
    if " more nutritious " in msgs:
        qtns.append(" more nutritious ")
        anss.append("more nutritious than what/whom? more nutritious compared to what/whom? ")
        flag = 1
    if " less nutritious " in msgs:
        qtns.append(" less nutritious ")
        anss.append("less nutritious than what/whom? less nutritious compared to what/whom? ")
        flag = 1
    if " more obedient " in msgs:
        qtns.append(" more obedient ")
        anss.append("more obedient than what/whom? more obedient compared to what/whom? ")
        flag = 1
    if " less obedient " in msgs:
        qtns.append(" less obedient ")
        anss.append("less obedient than what/whom? less obedient compared to what/whom? ")
        flag = 1
    if " more obese " in msgs:
        qtns.append(" more obese ")
        anss.append("more obese than what/whom? more obese compared to what/whom? ")
        flag = 1
    if " less obese " in msgs:
        qtns.append(" less obese ")
        anss.append("less obese than what/whom? less obese compared to what/whom? ")
        flag = 1
    if " more obnoxious " in msgs:
        qtns.append(" more obnoxious ")
        anss.append("more obnoxious than what/whom? more obnoxious compared to what/whom? ")
        flag = 1
    if " less obnoxious " in msgs:
        qtns.append(" less obnoxious ")
        anss.append("less obnoxious than what/whom? less obnoxious compared to what/whom? ")
        flag = 1
    if " more odder " in msgs:
        qtns.append(" more odder ")
        anss.append("more odder than what/whom? more odder compared to what/whom? ")
        flag = 1
    if " less odder " in msgs:
        qtns.append(" less odder ")
        anss.append("less odder than what/whom? less odder compared to what/whom? ")
        flag = 1
    if " more oilier " in msgs:
        qtns.append(" more oilier ")
        anss.append("more oilier than what/whom? more oilier compared to what/whom? ")
        flag = 1
    if " less oilier " in msgs:
        qtns.append(" less oilier ")
        anss.append("less oilier than what/whom? less oilier compared to what/whom? ")
        flag = 1
    if " more older " in msgs:
        qtns.append(" more older ")
        anss.append("more older than what/whom? more older compared to what/whom? ")
        flag = 1
    if " less older " in msgs:
        qtns.append(" less older ")
        anss.append("less older than what/whom? less older compared to what/whom? ")
        flag = 1
    if " more elder " in msgs:
        qtns.append(" more elder ")
        anss.append("more elder than what/whom? more elder compared to what/whom? ")
        flag = 1
    if " less elder " in msgs:
        qtns.append(" less elder ")
        anss.append("less elder than what/whom? less elder compared to what/whom? ")
        flag = 1
    if " more overconfident " in msgs:
        qtns.append(" more overconfident ")
        anss.append("more overconfident than what/whom? more overconfident compared to what/whom? ")
        flag = 1
    if " less overconfident " in msgs:
        qtns.append(" less overconfident ")
        anss.append("less overconfident than what/whom? less overconfident compared to what/whom? ")
        flag = 1
    if " more peaceful " in msgs:
        qtns.append(" more peaceful ")
        anss.append("more peaceful than what/whom? more peaceful compared to what/whom? ")
        flag = 1
    if " less peaceful " in msgs:
        qtns.append(" less peaceful ")
        anss.append("less peaceful than what/whom? less peaceful compared to what/whom? ")
        flag = 1
    if " more perfect " in msgs:
        qtns.append(" more perfect ")
        anss.append("more perfect than what/whom? more perfect compared to what/whom? ")
        flag = 1
    if " less perfect " in msgs:
        qtns.append(" less perfect ")
        anss.append("less perfect than what/whom? less perfect compared to what/whom? ")
        flag = 1
    if " more pinker " in msgs:
        qtns.append(" more pinker ")
        anss.append("more pinker than what/whom? more pinker compared to what/whom? ")
        flag = 1
    if " less pinker " in msgs:
        qtns.append(" less pinker ")
        anss.append("less pinker than what/whom? less pinker compared to what/whom? ")
        flag = 1
    if " more plainer " in msgs:
        qtns.append(" more plainer ")
        anss.append("more plainer than what/whom? more plainer compared to what/whom? ")
        flag = 1
    if " less plainer " in msgs:
        qtns.append(" less plainer ")
        anss.append("less plainer than what/whom? less plainer compared to what/whom? ")
        flag = 1
    if " more politer " in msgs:
        qtns.append(" more politer ")
        anss.append("more politer than what/whom? more politer compared to what/whom? ")
        flag = 1
    if " less politer " in msgs:
        qtns.append(" less politer ")
        anss.append("less politer than what/whom? less politer compared to what/whom? ")
        flag = 1
    if " more poorer " in msgs:
        qtns.append(" more poorer ")
        anss.append("more poorer than what/whom? more poorer compared to what/whom? ")
        flag = 1
    if " less poorer " in msgs:
        qtns.append(" less poorer ")
        anss.append("less poorer than what/whom? less poorer compared to what/whom? ")
        flag = 1
    if " more popular " in msgs:
        qtns.append(" more popular ")
        anss.append("more popular than what/whom? more popular compared to what/whom? ")
        flag = 1
    if " less popular " in msgs:
        qtns.append(" less popular ")
        anss.append("less popular than what/whom? less popular compared to what/whom? ")
        flag = 1
    if " more powerful " in msgs:
        qtns.append(" more powerful ")
        anss.append("more powerful than what/whom? more powerful compared to what/whom? ")
        flag = 1
    if " less powerful " in msgs:
        qtns.append(" less powerful ")
        anss.append("less powerful than what/whom? less powerful compared to what/whom? ")
        flag = 1
    if " more precious " in msgs:
        qtns.append(" more precious ")
        anss.append("more precious than what/whom? more precious compared to what/whom? ")
        flag = 1
    if " less precious " in msgs:
        qtns.append(" less precious ")
        anss.append("less precious than what/whom? less precious compared to what/whom? ")
        flag = 1
    if " more prettier " in msgs:
        qtns.append(" more prettier ")
        anss.append("more prettier than what/whom? more prettier compared to what/whom? ")
        flag = 1
    if " less prettier " in msgs:
        qtns.append(" less prettier ")
        anss.append("less prettier than what/whom? less prettier compared to what/whom? ")
        flag = 1
    if " more prouder " in msgs:
        qtns.append(" more prouder ")
        anss.append("more prouder than what/whom? more prouder compared to what/whom? ")
        flag = 1
    if " less prouder " in msgs:
        qtns.append(" less prouder ")
        anss.append("less prouder than what/whom? less prouder compared to what/whom? ")
        flag = 1
    if " more purer " in msgs:
        qtns.append(" more purer ")
        anss.append("more purer than what/whom? more purer compared to what/whom? ")
        flag = 1
    if " less purer " in msgs:
        qtns.append(" less purer ")
        anss.append("less purer than what/whom? less purer compared to what/whom? ")
        flag = 1
    if " more quicker " in msgs:
        qtns.append(" more quicker ")
        anss.append("more quicker than what/whom? more quicker compared to what/whom? ")
        flag = 1
    if " less quicker " in msgs:
        qtns.append(" less quicker ")
        anss.append("less quicker than what/whom? less quicker compared to what/whom? ")
        flag = 1
    if " more quieter " in msgs:
        qtns.append(" more quieter ")
        anss.append("more quieter than what/whom? more quieter compared to what/whom? ")
        flag = 1
    if " less quieter " in msgs:
        qtns.append(" less quieter ")
        anss.append("less quieter than what/whom? less quieter compared to what/whom? ")
        flag = 1
    if " more rapider " in msgs:
        qtns.append(" more rapider ")
        anss.append("more rapider than what/whom? more rapider compared to what/whom? ")
        flag = 1
    if " less rapider " in msgs:
        qtns.append(" less rapider ")
        anss.append("less rapider than what/whom? less rapider compared to what/whom? ")
        flag = 1
    if " more rarer " in msgs:
        qtns.append(" more rarer ")
        anss.append("more rarer than what/whom? more rarer compared to what/whom? ")
        flag = 1
    if " less rarer " in msgs:
        qtns.append(" less rarer ")
        anss.append("less rarer than what/whom? less rarer compared to what/whom? ")
        flag = 1
    if " more rawer " in msgs:
        qtns.append(" more rawer ")
        anss.append("more rawer than what/whom? more rawer compared to what/whom? ")
        flag = 1
    if " less rawer " in msgs:
        qtns.append(" less rawer ")
        anss.append("less rawer than what/whom? less rawer compared to what/whom? ")
        flag = 1
    if " more redder " in msgs:
        qtns.append(" more redder ")
        anss.append("more redder than what/whom? more redder compared to what/whom? ")
        flag = 1
    if " less redder " in msgs:
        qtns.append(" less redder ")
        anss.append("less redder than what/whom? less redder compared to what/whom? ")
        flag = 1
    if " more remarkable " in msgs:
        qtns.append(" more remarkable ")
        anss.append("more remarkable than what/whom? more remarkable compared to what/whom? ")
        flag = 1
    if " less remarkable " in msgs:
        qtns.append(" less remarkable ")
        anss.append("less remarkable than what/whom? less remarkable compared to what/whom? ")
        flag = 1
    if " more responsible " in msgs:
        qtns.append(" more responsible ")
        anss.append("more responsible than what/whom? more responsible compared to what/whom? ")
        flag = 1
    if " less responsible " in msgs:
        qtns.append(" less responsible ")
        anss.append("less responsible than what/whom? less responsible compared to what/whom? ")
        flag = 1
    if " more richer " in msgs:
        qtns.append(" more richer ")
        anss.append("more richer than what/whom? more richer compared to what/whom? ")
        flag = 1
    if " less richer " in msgs:
        qtns.append(" less richer ")
        anss.append("less richer than what/whom? less richer compared to what/whom? ")
        flag = 1
    if " more riper " in msgs:
        qtns.append(" more riper ")
        anss.append("more riper than what/whom? more riper compared to what/whom? ")
        flag = 1
    if " less riper " in msgs:
        qtns.append(" less riper ")
        anss.append("less riper than what/whom? less riper compared to what/whom? ")
        flag = 1
    if " more riskier " in msgs:
        qtns.append(" more riskier ")
        anss.append("more riskier than what/whom? more riskier compared to what/whom? ")
        flag = 1
    if " less riskier " in msgs:
        qtns.append(" less riskier ")
        anss.append("less riskier than what/whom? less riskier compared to what/whom? ")
        flag = 1
    if " more romantic " in msgs:
        qtns.append(" more romantic ")
        anss.append("more romantic than what/whom? more romantic compared to what/whom? ")
        flag = 1
    if " less romantic " in msgs:
        qtns.append(" less romantic ")
        anss.append("less romantic than what/whom? less romantic compared to what/whom? ")
        flag = 1
    if " more roomier " in msgs:
        qtns.append(" more roomier ")
        anss.append("more roomier than what/whom? more roomier compared to what/whom? ")
        flag = 1
    if " less roomier " in msgs:
        qtns.append(" less roomier ")
        anss.append("less roomier than what/whom? less roomier compared to what/whom? ")
        flag = 1
    if " more rougher " in msgs:
        qtns.append(" more rougher ")
        anss.append("more rougher than what/whom? more rougher compared to what/whom? ")
        flag = 1
    if " less rougher " in msgs:
        qtns.append(" less rougher ")
        anss.append("less rougher than what/whom? less rougher compared to what/whom? ")
        flag = 1
    if " more royal " in msgs:
        qtns.append(" more royal ")
        anss.append("more royal than what/whom? more royal compared to what/whom? ")
        flag = 1
    if " less royal " in msgs:
        qtns.append(" less royal ")
        anss.append("less royal than what/whom? less royal compared to what/whom? ")
        flag = 1
    if " more ruder " in msgs:
        qtns.append(" more ruder ")
        anss.append("more ruder than what/whom? more ruder compared to what/whom? ")
        flag = 1
    if " less ruder " in msgs:
        qtns.append(" less ruder ")
        anss.append("less ruder than what/whom? less ruder compared to what/whom? ")
        flag = 1
    if " more rustier " in msgs:
        qtns.append(" more rustier ")
        anss.append("more rustier than what/whom? more rustier compared to what/whom? ")
        flag = 1
    if " less rustier " in msgs:
        qtns.append(" less rustier ")
        anss.append("less rustier than what/whom? less rustier compared to what/whom? ")
        flag = 1
    if " more sadder " in msgs:
        qtns.append(" more sadder ")
        anss.append("more sadder than what/whom? more sadder compared to what/whom? ")
        flag = 1
    if " less sadder " in msgs:
        qtns.append(" less sadder ")
        anss.append("less sadder than what/whom? less sadder compared to what/whom? ")
        flag = 1
    if " more safer " in msgs:
        qtns.append(" more safer ")
        anss.append("more safer than what/whom? more safer compared to what/whom? ")
        flag = 1
    if " less safer " in msgs:
        qtns.append(" less safer ")
        anss.append("less safer than what/whom? less safer compared to what/whom? ")
        flag = 1
    if " more saltier " in msgs:
        qtns.append(" more saltier ")
        anss.append("more saltier than what/whom? more saltier compared to what/whom? ")
        flag = 1
    if " less saltier " in msgs:
        qtns.append(" less saltier ")
        anss.append("less saltier than what/whom? less saltier compared to what/whom? ")
        flag = 1
    if " more saner " in msgs:
        qtns.append(" more saner ")
        anss.append("more saner than what/whom? more saner compared to what/whom? ")
        flag = 1
    if " less saner " in msgs:
        qtns.append(" less saner ")
        anss.append("less saner than what/whom? less saner compared to what/whom? ")
        flag = 1
    if " more scarier " in msgs:
        qtns.append(" more scarier ")
        anss.append("more scarier than what/whom? more scarier compared to what/whom? ")
        flag = 1
    if " less scarier " in msgs:
        qtns.append(" less scarier ")
        anss.append("less scarier than what/whom? less scarier compared to what/whom? ")
        flag = 1
    if " more scintillating " in msgs:
        qtns.append(" more scintillating ")
        anss.append("more scintillating than what/whom? more scintillating compared to what/whom? ")
        flag = 1
    if " less scintillating " in msgs:
        qtns.append(" less scintillating ")
        anss.append("less scintillating than what/whom? less scintillating compared to what/whom? ")
        flag = 1
    if " more secretive " in msgs:
        qtns.append(" more secretive ")
        anss.append("more secretive than what/whom? more secretive compared to what/whom? ")
        flag = 1
    if " less secretive " in msgs:
        qtns.append(" less secretive ")
        anss.append("less secretive than what/whom? less secretive compared to what/whom? ")
        flag = 1
    if " more selfish " in msgs:
        qtns.append(" more selfish ")
        anss.append("more selfish than what/whom? more selfish compared to what/whom? ")
        flag = 1
    if " less selfish " in msgs:
        qtns.append(" less selfish ")
        anss.append("less selfish than what/whom? less selfish compared to what/whom? ")
        flag = 1
    if " more serious " in msgs:
        qtns.append(" more serious ")
        anss.append("more serious than what/whom? more serious compared to what/whom? ")
        flag = 1
    if " less serious " in msgs:
        qtns.append(" less serious ")
        anss.append("less serious than what/whom? less serious compared to what/whom? ")
        flag = 1
    if " more shallower " in msgs:
        qtns.append(" more shallower ")
        anss.append("more shallower than what/whom? more shallower compared to what/whom? ")
        flag = 1
    if " less shallower " in msgs:
        qtns.append(" less shallower ")
        anss.append("less shallower than what/whom? less shallower compared to what/whom? ")
        flag = 1
    if " more sharper " in msgs:
        qtns.append(" more sharper ")
        anss.append("more sharper than what/whom? more sharper compared to what/whom? ")
        flag = 1
    if " less sharper " in msgs:
        qtns.append(" less sharper ")
        anss.append("less sharper than what/whom? less sharper compared to what/whom? ")
        flag = 1
    if " more shinier " in msgs:
        qtns.append(" more shinier ")
        anss.append("more shinier than what/whom? more shinier compared to what/whom? ")
        flag = 1
    if " less shinier " in msgs:
        qtns.append(" less shinier ")
        anss.append("less shinier than what/whom? less shinier compared to what/whom? ")
        flag = 1
    if " more shocking " in msgs:
        qtns.append(" more shocking ")
        anss.append("more shocking than what/whom? more shocking compared to what/whom? ")
        flag = 1
    if " less shocking " in msgs:
        qtns.append(" less shocking ")
        anss.append("less shocking than what/whom? less shocking compared to what/whom? ")
        flag = 1
    if " more shorter " in msgs:
        qtns.append(" more shorter ")
        anss.append("more shorter than what/whom? more shorter compared to what/whom? ")
        flag = 1
    if " less shorter " in msgs:
        qtns.append(" less shorter ")
        anss.append("less shorter than what/whom? less shorter compared to what/whom? ")
        flag = 1
    if " more shyer " in msgs:
        qtns.append(" more shyer ")
        anss.append("more shyer than what/whom? more shyer compared to what/whom? ")
        flag = 1
    if " less shyer " in msgs:
        qtns.append(" less shyer ")
        anss.append("less shyer than what/whom? less shyer compared to what/whom? ")
        flag = 1
    if " more sillier " in msgs:
        qtns.append(" more sillier ")
        anss.append("more sillier than what/whom? more sillier compared to what/whom? ")
        flag = 1
    if " less sillier " in msgs:
        qtns.append(" less sillier ")
        anss.append("less sillier than what/whom? less sillier compared to what/whom? ")
        flag = 1
    if " more simpler " in msgs:
        qtns.append(" more simpler ")
        anss.append("more simpler than what/whom? more simpler compared to what/whom? ")
        flag = 1
    if " less simpler " in msgs:
        qtns.append(" less simpler ")
        anss.append("less simpler than what/whom? less simpler compared to what/whom? ")
        flag = 1
    if " more sincere " in msgs:
        qtns.append(" more sincere ")
        anss.append("more sincere than what/whom? more sincere compared to what/whom? ")
        flag = 1
    if " less sincere " in msgs:
        qtns.append(" less sincere ")
        anss.append("less sincere than what/whom? less sincere compared to what/whom? ")
        flag = 1
    if " more sincerer " in msgs:
        qtns.append(" more sincerer ")
        anss.append("more sincerer than what/whom? more sincerer compared to what/whom? ")
        flag = 1
    if " less sincerer " in msgs:
        qtns.append(" less sincerer ")
        anss.append("less sincerer than what/whom? less sincerer compared to what/whom? ")
        flag = 1
    if " more skinnier " in msgs:
        qtns.append(" more skinnier ")
        anss.append("more skinnier than what/whom? more skinnier compared to what/whom? ")
        flag = 1
    if " less skinnier " in msgs:
        qtns.append(" less skinnier ")
        anss.append("less skinnier than what/whom? less skinnier compared to what/whom? ")
        flag = 1
    if " more sleepier " in msgs:
        qtns.append(" more sleepier ")
        anss.append("more sleepier than what/whom? more sleepier compared to what/whom? ")
        flag = 1
    if " less sleepier " in msgs:
        qtns.append(" less sleepier ")
        anss.append("less sleepier than what/whom? less sleepier compared to what/whom? ")
        flag = 1
    if " more slimmer " in msgs:
        qtns.append(" more slimmer ")
        anss.append("more slimmer than what/whom? more slimmer compared to what/whom? ")
        flag = 1
    if " less slimmer " in msgs:
        qtns.append(" less slimmer ")
        anss.append("less slimmer than what/whom? less slimmer compared to what/whom? ")
        flag = 1
    if " more slimier " in msgs:
        qtns.append(" more slimier ")
        anss.append("more slimier than what/whom? more slimier compared to what/whom? ")
        flag = 1
    if " less slimier " in msgs:
        qtns.append(" less slimier ")
        anss.append("less slimier than what/whom? less slimier compared to what/whom? ")
        flag = 1
    if " more slower " in msgs:
        qtns.append(" more slower ")
        anss.append("more slower than what/whom? more slower compared to what/whom? ")
        flag = 1
    if " less slower " in msgs:
        qtns.append(" less slower ")
        anss.append("less slower than what/whom? less slower compared to what/whom? ")
        flag = 1
    if " more smaller " in msgs:
        qtns.append(" more smaller ")
        anss.append("more smaller than what/whom? more smaller compared to what/whom? ")
        flag = 1
    if " less smaller " in msgs:
        qtns.append(" less smaller ")
        anss.append("less smaller than what/whom? less smaller compared to what/whom? ")
        flag = 1
    if " more smarter " in msgs:
        qtns.append(" more smarter ")
        anss.append("more smarter than what/whom? more smarter compared to what/whom? ")
        flag = 1
    if " less smarter " in msgs:
        qtns.append(" less smarter ")
        anss.append("less smarter than what/whom? less smarter compared to what/whom? ")
        flag = 1
    if " more smellier " in msgs:
        qtns.append(" more smellier ")
        anss.append("more smellier than what/whom? more smellier compared to what/whom? ")
        flag = 1
    if " less smellier " in msgs:
        qtns.append(" less smellier ")
        anss.append("less smellier than what/whom? less smellier compared to what/whom? ")
        flag = 1
    if " more smokier " in msgs:
        qtns.append(" more smokier ")
        anss.append("more smokier than what/whom? more smokier compared to what/whom? ")
        flag = 1
    if " less smokier " in msgs:
        qtns.append(" less smokier ")
        anss.append("less smokier than what/whom? less smokier compared to what/whom? ")
        flag = 1
    if " more smoother " in msgs:
        qtns.append(" more smoother ")
        anss.append("more smoother than what/whom? more smoother compared to what/whom? ")
        flag = 1
    if " less smoother " in msgs:
        qtns.append(" less smoother ")
        anss.append("less smoother than what/whom? less smoother compared to what/whom? ")
        flag = 1
    if " more softer " in msgs:
        qtns.append(" more softer ")
        anss.append("more softer than what/whom? more softer compared to what/whom? ")
        flag = 1
    if " less softer " in msgs:
        qtns.append(" less softer ")
        anss.append("less softer than what/whom? less softer compared to what/whom? ")
        flag = 1
    if " more sooner " in msgs:
        qtns.append(" more sooner ")
        anss.append("more sooner than what/whom? more sooner compared to what/whom? ")
        flag = 1
    if " less sooner " in msgs:
        qtns.append(" less sooner ")
        anss.append("less sooner than what/whom? less sooner compared to what/whom? ")
        flag = 1
    if " more sorer " in msgs:
        qtns.append(" more sorer ")
        anss.append("more sorer than what/whom? more sorer compared to what/whom? ")
        flag = 1
    if " less sorer " in msgs:
        qtns.append(" less sorer ")
        anss.append("less sorer than what/whom? less sorer compared to what/whom? ")
        flag = 1
    if " more sorrier " in msgs:
        qtns.append(" more sorrier ")
        anss.append("more sorrier than what/whom? more sorrier compared to what/whom? ")
        flag = 1
    if " less sorrier " in msgs:
        qtns.append(" less sorrier ")
        anss.append("less sorrier than what/whom? less sorrier compared to what/whom? ")
        flag = 1
    if " more sourer " in msgs:
        qtns.append(" more sourer ")
        anss.append("more sourer than what/whom? more sourer compared to what/whom? ")
        flag = 1
    if " less sourer " in msgs:
        qtns.append(" less sourer ")
        anss.append("less sourer than what/whom? less sourer compared to what/whom? ")
        flag = 1
    if " more spicier " in msgs:
        qtns.append(" more spicier ")
        anss.append("more spicier than what/whom? more spicier compared to what/whom? ")
        flag = 1
    if " less spicier " in msgs:
        qtns.append(" less spicier ")
        anss.append("less spicier than what/whom? less spicier compared to what/whom? ")
        flag = 1
    if " more spiritual " in msgs:
        qtns.append(" more spiritual ")
        anss.append("more spiritual than what/whom? more spiritual compared to what/whom? ")
        flag = 1
    if " less spiritual " in msgs:
        qtns.append(" less spiritual ")
        anss.append("less spiritual than what/whom? less spiritual compared to what/whom? ")
        flag = 1
    if " more splendid " in msgs:
        qtns.append(" more splendid ")
        anss.append("more splendid than what/whom? more splendid compared to what/whom? ")
        flag = 1
    if " less splendid " in msgs:
        qtns.append(" less splendid ")
        anss.append("less splendid than what/whom? less splendid compared to what/whom? ")
        flag = 1
    if " more steeper " in msgs:
        qtns.append(" more steeper ")
        anss.append("more steeper than what/whom? more steeper compared to what/whom? ")
        flag = 1
    if " less steeper " in msgs:
        qtns.append(" less steeper ")
        anss.append("less steeper than what/whom? less steeper compared to what/whom? ")
        flag = 1
    if " more stingier " in msgs:
        qtns.append(" more stingier ")
        anss.append("more stingier than what/whom? more stingier compared to what/whom? ")
        flag = 1
    if " less stingier " in msgs:
        qtns.append(" less stingier ")
        anss.append("less stingier than what/whom? less stingier compared to what/whom? ")
        flag = 1
    if " more stranger " in msgs:
        qtns.append(" more stranger ")
        anss.append("more stranger than what/whom? more stranger compared to what/whom? ")
        flag = 1
    if " less stranger " in msgs:
        qtns.append(" less stranger ")
        anss.append("less stranger than what/whom? less stranger compared to what/whom? ")
        flag = 1
    if " more stricter " in msgs:
        qtns.append(" more stricter ")
        anss.append("more stricter than what/whom? more stricter compared to what/whom? ")
        flag = 1
    if " less stricter " in msgs:
        qtns.append(" less stricter ")
        anss.append("less stricter than what/whom? less stricter compared to what/whom? ")
        flag = 1
    if " more stronger " in msgs:
        qtns.append(" more stronger ")
        anss.append("more stronger than what/whom? more stronger compared to what/whom? ")
        flag = 1
    if " less stronger " in msgs:
        qtns.append(" less stronger ")
        anss.append("less stronger than what/whom? less stronger compared to what/whom? ")
        flag = 1
    if " more successful " in msgs:
        qtns.append(" more successful ")
        anss.append("more successful than what/whom? more successful compared to what/whom? ")
        flag = 1
    if " less successful " in msgs:
        qtns.append(" less successful ")
        anss.append("less successful than what/whom? less successful compared to what/whom? ")
        flag = 1
    if " more sunnier " in msgs:
        qtns.append(" more sunnier ")
        anss.append("more sunnier than what/whom? more sunnier compared to what/whom? ")
        flag = 1
    if " less sunnier " in msgs:
        qtns.append(" less sunnier ")
        anss.append("less sunnier than what/whom? less sunnier compared to what/whom? ")
        flag = 1
    if " more sweatier " in msgs:
        qtns.append(" more sweatier ")
        anss.append("more sweatier than what/whom? more sweatier compared to what/whom? ")
        flag = 1
    if " less sweatier " in msgs:
        qtns.append(" less sweatier ")
        anss.append("less sweatier than what/whom? less sweatier compared to what/whom? ")
        flag = 1
    if " more sweeter " in msgs:
        qtns.append(" more sweeter ")
        anss.append("more sweeter than what/whom? more sweeter compared to what/whom? ")
        flag = 1
    if " less sweeter " in msgs:
        qtns.append(" less sweeter ")
        anss.append("less sweeter than what/whom? less sweeter compared to what/whom? ")
        flag = 1
    if " more tactful " in msgs:
        qtns.append(" more tactful ")
        anss.append("more tactful than what/whom? more tactful compared to what/whom? ")
        flag = 1
    if " less tactful " in msgs:
        qtns.append(" less tactful ")
        anss.append("less tactful than what/whom? less tactful compared to what/whom? ")
        flag = 1
    if " more tailor-made " in msgs:
        qtns.append(" more tailor-made ")
        anss.append("more tailor-made than what/whom? more tailor-made compared to what/whom? ")
        flag = 1
    if " less tailor-made " in msgs:
        qtns.append(" less tailor-made ")
        anss.append("less tailor-made than what/whom? less tailor-made compared to what/whom? ")
        flag = 1
    if " more take-charge " in msgs:
        qtns.append(" more take-charge ")
        anss.append("more take-charge than what/whom? more take-charge compared to what/whom? ")
        flag = 1
    if " less take-charge " in msgs:
        qtns.append(" less take-charge ")
        anss.append("less take-charge than what/whom? less take-charge compared to what/whom? ")
        flag = 1
    if " more talented " in msgs:
        qtns.append(" more talented ")
        anss.append("more talented than what/whom? more talented compared to what/whom? ")
        flag = 1
    if " less talented " in msgs:
        qtns.append(" less talented ")
        anss.append("less talented than what/whom? less talented compared to what/whom? ")
        flag = 1
    if " more taller " in msgs:
        qtns.append(" more taller ")
        anss.append("more taller than what/whom? more taller compared to what/whom? ")
        flag = 1
    if " less taller " in msgs:
        qtns.append(" less taller ")
        anss.append("less taller than what/whom? less taller compared to what/whom? ")
        flag = 1
    if " more tanner " in msgs:
        qtns.append(" more tanner ")
        anss.append("more tanner than what/whom? more tanner compared to what/whom? ")
        flag = 1
    if " less tanner " in msgs:
        qtns.append(" less tanner ")
        anss.append("less tanner than what/whom? less tanner compared to what/whom? ")
        flag = 1
    if " more tangible " in msgs:
        qtns.append(" more tangible ")
        anss.append("more tangible than what/whom? more tangible compared to what/whom? ")
        flag = 1
    if " less tangible " in msgs:
        qtns.append(" less tangible ")
        anss.append("less tangible than what/whom? less tangible compared to what/whom? ")
        flag = 1
    if " more tasteful " in msgs:
        qtns.append(" more tasteful ")
        anss.append("more tasteful than what/whom? more tasteful compared to what/whom? ")
        flag = 1
    if " less tasteful " in msgs:
        qtns.append(" less tasteful ")
        anss.append("less tasteful than what/whom? less tasteful compared to what/whom? ")
        flag = 1
    if " more tasty " in msgs:
        qtns.append(" more tasty ")
        anss.append("more tasty than what/whom? more tasty compared to what/whom? ")
        flag = 1
    if " less tasty " in msgs:
        qtns.append(" less tasty ")
        anss.append("less tasty than what/whom? less tasty compared to what/whom? ")
        flag = 1
    if " more tastier " in msgs:
        qtns.append(" more tastier ")
        anss.append("more tastier than what/whom? more tastier compared to what/whom? ")
        flag = 1
    if " less tastier " in msgs:
        qtns.append(" less tastier ")
        anss.append("less tastier than what/whom? less tastier compared to what/whom? ")
        flag = 1
    if " more teachable " in msgs:
        qtns.append(" more teachable ")
        anss.append("more teachable than what/whom? more teachable compared to what/whom? ")
        flag = 1
    if " less teachable " in msgs:
        qtns.append(" less teachable ")
        anss.append("less teachable than what/whom? less teachable compared to what/whom? ")
        flag = 1
    if " more teeming " in msgs:
        qtns.append(" more teeming ")
        anss.append("more teeming than what/whom? more teeming compared to what/whom? ")
        flag = 1
    if " less teeming " in msgs:
        qtns.append(" less teeming ")
        anss.append("less teeming than what/whom? less teeming compared to what/whom? ")
        flag = 1
    if " more tempean " in msgs:
        qtns.append(" more tempean ")
        anss.append("more tempean than what/whom? more tempean compared to what/whom? ")
        flag = 1
    if " less tempean " in msgs:
        qtns.append(" less tempean ")
        anss.append("less tempean than what/whom? less tempean compared to what/whom? ")
        flag = 1
    if " more temperate " in msgs:
        qtns.append(" more temperate ")
        anss.append("more temperate than what/whom? more temperate compared to what/whom? ")
        flag = 1
    if " less temperate " in msgs:
        qtns.append(" less temperate ")
        anss.append("less temperate than what/whom? less temperate compared to what/whom? ")
        flag = 1
    if " more tenable " in msgs:
        qtns.append(" more tenable ")
        anss.append("more tenable than what/whom? more tenable compared to what/whom? ")
        flag = 1
    if " less tenable " in msgs:
        qtns.append(" less tenable ")
        anss.append("less tenable than what/whom? less tenable compared to what/whom? ")
        flag = 1
    if " more tenacious " in msgs:
        qtns.append(" more tenacious ")
        anss.append("more tenacious than what/whom? more tenacious compared to what/whom? ")
        flag = 1
    if " less tenacious " in msgs:
        qtns.append(" less tenacious ")
        anss.append("less tenacious than what/whom? less tenacious compared to what/whom? ")
        flag = 1
    if " more tender-hearted " in msgs:
        qtns.append(" more tender-hearted ")
        anss.append("more tender-hearted than what/whom? more tender-hearted compared to what/whom? ")
        flag = 1
    if " less tender-hearted " in msgs:
        qtns.append(" less tender-hearted ")
        anss.append("less tender-hearted than what/whom? less tender-hearted compared to what/whom? ")
        flag = 1
    if " more tense " in msgs:
        qtns.append(" more tense ")
        anss.append("more tense than what/whom? more tense compared to what/whom? ")
        flag = 1
    if " less tense " in msgs:
        qtns.append(" less tense ")
        anss.append("less tense than what/whom? less tense compared to what/whom? ")
        flag = 1
    if " more terrible " in msgs:
        qtns.append(" more terrible ")
        anss.append("more terrible than what/whom? more terrible compared to what/whom? ")
        flag = 1
    if " less terrible " in msgs:
        qtns.append(" less terrible ")
        anss.append("less terrible than what/whom? less terrible compared to what/whom? ")
        flag = 1
    if " more terrific " in msgs:
        qtns.append(" more terrific ")
        anss.append("more terrific than what/whom? more terrific compared to what/whom? ")
        flag = 1
    if " less terrific " in msgs:
        qtns.append(" less terrific ")
        anss.append("less terrific than what/whom? less terrific compared to what/whom? ")
        flag = 1
    if " more testimonial " in msgs:
        qtns.append(" more testimonial ")
        anss.append("more testimonial than what/whom? more testimonial compared to what/whom? ")
        flag = 1
    if " less testimonial " in msgs:
        qtns.append(" less testimonial ")
        anss.append("less testimonial than what/whom? less testimonial compared to what/whom? ")
        flag = 1
    if " more thankful " in msgs:
        qtns.append(" more thankful ")
        anss.append("more thankful than what/whom? more thankful compared to what/whom? ")
        flag = 1
    if " less thankful " in msgs:
        qtns.append(" less thankful ")
        anss.append("less thankful than what/whom? less thankful compared to what/whom? ")
        flag = 1
    if " more thankworthy " in msgs:
        qtns.append(" more thankworthy ")
        anss.append("more thankworthy than what/whom? more thankworthy compared to what/whom? ")
        flag = 1
    if " less thankworthy " in msgs:
        qtns.append(" less thankworthy ")
        anss.append("less thankworthy than what/whom? less thankworthy compared to what/whom? ")
        flag = 1
    if " more therapeutic " in msgs:
        qtns.append(" more therapeutic ")
        anss.append("more therapeutic than what/whom? more therapeutic compared to what/whom? ")
        flag = 1
    if " less therapeutic " in msgs:
        qtns.append(" less therapeutic ")
        anss.append("less therapeutic than what/whom? less therapeutic compared to what/whom? ")
        flag = 1
    if " more thick " in msgs:
        qtns.append(" more thick ")
        anss.append("more thick than what/whom? more thick compared to what/whom? ")
        flag = 1
    if " less thick " in msgs:
        qtns.append(" less thick ")
        anss.append("less thick than what/whom? less thick compared to what/whom? ")
        flag = 1
    if " more thicker " in msgs:
        qtns.append(" more thicker ")
        anss.append("more thicker than what/whom? more thicker compared to what/whom? ")
        flag = 1
    if " less thicker " in msgs:
        qtns.append(" less thicker ")
        anss.append("less thicker than what/whom? less thicker compared to what/whom? ")
        flag = 1
    if " more thin " in msgs:
        qtns.append(" more thin ")
        anss.append("more thin than what/whom? more thin compared to what/whom? ")
        flag = 1
    if " less thin " in msgs:
        qtns.append(" less thin ")
        anss.append("less thin than what/whom? less thin compared to what/whom? ")
        flag = 1
    if " more thinner " in msgs:
        qtns.append(" more thinner ")
        anss.append("more thinner than what/whom? more thinner compared to what/whom? ")
        flag = 1
    if " less thinner " in msgs:
        qtns.append(" less thinner ")
        anss.append("less thinner than what/whom? less thinner compared to what/whom? ")
        flag = 1
    if " more thirstier " in msgs:
        qtns.append(" more thirstier ")
        anss.append("more thirstier than what/whom? more thirstier compared to what/whom? ")
        flag = 1
    if " less thirstier " in msgs:
        qtns.append(" less thirstier ")
        anss.append("less thirstier than what/whom? less thirstier compared to what/whom? ")
        flag = 1
    if " more thorough " in msgs:
        qtns.append(" more thorough ")
        anss.append("more thorough than what/whom? more thorough compared to what/whom? ")
        flag = 1
    if " less thorough " in msgs:
        qtns.append(" less thorough ")
        anss.append("less thorough than what/whom? less thorough compared to what/whom? ")
        flag = 1
    if " more thoughtful " in msgs:
        qtns.append(" more thoughtful ")
        anss.append("more thoughtful than what/whom? more thoughtful compared to what/whom? ")
        flag = 1
    if " less thoughtful " in msgs:
        qtns.append(" less thoughtful ")
        anss.append("less thoughtful than what/whom? less thoughtful compared to what/whom? ")
        flag = 1
    if " more tiny " in msgs:
        qtns.append(" more tiny ")
        anss.append("more tiny than what/whom? more tiny compared to what/whom? ")
        flag = 1
    if " less tiny " in msgs:
        qtns.append(" less tiny ")
        anss.append("less tiny than what/whom? less tiny compared to what/whom? ")
        flag = 1
    if " more tinier " in msgs:
        qtns.append(" more tinier ")
        anss.append("more tinier than what/whom? more tinier compared to what/whom? ")
        flag = 1
    if " less tinier " in msgs:
        qtns.append(" less tinier ")
        anss.append("less tinier than what/whom? less tinier compared to what/whom? ")
        flag = 1
    if " more tired " in msgs:
        qtns.append(" more tired ")
        anss.append("more tired than what/whom? more tired compared to what/whom? ")
        flag = 1
    if " less tired " in msgs:
        qtns.append(" less tired ")
        anss.append("less tired than what/whom? less tired compared to what/whom? ")
        flag = 1
    if " more tougher " in msgs:
        qtns.append(" more tougher ")
        anss.append("more tougher than what/whom? more tougher compared to what/whom? ")
        flag = 1
    if " less tougher " in msgs:
        qtns.append(" less tougher ")
        anss.append("less tougher than what/whom? less tougher compared to what/whom? ")
        flag = 1
    if " more truer " in msgs:
        qtns.append(" more truer ")
        anss.append("more truer than what/whom? more truer compared to what/whom? ")
        flag = 1
    if " less truer " in msgs:
        qtns.append(" less truer ")
        anss.append("less truer than what/whom? less truer compared to what/whom? ")
        flag = 1
    if " more uglier " in msgs:
        qtns.append(" more uglier ")
        anss.append("more uglier than what/whom? more uglier compared to what/whom? ")
        flag = 1
    if " less uglier " in msgs:
        qtns.append(" less uglier ")
        anss.append("less uglier than what/whom? less uglier compared to what/whom? ")
        flag = 1
    if " more unique " in msgs:
        qtns.append(" more unique ")
        anss.append("more unique than what/whom? more unique compared to what/whom? ")
        flag = 1
    if " less unique " in msgs:
        qtns.append(" less unique ")
        anss.append("less unique than what/whom? less unique compared to what/whom? ")
        flag = 1
    if " more untidy " in msgs:
        qtns.append(" more untidy ")
        anss.append("more untidy than what/whom? more untidy compared to what/whom? ")
        flag = 1
    if " less untidy " in msgs:
        qtns.append(" less untidy ")
        anss.append("less untidy than what/whom? less untidy compared to what/whom? ")
        flag = 1
    if " more upset " in msgs:
        qtns.append(" more upset ")
        anss.append("more upset than what/whom? more upset compared to what/whom? ")
        flag = 1
    if " less upset " in msgs:
        qtns.append(" less upset ")
        anss.append("less upset than what/whom? less upset compared to what/whom? ")
        flag = 1
    if " more victorious " in msgs:
        qtns.append(" more victorious ")
        anss.append("more victorious than what/whom? more victorious compared to what/whom? ")
        flag = 1
    if " less victorious " in msgs:
        qtns.append(" less victorious ")
        anss.append("less victorious than what/whom? less victorious compared to what/whom? ")
        flag = 1
    if " more violent " in msgs:
        qtns.append(" more violent ")
        anss.append("more violent than what/whom? more violent compared to what/whom? ")
        flag = 1
    if " less violent " in msgs:
        qtns.append(" less violent ")
        anss.append("less violent than what/whom? less violent compared to what/whom? ")
        flag = 1
    if " more vulgar " in msgs:
        qtns.append(" more vulgar ")
        anss.append("more vulgar than what/whom? more vulgar compared to what/whom? ")
        flag = 1
    if " less vulgar " in msgs:
        qtns.append(" less vulgar ")
        anss.append("less vulgar than what/whom? less vulgar compared to what/whom? ")
        flag = 1
    if " more warmer " in msgs:
        qtns.append(" more warmer ")
        anss.append("more warmer than what/whom? more warmer compared to what/whom? ")
        flag = 1
    if " less warmer " in msgs:
        qtns.append(" less warmer ")
        anss.append("less warmer than what/whom? less warmer compared to what/whom? ")
        flag = 1
    if " more weaker " in msgs:
        qtns.append(" more weaker ")
        anss.append("more weaker than what/whom? more weaker compared to what/whom? ")
        flag = 1
    if " less weaker " in msgs:
        qtns.append(" less weaker ")
        anss.append("less weaker than what/whom? less weaker compared to what/whom? ")
        flag = 1
    if " more wealthier " in msgs:
        qtns.append(" more wealthier ")
        anss.append("more wealthier than what/whom? more wealthier compared to what/whom? ")
        flag = 1
    if " less wealthier " in msgs:
        qtns.append(" less wealthier ")
        anss.append("less wealthier than what/whom? less wealthier compared to what/whom? ")
        flag = 1
    if " more weirder " in msgs:
        qtns.append(" more weirder ")
        anss.append("more weirder than what/whom? more weirder compared to what/whom? ")
        flag = 1
    if " less weirder " in msgs:
        qtns.append(" less weirder ")
        anss.append("less weirder than what/whom? less weirder compared to what/whom? ")
        flag = 1
    if " more wetter " in msgs:
        qtns.append(" more wetter ")
        anss.append("more wetter than what/whom? more wetter compared to what/whom? ")
        flag = 1
    if " less wetter " in msgs:
        qtns.append(" less wetter ")
        anss.append("less wetter than what/whom? less wetter compared to what/whom? ")
        flag = 1
    if " more wider " in msgs:
        qtns.append(" more wider ")
        anss.append("more wider than what/whom? more wider compared to what/whom? ")
        flag = 1
    if " less wider " in msgs:
        qtns.append(" less wider ")
        anss.append("less wider than what/whom? less wider compared to what/whom? ")
        flag = 1
    if " more wilder " in msgs:
        qtns.append(" more wilder ")
        anss.append("more wilder than what/whom? more wilder compared to what/whom? ")
        flag = 1
    if " less wilder " in msgs:
        qtns.append(" less wilder ")
        anss.append("less wilder than what/whom? less wilder compared to what/whom? ")
        flag = 1
    if " more windier " in msgs:
        qtns.append(" more windier ")
        anss.append("more windier than what/whom? more windier compared to what/whom? ")
        flag = 1
    if " less windier " in msgs:
        qtns.append(" less windier ")
        anss.append("less windier than what/whom? less windier compared to what/whom? ")
        flag = 1
    if " more wiser " in msgs:
        qtns.append(" more wiser ")
        anss.append("more wiser than what/whom? more wiser compared to what/whom? ")
        flag = 1
    if " less wiser " in msgs:
        qtns.append(" less wiser ")
        anss.append("less wiser than what/whom? less wiser compared to what/whom? ")
        flag = 1
    if " more wittier " in msgs:
        qtns.append(" more wittier ")
        anss.append("more wittier than what/whom? more wittier compared to what/whom? ")
        flag = 1
    if " less wittier " in msgs:
        qtns.append(" less wittier ")
        anss.append("less wittier than what/whom? less wittier compared to what/whom? ")
        flag = 1
    if " more wonderful " in msgs:
        qtns.append(" more wonderful ")
        anss.append("more wonderful than what/whom? more wonderful compared to what/whom? ")
        flag = 1
    if " less wonderful " in msgs:
        qtns.append(" less wonderful ")
        anss.append("less wonderful than what/whom? less wonderful compared to what/whom? ")
        flag = 1
    if " more worldlier " in msgs:
        qtns.append(" more worldlier ")
        anss.append("more worldlier than what/whom? more worldlier compared to what/whom? ")
        flag = 1
    if " less worldlier " in msgs:
        qtns.append(" less worldlier ")
        anss.append("less worldlier than what/whom? less worldlier compared to what/whom? ")
        flag = 1
    if " more worried " in msgs:
        qtns.append(" more worried ")
        anss.append("more worried than what/whom? more worried compared to what/whom? ")
        flag = 1
    if " less worried " in msgs:
        qtns.append(" less worried ")
        anss.append("less worried than what/whom? less worried compared to what/whom? ")
        flag = 1
    if " more worthier " in msgs:
        qtns.append(" more worthier ")
        anss.append("more worthier than what/whom? more worthier compared to what/whom? ")
        flag = 1
    if " less worthier " in msgs:
        qtns.append(" less worthier ")
        anss.append("less worthier than what/whom? less worthier compared to what/whom? ")
        flag = 1
    if " more younger " in msgs:
        qtns.append(" more younger ")
        anss.append("more younger than what/whom? more younger compared to what/whom? ")
        flag = 1
    if " less younger " in msgs:
        qtns.append(" less younger ")
        anss.append("less younger than what/whom? less younger compared to what/whom? ")
        flag = 1
    if " more youthful " in msgs:
        qtns.append(" more youthful ")
        anss.append("more youthful than what/whom? more youthful compared to what/whom? ")
        flag = 1
    if " less youthful " in msgs:
        qtns.append(" less youthful ")
        anss.append("less youthful than what/whom? less youthful compared to what/whom? ")
        flag = 1
    if " more zealous " in msgs:
        qtns.append(" more zealous ")
        anss.append("more zealous than what/whom? more zealous compared to what/whom? ")
        flag = 1
    if " less zealous " in msgs:
        qtns.append(" less zealous ")
        anss.append("less zealous than what/whom? less zealous compared to what/whom? ")
        flag = 1
    if " abactinal " in msgs:
        qtns.append(" abactinal ")
        anss.append("How specifically do you know abactinal? According to whom? ")
        flag = 1
    if " abandoned " in msgs:
        qtns.append(" abandoned ")
        anss.append("How specifically do you know abandoned? According to whom? ")
        flag = 1
    if " abashed " in msgs:
        qtns.append(" abashed ")
        anss.append("How specifically do you know abashed? According to whom? ")
        flag = 1
    if " abatable " in msgs:
        qtns.append(" abatable ")
        anss.append("How specifically do you know abatable? According to whom? ")
        flag = 1
    if " abatic " in msgs:
        qtns.append(" abatic ")
        anss.append("How specifically do you know abatic? According to whom? ")
        flag = 1
    if " abaxial " in msgs:
        qtns.append(" abaxial ")
        anss.append("How specifically do you know abaxial? According to whom? ")
        flag = 1
    if " abbatial " in msgs:
        qtns.append(" abbatial ")
        anss.append("How specifically do you know abbatial? According to whom? ")
        flag = 1
    if " abbreviated " in msgs:
        qtns.append(" abbreviated ")
        anss.append("How specifically do you know abbreviated? According to whom? ")
        flag = 1
    if " abducent " in msgs:
        qtns.append(" abducent ")
        anss.append("How specifically do you know abducent? According to whom? ")
        flag = 1
    if " abducting " in msgs:
        qtns.append(" abducting ")
        anss.append("How specifically do you know abducting? According to whom? ")
        flag = 1
    if " aberrant " in msgs:
        qtns.append(" aberrant ")
        anss.append("How specifically do you know aberrant? According to whom? ")
        flag = 1
    if " abeyant " in msgs:
        qtns.append(" abeyant ")
        anss.append("How specifically do you know abeyant? According to whom? ")
        flag = 1
    if " abhorrent " in msgs:
        qtns.append(" abhorrent ")
        anss.append("How specifically do you know abhorrent? According to whom? ")
        flag = 1
    if " abiding " in msgs:
        qtns.append(" abiding ")
        anss.append("How specifically do you know abiding? According to whom? ")
        flag = 1
    if " abient " in msgs:
        qtns.append(" abient ")
        anss.append("How specifically do you know abient? According to whom? ")
        flag = 1
    if " abundant " in msgs:
        qtns.append(" abundant ")
        anss.append("How specifically do you know abundant? According to whom? ")
        flag = 1
    if " accurate " in msgs:
        qtns.append(" accurate ")
        anss.append("How specifically do you know accurate? According to whom? ")
        flag = 1
    if " addicted " in msgs:
        qtns.append(" addicted ")
        anss.append("How specifically do you know addicted? According to whom? ")
        flag = 1
    if " adorable " in msgs:
        qtns.append(" adorable ")
        anss.append("How specifically do you know adorable? According to whom? ")
        flag = 1
    if " adventurous " in msgs:
        qtns.append(" adventurous ")
        anss.append("How specifically do you know adventurous? According to whom? ")
        flag = 1
    if " afraid " in msgs:
        qtns.append(" afraid ")
        anss.append("How specifically do you know afraid? According to whom? ")
        flag = 1
    if " aggressive " in msgs:
        qtns.append(" aggressive ")
        anss.append("How specifically do you know aggressive? According to whom? ")
        flag = 1
    if " alcoholic " in msgs:
        qtns.append(" alcoholic ")
        anss.append("How specifically do you know alcoholic? According to whom? ")
        flag = 1
    if " alert " in msgs:
        qtns.append(" alert ")
        anss.append("How specifically do you know alert? According to whom? ")
        flag = 1
    if " aloof " in msgs:
        qtns.append(" aloof ")
        anss.append("How specifically do you know aloof? According to whom? ")
        flag = 1
    if " ambitious " in msgs:
        qtns.append(" ambitious ")
        anss.append("How specifically do you know ambitious? According to whom? ")
        flag = 1
    if " ancient " in msgs:
        qtns.append(" ancient ")
        anss.append("How specifically do you know ancient? According to whom? ")
        flag = 1
    if " angriest " in msgs:
        qtns.append(" angriest ")
        anss.append("How specifically do you know angriest? According to whom? ")
        flag = 1
    if " animated " in msgs:
        qtns.append(" animated ")
        anss.append("How specifically do you know animated? According to whom? ")
        flag = 1
    if " annoying " in msgs:
        qtns.append(" annoying ")
        anss.append("How specifically do you know annoying? According to whom? ")
        flag = 1
    if " anxious " in msgs:
        qtns.append(" anxious ")
        anss.append("How specifically do you know anxious? According to whom? ")
        flag = 1
    if " arrogant " in msgs:
        qtns.append(" arrogant ")
        anss.append("How specifically do you know arrogant? According to whom? ")
        flag = 1
    if " ashamed " in msgs:
        qtns.append(" ashamed ")
        anss.append("How specifically do you know ashamed? According to whom? ")
        flag = 1
    if " attractive " in msgs:
        qtns.append(" attractive ")
        anss.append("How specifically do you know attractive? According to whom? ")
        flag = 1
    if " auspicious " in msgs:
        qtns.append(" auspicious ")
        anss.append("How specifically do you know auspicious? According to whom? ")
        flag = 1
    if " awesome " in msgs:
        qtns.append(" awesome ")
        anss.append("How specifically do you know awesome? According to whom? ")
        flag = 1
    if " awful " in msgs:
        qtns.append(" awful ")
        anss.append("How specifically do you know awful? According to whom? ")
        flag = 1
    if " baddest " in msgs:
        qtns.append(" baddest ")
        anss.append("How specifically do you know baddest? According to whom? ")
        flag = 1
    if " worst " in msgs:
        qtns.append(" worst ")
        anss.append("How specifically do you know worst? According to whom? ")
        flag = 1
    if " barren " in msgs:
        qtns.append(" barren ")
        anss.append("How specifically do you know barren? According to whom? ")
        flag = 1
    if " barricaded " in msgs:
        qtns.append(" barricaded ")
        anss.append("How specifically do you know barricaded? According to whom? ")
        flag = 1
    if " barytic " in msgs:
        qtns.append(" barytic ")
        anss.append("How specifically do you know barytic? According to whom? ")
        flag = 1
    if " basal " in msgs:
        qtns.append(" basal ")
        anss.append("How specifically do you know basal? According to whom? ")
        flag = 1
    if " basaltic " in msgs:
        qtns.append(" basaltic ")
        anss.append("How specifically do you know basaltic? According to whom? ")
        flag = 1
    if " baseborn " in msgs:
        qtns.append(" baseborn ")
        anss.append("How specifically do you know baseborn? According to whom? ")
        flag = 1
    if " based " in msgs:
        qtns.append(" based ")
        anss.append("How specifically do you know based? According to whom? ")
        flag = 1
    if " baseless " in msgs:
        qtns.append(" baseless ")
        anss.append("How specifically do you know baseless? According to whom? ")
        flag = 1
    if " bashful " in msgs:
        qtns.append(" bashful ")
        anss.append("How specifically do you know bashful? According to whom? ")
        flag = 1
    if " basic " in msgs:
        qtns.append(" basic ")
        anss.append("How specifically do you know basic? According to whom? ")
        flag = 1
    if " bathyal " in msgs:
        qtns.append(" bathyal ")
        anss.append("How specifically do you know bathyal? According to whom? ")
        flag = 1
    if " battleful " in msgs:
        qtns.append(" battleful ")
        anss.append("How specifically do you know battleful? According to whom? ")
        flag = 1
    if " battlemented " in msgs:
        qtns.append(" battlemented ")
        anss.append("How specifically do you know battlemented? According to whom? ")
        flag = 1
    if " batty " in msgs:
        qtns.append(" batty ")
        anss.append("How specifically do you know batty? According to whom? ")
        flag = 1
    if " batwing " in msgs:
        qtns.append(" batwing ")
        anss.append("How specifically do you know batwing? According to whom? ")
        flag = 1
    if " beautiful " in msgs:
        qtns.append(" beautiful ")
        anss.append("How specifically do you know beautiful? According to whom? ")
        flag = 1
    if " belligerent " in msgs:
        qtns.append(" belligerent ")
        anss.append("How specifically do you know belligerent? According to whom? ")
        flag = 1
    if " beneficial " in msgs:
        qtns.append(" beneficial ")
        anss.append("How specifically do you know beneficial? According to whom? ")
        flag = 1
    if " biased " in msgs:
        qtns.append(" biased ")
        anss.append("How specifically do you know biased? According to whom? ")
        flag = 1
    if " biggest " in msgs:
        qtns.append(" biggest ")
        anss.append("How specifically do you know biggest? According to whom? ")
        flag = 1
    if " bitter " in msgs:
        qtns.append(" bitter ")
        anss.append("How specifically do you know bitter? According to whom? ")
        flag = 1
    if " bitterest " in msgs:
        qtns.append(" bitterest ")
        anss.append("How specifically do you know bitterest? According to whom? ")
        flag = 1
    if " bizarre " in msgs:
        qtns.append(" bizarre ")
        anss.append("How specifically do you know bizarre? According to whom? ")
        flag = 1
    if " blackest " in msgs:
        qtns.append(" blackest ")
        anss.append("How specifically do you know blackest? According to whom? ")
        flag = 1
    if " blandest " in msgs:
        qtns.append(" blandest ")
        anss.append("How specifically do you know blandest? According to whom? ")
        flag = 1
    if " bloodiest " in msgs:
        qtns.append(" bloodiest ")
        anss.append("How specifically do you know bloodiest? According to whom? ")
        flag = 1
    if " bluest " in msgs:
        qtns.append(" bluest ")
        anss.append("How specifically do you know bluest? According to whom? ")
        flag = 1
    if " boldest " in msgs:
        qtns.append(" boldest ")
        anss.append("How specifically do you know boldest? According to whom? ")
        flag = 1
    if " boring " in msgs:
        qtns.append(" boring ")
        anss.append("How specifically do you know boring? According to whom? ")
        flag = 1
    if " bossiest " in msgs:
        qtns.append(" bossiest ")
        anss.append("How specifically do you know bossiest? According to whom? ")
        flag = 1
    if " brainy " in msgs:
        qtns.append(" brainy ")
        anss.append("How specifically do you know brainy? According to whom? ")
        flag = 1
    if " brainiest " in msgs:
        qtns.append(" brainiest ")
        anss.append("How specifically do you know brainiest? According to whom? ")
        flag = 1
    if " bravest " in msgs:
        qtns.append(" bravest ")
        anss.append("How specifically do you know bravest? According to whom? ")
        flag = 1
    if " briefest " in msgs:
        qtns.append(" briefest ")
        anss.append("How specifically do you know briefest? According to whom? ")
        flag = 1
    if " brightest " in msgs:
        qtns.append(" brightest ")
        anss.append("How specifically do you know brightest? According to whom? ")
        flag = 1
    if " broadest " in msgs:
        qtns.append(" broadest ")
        anss.append("How specifically do you know broadest? According to whom? ")
        flag = 1
    if " broken " in msgs:
        qtns.append(" broken ")
        anss.append("How specifically do you know broken? According to whom? ")
        flag = 1
    if " busiest " in msgs:
        qtns.append(" busiest ")
        anss.append("How specifically do you know busiest? According to whom? ")
        flag = 1
    if " calmest " in msgs:
        qtns.append(" calmest ")
        anss.append("How specifically do you know calmest? According to whom? ")
        flag = 1
    if " capable " in msgs:
        qtns.append(" capable ")
        anss.append("How specifically do you know capable? According to whom? ")
        flag = 1
    if " careful " in msgs:
        qtns.append(" careful ")
        anss.append("How specifically do you know careful? According to whom? ")
        flag = 1
    if " careless " in msgs:
        qtns.append(" careless ")
        anss.append("How specifically do you know careless? According to whom? ")
        flag = 1
    if " caring " in msgs:
        qtns.append(" caring ")
        anss.append("How specifically do you know caring? According to whom? ")
        flag = 1
    if " cautious " in msgs:
        qtns.append(" cautious ")
        anss.append("How specifically do you know cautious? According to whom? ")
        flag = 1
    if " charming " in msgs:
        qtns.append(" charming ")
        anss.append("How specifically do you know charming? According to whom? ")
        flag = 1
    if " cheapest " in msgs:
        qtns.append(" cheapest ")
        anss.append("How specifically do you know cheapest? According to whom? ")
        flag = 1
    if " cheerful " in msgs:
        qtns.append(" cheerful ")
        anss.append("How specifically do you know cheerful? According to whom? ")
        flag = 1
    if " chewiest " in msgs:
        qtns.append(" chewiest ")
        anss.append("How specifically do you know chewiest? According to whom? ")
        flag = 1
    if " chubbiest " in msgs:
        qtns.append(" chubbiest ")
        anss.append("How specifically do you know chubbiest? According to whom? ")
        flag = 1
    if " classiest " in msgs:
        qtns.append(" classiest ")
        anss.append("How specifically do you know classiest? According to whom? ")
        flag = 1
    if " cleanest " in msgs:
        qtns.append(" cleanest ")
        anss.append("How specifically do you know cleanest? According to whom? ")
        flag = 1
    if " clearest " in msgs:
        qtns.append(" clearest ")
        anss.append("How specifically do you know clearest? According to whom? ")
        flag = 1
    if " cleverest " in msgs:
        qtns.append(" cleverest ")
        anss.append("How specifically do you know cleverest? According to whom? ")
        flag = 1
    if " closest " in msgs:
        qtns.append(" closest ")
        anss.append("How specifically do you know closest? According to whom? ")
        flag = 1
    if " cloudiest " in msgs:
        qtns.append(" cloudiest ")
        anss.append("How specifically do you know cloudiest? According to whom? ")
        flag = 1
    if " clumsiest " in msgs:
        qtns.append(" clumsiest ")
        anss.append("How specifically do you know clumsiest? According to whom? ")
        flag = 1
    if " coarsest " in msgs:
        qtns.append(" coarsest ")
        anss.append("How specifically do you know coarsest? According to whom? ")
        flag = 1
    if " coldest " in msgs:
        qtns.append(" coldest ")
        anss.append("How specifically do you know coldest? According to whom? ")
        flag = 1
    if " colorful " in msgs:
        qtns.append(" colorful ")
        anss.append("How specifically do you know colorful? According to whom? ")
        flag = 1
    if " comfortable " in msgs:
        qtns.append(" comfortable ")
        anss.append("How specifically do you know comfortable? According to whom? ")
        flag = 1
    if " concerned " in msgs:
        qtns.append(" concerned ")
        anss.append("How specifically do you know concerned? According to whom? ")
        flag = 1
    if " confused " in msgs:
        qtns.append(" confused ")
        anss.append("How specifically do you know confused? According to whom? ")
        flag = 1
    if " consistent " in msgs:
        qtns.append(" consistent ")
        anss.append("How specifically do you know consistent? According to whom? ")
        flag = 1
    if " coolest " in msgs:
        qtns.append(" coolest ")
        anss.append("How specifically do you know coolest? According to whom? ")
        flag = 1
    if " craziest " in msgs:
        qtns.append(" craziest ")
        anss.append("How specifically do you know craziest? According to whom? ")
        flag = 1
    if " creamiest " in msgs:
        qtns.append(" creamiest ")
        anss.append("How specifically do you know creamiest? According to whom? ")
        flag = 1
    if " creepiest " in msgs:
        qtns.append(" creepiest ")
        anss.append("How specifically do you know creepiest? According to whom? ")
        flag = 1
    if " crispiest " in msgs:
        qtns.append(" crispiest ")
        anss.append("How specifically do you know crispiest? According to whom? ")
        flag = 1
    if " crowded " in msgs:
        qtns.append(" crowded ")
        anss.append("How specifically do you know crowded? According to whom? ")
        flag = 1
    if " cruelest " in msgs:
        qtns.append(" cruelest ")
        anss.append("How specifically do you know cruelest? According to whom? ")
        flag = 1
    if " crunchiest " in msgs:
        qtns.append(" crunchiest ")
        anss.append("How specifically do you know crunchiest? According to whom? ")
        flag = 1
    if " curious " in msgs:
        qtns.append(" curious ")
        anss.append("How specifically do you know curious? According to whom? ")
        flag = 1
    if " curliest " in msgs:
        qtns.append(" curliest ")
        anss.append("How specifically do you know curliest? According to whom? ")
        flag = 1
    if " curviest " in msgs:
        qtns.append(" curviest ")
        anss.append("How specifically do you know curviest? According to whom? ")
        flag = 1
    if " cutest " in msgs:
        qtns.append(" cutest ")
        anss.append("How specifically do you know cutest? According to whom? ")
        flag = 1
    if " daftest " in msgs:
        qtns.append(" daftest ")
        anss.append("How specifically do you know daftest? According to whom? ")
        flag = 1
    if " daily " in msgs:
        qtns.append(" daily ")
        anss.append("How specifically do you know daily? According to whom? ")
        flag = 1
    if " dainty " in msgs:
        qtns.append(" dainty ")
        anss.append("How specifically do you know dainty? According to whom? ")
        flag = 1
    if " damaged " in msgs:
        qtns.append(" damaged ")
        anss.append("How specifically do you know damaged? According to whom? ")
        flag = 1
    if " damn " in msgs:
        qtns.append(" damn ")
        anss.append("How specifically do you know damn? According to whom? ")
        flag = 1
    if " damning " in msgs:
        qtns.append(" damning ")
        anss.append("How specifically do you know damning? According to whom? ")
        flag = 1
    if " dampest " in msgs:
        qtns.append(" dampest ")
        anss.append("How specifically do you know dampest? According to whom? ")
        flag = 1
    if " dampish " in msgs:
        qtns.append(" dampish ")
        anss.append("How specifically do you know dampish? According to whom? ")
        flag = 1
    if " dangerous " in msgs:
        qtns.append(" dangerous ")
        anss.append("How specifically do you know dangerous? According to whom? ")
        flag = 1
    if " darkest " in msgs:
        qtns.append(" darkest ")
        anss.append("How specifically do you know darkest? According to whom? ")
        flag = 1
    if " darkling " in msgs:
        qtns.append(" darkling ")
        anss.append("How specifically do you know darkling? According to whom? ")
        flag = 1
    if " darned " in msgs:
        qtns.append(" darned ")
        anss.append("How specifically do you know darned? According to whom? ")
        flag = 1
    if " dauntless " in msgs:
        qtns.append(" dauntless ")
        anss.append("How specifically do you know dauntless? According to whom? ")
        flag = 1
    if " daylong " in msgs:
        qtns.append(" daylong ")
        anss.append("How specifically do you know daylong? According to whom? ")
        flag = 1
    if " deadliest " in msgs:
        qtns.append(" deadliest ")
        anss.append("How specifically do you know deadliest? According to whom? ")
        flag = 1
    if " deepest " in msgs:
        qtns.append(" deepest ")
        anss.append("How specifically do you know deepest? According to whom? ")
        flag = 1
    if " defective " in msgs:
        qtns.append(" defective ")
        anss.append("How specifically do you know defective? According to whom? ")
        flag = 1
    if " delicate " in msgs:
        qtns.append(" delicate ")
        anss.append("How specifically do you know delicate? According to whom? ")
        flag = 1
    if " delicious " in msgs:
        qtns.append(" delicious ")
        anss.append("How specifically do you know delicious? According to whom? ")
        flag = 1
    if " densest " in msgs:
        qtns.append(" densest ")
        anss.append("How specifically do you know densest? According to whom? ")
        flag = 1
    if " depressed " in msgs:
        qtns.append(" depressed ")
        anss.append("How specifically do you know depressed? According to whom? ")
        flag = 1
    if " determined " in msgs:
        qtns.append(" determined ")
        anss.append("How specifically do you know determined? According to whom? ")
        flag = 1
    if " different " in msgs:
        qtns.append(" different ")
        anss.append("How specifically do you know different? According to whom? ")
        flag = 1
    if " difficult " in msgs:
        qtns.append(" difficult ")
        anss.append("How specifically do you know difficult? According to whom? ")
        flag = 1
    if " dirtiest " in msgs:
        qtns.append(" dirtiest ")
        anss.append("How specifically do you know dirtiest? According to whom? ")
        flag = 1
    if " disgusting " in msgs:
        qtns.append(" disgusting ")
        anss.append("How specifically do you know disgusting? According to whom? ")
        flag = 1
    if " driest " in msgs:
        qtns.append(" driest ")
        anss.append("How specifically do you know driest? According to whom? ")
        flag = 1
    if " dullest " in msgs:
        qtns.append(" dullest ")
        anss.append("How specifically do you know dullest? According to whom? ")
        flag = 1
    if " dumbest " in msgs:
        qtns.append(" dumbest ")
        anss.append("How specifically do you know dumbest? According to whom? ")
        flag = 1
    if " dustiest " in msgs:
        qtns.append(" dustiest ")
        anss.append("How specifically do you know dustiest? According to whom? ")
        flag = 1
    if " earliest " in msgs:
        qtns.append(" earliest ")
        anss.append("How specifically do you know earliest? According to whom? ")
        flag = 1
    if " easiest " in msgs:
        qtns.append(" easiest ")
        anss.append("How specifically do you know easiest? According to whom? ")
        flag = 1
    if " educated " in msgs:
        qtns.append(" educated ")
        anss.append("How specifically do you know educated? According to whom? ")
        flag = 1
    if " efficient " in msgs:
        qtns.append(" efficient ")
        anss.append("How specifically do you know efficient? According to whom? ")
        flag = 1
    if " elderly " in msgs:
        qtns.append(" elderly ")
        anss.append("How specifically do you know elderly? According to whom? ")
        flag = 1
    if " elegant " in msgs:
        qtns.append(" elegant ")
        anss.append("How specifically do you know elegant? According to whom? ")
        flag = 1
    if " embarrassed " in msgs:
        qtns.append(" embarrassed ")
        anss.append("How specifically do you know embarrassed? According to whom? ")
        flag = 1
    if " emptiest " in msgs:
        qtns.append(" emptiest ")
        anss.append("How specifically do you know emptiest? According to whom? ")
        flag = 1
    if " encouraging " in msgs:
        qtns.append(" encouraging ")
        anss.append("How specifically do you know encouraging? According to whom? ")
        flag = 1
    if " enthusiastic " in msgs:
        qtns.append(" enthusiastic ")
        anss.append("How specifically do you know enthusiastic? According to whom? ")
        flag = 1
    if " excellent " in msgs:
        qtns.append(" excellent ")
        anss.append("How specifically do you know excellent? According to whom? ")
        flag = 1
    if " exciting " in msgs:
        qtns.append(" exciting ")
        anss.append("How specifically do you know exciting? According to whom? ")
        flag = 1
    if " expensive " in msgs:
        qtns.append(" expensive ")
        anss.append("How specifically do you know expensive? According to whom? ")
        flag = 1
    if " fabulous " in msgs:
        qtns.append(" fabulous ")
        anss.append("How specifically do you know fabulous? According to whom? ")
        flag = 1
    if " faintest " in msgs:
        qtns.append(" faintest ")
        anss.append("How specifically do you know faintest? According to whom? ")
        flag = 1
    if " fairest " in msgs:
        qtns.append(" fairest ")
        anss.append("How specifically do you know fairest? According to whom? ")
        flag = 1
    if " faithful " in msgs:
        qtns.append(" faithful ")
        anss.append("How specifically do you know faithful? According to whom? ")
        flag = 1
    if " famous " in msgs:
        qtns.append(" famous ")
        anss.append("How specifically do you know famous? According to whom? ")
        flag = 1
    if " fanciest " in msgs:
        qtns.append(" fanciest ")
        anss.append("How specifically do you know fanciest? According to whom? ")
        flag = 1
    if " fantastic " in msgs:
        qtns.append(" fantastic ")
        anss.append("How specifically do you know fantastic? According to whom? ")
        flag = 1
    if " farthest " in msgs:
        qtns.append(" farthest ")
        anss.append("How specifically do you know farthest? According to whom? ")
        flag = 1
    if " fastest " in msgs:
        qtns.append(" fastest ")
        anss.append("How specifically do you know fastest? According to whom? ")
        flag = 1
    if " fattest " in msgs:
        qtns.append(" fattest ")
        anss.append("How specifically do you know fattest? According to whom? ")
        flag = 1
    if " fearful " in msgs:
        qtns.append(" fearful ")
        anss.append("How specifically do you know fearful? According to whom? ")
        flag = 1
    if " fearless " in msgs:
        qtns.append(" fearless ")
        anss.append("How specifically do you know fearless? According to whom? ")
        flag = 1
    if " fertile " in msgs:
        qtns.append(" fertile ")
        anss.append("How specifically do you know fertile? According to whom? ")
        flag = 1
    if " fewest " in msgs:
        qtns.append(" fewest ")
        anss.append("How specifically do you know fewest? According to whom? ")
        flag = 1
    if " fiercest " in msgs:
        qtns.append(" fiercest ")
        anss.append("How specifically do you know fiercest? According to whom? ")
        flag = 1
    if " filthiest " in msgs:
        qtns.append(" filthiest ")
        anss.append("How specifically do you know filthiest? According to whom? ")
        flag = 1
    if " finest " in msgs:
        qtns.append(" finest ")
        anss.append("How specifically do you know finest? According to whom? ")
        flag = 1
    if " firmest " in msgs:
        qtns.append(" firmest ")
        anss.append("How specifically do you know firmest? According to whom? ")
        flag = 1
    if " fittest " in msgs:
        qtns.append(" fittest ")
        anss.append("How specifically do you know fittest? According to whom? ")
        flag = 1
    if " flakiest " in msgs:
        qtns.append(" flakiest ")
        anss.append("How specifically do you know flakiest? According to whom? ")
        flag = 1
    if " flattest " in msgs:
        qtns.append(" flattest ")
        anss.append("How specifically do you know flattest? According to whom? ")
        flag = 1
    if " foolish " in msgs:
        qtns.append(" foolish ")
        anss.append("How specifically do you know foolish? According to whom? ")
        flag = 1
    if " forgetful " in msgs:
        qtns.append(" forgetful ")
        anss.append("How specifically do you know forgetful? According to whom? ")
        flag = 1
    if " freshest " in msgs:
        qtns.append(" freshest ")
        anss.append("How specifically do you know freshest? According to whom? ")
        flag = 1
    if " friendliest " in msgs:
        qtns.append(" friendliest ")
        anss.append("How specifically do you know friendliest? According to whom? ")
        flag = 1
    if " fullest " in msgs:
        qtns.append(" fullest ")
        anss.append("How specifically do you know fullest? According to whom? ")
        flag = 1
    if " funniest " in msgs:
        qtns.append(" funniest ")
        anss.append("How specifically do you know funniest? According to whom? ")
        flag = 1
    if " gentlest " in msgs:
        qtns.append(" gentlest ")
        anss.append("How specifically do you know gentlest? According to whom? ")
        flag = 1
    if " glamorous " in msgs:
        qtns.append(" glamorous ")
        anss.append("How specifically do you know glamorous? According to whom? ")
        flag = 1
    if " gloomiest " in msgs:
        qtns.append(" gloomiest ")
        anss.append("How specifically do you know gloomiest? According to whom? ")
        flag = 1
    if " glorious " in msgs:
        qtns.append(" glorious ")
        anss.append("How specifically do you know glorious? According to whom? ")
        flag = 1
    if " best " in msgs:
        qtns.append(" best ")
        anss.append("How specifically do you know best? According to whom? ")
        flag = 1
    if " gorgeous " in msgs:
        qtns.append(" gorgeous ")
        anss.append("How specifically do you know gorgeous? According to whom? ")
        flag = 1
    if " graceful " in msgs:
        qtns.append(" graceful ")
        anss.append("How specifically do you know graceful? According to whom? ")
        flag = 1
    if " grandest " in msgs:
        qtns.append(" grandest ")
        anss.append("How specifically do you know grandest? According to whom? ")
        flag = 1
    if " grateful " in msgs:
        qtns.append(" grateful ")
        anss.append("How specifically do you know grateful? According to whom? ")
        flag = 1
    if " gravest " in msgs:
        qtns.append(" gravest ")
        anss.append("How specifically do you know gravest? According to whom? ")
        flag = 1
    if " greasiest " in msgs:
        qtns.append(" greasiest ")
        anss.append("How specifically do you know greasiest? According to whom? ")
        flag = 1
    if " greatest " in msgs:
        qtns.append(" greatest ")
        anss.append("How specifically do you know greatest? According to whom? ")
        flag = 1
    if " greediest " in msgs:
        qtns.append(" greediest ")
        anss.append("How specifically do you know greediest? According to whom? ")
        flag = 1
    if " greenest " in msgs:
        qtns.append(" greenest ")
        anss.append("How specifically do you know greenest? According to whom? ")
        flag = 1
    if " grossest " in msgs:
        qtns.append(" grossest ")
        anss.append("How specifically do you know grossest? According to whom? ")
        flag = 1
    if " guiltiest " in msgs:
        qtns.append(" guiltiest ")
        anss.append("How specifically do you know guiltiest? According to whom? ")
        flag = 1
    if " hairiest " in msgs:
        qtns.append(" hairiest ")
        anss.append("How specifically do you know hairiest? According to whom? ")
        flag = 1
    if " handsome " in msgs:
        qtns.append(" handsome ")
        anss.append("How specifically do you know handsome? According to whom? ")
        flag = 1
    if " handiest " in msgs:
        qtns.append(" handiest ")
        anss.append("How specifically do you know handiest? According to whom? ")
        flag = 1
    if " happiest " in msgs:
        qtns.append(" happiest ")
        anss.append("How specifically do you know happiest? According to whom? ")
        flag = 1
    if " hardest " in msgs:
        qtns.append(" hardest ")
        anss.append("How specifically do you know hardest? According to whom? ")
        flag = 1
    if " harshest " in msgs:
        qtns.append(" harshest ")
        anss.append("How specifically do you know harshest? According to whom? ")
        flag = 1
    if " healthiest " in msgs:
        qtns.append(" healthiest ")
        anss.append("How specifically do you know healthiest? According to whom? ")
        flag = 1
    if " heaviest " in msgs:
        qtns.append(" heaviest ")
        anss.append("How specifically do you know heaviest? According to whom? ")
        flag = 1
    if " helpful " in msgs:
        qtns.append(" helpful ")
        anss.append("How specifically do you know helpful? According to whom? ")
        flag = 1
    if " highest " in msgs:
        qtns.append(" highest ")
        anss.append("How specifically do you know highest? According to whom? ")
        flag = 1
    if " hilarious " in msgs:
        qtns.append(" hilarious ")
        anss.append("How specifically do you know hilarious? According to whom? ")
        flag = 1
    if " hippest " in msgs:
        qtns.append(" hippest ")
        anss.append("How specifically do you know hippest? According to whom? ")
        flag = 1
    if " historical " in msgs:
        qtns.append(" historical ")
        anss.append("How specifically do you know historical? According to whom? ")
        flag = 1
    if " horrible " in msgs:
        qtns.append(" horrible ")
        anss.append("How specifically do you know horrible? According to whom? ")
        flag = 1
    if " hottest " in msgs:
        qtns.append(" hottest ")
        anss.append("How specifically do you know hottest? According to whom? ")
        flag = 1
    if " huge " in msgs:
        qtns.append(" huge ")
        anss.append("How specifically do you know huge? According to whom? ")
        flag = 1
    if " humblest " in msgs:
        qtns.append(" humblest ")
        anss.append("How specifically do you know humblest? According to whom? ")
        flag = 1
    if " humorous " in msgs:
        qtns.append(" humorous ")
        anss.append("How specifically do you know humorous? According to whom? ")
        flag = 1
    if " hungriest " in msgs:
        qtns.append(" hungriest ")
        anss.append("How specifically do you know hungriest? According to whom? ")
        flag = 1
    if " iciest " in msgs:
        qtns.append(" iciest ")
        anss.append("How specifically do you know iciest? According to whom? ")
        flag = 1
    if " ignorant " in msgs:
        qtns.append(" ignorant ")
        anss.append("How specifically do you know ignorant? According to whom? ")
        flag = 1
    if " illegal " in msgs:
        qtns.append(" illegal ")
        anss.append("How specifically do you know illegal? According to whom? ")
        flag = 1
    if " imaginary " in msgs:
        qtns.append(" imaginary ")
        anss.append("How specifically do you know imaginary? According to whom? ")
        flag = 1
    if " impolite " in msgs:
        qtns.append(" impolite ")
        anss.append("How specifically do you know impolite? According to whom? ")
        flag = 1
    if " important " in msgs:
        qtns.append(" important ")
        anss.append("How specifically do you know important? According to whom? ")
        flag = 1
    if " impossible " in msgs:
        qtns.append(" impossible ")
        anss.append("How specifically do you know impossible? According to whom? ")
        flag = 1
    if " innocent " in msgs:
        qtns.append(" innocent ")
        anss.append("How specifically do you know innocent? According to whom? ")
        flag = 1
    if " intelligent " in msgs:
        qtns.append(" intelligent ")
        anss.append("How specifically do you know intelligent? According to whom? ")
        flag = 1
    if " interesting " in msgs:
        qtns.append(" interesting ")
        anss.append("How specifically do you know interesting? According to whom? ")
        flag = 1
    if " itchiest " in msgs:
        qtns.append(" itchiest ")
        anss.append("How specifically do you know itchiest? According to whom? ")
        flag = 1
    if " jealous " in msgs:
        qtns.append(" jealous ")
        anss.append("How specifically do you know jealous? According to whom? ")
        flag = 1
    if " jolliest " in msgs:
        qtns.append(" jolliest ")
        anss.append("How specifically do you know jolliest? According to whom? ")
        flag = 1
    if " juiciest " in msgs:
        qtns.append(" juiciest ")
        anss.append("How specifically do you know juiciest? According to whom? ")
        flag = 1
    if " juvenile " in msgs:
        qtns.append(" juvenile ")
        anss.append("How specifically do you know juvenile? According to whom? ")
        flag = 1
    if " kindest " in msgs:
        qtns.append(" kindest ")
        anss.append("How specifically do you know kindest? According to whom? ")
        flag = 1
    if " largest " in msgs:
        qtns.append(" largest ")
        anss.append("How specifically do you know largest? According to whom? ")
        flag = 1
    if " latest " in msgs:
        qtns.append(" latest ")
        anss.append("How specifically do you know latest? According to whom? ")
        flag = 1
    if " laziest " in msgs:
        qtns.append(" laziest ")
        anss.append("How specifically do you know laziest? According to whom? ")
        flag = 1
    if " legal " in msgs:
        qtns.append(" legal ")
        anss.append("How specifically do you know legal? According to whom? ")
        flag = 1
    if " lightest " in msgs:
        qtns.append(" lightest ")
        anss.append("How specifically do you know lightest? According to whom? ")
        flag = 1
    if " likeliest " in msgs:
        qtns.append(" likeliest ")
        anss.append("How specifically do you know likeliest? According to whom? ")
        flag = 1
    if " literate " in msgs:
        qtns.append(" literate ")
        anss.append("How specifically do you know literate? According to whom? ")
        flag = 1
    if " littlest " in msgs:
        qtns.append(" littlest ")
        anss.append("How specifically do you know littlest? According to whom? ")
        flag = 1
    if " least " in msgs:
        qtns.append(" least ")
        anss.append("How specifically do you know least? According to whom? ")
        flag = 1
    if " liveliest " in msgs:
        qtns.append(" liveliest ")
        anss.append("How specifically do you know liveliest? According to whom? ")
        flag = 1
    if " loneliest " in msgs:
        qtns.append(" loneliest ")
        anss.append("How specifically do you know loneliest? According to whom? ")
        flag = 1
    if " longest " in msgs:
        qtns.append(" longest ")
        anss.append("How specifically do you know longest? According to whom? ")
        flag = 1
    if " loudest " in msgs:
        qtns.append(" loudest ")
        anss.append("How specifically do you know loudest? According to whom? ")
        flag = 1
    if " loveliest " in msgs:
        qtns.append(" loveliest ")
        anss.append("How specifically do you know loveliest? According to whom? ")
        flag = 1
    if " lowest " in msgs:
        qtns.append(" lowest ")
        anss.append("How specifically do you know lowest? According to whom? ")
        flag = 1
    if " luckiest " in msgs:
        qtns.append(" luckiest ")
        anss.append("How specifically do you know luckiest? According to whom? ")
        flag = 1
    if " macho " in msgs:
        qtns.append(" macho ")
        anss.append("How specifically do you know macho? According to whom? ")
        flag = 1
    if " maddest " in msgs:
        qtns.append(" maddest ")
        anss.append("How specifically do you know maddest? According to whom? ")
        flag = 1
    if " magical " in msgs:
        qtns.append(" magical ")
        anss.append("How specifically do you know magical? According to whom? ")
        flag = 1
    if " magnificent " in msgs:
        qtns.append(" magnificent ")
        anss.append("How specifically do you know magnificent? According to whom? ")
        flag = 1
    if " most " in msgs:
        qtns.append(" most ")
        anss.append("How specifically do you know most? According to whom? ")
        flag = 1
    if " massive " in msgs:
        qtns.append(" massive ")
        anss.append("How specifically do you know massive? According to whom? ")
        flag = 1
    if " mature " in msgs:
        qtns.append(" mature ")
        anss.append("How specifically do you know mature? According to whom? ")
        flag = 1
    if " meanest " in msgs:
        qtns.append(" meanest ")
        anss.append("How specifically do you know meanest? According to whom? ")
        flag = 1
    if " messiest " in msgs:
        qtns.append(" messiest ")
        anss.append("How specifically do you know messiest? According to whom? ")
        flag = 1
    if " mildest " in msgs:
        qtns.append(" mildest ")
        anss.append("How specifically do you know mildest? According to whom? ")
        flag = 1
    if " modern " in msgs:
        qtns.append(" modern ")
        anss.append("How specifically do you know modern? According to whom? ")
        flag = 1
    if " moistest " in msgs:
        qtns.append(" moistest ")
        anss.append("How specifically do you know moistest? According to whom? ")
        flag = 1
    if " narrowest " in msgs:
        qtns.append(" narrowest ")
        anss.append("How specifically do you know narrowest? According to whom? ")
        flag = 1
    if " nastiest " in msgs:
        qtns.append(" nastiest ")
        anss.append("How specifically do you know nastiest? According to whom? ")
        flag = 1
    if " naughtiest " in msgs:
        qtns.append(" naughtiest ")
        anss.append("How specifically do you know naughtiest? According to whom? ")
        flag = 1
    if " nearest " in msgs:
        qtns.append(" nearest ")
        anss.append("How specifically do you know nearest? According to whom? ")
        flag = 1
    if " neatest " in msgs:
        qtns.append(" neatest ")
        anss.append("How specifically do you know neatest? According to whom? ")
        flag = 1
    if " neediest " in msgs:
        qtns.append(" neediest ")
        anss.append("How specifically do you know neediest? According to whom? ")
        flag = 1
    if " nervous " in msgs:
        qtns.append(" nervous ")
        anss.append("How specifically do you know nervous? According to whom? ")
        flag = 1
    if " newest " in msgs:
        qtns.append(" newest ")
        anss.append("How specifically do you know newest? According to whom? ")
        flag = 1
    if " nicest " in msgs:
        qtns.append(" nicest ")
        anss.append("How specifically do you know nicest? According to whom? ")
        flag = 1
    if " noisiest " in msgs:
        qtns.append(" noisiest ")
        anss.append("How specifically do you know noisiest? According to whom? ")
        flag = 1
    if " nutritious " in msgs:
        qtns.append(" nutritious ")
        anss.append("How specifically do you know nutritious? According to whom? ")
        flag = 1
    if " obedient " in msgs:
        qtns.append(" obedient ")
        anss.append("How specifically do you know obedient? According to whom? ")
        flag = 1
    if " obese " in msgs:
        qtns.append(" obese ")
        anss.append("How specifically do you know obese? According to whom? ")
        flag = 1
    if " obnoxious " in msgs:
        qtns.append(" obnoxious ")
        anss.append("How specifically do you know obnoxious? According to whom? ")
        flag = 1
    if " oddest " in msgs:
        qtns.append(" oddest ")
        anss.append("How specifically do you know oddest? According to whom? ")
        flag = 1
    if " oiliest " in msgs:
        qtns.append(" oiliest ")
        anss.append("How specifically do you know oiliest? According to whom? ")
        flag = 1
    if " oldest " in msgs:
        qtns.append(" oldest ")
        anss.append("How specifically do you know oldest? According to whom? ")
        flag = 1
    if " ?eldest " in msgs:
        qtns.append(" ?eldest ")
        anss.append("How specifically do you know ?eldest? According to whom? ")
        flag = 1
    if " overconfident " in msgs:
        qtns.append(" overconfident ")
        anss.append("How specifically do you know overconfident? According to whom? ")
        flag = 1
    if " peaceful " in msgs:
        qtns.append(" peaceful ")
        anss.append("How specifically do you know peaceful? According to whom? ")
        flag = 1
    if " perfect " in msgs:
        qtns.append(" perfect ")
        anss.append("How specifically do you know perfect? According to whom? ")
        flag = 1
    if " pinkest " in msgs:
        qtns.append(" pinkest ")
        anss.append("How specifically do you know pinkest? According to whom? ")
        flag = 1
    if " plainest " in msgs:
        qtns.append(" plainest ")
        anss.append("How specifically do you know plainest? According to whom? ")
        flag = 1
    if " politest " in msgs:
        qtns.append(" politest ")
        anss.append("How specifically do you know politest? According to whom? ")
        flag = 1
    if " poorest " in msgs:
        qtns.append(" poorest ")
        anss.append("How specifically do you know poorest? According to whom? ")
        flag = 1
    if " popular " in msgs:
        qtns.append(" popular ")
        anss.append("How specifically do you know popular? According to whom? ")
        flag = 1
    if " powerful " in msgs:
        qtns.append(" powerful ")
        anss.append("How specifically do you know powerful? According to whom? ")
        flag = 1
    if " precious " in msgs:
        qtns.append(" precious ")
        anss.append("How specifically do you know precious? According to whom? ")
        flag = 1
    if " prettiest " in msgs:
        qtns.append(" prettiest ")
        anss.append("How specifically do you know prettiest? According to whom? ")
        flag = 1
    if " proudest " in msgs:
        qtns.append(" proudest ")
        anss.append("How specifically do you know proudest? According to whom? ")
        flag = 1
    if " purest " in msgs:
        qtns.append(" purest ")
        anss.append("How specifically do you know purest? According to whom? ")
        flag = 1
    if " quickest " in msgs:
        qtns.append(" quickest ")
        anss.append("How specifically do you know quickest? According to whom? ")
        flag = 1
    if " quietest " in msgs:
        qtns.append(" quietest ")
        anss.append("How specifically do you know quietest? According to whom? ")
        flag = 1
    if " rapidest " in msgs:
        qtns.append(" rapidest ")
        anss.append("How specifically do you know rapidest? According to whom? ")
        flag = 1
    if " rarest " in msgs:
        qtns.append(" rarest ")
        anss.append("How specifically do you know rarest? According to whom? ")
        flag = 1
    if " rawest " in msgs:
        qtns.append(" rawest ")
        anss.append("How specifically do you know rawest? According to whom? ")
        flag = 1
    if " reddest " in msgs:
        qtns.append(" reddest ")
        anss.append("How specifically do you know reddest? According to whom? ")
        flag = 1
    if " remarkable " in msgs:
        qtns.append(" remarkable ")
        anss.append("How specifically do you know remarkable? According to whom? ")
        flag = 1
    if " responsible " in msgs:
        qtns.append(" responsible ")
        anss.append("How specifically do you know responsible? According to whom? ")
        flag = 1
    if " richest " in msgs:
        qtns.append(" richest ")
        anss.append("How specifically do you know richest? According to whom? ")
        flag = 1
    if " ripest " in msgs:
        qtns.append(" ripest ")
        anss.append("How specifically do you know ripest? According to whom? ")
        flag = 1
    if " riskiest " in msgs:
        qtns.append(" riskiest ")
        anss.append("How specifically do you know riskiest? According to whom? ")
        flag = 1
    if " romantic " in msgs:
        qtns.append(" romantic ")
        anss.append("How specifically do you know romantic? According to whom? ")
        flag = 1
    if " roomiest " in msgs:
        qtns.append(" roomiest ")
        anss.append("How specifically do you know roomiest? According to whom? ")
        flag = 1
    if " roughest " in msgs:
        qtns.append(" roughest ")
        anss.append("How specifically do you know roughest? According to whom? ")
        flag = 1
    if " royal " in msgs:
        qtns.append(" royal ")
        anss.append("How specifically do you know royal? According to whom? ")
        flag = 1
    if " rudest " in msgs:
        qtns.append(" rudest ")
        anss.append("How specifically do you know rudest? According to whom? ")
        flag = 1
    if " rustiest " in msgs:
        qtns.append(" rustiest ")
        anss.append("How specifically do you know rustiest? According to whom? ")
        flag = 1
    if " saddest " in msgs:
        qtns.append(" saddest ")
        anss.append("How specifically do you know saddest? According to whom? ")
        flag = 1
    if " safest " in msgs:
        qtns.append(" safest ")
        anss.append("How specifically do you know safest? According to whom? ")
        flag = 1
    if " saltiest " in msgs:
        qtns.append(" saltiest ")
        anss.append("How specifically do you know saltiest? According to whom? ")
        flag = 1
    if " sanest " in msgs:
        qtns.append(" sanest ")
        anss.append("How specifically do you know sanest? According to whom? ")
        flag = 1
    if " scariest " in msgs:
        qtns.append(" scariest ")
        anss.append("How specifically do you know scariest? According to whom? ")
        flag = 1
    if " scintillating " in msgs:
        qtns.append(" scintillating ")
        anss.append("How specifically do you know scintillating? According to whom? ")
        flag = 1
    if " secretive " in msgs:
        qtns.append(" secretive ")
        anss.append("How specifically do you know secretive? According to whom? ")
        flag = 1
    if " selfish " in msgs:
        qtns.append(" selfish ")
        anss.append("How specifically do you know selfish? According to whom? ")
        flag = 1
    if " serious " in msgs:
        qtns.append(" serious ")
        anss.append("How specifically do you know serious? According to whom? ")
        flag = 1
    if " shallowest " in msgs:
        qtns.append(" shallowest ")
        anss.append("How specifically do you know shallowest? According to whom? ")
        flag = 1
    if " sharpest " in msgs:
        qtns.append(" sharpest ")
        anss.append("How specifically do you know sharpest? According to whom? ")
        flag = 1
    if " shiniest " in msgs:
        qtns.append(" shiniest ")
        anss.append("How specifically do you know shiniest? According to whom? ")
        flag = 1
    if " shocking " in msgs:
        qtns.append(" shocking ")
        anss.append("How specifically do you know shocking? According to whom? ")
        flag = 1
    if " shortest " in msgs:
        qtns.append(" shortest ")
        anss.append("How specifically do you know shortest? According to whom? ")
        flag = 1
    if " shyest " in msgs:
        qtns.append(" shyest ")
        anss.append("How specifically do you know shyest? According to whom? ")
        flag = 1
    if " silliest " in msgs:
        qtns.append(" silliest ")
        anss.append("How specifically do you know silliest? According to whom? ")
        flag = 1
    if " simplest " in msgs:
        qtns.append(" simplest ")
        anss.append("How specifically do you know simplest? According to whom? ")
        flag = 1
    if " sincere " in msgs:
        qtns.append(" sincere ")
        anss.append("How specifically do you know sincere? According to whom? ")
        flag = 1
    if " sincerest " in msgs:
        qtns.append(" sincerest ")
        anss.append("How specifically do you know sincerest? According to whom? ")
        flag = 1
    if " skinniest " in msgs:
        qtns.append(" skinniest ")
        anss.append("How specifically do you know skinniest? According to whom? ")
        flag = 1
    if " sleepiest " in msgs:
        qtns.append(" sleepiest ")
        anss.append("How specifically do you know sleepiest? According to whom? ")
        flag = 1
    if " slimmest " in msgs:
        qtns.append(" slimmest ")
        anss.append("How specifically do you know slimmest? According to whom? ")
        flag = 1
    if " slimiest " in msgs:
        qtns.append(" slimiest ")
        anss.append("How specifically do you know slimiest? According to whom? ")
        flag = 1
    if " slowest " in msgs:
        qtns.append(" slowest ")
        anss.append("How specifically do you know slowest? According to whom? ")
        flag = 1
    if " smallest " in msgs:
        qtns.append(" smallest ")
        anss.append("How specifically do you know smallest? According to whom? ")
        flag = 1
    if " smartest " in msgs:
        qtns.append(" smartest ")
        anss.append("How specifically do you know smartest? According to whom? ")
        flag = 1
    if " smelliest " in msgs:
        qtns.append(" smelliest ")
        anss.append("How specifically do you know smelliest? According to whom? ")
        flag = 1
    if " smokiest " in msgs:
        qtns.append(" smokiest ")
        anss.append("How specifically do you know smokiest? According to whom? ")
        flag = 1
    if " smoothest " in msgs:
        qtns.append(" smoothest ")
        anss.append("How specifically do you know smoothest? According to whom? ")
        flag = 1
    if " softest " in msgs:
        qtns.append(" softest ")
        anss.append("How specifically do you know softest? According to whom? ")
        flag = 1
    if " soonest " in msgs:
        qtns.append(" soonest ")
        anss.append("How specifically do you know soonest? According to whom? ")
        flag = 1
    if " sorest " in msgs:
        qtns.append(" sorest ")
        anss.append("How specifically do you know sorest? According to whom? ")
        flag = 1
    if " sorriest " in msgs:
        qtns.append(" sorriest ")
        anss.append("How specifically do you know sorriest? According to whom? ")
        flag = 1
    if " sourest " in msgs:
        qtns.append(" sourest ")
        anss.append("How specifically do you know sourest? According to whom? ")
        flag = 1
    if " spiciest " in msgs:
        qtns.append(" spiciest ")
        anss.append("How specifically do you know spiciest? According to whom? ")
        flag = 1
    if " spiritual " in msgs:
        qtns.append(" spiritual ")
        anss.append("How specifically do you know spiritual? According to whom? ")
        flag = 1
    if " splendid " in msgs:
        qtns.append(" splendid ")
        anss.append("How specifically do you know splendid? According to whom? ")
        flag = 1
    if " steepest " in msgs:
        qtns.append(" steepest ")
        anss.append("How specifically do you know steepest? According to whom? ")
        flag = 1
    if " stingiest " in msgs:
        qtns.append(" stingiest ")
        anss.append("How specifically do you know stingiest? According to whom? ")
        flag = 1
    if " strangest " in msgs:
        qtns.append(" strangest ")
        anss.append("How specifically do you know strangest? According to whom? ")
        flag = 1
    if " strictest " in msgs:
        qtns.append(" strictest ")
        anss.append("How specifically do you know strictest? According to whom? ")
        flag = 1
    if " strongest " in msgs:
        qtns.append(" strongest ")
        anss.append("How specifically do you know strongest? According to whom? ")
        flag = 1
    if " successful " in msgs:
        qtns.append(" successful ")
        anss.append("How specifically do you know successful? According to whom? ")
        flag = 1
    if " sunniest " in msgs:
        qtns.append(" sunniest ")
        anss.append("How specifically do you know sunniest? According to whom? ")
        flag = 1
    if " sweatiest " in msgs:
        qtns.append(" sweatiest ")
        anss.append("How specifically do you know sweatiest? According to whom? ")
        flag = 1
    if " sweetest " in msgs:
        qtns.append(" sweetest ")
        anss.append("How specifically do you know sweetest? According to whom? ")
        flag = 1
    if " tactful " in msgs:
        qtns.append(" tactful ")
        anss.append("How specifically do you know tactful? According to whom? ")
        flag = 1
    if " tailor-made " in msgs:
        qtns.append(" tailor-made ")
        anss.append("How specifically do you know tailor-made? According to whom? ")
        flag = 1
    if " take-charge " in msgs:
        qtns.append(" take-charge ")
        anss.append("How specifically do you know take-charge? According to whom? ")
        flag = 1
    if " talented " in msgs:
        qtns.append(" talented ")
        anss.append("How specifically do you know talented? According to whom? ")
        flag = 1
    if " tallest " in msgs:
        qtns.append(" tallest ")
        anss.append("How specifically do you know tallest? According to whom? ")
        flag = 1
    if " tannest " in msgs:
        qtns.append(" tannest ")
        anss.append("How specifically do you know tannest? According to whom? ")
        flag = 1
    if " tangible " in msgs:
        qtns.append(" tangible ")
        anss.append("How specifically do you know tangible? According to whom? ")
        flag = 1
    if " tasteful " in msgs:
        qtns.append(" tasteful ")
        anss.append("How specifically do you know tasteful? According to whom? ")
        flag = 1
    if " tasty " in msgs:
        qtns.append(" tasty ")
        anss.append("How specifically do you know tasty? According to whom? ")
        flag = 1
    if " tastiest " in msgs:
        qtns.append(" tastiest ")
        anss.append("How specifically do you know tastiest? According to whom? ")
        flag = 1
    if " teachable " in msgs:
        qtns.append(" teachable ")
        anss.append("How specifically do you know teachable? According to whom? ")
        flag = 1
    if " teeming " in msgs:
        qtns.append(" teeming ")
        anss.append("How specifically do you know teeming? According to whom? ")
        flag = 1
    if " tempean " in msgs:
        qtns.append(" tempean ")
        anss.append("How specifically do you know tempean? According to whom? ")
        flag = 1
    if " temperate " in msgs:
        qtns.append(" temperate ")
        anss.append("How specifically do you know temperate? According to whom? ")
        flag = 1
    if " tenable " in msgs:
        qtns.append(" tenable ")
        anss.append("How specifically do you know tenable? According to whom? ")
        flag = 1
    if " tenacious " in msgs:
        qtns.append(" tenacious ")
        anss.append("How specifically do you know tenacious? According to whom? ")
        flag = 1
    if " tender-hearted " in msgs:
        qtns.append(" tender-hearted ")
        anss.append("How specifically do you know tender-hearted? According to whom? ")
        flag = 1
    if " tense " in msgs:
        qtns.append(" tense ")
        anss.append("How specifically do you know tense? According to whom? ")
        flag = 1
    if " terrible " in msgs:
        qtns.append(" terrible ")
        anss.append("How specifically do you know terrible? According to whom? ")
        flag = 1
    if " terrific " in msgs:
        qtns.append(" terrific ")
        anss.append("How specifically do you know terrific? According to whom? ")
        flag = 1
    if " testimonial " in msgs:
        qtns.append(" testimonial ")
        anss.append("How specifically do you know testimonial? According to whom? ")
        flag = 1
    if " thankful " in msgs:
        qtns.append(" thankful ")
        anss.append("How specifically do you know thankful? According to whom? ")
        flag = 1
    if " thankworthy " in msgs:
        qtns.append(" thankworthy ")
        anss.append("How specifically do you know thankworthy? According to whom? ")
        flag = 1
    if " therapeutic " in msgs:
        qtns.append(" therapeutic ")
        anss.append("How specifically do you know therapeutic? According to whom? ")
        flag = 1
    if " thick " in msgs:
        qtns.append(" thick ")
        anss.append("How specifically do you know thick? According to whom? ")
        flag = 1
    if " thickest " in msgs:
        qtns.append(" thickest ")
        anss.append("How specifically do you know thickest? According to whom? ")
        flag = 1
    if " thin " in msgs:
        qtns.append(" thin ")
        anss.append("How specifically do you know thin? According to whom? ")
        flag = 1
    if " thinnest " in msgs:
        qtns.append(" thinnest ")
        anss.append("How specifically do you know thinnest? According to whom? ")
        flag = 1
    if " thirstiest " in msgs:
        qtns.append(" thirstiest ")
        anss.append("How specifically do you know thirstiest? According to whom? ")
        flag = 1
    if " thorough " in msgs:
        qtns.append(" thorough ")
        anss.append("How specifically do you know thorough? According to whom? ")
        flag = 1
    if " thoughtful " in msgs:
        qtns.append(" thoughtful ")
        anss.append("How specifically do you know thoughtful? According to whom? ")
        flag = 1
    if " tiny " in msgs:
        qtns.append(" tiny ")
        anss.append("How specifically do you know tiny? According to whom? ")
        flag = 1
    if " tiniest " in msgs:
        qtns.append(" tiniest ")
        anss.append("How specifically do you know tiniest? According to whom? ")
        flag = 1
    if " tired " in msgs:
        qtns.append(" tired ")
        anss.append("How specifically do you know tired? According to whom? ")
        flag = 1
    if " toughest " in msgs:
        qtns.append(" toughest ")
        anss.append("How specifically do you know toughest? According to whom? ")
        flag = 1
    if " truest " in msgs:
        qtns.append(" truest ")
        anss.append("How specifically do you know truest? According to whom? ")
        flag = 1
    if " ugliest " in msgs:
        qtns.append(" ugliest ")
        anss.append("How specifically do you know ugliest? According to whom? ")
        flag = 1
    if " unique " in msgs:
        qtns.append(" unique ")
        anss.append("How specifically do you know unique? According to whom? ")
        flag = 1
    if " untidy " in msgs:
        qtns.append(" untidy ")
        anss.append("How specifically do you know untidy? According to whom? ")
        flag = 1
    if " upset " in msgs:
        qtns.append(" upset ")
        anss.append("How specifically do you know upset? According to whom? ")
        flag = 1
    if " victorious " in msgs:
        qtns.append(" victorious ")
        anss.append("How specifically do you know victorious? According to whom? ")
        flag = 1
    if " violent " in msgs:
        qtns.append(" violent ")
        anss.append("How specifically do you know violent? According to whom? ")
        flag = 1
    if " vulgar " in msgs:
        qtns.append(" vulgar ")
        anss.append("How specifically do you know vulgar? According to whom? ")
        flag = 1
    if " warmest " in msgs:
        qtns.append(" warmest ")
        anss.append("How specifically do you know warmest? According to whom? ")
        flag = 1
    if " weakest " in msgs:
        qtns.append(" weakest ")
        anss.append("How specifically do you know weakest? According to whom? ")
        flag = 1
    if " wealthiest " in msgs:
        qtns.append(" wealthiest ")
        anss.append("How specifically do you know wealthiest? According to whom? ")
        flag = 1
    if " weirdest " in msgs:
        qtns.append(" weirdest ")
        anss.append("How specifically do you know weirdest? According to whom? ")
        flag = 1
    if " wettest " in msgs:
        qtns.append(" wettest ")
        anss.append("How specifically do you know wettest? According to whom? ")
        flag = 1
    if " widest " in msgs:
        qtns.append(" widest ")
        anss.append("How specifically do you know widest? According to whom? ")
        flag = 1
    if " wildest " in msgs:
        qtns.append(" wildest ")
        anss.append("How specifically do you know wildest? According to whom? ")
        flag = 1
    if " windiest " in msgs:
        qtns.append(" windiest ")
        anss.append("How specifically do you know windiest? According to whom? ")
        flag = 1
    if " wisest " in msgs:
        qtns.append(" wisest ")
        anss.append("How specifically do you know wisest? According to whom? ")
        flag = 1
    if " wittiest " in msgs:
        qtns.append(" wittiest ")
        anss.append("How specifically do you know wittiest? According to whom? ")
        flag = 1
    if " wonderful " in msgs:
        qtns.append(" wonderful ")
        anss.append("How specifically do you know wonderful? According to whom? ")
        flag = 1
    if " worldliest " in msgs:
        qtns.append(" worldliest ")
        anss.append("How specifically do you know worldliest? According to whom? ")
        flag = 1
    if " worried " in msgs:
        qtns.append(" worried ")
        anss.append("How specifically do you know worried? According to whom? ")
        flag = 1
    if " worthiest " in msgs:
        qtns.append(" worthiest ")
        anss.append("How specifically do you know worthiest? According to whom? ")
        flag = 1
    if " youngest " in msgs:
        qtns.append(" youngest ")
        anss.append("How specifically do you know youngest? According to whom? ")
        flag = 1
    if " youthful " in msgs:
        qtns.append(" youthful ")
        anss.append("How specifically do you know youthful? According to whom? ")
        flag = 1
    if " zealous " in msgs:
        qtns.append(" zealous ")
        anss.append("How specifically do you know zealous? According to whom? ")
        flag = 1
    if " ability " in msgs:
        qtns.append(" ability ")
        anss.append("Which ability ")
        flag = 1
    if " accountant " in msgs:
        qtns.append(" accountant ")
        anss.append("Which accountant ")
        flag = 1
    if " actor " in msgs:
        qtns.append(" actor ")
        anss.append("Which actor ")
        flag = 1
    if " actress " in msgs:
        qtns.append(" actress ")
        anss.append("Which actress ")
        flag = 1
    if " advantage " in msgs:
        qtns.append(" advantage ")
        anss.append("Which advantage ")
        flag = 1
    if " advice " in msgs:
        qtns.append(" advice ")
        anss.append("Which advice ")
        flag = 1
    if " agenda " in msgs:
        qtns.append(" agenda ")
        anss.append("Which agenda ")
        flag = 1
    if " apology " in msgs:
        qtns.append(" apology ")
        anss.append("Which apology ")
        flag = 1
    if " application " in msgs:
        qtns.append(" application ")
        anss.append("Which application ")
        flag = 1
    if " architect " in msgs:
        qtns.append(" architect ")
        anss.append("Which architect ")
        flag = 1
    if " artist " in msgs:
        qtns.append(" artist ")
        anss.append("Which artist ")
        flag = 1
    if " assistant " in msgs:
        qtns.append(" assistant ")
        anss.append("Which assistant ")
        flag = 1
    if " attorney " in msgs:
        qtns.append(" attorney ")
        anss.append("Which attorney ")
        flag = 1
    if " banker " in msgs:
        qtns.append(" banker ")
        anss.append("Which banker ")
        flag = 1
    if " barber " in msgs:
        qtns.append(" barber ")
        anss.append("Which barber ")
        flag = 1
    if " bartender " in msgs:
        qtns.append(" bartender ")
        anss.append("Which bartender ")
        flag = 1
    if " benefit " in msgs:
        qtns.append(" benefit ")
        anss.append("Which benefit ")
        flag = 1
    if " bill " in msgs:
        qtns.append(" bill ")
        anss.append("Which bill ")
        flag = 1
    if " bonus " in msgs:
        qtns.append(" bonus ")
        anss.append("Which bonus ")
        flag = 1
    if " bookkeeper " in msgs:
        qtns.append(" bookkeeper ")
        anss.append("Which bookkeeper ")
        flag = 1
    if " boss " in msgs:
        qtns.append(" boss ")
        anss.append("Which boss ")
        flag = 1
    if " brand " in msgs:
        qtns.append(" brand ")
        anss.append("Which brand ")
        flag = 1
    if " budget " in msgs:
        qtns.append(" budget ")
        anss.append("Which budget ")
        flag = 1
    if " builder " in msgs:
        qtns.append(" builder ")
        anss.append("Which builder ")
        flag = 1
    if " businessman " in msgs:
        qtns.append(" businessman ")
        anss.append("Which businessman ")
        flag = 1
    if " businessperson " in msgs:
        qtns.append(" businessperson ")
        anss.append("Which businessperson ")
        flag = 1
    if " businesswoman " in msgs:
        qtns.append(" businesswoman ")
        anss.append("Which businesswoman ")
        flag = 1
    if " butcher " in msgs:
        qtns.append(" butcher ")
        anss.append("Which butcher ")
        flag = 1
    if " capability " in msgs:
        qtns.append(" capability ")
        anss.append("Which capability ")
        flag = 1
    if " career " in msgs:
        qtns.append(" career ")
        anss.append("Which career ")
        flag = 1
    if " carpenter " in msgs:
        qtns.append(" carpenter ")
        anss.append("Which carpenter ")
        flag = 1
    if " cashier " in msgs:
        qtns.append(" cashier ")
        anss.append("Which cashier ")
        flag = 1
    if " change " in msgs:
        qtns.append(" change ")
        anss.append("Which change ")
        flag = 1
    if " chef " in msgs:
        qtns.append(" chef ")
        anss.append("Which chef ")
        flag = 1
    if " coach " in msgs:
        qtns.append(" coach ")
        anss.append("Which coach ")
        flag = 1
    if " company " in msgs:
        qtns.append(" company ")
        anss.append("Which company ")
        flag = 1
    if " competitions " in msgs:
        qtns.append(" competitions ")
        anss.append("Which competition ")
        flag = 1
    if " conclusion " in msgs:
        qtns.append(" conclusion ")
        anss.append("Which conclusion ")
        flag = 1
    if " controller " in msgs:
        qtns.append(" controller ")
        anss.append("Which controller ")
        flag = 1
    if " cost " in msgs:
        qtns.append(" cost ")
        anss.append("Which cost ")
        flag = 1
    if " cover letter " in msgs:
        qtns.append(" cover letter ")
        anss.append("Which cover letter ")
        flag = 1
    if " customer " in msgs:
        qtns.append(" customer ")
        anss.append("Which customer ")
        flag = 1
    if " deadline " in msgs:
        qtns.append(" deadline ")
        anss.append("Which deadline ")
        flag = 1
    if " debt " in msgs:
        qtns.append(" debt ")
        anss.append("Which debt ")
        flag = 1
    if " decision " in msgs:
        qtns.append(" decision ")
        anss.append("Which decision ")
        flag = 1
    if " decrease " in msgs:
        qtns.append(" decrease ")
        anss.append("Which decrease ")
        flag = 1
    if " defect " in msgs:
        qtns.append(" defect ")
        anss.append("Which defect ")
        flag = 1
    if " delivery " in msgs:
        qtns.append(" delivery ")
        anss.append("Which delivery ")
        flag = 1
    if " dentist " in msgs:
        qtns.append(" dentist ")
        anss.append("Which dentist ")
        flag = 1
    if " department " in msgs:
        qtns.append(" department ")
        anss.append("Which department ")
        flag = 1
    if " description " in msgs:
        qtns.append(" description ")
        anss.append("Which description ")
        flag = 1
    if " designer " in msgs:
        qtns.append(" designer ")
        anss.append("Which designer ")
        flag = 1
    if " developer " in msgs:
        qtns.append(" developer ")
        anss.append("Which developer ")
        flag = 1
    if " device " in msgs:
        qtns.append(" device ")
        anss.append("Which device ")
        flag = 1
    if " dietician " in msgs:
        qtns.append(" dietician ")
        anss.append("Which dietician ")
        flag = 1
    if " difference " in msgs:
        qtns.append(" difference ")
        anss.append("Which difference ")
        flag = 1
    if " director " in msgs:
        qtns.append(" director ")
        anss.append("Which director ")
        flag = 1
    if " doctor " in msgs:
        qtns.append(" doctor ")
        anss.append("Which doctor ")
        flag = 1
    if " economist " in msgs:
        qtns.append(" economist ")
        anss.append("Which economist ")
        flag = 1
    if " editor " in msgs:
        qtns.append(" editor ")
        anss.append("Which editor ")
        flag = 1
    if " electrician " in msgs:
        qtns.append(" electrician ")
        anss.append("Which electrician ")
        flag = 1
    if " employee " in msgs:
        qtns.append(" employee ")
        anss.append("Which employee ")
        flag = 1
    if " employer " in msgs:
        qtns.append(" employer ")
        anss.append("Which employer ")
        flag = 1
    if " engineer " in msgs:
        qtns.append(" engineer ")
        anss.append("Which engineer ")
        flag = 1
    if " equipment " in msgs:
        qtns.append(" equipment ")
        anss.append("Which equipment ")
        flag = 1
    if " error " in msgs:
        qtns.append(" error ")
        anss.append("Which error ")
        flag = 1
    if " estimate " in msgs:
        qtns.append(" estimate ")
        anss.append("Which estimate ")
        flag = 1
    if " experience " in msgs:
        qtns.append(" experience ")
        anss.append("Which experience ")
        flag = 1
    if " explanation " in msgs:
        qtns.append(" explanation ")
        anss.append("Which explanation ")
        flag = 1
    if " facility " in msgs:
        qtns.append(" facility ")
        anss.append("Which facility ")
        flag = 1
    if " factory " in msgs:
        qtns.append(" factory ")
        anss.append("Which factory ")
        flag = 1
    if " farmer " in msgs:
        qtns.append(" farmer ")
        anss.append("Which farmer ")
        flag = 1
    if " fault " in msgs:
        qtns.append(" fault ")
        anss.append("Which fault ")
        flag = 1
    if " feedback " in msgs:
        qtns.append(" feedback ")
        anss.append("Which feedback ")
        flag = 1
    if " filmmaker " in msgs:
        qtns.append(" filmmaker ")
        anss.append("Which filmmaker ")
        flag = 1
    if " fisherman " in msgs:
        qtns.append(" fisherman ")
        anss.append("Which fisherman ")
        flag = 1
    if " flight attendant " in msgs:
        qtns.append(" flight attendant ")
        anss.append("Which flight attendant ")
        flag = 1
    if " goal " in msgs:
        qtns.append(" goal ")
        anss.append("Which goal ")
        flag = 1
    if " growth " in msgs:
        qtns.append(" growth ")
        anss.append("Which growth ")
        flag = 1
    if " guarantee " in msgs:
        qtns.append(" guarantee ")
        anss.append("Which guarantee ")
        flag = 1
    if " hygienist " in msgs:
        qtns.append(" hygienist ")
        anss.append("Which hygienist ")
        flag = 1
    if " improvement " in msgs:
        qtns.append(" improvement ")
        anss.append("Which improvement ")
        flag = 1
    if " increase " in msgs:
        qtns.append(" increase ")
        anss.append("Which increase ")
        flag = 1
    if " industry " in msgs:
        qtns.append(" industry ")
        anss.append("Which industry ")
        flag = 1
    if " instruction " in msgs:
        qtns.append(" instruction ")
        anss.append("Which instruction ")
        flag = 1
    if " interest " in msgs:
        qtns.append(" interest ")
        anss.append("Which interest ")
        flag = 1
    if " interview " in msgs:
        qtns.append(" interview ")
        anss.append("Which interview ")
        flag = 1
    if " inventory " in msgs:
        qtns.append(" inventory ")
        anss.append("Which inventory ")
        flag = 1
    if " invoice " in msgs:
        qtns.append(" invoice ")
        anss.append("Which invoice ")
        flag = 1
    if " jeweler " in msgs:
        qtns.append(" jeweler ")
        anss.append("Which jeweler ")
        flag = 1
    if " job " in msgs:
        qtns.append(" job ")
        anss.append("Which job ")
        flag = 1
    if " judge " in msgs:
        qtns.append(" judge ")
        anss.append("Which judge ")
        flag = 1
    if " knowledge " in msgs:
        qtns.append(" knowledge ")
        anss.append("Which knowledge ")
        flag = 1
    if " lawyer " in msgs:
        qtns.append(" lawyer ")
        anss.append("Which lawyer ")
        flag = 1
    if " layoff " in msgs:
        qtns.append(" layoff ")
        anss.append("Which layoff ")
        flag = 1
    if " limit " in msgs:
        qtns.append(" limit ")
        anss.append("Which limit ")
        flag = 1
    if " loss " in msgs:
        qtns.append(" loss ")
        anss.append("Which loss ")
        flag = 1
    if " machine " in msgs:
        qtns.append(" machine ")
        anss.append("Which machine ")
        flag = 1
    if " manager " in msgs:
        qtns.append(" manager ")
        anss.append("Which manager ")
        flag = 1
    if " margin " in msgs:
        qtns.append(" margin ")
        anss.append("Which margin ")
        flag = 1
    if " market " in msgs:
        qtns.append(" market ")
        anss.append("Which market ")
        flag = 1
    if " mechanic " in msgs:
        qtns.append(" mechanic ")
        anss.append("Which mechanic ")
        flag = 1
    if " message " in msgs:
        qtns.append(" message ")
        anss.append("Which message ")
        flag = 1
    if " mistake " in msgs:
        qtns.append(" mistake ")
        anss.append("Which mistake ")
        flag = 1
    if " musician " in msgs:
        qtns.append(" musician ")
        anss.append("Which musician ")
        flag = 1
    if " nurse " in msgs:
        qtns.append(" nurse ")
        anss.append("Which nurse ")
        flag = 1
    if " nutritionist " in msgs:
        qtns.append(" nutritionist ")
        anss.append("Which nutritionist ")
        flag = 1
    if " objective " in msgs:
        qtns.append(" objective ")
        anss.append("Which objective ")
        flag = 1
    if " offer " in msgs:
        qtns.append(" offer ")
        anss.append("Which offer ")
        flag = 1
    if " opinion " in msgs:
        qtns.append(" opinion ")
        anss.append("Which opinion ")
        flag = 1
    if " optician " in msgs:
        qtns.append(" optician ")
        anss.append("Which optician ")
        flag = 1
    if " option " in msgs:
        qtns.append(" option ")
        anss.append("Which option ")
        flag = 1
    if " order " in msgs:
        qtns.append(" order ")
        anss.append("Which order ")
        flag = 1
    if " organisation " in msgs:
        qtns.append(" organisation ")
        anss.append("Which organisation ")
        flag = 1
    if " painter " in msgs:
        qtns.append(" painter ")
        anss.append("Which painter ")
        flag = 1
    if " payment " in msgs:
        qtns.append(" payment ")
        anss.append("Which payment ")
        flag = 1
    if " permission " in msgs:
        qtns.append(" permission ")
        anss.append("Which permission ")
        flag = 1
    if " pharmacist " in msgs:
        qtns.append(" pharmacist ")
        anss.append("Which pharmacist ")
        flag = 1
    if " photographer " in msgs:
        qtns.append(" photographer ")
        anss.append("Which photographer ")
        flag = 1
    if " physician " in msgs:
        qtns.append(" physician ")
        anss.append("Which physician ")
        flag = 1
    if " physician's assistant " in msgs:
        qtns.append(" physician's assistant ")
        anss.append("Which physician's assistant ")
        flag = 1
    if " pilot " in msgs:
        qtns.append(" pilot ")
        anss.append("Which pilot ")
        flag = 1
    if " plan " in msgs:
        qtns.append(" plan ")
        anss.append("Which plan ")
        flag = 1
    if " plumber " in msgs:
        qtns.append(" plumber ")
        anss.append("Which plumber ")
        flag = 1
    if " police officer " in msgs:
        qtns.append(" police officer ")
        anss.append("Which police officer ")
        flag = 1
    if " politician " in msgs:
        qtns.append(" politician ")
        anss.append("Which politician ")
        flag = 1
    if " preparation " in msgs:
        qtns.append(" preparation ")
        anss.append("Which preparation ")
        flag = 1
    if " price " in msgs:
        qtns.append(" price ")
        anss.append("Which price ")
        flag = 1
    if " product " in msgs:
        qtns.append(" product ")
        anss.append("Which product ")
        flag = 1
    if " production " in msgs:
        qtns.append(" production ")
        anss.append("Which production ")
        flag = 1
    if " professor " in msgs:
        qtns.append(" professor ")
        anss.append("Which professor ")
        flag = 1
    if " profit " in msgs:
        qtns.append(" profit ")
        anss.append("Which profit ")
        flag = 1
    if " programmer " in msgs:
        qtns.append(" programmer ")
        anss.append("Which programmer ")
        flag = 1
    if " promotion " in msgs:
        qtns.append(" promotion ")
        anss.append("Which promotion ")
        flag = 1
    if " psychologist " in msgs:
        qtns.append(" psychologist ")
        anss.append("Which psychologist ")
        flag = 1
    if " purchase " in msgs:
        qtns.append(" purchase ")
        anss.append("Which purchase ")
        flag = 1
    if " raise " in msgs:
        qtns.append(" raise ")
        anss.append("Which raise ")
        flag = 1
    if " receptionist " in msgs:
        qtns.append(" receptionist ")
        anss.append("Which receptionist ")
        flag = 1
    if " refund " in msgs:
        qtns.append(" refund ")
        anss.append("Which refund ")
        flag = 1
    if " reminder " in msgs:
        qtns.append(" reminder ")
        anss.append("Which reminder ")
        flag = 1
    if " report " in msgs:
        qtns.append(" report ")
        anss.append("Which report ")
        flag = 1
    if " responsibility " in msgs:
        qtns.append(" responsibility ")
        anss.append("Which responsibility ")
        flag = 1
    if " result " in msgs:
        qtns.append(" result ")
        anss.append("Which result ")
        flag = 1
    if " rise " in msgs:
        qtns.append(" rise ")
        anss.append("Which rise ")
        flag = 1
    if " risk " in msgs:
        qtns.append(" risk ")
        anss.append("Which risk ")
        flag = 1
    if " salary " in msgs:
        qtns.append(" salary ")
        anss.append("Which salary ")
        flag = 1
    if " sale " in msgs:
        qtns.append(" sale ")
        anss.append("Which sale ")
        flag = 1
    if " salesman " in msgs:
        qtns.append(" salesman ")
        anss.append("Which salesman ")
        flag = 1
    if " salesperson " in msgs:
        qtns.append(" salesperson ")
        anss.append("Which salesperson ")
        flag = 1
    if " saleswoman " in msgs:
        qtns.append(" saleswoman ")
        anss.append("Which saleswoman ")
        flag = 1
    if " schedule " in msgs:
        qtns.append(" schedule ")
        anss.append("Which schedule ")
        flag = 1
    if " secretary " in msgs:
        qtns.append(" secretary ")
        anss.append("Which secretary ")
        flag = 1
    if " share " in msgs:
        qtns.append(" share ")
        anss.append("Which share ")
        flag = 1
    if " shop " in msgs:
        qtns.append(" shop ")
        anss.append("Which shop ")
        flag = 1
    if " singer " in msgs:
        qtns.append(" singer ")
        anss.append("Which singer ")
        flag = 1
    if " skill " in msgs:
        qtns.append(" skill ")
        anss.append("Which skill ")
        flag = 1
    if " stock " in msgs:
        qtns.append(" stock ")
        anss.append("Which stock ")
        flag = 1
    if " strategy " in msgs:
        qtns.append(" strategy ")
        anss.append("Which strategy ")
        flag = 1
    if " success " in msgs:
        qtns.append(" success ")
        anss.append("Which success ")
        flag = 1
    if " suggestion " in msgs:
        qtns.append(" suggestion ")
        anss.append("Which suggestion ")
        flag = 1
    if " supply " in msgs:
        qtns.append(" supply ")
        anss.append("Which supply ")
        flag = 1
    if " support " in msgs:
        qtns.append(" support ")
        anss.append("Which support ")
        flag = 1
    if " surgeon " in msgs:
        qtns.append(" surgeon ")
        anss.append("Which surgeon ")
        flag = 1
    if " target " in msgs:
        qtns.append(" target ")
        anss.append("Which target ")
        flag = 1
    if " teacher " in msgs:
        qtns.append(" teacher ")
        anss.append("Which teacher ")
        flag = 1
    if " therapist " in msgs:
        qtns.append(" therapist ")
        anss.append("Which therapist ")
        flag = 1
    if " thing " in msgs:
        qtns.append(" thing ")
        anss.append("Which thing ")
        flag = 1
    if " tool " in msgs:
        qtns.append(" tool ")
        anss.append("Which tool ")
        flag = 1
    if " translator " in msgs:
        qtns.append(" translator ")
        anss.append("Which translator ")
        flag = 1
    if " undertaker " in msgs:
        qtns.append(" undertaker ")
        anss.append("Which undertaker ")
        flag = 1
    if " veterinarian " in msgs:
        qtns.append(" veterinarian ")
        anss.append("Which veterinarian ")
        flag = 1
    if " videographer " in msgs:
        qtns.append(" videographer ")
        anss.append("Which videographer ")
        flag = 1
    if " wage " in msgs:
        qtns.append(" wage ")
        anss.append("Which wage ")
        flag = 1
    if " waiter " in msgs:
        qtns.append(" waiter ")
        anss.append("Which waiter ")
        flag = 1
    if " waitress " in msgs:
        qtns.append(" waitress ")
        anss.append("Which waitress ")
        flag = 1
    if " warranty " in msgs:
        qtns.append(" warranty ")
        anss.append("Which warranty ")
        flag = 1
    if " writer " in msgs:
        qtns.append(" writer ")
        anss.append("Which writer ")
        flag = 1
    if " abilities " in msgs:
        qtns.append(" abilities ")
        anss.append("All? Only some? Which abilities specifically? ")
        flag = 1
    if " accountants " in msgs:
        qtns.append(" accountants ")
        anss.append("All? Only some? Which accountants specifically? ")
        flag = 1
    if " actors " in msgs:
        qtns.append(" actors ")
        anss.append("All? Only some? Which actors specifically? ")
        flag = 1
    if " actresses " in msgs:
        qtns.append(" actresses ")
        anss.append("All? Only some? Which actresses specifically? ")
        flag = 1
    if " advantages " in msgs:
        qtns.append(" advantages ")
        anss.append("All? Only some? Which advantages specifically? ")
        flag = 1
    if " advice " in msgs:
        qtns.append(" advice ")
        anss.append("All? Only some? Which advice specifically? ")
        flag = 1
    if " agenda " in msgs:
        qtns.append(" agenda ")
        anss.append("All? Only some? Which agenda specifically? ")
        flag = 1
    if " apologies " in msgs:
        qtns.append(" apologies ")
        anss.append("All? Only some? Which apologies specifically? ")
        flag = 1
    if " applications " in msgs:
        qtns.append(" applications ")
        anss.append("All? Only some? Which applications specifically? ")
        flag = 1
    if " architects " in msgs:
        qtns.append(" architects ")
        anss.append("All? Only some? Which architects specifically? ")
        flag = 1
    if " artists " in msgs:
        qtns.append(" artists ")
        anss.append("All? Only some? Which artists specifically? ")
        flag = 1
    if " assistants " in msgs:
        qtns.append(" assistants ")
        anss.append("All? Only some? Which assistants specifically? ")
        flag = 1
    if " attorneys " in msgs:
        qtns.append(" attorneys ")
        anss.append("All? Only some? Which attorneys specifically? ")
        flag = 1
    if " bankers " in msgs:
        qtns.append(" bankers ")
        anss.append("All? Only some? Which bankers specifically? ")
        flag = 1
    if " barbers " in msgs:
        qtns.append(" barbers ")
        anss.append("All? Only some? Which barbers specifically? ")
        flag = 1
    if " bartenders " in msgs:
        qtns.append(" bartenders ")
        anss.append("All? Only some? Which bartenders specifically? ")
        flag = 1
    if " benefits " in msgs:
        qtns.append(" benefits ")
        anss.append("All? Only some? Which benefits specifically? ")
        flag = 1
    if " bills " in msgs:
        qtns.append(" bills ")
        anss.append("All? Only some? Which bills specifically? ")
        flag = 1
    if " bonuses " in msgs:
        qtns.append(" bonuses ")
        anss.append("All? Only some? Which bonuses specifically? ")
        flag = 1
    if " bookkeepers " in msgs:
        qtns.append(" bookkeepers ")
        anss.append("All? Only some? Which bookkeepers specifically? ")
        flag = 1
    if " bosses " in msgs:
        qtns.append(" bosses ")
        anss.append("All? Only some? Which bosses specifically? ")
        flag = 1
    if " brands " in msgs:
        qtns.append(" brands ")
        anss.append("All? Only some? Which brands specifically? ")
        flag = 1
    if " budgets " in msgs:
        qtns.append(" budgets ")
        anss.append("All? Only some? Which budgets specifically? ")
        flag = 1
    if " builders " in msgs:
        qtns.append(" builders ")
        anss.append("All? Only some? Which builders specifically? ")
        flag = 1
    if " businessmen " in msgs:
        qtns.append(" businessmen ")
        anss.append("All? Only some? Which businessmen specifically? ")
        flag = 1
    if " businesspersons " in msgs:
        qtns.append(" businesspersons ")
        anss.append("All? Only some? Which businesspersons specifically? ")
        flag = 1
    if " businesswomen " in msgs:
        qtns.append(" businesswomen ")
        anss.append("All? Only some? Which businesswomen specifically? ")
        flag = 1
    if " butchers " in msgs:
        qtns.append(" butchers ")
        anss.append("All? Only some? Which butchers specifically? ")
        flag = 1
    if " capabilities " in msgs:
        qtns.append(" capabilities ")
        anss.append("All? Only some? Which capabilities specifically? ")
        flag = 1
    if " careers " in msgs:
        qtns.append(" careers ")
        anss.append("All? Only some? Which careers specifically? ")
        flag = 1
    if " carpenters " in msgs:
        qtns.append(" carpenters ")
        anss.append("All? Only some? Which carpenters specifically? ")
        flag = 1
    if " cashiers " in msgs:
        qtns.append(" cashiers ")
        anss.append("All? Only some? Which cashiers specifically? ")
        flag = 1
    if " changes " in msgs:
        qtns.append(" changes ")
        anss.append("All? Only some? Which changes specifically? ")
        flag = 1
    if " chefs " in msgs:
        qtns.append(" chefs ")
        anss.append("All? Only some? Which chefs specifically? ")
        flag = 1
    if " coaches " in msgs:
        qtns.append(" coaches ")
        anss.append("All? Only some? Which coaches specifically? ")
        flag = 1
    if " companies " in msgs:
        qtns.append(" companies ")
        anss.append("All? Only some? Which companies specifically? ")
        flag = 1
    if " competitions " in msgs:
        qtns.append(" competitions ")
        anss.append("All? Only some? Which competitions specifically? ")
        flag = 1
    if " conclusions " in msgs:
        qtns.append(" conclusions ")
        anss.append("All? Only some? Which conclusions specifically? ")
        flag = 1
    if " controllers " in msgs:
        qtns.append(" controllers ")
        anss.append("All? Only some? Which controllers specifically? ")
        flag = 1
    if " costs " in msgs:
        qtns.append(" costs ")
        anss.append("All? Only some? Which costs specifically? ")
        flag = 1
    if " cover letters " in msgs:
        qtns.append(" cover letters ")
        anss.append("All? Only some? Which cover letters specifically? ")
        flag = 1
    if " customers " in msgs:
        qtns.append(" customers ")
        anss.append("All? Only some? Which customers specifically? ")
        flag = 1
    if " deadlines " in msgs:
        qtns.append(" deadlines ")
        anss.append("All? Only some? Which deadlines specifically? ")
        flag = 1
    if " debts " in msgs:
        qtns.append(" debts ")
        anss.append("All? Only some? Which debts specifically? ")
        flag = 1
    if " decisions " in msgs:
        qtns.append(" decisions ")
        anss.append("All? Only some? Which decisions specifically? ")
        flag = 1
    if " decreases " in msgs:
        qtns.append(" decreases ")
        anss.append("All? Only some? Which decreases specifically? ")
        flag = 1
    if " defects " in msgs:
        qtns.append(" defects ")
        anss.append("All? Only some? Which defects specifically? ")
        flag = 1
    if " deliveries " in msgs:
        qtns.append(" deliveries ")
        anss.append("All? Only some? Which deliveries specifically? ")
        flag = 1
    if " dentists " in msgs:
        qtns.append(" dentists ")
        anss.append("All? Only some? Which dentists specifically? ")
        flag = 1
    if " departments " in msgs:
        qtns.append(" departments ")
        anss.append("All? Only some? Which departments specifically? ")
        flag = 1
    if " descriptions " in msgs:
        qtns.append(" descriptions ")
        anss.append("All? Only some? Which descriptions specifically? ")
        flag = 1
    if " designers " in msgs:
        qtns.append(" designers ")
        anss.append("All? Only some? Which designers specifically? ")
        flag = 1
    if " developers " in msgs:
        qtns.append(" developers ")
        anss.append("All? Only some? Which developers specifically? ")
        flag = 1
    if " devices " in msgs:
        qtns.append(" devices ")
        anss.append("All? Only some? Which devices specifically? ")
        flag = 1
    if " dieticians " in msgs:
        qtns.append(" dieticians ")
        anss.append("All? Only some? Which dieticians specifically? ")
        flag = 1
    if " differences " in msgs:
        qtns.append(" differences ")
        anss.append("All? Only some? Which differences specifically? ")
        flag = 1
    if " directors " in msgs:
        qtns.append(" directors ")
        anss.append("All? Only some? Which directors specifically? ")
        flag = 1
    if " doctors " in msgs:
        qtns.append(" doctors ")
        anss.append("All? Only some? Which doctors specifically? ")
        flag = 1
    if " economists " in msgs:
        qtns.append(" economists ")
        anss.append("All? Only some? Which economists specifically? ")
        flag = 1
    if " editors " in msgs:
        qtns.append(" editors ")
        anss.append("All? Only some? Which editors specifically? ")
        flag = 1
    if " electricians " in msgs:
        qtns.append(" electricians ")
        anss.append("All? Only some? Which electricians specifically? ")
        flag = 1
    if " employees " in msgs:
        qtns.append(" employees ")
        anss.append("All? Only some? Which employees specifically? ")
        flag = 1
    if " employers " in msgs:
        qtns.append(" employers ")
        anss.append("All? Only some? Which employers specifically? ")
        flag = 1
    if " engineers " in msgs:
        qtns.append(" engineers ")
        anss.append("All? Only some? Which engineers specifically? ")
        flag = 1
    if " equipment " in msgs:
        qtns.append(" equipment ")
        anss.append("All? Only some? Which equipment specifically? ")
        flag = 1
    if " errors " in msgs:
        qtns.append(" errors ")
        anss.append("All? Only some? Which errors specifically? ")
        flag = 1
    if " estimates " in msgs:
        qtns.append(" estimates ")
        anss.append("All? Only some? Which estimates specifically? ")
        flag = 1
    if " experiences " in msgs:
        qtns.append(" experiences ")
        anss.append("All? Only some? Which experiences specifically? ")
        flag = 1
    if " explanations " in msgs:
        qtns.append(" explanations ")
        anss.append("All? Only some? Which explanations specifically? ")
        flag = 1
    if " facilities " in msgs:
        qtns.append(" facilities ")
        anss.append("All? Only some? Which facilities specifically? ")
        flag = 1
    if " factories " in msgs:
        qtns.append(" factories ")
        anss.append("All? Only some? Which factories specifically? ")
        flag = 1
    if " farmers " in msgs:
        qtns.append(" farmers ")
        anss.append("All? Only some? Which farmers specifically? ")
        flag = 1
    if " faults " in msgs:
        qtns.append(" faults ")
        anss.append("All? Only some? Which faults specifically? ")
        flag = 1
    if " feedback " in msgs:
        qtns.append(" feedback ")
        anss.append("All? Only some? Which feedback specifically? ")
        flag = 1
    if " filmmakers " in msgs:
        qtns.append(" filmmakers ")
        anss.append("All? Only some? Which filmmakers specifically? ")
        flag = 1
    if " fishermen " in msgs:
        qtns.append(" fishermen ")
        anss.append("All? Only some? Which fishermen specifically? ")
        flag = 1
    if " flight attendants " in msgs:
        qtns.append(" flight attendants ")
        anss.append("All? Only some? Which flight attendants specifically? ")
        flag = 1
    if " goals " in msgs:
        qtns.append(" goals ")
        anss.append("All? Only some? Which goals specifically? ")
        flag = 1
    if " growth " in msgs:
        qtns.append(" growth ")
        anss.append("All? Only some? Which growth specifically? ")
        flag = 1
    if " guarantees " in msgs:
        qtns.append(" guarantees ")
        anss.append("All? Only some? Which guarantees specifically? ")
        flag = 1
    if " hygienists " in msgs:
        qtns.append(" hygienists ")
        anss.append("All? Only some? Which hygienists specifically? ")
        flag = 1
    if " improvements " in msgs:
        qtns.append(" improvements ")
        anss.append("All? Only some? Which improvements specifically? ")
        flag = 1
    if " increases " in msgs:
        qtns.append(" increases ")
        anss.append("All? Only some? Which increases specifically? ")
        flag = 1
    if " industries " in msgs:
        qtns.append(" industries ")
        anss.append("All? Only some? Which industries specifically? ")
        flag = 1
    if " instructions " in msgs:
        qtns.append(" instructions ")
        anss.append("All? Only some? Which instructions specifically? ")
        flag = 1
    if " interests " in msgs:
        qtns.append(" interests ")
        anss.append("All? Only some? Which interests specifically? ")
        flag = 1
    if " interviews " in msgs:
        qtns.append(" interviews ")
        anss.append("All? Only some? Which interviews specifically? ")
        flag = 1
    if " inventories " in msgs:
        qtns.append(" inventories ")
        anss.append("All? Only some? Which inventories specifically? ")
        flag = 1
    if " invoices " in msgs:
        qtns.append(" invoices ")
        anss.append("All? Only some? Which invoices specifically? ")
        flag = 1
    if " jewelers " in msgs:
        qtns.append(" jewelers ")
        anss.append("All? Only some? Which jewelers specifically? ")
        flag = 1
    if " jobs " in msgs:
        qtns.append(" jobs ")
        anss.append("All? Only some? Which jobs specifically? ")
        flag = 1
    if " judges " in msgs:
        qtns.append(" judges ")
        anss.append("All? Only some? Which judges specifically? ")
        flag = 1
    if " knowledge " in msgs:
        qtns.append(" knowledge ")
        anss.append("All? Only some? Which knowledge specifically? ")
        flag = 1
    if " lawyers " in msgs:
        qtns.append(" lawyers ")
        anss.append("All? Only some? Which lawyers specifically? ")
        flag = 1
    if " layoffs " in msgs:
        qtns.append(" layoffs ")
        anss.append("All? Only some? Which layoffs specifically? ")
        flag = 1
    if " limits " in msgs:
        qtns.append(" limits ")
        anss.append("All? Only some? Which limits specifically? ")
        flag = 1
    if " losses " in msgs:
        qtns.append(" losses ")
        anss.append("All? Only some? Which losses specifically? ")
        flag = 1
    if " machines " in msgs:
        qtns.append(" machines ")
        anss.append("All? Only some? Which machines specifically? ")
        flag = 1
    if " managers " in msgs:
        qtns.append(" managers ")
        anss.append("All? Only some? Which managers specifically? ")
        flag = 1
    if " margins " in msgs:
        qtns.append(" margins ")
        anss.append("All? Only some? Which margins specifically? ")
        flag = 1
    if " markets " in msgs:
        qtns.append(" markets ")
        anss.append("All? Only some? Which markets specifically? ")
        flag = 1
    if " mechanics " in msgs:
        qtns.append(" mechanics ")
        anss.append("All? Only some? Which mechanics specifically? ")
        flag = 1
    if " messages " in msgs:
        qtns.append(" messages ")
        anss.append("All? Only some? Which messages specifically? ")
        flag = 1
    if " mistakes " in msgs:
        qtns.append(" mistakes ")
        anss.append("All? Only some? Which mistakes specifically? ")
        flag = 1
    if " musicians " in msgs:
        qtns.append(" musicians ")
        anss.append("All? Only some? Which musicians specifically? ")
        flag = 1
    if " nurses " in msgs:
        qtns.append(" nurses ")
        anss.append("All? Only some? Which nurses specifically? ")
        flag = 1
    if " nutritionists " in msgs:
        qtns.append(" nutritionists ")
        anss.append("All? Only some? Which nutritionists specifically? ")
        flag = 1
    if " objectives " in msgs:
        qtns.append(" objectives ")
        anss.append("All? Only some? Which objectives specifically? ")
        flag = 1
    if " offers " in msgs:
        qtns.append(" offers ")
        anss.append("All? Only some? Which offers specifically? ")
        flag = 1
    if " opinions " in msgs:
        qtns.append(" opinions ")
        anss.append("All? Only some? Which opinions specifically? ")
        flag = 1
    if " opticians " in msgs:
        qtns.append(" opticians ")
        anss.append("All? Only some? Which opticians specifically? ")
        flag = 1
    if " options " in msgs:
        qtns.append(" options ")
        anss.append("All? Only some? Which options specifically? ")
        flag = 1
    if " orders " in msgs:
        qtns.append(" orders ")
        anss.append("All? Only some? Which orders specifically? ")
        flag = 1
    if " organisations " in msgs:
        qtns.append(" organisations ")
        anss.append("All? Only some? Which organisations specifically? ")
        flag = 1
    if " painters " in msgs:
        qtns.append(" painters ")
        anss.append("All? Only some? Which painters specifically? ")
        flag = 1
    if " payments " in msgs:
        qtns.append(" payments ")
        anss.append("All? Only some? Which payments specifically? ")
        flag = 1
    if " permissions " in msgs:
        qtns.append(" permissions ")
        anss.append("All? Only some? Which permissions specifically? ")
        flag = 1
    if " pharmacists " in msgs:
        qtns.append(" pharmacists ")
        anss.append("All? Only some? Which pharmacists specifically? ")
        flag = 1
    if " photographers " in msgs:
        qtns.append(" photographers ")
        anss.append("All? Only some? Which photographers specifically? ")
        flag = 1
    if " physicians " in msgs:
        qtns.append(" physicians ")
        anss.append("All? Only some? Which physicians specifically? ")
        flag = 1
    if " physician's assistants " in msgs:
        qtns.append(" physician's assistants ")
        anss.append("All? Only some? Which physician's assistants specifically? ")
        flag = 1
    if " pilots " in msgs:
        qtns.append(" pilots ")
        anss.append("All? Only some? Which pilots specifically? ")
        flag = 1
    if " plans " in msgs:
        qtns.append(" plans ")
        anss.append("All? Only some? Which plans specifically? ")
        flag = 1
    if " plumbers " in msgs:
        qtns.append(" plumbers ")
        anss.append("All? Only some? Which plumbers specifically? ")
        flag = 1
    if " police officers " in msgs:
        qtns.append(" police officers ")
        anss.append("All? Only some? Which police officers specifically? ")
        flag = 1
    if " politicians " in msgs:
        qtns.append(" politicians ")
        anss.append("All? Only some? Which politicians specifically? ")
        flag = 1
    if " preparations " in msgs:
        qtns.append(" preparations ")
        anss.append("All? Only some? Which preparations specifically? ")
        flag = 1
    if " prices " in msgs:
        qtns.append(" prices ")
        anss.append("All? Only some? Which prices specifically? ")
        flag = 1
    if " products " in msgs:
        qtns.append(" products ")
        anss.append("All? Only some? Which products specifically? ")
        flag = 1
    if " productions " in msgs:
        qtns.append(" productions ")
        anss.append("All? Only some? Which productions specifically? ")
        flag = 1
    if " professors " in msgs:
        qtns.append(" professors ")
        anss.append("All? Only some? Which professors specifically? ")
        flag = 1
    if " profits " in msgs:
        qtns.append(" profits ")
        anss.append("All? Only some? Which profits specifically? ")
        flag = 1
    if " programmers " in msgs:
        qtns.append(" programmers ")
        anss.append("All? Only some? Which programmers specifically? ")
        flag = 1
    if " promotions " in msgs:
        qtns.append(" promotions ")
        anss.append("All? Only some? Which promotions specifically? ")
        flag = 1
    if " psychologists " in msgs:
        qtns.append(" psychologists ")
        anss.append("All? Only some? Which psychologists specifically? ")
        flag = 1
    if " purchases " in msgs:
        qtns.append(" purchases ")
        anss.append("All? Only some? Which purchases specifically? ")
        flag = 1
    if " raises " in msgs:
        qtns.append(" raises ")
        anss.append("All? Only some? Which raises specifically? ")
        flag = 1
    if " receptionists " in msgs:
        qtns.append(" receptionists ")
        anss.append("All? Only some? Which receptionists specifically? ")
        flag = 1
    if " refunds " in msgs:
        qtns.append(" refunds ")
        anss.append("All? Only some? Which refunds specifically? ")
        flag = 1
    if " reminders " in msgs:
        qtns.append(" reminders ")
        anss.append("All? Only some? Which reminders specifically? ")
        flag = 1
    if " reports " in msgs:
        qtns.append(" reports ")
        anss.append("All? Only some? Which reports specifically? ")
        flag = 1
    if " responsibilities " in msgs:
        qtns.append(" responsibilities ")
        anss.append("All? Only some? Which responsibilities specifically? ")
        flag = 1
    if " results " in msgs:
        qtns.append(" results ")
        anss.append("All? Only some? Which results specifically? ")
        flag = 1
    if " rise " in msgs:
        qtns.append(" rise ")
        anss.append("All? Only some? Which rise specifically? ")
        flag = 1
    if " risks " in msgs:
        qtns.append(" risks ")
        anss.append("All? Only some? Which risks specifically? ")
        flag = 1
    if " salaries " in msgs:
        qtns.append(" salaries ")
        anss.append("All? Only some? Which salaries specifically? ")
        flag = 1
    if " sales " in msgs:
        qtns.append(" sales ")
        anss.append("All? Only some? Which sales specifically? ")
        flag = 1
    if " salesmen " in msgs:
        qtns.append(" salesmen ")
        anss.append("All? Only some? Which salesmen specifically? ")
        flag = 1
    if " salespersons " in msgs:
        qtns.append(" salespersons ")
        anss.append("All? Only some? Which salespersons specifically? ")
        flag = 1
    if " saleswomen " in msgs:
        qtns.append(" saleswomen ")
        anss.append("All? Only some? Which saleswomen specifically? ")
        flag = 1
    if " schedules " in msgs:
        qtns.append(" schedules ")
        anss.append("All? Only some? Which schedules specifically? ")
        flag = 1
    if " secretaries " in msgs:
        qtns.append(" secretaries ")
        anss.append("All? Only some? Which secretaries specifically? ")
        flag = 1
    if " services " in msgs:
        qtns.append(" services ")
        anss.append("All? Only some? Which services specifically? ")
        flag = 1
    if " shares " in msgs:
        qtns.append(" shares ")
        anss.append("All? Only some? Which shares specifically? ")
        flag = 1
    if " shops " in msgs:
        qtns.append(" shops ")
        anss.append("All? Only some? Which shops specifically? ")
        flag = 1
    if " singers " in msgs:
        qtns.append(" singers ")
        anss.append("All? Only some? Which singers specifically? ")
        flag = 1
    if " skills " in msgs:
        qtns.append(" skills ")
        anss.append("All? Only some? Which skills specifically? ")
        flag = 1
    if " stocks " in msgs:
        qtns.append(" stocks ")
        anss.append("All? Only some? Which stocks specifically? ")
        flag = 1
    if " strategies " in msgs:
        qtns.append(" strategies ")
        anss.append("All? Only some? Which strategies specifically? ")
        flag = 1
    if " successes " in msgs:
        qtns.append(" successes ")
        anss.append("All? Only some? Which successes specifically? ")
        flag = 1
    if " suggestions " in msgs:
        qtns.append(" suggestions ")
        anss.append("All? Only some? Which suggestions specifically? ")
        flag = 1
    if " supplies " in msgs:
        qtns.append(" supplies ")
        anss.append("All? Only some? Which supplies specifically? ")
        flag = 1
    if " supports " in msgs:
        qtns.append(" supports ")
        anss.append("All? Only some? Which supports specifically? ")
        flag = 1
    if " surgeons " in msgs:
        qtns.append(" surgeons ")
        anss.append("All? Only some? Which surgeons specifically? ")
        flag = 1
    if " targets " in msgs:
        qtns.append(" targets ")
        anss.append("All? Only some? Which targets specifically? ")
        flag = 1
    if " teachers " in msgs:
        qtns.append(" teachers ")
        anss.append("All? Only some? Which teachers specifically? ")
        flag = 1
    if " therapists " in msgs:
        qtns.append(" therapists ")
        anss.append("All? Only some? Which therapists specifically? ")
        flag = 1
    if " things " in msgs:
        qtns.append(" things ")
        anss.append("All? Only some? Which things specifically? ")
        flag = 1
    if " tools " in msgs:
        qtns.append(" tools ")
        anss.append("All? Only some? Which tools specifically? ")
        flag = 1
    if " translators " in msgs:
        qtns.append(" translators ")
        anss.append("All? Only some? Which translators specifically? ")
        flag = 1
    if " undertakers " in msgs:
        qtns.append(" undertakers ")
        anss.append("All? Only some? Which undertakers specifically? ")
        flag = 1
    if " veterinarians " in msgs:
        qtns.append(" veterinarians ")
        anss.append("All? Only some? Which veterinarians specifically? ")
        flag = 1
    if " videographers " in msgs:
        qtns.append(" videographers ")
        anss.append("All? Only some? Which videographers specifically? ")
        flag = 1
    if " wages " in msgs:
        qtns.append(" wages ")
        anss.append("All? Only some? Which wages specifically? ")
        flag = 1
    if " waiters " in msgs:
        qtns.append(" waiters ")
        anss.append("All? Only some? Which waiters specifically? ")
        flag = 1
    if " waitresses " in msgs:
        qtns.append(" waitresses ")
        anss.append("All? Only some? Which waitresses specifically? ")
        flag = 1
    if " warranties " in msgs:
        qtns.append(" warranties ")
        anss.append("All? Only some? Which warranties specifically? ")
        flag = 1
    if " writers " in msgs:
        qtns.append(" writers ")
        anss.append("All? Only some? Which writers specifically? ")
        flag = 1
    if " cannot " in msgs:
        qtns.append(" cannot ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " can't " in msgs:
        qtns.append(" can't ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " will not " in msgs:
        qtns.append(" will not ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " won't " in msgs:
        qtns.append(" won't ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " may not " in msgs:
        qtns.append(" may not ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " impossible " in msgs:
        qtns.append(" impossible ")
        anss.append("What specifically stops you? ")
        flag = 1
    if " not possible " in msgs:
        qtns.append(" not possible ")
        anss.append("What specifically stops you? ")
        flag = 1

    print("Okay! ")
    if flag == 0:
        print("Your problem has been recorded! ")
    return qtns, anss