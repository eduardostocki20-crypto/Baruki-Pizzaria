# Minha Pizzaria — starter em Python + Flet

Estrutura inicial para um app de pedidos com interface Flet e API FastAPI.
O nome "Minha Pizzaria" é provisório.

## Requisitos
- Python 3.10+
- Windows, macOS ou Linux

## 1. Instalar
Abra o terminal nesta pasta e execute:

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Depois:
```bash
pip install -r requirements.txt
```

## 2. Executar o aplicativo
```bash
flet run --web src/main.py
```
Para abrir como janela desktop:
```bash
flet run src/main.py
```

## 3. Executar a API (outro terminal)
```bash
uvicorn backend.main:app --reload
```
A documentação interativa da API ficará em:
http://127.0.0.1:8000/docs

## O que já existe
- Tela inicial moderna em Flet
- Categorias e produtos demonstrativos
- Adicionar itens ao carrinho e visualizar subtotal
- API inicial com rota de saúde, listagem de produtos e criação/listagem de pedidos
- SQLite para desenvolvimento local

## Importante antes de vender de verdade
Esta é uma base de desenvolvimento, não um sistema pronto para produção.
- Os produtos e preços exibidos são demonstrativos.
- O checkout ainda não cobra pagamentos.
- Mercado Pago será o provedor inicial, mas a configuração foi centralizada para permitir trocar futuramente por outro provedor integrado.
- A conta bancária de recebimento/saque deve ser cadastrada no painel oficial do provedor; o app poderá exibir apenas uma identificação segura da conta (banco e últimos 4 dígitos).
- Nunca armazene número completo de cartão ou CVV no banco.
- Antes de publicar, adicionar autenticação administrativa, validação de pedidos, proteção contra fraude, HTTPS, backups, testes e configuração de produção.

## Próximas etapas
1. Definir nome, logo e identidade visual.
2. Cadastrar cardápio real, tamanhos, sabores, bordas e adicionais.
3. Criar cadastro/login, endereços e cálculo de entrega.
4. Integrar checkout seguro com o provedor escolhido.
5. Criar painel administrativo e fluxo de produção/entrega.
6. Publicar a API e o app; gerar builds Android/iOS.


Veja `PAYMENTS.md` para as regras da área de pagamentos e recebimentos e `backend/payment_config.py` para a configuração central do provedor.
