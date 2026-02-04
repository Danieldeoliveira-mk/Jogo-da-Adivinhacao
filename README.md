# Jogo da Adivinhação
 
Oi, tudo bem? Meu nome é Daniel de Oliveira e criei esse programinha como forma de aprender python.

Esse é um jogo de adivinhação onde o usuário deve descobrir qual é o numero aleatorio que a maquina sorteou.

## Requisitos:
Para executar o programa corretamente é necessario ter o python em seu computador e instalar esses dois pacotes Python:<br>
`colorama`
`readchar`

Execute os seguintes comandos no terminal dentro da pasta onde deseja rodar o programa:<br>

Crie e ative o ambiente virtual:<br>

* **No Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

* **No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
**Instale os pacotes Python:**
```
pip install -r requisitos.txt
```
## Caracteristicas/Recursos:
* **Dicas Dinâmicas:** O jogo informa se o seu chute foi maior ou menor que o número sorteado.
* **Termômetro:** O programa avisa se você está "congelando", "frio", "quente" ou "fervendo" (baseado na proximidade do número).
* **Sistema de Ranking:** Persistência de dados em JSON que armazena as 10 melhores performances.
* **Modo Difícil:** Um desafio extra com limite de 10 tentativas.
* **Interface Colorida:** Uso da biblioteca colorama para melhor feedback visual no terminal.

## Sobre a produção do código:
Programei fazendo pesquisas no google, consultando ia, consultando o w3schools e o stackoverflow.<br>
Não copiei código dessas pesquisas, apenas adaptei alguns códigos e idéias/lógica ao programa
