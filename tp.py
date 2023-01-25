import pymongo,os
os.environ['MONGODB_URI'] = "mongodb+srv://pharshil1902:hhpdhphrp@cluster0.pxxvw.mongodb.net/techqrt_chatbot?retryWrites=true&w=majority"
client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
mydb = client["techqrt_chatbot"]
mycol = mydb["user_data"]
x = mycol.find({'user.name':'harshil@gmail.com'})
print(x[0]['user']['problems'])






def ambi_solver(question,answer):
    if (type(answer ) != list):
                answer = answer.lower()
                
    if ("to be " in str(answer ).lower()):
        print("ONE")
        aws = answer.split(" ")
        print(aws)
        to_id = 0
        for j in range(0, len(aws)):
            if (aws[j] == "be"):
                to_id = j
        print(to_id)
        wes = ""
        for k in range(to_id + 2, len(aws)):
            wes += str(aws[k])
            wes += " "
        dse = wes.split(" ")
        if (len(dse) > 2):
    
            print(len(dse))
            print(f"WES::: {dse}")
            #an.append(f"How to be {aws[to_id+1]} {wes} ?")
            # answer[i] = f"{answer[i]}"
            #answer[i] = f"How to be {aws[to_id+1]} {wes} ?"
            session['user']['problems'][session['id']]['how_to_stmts'].append(answer)
        
    elif (" to " in str(answer ).lower()):
        print("TEO")
        aws = answer.split(" ")
        print(aws)
        to_id = 0
        for j in range(0, len(aws)):
            if (aws[j] == "to"):
                to_id = j
        print(to_id)
        wes = ""

        for k in range(to_id + 2, len(aws)):
            wes += str(aws[k])
            wes += " "
        ress = "FF"
        dse = wes.split(" ")
        if (to_id < len(aws) - 1):
            print(aws[to_id + 1])
            ress = verb_or_not(aws[to_id + 1])
            print(ress)
        if (ress == "VERB" and len(dse) > 2):
            print(ress)
            # <br> {answer[i]} <br><i style='color:blue;'>How to {aws[to_id+1]} {wes} ?</i>
           
            print(len(dse))
            print(f"WES::: {dse}")
            #an.append(f"How to {aws[to_id+1]} {wes} ?")
            # answer[i] = f"{answer[i]}"
            #answer[i] = f"How to {aws[to_id+1]} {wes} ?"
            #to_do_list.append(i)
            session['user']['problems'][session['id']]['how_to_stmts'].append(f"How to {aws[to_id+1]} {wes} ?")
        else:
            pass
    elif ("because of" in str(answer).lower()):
        print("THREE")
        print("-----------------")
        aws = answer
        aws = aws.replace(".", "")
        aws = aws.replace("\n", "")
        aws = aws.replace("\r", "")
        aws = aws.split(" ")
        to_id = 0
        print(aws)
        for j in range(0, len(aws)):
            if (aws[j] == 'because'):
                to_id = j
                break
        wess = "How does "
        for j in range(to_id + 2, len(aws)):
            wess += (aws[j])
            wess += " "
        wess += "mean "
        for j in range(0, to_id):
            wess += (aws[j])
            wess += " "
        wess += "?\n"
        print(wess)
        session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        # to_do_list.append(i)

    elif (" as " in str(answer).lower()):
        print("THREE")
        print("-----------------")
        aws = answer
        aws = aws.replace(".", "")
        aws = aws.replace("\n", "")
        aws = aws.replace("\r", "")
        aws = aws.split(" ")
        to_id = 0
        print(aws)
        for j in range(0, len(aws)):
            if (aws[j] == 'as'):
                to_id = j
                break
        wess = "How does "
        for j in range(to_id + 1, len(aws)):
            wess += (aws[j])
            wess += " "
        wess += "mean "
        for j in range(0, to_id):
            wess += (aws[j])
            wess += " "
        wess += "?\n"
        print(wess)
        session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        # to_do_list.append(i)        
    elif (" since " in str(answer).lower()):
        print("THREE")
        print("-----------------")
        aws = answer
        aws = aws.replace(".", "")
        aws = aws.replace("\n", "")
        aws = aws.replace("\r", "")
        aws = aws.split(" ")
        to_id = 0
        print(aws)
        for j in range(0, len(aws)):
            if (aws[j] == 'since'):
                to_id = j
                break
        wess = "How does "
        for j in range(to_id + 1, len(aws)):
            wess += (aws[j])
            wess += " "
        wess += "mean "
        for j in range(0, to_id):
            wess += (aws[j])
            wess += " "
        wess += "?\n"
        print(wess)
        session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        # to_do_list.append(i)

    elif ("because" in str(answer).lower()):
        print("THREE")
        print("-----------------")
        aws = answer
        aws = aws.replace(".", "")
        aws = aws.replace("\n", "")
        aws = aws.replace("\r", "")
        aws = aws.split(" ")
        aws = aws.split(" ")
        to_id = 0
        print(aws)
        for j in range(0, len(aws)):
            if (aws[j] == 'because'):
                to_id = j
                break
        wess = "How does "
        for j in range(to_id + 1, len(aws)):
            wes += (aws[j])
            wes += " "
        wess += "mean "
        for j in range(0, to_id):
            wess += (aws[j])
            wess += " "
        wess += "?\n"
        print(wess)
        session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        # to_do_list.append(i)  
    elif ("is the problem stemming from environment and cultural factors?" in str(question).lower()):
        if len(answer)>3:
            wess = "How to change "
            change = str(answer).strip('[')
            change = change.strip(']')
            change = change.split(',')
            f=False
            for word in change:
                word = word.strip("'")
                #print(word)
                if(f):
                    word = " " + str(word[2:])
                f=True
                #print(word)
                wess += word.strip("\'")
            
                wess += ","

            wess = wess.strip(',')
            wess += '?'
            session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        else:
            pass
            

    elif("is this problem coming from your value system?" in str(question).lower()):
        if len(answer)>3:
            wess = "How to change "
            change = str(answer).strip('[')
            change = change.strip(']')
            change = change.split(',')
            f=False
            for word in change:
                word = word.strip("'")
                #print(word)
                if(f):
                    word = " " + str(word[2:])
                f=True
                #print(word)
                wess += word.strip("\'")
            
                
                wess += ","

            wess = wess.strip(',')
            wess += '?'
            session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        else:
            pass