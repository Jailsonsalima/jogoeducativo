mapa = [
    [0, 0, 0, 1, 9],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

def executar_comandos(comandos):
    posicao = [3, 0]  # posição inicial
    resultado = {"status": "em_andamento", "posicao": posicao}

    for comando in comandos:
        if comando.startswith("go"):
            direcao, passos = comando.replace("go(", "").replace(")", "").split(",")
            direcao = direcao.strip("' ")
            passos = int(passos)

            for _ in range(passos):
                if direcao == "up":
                    posicao[0] -= 1
                elif direcao == "down":
                    posicao[0] += 1
                elif direcao == "left":
                    posicao[1] -= 1
                elif direcao == "right":
                    posicao[1] += 1

                # Verificações
                if posicao[0] < 0 or posicao[0] >= len(mapa) or posicao[1] < 0 or posicao[1] >= len(mapa[0]):
                    resultado["status"] = "caiu_no_rio"
                    return resultado

                if mapa[posicao[0]][posicao[1]] == 1:
                    resultado["status"] = "bateu_obstaculo"
                    return resultado

                if mapa[posicao[0]][posicao[1]] == 9:
                    resultado["status"] = "chegou_objetivo"
                    return resultado

    resultado["posicao"] = posicao
    return resultado
