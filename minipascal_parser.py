import ply.yacc as yacc
from minic_lexer import tokens
import minic_lexer
import sys

program : function
		| program function

function : FUN ID arguments locals BEGIN statements END

arguments : LPAREN RPAREN
		  | LPAREN declaration_variables RPAREN

declaration_variables : param
					  | declaration_variables COMMA param

param : ID COLON type
	  | ID COLON ID

locals : dec_list SEMICOLON
	   | empty

dec_list : var_dec
		 | dec_list SEMICOLON var_dec

var_dec : param
		| function

type : INT
	 | FLOAT
	 | INT LBRACKET expression RBRACKET
	 | FLOAT LBRACKET expression RBRACKET

staments : stament
         | staments SEMICOLON statement

stament : WHILE relation DO stament				#while
		| IF relation THEN stament else 		#if
		| ID COLONEQUAL expression 				#assign
		| PRINT LPARENT TEXT RPARENT 			#print
		| WRITE LPARENT expression RPARENT 		#write
		| READ LPARENT location_read RPARENT	#read
		| RETURN expression 					#return
		| ID LPARENT expression RPARENT			#call function
		| SKIP SEMICOLON						#skip
		| BREAK SEMICOLON						#break
		| BEGIN staments END					#begin end
				
else : ELSE stament
	 | empty

location_read : ID
			  | ID LBRACKET expression RBRACKET

expression : expression PLUS expression
		   | expression DIVIDE expression
		   | expression MULT expression
		   | expression MINUS expression
		   | MINUS expression
		   | LPARENT expression RPARENT
		   | ID LPARENT expression_list RPARENT
		   | ID
		   | ID LBRACKET expression RBRACKET
		   | INUMERO
		   | FNUMERO
		   | INT LPARENT expression RPARENT
		   | FLOAT LPARENT expression RPARENT


expression_list : expresion
			    | expresion COMMA expression
			    | #empty


relation : expression GREATER expression
		 | expression LESS expression
		 | expression GREATEREQUAL expression
		 | expression LESSEQUAL expression
		 | expression DISTINT expression
		 | expression NOT expression
		 | expression OR expression
		 | expression AND expression
		 | NOT expression
		 | LPARENT expression RPARENT 