import os
import json
class Score():
    def __init__(self, caminho) -> None:
        self.caminho = caminho
        if not os.path.exists(caminho):
            self.conteudo= []
        else:
            self.conteudo = json.load(open(caminho, "r"))
    def salva_user(self, lista):
        file = open(self.caminho, "w")
        json.dump(lista, file, indent=4)
    def existe_usuario(self, nome):
        file = self.conteudo
        for n in file:
            if n["nome"]==nome:
                return True
            else:
                return False
    def add_user(self, usuario: dict):
        # usuarios = self.conteudo
        # if Score.existe_usuario(self, nome= usuario["nome"]):
        #     for n in usuarios:
        #         if n["nome"]==usuario["nome"]:
        #             n["score"] = usuario["score"]
        # else:
        #     usuarios.append(usuario)
        # Score.salva_user(self, lista=usuarios)
        usuario_limpo = {
            "nome": str(usuario["nome"]),
            "score": int(usuario["score"])
        }

        for u in self.conteudo:
            if u["nome"] == usuario_limpo["nome"]:
                u["score"] = usuario_limpo["score"]
                Score.salva_user(self, lista=self.conteudo)
                return

        self.conteudo.append(usuario_limpo)
        Score.salva_user(self, lista=self.conteudo)

class Home():
    def __init__(self) -> None:
        pass
