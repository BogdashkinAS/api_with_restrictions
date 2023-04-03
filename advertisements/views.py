from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['creator', 'created_at']
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    

    def get_permissions(self):
        
        """Получение прав для действий."""
        if self.request.method == 'PATCH':
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
    
   