import io

import pandas as pd

from flask import Flask, render_template, request, session, abort, flash, redirect, url_for, jsonify, Response, \
    make_response
import spacy
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource
from waitress import serve
import os
import urllib.parse
os.environ['MONGODB_URI'] = "mongodb+srv://pharshil1902:hhpdhphrp@cluster0.pxxvw.mongodb.net/techqrt_chatbot?retryWrites=true&w=majority"
import pymongo
import uuid
global client
import ambiguity as am
from flask_bcrypt import Bcrypt
print(os.getenv('MONGODB_URI'))
client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
mydb = client["techqrt_chatbot"]    
global mycol
mycol = mydb["user_data"]


def verb_or_not(word):
    sp = spacy.load('en_core_web_sm')
    sen = sp(word)
    return (sen[0].pos_)



global app
app = Flask(__name__)

bcrypt = Bcrypt(app)

api = Api(app)
global ques
ques = []

global ques_list
ques_list = []
global tot
tot = []
global ans_dict
ans_dict = {}

global ent
ent = ''

global data
data = ['', '', '', '', ques, '', '']
global tot_ques
tot_ques = set()
global tot_ques_list
tot_ques_list = set()
global ans
ans = ['', '', '', '', '']
ques = [
    'How does the problem look? What is visible when the issue exists? Describe what you see when the problem occurs.',
    'How does the problem sound? What is audible when the issue exists? Describe what you hear when the problem occurs.',
    'How does the problem feel? What is felt when the issue exists? Describe what it feels like when the problem occurs.',
    'How does the problem smell? Describe what it smells like when the problem occurs.',
    'How does the problem taste? Describe what it tastes like when the problem occurs.'
]
data[4] = ques
ques_list = [
    "What is the purpose for addressing this problem?",
    'For whom is this a problem? Identify the specific individual, role or group.',
    'Do you believe the challenge exists? Who else (e.g., team, boss, client) believes the challenge exists?',
    'Is this problem coming from your value system?',
    'Is this problem coming because of a skills gap?',
    'Is the problem stemming out of a behavior issue?',
    'Is the problem stemming from environment and cultural factors?'
]
ans_dict[ques_list[0]] = ''
ans_dict[ques_list[1]] = ''
ans_dict[ques_list[2]] = ''
ans_dict[ques_list[3]] = ''
ans_dict[ques_list[4]] = ''
ans_dict[ques_list[5]] = ''
ans_dict[ques_list[6]] = ''

ans_dict[ques[0]] = ''
ans_dict[ques[1]] = ''
ans_dict[ques[2]] = ''
ans_dict[ques[3]] = ''
ans_dict[ques[4]] = ''

# 0 = uname
# 1 = passwd
# 2 = initial desc problem
# 3 = summary sentence
# 4 = list of problems
# 5 = links for the ques
global question
global answer
question = []
answer = []

hints = [
    'How does the problem look? What is visible when the issue occurs? Describe what you see when the problem exists. As you are sitting in your chair, visualize (with your eyes open or eyes closed) as though the problem is happening now. Examples:',
    'How does the problem sound? What is audible when the issue occurs? Describe what you hear when the problem exists. As you are sitting in your chair, listen as though the problem is happening now. Examples:',
    'How does the problem feel? What is felt when the issue occurs? Describe what it feels like when the problem exists. As you are sitting in your chair, feel as though the problem is happening now. Examples:',
    'How does the problem smell? What is smelt when the issue occurs? Describe what it smells like when the problem exists. As you are sitting in your chair, open up your sensory channels and describe the smells you may experience if the problem is happening now. Examples:',
    'How does the problem taste? What is smelt when the issue occurs? Describe what it tastes like when the problem exists. As you are sitting in your chair, open up your sensory channels and describe the tastes you may experience if the problem is happening now. Examples:',
]

holihints = [
    'holistic help1 - To be added',
    'holistic help2 - To be added',
    'Belief is about whether someone believes that something is possible, whether something is necessary or unnecessary.Do you believe that the problem / issue / opportunity exists? Does anyone else (e.g., team, boss, client) believe the problem / issue / opportunity exists? Does someone believe this problem / issue / opportunity could exist? Examples:',
    'holostic help4 - To be added',
    'Skills refers to the possibilities, competencies, qualities, and strategies that people can apply to engage in or initiate any activity or change. These could be technical competencies in your field and could also refer to “soft skills” such as the ability to adapt to the new, changing situation. Is the problem originating from a skills gap?  If yes, which skills? Examples:',
    'Behavior is about what people do and say. If an onlooker were to observe another person, the behaviors are what the onlooker would see, feel, or hear when the observed person is carrying out an activity. Behavior refers to action and reaction of a person in a particular environment. A person describes what he thought, did and what effect this action had in a certain situation. Is the problem originating from a behavior issue?  If yes, which behaviors?',
    'Environment refers to the external circumstances, factors & conditions that can influence the problem. Each problem takes place in a given time and geographical location. Cultural factors reflect what is important within the context of the organization (yours and / or the client). Is the problem originating from environmental and / or cultural factors? If yes, which factors? Examples: organisation culture, system, boss, management, industry, government, downturn, recession, natural calamities, family support, team support, friends, regulatory or legal constraints',

]

app.config['SECRET_KEY'] = "HY998246sedgsdJjw#%"


def update_db():

    result = mycol.update_many(
    {"user.name":f"{session['user']['name']}"},
    {
            "$set":{
                    f"user.problems":session['user']['problems']
                    },
    }
    )

    session['user'] = mycol.find({'user.name': session['user']['name'] })[0]['user']
    return result

        
@app.route('/',methods=['POST','GET'])
def signin():
    global data
    if('user' in session):
                print(f"session before: { session['user']} ")
                user = session['user']
                return render_template("page-d.html", data=data,user=user)
    else:

        global tot
        tot = []
        global ans_dict
        ans_dict = {}
        global question
        global queries
        queries = {}
        global answer
        question = []
        answer = []
        data = ['', '', '', '', ques, '', '', '']
        global tot_ques
        tot_ques = set()
        global tot_ques_list
        tot_ques_list = set()
        global ans
        ans = ['', '', '', '', '']
        data[4] = ques
        ans_dict[ques_list[0]] = ''
        ans_dict[ques_list[1]] = ''
        ans_dict[ques_list[2]] = ''
        ans_dict[ques_list[3]] = ''
        ans_dict[ques_list[4]] = ''
        ans_dict[ques_list[5]] = ''
        ans_dict[ques_list[6]] = ''

        ans_dict[ques[0]] = ''
        ans_dict[ques[1]] = ''
        ans_dict[ques[2]] = ''
        ans_dict[ques[3]] = ''
        ans_dict[ques[4]] = ''
        queries = {}
        answer = []
        tot = []
        tot_list = []
        global new_ques
        new_ques = {}

        question = []

        return render_template("index.html", data=data)


@app.route('/go_to_problem/<string:idd>',methods=['POST','GET'])
def go_to_problem(idd):
     
    user = session['user']
    for i in range(0,len(user['problems'])):
        if(idd == user['problems'][i]['problem_id'] ):
            session['id'] = i
            break

    data[2] = user['problems'][i]['initial_desc']
    session['page_no']=1
    return render_template('first_page.html',data=data,user=user,id = session['id'])

@app.route('/delete_problem/<string:idd>', methods=['POST', 'GET'])
def delete_problem(idd):
    result = mycol.update_many(
    {"user.name":f"{session['user']['name']}"},
    {
            "$pull":{
                    "user.problems":{'problem_id': idd}
                    },
    }
    )
    session['user'] = mycol.find({'user.name': session['user']['name'] })[0]['user']
    return render_template('page-d.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    return render_template('create_user.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')    

@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    if request.method == 'GET':
        return render_template('index.html')
    req = request.form
    name = req['name']
    password = req['password']

    hashed_password = bcrypt.generate_password_hash(password)
   
    result = mycol.insert_one(
        {
            'user':{
                'name':name,
                'password': hashed_password,
                'problems':[]
            }
        }
    )
    session['user'] = mycol.find({'user.name': name })[0]['user']
    return render_template('page-d.html')

global hints_ 
hints_ = {
   "how_prob_look": """ <b><u>Additional Information & Examples:</u></b> 
    <br> <div class="">
    <img src="/static/images/Picture2.png" alt="mike" width="750" height="500" />""",

    'how_prob_sound':"""<b><u>Additional Information & Examples:</u></b> 
    <img src="/static/images/Picture3.png" alt="mike" width="750" height="500" />""",


    'how_prob_feel':""" <b><u>Additional Information & Examples:</u></b> 
    <img src="/static/images/Picture4.png" alt="mike" width="750" height="500" />""",

    'how_prob_smell':"""<b><u>Additional Information & Examples:</u></b> 
    <img src="/static/images/Picture5.png" alt="mike" width="750" height="500" />""",

    'how_prob_taste':"""<b><u>Additional Information & Examples:</u></b> 
    <img src="/static/images/Picture6.png" alt="mike" width="750" height="500" />""",

    'purpose':"""Purpose is the highest level of affiliation mission, or vision. What is the “big picture” or larger goal we are trying to achieve? 
            <br> A.) What for?
            <br> B.)Who for?
            <br> C.)What is your mission?

            Towards what purpose is this problem being considered? What goal or objective are you aiming to achieve? What undesirable outcome are you aiming to avoid?

            Examples: 
            <br> 1.) To ensure our company’s financial stability and independence.
            <br> 2.) To help solve business problems with less time and cost.
            <br> 3.) To retain customers by enhancing their delight with our products and services.
            """,
    'for_whom':"""<img src="/static/images/Picture7.png" alt="mike" width="750" height="500" /> """,
    'is_prob_real':"""<img src="/static/images/Picture8.png" alt="mike" width="750" height="500" />""",
    'is_prob_value_sys':"""Values are standards or ideals with which we evaluate actions, people, things, or situations. 

                    <br>Values are why you want what you want. Values are what motivate us and influence our actions. An understanding of Values can be used to motivate ourselves and others more effectively.

                    <br>Our individual values are the basis of our motivation and the choices we make. They are those things that are important to us.  

                    <br>Corporate values fuel corporate vision. Leaders motivate people by finding out what is important to them. Values are usually abstract words such as love, happiness, achievement, ambition, health and fun.

                    <br>Is this problem arising from values (or the lack of values)?  If yes, which values?

                    <br>Examples: 
                        <br> 1.) Authenticity (self-awareness, self-mastery, self-belief, self-truth)
                        <br> 2.) Awareness (mindfulness, objectivity, empathy, reflection)
                        <br> 3.) Courage (confrontation, transformation, action, connection) 
                        <br> 4.) Enthusiasm (attitude, energy, curiosity, humor) 
                        <br> 5.) Faith (gratitude, forgiveness, love, spirituality) 
                        <br> 6.) Focus (clarity, concentration, speed, momentum) 
                        <br> 7.) Integrity (honesty, reliability, humility, stewardship) 
                        <br> 8.) Leadership (expectations, example, encouragement, celebration) 
                        <br> 9.) Perseverance (preparation, perspective, toughness, learning) 
                        <br> 10.) Purpose (aspiration, intentionality, selflessness, balance) 
                        <br> 11.) Service (helpfulness, charity, compassion, renewal) 
                        <br> 12.) Vision (attention, imagination, articulation, belief) 
                    """,
    'is_prob_skill_gap':"""<img src="/static/images/Picture9.png" alt="mike" width="750" height="500" />""",
    'behavior_prob':"""<img src="/static/images/Picture10.png" alt="mike" width="750" height="500" />""",
    'is_prob_envt_culture':"""Each problem occurs in a given time, place and context. 
                <br>Environment refers to the external circumstances, factors & conditions that can influence the problem. 
                <br>Cultural factors reflect what is important within the context of the organization (yours and / or the client). 

                <br>Is the problem originating from environmental and/or cultural factors? If yes, which factors? 

                <br>Examples: 

                    <br> 1.) organisation culture
                    <br> 2.) system
                    <br> 3.) boss
                    <br> 4.) management
                    <br> 5.) leadership
                    <br> 6.) industry
                    <br> 7.) government
                    <br> 8.) downturn
                    <br> 9.) recession
                    <br> 10.) natural calamities
                    <br> 11.) family support
                    <br> 12.) team support 
                    <br> 13.) friends
                    <br> 14.) regulatory or legal constraints
                """,

}

global ques_explain
ques_explain = {
    "how_prob_look": """Explanation: 
How does the challenge look? What is visible when the issue occurs? Describe what you see when the situation exists. 
As you are sitting in your chair, visualize (with your eyes open or eyes closed) as though the challenge is happening now. 

Answer is limited to 100 characters (including blank spaces).
Please click “Help” button for additional information and examples.

                                          "Knowing how each of our senses influences our internal perception leads to a more complete 
                                                                                   awareness of the situation.”""",
    'how_prob_sound':"""Explanation: 
How does the challenge sound? What is audible when the issue occurs? Describe what you hear when the situation exists. 
As you are sitting in your chair, listen as though the challenge is happening now. 

Answer is limited to 100 characters (including blank spaces).
Please click “Help” button for additional information and examples.

                                           "Knowing how each of our senses influences our internal perception leads to a more complete 
                                                                                   awareness of the situation.”""",
    'how_prob_feel':"""Explanation: 
How does the challenge feel? What is felt when the issue occurs? Describe what it feels like when the situation exists. 
As you are sitting in your chair, feel as though the challenge is happening now. 
Answer is limited to 100 characters (including blank spaces).
Please click “Help” button for additional information and examples.

                                           "Knowing how each of our senses influences our internal perception leads to a more complete 
                                                                                   awareness of the situation.”""",
    'how_prob_smell':"""Explanation: 
How does the challenge smell? What is smelt when the issue occurs? Describe what it smells like when the situation exists. 
As you are sitting in your chair, open up your sensory channels and describe the smells you may experience if the problem is happening now. 
In case there is absolutely no “smell sensation” to your challenge, you may answer Not Applicable or N/A.
Answer is limited to 100 characters (including blank spaces).
Please click “Help” button for additional information and examples.

                                           "Knowing how each of our senses influences our internal perception leads to a more complete 
                                                                                   awareness of the situation.”""",
    'how_prob_taste':"""Explanation: 
How does the challenge taste? What is tasted when the issue occurs? Describe what it tastes like when the situation exists. 
As you are sitting in your chair, open up your sensory channels and describe the tastes you may experience if the challenge is happening now. 
In case there is absolutely no “taste sensation” to your challenge, you may answer Not Applicable or N/A.

Answer is limited to 100 characters (including blank spaces). 
Please click “Help” button for additional information and examples.

                                           "Knowing how each of our senses influences our internal perception leads to a more complete 
                                                                                   awareness of the situation.”""",
    'purpose':"""Explanation: 
Purpose is the highest holistic level of affiliation mission, or vision. What is the “big picture” or larger goal we are trying to achieve? 
What for?
Who for?
What is your mission?
Towards what higher purpose is this challenge/goal/objective being considered? 
What goal or objective are you aiming to achieve? 
What undesirable outcome are you aiming to avoid?

Answer is limited to 100 characters (including blank spaces).
Please click “Help” button for additional information and examples.""",
    'for_whom':"""Explanation: 
>Identity is about the question: “who are we?”. 
>This enables people who are going through change to forge a shared identity. 
>For whom is this a challenge, opportunity or issue? 
>Because of whom does this situation exist? 

Description is limited to 100 characters (including blank spaces).

Please click “Help” button for additional information and examples.""",
    'is_prob_real':"""Explanation: 
>Belief is about whether someone believes that something is possible, whether something is necessary or unnecessary.

Answer is limited to 100 characters (including blank spaces).

Please click “Help” button for additional information and examples.""",
    'is_prob_value_sys':"""Explanation: 
>Values are standards or ideals with which we evaluate actions, people, things, or situations. 
>Values are what motivate us and influence our actions. 
>Values are usually abstract words such as love, happiness, achievement, courage, humility, integrity, fulfillment, ambition, health and fun.

Please click “Help” button for additional information and examples.""",
    'is_prob_skill_gap':"""Explanation: 
Skills refers to the possibilities, competencies,( technical and soft skills) qualities, and strategies that people can apply to engage in or initiate any activity or change.
In case there is absolutely no “skill gap” to your challenge, you may answer Not Applicable or N/A.

Please click “Help” button for additional information and examples.""",
    'behavior_prob':"""Explanation: 
Behavior is about what people do and say.
Behavior refers to action and reaction of a person in a particular environment. 
A person describes what he thought, did and what effect this action/behaviour had in a certain situation.
In case there is absolutely no “behavior issue” to your challenge, you may answer Not Applicable or N/A.

Please click “Help” button for additional information and examples.""",
    'is_prob_envt_culture':"""Explanation: 
Each problem occurs in a given time, place and context. 
Environment refers to the external circumstances, factors & conditions that can influence the problem. 
Cultural factors reflect what is important within the context of the organization (yours and / or the client). 

Please click “Help” button for additional information and examples.""",
}
# session['questions'][session['current_ques_id']]
@app.route('/create_problem', methods=['POST', 'GET'])
def create_problem():
    if request.method == 'GET':
        return render_template('page-d.html')

    if len(session['user']['problems']) != 0:
        index = len(session['user']['problems']) - 1
        problem_id = int(session['user']['problems'][index]['problem_id']) + 1
    else:
        problem_id = len(session['user']['problems']) + 1
    
    user = session['user']
    user['problems'].append(
        {
                        "problem_id":f"{problem_id}",
                        "problem_name":"",
                        "initial_desc":"",
                        "initial_prob_st":"",
                        "how_prob_look":{
                            "ques":"How does the problem look? What is visible when the issue exists? Describe what you see when the problem occurs.",
                            "ans":"",

                        },
                        "how_prob_sound":{
                            "ques":"How does the problem sound? What is audible when the issue exists? Describe what you hear when the problem occurs.",
                            "ans":"",
                        
                        },
                        "how_prob_feel":{
                            "ques":"How does the problem feel? What is felt when the issue exists? Describe what it feels like when the problem occurs.",
                            "ans":"",
                          
                        },
                        "how_prob_smell":{
                            "ques":"How does the problem smell? Describe what it smells like when the problem occurs.",
                            "ans":"",
                          
                        },
                        "how_prob_taste":{
                            "ques":"How does the problem taste? Describe what it tastes like when the problem occurs.",
                            "ans":"",
                           
                        },
                        "purpose":{
                            "ques":"What is the purpose for addressing this problem?",
                            "ans":"",
                        },
                        "for_whom":{
                            "ques":"For whom is this a problem? Identify the specific individual, role or group.",
                            "ans":"",
                        },
                        "is_prob_real":{
                            "ques":"Do you believe the challenge exists? Who else (e.g., team, boss, client) believes the challenge exists?",
                            "ans":"",
                        },
                        "is_prob_value_sys":{
                            "ques":"Is this problem coming from your value system?",
                            "ans":"",
                            "yesno":"0"
                        },
                        "is_prob_skill_gap":{
                            "ques":"Is this problem coming because of a skills gap?",
                            "ans":"",
                        },
                        "behavior_prob":{
                            "ques":"Is the problem stemming out of a behavior issue?",
                            "ans":"",
                        },
                        "is_prob_envt_culture":{
                            "ques":"Is the problem stemming from environment and cultural factors?",
                            "ans":"",
                            "yesno":"0"
                        },
                        "how_to_stmts":[
                         ],
                        "how_to_st":"",
                        "what_would":{
                            "ques":"",
                            "ans":""
                        },
                        "selected_how_to":{
                            "question":"",
                            "ambiguity":[
                                {
                                    "vague":"",
                                    "ques":"",
                                    "ans":""
                                }
                            ]
                        },
                        "before_ambi":"",
                        "final_question":""
                    }
    )
    session['user'] = user
    session['current_ques_id'] = problem_id
    print(session['current_ques_id'])
    update_db()
    return redirect(f'/go_to_problem/{problem_id}')



@app.route('/signin', methods=['POST', 'GET'])
def signing():
    global data
    req = request.form
    # IF 'GET' REQUEST -- DIRECTLY RENDERS DASHBOARD 
    if (request.method == 'GET'):
        return render_template("page-d.html", data=data,user=session['user'])
    else:
        # REDUNDTANT DATA --- START
        data[0] = req['uname']
        data[1] = req['passwd']
        print(data[0], data[1])
        data[2] = ''
        data[3] = ''
        data[6] = ''
        # REDUNDTANT DATA --- END

        # For database perspective
        mydb = client["techqrt_chatbot"]     #GETS COLLECTION
        mycol = mydb["user_data"]            # DB 
        
        x = mycol.find()
        user = {'name':f"{req['uname']}",'password':f"{req['passwd']}"}     # CREATES USER OBJECT
        # CHECKS IF 'USER' THERE IN SESSION OR NOT
        if('user' in session):      
                print(f"session before: { session['user']} ") 
                # TAKES USER FROM SESSION STORAGE
                user = session['user']
                # RENDERS FIRST_PAGE
                return render_template("first_page.html", data=data,user=user)
        # CHECKS FOR USER THERE IN DATABASE OR NOT        
        for users in x:
            user_id = users['_id']
            print(user_id)
            print(users['user']['name'])
            print(user['name'])
            # IF USERNAME THERE IN DB:
            if(users['user']['name'] == user['name']):
                    print(users['user']['password'])
                    print(user['password'])
                    # CHECKS IF USER-PASSWORD-HASH IS CORRECT OR NOT
                    if(bcrypt.check_password_hash(users['user']['password'],user['password'] )):
                        session['user'] = users['user']
                        print(f"session after: { type(session['user']) } ")
                        user = session['user']
                        # RENDERS DASHBOARD
                        return render_template("page-d.html", data=data,user=user)
        return redirect('/')


@app.route('/second_db', methods=['POST', 'GET'])
def second_db():
    req = request.form
    user = session['user']
    #print(session['user'])
    if (request.method == 'GET'):
        return render_template("second.html", data=data,user=user)
    else:
        data[2] = req['problem_desc']
        data[6] = req['prob_name']
        question.append("Initial Description of the Problem")
        answer.append(data[2])
        i = session['id']
        user['problems'][i]['initial_desc'] = req['problem_desc']
        user['problems'][i]['problem_name'] = req['prob_name']
        session['user'] = user
        d = update_db()

  
        return render_template('first_page.html', data=data)

@app.route('/second', methods=['POST', 'GET'])
def second():
    req = request.form
    if (request.method == 'GET'):
        session['page_no'] -= 1        
        return render_template("second.html", data=data)
    else:
        data[2] = req['problem_desc']
        data[6] = req['prob_name']
        question.append("Initial Description of the Problem")
        answer.append(data[2])
        session['page_no'] +=1
        return render_template('second.html', data=data)


@app.route('/list_problem_db', methods=['POST', 'GET'])
def list_problem_db(): 
    req = request.form
    user = session['user']
    i= session['id']
    user['problems'][i]['initial_prob_st'] = str(req['second'])
    session['user'] = user
    d = update_db() 
    
    return render_template('second.html')


@app.route('/list_problem', methods=['POST', 'GET'])
def list_problem():
    req = request.form
    data[3] = req['second']
    question.append("Initial Problem Summary Sentence")
    answer.append(data[3])
 

    session['answers'] =  ['','','']

    session['questions'] = [
        'how_prob_look',
        'how_prob_sound',
        'how_prob_feel',
        'how_prob_smell',
        'how_prob_taste',
        'purpose',
        'for_whom',
        'is_prob_real',
        'is_prob_value_sys',
        'is_prob_skill_gap',
        'behavior_prob',
        'is_prob_envt_culture',
        
    ]
    session['current_ques_id'] = -1
    i = session['id']
    

    
    session['answers'] =  ['','','']

    print(session['user']['problems'][i]['initial_prob_st'])
    session['page_no'] += 1


    return render_template('list_problems.html', data=data)

@app.route('/download', methods=['POST'])
def route_download():
    x = mycol.find()
    i = session['id']
    all_problems = session['user']['problems']


    final_question = session['user']['problems'][session['id']]['selected_how_to']['question']
    print(final_question)
    dataFrame = pd.DataFrame(data = all_problems, columns=['problem_id','initial_desc','initial_prob_st','how_prob_feel','how_prob_look','how_prob_smell','how_prob_sound','how_prob_taste','purpose','for_whom','is_prob_envt_culture','is_prob_real','is_prob_skill_gap','is_prob_value_sys','behavior_prob','final_question'])

    # index = dataFrame.loc[:,['problem_id','initial_desc','initial_prob_st','how_prob_feel','how_prob_look','how_prob_smell','how_prob_sound','how_prob_taste','is_prob_envt_culture','is_prob_real','is_prob_skill_gap','is_prob_value_sys']]
    # inserting_final_ans = index.insert(12, "final_question", final_question)
    # print(inserting_final_ans)

    print('test2')
    print(dataFrame)
    for i in range(0, len(dataFrame.index)):
        dataFrame['is_prob_real'][i] = dict(dataFrame['is_prob_real'][i])
        # print(dataFrame.iloc[i, [9]])
        # print(dataFrame[3][i][0])

        # dataFrame[3][i] = dataFrame[3][i]['ans']


        dataFrame['is_prob_real'][i] = dataFrame['is_prob_real'][i]['ans']
        dataFrame['how_prob_feel'][i] = dataFrame['how_prob_feel'][i]['ans']
        dataFrame['how_prob_look'][i] = dataFrame['how_prob_look'][i]['ans']
        dataFrame['how_prob_smell'][i] = dataFrame['how_prob_smell'][i]['ans']
        dataFrame['how_prob_sound'][i] = dataFrame['how_prob_sound'][i]['ans']
        dataFrame['how_prob_taste'][i] = dataFrame['how_prob_taste'][i]['ans']
        dataFrame['is_prob_envt_culture'][i] = dataFrame['is_prob_envt_culture'][i]['ans']
        dataFrame['is_prob_skill_gap'][i] = dataFrame['is_prob_skill_gap'][i]['ans']
        dataFrame['is_prob_value_sys'][i] = dataFrame['is_prob_value_sys'][i]['ans']
        dataFrame['behavior_prob'][i] = dataFrame['behavior_prob'][i]['ans']
        dataFrame['for_whom'][i] = dataFrame['for_whom'][i]['ans']
        dataFrame['purpose'][i] = dataFrame['purpose'][i]['ans']


   
    # datatoexcel = pd.ExcelWriter('CarsData1.xlsx', engine='xlsxwriter')
    #
    # # write DataFrame to excel
    # dataFrame.to_excel(datatoexcel, sheet_name='my_analysis', index=False, na_rep='NaN')
    #
    # # for column in dataFrame:
    # #     column_width = max(dataFrame[column].astype(str).map(len).max(), len(column))
    # #     col_idx = dataFrame.columns.get_loc(column)
    # #     datatoexcel.sheets['my_analysis'].set_column(col_idx, col_idx, column_width)
    # col_idx = dataFrame.columns.get_loc('how_prob_sound')
    # datatoexcel.sheets['my_analysis'].set_column(col_idx, col_idx, 30)
    # # save the
    # datatoexcel.save()
    #
    # print(datatoexcel)
    
    # resp = make_response(pd.read_excel(datatoexcel).to_csv())
    # print(resp)
    resp = make_response(dataFrame.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv; charset=UTF-8"
    return resp
    
    # 
    # datatoexcel = pd.ExcelWriter('path_to_excel.xlsx')
    # dataFrame.to_excel(datatoexcel)
    # datatoexcel.save()
    # headers = {
    #     'Content-Disposition': 'attachment; filename=output.xlsx',
    #     'Content-type': 'application/vnd.ms-excel'
    # }
    # return Response(dataFrame.to_excel(), mimetype='application/vnd.ms-excel', headers=headers)


def tag_ret():

    if (session['current_ques_id'] == 8):
        r_ans = """ """
        lis = ['Authenticity',
               'Awareness',
               'Courage',
               'Enthusiasm',
               'Faith',
               'Focus',
               'Integrity',
               'Leadership',
               'Perseverance',
               'Purpose',
               'Service',
               'Vision'
               ]

        for i in lis:
            if len(session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]) == 0:
                session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]=[]
            if (i in session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['ans']):
                # r_ans+=f"""<input type="checkbox" name="answer" value="{i}" checked>{i}<br>"""
                r_ans += f"""<ul  style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input class="check" type="checkbox" id="answer" name="answer" value="{i}" checked> {i}</ul>"""
            else:
                # r_ans+=f"""<input type="checkbox" name="answer" value="{i}" >{i}<br>"""
                r_ans += f"""<ul style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input class="check" type="checkbox" id="answer" name="answer" value="{i}" > {i}</ul>"""

        y=""
        n=""
        d=""
        print("heee")
        if session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['yesno'] == '1': 
            
            y="checked"
            n=""

        else:
            y=""
            n="checked"   
            d="""style="display:none;" """ 
        # return f"""<center><input   type="radio" onchange="db()" name="yn" id="y" value="1">Yes<input type="radio" name="yn" id="n" onchange="db()" value="0">No<br><br><br><div id="dv" style="display:none;"><center>{r_ans}</center></div>"""
        return f"""<textarea onkeyup="mycounter()" class="form-control" style="font-size: 15px;font-weight: bold;" rows="8"  maxlength = "100"  disabled>{session['explain']}</textarea><center style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input   type="radio" onchange="db()" name="yn" id="y" value="1" {y} required>Yes<br><input type="radio" name="yn" id="n" onchange="db()" value="0" {n} required>No<br></center><br><br><div id="dv" {d} >{r_ans}</div>"""

    elif (session['current_ques_id'] == 11):
        r_ans = """ """
        lis = ['boss',
               'downturn',
               'government',
               'industry',
               'lack of family support',
               'lack of team support',
               'leadership',
               'management',
               'natural calamities',
               'organisation culture',
               'recession',
               'regulatory or legal constraints',
               'system'
               ]
        for i in lis:
            if len(session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]) == 0: 
                session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]=[]
            if (i in session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['ans']):
                # r_ans+=f"""<input type="checkbox" name="answer" value="{i}" checked>{i}<br>"""
                r_ans += f"""<ul  style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input class="check" type="checkbox" id="answer" name="answer" value="{i}" checked> {i}</ul>"""
            else:
                # r_ans+=f"""<input type="checkbox" name="answer" value="{i}" >{i}<br>"""
                r_ans += f"""<ul style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input class="check" type="checkbox" id="answer" name="answer" value="{i}" > {i}</ul>"""

        y=""
        n=""
        d=""
        if session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['yesno'] == '1':  
            y="checked"
            n=""

        else:
            y=""
            n="checked"   
            d="""style="display:none;" """ 
        # return f"""<center><input   type="radio" onchange="db()" name="yn" id="y" value="1">Yes<input type="radio" name="yn" id="n" onchange="db()" value="0">No<br><br><br><div id="dv" style="display:none;"><center>{r_ans}</center></div>"""
        return f"""<textarea onkeyup="mycounter()" class="form-control" style="font-size: 15px;font-weight: bold;" rows="8"  maxlength = "100"  disabled>{session['explain']}</textarea><center style=" font-size: 22px;font-family: 'Cabin';color: #0b4c68;"><input   type="radio" onchange="db()" name="yn" id="y" value="1" {y} required>Yes<br><input type="radio" name="yn" id="n" onchange="db()" value="0" {n} required>No<br></center><br><br><div id="dv" {d} >{r_ans}</div>"""


    else:
        # return f""" <textarea class="textarea"  name="answer" id="" cols="80" rows="20">{ans}</textarea>"""
        # d = session['user']['problems'][session['id']][session['questions'][session['current_ques_id']]]['ans']
        return f"""<textarea onkeyup="mycounter()" class="form-control" style="font-size: 15px;font-weight: bold;" rows="9"  maxlength = "100"  disabled>{session['explain']}</textarea> <textarea onkeyup="mycounter()" class="form-control" rows="3" id="answer" maxlength = "100" placeholder="Enter answer here (limit 100 characters)" name="answer">{session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['ans']}</textarea> <span id="counter"></span>"""
# {session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ]['ans']}

@app.route('/list_problems_db', methods=['POST', 'GET'])
def list_problems_db():
    print("innnn")

    req = request.form
    user = session['user']
    i = session['id']
    
    print(req.getlist('answer'))
    
    if session['current_ques_id'] in [8,11]:
        
        user['problems'][i][session['questions'][session['current_ques_id']]]['yesno'] = req['yn']
        
        print(req['yn'])
        if req['yn']=='0':
           
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = []
        else:
           print(req['answer'])
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req.getlist('answer')
    else:
        user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req['answer']
    session['user'] = user
    
    d = update_db()
    print("yess")
    session['type'] = tag_ret()
    print("yess----")
    return render_template('ques_page.html',save=1)

@app.route('/list_problems_db_ns', methods=['POST', 'GET'])
def list_problems_db_ns():
    print("innnn")
    # i = session['id']
    # print(session['user']['problems'][i]['initial_prob_st'])
    # x = mycol.find({'user.problems': session['user']['problems'][i]['initial_prob_st']})
    # print(x)
    # for y in x:
    #     print(y)
    
    req = request.form
    user = session['user']

    i = session['id']
    print(i)


    if session['current_ques_id'] == -1:
        session['current_ques_id'] = 0
        session['hint'] = hints_[session['questions'][session['current_ques_id']]]
        session['save_check'] = 0
        session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
        session['type'] = tag_ret()
        return render_template('ques_page.html',save=0)
    if session['current_ques_id'] in [8,11]:
        
        user['problems'][i][session['questions'][session['current_ques_id']]]['yesno'] = req['yn']
        
        print(req['yn'])
        if req['yn']=='0':
           
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = []
        else:
           print(req['answer'])
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req.getlist('answer')
    else:
        user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req['answer']
    session['user'] = user

    d = update_db()
    print("yess")
    session['type'] = tag_ret()
    print("yess----")
    # ----------------------------------------------------
    print(session['current_ques_id'])
    if request.method == 'GET':
        print("get got")
        session['page_no'] -= 1
        return render_template('summary.html')
    if session['current_ques_id'] == 11:
        session['page_no'] += 1
        return render_template('summary.html')
    session['page_no'] += 1    
    if session['current_ques_id'] == 4:
        return render_template('holistic.html',ques_list=ques_list)
    i = session['id']
    #print(session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ])
    
    session['current_ques_id'] = session['current_ques_id'] + 1
    print(hints_[session['questions'][0]])
    print(session['current_ques_id'])
    session['hint'] = hints_[session['questions'][session['current_ques_id']]] 
    session['save_check'] = 0
    session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
    
    session['type'] = tag_ret() 

    print(f"ques-no: ------------ {session['current_ques_id']}")  
    print(session['type']) 



    return render_template('ques_page.html',save=0)

@app.route('/list_problems_db_bs', methods=['POST', 'GET'])
def list_problems_db_bs():
    print("innnn")
    req = request.form
    print(req)
    user = session['user']
    i = session['id']
    if request.method == 'GET' and session['current_ques_id'] == 11:
        session['page_no'] -= 1
        return render_template('ques_page.html',save=0)
    
    print(req.getlist('answer'))
    
    if session['current_ques_id'] in [8,11]:
        
        user['problems'][i][session['questions'][session['current_ques_id']]]['yesno'] = req['yn']
        
        print(req['yn'])
        if req['yn']=='0':
           
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = []
        else:
           print(req['answer'])
           user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req.getlist('answer')
    else:
        user['problems'][i][session['questions'][session['current_ques_id']]]['ans'] = req['answer']
    session['user'] = user
    
    d = update_db()
    print("yess")
    session['type'] = tag_ret()
    print("yess----")
    # -------------------------------------
   
    session['page_no'] -= 1
    if session['current_ques_id'] == 0:
        session['current_ques_id'] = -1
        session['hint'] = hints_[session['questions'][session['current_ques_id']]]
        session['save_check'] = 0
        session['explain'] = ques_explain[session['questions'][session['current_ques_id']]] 
        return render_template('list_problems.html')
    session['current_ques_id'] = session['current_ques_id'] - 1
    session['hint'] = hints_[session['questions'][session['current_ques_id']]] 
    session['save_check'] = 0
    session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
    if session['current_ques_id'] == 4:
        return render_template('holistic.html',ques_list=ques_list)
    session['type'] = tag_ret()
    return render_template('ques_page.html',save=0)

@app.route('/sum', methods=['POST', 'GET'])
def sum():
    if request.method == 'GET':
            session['page_no'] -= 1   
            return render_template('summary.html') 
    session['page_no'] += 1    

@app.route('/how_to_screen', methods=['POST', 'GET'])
def how_to_screen():
    if request.method == 'GET':
            session['page_no'] -= 1   
            return render_template('how_to.html') 
    req = request.form 
    session['page_no'] += 1
    length = len(session['questions'])
    for i in range(0,length):
       session['user']['problems'][session['id']][session['questions'][i] ]['ans'] = req[f"question{i}" ]
    session['user']['problems'][session['id']]['initial_prob_st'] = req['initial_prob_st']
    session['user']['problems'][session['id']]['initial_desc'] = req['initial_desc']
    return render_template('how_to.html')

@app.route('/list_problems_db_f', methods=['POST', 'GET'])
def list_problems_db_f():
    print(session['current_ques_id'])
    if request.method == 'GET':
        print("get got")
        session['page_no'] -= 1
        return render_template('summary.html')
    if session['current_ques_id'] == 11:
        session['page_no'] += 1
        return render_template('summary.html')
    session['page_no'] += 1    
    if session['current_ques_id'] == 4:
        return render_template('holistic.html',ques_list=ques_list)
    i = session['id']
    #print(session['user']['problems'][session['id']][session['questions'][session['current_ques_id']] ])
    if session['current_ques_id'] == -1:
        session['current_ques_id'] = 0
        session['hint'] = hints_[session['questions'][session['current_ques_id']]]
        session['save_check'] = 0
        session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
        session['type'] = tag_ret()
        return render_template('ques_page.html')
    session['current_ques_id'] = session['current_ques_id'] + 1
    print(hints_[session['questions'][0]])
    print(session['current_ques_id'])
    session['hint'] = hints_[session['questions'][session['current_ques_id']]] 
    session['save_check'] = 0
    session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
    
    session['type'] = tag_ret() 

    print(f"ques-no: ------------ {session['current_ques_id']}")  
    print(session['type']) 
    
    return render_template('ques_page.html',save=0)
# session['user']['problems'][session['id']][session['questions'][session['current_ques_id']]]['hint']

@app.route('/list_problems_db_b', methods=['POST', 'GET'])
def list_problems_db_b():
     
    if request.method == 'GET' and session['current_ques_id'] == 11:
        session['page_no'] -= 1
        return render_template('ques_page.html',save=0)
    session['page_no'] -= 1
    if session['current_ques_id'] == 0:
        session['current_ques_id'] = -1
        session['hint'] = hints_[session['questions'][session['current_ques_id']]]
        session['save_check'] = 0
        session['explain'] = ques_explain[session['questions'][session['current_ques_id']]] 
        return render_template('list_problems.html')
    session['current_ques_id'] = session['current_ques_id'] - 1
    session['hint'] = hints_[session['questions'][session['current_ques_id']]] 
    session['save_check'] = 0
    session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
    if session['current_ques_id'] == 4:
        return render_template('holistic.html',ques_list=ques_list)
    session['type'] = tag_ret()
    return render_template('ques_page.html',save=0)

@app.route('/after_holi',methods=['GET','POST'])
def after_holi():
    session['current_ques_id'] = session['current_ques_id'] + 1
    session['hint'] = hints_[session['questions'][session['current_ques_id']]] 
    session['save_check'] = 0
    session['explain'] = ques_explain[session['questions'][session['current_ques_id']]]
    session['type'] = tag_ret()  
    session['page_no'] += 1
    return render_template('ques_page.html',save=0)

@app.route('/before_holi',methods=['GET','POST'])
def before_holi():
    session['type'] = tag_ret()
    print("runn")
    session['page_no'] -= 1   
    return render_template('ques_page.html',save=0)    


@app.route('/list_problems', methods=['POST', 'GET'])
def list_problems():
    req = request.form

    if (request.method == 'POST'):

        if (5 > 0):

            global tot
            tot = [0, 1, 2, 3, 4]

            for i in tot:
                tot_ques.add(i)
            print(f"totlist: {tot}")

            page = int(0)
            print(page)
            tt = tot
            print(id(tot))
            ans_dict[ques[int(tt[page])]] = ''
            return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])],
                                   hint=hints[int(tot[int(page)])], no=int(page),
                                   ans=ans_dict[ques_list[int(tot[int(page)])]], num=int(tot[page]))
        else:
            return redirect(url_for('holistic'))
    else:
        return render_template("list_problems.html", data=data, ques=ques)


@app.route('/holistic', methods=['POST', 'GET'])
def holistic():
    """req = request.form

    if(request.method == 'GET'):
        return render_template("holistic.html",data=data,ques_list = ques_list)
    else:
        return render_template('holistic.html',data=data,ques_list=ques_list)"""
    req = request.form
    if (request.method == 'POST'):

        if (7 > 0):

            global tot_list
            tot_list = [0, 1, 2, 3, 4, 5, 6]

            for i in tot_list:
                tot_ques_list.add(i)
            print(f"totlist: {tot_list}")
            page = int(0)
            print(page)
            tt = tot_list

            print(id(tot_list))
            ans = ans_dict[ques_list[page]]
            tag = tag_ret(int(tot_list[int(page)]), ans)
            print(tag)
            return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                                   no=int(page), ans=ans_dict[ques_list[int(tot_list[int(page)])]], num=int(tt[page]),
                                   tag=tag)
        else:

            for i in range(0, len(tot)):
                question.append(ques[int(tot[i])])
                answer.append(ans_dict[ques[int(tot[i])]])
            for i in range(0, len(tot)):
                question.append(ques_list[int(tot_list[i])])
                answer.append(ans_dict[ques_list[int(tot_list[i])]])

            return render_template('summary.html', question=question, answer=answer)
    else:
        return render_template("holistic.html", data=data, ques_list=ques_list)
    # list-problems button to open particular ques & ques2 for holistic


@app.route('/ques_page', methods=['POST', 'GET'])
def ques_page():
    if (request.method == 'GET'):
        page = 0
        return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[page])], no=int(page),
                               ans=ans_dict[ques[int(tot[int(page)])]])
    else:
        req = request.form

        for i in req.getlist('tot_ques'):
            tot_ques.add(i)
        page = int(req['butt'])
        print(page)
        return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                               ans=ans_dict[ques[int(tot[int(page)])]])


@app.route('/holi', methods=['POST', 'GET'])
def holi():
    return render_template('holistic.html', data=data, ques_list=ques_list)


@app.route('/save_ans', methods=['POST', 'GET'])
def save_ans():
    if (request.method == 'GET'):
        page = 0
        return render_template("ques_page.html", data=data, ques=ques, page=ques[page], no=int(page),
                               ans=ans_dict[ques[int(tot[int(page)])]])
    else:
        req = request.form
        page = req['page']
        ans_dict[page] = req['answer']
        page = int(req['no'])

        anw = req['answer']

        ans[page] = anw

        print(page)
        print(ans[page])
        return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                               ans=ans_dict[ques[int(tot[int(page)])]], num=int(req['num']))


@app.route('/ques_page2', methods=['POST', 'GET'])
def ques_page2():
    if (request.method == 'GET'):
        page = 0
        ans = ans_dict[ques_list[int(tot[int(page)])]]
        tag = tag_ret(int(tot_list[int(page)]), ans)
        return render_template("ques_page_2.html", data=data, ques=queslist, page=ques[page], no=int(page),
                               ans=ans_dict[ques_list[int(tot[int(page)])]], tag=tag)
    else:
        req = request.form

        for i in req.getlist('tot_ques'):
            tot_ques.add(i)

        page = req['butt']
        print(page)
        ans = ans_dict[ques_list[page]]
        tag = tag_ret(int(tot_list[int(page)]), ans)
        return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                               no=int(page), ans=ans_dict[ques_list[int(tot_list[int(page)])]], tag=tag)


@app.route('/first_seq_ques', methods=['POST', 'GET'])
def first_seq_ques():
    req = request.form

    if (request.method == 'POST'):

        if (len(req.getlist('tot_ques')) > 0):

            global tot
            tot = [0, 1, 2, 3, 4]

            for i in req.getlist('tot_ques'):
                tot_ques.add(i)
            print(f"totlist: {tot}")

            page = int(0)
            print(page)
            tt = tot
            print(id(tot))
            ans_dict[ques[int(tt[page])]] = ''
            return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                                   ans=ans_dict[ques_list[int(tot[int(page)])]], num=int(tt[page]))
        else:
            return redirect(url_for('holistic'))
    else:
        return render_template("list_problems.html", data=data, ques=ques)


@app.route('/seq_ques', methods=['POST', 'GET'])
def seq_ques():
    if (request.method == 'POST'):
        global ans_dict
        req = request.form
        page = req['page']
        ans_dict[page] = req['answer']
        req = request.form
        print(req['no'])
        print(len(tot))
        if (int(req['no']) + 1 == len(tot)):

            global tot_list
            tot_list = [0, 1, 2, 3, 4, 5, 6]
            global ques_list
           
            
          
            for i in tot_list:
                tot_ques_list.add(i)
            print(f"totlist: {tot_list}")
            page = int(0)
            print(page)
            tt = tot_list

            print(id(tot_list))
            print(ans_dict)
            ans = ans_dict[ques_list[page]]
            tag = tag_ret(int(tot_list[int(page)]), ans)
            print(tag)
            return redirect(url_for('holi'))
        else:
            no = int(req['no'])
            no += 1
            page = no
            return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])],
                                   hint=hints[int(tot[int(page)])], no=int(page),
                                   ans=ans_dict[ques[int(tot[int(page)])]], num=int(tot[int(page)]))
    else:
        return render_template("list_problems.html", data=data)


@app.route('/first_seq_ques_list', methods=['POST', 'GET'])
def first_seq_ques_list():
    req = request.form
    if (request.method == 'POST'):

        if (len(req.getlist('tot_ques')) > 0):

            global tot_list
            tot_list = [0, 1, 2, 3, 4, 5, 6]

            for i in req.getlist('tot_ques'):
                tot_ques_list.add(i)
            print(f"totlist: {tot_list}")
            page = int(0)
            print(page)
            tt = tot_list
            global ans_dict
           

            print(id(tot_list))
            ans = ans_dict[ques_list[page]]
            tag = tag_ret(int(tot_list[int(page)]), ans)
            print(tag)
            return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                                   holihint=holihints[int(tot_list[int(page)])], no=int(page),
                                   ans=ans_dict[ques_list[int(tot_list[int(page)])]], num=int(tt[page]), tag=tag,
                                   ques_list=ques_list)
        else:

            for i in range(0, len(tot)):
                question.append(ques[int(tot[i])])
                answer.append(ans_dict[ques[int(tot[i])]])
            for i in range(0, len(tot)):
                question.append(ques_list[int(tot_list[i])])
                answer.append(ans_dict[ques_list[int(tot_list[i])]])

            return render_template('summary.html', question=question, answer=answer)
    else:
        return render_template("holistic.html", data=data, ques_list=ques_list)


@app.route('/seq_ques_list', methods=['POST', 'GET'])
def seq_ques_list():
    global ques_list
    

    if (request.method == 'POST'):
        req = request.form
        page = req['page']
        if (int(req['num']) == 3):
            ans_dict[page] = req.getlist('answer')
        elif (int(req['num']) == 6):
            ans_dict[page] = req.getlist('answer')
        else:
            ans_dict[page] = req['answer']
        req = request.form
        print(req['no'])
        no = int(req['no'])
        no+=1
        if (int(req['no']) + 1 == len(tot_list)):

            for i in range(0, len(tot)):
                question.append(ques[int(tot[i])])
                answer.append(ans_dict[ques[int(tot[i])]])
            for i in range(0, len(tot_list)):
                question.append(ques_list[int(tot_list[i])])
                answer.append(ans_dict[ques_list[int(tot_list[i])]])

            return render_template('summary.html', question=question, answer=answer, ques_list=ques_list,no=no)
        else:
            no = int(req['no'])
            no += 1
            page = no
            ans = ans_dict[ques_list[int(tot_list[page])]]
            print(ans)
            tag = tag_ret(int(tot_list[page]), ans)
            return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                                   holihint=holihints[int(tot_list[int(page)])], no=int(page),
                                   ans=ans_dict[ques_list[int(tot_list[int(page)])]], num=int(tot_list[page]), tag=tag)
    else:
        return render_template("holistic.html", data=data)


@app.route('/seq_ques_list_back', methods=['POST', 'GET'])
def seq_ques_list_back():
    if (request.method == 'POST'):
        req = request.form
        page = req['page']
        print(f"no: {req['no']}")

        if (int(req['no']) == 0):
            page = 4
            return redirect(url_for('holi'))
        else:
            if (int(req['num']) == 3):
                ans_dict[page] = req.getlist('answer')
            elif (int(req['num']) == 6):
                ans_dict[page] = req.getlist('answer')
            else:
                ans_dict[page] = req['answer']
            req = request.form
            no = int(req['no'])
            no -= 1
            
            page = no
            ans = ans_dict[ques_list[int(tot_list[page])]]
            print(ans)
            tag = tag_ret(int(tot_list[page]), ans)
            return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                                   holihint=holihints[int(tot_list[int(page)])], no=int(page),
                                   ans=ans_dict[ques_list[int(tot_list[int(page)])]], num=int(tot_list[int(page)]),
                                   tag=tag, ques_list=ques_list)
    else:
        return redirect(url_for('holistic'))


@app.route('/seq_ques_back', methods=['POST', 'GET'])
def seq_ques_back():
    if (request.method == 'POST'):
        req = request.form
        page = req['page']
        ans_dict[page] = req['answer']
        req = request.form
        print(f"no: {req['no']}")
        print(tot_list)

        if (int(req['no']) == 0):
            return render_template('list_problems.html', data=data)
        else:
            no = int(req['no'])
            no -= 1
            page = no

            return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                                  hint=hints[int(tot[int(page)])], ans=ans_dict[ques[int(tot[int(page)])]], num=int(tot[page]))
    else:
        return redirect(url_for('holistic'))


@app.route('/save_ans_list', methods=['POST', 'GET'])
def save_ans_list():
    if (request.method == 'GET'):
        page = 0
        ans = ans_dict[ques_list[page]]
        tag = tag_ret(page, ans)
        return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[page], no=int(page),
                               ans=ans_dict[ques_list[int(tot_list[int(page)])]], tag=tag)
    else:
        req = request.form
        page = req['page']
        ans_dict[page] = req['answer']
        page = int(req['no'])

        anw = req['answer']

        ans[page] = anw

        print(page)
        print(ans[page])
        ans = ans_dict[ques_list[page]]
        tag = tag_ret(page, ans)
        return render_template("ques_page_2.html", data=data, ques=ques, page=ques_list[int(tot_list[int(page)])],
                               no=int(page), ans=ans_dict[ques_list[int(tot_list[int(page)])]], num=int(req['num']),
                               tag=tag)


@app.route('/back_from_holistic', methods=['POST', 'GET'])
def back_from_holistic():
    if (request.method == 'GET'):
        page = 4
        return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                               ans=ans_dict[ques_list[int(tot[int(page)])]], num=int(tot[page]))
    else:

        page = len(tot) - 1
        print(page)
        if (page < 0):
            return redirect(url_for('list_problems'))
        else:
            return render_template("ques_page.html", data=data, ques=ques, page=ques[int(tot[int(page)])], no=int(page),
                                   ans=ans_dict[ques[int(tot[int(page)])]], num=int(tot[page]))


@app.route('/summary', methods=['POST', 'GET'])
def summary():
    queries = {}
    if (request.method == 'GET'):
        return redirect(url_for('holistic'))
    else:
        return render_template('summary.html', data=data, ques=ques, ans_dict=ans_dict, ques_list=ques_list)


def ambigous(msg):
    return am.ambi(msg)

@app.route('/dash',methods=['GET'])
def dash():
    return render_template('page-d.html')
def get_data(questions, answers):
    global question
    global answer
    question = questions
    answer = answers


@app.route('/ambiguity', methods=['POST', 'GET'])
def ambiguity():
    """
    req = request.form

    print(len(que))
    print(an)
    i = int(req['i'])
    print(i)
    an[to_do_list[i]] = req['ans']

    """
    global question
    global answer
    global queries
    global to_do_list
    global new_q

    to_do_list = []
    req = request.form
    print(req.getlist('data'))
    # ch=[0]
    print("_________________")
    print(que)
    print("________________")
    print
    s = req.getlist('data')

    new_q = req['add_inp']
    no = int(req['no'])
    print(to_do_list)

    for i in s:
        to_do_list.append(int(i))
    if (new_q != "" and ("how to " in str(new_q).lower())):
        question.append(new_q)
        answer.append(new_q)
        to_do_list.append(len(question) - 1)
    if (len(to_do_list) == 0):
        question.append(new_q)
        answer.append(new_q)
        to_do_list.append(0)

    queries = {}
    req = request.form
    print("--------------------")
    print(question)
    print(answer)
    print(to_do_list)
    print("-------------------")

    qua = []
    awq = []

    for i in range(len(to_do_list)):
        qua.append(question[to_do_list[i]])
        awq.append(answer[to_do_list[i]])

    print("_--------____________---------------")
    print(question)
    print(answer)
    print(an)
    print("________---------------__________")
    for i in range(0, len(question)):
        a = ""

        if (type(answer[i]) == list):
            for j in answer[i]:
                a += f"{j} ,"
            answer[i] = a
        else:
            a = answer[i]
        print(a)

        if ("how to " in str(a).lower()):
            aws = a.split(" ")
            print(aws)
            to_id = 0
            for j in range(0, len(aws)):
                if (aws[j] == "how"):
                    to_id = j
            print(to_id)
            wes = ""
            for k in range(to_id + 2, len(aws)):
                wes += str(aws[k])
                wes += " "
            dse = wes.split(" ")

            qtns, anss = [f'How to {aws[to_id+1]} {wes}'.strip()], [
                f' What would happen if you were {aws[to_id+1]} {wes}']

        else:
            qtns, anss = ambigous(a)
        print(qtns)
        print(anss)
        if (len(qtns) == 0):
            qtns = [""]
            anss = [""]

        queries[question[i]] = [qtns, anss]
    # print(queries)
    question = qua

    print(queries)
    subbtn = ""
    return render_template('ambiguity.html', question=question, answer=answer, queries=queries, i=0, subbtn=subbtn,
                           to_do_list=to_do_list,no=no+1)


@app.route('/next_ambi', methods=['POST'])
def next_ambi():
    global question
    global answer
    req = request.form
    global queries
    # queries={'Initial Description of the Problem': [['How to be in top 5 in the global services sector  ?'], [' What would happen if you were in top 5 in the global services sector  ? ']], 'Having entered the initial description of the problem.': [[''], ['']], 'How does the problem look?': [[''], ['']], 'How does the problem sound?': [[''], ['']], 'How does the problem feel?': [['overwhelmed', 'great', 'when'], ['how specifically are you overwhelemed?', 'How can you say great?', "How often is 'when'?"]], 'How does the problem smell?': [['ordinary'], ['how ordinary?']], 'How does the problem taste? ': [['less', 'when'], ['less means how many?', "How often is 'when'?"]], 'Towards what purpose is this a problem?': [['How to be in top 5 globally in the services sector in our industry\r\n  ?'], [' What would happen if you were in top 5 globally in the services sector in our industry\r\n  ? '], ['we would dominate the Asian market and be a major player in Europe and the Americas. ']], 'For whom is this a problem?': [['all'], ['All means how many?']], 'Is this really a problem? Do you believe that the problem exists?  Is this problem coming from your teamâ€™s belief? ': [['this', 'that', 'all', 'must', 'that', 'all'], ['What do you mean by this? Can you be more specific?', '', 'All means how many?', 'What would happen if not done?', '', 'All means how many?']], 'Is this problem coming from your value system?': [[''], ['']], 'Is this problem coming because of a skills gap?': [['all', 'may'], ['All means how many?', 'may? or definitely need?']], 'Is the problem stemming out of a behavior issue?': [[''], ['']], 'Is the problem stemming from environment and cultural factors?': [[''], ['']]}
    # question=['Towards what purpose is this a problem?']
    # answer=['How to be in top 5 in the global services sector  ?', '', 'well we are in the top 1000 now. i see a very long way up to the top 5\r\n', 'lot of commotion and the sound of a race gun, steps running towards the goal point\r\n', 'How to feel overwhelmed. when i see myself in top 5 i feel great\r\n  ?', 'smell ordinary without any fragrance as one in top 1000 is not a big deal in our industry\r\n', 'taste saltless and sugarless. when we go in top 5 i can taste both sugar and salt\r\n', 'How to be in top 5 globally in the services sector in our industry\r\n  ?', 'for me and all my team members\r\n', 'yes all of us believe that this problem of not in top 5 exists. all of us believe that we must be in top 5 except of course our competitors\r\n', '', 'not really and may be\r\n', 'How to reach the top\r\n  ?', '']

    i = req['i']
    i = int(i)
    # global to_do_list
    # to_do_list=[7]
    print(f'todolist {to_do_list}')
    print(i)
    print(f"str: {answer[to_do_list[i]]}")
    queries[question[i]].append(req.getlist(f'ans{i}'))
    answer[to_do_list[i]] = answer[to_do_list[i]][:-2] + (' so ' + str(req.getlist(f'ans{i}')[0])) + '?'
   
    print(queries)

    print(answer)
    global new_q

    if (i == len(question) - 1):
        print("--------------------------------")
        print(queries)
        print(i)
        print(question)
        print(answer)

        import re
        
        print(answer)
        for ans in range(0, len(answer)):
            #    print(len(answer[ans]))
            if (len(answer[ans]) <= 2):
                answer[ans] = "NaN"
        print(question)
        print(answer)

        global new_ques
        global new_ans
        new_ques = {}
        new_ans = {}

        for i in range(len(question)):
            qtns = []
            anss = []
            print(queries[question[i]][2])
            # print(new_ques[question[i]][j][0][0])
            new_ques[question[i]] = []
            a = answer[i]
            #for j in range(len(queries[question[i]][2])):
            #    a += f"{queries[question[i]][0][j]} so {queries[question[i]][2][j]} "
            qtns, anss = ambigous(a)

            print(qtns, anss)
            if (len(qtns) == 0):
                qtns = [""]
                anss = [""]

            new_ques[question[i]] = [qtns, anss]
            # print(new_ques)

        subbtn = ""
        # new_ques[question[i]][j][0][0]
        no = int(req['no'])+1
        return render_template('ambi_repeat.html', question=question, answer=answer, queries=new_ques, i=0,
                               subbtn=subbtn, to_do_list=to_do_list,no=no)
        # return render_template('after_changes_summary.html',question=question,answer=answer,queries=queries,to_do_list=to_do_list)

        # subbtn = f"<button type='submit' formaction='/submitting' formmethod='POST'>  submit </button>"
    else:
        subbtn = ""
        i += 1
        no = int(req['no'])+1
        return render_template('ambiguity.html', qq=qq, question=question, answer=answer, queries=queries, i=i,
                               subbtn=subbtn, to_do_list=to_do_list,no=no)

@app.route('/next_ambi_db', methods=['POST','GET'])
def next_ambi_db():

    session['page_no'] += 1
    req = request.form
    session['user']['problems'][session['id']]['what_would']['ans'] = str(req.getlist(f'ans')[0])
    session['user']['problems'][session['id']]['before_ambi'] = session['user']['problems'][session['id']]['how_to_st'][:-2].strip() + (' so ' + session['user']['problems'][session['id']]['what_would']['ans']) + '?'
    print("ambiiii-----"+str(session['user']['problems'][session['id']]['before_ambi']))
    qtns, anss = ambigous(session['user']['problems'][session['id']]['before_ambi'])
    print(qtns,anss)
    session['user']['problems'][session['id']]['selected_how_to']['question'] = session['user']['problems'][session['id']]['before_ambi']
    a = []
    for i in range(0, len(qtns)):
        aa = {
            'vague':qtns[i],
            'ques':anss[i],
            'ans':""
        }
        a.append(aa)    
    session['user']['problems'][session['id']]['selected_how_to']['ambiguity'] = a
    d = update_db()

    return render_template('ambi_repeat.html')

@app.route('/next_ambi_2_db', methods=['POST'])
def next_ambi_2_db():
    session['page_no'] += 1
    req = request.form
    for i in range(len(session['user']['problems'][session['id']]['selected_how_to']['ambiguity'])):
        session['user']['problems'][session['id']]['selected_how_to']['ambiguity'][i]['ans'] = req.getlist(f'ans{i}')[0]
        print(session['user']['problems'][session['id']]['selected_how_to']['ambiguity'][i]['ans'])

    if 'style=' not in str(session['user']['problems'][session['id']]['selected_how_to']['question']):
        print(session['user']['problems'][session['id']]['selected_how_to']['ambiguity'])
        for i in range(len(session['user']['problems'][session['id']]['selected_how_to']['ambiguity'])):

           session['user']['problems'][session['id']]['selected_how_to']['question'] = str(session['user']['problems'][session['id']]['selected_how_to']['question']).replace(

               session['user']['problems'][session['id']]['selected_how_to']['ambiguity'][i]['vague'].strip(),
               f"<i style='color:blue;'>{session['user']['problems'][session['id']]['selected_how_to']['ambiguity'][i]['vague']}</i> ({session['user']['problems'][session['id']]['selected_how_to']['ambiguity'][i]['ans']})"
           )


    print(session['user']['problems'][session['id']]['selected_how_to']['question'])


    splitting_style_from_question = session['user']['problems'][session['id']]['selected_how_to']['question'].split("<i style='color:blue;'> ")
    splitted_style = ''

    for x in splitting_style_from_question:
        splitted_style += x
    print('splitting style --------')
    print(splitted_style)

    splitting_i_from_question = splitted_style.split('</i>')

    final_quest = ''

    for y in splitting_i_from_question:
        final_quest += y
    print('check final splitting -------')
    print(final_quest)



    print('check final_qeustion')
    session['user']['problems'][session['id']]['final_question'] = final_quest
    print(session['user']['problems'][session['id']]['final_question'])



    d=update_db()
    return render_template('after_changes_summary.html')

@app.route('/next_ambi_2', methods=['POST'])
def next_ambi_2():
    req = request.form
    i = req['i']
    i = int(i)
    print(i)
    print(to_do_list)
    new_ques[question[i]].append(req.getlist(f'ans{i}'))
    print(new_ques)
    if (i == len(question) - 1):
        print("--------------------------------")
        print(new_ques)

        import re
        for i in range(0, len(question)):
            x = len(new_ques[question[i]]) - 1
            print(new_ques[question[i]][2])
            wwws = answer[to_do_list[i]]
            print(wwws)
            for j in range(0, len(new_ques[question[i]][2])):
                if (len(new_ques[question[i]][0][j]) > 2):
                    if (new_ques[question[i]][0][j] == "more"):
                        answer[to_do_list[i]] = answer[to_do_list[i]].replace(new_ques[question[i]][0][j],
                                                                              f"({new_ques[question[i]][2][j]}) <i style='color:blue;'>{new_ques[question[i]][0][j]}</i> ")
                    else:
                        answer[to_do_list[i]] = answer[to_do_list[i]].replace(new_ques[question[i]][0][j],
                                                                              f"<i style='color:blue;'>{new_ques[question[i]][0][j]}</i> ({new_ques[question[i]][2][j]})")
                        # pass
        print(answer)
        for ans in range(0, len(answer)):
            #    print(len(answer[ans]))
            if (len(answer[ans]) <= 2):
                answer[ans] = "NaN"
        print(question)
        print(answer)

        for i in range(0, len(question)):
            a = ""

            if (type(answer[i]) == list):
                for j in answer[i]:
                    a += f"{j} ,"
                answer[i] = a
            else:
                a = answer[i]
            print(a)
            qtns, anss = ambigous(a)
            print(qtns)
            print(anss)
            if (len(qtns) == 0):
                qtns = [""]
                anss = [""]

            queries[question[i]] = [qtns, anss]

        for i in range(0, len(question)):
            for j in range(0, len(queries[question[i]][0])):
                if (len(queries[question[i]][0][j]) > 2):
                    answer[i] = answer[i].replace(queries[question[i]][0][j],
                                                  f"<i style='color:blue;'>{queries[question[i]][0][j]}</i>")

        subbtn = ""
        no = int(req['no'])+1
        return render_template('after_changes_summary.html', question=question, answer=answer, queries=queries,
                               to_do_list=to_do_list,no=no)

        # subbtn = f"<button type='submit' formaction='/submitting' formmethod='POST'>  submit </button>"
    else:
        subbtn = ""
        i += 1
        no = int(req['no'])+1
        return render_template('ambi_repeat.html', question=question, answer=answer, queries=new_ques, i=i,
                               subbtn=subbtn, to_do_list=to_do_list,no=no)


@app.route('/submitting', methods=['POST'])
def submitting(queries, question, answer):
    # req = request.form

    """
    for i in range(0,len(question)):
        print(req.getlist(f'ans{i}'))
        queries[question[i]].append(req.getlist(f'ans{i}'))
    """
    print("--------------------------------")
    print(queries)
    print(to_do_list)

    for i in range(0, len(question)):
        for j in range(0, len(queries[question[i]][2])):
            if (len(queries[question[i]][0][j]) > 2):
                answer[i] = answer[i].replace(queries[question[i]][0][j],
                                              f"<i style='color:blue;'>{queries[question[i]][0][j]}</i> ({queries[question[i]][2][j]})")

    print(answer)

    return render_template('after_changes_summary.html', question=question, answer=answer, queries=queries,
                           to_do_list=to_do_list)


def ambi_solver(question,answer):
    if (type(answer ) != list):
                answer = answer.lower()
                
    if ("to be " in str(answer ).lower()):
        print("ONE")
         ############## New Changes ##############
        print('dseee------')
        ans_replace = answer.replace('.', '')
        ########## NEw CHanges ############
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
            wess = f"How to be {aws[to_id+1]} {wes} ?"
            if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
                session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        
    elif (" to " in str(answer ).lower()):
        print("TEO")
        ############## New Changes ##############
        print('dseee------')
        ans_replace = answer.replace('.', '')
        aws = ans_replace.split(" ")
        print(aws)
        ############## New Changes ##############
        
        to_id = 0
        for j in range(0, len(aws)):
            if (aws[j] == "to"):
                to_id = j
                break
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
            wess = f"How to {aws[to_id+1]} {wes} ?"
            if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
                session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
          
        else:
            pass
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
            if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
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
            if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
                session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        else:
            pass
    """
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
                to_id = jx
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
        if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
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
        if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
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
        if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
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
        if wess not in session['user']['problems'][session['id']]['how_to_stmts']:
            session['user']['problems'][session['id']]['how_to_stmts'].append(wess)
        # to_do_list.append(i)  
    """    
    

@app.route('/to_word_ambi_db', methods=['POST','GET'])
def to_word_ambi_db():

    if request.method == 'GET':
            session['page_no'] -= 1   
            return render_template('select_to.html')  
    session['page_no'] += 1
    req = request.form
    length =len(session['questions'])
    how_to = session['user']['problems'][session['id']]['how_to_stmts']

    
    print(len(how_to))
    #print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

    if len(session['user']['problems'][session['id']]['how_to_stmts']) == 0:
        session['user']['problems'][session['id']]['how_to_stmts'] = []
    session['user']['problems'][session['id']]['how_to_stmts'] = []    
    for i in range(0, length):
            ambi_solver(session['user']['problems'][session['id']][session['questions'][i] ]['ques'],session['user']['problems'][session['id']][session['questions'][i] ]['ans'])
    
    ambi_solver('abc',session['user']['problems'][session['id']]['initial_prob_st'])
    ambi_solver('abc',session['user']['problems'][session['id']]['initial_desc'])
    d = update_db() 
    return render_template('select_to.html')   

@app.route('/ambiguity_db',methods=['POST','GET'])
def ambiguity_db():
    req = request.form
    
    if request.method == 'GET':
        session['page_no'] -= 1   
        return render_template('ambi_what_would.html')
    session['page_no'] += 1
    print(req['add_inp'])
    how_to = req.getlist('data')
    print(how_to)

    if len(req['add_inp']) > 0:
        how_to = req['add_inp']
        session['user']['problems'][session['id']]['how_to_stmts'].append(req['add_inp'])
        session['user']['problems'][session['id']]['how_to_st'] = how_to
    else:
        session['user']['problems'][session['id']]['how_to_st'] = how_to[0]
    
    
    d = update_db()

    aws = session['user']['problems'][session['id']]['how_to_st'].split(" ")
    print(aws)
    to_id = 0
    for j in range(0, len(aws)):
        if (aws[j] == "how"):
            to_id = j
    print(to_id)
    wes = ""
    for k in range(to_id + 2, len(aws)):
        wes += str(aws[k])
        wes += " "
    dse = wes.split(" ")

    wess = f' What would happen if you were {aws[to_id+1]} {wes}'
    session['user']['problems'][session['id']]['what_would']['ques'] = str(wess)
    d = update_db()

    return render_template('ambi_what_would.html')

@app.route('/to_word_ambi', methods=['POST'])
def to_word_ambi():
    print("---------sdf sdf sdf sdfsdf sdfs dfsdf------------------------")
    req = request.form
    length = int(req['length'])
    global question
    global answer
    answer = []

    for i in range(0, length):
        answer.append(req[question[i]])
    print(answer)

    # print(len(question))
    global que
    global an
    global to_do_list
    to_do_list = []
    que = []
    an = []

    for i in range(0, len(question)):
        print(answer[i])
        if (type(answer[i]) != list):
            answer[i] = answer[i].lower()

        if ("to be " in str(answer[i]).lower()):
            print("ONE")
            aws = answer[i].split(" ")
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
                que.append(question[i])
                print(len(dse))
                print(f"WES::: {dse}")
                an.append(f"How to be {aws[to_id+1]} {wes} ?")
                # answer[i] = f"{answer[i]}"
                answer[i] = f"How to be {aws[to_id+1]} {wes} ?"
                to_do_list.append(i)

        elif (" to " in answer[i]):
            print("TEO")
            aws = answer[i].split(" ")
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
                que.append(question[i])
                print(len(dse))
                print(f"WES::: {dse}")
                an.append(f"How to {aws[to_id+1]} {wes} ?")
                # answer[i] = f"{answer[i]}"
                answer[i] = f"How to {aws[to_id+1]} {wes} ?"
                to_do_list.append(i)
            else:
                que.append(question[i])
                an.append(answer[i])

        
        #for testing the organization
        elif ("is the problem stemming from environment and cultural factors?" in str(question[i]).lower()):
            if len(answer[i])>3:
                wess = "How to change "
                change = str(answer[i]).strip('[')
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
                que.append(question[i])
                an.append(wess)
                to_do_list.append(i)
                answer[i]=wess
            else:
                print("NONE")
                aws = str(answer[i]).split(" ")
                print(aws)
                que.append(question[i])
                an.append(answer[i])
                

        elif("is this problem coming from your value system?" in str(question[i]).lower()):
            if len(answer[i])>3:
                wess = "How to change "
                change = str(answer[i]).strip('[')
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
                que.append(question[i])
                an.append(wess)
                to_do_list.append(i)
                answer[i]=wess
            else:
                print("NONE")
                aws = str(answer[i]).split(" ")
                print(aws)
                que.append(question[i])
                an.append(answer[i])
            


        else:
            print("NONE")
            aws = str(answer[i]).split(" ")
            print(aws)
            que.append(question[i])
            an.append(answer[i])
        
        """
        elif ("because of" in str(answer[i]).lower()):
            print("THREE")
            print("-----------------")
            answer[i] = answer[i].replace(".", "")
            answer[i] = answer[i].replace("\n", "")
            answer[i] = answer[i].replace("\r", "")
            aws = answer[i].split(" ")
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
            answer[i] = wess
            que.append(question[i])
            an.append(answer[i])
            # to_do_list.append(i)

        elif (" as " in str(answer[i]).lower()):
            print("THREE")
            print("-----------------")
            answer[i] = answer[i].replace(".", "")
            answer[i] = answer[i].replace("\n", "")
            answer[i] = answer[i].replace("\r", "")
            aws = answer[i].split(" ")
            to_id = 0
            print(aws)
            for j in range(0, len(aws)):
                if (aws[j] == 'because'):
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
            answer[i] = wess
            que.append(question[i])
            an.append(answer[i])
            # to_do_list.append(i)

        elif (" since " in str(answer[i]).lower()):
            print("THREE")
            print("-----------------")
            answer[i] = answer[i].replace(".", "")
            answer[i] = answer[i].replace("\n", "")
            answer[i] = answer[i].replace("\r", "")
            aws = answer[i].split(" ")
            to_id = 0
            print(aws)
            for j in range(0, len(aws)):
                if (aws[j] == 'because'):
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
            answer[i] = wess
            que.append(question[i])
            an.append(answer[i])
            # to_do_list.append(i)

        elif ("because" in str(answer[i]).lower()):
            print("THREE")
            print("-----------------")
            answer[i] = answer[i].replace(".", "")
            answer[i] = answer[i].replace("\n", "")
            answer[i] = answer[i].replace("\r", "")
            aws = answer[i].split(" ")
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
            answer[i] = wess
            que.append(question[i])
            an.append(answer[i])
            # to_do_list.append(i)
        """

        print("HEEE") 
    print(len(que))
    print(an)
    print(to_do_list)
    no = int(req['no'])
    # ch = []
    # for i in range(len(to_do_list)):
    #    ch.append(f"""<input type="checkbox" name="{i}" id="" value="{i}" >""")
    return render_template('select_to.html', an=an, que=que, to_do_list=to_do_list,no=no+1)


@app.route('/select_how', methods=['POST'])
def select_how():
    req = request.form
    print(req.getlist('data'))
    # ch=[0]
    print("_________________")
    print(que)
    print("________________")
    s = req.getlist('data')
    global to_do_list
    to_do_list = []
    for i in s:
        to_do_list.append(int(i))

    if (len(to_do_list) == 1):
        question = que
        answer = an
        get_data(que, an)
        an[to_do_list[0]] = ""
        return render_template('to_word_ambi.html', an=an, que=que, ds="""style='display:none' """, i=0,
                               subbtn="""<button class="btn btn-sm btn-primary" type="submit" formaction="/ambiguity" formmethod="POST">  Check Ambiguity </button>""",
                               to_do_list=to_do_list)
    else:
        an[to_do_list[0]] = ""
        return render_template('to_word_ambi.html', an=an, que=que, i=0, to_do_list=to_do_list)


@app.route('/next_am', methods=['POST'])
def next_am():
    req = request.form
    print(to_do_list)
    # print(len(que))
    print(an)
    i = int(req['i'])
    print(i)
    an[to_do_list[i]] = req['ans']

    print(an)

    if (i >= len(to_do_list) - 2):
        question = que
        answer = an
        get_data(que, an)
        i += 1
        an[to_do_list[i]] = ""
        return render_template('to_word_ambi.html', an=an, que=que, ds="""style='display:none' """, i=i,
                               subbtn="""<button class="btn btn-sm btn-primary" type="submit" formaction="/ambiguity" formmethod="POST">  Check Ambiguity </button>""",
                               to_do_list=to_do_list)
    i += 1
    an[to_do_list[i]] = ""

    return render_template('to_word_ambi.html', an=an, que=que, i=i, to_do_list=to_do_list)


@app.route('/finish', methods=['POST'])
def finish():
    req = request.form
    no = int(req['no'])+1
    return render_template('final.html',no=no)


@app.route('/return_s', methods=['POST','GET'])
def return_s():
    global tot
    tot = []
    global ans_dict
    ans_dict = {}
    global question
    global queries
    queries = {}
    global answer
    question = []
    answer = []

    data = ['', '', '', '', ques, '', '', '']
    global tot_ques
    tot_ques = set()
    global tot_ques_list
    tot_ques_list = set()
    global ans
    ans = ['', '', '', '', '']
    data[4] = ques
    ans_dict[ques_list[0]] = ''
    ans_dict[ques_list[1]] = ''
    ans_dict[ques_list[2]] = ''
    ans_dict[ques_list[3]] = ''
    ans_dict[ques_list[4]] = ''
    ans_dict[ques_list[5]] = ''
    ans_dict[ques_list[6]] = ''

    ans_dict[ques[0]] = ''
    ans_dict[ques[1]] = ''
    ans_dict[ques[2]] = ''
    ans_dict[ques[3]] = ''
    ans_dict[ques[4]] = ''
    queries = {}
    answer = []
    tot = []
    tot_list = []
    global new_ques
    new_ques = {}

    question = []
    d=update_db()
    if('user' in session):
        print(f"session : { session['user']} ")
    session.pop('user')    
    return render_template("index.html", data=data)


class hello(Resource):
    def post(self, usname):
        return f"Hello! {usname}, Welcome to our unit"
api.add_resource(hello, '/hello/<string:usname>')


if __name__ == "__main__":
    import os

    global tot_list
    tot_list = []

    port = int(os.environ.get('PORT', 8000))
    #serve(app, host='0.0.0.0', port=port)
    app.run(port=port,debug=True)

