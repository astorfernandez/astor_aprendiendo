class StringUtils:

    def texto_centrado(self, texto, cant_caracteres):
        if not texto:
            return texto

        ret = texto
        while len(ret) < cant_caracteres:
            ret = ' ' + ret + ' '

        if len(ret) > cant_caracteres:
            ret = ret[0:cant_caracteres]
        return ret

    def cortar_texto(self, text, cant_max):
        """
        Funcion que corta hasta cant_max el texto de entrada text

        entrada                 ->  salida
        ------------------------------------------
        'hola'                  -> 'hola            '
        '01234567890123456789'  -> '0123456789012345'
        """
        ret = text
        if ret is None:
            return ret

        if len(ret) == cant_max:
            return ret

        if len(ret) > cant_max:
            return ret[0:cant_max]

        while len(ret) < cant_max:
            ret = ret + ' '

        return ret

    def justificar_texto(self, texto, cant_caracteres):
        ret = texto
        if ret is None:
            return ret
        if len(ret) > cant_caracteres:
            mensaje = 'la cagaste boludo'
            raise Exception(mensaje)
        while len(ret) < cant_caracteres:
            ret = ' ' + ret
        return ret

    def normalizar_texto(self, texto, cant_caracteres):
        ret = texto
        if ret is None:
            return ret
        if len(ret) > cant_caracteres:
            mensaje = 'la cagaste boludo'
            raise Exception(mensaje)
        while len(ret) < cant_caracteres:
            ret = ret + ' '
        return ret
