import ply.lex as lex
import sys
import re

file = open("read.py")

# Diccionario de palabras reservadas
reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'True': 'TRUE',
    'False': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

# Lista de tokens
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMI',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'DOUBLE_EQUAL',
    'NOT_EQUAL',
] + list(reservadas.values())

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_SEMI = r';'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_DOUBLE_EQUAL = r'=='
t_NOT_EQUAL = r'!='

# Expresiones regulares con acciones asociadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de espacios en blanco y comentarios
def t_whitespace(t):
    r'\s+'
    pass

def t_comment(t):
    r'\#.*'
    pass

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}, posición {t.lexpos}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
contents = file.read()
print("Analizador Léxico")
print("----------------------------------")

count=0
program = contents.split("\n")
print("Archivo leido\n",contents)
print("----------------------------------")
print("Division en tokens")
for line in program:
    count = count + 1
    tokens=line.split(' ')
    print("Linea ",count, " Tokens: ",tokens)

# Leer archivo de texto
#filename = 'read.py'
#with open(filename, "r") as file:
    #contents = file.read()
    #tokens=line.split(' ')
    #print("Los tokens son:" , tokens)
    

# Análisis léxico
print("\n CLASIFICACION DE TOKENS \n")
lexer.input(contents)
for tok in lexer:
    print(f"Linea {tok.lineno:3} Posicion {tok.lexpos:3} Tipo {tok.type:16} Valor {tok.value:10}")
