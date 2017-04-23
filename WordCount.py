
boundedRationality = {"natural disasters": 0,	"throughout history": 0, "xenophobia": 0, "moral obligation": 0}

count = 0
with open("/home/nikita/Projects/DM/speech", 'r') as speech:
    for line in speech:
        lineSplit = line.split(" ")
        for i in range(0, len(lineSplit)):
            word = lineSplit[i]
            for key, value in boundedRationality.items():
                phrase = word
                for j in range(1, len(key.split(" "))):
                    if j + i < len(lineSplit):
                        phrase += " " + lineSplit[j + i]
                if phrase.lower() == key.lower():
                    boundedRationality[key] += 1

print(boundedRationality)