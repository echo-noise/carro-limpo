from haystack import indexes

from apps.clientes.models import Cliente
# from apps.servicos.models import Servico
# from apps.faturas.models import Fatura


class ClienteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr="user")
    nome = indexes.CharField(model_attr="nome")
    telefone = indexes.CharField(model_attr="telefone")
    email = indexes.CharField(model_attr="email")
    documento = indexes.CharField(model_attr="documento")
    placa = indexes.CharField(model_attr="placa")
    marca = indexes.CharField(model_attr="marca")
    modelo = indexes.CharField(model_attr="modelo")
    cor = indexes.CharField(model_attr="cor")
    model_verbose = indexes.CharField(model_attr="_meta__verbose_name_plural",
                                      faceted=True)

    def get_model(self):
        return Cliente

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
