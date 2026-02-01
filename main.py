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


    def existe_usuario(self, nome, dificuldade):
        file = self.conteudo
        for n in file:
            if n["nome"]==nome and n["dificuldade"]==dificuldade:
                return True
        return False
    def existe_nome(self, nome):
        for u in self.conteudo:
            if u["nome"] == nome:
                return True
        return False
            

    def add_user(self, usuario: dict):
        usuario_limpo = {
            "nome": str(usuario["nome"]),
            "score": int(usuario["score"]),
            "dificuldade": str(usuario["dificuldade"])
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
    def mostra_scores(self):
        facil = []
        dificil = []
        for a in self.conteudo:
            if a["dificuldade"]=="facil":
                facil.append(a)
            else:
                dificil.append(a)

        print(f"\033[0;32mFacil\033[m {' '*25}\033[0;31mDificil\033[m")
        for i in range(max(len(facil),len(dificil))):
            linha = ""
            if i < len(facil):
                linha += f"{i+1}° - {facil[i]['nome']} ({facil[i]['score']} pts)"
            else:
                linha += " " * 30

            linha += "\t"
            if i < len(dificil):
                linha += f"{i+1}° - {dificil[i]['nome']} ({dificil[i]['score']} pts)"

            print(linha)



        
