from behave import given, when, then

@given('que eu insiro o primeiro número "{num1:d}"')
def step_insere_primeiro_numero(context, num1):
    context.num1 = num1

@given('que eu insiro o segundo número "{num2:d}"')
def step_insere_segundo_numero(context, num2):
    context.num2 = num2

@when('eu calculo a média')
def step_calcula_media(context):
    context.media_calculada = (context.num1 + context.num2) / 2

@then('a média dos dois números deve ser "{media_esperada:d}"')
def step_verifica_media(context, media_esperada):
    assert context.media_calculada == media_esperada, f"Média esperada: {media_esperada}, Média calculada: {context.media_calculada}"
