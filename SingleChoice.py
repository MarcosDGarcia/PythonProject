# Project MultipleChoice is a questionnaire
import time
import random

questions = {1: 'Which is the coolder place in Earth?\na) Antartic\nb) Buenos Aires\nc) Toronto\nd) Russia',
             2: 'Who had write La Odisea?\na) Prometeo\nb) Homero\nc) Aristoteles\nd) Perón',
             3: 'What is the name of Mongolia capital?\na) Mongolia\nb) Brasilia\nc) Ulan\nd) Ulan Bator',
             4: 'Which is the longest river on Earth?\na) Rio de la Plata\nb) Nilo\nc) Amazonas\nd) Misisipi',
             5: 'Where had born the Olimpics?\na) Suecia\nb) Roma\nc) Grecia\nd) Estados Unidos',
             6: 'Which kind of animal is the wale?\na) Mammal\nb) Fish\nc) Reptile\nd) Rotifer',
             7: 'How many bones have an adult human been?\na) 200\nb) 178\nc) 206\nd) 255',
             8: 'Where the World War II ends?\na) 1946\nb) 1945\nc) 1944\nd) 1942',
             9: 'Where is located the Pisa Tower?\na) France\nb) Spain\nc) England\nd) Italy',
             10: 'What is the name of the result of multiplication?\na) Result\nb) Finish\nc) Product\nd) Conclusion',
             11: 'Which is the biggest ocean?\na) Pacific\nb) Atlantic\nc) Indiac\nd) Artic',
             12: 'What product is the principal of Guatemala?\na) Aluminium\nb) Coffee\nc) Cocoa\nd) Gold',
             13: 'Who is called The King of Rock?\na) Elton Johns\nb)Elvis Presley\nc) Pappo\nd) Freddy Mercury',
             14: 'Which is the biggest country?\na)Australia\nb) USA\nc) Groelandia\nd) Russia',
             15: 'Where is located the Eiffel Tower?\na) France\nb) Italy\nc) Spain\nd) Russia',
             16: 'Which sport had done Michael Jordan?\na) Basquetball\nb) Football\nc) Hockey\nd) Rugby',
             17: 'If 50 is the 100%, how much is 90%?\na) 30\nb) 45\nc) 40\nd) 5',
             18: 'From where is Zlatan Ibrahimovic\na) Sweden\nb) Switzerland\nc) England\nd) Poland',
             19: 'Which was the first worked metal by the humans?\na) Bronze\nb) Cupper\n c) Aluminium\nd) Iron',
             20: 'What was the Concorde?\na) Highspeed car\nb) Submarine\n c) Time-machine\n d) Superspeed plane'
             }
answers = {1: 'a',
           2: 'b',
           3: 'd',
           4: 'c',
           5: 'c',
           6: 'a',
           7: 'c',
           8: 'b',
           9: 'd',
           10: 'c',
           11: 'a',
           12: 'b',
           13: 'b',
           14: 'd',
           15: 'a',
           16: 'a',
           17: 'b',
           18: 'a',
           19: 'b',
           20: 'd'
           }

print("Wellcome to the questionnaire SingleChoice\n"
      "In it you may answer 10 questions. Each one have a punctuation of 1 if is correct. If not, will be -1.\n"
      "If you don't answer a question, you will have 0 point.\n"
      "You will have 2 minutes to finish the excercises. The questions no answered, will have 0 points.")
FirstName = input("Name: ")
FirstName = FirstName.capitalize()
LastName = input("LastName: ")
LastName = LastName.capitalize()
Age = int(input("Age: "))
points = 0

def countdown(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        msformat = "{:02d}:{:02d}".format(m, s)
        print(msformat, end="\n")
        time.sleep(1)
        seconds -= 1
    print('Start!')
def countdown2(seconds):
    while seconds:
        m, s = divmod(seconds, 60)
        msformat = "{:02d}:{:02d}".format(m, s)
        time.sleep(1)
        seconds -= 1

countdown(3)
countdown2(1)
start = time.time()
end = time.time()
timer = end - start
timer = int(timer)
i = 0
correct = 0
incorrect = 0
NA = 0
listq = [0]
while i < 10 and timer < 120:
    question = random.randint(1, 10)
    while question in listq:
        question = random.randint(1, 10)
    listq.append(question)
    print('\n' + str(i+1) + ') ' + questions[question])
    ans = input("Enter a/b/c/d or 'no' if you don't know: ")
    while ans != 'a' and ans != 'b' and ans != 'c' and ans != 'd' and ans != 'no':
        ans = input("Try again: a/b/c/d or 'no': ")
    end = time.time()
    timer = end - start
    timer = int(timer)
    i += 1
    if timer < 120:
        if ans == answers[question]:
            points += 1
            correct += 1
        elif ans == 'no':
            points = points
            NA += 1
        else:
            points -= 1
            incorrect += 1
    else:
        print('Time Over! Sadly, the last question does not count.')
end = time.time()
timer = end - start
timer = int(timer)
m, s = divmod(timer, 60)
msformat = "{:02d}:{:02d}".format(m, s)
time.sleep(1)
print('\nEndgame')
print('Your have done this questionnaire in ' + msformat, end="\n")
print('And you have done a total of points: ' + str(points))

f = open("CompetitionSingleChoice.txt", "a")
with open("CompetitionSingleChoice.txt") as fileCSC:
    t_line = sum(1 for line in fileCSC)+1
f.write(str(t_line) + ", " + FirstName + ", " + LastName + ", " + str(points) + ", " + str(msformat) + ", " +
        str(correct) + ", " + str(incorrect) + ", " + str(NA) + ";\n")
f.close()

