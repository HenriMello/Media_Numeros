
Feature: Calculadora de Média
  Para calcular a média de dois números
  Como usuário
  Eu quero inserir dois números e obter a média deles

  Scenario: Calcular a média de dois números
    Given que eu insiro o primeiro número "10"
    And que eu insiro o segundo número "20"
    When eu calculo a média
    Then a média dos dois números deve ser "15"
