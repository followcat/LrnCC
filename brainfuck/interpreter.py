import os
import sys

import bflexer
import bfparser


class Tape(object):
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]

    def set(self, val):
        self.thetape[self.position] = val

    def inc(self, value):
        self.thetape[self.position] += value

    def dec(self, value):
        self.thetape[self.position] -= value

    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)

    def devance(self):
        self.position -= 1

    def execloop(self, parsed, jump_map):
        pc = 0
        while pc < len(parsed):
            code, value = parsed[pc]
            if code == ">":
                self.advance()
            elif code == "<":
                self.devance()
            elif code == "+":
                self.inc(value[0])
            elif code == "-":
                self.dec(value[0])
            elif code == ".":
                os.write(1, chr(self.get()))
            elif code == ",":
                self.set(ord(os.read(0, 1)[0]))
            elif code == "[" and self.get() == 0:
                pc = jump_map[pc]
            elif code == "]" and self.get() != 0:
                pc = jump_map[pc]
            pc += 1


def run(fp):
    program_contents = ""
    while True:
        read = fp.read()
        if len(read) == 0:
            break
        program_contents += read
    fp.close()
    tokens = bflexer.lexer.lex(program_contents)
    parser = bfparser.Parser()
    parser.parse(tokens)
    tape = Tape()
    tape.execloop(parser.parsed, parser.jump_map)


def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print("You must supply a filename")
        return 1
    run(open(filename))
    return 0


def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
