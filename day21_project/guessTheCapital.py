# Guess the capital mini project
# there are still edge casses need covering!
import time
import random

print("\n💭 Welcome to guessing the capital program. 💭")
time.sleep(2)

print("\nYou will be guessing the captial of countries. 🤔")
time.sleep(2)

print("\nRemember you have limited attempts and I will keep track of your score.")
time.sleep(2)

print("\nYou can quit anytime by 'q'\n")
questions = [
    ["What’s the capital of the United States? ", "washington"],
    ["What’s the capital of Canada? ", "ottawa"],
    ["What’s the capital of Mexico? ", "mexico city"],
    ["What’s the capital of Guatemala? ", "guatemala city"],
    ["What’s the capital of Belize? ", "belmopan"],
    ["What’s the capital of El Salvador? ", "san salvador"],
    ["What’s the capital of Honduras? ", "tegucigalpa"],
    ["What’s the capital of Nicaragua? ", "managua"],
    ["What’s the capital of Costa Rica? ", "san jose"],
    ["What’s the capital of Panama? ", "panama city"],
    ["What’s the capital of Cuba? ", "havana"],
    ["What’s the capital of Jamaica? ", "kingston"],
    ["What’s the capital of Haiti? ", "port-au-prince"],
    ["What’s the capital of the Dominican Republic? ", "santo domingo"],
    ["What’s the capital of the Bahamas? ", "nassau"],
    ["What’s the capital of Barbados? ", "bridgetown"],
    ["What’s the capital of Trinidad and Tobago? ", "port of spain"],
    ["What’s the capital of Saint Lucia? ", "castries"],
    ["What’s the capital of Dominica? ", "roseau"],
    ["What’s the capital of Antigua and Barbuda? ", "saint john's"],
    ["What’s the capital of Brazil? ", "brasilia"],
    ["What’s the capital of Argentina? ", "buenos aires"],
    ["What’s the capital of Colombia? ", "bogota"],
    ["What’s the capital of Chile? ", "santiago"],
    ["What’s the capital of Peru? ", "lima"],
    ["What’s the capital of Venezuela? ", "caracas"],
    ["What’s the capital of Ecuador? ", "quito"],
    ["What’s the capital of Bolivia? ", "la paz"],
    ["What’s the capital of Paraguay? ", "asuncion"],
    ["What’s the capital of Uruguay? ", "montevideo"],
    ["What’s the capital of the United Kingdom? ", "london"],
    ["What’s the capital of France? ", "paris"],
    ["What’s the capital of Germany? ", "berlin"],
    ["What’s the capital of Italy? ", "rome"],
    ["What’s the capital of Spain? ", "madrid"],
    ["What’s the capital of Portugal? ", "lisbon"],
    ["What’s the capital of the Netherlands? ", "amsterdam"],
    ["What’s the capital of Belgium? ", "brussels"],
    ["What’s the capital of Switzerland? ", "bern"],
    ["What’s the capital of Austria? ", "vienna"],
    ["What’s the capital of Sweden? ", "stockholm"],
    ["What’s the capital of Norway? ", "oslo"],
    ["What’s the capital of Denmark? ", "copenhagen"],
    ["What’s the capital of Finland? ", "helsinki"],
    ["What’s the capital of Ireland? ", "dublin"],
    ["What’s the capital of Poland? ", "warsaw"],
    ["What’s the capital of the Czech Republic? ", "prague"],
    ["What’s the capital of Greece? ", "athens"],
    ["What’s the capital of Romania? ", "bucharest"],
    ["What’s the capital of Ukraine? ", "kyiv"],
    ["What’s the capital of Russia? ", "moscow"],
    ["What’s the capital of Turkey? ", "ankara"],
    ["What’s the capital of Hungary? ", "budapest"],
    ["What’s the capital of Bulgaria? ", "sofia"],
    ["What’s the capital of Croatia? ", "zagreb"],
    ["What’s the capital of Serbia? ", "belgrade"],
    ["What’s the capital of China? ", "beijing"],
    ["What’s the capital of India? ", "new delhi"],
    ["What’s the capital of Japan? ", "tokyo"],
    ["What’s the capital of South Korea? ", "seoul"],
    ["What’s the capital of North Korea? ", "pyongyang"],
    ["What’s the capital of Indonesia? ", "jakarta"],
    ["What’s the capital of Thailand? ", "bangkok"],
    ["What’s the capital of Vietnam? ", "hanoi"],
    ["What’s the capital of the Philippines? ", "manila"],
    ["What’s the capital of Malaysia? ", "kuala lumpur"],
    ["What’s the capital of Singapore? ", "singapore"],
    ["What’s the capital of Pakistan? ", "islamabad"],
    ["What’s the capital of Bangladesh? ", "dhaka"],
    ["What’s the capital of Saudi Arabia? ", "riyadh"],
    ["What’s the capital of the United Arab Emirates? ", "abu dhabi"],
    ["What’s the capital of Palestine? ", "jerusalem"],
    ["What’s the capital of Iran? ", "tehran"],
    ["What’s the capital of Iraq? ", "baghdad"],
    ["What’s the capital of Jordan? ", "amman"],
    ["What’s the capital of Lebanon? ", "beirut"],
    ["What’s the capital of Qatar? ", "doha"],
    ["What’s the capital of Kuwait? ", "kuwait city"],
    ["What’s the capital of Oman? ", "muscat"],
    ["What’s the capital of Bahrain? ", "manama"],
    ["What’s the capital of Yemen? ", "sanaa"],
    ["What’s the capital of Syria? ", "damascus"],
    ["What’s the capital of Nepal? ", "kathmandu"],
    ["What’s the capital of Sri Lanka? ", "sri jayawardenepura kotte"],
    ["What’s the capital of Kazakhstan? ", "astana"],
    ["What’s the capital of Nigeria? ", "abuja"],
    ["What’s the capital of Egypt? ", "cairo"],
    ["What’s the capital of South Africa? ", "pretoria"],
    ["What’s the capital of Kenya? ", "nairobi"],
    ["What’s the capital of Morocco? ", "rabat"],
    ["What’s the capital of Ghana? ", "accra"],
    ["What’s the capital of Ethiopia? ", "addis ababa"],
    ["What’s the capital of Algeria? ", "algiers"],
    ["What’s the capital of Tunisia? ", "tunis"],
    ["What’s the capital of Tanzania? ", "dodoma"],
    ["What’s the capital of Australia? ", "canberra"],
    ["What’s the capital of New Zealand? ", "wellington"],
    ["What’s the capital of Fiji? ", "suva"],
    ["What’s the capital of Papua New Guinea? ", "port moresby"],
    ["What’s the capital of Iceland? ", "reykjavik"]
]
random.shuffle(questions)
score = 0
guessesAvr = 0
userGuess = ''
for question in questions:
    guesses = 0
    while guesses < 3: 
        userGuess = input(f"- {question[0]}").strip()
        if userGuess.lower() == question[1]:
            print("\n✅ Correct!\n")
            score += 1
            #guesses += 1 this caused an edge case to fail
            guessesAvr += 1
            break
        elif userGuess.lower() == 'q':
            break
        else:
            print("\n❌ Incorrect\n")
            guesses += 1
            guessesAvr += 1
    if guesses >= 3:
        print(f"❌ Too many wrong attempts the answer is {question[1]} ❌\n")
    if userGuess.lower() == 'q':
        break
newScore = (score / guessesAvr) * 100
if newScore >= 70:
    message = "That is impressive. 🏆"
elif newScore > 50:
    message = "Not too bad I guess. 👍"
elif newScore > 30:
     message = "You definitely can do better! 😕"
else:
     message = "That was a bad game. Try again! 😬"
print(f"\nThanks for playing! Your score is {score} / {guessesAvr} for an accuracy of {newScore}%, {message}\n")