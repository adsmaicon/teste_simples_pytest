from calc import Calculadora


@given(u'que o valor mostrado seja {valor:d}')
def step_impl(context, valor):
    context.calc = Calculadora()


@given(u'que o primeiro valor seja {valor:d}')
def step_impl(context, valor):
    context.calc.primeiro = valor


@given(u'o segundo valor seja {valor:d}')
def step_impl(context, valor):
    context.calc.segundo = valor


@when(u'executar a operação "somar"')
def step_impl(context):
    context.resultado = context.calc.sum()


@then(u'o resultado da operação deve ser {valor:d}')
def step_impl(context, valor):
    assert context.resultado == valor