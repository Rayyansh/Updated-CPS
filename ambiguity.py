import spacy
nlp = spacy.load("en_core_web_sm")
with open('adj.txt') as f:
    data_adj = f.read().splitlines() 
print(data_adj)

with open('noun.txt') as f:
    data_noun = f.read().splitlines() 
print(data_noun)

with open('adj_comp.txt') as f:
    data_adj_comp = f.read().splitlines() 
print(data_noun)

with open('adj_sup.txt') as f:
    data_adj_sup = f.read().splitlines() 
print(data_noun)

with open('noun_plural.txt') as f:
    data_noun_plural = f.read().splitlines() 
print(data_noun_plural)

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
    flag=0

    splitted_msgs = msgs.split()
    """
      

    tmp = nlp(each_word)
     
        print(tmp[0].text, tmp[0].lemma_, tmp[0].pos_, tmp[0].tag_, tmp[0].dep_,tmp[0].shape_, tmp[0].is_alpha, tmp[0].is_stop)
        if(tmp[0].pos_ ==  "ADJ"):
            
            if f" more {each_word} " in msgs:
               
                qtns.append(f" more {each_word} ")
                anss.append(f"{each_word} than what/whom? {each_word} compared to what/whom?")
                flag=1
            elif f" {each_word} " in msgs:
                qtns.append(f" {each_word} ")
                anss.append(f"What do you mean by {each_word}? Please specify. ")
            flag=1   
    """


    # adjective
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    for each_word in data_adj:
        each_word = each_word.lower()
        if each_word == "":      
                print(f" more ")
                if f" more " in msgs and f==0:
                    print(f" more ")
                    qtns.append(f" more ")
                    anss.append(f"more than what/whom? more compared to what/whom?")
            
                    flag=1
                elif f" less " in msgs and g==0:
                    print(f" less ")
                    qtns.append(f" less")
                    anss.append(f"less than what/whom? less compared to what/whom?")
                    flag=1    
                  
                elif f" most " in msgs and h==0:
                    print(f" most ")
                    qtns.append(f" most ")
                    anss.append(f"How specifically do you know most? According to whom?")
                    flag=1  
                elif f" least " in msgs and i==0:
                    print(f" least ")
                    qtns.append(f" least ")
                    anss.append(f"How specifically do you know least? According to whom?")
                    flag=1   
                elif f" very " in msgs and m==0:
                    print(f" very ")
                    qtns.append(f" very ")
                    anss.append(f"How specifically do you know very? According to whom?")
                    flag=1   
                elif f" extremely " in msgs and j==0:
                    print(f" extremely ")
                    qtns.append(f" extremely ")
                    anss.append(f"How specifically do you know extremely? According to whom?")
                    flag=1   
                elif f" especially " in msgs and k==0:
                    print(f" especially ")
                    qtns.append(f" especially ")
                    anss.append(f"How specifically do you know especially? According to whom?")
                    flag=1 
                elif f" absolutely " in msgs and l==0:
                    print(f" absolutely ")
                    qtns.append(f" absolutely ")
                    anss.append(f"How specifically do you know absolutely? According to whom?")
                    flag=1                          
               
        else:        
                if f" {each_word} " in msgs:
                    print("adj")
                
                    print(f" more {each_word} ")
                    if f" more {each_word} " in msgs:
                        print(f" more {each_word} ")
                        qtns.append(f" more {each_word} ")
                        anss.append(f"{each_word} than what/whom? {each_word} compared to what/whom?")
                        f=1
                        flag=1
                    elif f" less {each_word} " in msgs:
                        print(f" less {each_word} ")
                        qtns.append(f" less {each_word} ")
                        anss.append(f"{each_word} than what/whom? {each_word} compared to what/whom?")
                        flag=1  
                        g=1  
                    elif f" most {each_word} " in msgs:
                        print(f" most {each_word} ")
                        qtns.append(f" most {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1  
                        h=1
                    elif f" least {each_word} " in msgs:
                        print(f" least {each_word} ")
                        qtns.append(f" least {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1   
                        i=1
                    elif f" very {each_word} " in msgs:
                        print(f" very {each_word} ")
                        qtns.append(f" very {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1   
                        m=0
                    elif f" extremely {each_word} " in msgs:
                        print(f" extremely {each_word} ")
                        qtns.append(f" extremely {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1  
                        j=1 
                    elif f" especially {each_word} " in msgs:
                        print(f" especially {each_word} ")
                        qtns.append(f" especially {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1 
                        k=1
                    elif f" absolutely {each_word} " in msgs:
                        print(f" absolutely {each_word} ")
                        qtns.append(f" absolutely {each_word} ")
                        anss.append(f"How specifically do you know {each_word}? According to whom?")
                        flag=1  
                        l=1                        
                    elif f" {each_word} " in msgs:
                        print(f" {each_word} ")
                        qtns.append(f" {each_word} ")
                        anss.append(f"What do you mean by {each_word}? Please specify. ")
                        flag=1 
    for each_word in data_adj_comp:
        each_word = each_word.lower()
        
        if (f" {each_word} " in msgs and (f" {each_word} " not in [' more ',' most ',' less ', ' least ' ])) :
            
            print("adj_comp")
            if f" {each_word} " in msgs:
                print(f" {each_word} ")
                qtns.append(f" {each_word} ")
                anss.append(f"What do you mean by {each_word}? Please specify. ")
                flag=1 
    for each_word in data_adj_sup:
        each_word = each_word.lower()
        
        if f" {each_word} " in msgs:
            print("adj_sup")
            if f" {each_word} " in msgs:
                print(f" {each_word} ")
                qtns.append(f" {each_word} ")
                anss.append(f"How specifically do you know {each_word}? According to whom?")
                flag=1 

    # noun 
    #data_noun =  ['ability', 'accountant', 'actor', 'actress', 'advantage', 'apology', 'application', 'architect', 'artist', 'assistant', 'attorney', 'banker', 'barber', 'bartender', 'benefit', 'bonus', 'bookkeeper', 'boss', 'builder', 'businessman', 'businessperson', 'businesswoman', 'butcher', 'capability', 'career', 'carpenter', 'cashier', 'company', 'competition', 'conclusion', 'controller', 'cost', 'cover', 'letter', 'customer', 'deadline', 'debt', 'decision', 'defect', 'delivery', 'dentist', 'department', 'description', 'designer', 'developer', 'device', 'dietician', 'difference', 'director', 'doctor', 'economist', 'editor', 'electrician', 'employee', 'employer']         
    for each_word in data_noun:
        each_word = each_word.lower()
        
        if f" {each_word} " in msgs:
            print("noun")
            print(f" {each_word} ")
            if f" {each_word} " in msgs:
                print(f" {each_word} ")
                qtns.append(f" {each_word} ")
                anss.append(f"which {each_word}?")
                flag=1
    for each_word in data_noun_plural:
        each_word = each_word.lower()
        
        if f" {each_word} " in msgs:
            print("noun_plural")
            print(f" {each_word} ")
            if f" {each_word} " in msgs:
                print(f" {each_word} ")
                qtns.append(f" {each_word} ")
                anss.append(f"All? Only some? Which {each_word} specifically? ")
                flag=1     

    return qtns, anss