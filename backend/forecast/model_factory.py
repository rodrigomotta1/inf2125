from forecast.forecast_models import ModeloDePrevisaoImagem, ModeloDePrevisaoSerie

class FactoryModeloDePrevisao:
    """
    Classe fábrica para criar instâncias de modelos de previsão com base no nome e parâmetros fornecidos.
    """

    @staticmethod
    def gerar_modelo(nome_modelo, parametros=None):
        """
        Cria e retorna uma instância de um modelo de previsão.
        :param nome_modelo: Nome do modelo a ser instanciado. Ex.: 'imagem', 'serie'
        :param parametros: Dicionário com parâmetros específicos do modelo.
        :return: Instância do modelo de previsão.
        """
        if nome_modelo == "imagem":
            return ModeloDePrevisaoImagem(nome_modelo="Previsão por Imagem", parametros=parametros)
        elif nome_modelo == "serie":
            return ModeloDePrevisaoSerie(nome_modelo="Previsão por Série Temporal", parametros=parametros)
        else:
            raise ValueError(f"Modelo de previsão '{nome_modelo}' não é suportado.")

