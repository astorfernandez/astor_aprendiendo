import unittest
from strings.StringUtils import StringUtils


class TestUtils(unittest.TestCase):

    def test_texto_centrado_001(self):
        # prep
        string_utils = StringUtils()
        texto = 'hola'
        cant_caracteres = 6

        # run
        results = string_utils.texto_centrado(texto, cant_caracteres)

        # results
        self.assertEqual(' hola ', results)

    def test_texto_centrado_002(self):
        # prep
        string_utils = StringUtils()
        texto = 'hola'
        cant_caracteres = 4

        # run
        results = string_utils.texto_centrado(texto, cant_caracteres)

        # results
        self.assertEqual('hola', results)

    def test_texto_centrado_003(self):
        # prep
        string_utils = StringUtils()
        texto = None
        cant_caracteres = 4

        # run
        results = string_utils.texto_centrado(texto, cant_caracteres)

        # results
        self.assertEqual(None, results)

    def test_texto_centrado_004(self):
        # prep
        string_utils = StringUtils()
        texto = 'hola'
        cant_caracteres = 7

        # run
        results = string_utils.texto_centrado(texto, cant_caracteres)

        # results
        self.assertEqual('  hola ', results)

    def test_texto_centrado_005(self):
        # prep
        string_utils = StringUtils()
        texto = 'hola'
        cant_caracteres = 8

        # run
        results = string_utils.texto_centrado(texto, cant_caracteres)

        # results
        self.assertEqual('  hola  ', results)

    def test_cortar_texto_001(self):
        # prep
        string_utils = StringUtils()
        text = '  hola  '
        cant_max = 7

        # run
        results = string_utils.cortar_texto(text, cant_max)

        # results
        self.assertEqual('  hola ', results)

    def test_cortar_texto_002(self):
        # prep
        string_utils = StringUtils()
        text = None
        cant_max = 4

        # run
        results = string_utils.cortar_texto(text, cant_max)

        # results
        self.assertEqual(None, results)

    def test_cortar_texto_003(self):
        # prep
        string_utils = StringUtils()
        text = 'hola'
        cant_max = 3

        # run
        results = string_utils.cortar_texto(text, cant_max)

        # results
        self.assertEqual('hol', results)

    def test_cortar_texto_004(self):
        # prep
        string_utils = StringUtils()
        text = '  hola  '
        cant_max = 10

        # run
        results = string_utils.cortar_texto(text, cant_max)

        # results
        self.assertEqual('  hola    ', results)

    def test_justificar_texto_001(self):
        # prep
        string_utils = StringUtils()
        text = 'hola'
        cant_caracteres = 7

        # run
        results = string_utils.justificar_texto(text, cant_caracteres)

        # results
        self.assertEqual('   hola', results)

    def test_justificar_texto_002(self):
        # prep
        string_utils = StringUtils()
        text = 'holahola'
        cant_caracteres = 8

        # run
        results = string_utils.justificar_texto(text, cant_caracteres)

        # results
        self.assertEqual(text, results)

    def test_justificar_texto_003(self):
        # prep
        string_utils = StringUtils()
        text = 'holahola'
        cant_caracteres = 7

        # run
        try:
            string_utils.justificar_texto(text, cant_caracteres)
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue('boludo' in str(e))

    def test_justificar_texto_004(self):
        # prep
        string_utils = StringUtils()
        text = None
        cant_caracteres = 4

        # run
        results = string_utils.justificar_texto(text, cant_caracteres)

        # results
        self.assertEqual(None, results)

    def test_normalizar_texto_001(self):
        # prep
        string_utils = StringUtils()
        text = 'hola'
        cant_caracteres = 7

        # run
        results = string_utils.normalizar_texto(text, cant_caracteres)

        # results
        self.assertEqual('hola   ', results)

    def test_normalizar_texto_002(self):
        # prep
        string_utils = StringUtils()
        text = 'holahola'
        cant_caracteres = 8

        # run
        results = string_utils.normalizar_texto(text, cant_caracteres)

        # results
        self.assertEqual(text, results)

    def test_normalizar_texto_003(self):
        # prep
        string_utils = StringUtils()
        text = 'holahola'
        cant_caracteres = 7

        # run
        try:
            string_utils.normalizar_texto(text, cant_caracteres)
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue('boludo' in str(e))

    def test_normalizar_texto_004(self):
        # prep
        string_utils = StringUtils()
        text = None
        cant_caracteres = 4

        # run
        results = string_utils.normalizar_texto(text, cant_caracteres)

        # results
        self.assertEqual(None, results)

