#!/usr/bin/env python3
"""
Máquina Norma - interpretador simples.

Este programa lê um arquivo .txt com instruções rotuladas da Máquina Norma:

  N ADD R PROX
  N SUB R PROX
  N ZER R LINHA_SE_ZERO LINHA_SE_NAO_ZERO

Onde:
- ADD soma 1 em um registrador.
- SUB subtrai 1 de um registrador, sem deixar negativo.
- ZER testa se um registrador está zerado.
- A execução termina quando o próximo rótulo não existe.
"""

import argparse
from pathlib import Path

REGS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

class Instrucao:
    def __init__(self, rotulo, op, reg, j1, j2=None, bruto=''):
        self.rotulo = int(rotulo)
        self.op = op.upper()
        self.reg = reg.upper()
        self.j1 = int(j1)
        self.j2 = int(j2) if j2 is not None else None
        self.bruto = bruto.strip()

def carregar_programa(caminho):
    programa = {}

    for n_linha, linha in enumerate(Path(caminho).read_text(encoding='utf-8').splitlines(), 1):

        limpa = linha.split('#', 1)[0].strip()

        if not limpa:
            continue

        partes = limpa.split()

        if len(partes) < 4:
            raise ValueError(f'Linha {n_linha} inválida: {linha}')

        rotulo, op, reg = partes[0], partes[1], partes[2]
        op = op.upper()

        if op in ('ADD', 'SUB'):
            if len(partes) != 4:
                raise ValueError(f'Linha {n_linha}: ADD/SUB devem ter 4 campos')

            inst = Instrucao(rotulo, op, reg, partes[3], bruto=limpa)

        elif op == 'ZER':
            if len(partes) != 5:
                raise ValueError(f'Linha {n_linha}: ZER deve ter 5 campos')

            inst = Instrucao(rotulo, op, reg, partes[3], partes[4], bruto=limpa)

        else:
            raise ValueError(f'Linha {n_linha}: operação inválida {op}. Use só ADD, SUB ou ZER.')

        if inst.rotulo in programa:
            raise ValueError(f'Rótulo repetido: {inst.rotulo}')

        programa[inst.rotulo] = inst

    return programa


def executar(caminho, valores, mostrar=None, inicio=1, traco=True, max_passos=1000000):
    programa = carregar_programa(caminho)

    regs = {r: 0 for r in REGS}

    for r, v in valores.items():
        r = r.upper()

        if r not in regs:
            regs[r] = 0

        if v < 0:
            raise ValueError('A Máquina Norma trabalha com números naturais; não use negativos.')

        regs[r] = int(v)
        
    pc = inicio
    
    passos = 0

    if traco:
        print(f'{estado(regs, mostrar)} , M) Entrada de Dados')

    while pc in programa:

        if passos >= max_passos:
            raise RuntimeError(f'Limite de passos atingido ({max_passos}). Talvez haja loop infinito ou entrada inválida.')

        inst = programa[pc]

        if traco:
            print(f'{estado(regs, mostrar)} , {inst.rotulo}) {texto_instrucao(inst)}')

        if inst.op == 'ADD':
            regs[inst.reg] = regs.get(inst.reg, 0) + 1
            pc = inst.j1

        elif inst.op == 'SUB':
            regs[inst.reg] = max(0, regs.get(inst.reg, 0) - 1)
            pc = inst.j1

        elif inst.op == 'ZER':
            pc = inst.j1 if regs.get(inst.reg, 0) == 0 else inst.j2

        passos += 1

    if traco:
        print(f'{estado(regs, mostrar)} , FIM) Próximo rótulo {pc} não existe. Execução encerrada.')

    return regs, passos

def texto_instrucao(inst):
    if inst.op == 'ADD':
        return f'FACA ADD({inst.reg}) VA_PARA {inst.j1}'

    if inst.op == 'SUB':
        return f'FACA SUB({inst.reg}) VA_PARA {inst.j1}'

    return f'SE ZER({inst.reg}) ENTAO VA_PARA {inst.j1} SENAO VA_PARA {inst.j2}'


def estado(regs, mostrar=None):
    mostrar = mostrar or REGS
    return '(' + ', '.join(f'{r}={regs.get(r, 0)}' for r in mostrar) + ')'


def parse_regs(texto):
    valores = {}

    if not texto:
        return valores

    for parte in texto.split(','):
        if not parte.strip():
            continue

        if '=' not in parte:
            raise ValueError('Use o formato A=2,B=3,C=0')

        r, v = parte.split('=', 1)
        valores[r.strip().upper()] = int(v.strip())

    return valores

def main():
    p = argparse.ArgumentParser(description='Executa programas da Máquina Norma.')

    p.add_argument('arquivo', help='arquivo .txt com instruções ADD/SUB/ZER')
    p.add_argument('--regs', default='', help='valores iniciais. Ex.: A=2,B=3')
    p.add_argument('--mostrar', default='A,B,C,D,E,F,G,H', help='registradores exibidos no traço')
    p.add_argument('--inicio', type=int, default=1, help='rótulo inicial')
    p.add_argument('--sem-traco', action='store_true', help='não imprime execução linha a linha')
    p.add_argument('--max-passos', type=int, default=1000000)

    args = p.parse_args()

    mostrar = [x.strip().upper() for x in args.mostrar.split(',') if x.strip()]

    regs, passos = executar(
        args.arquivo,
        parse_regs(args.regs),
        mostrar=mostrar,
        inicio=args.inicio,
        traco=not args.sem_traco,
        max_passos=args.max_passos
    )

    if args.sem_traco:
        print(f'Passos: {passos}')
        print(estado(regs, mostrar))

if __name__ == '__main__':
    main()