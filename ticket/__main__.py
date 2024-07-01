from ticket.Ticket import Ticket


def main():
    order = list()

    order.append({
        'product': 'burguer',
        'amount': 3,
        'unit_price': 100
    })

    order.append({
        'product': 'hotdog',
        'amount': 2,
        'unit_price': 20
    })

    order.append({
        'product': 'icecream',
        'unit_price': 70
    })

    ticket = Ticket()

    ticket.print_ticket(order)


if __name__ == "__main__":
    main()
