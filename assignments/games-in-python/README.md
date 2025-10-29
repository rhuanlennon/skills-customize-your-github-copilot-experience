
# 🎮 Jogo da Forca (Games in Python)

Crie o clássico jogo da forca usando Python — praticando strings, estruturas de repetição e entrada do usuário.

## Objetivos

Um jogo da forca onde o jogador tenta adivinhar uma palavra letra a letra antes de esgotar as tentativas. O jogo deve mostrar o progresso com espaços reservados, listar letras erradas e indicar vitória ou derrota ao final.

### Competências praticadas

- Manipulação de strings
- Laços (for/while)
- Estruturas condicionais (if/else)
- Entrada e saída no terminal
- Uso do módulo random para seleção de palavras

## Objetivos de aprendizagem

Ao final dessa tarefa você deverá ser capaz de:

- Implementar lógica de controle de fluxo para um jogo interativo
- Trabalhar com listas e strings para atualizar o estado do jogo
- Validar e processar input do usuário de forma segura

## Pré-requisitos

- Python 3.8+ instalado
- Conhecimentos básicos de listas, strings e loops

## Tarefas

O seu jogo deve:

- Selecionar aleatoriamente uma palavra a partir de uma lista pré-definida
- Aceitar palpites de letras e atualizar o estado exibido (ex.: _ a _ _ o)
- Mostrar letras já chutadas (corretas e incorretas)
- Controlar o número de tentativas restantes e encerrar quando chegarem a zero
- Exibir mensagens claras de vitória ou derrota

## Requisitos opcionais (Stretch Goals)

- Permitir que o jogador escolha um nível de dificuldade (mais/menos tentativas)
- Ler a lista de palavras de um arquivo CSV ou TXT
- Suportar tentativa de adivinhação da palavra inteira
- Mostrar um pequeno desenho da forca que evolui conforme erros

## Estrutura de arquivos

Arquivos relevantes nesta pasta:

- `starter-code.py` — ponto de partida fornecido
- `README.md` — este arquivo (instruções e critérios)

Se você adicionar recursos, documente-os nesta README e mantenha a estrutura organizada.

## Como executar (local)

1. Abra um terminal na pasta `assignments/games-in-python`.
2. Execute:

```bash
python3 starter-code.py
```

Observação: se você renomear o arquivo principal, atualize o comando acima.

## Critérios de avaliação (rubrica)

Para a entrega ser considerada completa, verifique:

- (✅) O jogo executa sem erros e segue os requisitos obrigatórios
- (✅) Entradas inválidas (ex.: números, mais de uma letra) são tratadas adequadamente
- (✅) Mensagens ao jogador são claras (progresso, tentativas restantes, letras usadas)

Para nota extra, implemente ao menos um dos requisitos opcionais e documente-o.

## Como submeter

1. Confirme que seu código está na pasta `assignments/games-in-python`.
2. Faça commit seguindo o padrão Conventional Commits, por exemplo:

```
git add .
git commit -m "feat(games-in-python): adicionar versão funcional do jogo da forca"
```

3. Abra um PR ou envie conforme as instruções do curso/professor.

## Dicas e casos de borda

- Verifique letras repetidas: chutes já usados não devem consumir tentativas
- Trate espaços e hífens se usar frases compostas como palavras-alvo
- Limpe ou normalize o input (ex.: transformar tudo em minúsculas)

Boa sorte — divirta-se codando e aprendendo!
