import pytest

from ticket.strings.StringUtils import StringUtils


@pytest.mark.unit
def test_texto_centrado_001():
    string_utils = StringUtils()
    texto = 'hola'
    cant_caracteres = 6
    results = string_utils.texto_centrado(texto, cant_caracteres)
    assert ' hola ' == results


@pytest.mark.unit
def test_texto_centrado_002():
    # prep
    string_utils = StringUtils()
    texto = 'hola'
    cant_caracteres = 4
    # run
    results = string_utils.texto_centrado(texto, cant_caracteres)
    # results
    assert 'hola' == results


@pytest.mark.unit
def test_texto_centrado_003():
    # prep
    string_utils = StringUtils()
    texto = None
    cant_caracteres = 4
    # run
    results = string_utils.texto_centrado(texto, cant_caracteres)
    # results
    assert (results is None)


@pytest.mark.unit
def test_texto_centrado_004():
    # prep
    string_utils = StringUtils()
    texto = 'hola'
    cant_caracteres = 7

    # run
    results = string_utils.texto_centrado(texto, cant_caracteres)

    # results
    assert '  hola ' == results


@pytest.mark.unit
def test_texto_centrado_005():
    # prep
    string_utils = StringUtils()
    texto = 'hola'
    cant_caracteres = 8

    # run
    results = string_utils.texto_centrado(texto, cant_caracteres)

    # results
    assert '  hola  ' == results


@pytest.mark.unit
def test_cortar_texto_001():
    # prep
    string_utils = StringUtils()
    text = '  hola  '
    cant_max = 7

    # run
    results = string_utils.cortar_texto(text, cant_max)

    # results
    assert '  hola ' == results


@pytest.mark.unit
def test_cortar_texto_002():
    # prep
    string_utils = StringUtils()
    text = None
    cant_max = 4

    # run
    results = string_utils.cortar_texto(text, cant_max)

    # results
    assert (results is None)


@pytest.mark.unit
def test_cortar_texto_003():
    # prep
    string_utils = StringUtils()
    text = 'hola'
    cant_max = 3

    # run
    results = string_utils.cortar_texto(text, cant_max)

    # results
    assert ('hol' == results)


@pytest.mark.unit
def test_cortar_texto_004():
    # prep
    string_utils = StringUtils()
    text = '  hola  '
    cant_max = 10

    # run
    results = string_utils.cortar_texto(text, cant_max)

    # results
    assert ('  hola    ' == results)


@pytest.mark.unit
def test_justificar_texto_001():
    # prep
    string_utils = StringUtils()
    text = 'hola'
    cant_caracteres = 7

    # run
    results = string_utils.justificar_texto(text, cant_caracteres)

    # results
    assert ('   hola' == results)


@pytest.mark.unit
def test_justificar_texto_002():
    # prep
    string_utils = StringUtils()
    text = 'holahola'
    cant_caracteres = 8

    # run
    results = string_utils.justificar_texto(text, cant_caracteres)

    # results
    assert (text == results)


@pytest.mark.unit
def test_justificar_texto_003():
    # prep
    string_utils = StringUtils()
    text = 'holahola'
    cant_caracteres = 7

    # run
    try:
        string_utils.justificar_texto(text, cant_caracteres)
        assert False
    except Exception as e:
        assert ('boludo' in str(e))


@pytest.mark.unit
def test_justificar_texto_004():
    # prep
    string_utils = StringUtils()
    text = None
    cant_caracteres = 4

    # run
    results = string_utils.justificar_texto(text, cant_caracteres)

    # results
    assert (results is None)


@pytest.mark.unit
def test_normalizar_texto_001():
    # prep
    string_utils = StringUtils()
    text = 'hola'
    cant_caracteres = 7

    # run
    results = string_utils.normalizar_texto(text, cant_caracteres)

    # results
    assert ('hola   ' == results)


@pytest.mark.unit
def test_normalizar_texto_002():
    # prep
    string_utils = StringUtils()
    text = 'holahola'
    cant_caracteres = 8

    # run
    results = string_utils.normalizar_texto(text, cant_caracteres)

    # results
    assert (text == results)


@pytest.mark.unit
def test_normalizar_texto_003():
    # prep
    string_utils = StringUtils()
    text = 'holahola'
    cant_caracteres = 7

    # run
    try:
        string_utils.normalizar_texto(text, cant_caracteres)
        assert False
    except Exception as e:
        assert ('boludo' in str(e))


@pytest.mark.unit
def test_normalizar_texto_004():
    # prep
    string_utils = StringUtils()
    text = None
    cant_caracteres = 4

    # run
    results = string_utils.normalizar_texto(text, cant_caracteres)

    # results
    assert (results is None)
