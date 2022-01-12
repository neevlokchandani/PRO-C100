class PrintArry():
	def __init__(self,arry,number,letter,word):
		self.arry = arry
		self.number = number
		self.letter = letter
		self.word = word
	
	def Print_arry(self,arry):
		print(self.arry)
	def Print_number(self,number):
		print(self.number)
	def Print_letter(self,letter):
		print(self.letter)
	def Print_word(self):
		print(self.word)
	


test = PrintArry(['neev','lokchandani'],[0,1,2,3,4,5,6,7],'n','done')

print(test.Print_word)
