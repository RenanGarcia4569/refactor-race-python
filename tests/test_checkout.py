import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from legacy_checkout import process_order

def test_vip_discount():
    customer = {"type": "vip"}
    items = [{"price": 100, "qty": 10}]
    total = process_order(customer, items, state="SP")
    assert total < 1000  # deve aplicar desconto

def test_employee_discount():
    customer = {"type": "employee"}
    items = [{"price": 50, "qty": 10}]
    total = process_order(customer, items, state="RJ")
    assert total < 500

def test_regular_discount():
    customer = {"type": "regular"}
    items = [{"price": 200, "qty": 5}]
    total = process_order(customer, items, state="MG")
    # subtotal 1000 → desconto 5% → 950 + imposto 7% = 1016.5
    assert round(total, 2) == 1016.5

def test_shipping_free():
    customer = {"type": "regular"}
    items = [{"price": 300, "qty": 1}]
    total = process_order(customer, items, state="SP")
    # subtotal 300 → frete grátis → imposto 12% = 36 → total 336
    assert round(total, 2) == 336.0

def test_tax_applied():
    customer = {"type": "vip"}
    items = [{"price": 100, "qty": 2}]
    total = process_order(customer, items, state="RJ")
    # deve aplicar imposto do RJ (15%)
    assert total > 150
