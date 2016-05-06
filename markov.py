# Python program that generates a text describing the architecture of a federal prison.

# Import libraries
from textblob import TextBlob, Word
import markovify
import random

# Get raw text as string.

with open("business.txt") as f:
	business = f.read()

with open("rules.txt") as f:
	rules = f.read()

# Strip lines

rooms = list()
for line in open('rooms.txt'):
    line = line.strip()
    rooms.append(line)
prison_rooms_1 = random.choice(rooms)
prison_rooms_2 = random.choice(rooms)
prison_rooms_3 = random.choice(rooms)
prison_rooms_4 = random.choice(rooms)
prison_rooms_5 = random.choice(rooms)

objects = list()
for line in open('objects.txt'):
    line = line.strip()
    objects.append(line)
prison_objects_1 = random.choice(objects)
prison_objects_2 = random.choice(objects)
prison_objects_3 = random.choice(objects)
prison_objects_4 = random.choice(objects)

headers = list()
for line in open('headers.txt'):
    line = line.strip()
    headers.append(line)
prison_headers_1 = random.choice(headers)
prison_headers_2 = random.choice(headers)
prison_headers_3 = random.choice(headers)

business_advice = list()
for line in open('business.txt'):
    line = line.strip()
    business_advice.append(line)
business_advice_1 = random.choice(business_advice)

questions = list()
for line in open('questions.txt'):
    line = line.strip()
    questions.append(line)
random_question_1 = random.choice(questions)
random_question_2 = random.choice(questions)
random_question_3 = random.choice(questions)

# Build Markov models

markov_business = markovify.Text(business)

business_sentence_1 = markov_business.make_sentence()
business_sentence_2 = markov_business.make_sentence()

markov_rules = markovify.Text(rules)

rules_sentence_1 = markov_rules.make_sentence()
rules_sentence_2 = markov_rules.make_sentence()
rules_sentence_3 = markov_rules.make_sentence()


# Create lists of transition words

first = ["First", "First off", "To begin with", "Step one", "To start", "First and foremost"]
first_random = random.choice(first)

second = ["Second", "Next", "For the next step", "Step two", "Once that's finished", "In that case"]
second_random = random.choice(second)

third = ["Third", "Next", "Finally", "Lastly", "Step three", "To conclude", "To finish"]
third_random = random.choice(third)

that = ["ensure", "it is imperative", "consider", "it is necessary"]
that_words_1 = random.choice(that)
that_words_2 = random.choice(that)
that_words_3 = random.choice(that)

referral = ["With regards to", "In terms of", "Regarding", "Respecting", "With respect to", "Pertaining to", "Touching on", "With reference to"]
referral_random = random.choice(referral)

counting = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
counting_random = random.choice(counting)

numbers = ["Two", "Three", "Four", "Five", "Six", "Seven", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twelve", "Thirteen"]
numbers_random = random.choice(numbers)

objects_words = ["Requirements", "Needs", "Technical Requirements", "Necessities", "Exigencies"]
random_objects_words = random.choice(objects_words)

instructions = ["Instructions", "How-to", "Guide", "Steps", "Questions", "Problem Areas", "Concerns", "Considerations"]
instructions_random = random.choice(instructions)

furnishings = ["Furnishings", "Equipment", "Components", "Provisions", "Materials"]
furnishings_random = random.choice(furnishings)


# Print the handbook
print "----------------------------------------------------------------"
print
print prison_headers_3.title()+": A Handbook for Prison Design and Maintenance, "+counting_random+" Edition"
print
print "----------------"
print "Chapter "+numbers_random+": "+instructions_random+" "+prison_headers_1+" in the "+prison_rooms_1.title()
print
print "--------Design "+instructions_random+" & Issues--------"
print referral_random+" the "+prison_rooms_1.lower()+", "+rules_sentence_1.lower()+" "+first_random+", "+that_words_1+" that "+rules_sentence_3.lower()+" "+second_random+", "+that_words_2+" that "+rules_sentence_2.lower()+" "+third_random+", "+that_words_3+" that "+business_sentence_1.lower()+" "+business_advice_1
print
print "--------"+furnishings_random+" & "+random_objects_words+"--------"
print "*"+prison_objects_1.capitalize()
print "*"+prison_objects_2.capitalize()
print "*"+prison_objects_3.capitalize()
print "*"+prison_objects_4.capitalize()
print
print "--------Space List--------"
print "*"+prison_rooms_3.capitalize()
print "*"+prison_rooms_2.capitalize()
print "*"+prison_rooms_4.capitalize()
print "*"+prison_rooms_5.capitalize()
print
print "--------Key Questions--------"
print random_question_1+" "+random_question_2+" "+random_question_3

