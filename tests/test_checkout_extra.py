import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from legacy_checkout import (
    calculate_subtotal,
    calculate_discount,
    calculate_shipping,
    calculate_tax,
    process_order
)

# -------------------------------
# Testes unitários das funções isoladas
# -------------------------------

def test_calculate_subtotal():
    items = [{"price": 10, "qty": 2}, {"price": 5, "qty": 3}]
    assert calculate_subtotal(items) == 35

def test_calculate_discount_vip():
    customer = {"type": "vip"}
    subtotal = 1200
    assert calculate_discount(customer, subtotal) == subtotal * 0.15

def test_calculate_discount_employee():
    customer = {"type": "employee"}
    subtotal = 500
    assert calculate_discount(customer, subtotal) == subtotal * 0.20

def test_calculate_shipping_free():
    subtotal = 250
    assert calculate_shipping("SP", subtotal) == 0

def test_calculate_shipping_express():
    subtotal = 100
    assert calculate_shipping("RJ", subtotal, express=True, peso=2) > 0

def test_calculate_tax_sp():
    valor = 100
    assert calculate_tax("SP", valor) == 12

def test_calculate_tax_default():
    valor = 100
    assert calculate_tax("BA", valor) == 5

# -------------------------------
# Testes integrados da função principal
# -------------------------------

def test_process_order_vip_with_coupon():
    customer = {"type": "vip"}
    items = [{"price": 100, "qty": 10}]
    total = process_order(customer, items, coupon="VIP50", state="SP")
    assert total > 0

def test_process_order_regular():
    customer = {"type": "regular"}
    items = [{"price": 200, "qty": 5}]
    total = process_order(customer, items, state="MG")
    assert round(total, 2) == 1016.5
