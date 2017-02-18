import random

print('+++++++++++++++++++++')
print('Christopher Strachey, "Loveletters" - 1952')
print('an homage')
print('+++++++++++++++++++++\n')

sal1List = ['beloved', 'darling', 'dear', 'dearest', 'fanciful']
sal2List = ['chickpea', 'dear', 'duck', 'jewel', 'love', 'moppet', 'sweetheart']
adjList = ['affectionate', 'amorous', 'anxious', 'avid', 'beautiful', 'breathless', 'burning',
           'covetous', 'craving', 'curious', 'eager', 'fervent', 'fondest', 'loveable',
           'lovesick', 'passionate', 'precious', 'seductive', 'sweet', 'sympathetic', 'tender',
           'unsatisfied', 'winning', 'wistful']
nounList = ['adoration', 'affection', 'ambition', 'appetite', 'ardour', 'being', 'burning', 'charm',
            'craving', 'desire', 'devotion', 'eagerness', 'enchantment', 'enthusiasm', 'fancy',
            'fellow feeling', 'fervour', 'fondness', 'heart', 'hunger', 'infatuation',
            'little liking', 'longing', 'love', 'lust', 'passion', 'rapture', 'sympathy', 'thirst',
            'wish', 'yearning']
advList = ['affectionately', 'ardently', 'anxiously', 'beautifully', 'burningly', 'covetously', 'curiously',
           'eagerly', 'fervently', 'fondly', 'impatiently', 'keenly', 'lovingly', 'passionately', 'seductively',
           'tenderly', 'wistfully']
verbList = ['adores', 'attracts', 'clings to', 'holds dear', 'hopes for', 'hungers for', 'likes', 'longs for',
            'loves', 'lusts after', 'pants for', 'pines for', 'sighs for', 'tempts', 'thirsts for', 'treasures',
            'yearns for', 'woos']

# template for letter: "sal1 sal2, My adj noun adv verb your adj noun. My noun verb
# your noun. You are my adj noun, my adj noun, my adj adj noun. Yours adv, M.U.C."

# method that generates random words for each slot and prints the letter
def printletter():
    # line = raw_input['prompt']

    sal1 = random.choice(sal1List)
    sal2 = random.choice(sal2List)
    adj1 = random.choice(adjList)
    noun1 = random.choice(nounList)
    adv1 = random.choice(advList)
    verb1 = random.choice(verbList)
    adj2 = random.choice(adjList)
    noun2 = random.choice(nounList)
    noun3 = random.choice(nounList)
    verb2 = random.choice(verbList)
    noun4 = random.choice(nounList)
    adj3 = random.choice(adjList)
    noun5 = random.choice(nounList)
    adj4 = random.choice(adjList)
    noun6 = random.choice(nounList)
    adj5 = random.choice(adjList)
    adj6 = random.choice(adjList)
    noun7 = random.choice(nounList)
    adv2 = random.choice(advList)
    # etc

    print(sal1 + " " + sal2 + ", \n\tmy " + adj1 + " " + noun1 + " " + adv1 + " " + verb1 + " your " + adj2 +
          " " + noun2 + ". \nmy " + noun3 + " " + verb2 + " your " + noun4 + ". you are my " + adj3 + " " + noun5 +
          ", \nmy " + adj4 + " " + noun6 + ", my " + adj5 + " " + adj6 + " " + noun7 + ". \n\tyours " + adv2 +
          ", \n\t\tM.U.C.")
    # maybe add a '----------------------------------------------------------------------'

# begin. print "generate a love letter"
line = raw_input("press enter to generate a love letter\n")
while line == '':  
    # run method
    printletter()
    # print "generate another"
    line = raw_input("\npress enter to generate another letter\nhad enough love? hit 'q' to stop\n")
print("goodbye")
