from abc import ABC, abstractmethod
import numpy as np


class ModeloDePrevisao(ABC):
    """
    Classe abstrata que define a interface para diferentes modelos de previsão de densidade.
    """

    def __init__(self, nome_modelo, parametros=None):
        """
        Inicializa o modelo com um nome e parâmetros opcionais.
        :param nome_modelo: Nome do modelo.
        :param parametros: Dicionário de parâmetros do modelo (opcional).
        """
        self.nome_modelo = nome_modelo
        self.parametros = parametros or {}

    @abstractmethod
    def processar(self, entrada):
        """
        Método abstrato para processar os dados de entrada e retornar uma previsão.
        Deve ser implementado pelas subclasses.
        :param entrada: Dados de entrada específicos do modelo.
        :return: Previsão calculada pelo modelo.
        """
        pass

    def __str__(self):
        return f"Modelo: {self.nome_modelo}"


class ModeloDePrevisaoImagem(ModeloDePrevisao):
    """
    Modelo de previsão especializado em análise de densidade com base em imagens.
    """

    def processar(self, entrada):
        """
        Processa uma imagem para estimar a densidade de pessoas.
        :param entrada: Imagem no formato numpy array.
        :return: Estimativa de densidade.
        """
        if not isinstance(entrada, np.ndarray):
            raise ValueError("A entrada deve ser uma imagem no formato numpy array.")
        
        # Exemplo simplificado de processamento (usar métodos reais aqui)
        estimativa = entrada.mean() * 10  # Processamento fictício para fins de exemplo
        return round(estimativa)


class ModeloDePrevisaoSerie(ModeloDePrevisao):
    """
    Modelo de previsão especializado em análise de séries temporais.
    """

    def processar(self, entrada):
        """
        Processa dados históricos para prever densidade.
        :param entrada: Lista de valores ou pandas DataFrame com dados históricos.
        :return: Previsão de densidade.
        """
        if not isinstance(entrada, list):
            raise ValueError("A entrada deve ser uma lista de valores ou pandas DataFrame.")
        
        # Exemplo simplificado de previsão (usar métodos reais aqui)
        estimativa = sum(entrada[-5:]) / 5  # Média dos últimos 5 valores
        return round(estimativa)