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

# Spanish Equivalents:
# Soy ([A-Z](.*)) - captures name
# (Mi nombre es|Me llamo) ([A-Z](.*)) - works for name capture
# (Yo |No |Yo no )?([Ee]stoy)([a-z ].*)* ([a-z].*)? - generalize for adjectives
# (Yo soy |Soy |Yo no soy)(una|not|a|[[:blank:]])*([a-z]*)( de |[[:blank:]])?([[:blank:]][A-Za-z]*|[A-Za-z]*)? - extracts person characteristics
# ([mM]ama|[mM]adre|[pP]apa)  - parental features
# (No |Yo )?([Qq]uiero )([A-Za-z](.*)+) ([A-Za-z].*). - want modal verb.
# (Debo) ([A-Za-z](.*)+) (al|de) ([A-Za-z].*). - must modal verb.
# (Yo )?([Pp]uedo) ([A-Za-z](.*)+) ([A-Za-z].*). - can modal verb
# ([Pp]ienso|[Ee]spero) - thoughts and aspirations
# ([Ss]iempre) - specific examples


greeting = 'Soy ([A-Z](.*))'
nameCapture = '(Mi nombre es|Me llamo) ([A-Z](.*)+)'
adjectives = '(Yo |No |Yo no )?([Ee]stoy)([a-z ]*) ([a-z]*)?'
personal = '(Soy|Yo soy|(Yo )?[nN]o soy) (una |de | )*([A-Za-z ]*)'

parents = '([mM]ama|[mM]adre|[pP]apa)'
wantModal = '(No |Yo )?([Qq]uiero )([A-Za-z]+)([A-Za-z ]+)*'
mustModal = '(Debo) ([A-Za-z]+) ((al|de|a|el) ([A-Za-z]*))'
canModal = '(Yo |Yo no |No )?([Pp]uedo) ([A-Za-z ]*) (([A-Za-z ]*)*)'

# general cases
thoughts = '([Pp]ienso|[Ee]spero)'
examples = '(siempre)'
insults = '(estupida|idiota)'

# example conversation
conversation = [
    'Me llamo Rolando',
    'Estoy un poco triste',
    'Porque mi mama quiere que yo me vaya de la casa.',
    'Ella dice que debo ordenar el cuarto',
    'Es que yo soy bastante desordenado.',
    'Porque no me gusta. No quiero ordenar.',
    'Porque no me da la gana',
    'No, estupida',
    'Bueno. No se. Me cuesta mucho. No puedo ser ordenado.',
    'Porque cuando era nino siempre me gustaba jugar en la naturaleza, donde todo es libre.',
    'Pienso que todo empezo cuando fui a la playa por primera vez.'
]

border = bcolors.OKBLUE + bcolors.BOLD + " | "

print(border + bcolors.OKGREEN + "***** ELIZA Chat-Bot (español edition) - by John McCambridge *****" + border) 

border = bcolors.OKBLUE + bcolors.BOLD + " | "

#while True:
for text in conversation:
    # text = str(input(border + bcolors.BOLD + bcolors.WHITE + ': '))
    output = ""

    if text:
        groupNameCapture = re.search(nameCapture, text, re.IGNORECASE)
        adjectiveCapture = re.search(adjectives, text, re.IGNORECASE)
        parentsCapture = re.search(parents, text, re.IGNORECASE)
        wantCapture = re.search(wantModal, text, re.IGNORECASE)
        mustCapture = re.search(mustModal, text, re.IGNORECASE)
        canCapture = re.search(canModal, text, re.IGNORECASE)
        personalCapture = re.search(personal, text, re.IGNORECASE)
        
        thoughtsCapture = re.search(thoughts, text, re.IGNORECASE)
        examplesCapture = re.search(examples, text, re.IGNORECASE)
        insultsCapture = re.search(insults, text,re.IGNORECASE)

        if groupNameCapture:
            output = "Hola, " + str(groupNameCapture.group(2)) + " - ¿Cómo estás?"

        elif parentsCapture:
            output = "Cuéntame más de tu " + str(parentsCapture.group(1)) + "."

        elif insultsCapture:
            choices = ["¡Hey, sin insultos! ", "Cálmate y cuéntame más."]
            output = choices[random.randint(0, len(choices) - 1)]

        elif adjectiveCapture:
            article = "" if adjectiveCapture.group(1) == None else str(adjectiveCapture.group(1))
            possessive = " no"

            if "no" not in article.lower():
                possessive = "" 

            output = "¿Porqué" + possessive + " estás " + str(adjectiveCapture.group(4)).strip() + "?"

        elif personalCapture:
            article = "" if personalCapture.group(3) == None else str(personalCapture.group(3))
            item = str(personalCapture.group(4))

            conditional = "" if "no" not in str(personalCapture.group(1)) else " no"
            output = "¿Porqué" + conditional + " eres " + article + item + "?"

        elif wantCapture:
            conditional = ""

            if wantCapture.group(1) != None:
                if wantCapture.group(1).lower().strip() == "no":
                    conditional = " no"

            modifier = str(wantCapture.group(4)) if str(wantCapture.group(4)) != "None" else "" 
            action = str(wantCapture.group(3)).replace("me", "te") if str(wantCapture.group(3)) != "None" else " "

            output = "¿Porqué" + conditional + " quieres " + action + modifier + "?"

        elif mustCapture:
            modifier = str(mustCapture.group(2)).replace("me", "te")
            output = "¿Porqué debes " + modifier + " " + str(mustCapture.group(3)) + "?"

        elif canCapture:
            conditional = "no" if "no" in canCapture.group(1).lower() else ""
            endingVerb = "" if str(canCapture.group(3)) == "" else str(canCapture.group(3))
            output = "¿Porqué " + conditional + " puedes " + str(canCapture.group(3)) + " " + str(canCapture.group(4)).strip() + "?"

        elif thoughtsCapture:
            output = "¿Porqué piensas eso?" if str(thoughtsCapture.group(1)).lower() == "pienso" else "¿Porqué esperas eso?"

        elif examplesCapture:
            output = "¿Puedes darme un ejemplo específico?"
            
        else:
            output = "Cuéntame más."

        output = border + "\t" + bcolors.OKGREEN + output

        print(output)