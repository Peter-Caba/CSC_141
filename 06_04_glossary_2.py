# Creating a glossary dictionary with more terms
glossary = { "Variable": "A storage location identified by a name that holds a value.",
    "Function": "A reusable block of code that performs a specific task.",
    "Loop": "A sequence of instructions that is repeated until a condition is met.",
    "List": "An ordered collection of items, which can be of different types.",
    "Dictionary": "A collection of key-value pairs, where each key is unique.",
    "Class": "A blueprint for creating objects that encapsulate data and behavior.",
    "Object": "An instance of a class that contains data and methods.",
    "Method": "A function defined within a class that operates on instances of that class.",
    "Inheritance": "A mechanism by which one class can inherit attributes and methods from another class.",
    "Syntax": "The set of rules that defines the combinations of symbols that are considered to be correctly structured programs."}


for word, meaning in glossary.items():
    print(f"{word}:\n    {meaning}\n")
