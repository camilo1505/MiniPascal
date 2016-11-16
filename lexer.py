import ply.lex as lex
import sys


tokens = (
	#PALABRAS RESERVADAS
    'ARRAY','BEGIN','VAR','USES','END','PROGRAM','CONST','STRING',
    #I/O
    'WRITE','READ','WRITELN','READLN',
	#CICLOS
    'WHILE','DO','FOR','TO','DOWNTO','REPEAT','UNTIL','BREAK',
	#CONDICIONES
	'IF','THEN','ELSE','CASE','OF',

    #FUNCIONES
    'FUNCTION','RETURN',

    #SIMBOLOS

    'MAS','MENOS','POR','DIV','ASIG','PUNTO','PCOMA','DPUN','COMA','EQ','LT','LE','GT','GE','PARI','PARD',
    'CORI','CORD','LLAVEI','LLAVED','NOT','DIF','OR','AND',
    #OTROS
    'ID','CNUM','NUM','INT','STR','CHAR','BOOL','FLOAT'
)

#Regular expressions and simple tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_ASIG = r':='
t_PUNTO = r'\.'
t_PCOMA = r';'
t_DPUN = r':'
t_COMA = r'\,'
t_EQ = r'='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_PARI = r'\('
t_PARD = r'\)'
t_CORI = r'\['
t_CORD = r'\]'
t_LLAVEI = r'{'
t_LLAVED = r'}'
t_DIF = r'!='
t_ignore = ' \t'


def t_ARRAY(t):
	r'ARRAY|array'
	return t

def t_RETURN(t):
	r'RETURN|return'
	return t

def t_BREAK(t):
	r'BREAK|break'
	return t

def t_BEGIN(t):
	r'BEGIN|begin'
	return t

def t_VAR(t):
	r'VAR|var'
	return t

def t_USES(t):
	r'USES|uses'
	return t

def t_END(t):
	r'END|end'
	return t

def t_PROGRAM(t):
	r'PROGRAM|program'
	return t

def t_CONST(t):
	r'CONST|const'
	return t

def t_WRITELN(t):
	r'WRITELN|writeln'
	return t

def t_READLN(t):
	r'READLN|readln'
	return t

def t_WRITE(t):
	r'WRITE|write'
	return t

def t_READ(t):
	r'READ|read'
	return t

def t_WHILE(t):
	r'WHILE|while'
	return t

def t_DO(t):
	r'DO|do'
	return t

def t_FOR(t):
	r'FOR|for'
	return t

def t_DOWNTO(t):
	r'DOWNTO|downto'
	return t

def t_REPEAT(t):
	r'REPEAT|repeat'
	return t

def t_UNTIL(t):
	r'UNTIL|until'
	return t

def t_IF(t):
	r'IF|if'
	return t

def t_THEN(t):
	r'THEN|then'
	return t

def t_ELSE(t):
	r'ELSE|else'
	return t

def t_CASE(t):
	r'CASE|case'
	return t

def t_OF(t):
	r'OF|of'
	return t

def t_FUNCTION(t):
	r'FUNCTION|function'
	return t

def t_AND(t):
	r'and|AND'
	return t

def t_NOT(t):
	r'NOT|not'
	return t

def t_OR(t):
	r'OR|or'
	return t

def t_CHAR(t):
	r'CHAR|char'
	return t

def t_FLOAT(t):
	r'FLOAT|float'
	return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_CNUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_INT(t):
	r'integer|INTEGER'
	return t

def t_STR(t):
	r'STRING|string'
	return t

def t_BOOL(t):
	r'BOOLEAN|boolean'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
	r'(\'|\").*(\'|\")'
	return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_TO(t):
	r'TO|to'
	return t

def t_comments(t):
    r'{(.|\n)*?}'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()


if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
