import ply.lex as lex
import sys

#Lista de Tokens

tokens = (
	#Palabras Claves.
	'ID', 'PRINT', 'FUNC', 'RETURN', 'BEGIN', 'THEN',
	'END', 'READ', 'WRITE',
	#Control de Flujo
	'IF', 'ELSE', 'WHILE', 'BREAK', 'SKIP', 'DO',
	#Operadores y delimitadores
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
	'SEMI', 'LPAREN', 'RPAREN', 'COMMA', 'COLON',
	'LBRACKET','RBRACKET',
	#Operaciones Booleanas
	'LT', 'LE', 'GT', 'GE', 'LAND', 'LOR', 'LNOT',
  	'EQ', 'NE',
  	#Literales
  	'INTEGER', 'FLOAT', 'STRING',
  	#Tipo de Dato
  	'TYPENAME',
)

#Ignorando la indentacion y espacios.
t_ignore =' \t'

#Definiendo simbolos simples.
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r':='
t_SEMI      = r';'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_LT        = r'<'
t_LE        = r'<='
t_EQ        = r'=='
t_GE        = r'>='
t_GT        = r'>'
t_NE        = r'!='
t_LAND      = r'and'
t_LOR       = r'or'
t_LNOT      = r'not'
t_COLON     = r':'

#Definiento tipo de dato.
def t_TYPENAME(t):
  r'\b(int|bool|float|var)\b'
  return t

#Definiendo el tipo de dato Flotante
def t_FLOAT(t):
	r'(?:(?:\d*\.\d+|\d+\.\d*)(?:[eE][-+]?\d+)?)|(?:\d+[eE][-+]?\d+)'
	t.value = float(t.value)
	return t

#Definiendo el tipo de dato Entero
def t_INTEGER(t):
  r'(?:0[xX]?)?\d+'
  #Si ingresa un numero en base 16
  if t.value.startswith(('0x','0X')):
    t.value = int(t.value,16)
  #Si ingresa un numero en base 8             
  elif t.value.startswith('0'):
    t.value = int(t.value,8)
  #Si ingresa un numero en base 10
  else:
    t.value = int(t.value)
  return t

#Definiento el tipo de dato String
def t_STRING(t):
  r'".*?"'
  return t

#Tipo de dato Booleano
def t_BOOLEAN(t):
  r'\b(true|false)\b'
  t.value = True if t.value=='true' else False
  return t

#Una o mas Lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Comentarios Pascal
def comments(t):
	r'{(.|\n)*?}'
	t.lexer.lineno += t.value.count('\n')
	return t

#Manejo de Errores
def t_error(t):
	print( "Caracter Ilegal: " + str(t.value[0]) )
	t.lexer.skip(1)

#Definiendo Palabras Reservadas
def t_IF(t):
	r'IF'
	return t
def t_ELSE(t):
	r'ELSE'
	return t
def t_WHILE(t):
	r'WHILE'
	return t
def t_CONST(t):
	r'CONST'
	return t
def t_FUNC(t):
	r'FUNC'
	return t
def t_PRINT(t):
	r'PRINT'
	return t
def t_BEGIN(t):
	r'BEGIN'
	return t
def t_END(t):
	r'END'
	return t
def t_THEN(t):
	r'THEN'
	return t
def t_BREAK(t):
	r'BREAK'
	return t
def t_READ(t):
	r'READ'
	return t
def t_WRITE(t):
	r'WRITE'
	return t
def t_RETURN(t):
	r'RETURN'
	return t
def t_SKIP(t):
	r'SKIP'
	return t
def t_DO(t):
	r'DO'
	return t

#Definiento Palabra clave ID
def t_ID(t):
  r'[a-zA-Z_]\w*'
  return t

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