# Refactor Race Python – Relatório Final

**Nome:** Renan Garcia  
**RA:** 325131727
**Curso/Disciplina:** Ciência da Computação – Garantia da Qualidade de Software
**Data:** 10/10/2026

## Introdução
Este projeto consistiu em refatorar um sistema legado de checkout em Python, com o objetivo de reduzir complexidade, aumentar cobertura de testes e melhorar a legibilidade.

## Refatorações realizadas
- Extração de funções auxiliares:
  - `calculate_subtotal`
  - `calculate_discount`
  - `calculate_shipping`
  - `calculate_tax`
- Remoção de duplicação de código.
- Simplificação de condicionais.
- Substituição de números mágicos por constantes.

## Cálculos explicados
- **Subtotal** = soma de preço × quantidade.
- **Desconto** = percentual aplicado sobre subtotal (VIP 15%, funcionário 20%).
- **Frete** = grátis acima de R$200, ou calculado por peso se expresso.
- **Imposto** = percentual sobre (subtotal – desconto + frete).
- **Total** = subtotal – desconto + frete + imposto.

Exemplo: Cliente regular em MG, 5 itens de R$200:
- Subtotal = 1000
- Desconto = 0
- Frete = 20
- Imposto = 50
- **Total = 1070**

## Métricas (Antes → Depois → Extras)
| Métrica              | Antes | Depois | Com Testes Extras |
|----------------------|-------|--------|-------------------|
| Complexidade média   | C/D   | A (3.6) | A (3.6) |
| Cobertura de testes  | ~60%  | 95%    | 99% |
| Erros de lint (Ruff) | Vários| 0      | 0 |

## Testes
- **Principais**: validam o fluxo completo de checkout.
- **Extras**: validam cada função isolada.
✅ Resultado: cobertura de testes aumentou para **99%**.

## Uso da IA
Durante o desenvolvimento, utilizei a **IA Copilot (Microsoft)** como apoio para:
- Resolver problemas de importação e estrutura de pacotes.
- Sugerir refatorações para reduzir complexidade.
- Criar testes unitários adicionais.
- Gerar documentação (README.md e METRICS.md).
- Orientar sobre fluxo de versionamento com Git.

## Link do GitHub
👉 [Repositório no GitHub](https://github.com/RenanGarcia4569/refactor-race-python/tree/main)
