import json
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from ..models import (
    Variant,
)
from ..serializers import (
    VariantSerializer,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.http import Http404
from django.http.response import JsonResponse

@api_view(['GET'])
@login_required
def snv_search(request, **kwargs):
    """
    """
    json_content = kwargs.get('JSON', False)
    query_params = request.query_params
    if 'query' in query_params:
        variant_id = query_params['query']
    else:
        return Response({"errors":["missing variant_id parameter"]})
#    variant_id = json.loads(request.body)["variant_id"]

    try:
        # Get all relevant information from the database 
        #variant = Variant.objects.get(variant_id=variant_id)
        variants = Variant.objects.filter(variant_id__startswith=variant_id).values('variant_id','id')
    except Variant.DoesNotExist:
        variants = None

    if request.method == 'GET':
        if variants:
            # Only send at most 10 variants
            data_out = {
                "variants": list(variants)[:10],
            }
        else:
            data_out = {
                "variants": [],
            }

        if json_content:
            return JsonResponse(data_out)
        else:
            return Response(data_out)