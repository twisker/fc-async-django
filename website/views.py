from django.http import JsonResponse


async def test_view(request):
    return JsonResponse({'hello': 'world'})
