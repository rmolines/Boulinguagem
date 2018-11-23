
from lexer import Lexer
# from parser import Parser

text_input = """
main() {
    x = 6;
    y = 4;
    wahren(y<x){
        y=y+1
        lehre(z);
        ob (y<z){
            schreibe(z);
        } sonst {
            schreibe(24);
        }
    }
}

main();"""

    
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)

# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens).eval()