# Atividade 3 de Git/GitHub

A atividade se divide em 3 grandes fases: Trabalho Solo, Trabalho em Dupla e Documentação.

## **Fase 1: Preparando Repositório**

**1. Interagir com o repositório do professor:**

- [x] Acessar o repo ``Daniel-Lim-Apo/CSharp-OOP-Tutorial`` (ou outro).
- [x] Clicar em Star (favoritar).
- [x] Clicar em Fork (criar uma cópia sua no GitHub).
- [x] Evidência: Print da página com a estrela marcada + print do seu perfil mostrando o repositório "forkado".

**2. Criar o repositório do Projeto Final:**

- [x] Criar um novo repositório privado: proj-final-<"seu-usuario">.
- [x] Marcar para iniciar com um ``README.md``.
- [x] Clonar o repositório para sua máquina.
- [x] (Opcional, mas recomendado): Adicionar um ``.gitignore`` (pode pegar um modelo pronto para Visual Studio ou a tecnologia que for usar).
- [x] Fazer o primeiro commit: ``chore: initial commit``.
- [x] Evidência: Print da página principal do seu repo no GitHub.

**3. Implementar Git Flow (Básico):**

- [x] Criar a branch ``develop`` a partir da ``main``.
- [x] Fazer ``push`` da ``develop`` para o GitHub.
- Comandos Chave:

```bash
# No seu repo local
git checkout -b develop
git push -u origin develop
```

- [x] Evidência: Print da lista de branches no GitHub (deve mostrar main e develop).

**4. Sua Primeira Feature:**

- [x] A partir da ``develop``, criar uma branch ``feature/nome-da-feature`` (ex: ``feature/update-readme``).
- [x] Fazer uma alteração simples (ex: adicionar detalhes ao README.md).
- [x] Commitar a mudança com uma mensagem clara (ex: ``docs: add project plan to readme``).
- [x] Fazer ``push`` da branch da feature.
- [x] Abrir um Pull Request (PR) no GitHub, comparando ``feature/update-readme`` com a base ``develop``.
- [x] Evidência: Print da tela do PR aberto.

## **Fase 2: O Jogo da Colaboração**

Agora a coisa fica interessante. Vocês vão "invadir" o repositório um do outro.

**Parte A:** Você é a Dona do Repositório

**1. Convidar seu Colega:**

- [X] No seu repo > ``Settings`` > ``Collaborators`` > Adicionar o user do colega com permissão de Write.
- [X] Evidência: Print da tela de colaboradores com o convite aceito.

**2. Revisar o Trabalho Dele:**

- [ ] Seu colega vai criar uma branch, commitar e abrir um PR para a ``develop`` do seu repositório.
- [ ] Você vai analisar o PR dele: olhar os arquivos modificados (``Files changed``), deixar comentários ou solicitar ajustes.
- [ ] Se estiver tudo OK, fazer o Merge do PR.
- Evidência: Prints da conversa no PR, do review e da confirmação do merge.

**Parte B:** Você é a Colaboradora

**1. Clonar e Trabalhar no Repo do Colega:**

- [ ] O colega te adiciona como Collaborator.
- [ ] Você clona o repo dele, entra na branch ``develop``.
- [ ] Cria sua branch de feature (ex: ``feature/add-user-docs``).
- [ ] Faz sua contribuição, commita e faz o ``push`` da sua branch.

**2. Abrir o Pull Request:**

- [ ] No repositório dele, você abre um PR da sua branch para a ``develop`` dele.
- [ ] Preenche título e descrição de forma clara.
- [ ] Acompanha o review dele e ajusta o que for preciso.
- Evidência: Prints da sua contribuição: PR aberto no repo dele, histórico de commits, etc.

## **Fase 3: Empacotando para Entrega**

Organizar as provas do crime.

**1. Finalizar e Taguear (Opcional, mas enriquece):**

- [ ] Criar uma tag para marcar uma "versão" do seu projeto (ex: v1.0.0).

Comandos Chave:

```bash
# Após o merge na main
git checkout main
git pull
git tag -a v1.0.0 -m "Release v1.0.0: Initial setup and health endpoint"
git push origin v1.0.0
```

- Evidência: Print da área de "Releases" ou "Tags" no GitHub.

**2. Bônus - Issues:**

- [ ] Criar uma ``Issue`` descrevendo uma tarefa.
- [ ] No PR que resolve essa tarefa, vincular a issue usando ``Closes #1`` na descrição.
- Evidência: Print da issue e do PR mostrando o vínculo.

**3. Montar o Relatório em PDF:**

- [ ] Seguir o modelo fornecido, preenchendo cada seção.
- [ ] Inserir os prints nos locais corretos.
- [ ] Nas seções de "Comentários" e "Reflexões", seja direta. O que você realmente aprendeu? Onde travou? Qual a diferença real entre ``fork`` e ``colaborador`` na prática?
