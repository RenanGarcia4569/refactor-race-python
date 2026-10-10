# REFactor Race Python

## 👥 Equipe
- Renan Garcia

## 📌 Descrição
Projeto de refatoração e testes de um sistema legado de checkout em Python.  
Objetivo: melhorar legibilidade, reduzir complexidade e aumentar cobertura de testes.

## 🔎 Diagnóstico Inicial
- Função `process_order` muito grande e com responsabilidades misturadas.
- Código duplicado (subtotal calculado duas vezes).
- Condicionais complexas e repetitivas.
- Uso de números mágicos e strings fixas.

## 🔧 Refatorações Realizadas
- Extração de funções auxiliares: `calculate_subtotal`, `calculate_discount`, `calculate_shipping`, `calculate_tax`.
- Substituição de números mágicos por constantes claras.
- Simplificação de condicionais.
- Remoção de duplicação de código.

## 🧪 Testes Adicionados
- Cliente VIP com cupom.
- Cliente regular com frete grátis.
- Funcionário com desconto.
- Impostos aplicados por estado.

## 📊 Métricas Antes e Depois
Vide arquivo **METRICS.md**.

## ⚙️ Decisões Técnicas
- Separação de responsabilidades para facilitar manutenção.
- Uso de funções puras para simplificar testes.
- Redução de duplicação de código.

## 🚀 Melhorias Futuras
- Implementar logs para auditoria de pedidos.
- Adicionar validação de entrada (ex.: itens sem preço ou quantidade negativa).
- Expandir regras de desconto e impostos para outros estados.

## 🧪 Testes
O projeto possui dois conjuntos de testes:
- **Testes principais**: validam o fluxo completo de checkout.
- **Testes extras**: validam cada função isolada (`calculate_subtotal`, `calculate_discount`, `calculate_shipping`, `calculate_tax`).

Resultado: cobertura de testes aumentou para **99%**.

---

## 🤖 Uso da IA no Projeto
Durante o desenvolvimento, utilizei a **IA Copilot (Microsoft)** como apoio para:
- Resolver problemas de importação e estrutura de pacotes.
- Sugerir refatorações para reduzir complexidade.
- Criar testes unitários adicionais.
- Gerar documentação (README.md e METRICS.md).
- Orientar sobre fluxo de versionamento com Git.

A IA funcionou como **assistente técnico**, acelerando o processo e garantindo maior qualidade no resultado final.


