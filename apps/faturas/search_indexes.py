from haystack import indexes

from .models import Fatura


class FaturaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr="user")
    numero = indexes.IntegerField(model_attr="id")
    pago = indexes.BooleanField(model_attr="pago")
    data_vencimento = indexes.DateField(model_attr="data")
    model_verbose = indexes.CharField(model_attr="_meta__verbose_name_plural")

    def get_model(self):
        return Fatura

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
