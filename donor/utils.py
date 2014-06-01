import paypalrestsdk
import logging

from buskr.settings import PAYPAL_MODE, PAYPAL_SECRET, PAYPAL_CLIENT_ID

logging.basicConfig(level=logging.DEBUG)

def get_credit_card_type(number):
    number = str(number)
    if len(number) == 13:
        if number[0] == "4":
            return 'visa'
    elif len(number) == 14:
        if number[:2] == "36":
            return 'mastercard'
    elif len(number) == 15:
        if number[:2] in ("34", "37"):
            return 'amex'
    elif len(number) == 16:
        if number[:4] == "6011":
            return 'discover'
        if number[:2] in ("51", "52", "53", "54", "55"):
            return 'mastercard'
        if number[0] == "4":
            return 'visa'
    return None

def split_card_holder_name(name):
    names = name.split(' ', 1)
    if len(names) == 1:
        names.append('')
    return names

def configure_paypal():
    return paypalrestsdk.configure({
        'mode': PAYPAL_MODE,
        'client_id': PAYPAL_CLIENT_ID,
        'client_secret': PAYPAL_SECRET
    })

def make_donation(donation):
    """Returns the result of attempting a payment through the PayPal api."""
    card = donation.card
    first_name, last_name = split_card_holder_name(card.cardholder_name)
    credit_card_type = get_credit_card_type(card.number)
    if not credit_card_type:
        return False

    configure_paypal()
    payment = paypalrestsdk.Payment({
        'intent': 'sale',
        'payer': {
            'payment_method': 'credit_card',
            'funding_instruments': [{
                'credit_card': {
                    'type': credit_card_type,
                    'number': str(card.number),
                    'expire_month': str(card.expire_month),
                    'expire_year': str(card.expire_year),
                    'cvv2': str(card.cvv2),
                    'first_name': first_name,
                    'last_name': last_name,
                }
            }]
        },
        'transactions': [{
            'amount': {
                'total': str(donation.amount),
                'currency': str(donation.currency),
            },
            'description': str(donation.description)
        }]
    })
    return payment.create()
