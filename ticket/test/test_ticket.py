import os

import pytest

from ticket.Ticket import Ticket


@pytest.mark.integration
def test_ticket_001():
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

    ticket = Ticket(a_archivo=False)

    ticket.imprimir_ticket(pedido)
    ticket.ticket_content
    ticket_splitted = ticket.ticket_content.split('\n')
    #self.assertTrue('PIZZA FORA' in ticket_splitted[0])
    assert 'PIZZA FORA' in ticket_splitted[0]
    #self.assertTrue( in ticket_splitted[])
    linea = ticket_splitted[6]
    items_linea = linea.split()
    #self.assertTrue(in ticket_splitted[\n])
