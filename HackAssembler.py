from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys

def main():
	parser = Parser(sys.argv[1])
	code = Code()
	name = sys.argv[1].split('.')[0] + '.hack'
	symbolTable = SymbolTable()
	out = open(name, 'w')
	lineCount = 0
	address = 16
	
	#first pass
	while(parser.has_more_commands()):
		parser.advance()
		if parser.command_type() == 'L':
			symbolTable.add_entry(parser.symbol(), to_bin(lineCount))
		else:
			lineCount += 1
		
	parser = Parser(sys.argv[1])
	
	#second pass
	while(parser.has_more_commands()):
		parser.advance()
		if parser.command_type() == 'A':
			s = parser.symbol()
			if is_number(s):
				out.write('0' + to_bin(s))
				out.write('\n')
			elif symbolTable.contains(s):
				out.write('0' + symbolTable.get_adress(s))
				out.write('\n')
			else:
				symbolTable.add_entry(s, to_bin(address))
				out.write('0' + to_bin(address))
				out.write('\n')
				address += 1
				
		elif parser.command_type() == 'C':
			d = parser.dest()
			c = parser.comp()
			j = parser.jump()
			out.write('111' + code.comp(c) + code.dest(d) + code.jump(j))
			out.write('\n')
	
	parser.close()
	out.close()

def to_bin(number):
		number = int(number) + 32768
		bNumber = bin(number).split('b')[1]
		bNumber = list(bNumber)
		bNumber = ''.join(bNumber[1:])
		return bNumber

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
	
if __name__ == '__main__':
	main()
