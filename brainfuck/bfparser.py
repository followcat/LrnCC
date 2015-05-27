import rply


pg = rply.ParserGenerator(
    [
        'ADVANCE', 'DEVANCE',
        'INC', 'DEC',
        'STDOUT', 'STDIN',
        'FORWARD', 'BACK',
    ])


class Parser(object):
    def __init__(self):
        self.parser = parser
        self.parsed = []
        self.jump_map = {}
        self.leftstack = []

    def step(self, token, value=0):
        return (token.getstr(), [value])

    def parse(self, tokens):
        self.parser.parse(tokens, state=self)

    @pg.production('expr : INC')
    @pg.production('expr : DEC')
    def first_incdec(self, p):
        step = self.step(p[0], 1)
        self.parsed.append(step)

    @pg.production('expr : expr INC')
    @pg.production('expr : expr DEC')
    def incdec(self, p):
        step = self.step(p[1], 1)
        self.parsed.append(step)

    @pg.production('expr : ADVANCE')
    def first_adv(self, p):
        step = self.step(p[0])
        self.parsed.append(step)

    @pg.production('expr : expr ADVANCE')
    @pg.production('expr : expr DEVANCE')
    def advdev(self, p):
        step = self.step(p[1])
        self.parsed.append(step)

    @pg.production('expr : expr FORWARD')
    def forward(self, p):
        self.leftstack.append(len(self.parsed))
        step = self.step(p[1])
        self.parsed.append(step)

    @pg.production('expr : expr BACK')
    def back(self, p):
        left = self.leftstack.pop()
        right = len(self.parsed)
        self.jump_map[left] = right
        self.jump_map[right] = left
        step = self.step(p[1])
        self.parsed.append(step)

    @pg.production('expr : STDOUT')
    @pg.production('expr : STDIN')
    def first_stdinout(self, p):
        step = self.step(p[0])
        self.parsed.append(step)

    @pg.production('expr : expr STDOUT')
    @pg.production('expr : expr STDIN')
    def stdinout(self, p):
        step = self.step(p[1])
        self.parsed.append(step)

parser = pg.build()
