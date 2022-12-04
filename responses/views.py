from django.shortcuts import render

from django.utils.translation import gettext as _
from random import choice as ch
from .models import (
    ResponsesBookPt,
    ResponsesBookFr,
    ResponsesBookEs,
    ResponsesBookEn,
)


def responses(request):
    args = {}

    model = ResponsesBookPt
    sentences = model.objects.all()
    rand_message = ch(sentences)
    args = {"sentence": rand_message}
    if request.method == "GET" and request.GET.get("bouton_submit"):
        bouton = request.GET["new_response"]
        rand_message = ch(sentences)
        args = {"sentence": rand_message}

    return render(request, "responses/responses.html", args)
