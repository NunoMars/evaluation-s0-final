from django.shortcuts import render

from django.utils.translation import gettext as _
from random import choice as ch
from .models import SentencesFr


def get_random_sentence(model):
    sentences = model.objects.all()
    return ch(sentences).sentence

def ball8(request):
    if request.method == "GET" and request.GET.get("bouton_submit"):
        user_question = request.GET["question"]
        page_title = "ORACLE"
        ball8_message = get_random_sentence(SentencesFr)
        return render(request, "ball8/ball8.html", {
            "page_title": page_title,
            "user_question": user_question,
            "ball8_message": ball8_message
        })
    return render(request, "ball8/ball8.html")
