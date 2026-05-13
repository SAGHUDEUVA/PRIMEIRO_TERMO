# 📘 Engenharia de Software: Elicitação e Levantamento de Requisitos

Este documento serve como plano de conteúdo e material de apoio para as aulas de engenharia de requisitos.

---

## 📌 1. Fundamentos: Requisitos Funcionais vs. Não Funcionais

A base do escopo de qualquer projeto de software reside na separação entre o comportamento esperado e as suas restrições operacionais.

### Requisitos Funcionais (RF)
*   **Definição:** Descrevem as ações, comportamentos e serviços que o sistema deve executar.
*   **Foco:** Entradas, processamento e saídas de dados.
*   **Exemplos Práticos:**
    *   **RF01:** O sistema deve permitir que o aluno visualize suas notas bimestrais.
    *   **RF02:** O sistema deve emitir um alerta em tempo real quando o estoque atingir o limite mínimo.

### Requisitos Não Funcionais (RNF)
*   **Definição:** Impõem restrições aos serviços ou funções oferecidos pelo sistema.
*   **Foco:** Qualidade, desempenho, segurança, confiabilidade, usabilidade e conformidade legal.
*   **Exemplos Práticos:**
    *   **RNF01:** A tela de login deve ser carregada em menos de 1.5 segundos sob conexão 4G.
    *   **RNF02:** Todas as senhas de usuários armazenadas no banco de dados devem ser criptografadas utilizando SHA-256.

---

## 👥 2. Técnicas de Elicitação de Requisitos

Métodos práticos utilizados pelo analista para extrair as necessidades reais das partes interessadas (*stakeholders*).

### Entrevistas
*   **Objetivo:** Coleta profunda de dados por meio do diálogo direto com usuários-chave.
*   **Tipos de Abordagem:**
    *   **Estruturada:** Baseada em um questionário fixo e fechado. Evita desvios do assunto.
    *   **Não Estruturada:** Conversa aberta conduzida pelas respostas do entrevistado. Boa para descobrir dores ocultas.
*   **Dica para a Aula:** Ensine os alunos a evitar perguntas indutivas (ex: *"Você prefere o botão azul, certo?"*).

### Brainstorm (Tempestade de Ideias)
*   **Objetivo:** Estimular a criatividade da equipe para levantar ideias inovadoras e resolver problemas complexos rapidamente.
*   **Regras de Ouro:**
    1.  Proibido criticar ou julgar qualquer ideia na fase inicial.
    2.  Focar na quantidade de ideias, não na qualidade imediata.
    3.  Construir propostas combinando ideias anteriores de outros participantes.

### Prototipagem
*   **Objetivo:** Construir uma representação visual ou funcional do software para validação rápida com o cliente.
*   **Níveis de Fidelidade:**
    *   **Baixa Fidelidade:** Desenhos à mão livre (*wireframes* em papel). Foco na arquitetura de informação e fluxo.
    *   **Alta Fidelidade:** Interfaces interativas e clicáveis feitas em ferramentas digitais (ex: Figma). Foco na experiência do usuário (UX) e visual final.

---

## 🗺️ 3. Modelagem e Diagramas

Modelos visuais que traduzem os requisitos em representações técnicas fáceis de compreender por desenvolvedores e clientes.

*   **Diagrama de Casos de Uso (UML):** Mapeia o comportamento do sistema sob a perspectiva do usuário. Mostra de forma clara a relação entre os **Atores** (quem usa) e os **Casos de Uso** (o que fazem).
*   **Diagrama de Fluxo de Dados (DFD):** Modela como as informações se movem através do sistema, especificando entradas, transformações de processos e armazenamentos de dados.
*   **Diagrama de Atividades:** Funciona como um fluxograma avançado, detalhando a sequência lógica de passos de um processo de negócio.

---

## 📑 4. Relatórios Técnicos e Documentação

Etapa final onde os requisitos levantados são formalizados e assinados pelo cliente antes do início do desenvolvimento.

### Estrutura do Documento de Especificação de Requisitos de Software (SRS)
1.  **Introdução:** Escopo do projeto, objetivos de negócio e definições/acrônimos.
2.  **Descrição Geral:** Perspectiva do produto, funções principais e restrições gerais do ambiente.
3.  **Requisitos Específicos:** Listagem detalhada e numerada de todos os RFs e RNFs.

### Matriz de Rastreabilidade
Uma tabela técnica utilizada para monitorar o ciclo de vida do requisito. Ela conecta a origem do requisito (ex: *Entrevista com Diretor*) ao código implementado e ao caso de teste correspondente, garantindo que nada seja esquecido ou desenvolvido fora do escopo.
