from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@api_view(['GET', 'POST'])
def comenzarJuego(request):
    return Response({
        'stateIntial': [],
    })
