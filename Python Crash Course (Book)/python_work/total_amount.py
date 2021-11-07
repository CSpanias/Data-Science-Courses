def total_amount_net(net_session, total_sessions, VAT = 0.2):
    """
    Calculates the total_amount that needs to be paid, and prints seperately
    the net_total, vat_total and gross_total.
    """

    vat_session = net_session * VAT
    vat_total = vat_session * total_sessions

    
    gross_session = net_session + vat_session
    gross_total = gross_session * total_sessions

    net_total = net_session * total_sessions

    print(f'The amounts per session is: ')
    print(f'\tNet: {net_session}\n\tGross: {gross_session}\n\tVat: {vat_session}')

    print(f'The total amounts are: ')
    print(f'\tNet: {net_total}\n\tGross: {gross_total}\n\tVat: {vat_total}.')


def total_amount_gross(gross_session, total_sessions, VAT=0.2):
    """
    Calculates the total_amount that needs to be paid, and prints seperately
    the net_total, vat_total and gross_total.
    """

    # Caclulate the net amount per session
    net_session = gross_session/(1.2)
    # Calculate the net total amount for all sessions
    net_total = net_session*total_sessions
    # Calculate the vat amount per ssion
    vat_session = net_session*VAT
    # Calculate the vat total amount for all sessions
    vat_total = vat_session*total_sessions

    # Calculate the gross total amount for all sessions
    gross_total = gross_session * total_sessions

    print(f'The amounts per session is: ')
    print(f'\tNet: {net_session}\n\tGross: {gross_session}\n\tVat: {vat_session}')

    print(f'The total amounts are: ')
    print(f'\tNet: {net_total}\n\tGross: {gross_total}\n\tVat: {vat_total}.')