import wikipedia as wk
import pyttsx3 as pytts

inputs = input("Search: ")

if(inputs == "exit"):
    exit(0)

search_result = wk.search(inputs, results=5)
print(search_result)

engine = pytts.init()

def QUERY():

    query = input("Choose search result: ")
    summary = wk.summary(query, sentences = 2)
    print(summary + ".. ")
    engine.say(summary)
    engine.runAndWait()

    elabqry = input("Would you like to have a more elaborate result?(y/n): ")
    if(elabqry == "y"):
        engine.say("Cool.")
        engine.runAndWait()

        summaryelab = wk.summary(query, sentences = 10) + ".. "
        print(summaryelab)
        engine.say(summaryelab)
        engine.runAndWait()

    elif(elabqry == "n"):
        engine.say("Goodbye")
        engine.runAndWait()
        exit(0)

    elif(not elabqry == "n" or "y"):
        print("Invalid input!")
        engine.say("Invalid input!")
        inputs
        engine.runAndWait()

QUERY()

