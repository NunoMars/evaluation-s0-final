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
            clairvoyantMessage(data.messages);
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