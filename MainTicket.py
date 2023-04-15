from ticket.Ticket import Ticket


if __name__ == '__main__':

    pedido = list()

    pedido.append({
        'producto': 'hamburguesa',
        'cantidad': 3,
        'precio_unitario': 100
    })

    pedido.append({
        'producto': 'pancho',
        'cantidad': 2,
        'precio_unitario': 20
    })

    pedido.append({
        'producto': 'sundae',
        'precio_unitario': 70
    })

    ticket = Ticket()

    ticket.imprimir_ticket(pedido)


