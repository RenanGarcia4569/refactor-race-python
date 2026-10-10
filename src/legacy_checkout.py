# Refatoração do sistema de checkout legado

def calculate_subtotal(items):
    """Calcula o subtotal dos itens."""
    return sum(item["price"] * item["qty"] for item in items if item["qty"] > 0)


def calculate_discount(customer, subtotal, coupon=""):
    """Aplica descontos de acordo com o tipo de cliente e cupom."""
    desconto = 0

    if customer["type"] == "vip":
        desconto = subtotal * (0.15 if subtotal >= 1000 else 0.10)
    elif customer["type"] == "employee":
        desconto = subtotal * 0.20
    elif customer["type"] == "regular" and subtotal >= 800:
        desconto = subtotal * 0.05

    if coupon == "PROMO10":
        desconto += 10
    elif coupon == "VIP50" and customer["type"] == "vip":
        desconto += 50

    return desconto


def calculate_shipping(state, subtotal, express=False, peso=1):
    """Calcula o frete com base no estado, subtotal e tipo de entrega."""
    base_shipping = 20 if state in ["SP", "RJ", "MG", "ES"] else 35

    if subtotal > 200:
        return 0

    shipping = base_shipping * peso
    if express:
        shipping *= 1.8

    return shipping


def calculate_tax(state, valor):
    """Calcula imposto de acordo com o estado."""
    tax_rates = {
        "SP": 0.12,
        "RJ": 0.15,
        "MG": 0.07,
        "ES": 0.10
    }
    return valor * tax_rates.get(state, 0.05)


def process_order(customer, items, coupon="", state="MG", express=False, peso=1):
    """Processa o pedido aplicando subtotal, desconto, frete e impostos."""
    subtotal = calculate_subtotal(items)
    desconto = calculate_discount(customer, subtotal, coupon)
    shipping = calculate_shipping(state, subtotal, express, peso)
    total = subtotal - desconto + shipping
    tax = calculate_tax(state, total)
    return total + tax
