import rply


lg = rply.LexerGenerator()
lg.add('ADVANCE', r'\>')
lg.add('DEVANCE', r'\<')
lg.add('INC', r'\+')
lg.add('DEC', r'\-')
lg.add('STDOUT', r'\.')
lg.add('STDIN', r'\,')
lg.add('FORWARD', r'\[')
lg.add('BACK', r'\]')

lg.ignore(r'[^\+\-\,\.\[\]\>\<]')

lexer = lg.build()
