import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',  
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',  
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',  
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':  
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':  
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':  
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':  
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin':     
  'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(35):
	# create the quiz and answer key files
	quizFile = open('capitalQuiz%s.txt' %(quizNum+1),'w')
	answerFile = open('answerQuiz%s.txt' %(quizNum+1),'w')

	# write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write(''*20+'State Capitals Quiz (Form %s)' %(quizNum+1))
	quizFile.write('\n\n')

	# shuffle the order of the states
	states = list(capitals.keys())
	random.shuffle(states)

	# loop through all 50 states, makes a question for each
	for questionNum in range(50):
		# get right & wrong answers
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers+[correctAnswer]
		random.shuffle(answerOptions)

		quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1, states[questionNum]))
		for i in range(4):
			quizFile.write('     %s.  %s\n' %('ABCD'[i], answerOptions[i]))
		quizFile.write('\n\n')

		# write answer key to file
		answerFile.write('%s. %s\n' %(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)])) 

	quizFile.close()
	answerFile.close()





