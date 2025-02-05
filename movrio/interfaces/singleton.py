from abc import ABC

class Singleton(ABC):
    """
    Classe base abstrata que implementa o padrão Singleton.
    Todas as subclasses compartilharão a mesma instância.
    """
    _instances = {}  # Dicionário para armazenar instâncias por classe

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)
        return cls._instances[cls]