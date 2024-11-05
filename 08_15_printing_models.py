

def print_models(unprinted_models, completed_models):
    """Simulate printing each model until there are no unprinted models."""
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}")
        completed_models.append(current_model)

def show_completed_models(completed_models):
    """Show all the models that have been printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"- {model}")


