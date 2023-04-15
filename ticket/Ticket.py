from dates.DateUtils import DateUtils
from strings.StringUtils import StringUtils
from files.FileUtils import FileUtils
from exchange_rate.ExchangeRateUtils import ExchangeRateUtils
from Constants import OUTPUT_PATH


class Ticket:
    LINEA = '---------------------------------------------'

    def __init__(self, a_archivo=True):
        self.a_archivo = a_archivo
        self.ticket_content = ''
        self.string_utils = StringUtils()
        self.date_utils = DateUtils()
        self.exchange_rate_utils = ExchangeRateUtils()

    def imprimir_ticket(self, pedidos):
        fecha = self.date_utils.get_date_as_str()
        self.imprimir_encabezado(fecha)
        total = 0

        for item in pedidos:
            # extraigo los atributos del item
            precio_unitario = item['precio_unitario']
            cantidad = item['cantidad'] if 'cantidad' in item else 1
            producto = item['producto']

            # realizo los calculos
            sub_total = precio_unitario * cantidad
            total = total + sub_total
            exchange_rate = self.exchange_rate_utils.get_exchange_rate('usd')
            total_usd = total / exchange_rate
            rounded_div = round(total_usd, 2)

            # imprimo la linea
            linea_item = self.armar_linea(cantidad, producto, precio_unitario, sub_total)
            self.print_store(linea_item)

#        self.imprimir_linea_total(total)
        self.imprimir_descuento(total,rounded_div)
        self.imprimir_linea_total(total, rounded_div)
        self.imprimir_descuento(total, rounded_div)

        fecha_formateada = fecha.replace('/', '-').replace(' ', '-').replace(':', '-')
        file_path = fecha_formateada + '.txt'
        content = self.ticket_content
        if self.a_archivo:
            self.archivar(OUTPUT_PATH, file_path, content)

    def archivar(self, ticket_dir, file_path, content):
        ticket_dir = OUTPUT_PATH
        file_utils = FileUtils()
        file_utils.write_file(content, ticket_dir, file_path)

    def print_store(self, text):
        text_aux = text.replace('\t', '    ')
        self.ticket_content = self.ticket_content + text_aux + '\n'
        print(text)

    def imprimir_encabezado(self, fecha):
        cant_caract = len(self.LINEA)
        fecha_centrada = self.string_utils.texto_centrado(fecha, cant_caract)
        titulo = self.string_utils.texto_centrado('PIZZA FORA', cant_caract)
        lugar = self.string_utils.texto_centrado('Liniers 1959-Tigre', cant_caract)

        linea_encabezado = self.armar_linea('Cant', 'Detalle', 'p.Unit.', 'Importe')

        self.print_store(titulo)
        self.print_store(lugar)
        self.print_store(fecha_centrada)
        self.print_store(self.LINEA)
        self.print_store(linea_encabezado)
        self.print_store(self.LINEA)

    def armar_linea(self, cant, detalle, precio_unitario, importe):
        cant_norm = self.string_utils.normalizar_texto(str(cant), 8)
        detalle_norm = self.string_utils.normalizar_texto(detalle, 19)
        precio_unitario_norm = self.string_utils.normalizar_texto(str(precio_unitario), 11)
        importe_norm = self.string_utils.normalizar_texto(str(importe), 10)
        linea = cant_norm + detalle_norm + precio_unitario_norm + importe_norm
        return linea

    def imprimir_linea_total(self, total, rounded_div):
        self.print_store(self.LINEA)
        longitud_linea = len(self.LINEA)
        total_justificado = self.string_utils.justificar_texto('$    ' + str(total), longitud_linea)
        total_justificado_usd = self.string_utils.justificar_texto('usd $    ' + str(rounded_div), longitud_linea)
        self.print_store(total_justificado)
        self.print_store(total_justificado_usd)

    def imprimir_descuento(self, total, rounded_div):
        if total >= 1000:
            cant_caracteres = len(self.LINEA)
            texto_justificado = self.string_utils.justificar_texto('10% de descuento', cant_caracteres)
            self.print_store(texto_justificado)
