import geradorJava, geradorPython, geradorR
import shutil
import gabaritos
import classes

class PaginaPrincipal:

    def __init__(self):
        self.modelo = 'graph.gv'
        self.gerarPython()

    def gerarPython(self):
            py = geradorPython.GeradorPython(self.modelo)
            py.principal()
            name = py.nome()
            self.save(name)
            
    def gerarJava(self):
            java = geradorJava.GeradorJava(self.modelo)
            java.principal()
            name = java.nome()
            self.save(name)
    
    def gerarR(self):

            r = geradorR.GeradorR(self.modelo)
            r.principal()
            name = r.nome()
            self.save(name) 
        
    def save(self, name):
        print("entrou no save")
        files = [('R Files', '*.R'), 
             ('Python Files', '*.py'),
             ('Java Files', '*.java')]
        c = open('codigo/'+ name, 'r')
        codigo = c.readlines()
        arquivo = open('codigosalvo.py', "w+")
        arquivo.writelines(codigo)
        c.close()
        arquivo.close()
       
if __name__ == "__main__":
        PaginaPrincipal()

