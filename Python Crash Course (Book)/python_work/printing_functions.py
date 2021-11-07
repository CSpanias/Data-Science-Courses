def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Currently printing: {current_design.title()}.')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print(f'\nThe following models have been printed:')
    for design in completed_models:
        print(design.title())