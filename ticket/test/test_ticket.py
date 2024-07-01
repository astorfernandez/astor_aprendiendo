import os

import pytest

from ticket.Ticket import Ticket


@pytest.mark.integration
def test_ticket_001():
    order = list()

    order.append({
        'product': 'burguer',
        'amount': 3,
        'unit_price': 100
    })

    order.append({
        'product': 'pancho',
        'amount': 2,
        'unit_price': 20
    })

    order.append({
        'product': 'sundae',
        'unit_price': 70
    })

    ticket = Ticket(a_archivo=False)

    ticket.print_ticket(order)
    ticket.ticket_content
    ticket_splitted = ticket.ticket_content.split('\n')
    # self.assertTrue('PIZZA FORA' in ticket_splitted[0])
    assert 'PIZZA FORA' in ticket_splitted[0]
    # self.assertTrue( in ticket_splitted[])
    linea = ticket_splitted[6]
    items_linea = linea.split()
    # self.assertTrue(in ticket_splitted[\n])
