def enthaeltWhile(quelltext):
    gefunden = False
    while len(quelltext) > 0:
        pos = quelltext.find("'")
        quelltextVorHochkomma = quelltext[:pos]
        quelltext = quelltext[pos:]
        if 'while' in quelltextVorHochkomma:
            gefunden = True
        quelltext = quelltext[1:]
        pos = quelltext.find("'")
        quelltext = quelltext[(pos+1):]   
    return gefunden

# Test
quelltextTest = """
def test( ):
    print('while')

"""
print(enthaeltWhile(quelltextTest))
