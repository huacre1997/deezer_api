from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status

from rest_framework.decorators import action


class BaseViewSet(viewsets.ModelViewSet):
    """Modelo Base que heredará a todas nuestras views """

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(updated_by=user)

    @action(detail=True, methods=['put'], name='Desactivar Registro')
    def desactivate(self, request, pk=None):
        """
        Método que cambia el estado a False al objeto
        """
        self.instance = self.get_object()
        if self.instance.is_active:
            self.instance.is_active = False
            self.instance.updated_by = self.request.user
            self.instance.save()
            return Response({"message": "Registro eliminado"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No existe ese Registro"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'], name='Restaurar Registro')
    def restore(self, request, pk=None):
        """
        Método que cambia estado a True al objeto
        """
        self.instance = self.get_object()
        if not self.instance.is_active:
            self.instance.is_active = True
            self.instance.updated_by = self.request.user
            self.instance.save()
            return Response({"message": "Registro restaurado"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Ese registro ya se encuentra activo"}, status=status.HTTP_200_OK)
