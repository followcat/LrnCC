What is PLY?
---------------------------
PLY is an implementation of lex and yacc parsing tools for Python. If you don't have the slightest idea what that means, you're probably in the wrong place. Otherwise, keep reading.

In a nutshell, PLY is nothing more than a straightforward lex/yacc implementation. Here is a list of its essential features:

    It's implemented entirely in Python.
    It uses LR-parsing which is reasonably efficient and well suited for larger grammars.
    PLY provides most of the standard lex/yacc features including support for empty productions, precedence rules, error recovery, and support for ambiguous grammars.
    PLY is straightforward to use and provides very extensive error checking.
    PLY doesn't try to do anything more or less than provide the basic lex/yacc functionality. In other words, it's not a large parsing framework or a component of some larger system.

[Go to PLY website.](http://www.dabeaz.com/ply/ "PLY")

What is rply?
---------------------------
A pure python parser generator, that also works with RPython. It is a more-or-less direct port of David Beazley's awesome PLY, with a new public API, and RPython support.

[Get rply in github.](https://github.com/alex/rply "rply")
