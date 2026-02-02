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

        if self.existe_usuario(usuario_limpo["nome"], usuario_limpo["dificuldade"]):
            self.salva_user(self.conteudo)
            return
        self.conteudo.append(usuario_limpo)
        self.salva_user(self.conteudo)
        return
    def encontra_menor(self, lista):
        menor = lista[0]["score"]
        indice = lista[0]
        for n in range(len(lista)):
            if lista[n]["score"]<menor:
                menor = lista[n]["score"]
                indice = lista[n]
        lista.remove(indice)
        return indice
    def mostra_scores(self):
        facil = [a for a in self.conteudo if a["dificuldade"]=="facil"]
        dificil = [a for a in self.conteudo if a["dificuldade"]=="dificil"]

        facil.sort(key=lambda lista: lista["score"])
        dificil.sort(key=lambda lista: lista["score"])

        print(f"\033[0;32mFacil\033[m {' '*25}\033[0;31mDificil\033[m")
        for i in range(max(len(facil),len(dificil))):
            linha = ""
            if i < len(facil):
                if i==0:
                    linha += f"\033[1;33m{i+1}° - {facil[i]["nome"]} ({facil[i]["score"]} pts)\033[m"
                elif i==1:
                    linha += f"\033[0;37m{i+1}° - {facil[i]["nome"]} ({facil[i]["score"]} pts)\033[m"
                elif i==2:
                    linha += f"\033[0;33m{i+1}° - {facil[i]["nome"]} ({facil[i]["score"]} pts)\033[m"
                else:
                    linha += f"{i+1}° - {facil[i]["nome"]} ({facil[i]["score"]} pts)"

            else:
                linha += " " * 30

            linha += "\t"
            if i < len(dificil):
                if i==0:
                    linha += f"\033[1;33m{i+1}° - {dificil[i]['nome']} ({dificil[i]['score']} pts)\033[m"
                elif i==1:
                    linha += f"\033[0;37m{i+1}° - {dificil[i]['nome']} ({dificil[i]['score']} pts)\033[m"
                elif i==2:
                    linha += f"\033[0;33m{i+1}° - {dificil[i]['nome']} ({dificil[i]['score']} pts)\033[m"
                else:
                    linha += f"{i+1}° - {dificil[i]['nome']} ({dificil[i]['score']} pts)"

            print(linha)
    def mostra_posicao(self, jogador, toques, dificuldade):
        for n in range(len(self.conteudo)):
            if self.conteudo[n]["nome"]==jogador and self.conteudo[n]["score"]==toques and self.conteudo[n]["dificuldade"]==dificuldade:
                print(f"O jogador: {jogador} esta na {n+1}° posição")



        
