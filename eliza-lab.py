# I am ([A-Z](.*)) - captures name
# (I am|I\'m|My name is|I'm called) ([A-Z](.*)) - works for name capture
# (I am|I\'m)([a-z[:blank:]].*)* ([a-z].*) - generalizes for adjectives
# (I'm|I am)( an| not| a|[[:blank:]])*([a-z]*)( at|[[:blank:]])?([[:blank:]][A-Za-z]*|[A-Za-z]*)? - extracts person characteristics
# ([mM]om|[mM]other|[dD]ad|[fF]ather) - extracts parental features
# I( don't)?( want) to ([A-Za-z](.*)+) ([A-Za-z].*). - want modal verb
# I (must) ([A-Za-z](.*)+) ([A-Za-z].*). - must modal verb
# I (can't|can) ([A-Za-z](.*)+) ([A-Za-z].*). - can modal verb
# (think|hope) - thoughts and aspirations

"""
Want Test Cases:
I want to go skiing.
I don't want to start programming.
I don't want to learn to ski.
I don't want to learn how to program.
I want to go ski.
"""


# Spanish Equivalents:
# Soy ([A-Z](.*)) - captures name
# (Mi nombre es|Me llamo) ([A-Z](.*)) - works for name capture
# ((Yo |No |Yo no )?[Ee]stoy)([a-z[:blank:]].*)* ([a-z].*) - generalize for adjectives
# (Yo soy |Soy |Yo no soy)(una|not|a|[[:blank:]])*([a-z]*)( de |[[:blank:]])?([[:blank:]][A-Za-z]*|[A-Za-z]*)? - extracts person characteristics
# ([mM]ama|[mM]adre|[pP]apa)  - parental features
# (No |Yo )?([Qq]uiero )([A-Za-z](.*)+) ([A-Za-z].*). - want modal verb.
# (Debo) ([A-Za-z](.*)+) (al|de) ([A-Za-z].*). - must modal verb.
# (Yo )?([Pp]uedo) ([A-Za-z](.*)+) ([A-Za-z].*). - can modal verb
# ([Pp]ienso|[Ee]spero) - thoughts and aspirations
# ([Ss]iempre) - specific examples

import re
import random

# color codes from: https://godoc.org/github.com/whitedevops/colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = "\033[97m"


greeting = 'I am ([A-Z](.*))'
nameCapture = '(My name is|I\'m called) ([A-Z](.*)+)'
adjectives = '(I am|I\'m)([a-z ].*)* ([a-z].*)'
personCharacteristics = '(I\'m |I am )(an |not an |a | )*([a-z]*)( at| )?( [A-Za-z]*|[A-Za-z]*)?'
parents = '([mM]om|[mM]other|[dD]ad|[fF]ather)'
wantModal = 'I( don\'t)?( want) to ([A-Za-z ]*)([A-Za-z ]*)?'
mustModal = 'I (must) ([A-Za-z ]*) ([A-Za-z]*)'
canModal = 'I (can\'t|can) ([A-Za-z]*)([A-Za-z ]*)'

# general cases
thoughts = '(think|hope)'
examples = '(always)'
insults = '(stupid|idiot|loser|sucker)'

border = bcolors.OKBLUE + bcolors.BOLD + " | "

print(border + bcolors.OKGREEN + "***** ELIZA Chat-Bot - by John McCambridge *****" + border) 

border = bcolors.OKBLUE + bcolors.BOLD + " | "

while True:
    text = str(input(border + bcolors.BOLD + bcolors.WHITE + ': '))

    if text:
        output = "Please tell me more..."

        groupHello = re.search(greeting, text, re.IGNORECASE)
        groupNameCapture = re.search(nameCapture, text, re.IGNORECASE)
        adjectiveCapture = re.search(adjectives, text, re.IGNORECASE)
        parentsCapture = re.search(parents, text, re.IGNORECASE)
        wantCapture = re.search(wantModal, text, re.IGNORECASE)
        mustCapture = re.search(mustModal, text, re.IGNORECASE)
        canCapture = re.search(canModal, text, re.IGNORECASE)
        
        thoughtsCapture = re.search(thoughts, text, re.IGNORECASE)
        examplesCapture = re.search(examples, text, re.IGNORECASE)
        insultsCapture = re.search(insults, text,re.IGNORECASE)

        if groupNameCapture:
            output = "Hello, " + str(groupNameCapture.group(2)) + "!"
        elif adjectiveCapture:
            article = "" if adjectiveCapture.group(2) == None else str(adjectiveCapture.group(2))
            possessive = "are"

            if "not" in article:
                possessive = "aren't"
                article = " " + article.replace("not", "").strip()

            output = "Why " + possessive + " you"+ article + " " + str(adjectiveCapture.group(3)).strip() + "?"
        elif parentsCapture:
            output = "Tell me more about your " + str(parentsCapture.group(1)) + "."
        elif wantCapture:
            # broken - I don't want to ski.
            conditional = "do" if wantCapture.group(1) == None else "don't"
            modifier = " " + str(wantCapture.group(4))
            output = "Why " + conditional + " you want to " + str(wantCapture.group(3)) + (modifier if modifier != " " else "") + "?"
        elif mustCapture:
            output = "Why must you " + str(mustCapture.group(2)) + " " + str(mustCapture.group(3)) + "?"
        elif canCapture:
            endingVerb = "" if str(canCapture.group(3)) == "" else str(canCapture.group(3))
            output = "Why " + str(canCapture.group(1)) + " you " + str(canCapture.group(2)).strip() + endingVerb + "?"
        elif thoughtsCapture:
            output = "Why do you think that?" if str(thoughtsCapture.group(1)) == "think" else "Why do you suppose that?"
        elif examplesCapture:
            output = "Can you give me a specific example?"
        elif insultsCapture:
            choices = ["Hey, no insults!", "Please be a little kinder!", "You will need to calm down a little."]
            output = choices[random.randint(0, len(choices) - 1)]
        else:
            output = "Tell me more."

        output = border + "\t" + bcolors.OKGREEN + output

        print(output)