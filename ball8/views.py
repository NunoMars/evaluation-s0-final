from django.shortcuts import render

from django.utils.translation import gettext as _
from random import choice as ch
from .models import SentencesFr


def ball8(request):
    args = {}
    model = SentencesFr
    if request.method == "GET" and request.GET.get("bouton_submit"):

        user_question = request.GET["question"]
        page_title = "ORACLE"
        args["page_title"] = page_title
        args["user_question"] = user_question

        sentences = model.objects.all()
        rand_message = ch(sentences)

        ball8_message = rand_message.sentence
        args["ball8_message"] = ball8_message

    return render(request, "ball8/ball8.html", args)
