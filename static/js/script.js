var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
    $messages.mCustomScrollbar();
    firstClairvoyantMessage();
});

function updateScrollbar() {
    $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
        scrollInertia: 10,
        timeout: 0
    });
}

function clairvoyantMessage(message) {
    $('.message.loading').remove();
    $('<div class="message new"><figure class="avatar"><img src= "../static/img/voyante.jpg"/></figure>' + message + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
}

function setDate() {
    d = new Date()
    if (m != d.getMinutes()) {
        m = d.getMinutes();
        $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
        $('<div class="checkmark-sent-delivered">&check;</div>').appendTo($('.message:last'));
        $('<div class="checkmark-read">&check;</div>').appendTo($('.message:last'));
    }
}

function insertMessage() {
    msg = $('.message-input').val();
    if ($.trim(msg) == '') {
        return false;
    }
    escapeHtml(msg);
    $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    $('.message-input').val(null);
    updateScrollbar();
    $('<div class="message loading new"><figure class="avatar"><img src="../static/img/voyante.jpg"/></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();
    getMessageClairvoyant(msg);
};

function escapeHtml(msg) {
    return msg
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};
var token = '{{csrf_token}}';

function getMessageClairvoyant(msg) {
    $.ajax({
        type: 'POST',
        headers: { "X-CSRFToken": token },
        url: '{% url "clairvoyante" %}',
        dataType: 'json',
        data: {
            messageInput: msg,
        },
        success: function(data) {
            if (data.subject == "menu") {
                menuChoices(data);
            }
            if (data.subject == "one_card") {
                oneCardResponse(data);
                recordChoice();
            }
            if (data.subject == "rec_no") {
                menuChoices(data);
            }
            if (data.subject == "sorry") {
                clairvoyantMessage(data.message);
            }
            if (data.subject == "rec_ok") {
                clairvoyantMessage(data.message);
            }
            if (data.subject == "cut") {
                displayMessageCut(data);
            }
            if (data.subject == "choose_deck") {
                chooseCutDeck(data);
            }
            if (data.subject == "final_response") {
                clairvoyantMessage(data.message.final_response_tittle);
                responseCard(data.message.response_card)
                recordChoice();
            }
            if (data.subject == "rec_response") {
                clairvoyantMessage(data.messages);
            }
            if (data.subject == "Error_record") {
                clairvoyantMessage(data.message);
            }
            if (data.subject == "succes_rec") {
                clairvoyantMessage(data.message);
            }
        },
    });
};

$('.message-submit').click(function() {
    insertMessage();
});

$(window).on('keydown', function(e) {
    if (e.which == 13) {
        insertMessage();
        return false;
    };
});

$('#message-form').submit(function(event) {
    event.preventDefault();
    insertMessage();
});

function firstClairvoyantMessage() {
    if ($('.message-input').val() != '') {
        return false;
    }
    sentence = "Bonjour, je suis Mme T, votre voyante virtuelle. Je vous propose d'éclairer votre avenir a l'aide du tarot! Mais avant tout, il nous faut faire connaissance. Quel est votre prénom svp?"

    var msg = "<div class='col'><div class='cta-inner text-center rounded'>" +
        "<p class='mb-0'>" +
        sentence +
        "</p> "
    clairvoyantMessage(msg);
};

function displayMessageCut(data) {
    message_cut = "<div class='cta-inner text-center rounded'>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h4>" + "Merci beaucoup " + data.user_name.charAt(0).toUpperCase() + data.user_name.slice(1) + " !</h4></p>" +
        " <p>" + "Encore une chose svp!" + "</p>" +
        " <p>" + "Cliquez afin de couper le jeu de cartes!" +
        "</p></div></div>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageCut();'/></div>" +
        "</div></div></div>"
    clairvoyantMessage(message_cut);
};

function recordChoice() {
    msg = "<div class='cta-inner text-center rounded'>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h3>" + "Voulez-vous enregistrer le tirage?" + "</h3></p></div></div>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h6>" + "SAUVEGARDER" + "</h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageRecYes();'/></p></div>" +
        "<div class='col'>" + "<p><h6>" + "NON" + "</h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageRecNo();'/></p></div>" +
        "</div></div>"
    clairvoyantMessage(msg);
};

function menuChoices(data) {
    menu = "<div class='cta-inner text-center rounded'>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h6>" + "Merci beaucoup " + data.user_name.charAt(0).toUpperCase() + data.user_name.slice(1) + " !</h6></p>" +
        "<p><h5>" + " Je mélange les lâmes du tarot..." + "</h5></p></div></div>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h5>" + "Choisissiez le domaine de la question!" + "</h5></p>" +
        "<p><h6>" + "Cliquez sur le paquet de cartes svp!" + "</h6></p></div></div>" +
        "<div class='row'>" +
        "<div class='col'>" +
        "<p><h6>" + "TIRAGE AMOUR" + "<h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageLove();'/></p></div>" +
        "<div class='col'>" +
        "<p><h6>" + "TIRAGE TRAVAIL" + "</h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageWork();'/></p></div>" +
        "<div class='col'>" +
        "<p><h6>" + " TIRAGE GENERAL" + "</h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageGen();'/></p></div>" +
        "<div class='col'>" +
        "<p><h6>" + "TIRAGE RAPIDE" + "</h6></p>" +
        "<p><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageOneCard();'/></p></div>" +
        "</div></div>"
    clairvoyantMessage(menu);
};

function oneCardResponse(data) {
    card_response = "<div class='col cta-inner text-center rounded'>" +
        "<h2>" + data.user_name.charAt(0).toUpperCase() + data.user_name.slice(1) + " vois-ci ce que le Tarot a vous dire!" + "</h2>" +
        "<a href='#'><img class='img-fluid card' src='" + '/static/img/cards/Back.jpg' + "'" +
        "onmouseover=" + '"this.src=' + "'" + data.card_image + "'" + '"' +
        " alt='' width='18%'/>" +
        "<p><h3>" + data.card_name.charAt(0).toUpperCase() + data.card_name.slice(1) + "</h3></p>" +
        "<div class='mb-0'><h3>" + "Attention" + "</h3></div>" +
        "<p class='mb-0'>" + data.card_signification_warnings + "</p>" +
        "<div class='mb-0'><h4>" + "En general" + "</h4></div>" +
        "<p class='mb-0'>" + data.card_signification_gen + "</p>" +
        "<div class='mb-0'><h4>" + "En amour" + "</h4></div>" +
        "<p class='mb-0'>" + data.card_signification_love + "</p>" +
        "<div class='mb-0'><h4>" + "Dans le travail" + "</h4></div>" +
        "<p class='mb-0'>" + data.card_signification_work + "</p>" +
        "</div>"
    clairvoyantMessage(card_response);
};

function chooseCutDeck(data) {
    deck_choice = "<div class='col'><div class='cta-inner text-center rounded'>" +
        "<p class='mb-0'><h4>" + "Merci !" + "</h4></p>" +
        "<p class='mb-0'>" + "On a donc deux paquets de cartes!" + "</p>" +
        "<p class='mb-0'>" + "Cliques sur celui de votre choix svp!" + "</p></div></div>" +
        "<div class='row'>" +
        "<div class='col''><div class='cta-inner text-center rounded'>" +
        "<h4>Ce paquet a " + data.len_left_deck + " cartes!" +
        "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageLeft();'/></div></div></div>" +
        "<div class='col''><div class='cta-inner text-center rounded'>" +
        "<h4>Celui ci a " + data.len_right_deck + " cartes!" +
        "<div class='mb-0'><input id='bouton_card' type='submit' class='bouton_card img-fluid' onClick='sendMessageRight();'/></div></div></div>" +
        "</div>"
    clairvoyantMessage(deck_choice);
};

function responseCard(data) {
    response_card_message = "<div class='col cta-inner text-center rounded'>" +
        "<h3>" + data.user_name.charAt(0).toUpperCase() + data.user_name.slice(1) +
        " vois-ci votre votre message, ce que le Tarot a vous dire!</h3>" +
        "<a href='#'><img class='img-fluid card' src='/static/img/cards/Back.jpg'" +
        "onmouseover=" + '"this.src=' + "'" + data.card_image + "'" + '"' +
        " alt='arcana card'/>" +
        "<p><h2>" + data.card_name.charAt(0).toUpperCase() + data.card_name.slice(1) + "</h2></p>" +
        "<div class='mb-0'><h3>" + "Réponse" + "</h3></div>" +
        "<p class='mb-0'>" + data.chosed_theme_signification + "</p>" +
        "<h3>Attention Toutefois</h3>" +
        "<p class='mb-0'>" + data.warnings + "</p>" +
        "</div>"
    clairvoyantMessage(response_card_message)
};


$('.button').click(function() {
    $('.menu .items span').toggleClass('active');
    $('.menu .button').toggleClass('active');
});

function sendMessageLove() {
    getMessageClairvoyant("love");
};

function sendMessageWork() {
    getMessageClairvoyant("work");
};

function sendMessageGen() {
    getMessageClairvoyant("gen");
};

function sendMessageOneCard() {
    getMessageClairvoyant("one");
};

function sendMessageCut() {
    getMessageClairvoyant("cut");
};

function sendMessageLeft() {
    getMessageClairvoyant("left");
};

function sendMessageRight() {
    getMessageClairvoyant("right");
};

function sendMessageRecYes() {
    getMessageClairvoyant("rec");
};

function sendMessageRecNo() {
    getMessageClairvoyant("rec_no");
};

$(window).unload(function() {
    $messages.mCustomScrollbar();
    msg = "Quit"
    getMessageClairvoyant(msg)
});

$('.button').click(function() {
    $('.menu .items span').toggleClass('active');
    $('.menu .button').toggleClass('active');
});