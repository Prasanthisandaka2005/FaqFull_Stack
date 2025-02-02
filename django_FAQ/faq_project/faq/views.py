from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ

@api_view(["GET"])
def get_faqs(request):
    lang = request.GET.get("lang", "en")
    cache_key = f"faqs_{lang}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    faqs = FAQ.objects.all()
    data = [
        {
            "question": faq.get_translated_faq(lang)[0],
            "answer": faq.get_translated_faq(lang)[1] or faq.answer, 
        }
        for faq in faqs
    ]

    cache.set(cache_key, data, timeout=3600)
    return Response(data)
