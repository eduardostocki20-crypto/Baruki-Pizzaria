"""Configuração central do provedor de pagamentos.

A integração real deve usar credenciais privadas no servidor e webhooks assinados.
Dados bancários completos e credenciais bancárias não devem ser armazenados aqui.
"""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class PaymentSettings:
    provider: str
    access_token: str
    webhook_secret: str
    payout_account_label: str
    payout_bank_name: str
    payout_account_last4: str

def get_payment_settings() -> PaymentSettings:
    return PaymentSettings(
        provider=os.getenv("PAYMENT_PROVIDER", "mercado_pago"),
        access_token=os.getenv("PAYMENT_ACCESS_TOKEN", ""),
        webhook_secret=os.getenv("PAYMENT_WEBHOOK_SECRET", ""),
        payout_account_label=os.getenv("PAYOUT_ACCOUNT_LABEL", ""),
        payout_bank_name=os.getenv("PAYOUT_BANK_NAME", ""),
        payout_account_last4=os.getenv("PAYOUT_ACCOUNT_LAST4", ""),
    )
