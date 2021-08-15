#Import https://replit.com/join/etldfxmvce-ajaymcvi
import importlib
import os.path
import random
import time
from tkinter import *
import sys
import operator

#GUI
Window = Tk()
Window.title("Alacrity")
Window['background'] = '#004999'
Homepage = LabelFrame(Window)
Homepage['background'] = '#004999'
Homepage.pack(padx=0, pady=0)

#Common intro widgets
IntroLabel2 = Label(
    Homepage,
    text=
    "The purpose of this program is to calculate how long it will take you to complete your homework based",
    bg='#004999',
    fg='#edc967')
IntroLabel3 = Label(
    Homepage,
    text=
    " on your current knowledge of the subject of your choice. No more procrastinating!",
    bg='#004999',
    fg='#edc967')


#Function to reset Homescreen
def Home():
	importlib.reload(SavedName)
	#Clear screen, thanks for the code Ajay
	for widgets in Homepage.winfo_children():
		widgets.grid_forget()

	if (os.path.isfile("SavedName.py")) == True:
		OldIntroLabel1 = Label(Homepage,
			text="Welcome back, " + SavedName.name +
			", to Alacrity.",
			bg='#004999',
			fg='#edc967')
		OldIntroLabel1.grid(row=0, column=0, columnspan=30)
	else:
		NewIntroLabel1 = Label(Homepage,
			text="Welcome to Alacrity",
			bg='#004999',
			fg='#edc967')
		NewIntroLabel1.grid(row=0, column=0, columnspan=30)

	IntroLabel2 = Label(
		Homepage,
		text=
		"The purpose of this program is to calculate how long it will take you to complete your homework based",
		bg='#004999',
		fg='#edc967')
	IntroLabel3 = Label(
		Homepage,
		text=
		" on your current knowledge of the subject of your choice. No more procrastinating!",
		bg='#004999',
		fg='#edc967')
	#Creating category widgetsHoHomepage
	GetRouteLabel = Label(
		Homepage,
		text=
		"Would you like to: calculate Homework time, re-take quiz, change name, or quit?")
	GetTimeButton = Button(Homepage,
		text="Time",
		width=5,
		command=Time,
		bg='#003d80',
		fg='#edc967')
	GetReQuizButton = Button(Homepage,
		text="Re-quiz",
		width=5,
		command=Quiz,
		bg='#003d80',
		fg='#edc967')
	GetReNameButton = Button(Homepage,
		text="Re-name",
		width=5,
		command=ChangeName,
		bg='#003d80',
		fg='#edc967')
	GetQuitButton = Button(Homepage,
		text="Quit",
		width=5,
		command=Quit,
		bg='#003d80',
		fg='#edc967')

	#Open category widgetsHomepagehome
	GetRouteLabel.grid(row=4, column=0, columnspan=30)
	GetTimeButton.grid(row=5, sticky=W)
	GetReQuizButton.grid(row=6, sticky=W)
	GetReNameButton.grid(row=7, sticky=W)
	GetQuitButton.grid(row=8, sticky=W)
	IntroLabel2.grid(row=1, column=0, columnspan=30)
	IntroLabel3.grid(row=3, column=0, columnspan=30)


#Checks if it's the users first time (see if their averages have been made)
if (os.path.isfile("SavedName.py")) == True:
	import SavedName
	SavedName.name

	#Check for SavedMath.py
	try:
		import SavedMath
		try:
			mathAvgTime = SavedMath.MathAvgTime
		except AttributeError:
			useless=1
	except ImportError:
		f = open("SavedMath.py", "w")
		f.close()

	#Check for SavedEnglish.py
	try:
		import SavedEnglish
		try:
			engAvgTime = SavedEnglish.EnglishAvgTime
		except AttributeError:
			useless=1
	except ImportError:
		f = open("SavedEnglish.py", "w")
		f.close()

	#Check for SavedScience.py
	try:
		import SavedScience
		try:
			sciAvgTime = SavedScience.ScienceAvgTime
		except AttributeError:
			useless=1
	except ImportError:
		f = open("SavedScience.py", "w")
		f.close()

	#Check for SavedHistory.py
	try:
		import SavedHistory
		try:
			hisAvgTime=SavedHistory.HistoryAvgTime
		except AttributeError:
			useless=1
	except ImportError:
		f = open("SavedHistory.py", "w")
		f.close()

	#Check for SavedCs.py
	try:
		import SavedCs
		try:
			cSAvgTime = SavedCs.CSAvgTime
		except AttributeError:
			useless=1
	except ImportError:
		f = open("SavedCs.py", "w")
		f.close()

	#Introduction Labels
	OldIntroLabel1 = Label(Homepage,
		text="Welcome back, " + SavedName.name +
		", to Alacrity.",
		bg='#004999',
		fg='#edc967')
	#Welcome back message
	OldIntroLabel1.grid(row=0, column=0, columnspan=30)
	IntroLabel2.grid(row=1, column=0, columnspan=30)
	IntroLabel3.grid(row=3, column=0, columnspan=30)

else:
	NewIntroLabel1 = Label(Homepage,
		text="Welcome to Alacrity",
		bg='#004999',
		fg='#edc967')

	NewIntroLabel1.grid(row=0, column=0, columnspan=30)
	IntroLabel2.grid(row=1, column=0, columnspan=30)
	IntroLabel3.grid(row=2, column=0, columnspan=30)

run = 1
while run == 1:
	if (os.path.isfile("SavedName.py")) == True:
		rerun = 1
		while rerun == 1:

			def Time():
				#Clear screen
				for widgets in Homepage.winfo_children():
					widgets.grid_forget()

				#makes a calculator

				currentOutput = Entry(Homepage,
					bg='#004999',
					fg='#edc967',
					width=40)
				currentOutput.grid(row=0, column=0, columnspan=4)

				def Clear():
					currentOutput.config(state=NORMAL)
					currentOutput.delete(0, END)
					currentOutput.config(state=DISABLED,
						bg='#004999',
						fg='#edc967')

				def Nums(Num):
					#Calculation, I don't really know this stuff
					if Num != int:
						#Gets time and converts it
						TotalTime = (int(currentOutput.get()) * (Num))  #To be changed
						avgSecs = int(TotalTime % 60)
						avgMins = int((TotalTime - avgSecs) // 60)
						avgHours = int((TotalTime // 60) // 60)
						#prints time in entry
						currentOutput.config(state=NORMAL)
						currentOutput.delete(0, END)
						currentOutput.insert(
							0,
							('It should take you ' + str(avgHours) + 'hrs : ' +
							str(avgMins) + 'mins : ' + str(avgSecs) + 's'))
						currentOutput.config(state=DISABLED,
							bg='#004999',
							fg='#edc967')
					else:
						currentOutput.config(state=NORMAL)
						realCurrent = currentOutput.get()
						currentOutput.delete(0, END)
						currentOutput.insert(0, str(realCurrent) + str(Num))
						currentOutput.config(state=DISABLED,
							bg='#004999',
							fg='#edc967')

				#Constructs button for the calculator
				one = Button(Homepage,
					text='1',
					command=lambda: Nums(1),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				two = Button(Homepage,
					text='2',
					command=lambda: Nums(2),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				three = Button(Homepage,
					text='3',
					command=lambda: Nums(3),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				four = Button(Homepage,
					text='4',
					command=lambda: Nums(4),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				five = Button(Homepage,
					text='5',
					command=lambda: Nums(5),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				six = Button(Homepage,
					text='6',
					command=lambda: Nums(6),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				seven = Button(Homepage,
					text='7',
					command=lambda: Nums(7),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				eight = Button(Homepage,
					text='8',
					command=lambda: Nums(8),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				nine = Button(Homepage,
					text='9',
					command=lambda: Nums(9),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				zero = Button(Homepage,
					text='0',
					command=lambda: Nums(0),
					bg='#004999',
					fg='#edc967',
					padx=35,
					pady=35)
				clear = Button(Homepage,
					text='clear',
					command=Clear,
					bg='#003d80',
					fg='#fc6a03',
					padx=21,
					pady=35)

				if "mathAvgTime" in globals():
					Math = Button(Homepage,
						text='Math',
						command=lambda: Nums(mathAvgTime),
						bg='#004999',
						fg='#edc967',
						width=10)
				else:
					Math = Button(Homepage,
						text='Math',
						state=DISABLED,
						bg='#004999',
						fg='#edc967',
						width=10)
				if "engAvgTime" in globals():
					English = Button(Homepage,
						text='English',
						command=lambda: Nums(engAvgTime),
						bg='#004999',
						fg='#edc967',
						width=10)
				else:
					English = Button(Homepage,
						text='English',
						state=DISABLED,
						bg='#004999',
						fg='#edc967',
						width=10)
				if "hisAvgTime" in globals():
					History = Button(Homepage,
						text='History',
						command=lambda: Nums(hisAvgTime),
						bg='#004999',
						fg='#edc967',
						width=10)
				else:
					History = Button(Homepage,
						text='History',
						state=DISABLED,
						bg='#004999',
						fg='#edc967',
						width=10)
				if "sciAvgTime" in globals():
					Science = Button(Homepage,
						text='Science',
						command=lambda: Nums(sciAvgTime),
						bg='#004999',
						fg='#edc967',
						width=10)
				else:
					Science = Button(Homepage,
						text='Science',
						state=DISABLED,
						bg='#004999',
						fg='#edc967',
						width=10)
				if "cSAvgTime" in globals():
					CS = Button(Homepage,
						text='Comp. Sci',
						command=lambda: Nums(cSAvgTime),
						bg='#004999',
						fg='#edc967',
						width=10)
				else:
					CS = Button(Homepage,
						text='Comp. Sci',
						state=DISABLED,
						bg='#004999',
						fg='#edc967',
						width=10)

				Exit = Button(Homepage,
					text='Exit',
					command=Home,
					bg='#003d80',
					fg='#fc6a03',
					padx=26,
					pady=35)

				one.grid(row=9, column=0, rowspan=4)
				two.grid(row=9, column=1, rowspan=4)
				three.grid(row=9, column=2, rowspan=4)
				four.grid(row=5, column=0, rowspan=4)
				five.grid(row=5, column=1, rowspan=4)
				six.grid(row=5, column=2, rowspan=4)
				seven.grid(row=1, column=0, rowspan=4)
				eight.grid(row=1, column=1, rowspan=4)
				nine.grid(row=1, column=2, rowspan=4)
				zero.grid(row=13, column=1, rowspan=4)
				clear.grid(row=13, column=2, rowspan=4)
				Math.grid(row=2, column=3, rowspan=2)
				English.grid(row=4, column=3, rowspan=2)
				History.grid(row=6, column=3, rowspan=2)
				Science.grid(row=8, column=3, rowspan=2)
				CS.grid(row=10, column=3, rowspan=2)
				Exit.grid(row=13, column=0, rowspan=4)

			def Quit():
				sys.exit()
				Homepage.destroy()

			def ChangeName():
				#Clear screen
				for widgets in Homepage.winfo_children():
					widgets.grid_forget()

				NewNameIntro = Label(Homepage,
					text="New name:",
					bg='#004999',
					fg='#edc967')
				NameEnteredEntry = Entry(Homepage,
					width=15,
					bg='#003d80',
					fg='#edc967')
				NewNameIntro.grid(row=0, column=0)
				NameEnteredEntry.grid(row=0, column=1)
				def NewName():
					name = NameEnteredEntry.get()
					NameEnteredEntry.delete(0, END)
					f = open("SavedName.py", "w")
					f.write("\n" "name = " + "'" + name + "'")
					f.close()
					NameEnteredEntry.config(state=DISABLED)
					Label(Homepage,
						text="I will call you " + name + " from now on",
						bg='#004999',
						fg='#edc967').grid(row=1, column=0)

				NameEnteredButton = Button(Homepage,
					text="Enter",
					width=5,
					command=NewName,
					bg='#004999',
					fg='#edc967')
				Exit = Button(Homepage, text="Exit", command=Home)
				NameEnteredButton.grid(row=0, column=2)
				Exit.grid(row=2, column=0)

			def Quiz():
				for widgets in Homepage.winfo_children():
					widgets.grid_forget()
				global questionNum
				global questionOptions
				questionNum=-1 #I add +1 later
				questionOptions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
				StartTimer = time.time()

				def EnglishQuiz():						#This is the new one
					global subject
					global question
					subject = "English"
					question=[
						#1
						"To which city does Romeo go after being exiled from Verona? \n a) Padua \n b) Mantua \n c) Venice \n d) None of the above\n",

						#2
						"Who performs Romeo and Juliet’s marriage? \n a) Friar Lawrence \n b) Friar Tomas \n	c) Friar Vincent \n d) Friar Mateo",

						#3
						"Tybalt kills Mercutio True or False? \n a) True \n b) False",

						#4
						"Which character first persuades Romeo to attend the feast? \n a) Benvolio \n b) Mercutio \n c) Juliet \n d) None of the above",

						#5
						"Romeo hears a lark the night after their wedding. True or False? \n a) True \n b) False",

						#6
						"To what does Romeo first compare Juliet during the balcony scene?\n a) The silver moon \n b) The stars\n c) A summer's day	\n d) The morning sun",

						#7
						"Paris is related to Prince Escalus. True or False?	\n a) True \n b) False",

						#8
						"Who proposes that a gold statue of Juliet be built in Verona? \n a) Romeo b) Montague \n c) Capulet \n d) All of the above",

						#9
						"Romeo is killed with a dagger in Juliet's tomb \n a) True \n b) False",

						#10
						"Romeo madly in love for with Juliet for the entirety of the play. True or False? \n a) True \n b) False",

						#11
						"Who discovers Juliet after she takes Friar Lawrence's potion?\n a) Lady Capulet\n b) Capulet\n c) Paris\n d) The Nurse\n",

						#12
						"Why is Romeo exiled? \n a) For killing Tybalt \n b) For marrying Julliet against her father's will\n c) For killing Mercutio\n d) For publicly admitting his atheism",

						#13
						"Who is the fairy that Mercutio says visits Romeo in dreams? \n a) Puck \n b) Queen Mab \n c) Beelzebub \n d) Jack o' the Clover",

						#14
						"What does the Nurse advise Juliet to do after Romeo is exiled? \n a) Follow her husband to Mantua \n b) Wait for Romeo in Verona \n c) Act as if Romeo is dead and marry Paris \n d) Commit suicide",

						#15
						"Romeo and Juliet meet at the pier from which Malvolio is departing for Spain. True or False? \n a) True \n b) False",

						#16
						"Why does the Apothecary agree to sell Romeo poison? \n a) He is poor, and needs the money \n b) He can see that Romeo is passionate \n c) He is afraid taht Romeo will hurt him if he refuses \n d) He is a friend of Friar Lawrence",

						#17
						"Who is the last person to see Juliet before she stabs herself dead? \n a) Paris \n b) Friar Lawrence \n c) Tybalt \n d) Romeo",

						#18
						"Why is Friar John unable to deliver Friar Lawrence's message to Romeo in Mantua? \n a) He is killed by a Capulet servant \n b) He is attacked by bandits on the road \n c) He is held inside a quarantiend house, and is unable to leave \n d) Romeo is stopped in Padua and never makes it to Mantua",

						#19
						"Romeo and Juliet meet on Saturday. True or false? \n a) True \n b) False",

						#20
						"What decade was Romeo and Juliet written? \n a) 1570s\n b) 1590s \n c) 1600s \n d) 1610s",

						#21
						"Whom does Mercutio curses as he lies dying after a duel? \n a) The Monstagues and Capulets \n b) Romeo \n c) Tybalt \n d) Romeo and Tybalt",

						#22
						"In what area is Friar Lawrence an expert? \n a) Roman history \n b) Languages \n c) Plants and herbs \n d) Swordfighting",

						#23
						"The term star-crossed is used to describe lovers. True or false? \n a) True \n b) False",					

						#24
						"Tybalt first challenge Romeo to a duel because he is offended that Romeo loves his cousin. True or false? \n a) True,\n b) False",

						#25
						"Shakespeare died in 1616. True or False?\n a) True \n b) False"]
					global questionAnswerOptions
					questionAnswerOptions=[4,4,2,4,2,4,2,4,2,2,4,4,4,4,2,4,4,4,2,4,4,4,2,2,2]
					global answerQuestion
					answerQuestion=["B","A","A","A","B","D","A","B","B","B","D","A","B","C","B","A","B","C","B","B","A","C","A","B","A"]
					NextQuestionLoad()

				def HistoryQuiz():
					global subject
					global question
					subject = "History"
					question=[
						#1
						"In the 1500s, fur hats became very popular in Europe. This created a huge demand for imported pelts from which hard-working and industrious animal from Canada.\n a) Muskrat\n Beaver\n c) Polar bear\n d)Arctic fox",
						
						#2
						"Jeanne Sauve was the first Canadian female to hold what important position?\n a) Zamboni driver for the Toronto Maple Leafs Hockey Club\n b) Top car buyer for Prime Minister\n c) Canada's Governor General\n d) Head Janitor for Canada's House of Parliament",
						
						#3
						"This man was Canada's Prime Minister during WWII. What was his name?\n a) William Lyon Mackenzie King\n b) Terrance Stanley Fox\n c) Gordon Merdith Lightfoot\n d) Gordon Meredith Lightfoot",
						
						#4
						"What animal, hunted almost to extinction, was once the main source of food for the Blackfoot Indians of Canada\n a) Whooping Crane\n b) Leatherback Turtle\n c) Bison\n d) Sea Otter",
						
						#5
						"Including the amateur era, which of the following two teams were Canada's first ice hockey teams to win a Stanley Cup Championship?\n a) Toronto Argonauts & Montreal Alouettes\n b) Toronto Raptors & Vancouver Grizzlies\n c) Toronto Blue Jays & Montreal Expos\n d) Winnipeg Victorias & Montreal Hockey Club",
						
						#6
						"What type of 'footwear,' used specifically for winter travel, was invented by Canada's first native peoples?\n a) Toboggan\n b) Snowmobile\n c) Snowshoes\n d) Dog sled",
						
						#7
						"The world-famous Canadian, Rick Hansen, travelled around the world to raise money for spinal cord research. What made this trip extremely difficult?\n a) He completed the trip in a wheelchair\n b) He became confused and went around the Great Wall of China 3 times\n c) He made the entire trip walking on his hands\n d) He almost drowned swimming across the Alantic and Pacific Oceans",
						
						#8
						"From 1920-1933, weven well known Canadians were known as 'The Group of Seven.' What wass this group famous for doing?\n a) They were a female hockey team who won eight Stanley Cups\n b) They built the CN Tower and Skydome in 1920-1933\n c) They were seven Canadian men who were friends of Adolph Hitler\n d) They were a group of talented landscape painters",
						
						#9
						"The name 'Canada' was taken from the same Iroquois Indian word 'canada.' What does 'canada' mean when translated to English?\n a) Bir red leaf\n b) Village\n c) Home of Santa Claus\n d) Lazy beaver",
						
						#10
						"In 1917 during the first world war, a Canadian city was flattened when two ships collided in the harbour, causing a large fire which then caused an enormous explosion. Which city am I talking about?\n a) Whitehorse, Yukon Territories\n b) Halifax, Nova Scotia\n c) Frederiction, New Brunswick\n d) Winnipeg, Manitoba",
						
						#11
						"Who is the current Prime Minister?\n a) Michelle Jean\n b) Dalton McGuinty\n c) Stephen Harpe\n d) Justin Trudeau",
						
						#12
						"What is the capital of Canada?\n a) Toronto\n b) Vancouver\n c) Ottawa\n d) Montreal", 
						
						#13
						"Canada entered into Confederation in 1867. True or false\n a) True\n b) False",
						
						#14
						"What country took control of Quebec away from France, by winning the battle of the Plains of Abraham?\n a) Britain\n b) Germany\n c) Russia\n d) United States",
						
						#15
						"The name of the route to Canada taken by blacks escaping slavery in the US is 'TransCanada Highway. True or false?\n a) True\n b) False",
						
						#16
						"Which province was the last to join Confederation?\n a) Newfoundland\n b) Ontario\n c) Manitoba\n d) Nunavut",
						
						#17
						"Remeberance Day in Canada falls on November 11. November 11 was the last day of which war?\n a) Korean War\n b) WW1\n c) Vietnam War\n d) Cold War",
						
						#18
						"The members of Blacks were once forced to pay a head tax to immigrate to Canada. True or false?\n a) True\n b) False",
						
						#19
						"What is the name of the Metis leader who was hanged by the federal government in 1885?\n a) Jame Cabot\n b) Christopher Colombus\n c) Louis Riel\n d) Pierre Bottineau",
						
						#20
						"What term is commonly used to refer to early French fur traders in Canada?\n a) Loyalists\n b) Voyageurs\n c) Entrepeneur\n Conquistadors",
						
						#21
						"Canada's head of government is the Governor General. True or false?\n a) True\n b) False",
						
						#22
						"Who was the first Prime Minister?\n a) Lester B Pearson\n b) Sir John A Macdonald\n c) Kim Campbell\n d) Piere Trudeau",
						
						#23
						"Canada has 10 provinces and 3 territories. Nunavut being the latest territory created in 1999. True or false?\n a) True\n",
						
						#24
						"Canada has only 1 official language. True or false?\n a) True\n b) False",
						
						#25
						"At the beginning of the 20th century the Dominion of Canada was a part of the British Empire, with the status of a colony. True or false?\n a) True\n b) False"]
					global questionAnswerOptions
					questionAnswerOptions=[4,4,4,4,4,4,4,4,4,4,4,4,2,4,2,4,4,2,4,4,2,4,4,2,2]
					global answerQuestion
					answerQuestion=["B","C","A","C","D","C","A","D","B","B","D","C","A","A","B","A","B","B","C","B","B","B","A","B","B",]
					NextQuestionLoad()
				
				def ScienceQuiz():						#This is the new one
					global subject
					global question
					subject = "Science"
					question=[
						#1
						"Electric resistance is typically measured in what units?\n a) Ohms\n b) Amperes\n c) Coulombs\n d) None of the above",

						#2
						"What orbits the nucleus of an atom?\n a) Electrons\n b) Neutrons\n c) Protons\n d) All of the above",

						#3
						"Conductors have high or low resistance?\n a) High\n b) Low",

						#4
						"Which famous scientist introduced the idea of natural selection?\n a) Issac Newton\n b) Albert Einstein\n c) Charles Darwin\n d) None of the above",

						#5
						"DNA is the shortened form of the term ‘Deoxyribonucleic acid’? True or False?\n a) True\n b) False\n ",

						#6
						"The area of biology devoted to the study of fungi is known as?\n a) Paleontology\n b) Ichtyology\n c) Entomology\n d) Mycology",

						#7
						"A neutron has no net electric charge. True or False?\n a) True\n b) False",

						#8
						"What is the hottest planet in our solar system?\n a) Earth\n b) Venus\n c) Mars\n d) Jupiter",

						#9
						"Plasma is a state of matter. True or False?\n a) True\n b) False",

						#10
						"Bases have a pH level below 7. True or False?\n a) True\n b) False",

						#11
						"The bulk of digestion takes place in the...\n a) Large Intestine\n b) Stomach\n c) Pancreas\n d) Small Intestine",

						#12
						"What color light has the highest frequency?\n a) Red\n b) Violet\n c) Yellow\n d) Green",

						#13
						"Which of the following is NOT an example of an arthropod?\n a) Sea horse\n b) Crab\n c) Centipede\n d) Spider",

						#14
						"Momentum is the...\n a) Push or pull that forces an object to change its speed or direction\n b) Tendency of an object to continue moving in the same direction\n c) Rate at which an object changes position\n d) Rate of change of velocity",

						#15
						"Momentum is...\n a) Sedimentary\n b) Igneous\n c) Metamorphic\n d) None of the above",

						#16
						"Which of the following depicts a chemical process?\n a) Iron forms rust\n b) Ice melts\n c) Water causes soil erosion\n d) Helium is combined with neon",

						#17
						"Which of the following kingdoms is considered the most primitive?\n a) Plantae\n b) Protista\n c) Fungi\n d) Monera",

						#18
						"Which of the following kingdoms is considered the most primitive?\n a) Neutrons and protons\n b) Electrons and protons\n c) Electrons and neutrons\n d) Neutrons and positrons",

						#19
						"This is the collection of all populations of a habitat.\n a) Community\n b) Biome\n c) Ecosystem\n d) Population",

						#20
						"____ are necessary for the body's maintenance, growth, and repair.\n a) Fats\n b) Proteins\n c) Carbohydrates\n d) Vitamins",

						#21
						"Over the course of 24 hours the...\n a) Earth rotates 360 degrees around the Sun\n b) Moon rotates 360 degrees around the Earth\n c) Earth rotates 360 degrees about its axis\n d) Moon rotates 360 degrees about its axis",

						#22
						"A ______ is a unit of inheritance\n a) Allele\n b) Genotype\n c) Phenotype\n d) Gene",

						#23
						"Which of the following is a sedimentary rock?\n a) Marble\n b) Shale\n c) Granite\n d) Slate",					

						#24
						"Table salt is considered...\n a) Covalent Compound\n b) Ionic Compound\n c) Ion\n d) All of the above",

						#25
						"Which of the following is the phylum that includes man?\n a) Mammalia\n b) Primata\n c) Chordata\n d) Animalia"]
					global questionAnswerOptions
					questionAnswerOptions=[4,4,2,4,2,4,2,4,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
					global answerQuestion
					answerQuestion=["A","A","B","C","A","D","A","B","A","B","D","B","A","A","B","A","D","A","A","B","C","D","B","B","C"]
					NextQuestionLoad()

				def CSQuiz():
					global subject
					global question
					subject = "CS"
					question=[
						#1:
						#Question One Correct Answer = True / A):
						"A network is a system or group of interconnected beings or things. True or False? \n a) True,\n b) False",
						#------------------------------------------------------------------
						#2:
						#Question Two Correct Answer = C):
						"What is the basic storage unit on a portable device? \n a) Byte \n b) Megabyte \n c) Bit \n d) Geopbyte",

						#------------------------------------------------------------------
						#3:
						#Question Three Correct Answer = True / A):
						"Before the 20th century, calculations were performed by humans. True or False? \n a) True, \n b) False",
					
						#------------------------------------------------------------------
						#4:
						#Question Four Correct Answer = False / B):
						"The Astrolabe, a mechanical computer was invented by the Greeks about 2100 years ago was used as a navigational aid by pilots. True or False? \n a) True \n b) False",
							
						#------------------------------------------------------------------
						#5:
						#Question Five Correct Answer = False / B):
						"There are 4 significant generations of computers. True or False? \n a) True \n b) False",
						

						#------------------------------------------------------------------
						#6:
						#Question Six Correct Answer = False / B):
						"LAN is widespread over a large geographic area. True or False? \n a) True \n b) False",
						#------------------------------------------------------------------
						#7:
						#Question Seven Correct Answer = False / B):
						"Network connections can only be wireless. True or False? \n a) True \n b) False",
						#------------------------------------------------------------------
						#8:
						#Question Eight Correct Answer = True / A):
						"The computer is an electronic device that executes program instructions. True or False? \n a) True \n b) False",
						#------------------------------------------------------------------
						#9:
						#Question Nine Correct Answer = B):
						"The Third Generation of computers used…. \n a) Transistor driven machines that stored information in memory \n b) Integrated circuits with miniaturized transistors on silicon chips, called semiconductors \n c) Vacuum tube as circuits and magnetic drums for memory \n d) Parallel processing and superconductors",

						#------------------------------------------------------------------
						#10:
						#Question Ten Correct Answer = True / A):
						"The Analytical Engine was the first programmable mechanical computer. True or False? \n a) True \n b) False",
						#------------------------------------------------------------------
						#11:
						#Question Eleven Correct Answer = D):
						"Who was Charles Babbage? \n a) Charles Babbage was a mathematician \n b) Charles Babbage was a mechanical engineer \n c) Charles Babbage was the inventor of the Analytical Engine \n d) All of the above",

						#------------------------------------------------------------------
						#12:
						#Question Twelve Correct Answer = True / A):
						"Spyware is a form of malicious software that monitors the user’s activities. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#13:
						#Question Thirteen Correct Answer = B):
						"What is the main difference between system software and application software? \n a) System software and application software fulfill the same purpose of running the computer’s hardware and therefore have no difference \n b) System software handles the running of the computer’s hardware whereas application software runs programs on the computer \n c) System software handles the running of the programs on the computer whereas application software runs the computer’s hardware \n d) System software handles the health of the computer whereas application software maintains the integrity of the computer’s hardware",

						#------------------------------------------------------------------
						#14:
						#Question Fourteen Correct Answer = False / B):
						"The Colossus was created and engineered by a group of British scientists whose base was located at Bletchley Circle. True or False \n a) True \n b) False",

						#------------------------------------------------------------------
						#15:
						#Question Fifteen Correct Answer = True / A):
						"The use of parallel processing and superconductors is making artificial intelligence a reality. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#16:
						#Question Sixteen Correct Answer = False / B):
						"Phishing is the act of giving consent to view personal data. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#17:
						#Question Seventeen Correct Answer = True / A):
						"WAN does not share internet access. True or False? \n a) True \n b) False"
						#------------------------------------------------------------------
						#18:
						#Question Eighteen Correct Answer = True / A):
						"Software provides instructions to the computer for specific tasks. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#19:
						#Question Nineteen Correct Answer = False / B):
						"Python requires a specific termination character to indicate the end of a statement. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#20:
						#Question Twenty Correct Answer = True / A):
						"Programs use an output stream to send data to a standard output device. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#21:
						#Question Twenty-One Correct Answer = True / A):
						"Comment lines begin with the octothorpe character #). True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#22:
						#Question Twenty-Two Correct Answer = D):
						"Proper use of commenting will... \n a) Make code maintenance much easier \n b) Make finding bugs faster \n c) Help others understand what the code is doing \n d) All of the above",

						#------------------------------------------------------------------
						#23:
						#Question Twenty-Three Correct Answer = False / B):
						"The arithmetic operator ' * ' represents division. True or False? \n a) True \n b) False",
					
						#------------------------------------------------------------------
						#24:
						#Question Twenty-Four Correct Answer = True / A):
						"The main difference between for loops and while loops is that for loops are used when it is known how many times the loop is to be repeated, whereas while loops are used when a specific condition must be met. True or False? \n a) True \n b) False",

						#------------------------------------------------------------------
						#25:
						#Question Twenty-Five Correct Answer = True / A):
						"Being a good digital means to demonstrate and practice safe, responsible, and legal use of technology. True or False? \n a) True \n b) False"]
					global questionAnswerOptions
					questionAnswerOptions=[2,4,2,2,2,2,2,2,2,4,2,4,2,4,2,2,2,2,2,2,2,4,2,2,2]
					global answerQuestion
					answerQuestion=["A","C","A","B","B","B","B","A","B","A","D","A","B","B","A","B","A","A","B","A","A","D","B","A","A"]
					NextQuestionLoad()

				def NextQuestionLoad():
					for widgets in Homepage.winfo_children():
						widgets.grid_forget()
					global questionNum
					global question
					global questionAnswerOptions
					global answerQuestion
					global questionOptions
					
					questionNum+=1
					selectedQuestion = random.choice(questionOptions)
					questionOptions.remove(selectedQuestion)

					#changing questionNum here is fine
					if questionNum<10:
						QuesGui(question[selectedQuestion], questionAnswerOptions[selectedQuestion], answerQuestion[selectedQuestion])
					else: #DON'T end the timer here
						QuizConclude(), #save info and exit to home

				#Doesn't work
					Exit = Button(Homepage,text='Exit',command=Home,bg='#003d80',fg='#fc6a03',padx=26,pady=35)
					Exit.grid(row=0,column=0)

				def QuesGui(question,n,answer):
					QuestionLabel = Label(Homepage,text=question, bg='#004999', fg='#edc967')
					QuestionLabel.grid(row=0,column=0,columnspan=3)

					def Check(button,answer):
						answer = locals()[answer]
						if(button==answer):
							answer.configure(text='CORRECT!',fg='green',bg='white')
						else:
							A.configure(text='Incorrect!',fg='red',bg='white')
							B.configure(text='Incorrect!',fg='red',bg='white')
							C.configure(text='Incorrect!',fg='red',bg='white')
							D.configure(text='Incorrect!',fg='red',bg='white')
							answer.configure(text='CORRECT!',fg='green',bg='white')



						Next.configure(state=ACTIVE)
						Next.configure(command=NextQuestionLoad,bg='#004999', fg='#edc967')
					if n==2:
						A=Button(Homepage,text='A',pady=40,padx=50,command=lambda: Check("A",answer),bg='#004999', fg='#edc967')
						B=Button(Homepage,text='B',pady=40,padx=50,command=lambda: Check("B",answer),bg='#004999', fg='#edc967')
						C=Button(Homepage,text='C',pady=40,padx=50,state=DISABLED)
						D=Button(Homepage,text='D',pady=40,padx=50,state=DISABLED)

					else:
						A=Button(Homepage,text='A',pady=40,padx=50,command=lambda: Check("A",answer),bg='#004999', fg='#edc967')
						B=Button(Homepage,text='B',pady=40,padx=50,command=lambda: Check("B",answer),bg='#004999', fg='#edc967')
						C=Button(Homepage,text='C',pady=40,padx=50,command=lambda: Check("C",answer),bg='#004999', fg='#edc967')
						D=Button(Homepage,text='D',pady=40,padx=50,command=lambda: Check("D",answer),bg='#004999', fg='#edc967')
					Next = Button(Homepage,text='Next Question',state=DISABLED)


					A.grid(row=1,column=0)
					B.grid(row=1,column=1)
					C.grid(row=2,column=0)
					D.grid(row=2,column=1)
					Next.grid(row=3,column=0,columnspan=2)

				def MathQuiz():
					global subjectQuiz
					subjectQuiz = "Math"
					questionNumMath=0
					MathScore=0
					currentOutput = Entry(Homepage, bg='#004999',fg='#edc967',width=41)
					currentOutput.grid(row=0,column=0,columnspan=4)

					def NewMathQues():
						opp=random.randint(1,4)
						if opp==1:
							opp=('+')
						if opp==2:
							opp=('-')
						if opp==3:
							opp=('x')
						if opp==4:
							opp=('//')
						opps = {'+' : operator.add,'-' : operator.sub, 'x' : operator.mul, '//' : operator.truediv}

						num2=random.randint(0,50)
						num1=random.randint(num2,50)
						
						MathQues=Label(Homepage,width=15,text=("What is "+str(num1)+" "+opp+" "+str(num2)),bg='#004999',fg='#edc967')
						MathQues.grid(row=5,column=3,rowspan=2)

						answer=int(opps[opp](num1,num2))
						return (answer)

					def clear():
						currentOutput.config(state=NORMAL)
						currentOutput.delete(0, END)
						currentOutput.config(state=DISABLED,bg='#004999',fg='#edc967')

					def Nums(Num):
						currentOutput.config(state=NORMAL)
						realCurrent = currentOutput.get()
						currentOutput.delete(0, END)
						currentOutput.insert(0, str(realCurrent) + str(Num))
						currentOutput.config(state=DISABLED,bg='#004999',fg='#edc967')

					def Check(answer):
						global MathScore
						if int(currentOutput.get())==answer:
							Correct=Label(Homepage,width=10,text="Correct",bg='white',fg='green')
							Correct.grid(row=7,column=3,rowspan=2)
							MathScore+=1
							Score=Label(Homepage,width=5,text=str(MathScore)+"/10",bg='#004999',fg='#edc967')
							Score.grid(row=13,column=3,rowspan=2)

						else:
							Incorrect=Label(Homepage,width=10,text="Incorrect",bg='white',fg='red')
							Incorrect.grid(row=7,column=3,rowspan=2)
							AnswerLabel=Label(Homepage,width=20,text="answer: "+str(answer),bg='#004999',fg='#edc967')
							AnswerLabel.grid(row=11,column=3,rowspan=2)

						currentOutput.config(state=NORMAL)
						currentOutput.delete(0,END)
						currentOutput.config(state=DISABLED)
						Next.config(state=NORMAL)

					def Next():
						if 'Instruction' in globals():
							Instruction.destroy()
						if 'Correct' in globals():
							Correct.destroy()
						if 'Incorrect' in globals():
							Incorrect.destroy()
						if 'AnswerLabel' in globals():
							AnswerLabel.destroy()	

						Next.config(state=DISABLED)
						currentOutput.config(state=NORMAL)

						global questionNumMath
						questionNumMath+=1
						if questionNumMath==1:
							start=time.time()
							
						if questionNumMath<=10:
							answer=NewMathQues()
							CheckButton=Button(Homepage,text="Check",command=lambda: Check(answer),bg='#004999',fg='#edc967')
							CheckButton.grid(row=4,column=3,rowspan=1)

						else:
							QuizConclude()



					Instruction = Label(Homepage, text="To start click 'Next Question'!",bg='#004999',fg='#edc967',width=41)
					Instruction.grid(row=0,column=0,columnspan=4)

					#Constructs button for the calculator
					one = Button(Homepage,text='1',command=lambda: Nums(1),bg='#004999',fg='#edc967',padx=35,pady=35)
					two = Button(Homepage,text='2',command=lambda: Nums(2),bg='#004999',fg='#edc967',padx=35,pady=35)
					three = Button(Homepage,text='3',command=lambda: Nums(3),bg='#004999',fg='#edc967',padx=35,pady=35)
					four = Button(Homepage,text='4',command=lambda: Nums(4),bg='#004999',fg='#edc967',padx=35,pady=35)
					five = Button(Homepage,text='5',command=lambda: Nums(5),bg='#004999',fg='#edc967',padx=35,pady=35)
					six = Button(Homepage,text='6',command=lambda: Nums(6),bg='#004999',fg='#edc967',padx=35,pady=35)
					seven = Button(Homepage,text='7',command=lambda: Nums(7),bg='#004999',fg='#edc967',padx=35,pady=35)
					eight = Button(Homepage,text='8',command=lambda: Nums(8),bg='#004999',fg='#edc967',padx=35,pady=35)
					nine = Button(Homepage,text='9',command=lambda: Nums(9),bg='#004999',fg='#edc967',padx=35,pady=35)
					zero = Button(Homepage,text='0',command=lambda: Nums(0),bg='#004999',fg='#edc967',padx=35,pady=35)
					clear = Button(Homepage, text='clear', command=clear, bg='#003d80',fg='#fc6a03', padx=21, pady=35)

					Next = Button(Homepage,text='Next Question',command=Next,bg='#004999',fg='#edc967', width=10)




					one.grid(row=10,column=0,rowspan=4)
					two.grid(row=10,column=1,rowspan=4)
					three.grid(row=10,column=2,rowspan=4)
					four.grid(row=6,column=0,rowspan=4)
					five.grid(row=6,column=1,rowspan=4)
					six.grid(row=6,column=2,rowspan=4)
					seven.grid(row=2,column=0,rowspan=4)
					eight.grid(row=2,column=1,rowspan=4)
					nine.grid(row=2,column=2,rowspan=4)
					zero.grid(row=14,column=1,rowspan=4)
					clear.grid(row=14, column=2, rowspan=4)
					Next.grid(row=3,column=3, rowspan=1)	

				def QuizConclude(): #In the works
					global subject
					EndTimer=time.time()
					#Add more, Timer stuff
					quizTime=(EndTimer-StartTimer)
					quizAvgTime=(EndTimer)/10
					if subject == "English":
						f=open("SavedEnglish.py", "w")
						f.write("\n"+"EnglishAvgTime = " + str(quizAvgTime)+"\n")
						f.close()
						importlib.reload(SavedEnglish)
						global engAvgTime
						engAvgTime=SavedEnglish.EnglishAvgTime

					elif subject == "History":
						f=open("SavedHistory.py", "w")
						f.write("\n" + "HistoryAvgTime = "+str(quizAvgTime)+"\n")
						f.close()
						importlib.reload(SavedHistory)
						global hisAvgTime
						hisAvgTime=SavedHistory.HistoryAvgTime
					elif subject == "Science":
						f=open("SavedScience.py", "w")
						f.write("\n" + "ScienceAvgTime = "+str(quizAvgTime)+"\n")
						f.close()
						importlib.reload(SavedScience)
						global sciAvgTime
						sciAvgTime=SavedScience.ScienceAvgTime
					elif subject == "CS":
						f=open("SavedCs.py", "w")
						f.write("\n" + "CSAvgTime = "+str(quizAvgTime)+"\n")
						f.close
						importlib.reload(SavedCs)
						global cSAvgTime
						cSAvgTime=SavedCs.CSAvgTime
					elif subject == "Math":
						f=open("SavedMath.py", "w")
						f.write("\n MathAvgTime = "+str(quizAvgTime)+"\n")
						f.close
						importlib.reload(SavedMath)
						mathAvgTime=SavedMath.MathAvgTime
					timeLabel=Label(Homepage,text="Your time has been saved you can now calculate how long it will take you to do your"+str(subject)+"homework!")
					Okay= Button(Homepage,"text=Got It!", command=Home())
					timeLabel(row=0,column=0,columnspan=3)
					Okay.grid(row=1,column=2)

					#Results
					#print("\nYou got {}/10 questions correct".format(correct))
					#secs = int(mathTime % 60)
					#mins = int((mathTime-secs) // 60)
					#hours = int((mathTime // 60) // 60)
					#print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
					#AvgMath = int(mathTime/10)
					#avgSecs = int(AvgMath % 60)
					#avgMins = int((AvgMath-avgSecs) // 60)
					#avgHours = int((AvgMath // 60) // 60)
					#print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))

				QuizSubjectChoiceLabel = Label(
					Homepage,
					text="What subject do you want to test?",
					bg='#004999',
					fg='#edc967')
				MathChoice = Button(Homepage,text='Math Quiz',command=MathQuiz(),bg='#004999',fg='#edc967')
				EnglishChoice = Button(Homepage,text='English Quiz',command=EnglishQuiz,bg='#004999',fg='#edc967')
				HistoryChoice = Button(Homepage,text='History Quiz',command=HistoryQuiz,bg='#004999',fg='#edc967')
				ScienceChoice = Button(Homepage,text='Science Quiz',bg='#004999',fg='#edc967')
				CsChoice = Button(Homepage,text='Computer Science Quiz',command=CSQuiz,bg='#004999',fg='#edc967')
				Exit = Button(Homepage,text='Exit',command=Home,bg='#003d80',fg='#fc6a03')

				#MathChoice.grid(row=1,column=0)
				EnglishChoice.grid(row=1, column=0)
				HistoryChoice.grid(row=2, column=0)
				ScienceChoice.grid(row=3, column=0)
				CsChoice.grid(row=4, column=0)
				Exit.grid(row=5, column=0)


			#Creating category widgetsHoHomepage
			GetRouteLabel = Label(
				Homepage,
				text=
				"Would you like to: calculate Homework time, re-take quiz, change name, or quit?",
				bg='#004999',
				fg='#edc967')
			GetTimeButton = Button(Homepage,
				text="Time",
				width=5,
				command=Time,
				bg='#003d80',
				fg='#edc967')
			GetReQuizButton = Button(Homepage,
				text="Quiz",
				width=5,
				command=Quiz,
				bg='#003d80',
				fg='#edc967')
			GetReNameButton = Button(Homepage,
				text="Name",
				width=5,
				command=ChangeName,
				bg='#003d80',
				fg='#edc967')
			GetQuitButton = Button(Homepage,
				text="Quit",
				width=5,
				command=Quit,
				bg='#003d80',
				fg='#edc967')

			#Open category widgetsHomepagehome
			GetRouteLabel.grid(row=4, column=0, columnspan=30)
			GetTimeButton.grid(row=5, sticky=W)
			GetReQuizButton.grid(row=6, sticky=W)
			GetReNameButton.grid(row=7, sticky=W)
			GetQuitButton.grid(row=8, sticky=W)

			Homepage.mainloop()
