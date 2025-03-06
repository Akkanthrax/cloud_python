# Gerenciador Financeiro - README

## Sobre o Projeto

Este projeto tem como objetivo auxiliar usuários a gerenciarem sua vida financeira. A plataforma permite que o usuário:

- Registre seus ganhos e gastos
- Defina objetivos financeiros
- Visualize um relatório detalhado sobre suas finanças

A aplicação será desenvolvida utilizando Python (backend), HTML, CSS, e JavaScript (frontend), seguindo a arquitetura MVC e utilizando a AWS (Lambda, Aurora, CodeDeploy, etc.) para hospedagem e escalabilidade.

## FASE 1 - Configuração Local (MVP)

1. Configuração do Ambiente
2. Criar o Banco de Dados
3. Criar a Autenticação (Login/Logout)
4. Criar o CRUD para Objetivos
5. Criar o CRUD para Gastos
6. Criar a Visão Geral Financeira
7. Melhorias Gerais

## Estrutura de Arquivos e Pastas

```plaintext
backend/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── objectives.py
│   │   ├── expenses.py
│   │   ├── financial_overview.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── config.py
├── requirements.txt
├── run.py
```

## FASE 2 - Preparação para Deploy na AWS

8. Configurar o Banco de Dados Aurora
9. Configurar a Hospedagem
10. Criar Funções Lambda
11. Configurar Deploy Contínuo
12. Monitoramento e Ajustes

## FASE 3 - Funcionalidades Extras

(Para depois que o MVP estiver rodando)

## Como Contribuir

Clone o repositório:

```sh
git clone https://github.com/seu-usuario/gerenciador-financeiro.git