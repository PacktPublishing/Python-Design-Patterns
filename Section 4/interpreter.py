class Expression:
    def interpret(self, text): pass


class TerminalExpression(Expression):
    def __init__(self, word):
        self.word = word

    def interpret(self, text):
        words = text.split()
        if self.word in text:
            return True
        else:
            return False


class OrExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) or self.exp2.interpret(text)


class AndExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def interpret(self, text):
        return self.exp1.interpret(text) and self.exp2.interpret(text)


john = TerminalExpression('John')
henry = TerminalExpression('Henry')
mary = TerminalExpression('Mary')
sarah = TerminalExpression('Sarah')

# construct the rule sarah and (mary or (john and henry))
