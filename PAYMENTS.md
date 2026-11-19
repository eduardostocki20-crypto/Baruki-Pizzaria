# Configurações de recebimento (planejamento)

A administração terá uma área **Configurações > Pagamentos e recebimentos** com:

- Provedor ativo: Mercado Pago inicialmente, com possibilidade de trocar futuramente.
- Campo para selecionar outro provedor quando a integração correspondente for implementada.
- Situação da conexão e data da última validação.
- Identificação da conta de recebimento (apelido, banco e apenas os 4 últimos dígitos).
- Atalho para abrir o painel oficial do provedor e configurar/alterar a conta bancária de saque.

**Segurança:** a conta bancária que recebe os valores das vendas deve ser cadastrada/validada diretamente no painel oficial do provedor (por exemplo, Mercado Pago). O app não deve pedir senha bancária, token, CVV ou armazenar número completo de cartão. O provedor processa o pagamento e faz o repasse para a conta bancária cadastrada na conta do lojista.

A tela administrativa de configuração só deve ser liberada depois de implementar login de administrador, controle de permissões e proteção das credenciais. Não exponha endpoints de alteração de provedor ou credenciais publicamente.
