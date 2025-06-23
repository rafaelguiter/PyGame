def calcular_max_lixos(fase):
    return 10 + (fase - 1) * 5

def desbloquear_proxima_fase(fases_desbloqueadas, fase_atual, acertos, max_lixos):
    if (acertos / max_lixos) >= 0.9 and fase_atual < len(fases_desbloqueadas):
        fases_desbloqueadas[fase_atual] = True
        return True
    return False