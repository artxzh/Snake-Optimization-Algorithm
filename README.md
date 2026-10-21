# Otimizador Snake com Optuna

Projeto em Python que executa o algoritmo Snake para minimizar funções de
benchmark. O Optuna pode buscar os coeficientes `c1`, `c2` e `c3` usados pelo
algoritmo.

## Requisitos

- Python 3.10 ou superior (recomendado: Python 3.12 ou 3.13)
- `pip`

Neste workspace, Optuna e NumPy foram instalados e testados com Python 3.13.16.
No Python 3.15, a instalação do Optuna pode falhar porque a dependência PyYAML
pode não ter wheel compatível e exigir Microsoft C++ Build Tools para compilar;
por isso, recomenda-se usar Python 3.13.

## Instalação

No PowerShell, abra a pasta raiz do projeto e execute:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se a política de execução do PowerShell impedir a ativação do ambiente, use o
executável do ambiente diretamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No VS Code, selecione `.venv\Scripts\python.exe` como interpretador do workspace
para que a análise e a execução usem as dependências instaladas nesse ambiente.

## Executar o otimizador

Execute o exemplo já configurado com a função Sphere:

```powershell
python main.py
```

O programa imprime a população resultante e o melhor valor encontrado, e grava
a população em `results/resultado.txt`.

## Buscar parâmetros com Optuna

Na pasta raiz do projeto, execute:

```powershell
python -m experiments.tune_parameters
```

Por padrão, o estudo executa 30 tentativas, com 5 dimensões, população de 50
indivíduos, 100 iterações por tentativa e semente 42. O estudo minimiza a função
Sphere com amostragem TPE. A busca considera `c1` e `c3` entre 0.1 e 1.0 e `c2`
entre 0.0001 e 0.1 em escala logarítmica. O melhor resultado e os parâmetros são
gravados em `results/optuna_best_params.json`. A primeira tentativa usa os
valores originais (`c1=0.5`, `c2=0.005`, `c3=0.7`), para comparação com os
valores encontrados.

Os valores podem ser ajustados pela linha de comando:

```powershell
python -m experiments.tune_parameters --trials 50 --dimensions 10 --max-iterations 200 --population-size 60 --seed 7
```

`--population-size` deve ser par e maior ou igual a 2. Para salvar o JSON em
outro local, use `--output caminho/arquivo.json`.

## Mudanças implementadas

- Adicionada a dependência Optuna e declaradas as dependências do projeto em
  `requirements.txt`.
- Criado `experiments/tune_parameters.py`, que usa um estudo Optuna com
  amostragem TPE para minimizar a função Sphere variando `c1`, `c2` e `c3`.
- O script permite configurar tentativas, dimensões, iterações, tamanho da
  população e semente. O tamanho da população é validado para manter a divisão
  equilibrada entre indivíduos machos e fêmeas.
- A população é separada novamente em machos e fêmeas a cada iteração, inclusive
  após a etapa de exploração aleatória.
- Os resultados da busca são gravados em JSON em `results/optuna_best_params.json`
  (ou no caminho indicado por `--output`).
- `snake_optimizer` agora recebe a função objetivo e os três coeficientes como
  parâmetros, mantendo os valores anteriores como padrões para compatibilidade
  com chamadas existentes.
- Corrigido o retorno antecipado de `snake_optimizer`: agora todas as iterações
  solicitadas são executadas antes do retorno da população.
- Corrigida a normalização temporal de `food_update`, para o fator de alimento
  variar durante a execução em vez de ficar saturado desde o início.
