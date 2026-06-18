#!/usr/bin/env python3
from pathlib import Path
import importlib.util

base = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location('norma_machine', base / 'norma_machine.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def run(fname, regs, show):
    
    out, passos = mod.executar(
        base / 'programas' / fname,
        regs,
        mostrar=show,
        traco=False,
        max_passos=5_000_000
    )

    return {r: out[r] for r in show}

tests = [

    # SOMA
    # Entrada: A=2, B=3
    # A macro soma A+B em C e zera A e B.
    ('01_soma.txt', {'A': 4, 'B': 2}, ['A', 'B', 'C'], {'A': 0, 'B': 0, 'C': 6}),

    # MULTIPLICAÇÃO
    # Entrada: A=4, B=3
    # A macro calcula A = A * B.
    # B deve ser restaurado e C, D ficam zerados.
    ('02_multiplicacao.txt', {'A': 4, 'B': 3}, ['A', 'B', 'C', 'D'], {'A': 12, 'B': 3, 'C': 0, 'D': 0}),

    # FATORIAL
    # Entrada: A=5
    # A macro calcula A = 5!.
    # 5! = 120.
    ('03_fatorial.txt', {'A': 5}, ['A', 'B', 'C', 'D'], {'A': 120, 'B': 0, 'C': 0, 'D': 0}),

    # MENOR
    # Entrada: A=2, B=5
    # Testa se A < B.
    ('04_menor.txt', {'A': 2, 'B': 5}, ['A', 'B', 'C'], {'A': 2, 'B': 5, 'C': 1}),

    # MENOR
    # Entrada: A=5, B=2
    # Testa se A < B.
    ('04_menor.txt', {'A': 5, 'B': 2}, ['A', 'B', 'C'], {'A': 5, 'B': 2, 'C': 0}),

    # TESTE DE MÓDULO ZERO
    # Entrada: A=12, B=3
    # Testa se A mod B é zero.
    ('05_teste_mod_zero.txt', {'A': 12, 'B': 3}, ['A', 'B', 'C'], {'A': 12, 'B': 3, 'C': 1}),

    # TESTE DE MÓDULO ZERO
    # Entrada: A=14, B=3
    # Testa se A mod B é zero.
    ('05_teste_mod_zero.txt', {'A': 14, 'B': 3}, ['A', 'B', 'C'], {'A': 14, 'B': 3, 'C': 0}),

    # PRIMO
    # Entrada: A=7
    # Testa se A é primo.
    ('06_primo.txt', {'A': 7}, ['A', 'B'], {'A': 7, 'B': 1}),

    # PRIMO
    # Entrada: A=9
    # Testa se A é primo.
    ('06_primo.txt', {'A': 9}, ['A', 'B'], {'A': 9, 'B': 0}),

    # POTÊNCIA
    # Entrada: A=2, B=5
    # A macro calcula C = A^B.
    # 2^5 = 32.
    ('07_potencia.txt', {'A': 2, 'B': 5}, ['A', 'B', 'C'], {'A': 2, 'B': 5, 'C': 32}),

    # FIBONACCI
    # Entrada: A=7
    # A macro calcula B = fib(A).
    ('08_fibonacci.txt', {'A': 7}, ['A', 'B'], {'A': 0, 'B': 13}),

    # DIVISÃO INTEIRA COM RESTO
    # Entrada: A=17, B=5
    # 17 dividido por 5 dá quociente 3 e resto 2.
    ('09_divisao_resto.txt', {'A': 17, 'B': 5}, ['A', 'B', 'C', 'D'], {'A': 0, 'B': 5, 'C': 3, 'D': 2}),

    # MDC
    # Entrada: A=48, B=18
    # O MDC de 48 e 18 é 6.
    # A saída fica em C.
    ('10_mdc.txt', {'A': 48, 'B': 18}, ['C'], {'C': 6}),

    # COEFICIENTE BINOMIAL
    # Entrada: A=5, B=2
    # Calcula C(5,2), ou seja, combinação de 5 tomados 2 a 2.
    # C(5,2) = 10.
    ('11_coeficiente_binomial.txt', {'A': 5, 'B': 2}, ['C'], {'C': 10}),

    # COEFICIENTE BINOMIAL
    # Entrada: A=6, B=3
    # Calcula C(6,3).
    # C(6,3) = 20.
    ('11_coeficiente_binomial.txt', {'A': 6, 'B': 3}, ['C'], {'C': 20}),
]

ok = True

for fname, regs, show, expected in tests:

    got = run(fname, regs, show)

    if got != expected:
        ok = False
        print('FALHOU', fname, regs, 'got', got, 'expected', expected)

    else:
        print('OK', fname, regs, got)

if not ok:
    raise SystemExit(1)

print('Todos os testes passaram.')