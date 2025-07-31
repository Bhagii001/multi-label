from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Label
from .serializers import LabelSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    @action(detail=False, methods=['get'])
    def by_language(self, request):
        lang = request.query_params.get('lang', 'en')
        labels = Label.objects.prefetch_related('translations')
        result = {}
        for label in labels:
            translation = label.translations.filter(language_code=lang).first()
            if translation:
                result[label.key] = translation.text
        return Response(result)
