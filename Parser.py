class Parser(object):
	
	def __init__(self, fileName):
		"""Opens the input file/stream and gets ready to parse it"""
		self.fh = open(fileName, 'r')
		self.currentLine = ''
		
	def has_more_commands(self):
		"""
		Returns a Boolean
		Indicates if there are more commands in the file
		"""
		i = self.fh.tell()
		c = self.fh.read()
		self.fh.seek(i)
		return c
		
	def advance(self):
		"""
		Reads the next command from the input and makes it the current 
		command. Should ve called only if has_more_commands() is True. 
		Inittially there is no current command.
		"""
		line = ''
		while not line:
			line = self.fh.readline()
			line = line.split('//')[0]
			line = line.rstrip('\n ').lstrip(' ')
		self.currentLine = line
		
	def command_type(self):
		"""
		Returns a string that represents the type of the command:
		A - A command
		C - C Command
		L - L Command
		"""
		if self.currentLine[0] == '@':
			return 'A'
		elif self.currentLine[0] == '(':
			return 'L'
		else:
			return 'C'
		
	def symbol(self):
		"""
		Returns a string that represents the symbol or decimal Xxx of the 
		current command @Xxx or (Xxx). Should be called only when command_type()
		is A_COMMAND or L_COMMAND.
		"""
		s = self.currentLine.lstrip('@ (').rstrip(' )')
		return s
		
	def dest(self):
		"""
		 Returns a string that is the dest mnemonic in the current C-command 
		 (8 possibilities). Should be called only when command_type() is 
		 C_COMMAND.
		"""
		if '=' in self.currentLine:
			return self.currentLine.split('=')[0]
		else:
			return ''
		
	def comp(self):
		"""
		Returns the comp mnemonic in the current C-command (28 possibilities). 
		Should be called only when command_type() is C_Command.
		"""
		if '=' in self.currentLine:
			comp = self.currentLine.split('=')[1]
			if ';' in self.currentLine:
				comp = self.curretLine.split(';')[0]
		else:
			comp = self.currentLine.split(';')[0]
		return comp

	def jump(self):
		"""
		Returns the comp mnemonic in the crrent C-command (8 possibilities). 
		Should be called only when command_type() is C_command.
		"""
		if ';' in self.currentLine:
			return self.currentLine.split(';')[1]
		else:
			return ''
			
	def close(self):
		"""
		Close file
		"""
		self.fh.close()
		
	
