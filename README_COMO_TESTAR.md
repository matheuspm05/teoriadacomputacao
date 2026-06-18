# Trabalho 2 - Máquina Norma

Este pacote tem a Máquina Norma em Python e 11 programas monolíticos separados.

## Arquivos principais

- `norma_machine.py`: interpretador da Máquina Norma.
- `programas/01_soma.txt`
- `programas/02_multiplicacao.txt`
- `programas/03_fatorial.txt`
- `programas/04_menor.txt`
- `programas/05_teste_mod_zero.txt`
- `programas/06_primo.txt`
- `programas/07_potencia.txt`
- `programas/08_fibonacci.txt`
- `programas/09_divisao_resto.txt`
- `programas/10_mdc.txt`
- `programas/11_coeficiente_binomial.txt`

## Regras respeitadas

Os arquivos de programas usam apenas:

- `ADD R PROX`: soma 1 no registrador `R`.
- `SUB R PROX`: subtrai 1 do registrador `R`, sem deixar negativo.
- `ZER R L0 L1`: testa se `R` é zero; se for, vai para `L0`; se não for, vai para `L1`.

O interpretador termina quando o programa desvia para um rótulo que não existe.

## Como executar

Abra o terminal dentro desta pasta e rode:

```bash
python norma_machine.py programas/01_soma.txt --regs A=2,B=3 --mostrar A,B,C,D
```

Para não imprimir a execução linha por linha:

```bash
python norma_machine.py programas/01_soma.txt --regs A=2,B=3 --mostrar A,B,C,D --sem-traco
```

## Como testar cada macro

### 1. Soma

```bash
python norma_machine.py programas/01_soma.txt --regs A=2,B=3 --mostrar A,B,C,D --sem-traco
```

Esperado: `A=0, B=0, C=5`.

### 2. Multiplicação

```bash
python norma_machine.py programas/02_multiplicacao.txt --regs A=4,B=3 --mostrar A,B,C,D --sem-traco
```

Esperado: `A=12, B=3, C=0, D=0`.

### 3. Fatorial

```bash
python norma_machine.py programas/03_fatorial.txt --regs A=5 --mostrar A,B,C,D --sem-traco
```

Esperado: `A=120`.

### 4. Menor

```bash
python norma_machine.py programas/04_menor.txt --regs A=2,B=5 --mostrar A,B,C,D,E --sem-traco
```

Esperado: `C=1`, pois `2 < 5`.

Outro teste:

```bash
python norma_machine.py programas/04_menor.txt --regs A=5,B=2 --mostrar A,B,C,D,E --sem-traco
```

Esperado: `C=0`.

### 5. Teste de módulo zero

```bash
python norma_machine.py programas/05_teste_mod_zero.txt --regs A=12,B=3 --mostrar A,B,C,D,E,F,G --sem-traco
```

Esperado: `C=1`, pois `12 mod 3 = 0`.

```bash
python norma_machine.py programas/05_teste_mod_zero.txt --regs A=14,B=3 --mostrar A,B,C,D,E,F,G --sem-traco
```

Esperado: `C=0`, pois `14 mod 3 = 2`.

### 6. Primo

```bash
python norma_machine.py programas/06_primo.txt --regs A=7 --mostrar A,B,C,D,E,F,G,H --sem-traco
```

Esperado: `B=1`.

```bash
python norma_machine.py programas/06_primo.txt --regs A=9 --mostrar A,B,C,D,E,F,G,H --sem-traco
```

Esperado: `B=0`.

### 7. Potência

```bash
python norma_machine.py programas/07_potencia.txt --regs A=2,B=5 --mostrar A,B,C,D,E,F --sem-traco
```

Esperado: `C=32`.

### 8. Fibonacci

```bash
python norma_machine.py programas/08_fibonacci.txt --regs A=7 --mostrar A,B,C,D,E --sem-traco
```

Esperado: `B=13`.

### 9. Divisão inteira com resto

```bash
python norma_machine.py programas/09_divisao_resto.txt --regs A=17,B=5 --mostrar A,B,C,D,E,F,G --sem-traco
```

Esperado: `C=3, D=2`.

### 10. MDC

```bash
python norma_machine.py programas/10_mdc.txt --regs A=48,B=18 --mostrar A,B,C,D,E,F,G,H --sem-traco
```

Esperado: `C=6`.

### 11. Coeficiente binomial

```bash
python norma_machine.py programas/11_coeficiente_binomial.txt --regs A=5,B=2 --mostrar A,B,C,D,E,F,G,H,I --sem-traco
```

Esperado: `C=10`.

Outro teste:

```bash
python norma_machine.py programas/11_coeficiente_binomial.txt --regs A=6,B=3 --mostrar A,B,C,D,E,F,G,H,I --sem-traco
```

Esperado: `C=20`.

## Como conferir se está certo

A conferência é feita comparando a saída final dos registradores com a definição matemática da macro.

Exemplo: no programa de divisão, com `A=17` e `B=5`, sabemos que `17 = 5*3 + 2`. Então o quociente precisa ser `C=3` e o resto precisa ser `D=2`.

Exemplo: no MDC, com `A=48` e `B=18`, o maior divisor comum é `6`. Então a saída precisa ter `C=6`.

Exemplo: no binomial, com `n=5` e `k=2`, a combinação é `5!/(2!*3!) = 10`. Então `C=10`.

## Observação importante

Algumas macros maiores, como fatorial, primo, potência, Fibonacci, MDC e binomial, podem gerar muitos passos, porque a Máquina Norma só sabe somar 1, subtrair 1 e testar zero. Por isso, para testes rápidos, use números pequenos.
