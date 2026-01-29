import os
import json
class Score():
    def __init__(self, caminho) -> None:
        self.caminho = caminho
        if os.path.exists(caminho) and os.path.getsize(caminho)<1:
            self.conteudo= []
        elif not os.path.exists(caminho):
            self.conteudo = []
        else:
            self.conteudo = json.load(open(caminho, "r"))


    def salva_user(self, lista):
        file = open(self.caminho, "w")
        json.dump(lista, file, indent=4)
        file.close()


    def existe_usuario(self, nome):
        file = self.conteudo
        for n in file:
            if n["nome"]==nome:
                return True
            else:
                return False
            

    def add_user(self, usuario: dict):
        usuario_limpo = {
            "nome": str(usuario["nome"]),
            "score": int(usuario["score"])
        }

        for u in self.conteudo:
            if u["nome"] == usuario_limpo["nome"]:
                if u["score"]< usuario_limpo["score"]:
                    u["score"] = usuario_limpo["score"]
                    self.salva_user(self.conteudo)
                    return
                self.salva_user(self.conteudo)
                return

        self.conteudo.append(usuario_limpo)
        self.salva_user(self.conteudo)

        
