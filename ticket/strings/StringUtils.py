class StringUtils:

    def centred_text(self, text, character_amount):
        if not text:
            return text

        ret = text
        while len(ret) < character_amount:
            ret = ' ' + ret + ' '

        if len(ret) > character_amount:
            ret = ret[0:character_amount]
        return ret

    def cut_text(self, text, max_char):
        """
        Function that cuts up to max_char the input text

        input                    ->     output
        -----------------------------------------------
        'hello'                  -> 'hello            '
        '01234567890123456789'   -> '0123456789012345'
        """
        ret = text
        if ret is None:
            return ret

        if len(ret) == max_char:
            return ret

        if len(ret) > max_char:
            return ret[0:max_char]

        while len(ret) < max_char:
            ret = ret + ' '

        return ret

    def justify_text(self, text, character_amount):
        ret = text
        if ret is None:
            return ret
        if len(ret) > character_amount:
            message = 'Error'
            raise Exception(message)
        while len(ret) < character_amount:
            ret = ' ' + ret
        return ret

    def normalize_text(self, text, character_amount):
        ret = text
        if ret is None:
            return ret
        if len(ret) > character_amount:
            message = 'Error'
            raise Exception(message)
        while len(ret) < character_amount:
            ret = ret + ' '
        return ret
