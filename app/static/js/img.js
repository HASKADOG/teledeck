const canvas = document.getElementById('img');
const ctx = canvas.getContext('2d');

var template_one = new Image();
template_one.src = '/static/template_img/tmp1_render.png';

var template_two = new Image();
template_two.src = '/static/template_img/tmp2_render.png';

var template_three = new Image();
template_three.src = '/static/template_img/tmp3_render.png';

var template_four = new Image();
template_four.src = '/static/template_img/tmp4_render.png';

var template_one_alpha = new Image();
template_one_alpha.src = '/static/template_img/tmp1_alpha.png';

var template_two_alpha = new Image();
template_two_alpha.src = '/static/template_img/tmp2_alpha.png';

var template_three_alpha = new Image();
template_three_alpha.src = '/static/template_img/tmp3_alpha.png';

var template_four_alpha = new Image();
template_four_alpha.src = '/static/template_img/tmp4_alpha.png';

template_one.onload = function () {
    render(document.getElementById('template-choose'), 0);
}




function render(template_num, is_alpha) {
    var template_choose = template_num;
    var template = template_choose.options[template_choose.selectedIndex].value;
    var red = document.getElementById('text_in_red');


    if ((template == 'one') && (is_alpha == 0)) {
        canvas.width = template_one.width;
        canvas.height = template_one.height;
        red.value = '';
        ctx.drawImage(template_one, 0, 0);
    }

    if ((template == 'two') && (is_alpha == 0)) {
        canvas.width = template_two.width;
        canvas.height = template_two.height;

        ctx.drawImage(template_two, 0, 0);
    }

    if ((template == 'three') && (is_alpha == 0)) {
        canvas.width = template_three.width;
        canvas.height = template_three.height;
        red.value = '';
        ctx.drawImage(template_three, 0, 0);
    }

    if ((template == 'four') && (is_alpha == 0)) {
        canvas.width = template_four.width;
        canvas.height = template_four.height;
        red.value = '';
        ctx.drawImage(template_four, 0, 0);
    }

    if ((template == 'one') && (is_alpha == 1)) {
        red.value = '';
        ctx.drawImage(template_one_alpha, 0, 0);
    }

    if ((template == 'two') && (is_alpha == 1)) {


        ctx.drawImage(template_two_alpha, 0, 0);
    }

    if ((template == 'three') && (is_alpha == 1)) {

        red.value = '';
        ctx.drawImage(template_three_alpha, 0, 0);
    }

    if ((template == 'four') && (is_alpha == 1)) {

        red.value = '';
        ctx.drawImage(template_one_alpha, 0, 0);
    }


}


function merge(show_alerts = 1) {
    var files = document.getElementById('image_in').files[0]; // input file
    var template_choose = document.getElementById('template-choose');
    var template = template_choose.options[template_choose.selectedIndex].value;


    fr = new FileReader();
    fr.onload = function () {
        var doggo = new Image();
        doggo.onload = function () {
            if ((template == 'two') && (((doggo.width > 1680) || (doggo.height > 460)) || ((doggo.width < 1680) || (doggo.height < 460)))) {
                if (show_alerts == 1) {
                    alert('Ваше изображение не соответсвует рекомендуемому разрешению. Вставка может сработать некорректно!');
                }
            }
            if ((template != 'two') && (((doggo.width > 1680) || (doggo.height > 570)) || ((doggo.width < 1680) || (doggo.height < 570)))) {
                if (show_alerts == 1) {
                    alert('Ваше изображение не соответсвует рекомендуемому разрешению. Вставка может сработать некорректно!');
                }
            }
            ctx.drawImage(doggo, 118, 144);
            draw_text();
            //render(document.getElementById('template-choose'), 1);


        }
        doggo.src = fr.result;
    }
    fr.readAsDataURL(files);
}


function uniq(show_alerts = 1) {
    var files = document.getElementById('image_uniq').files[0]; // input file



    fr = new FileReader();
    fr.onload = function () {
        var doggo = new Image();
        doggo.onload = function () {
            if (((doggo.width > 1920) || (doggo.height > 1080)) || ((doggo.width < 1920) || (doggo.height < 1080))) {

                    alert('Ваше изображение не соответсвует рекомендуемому разрешению. Требуется изображение 1920*1080');

            }
            else {
                            ctx.drawImage(doggo, 0, 0);

            }


            //render(document.getElementById('template-choose'), 1);


        }
        doggo.src = fr.result;
    }
    fr.readAsDataURL(files);
}






      function wrapText(context, text, x, y, maxWidth, lineHeight) {
        var words = text.split(' ');
        var line = '';

        for(var n = 0; n < words.length; n++) {
          var testLine = line + words[n] + ' ';
          var metrics = context.measureText(testLine);
          var testWidth = metrics.width;
          if (testWidth > maxWidth && n > 0) {
            context.fillText(line, x, y);
            line = words[n] + ' ';
            y += lineHeight;
          }
          else {
            line = testLine;
          }
        }
        context.fillText(line, x, y);
      }

function draw_text() {
    var head = document.getElementById('head').value;
    var red = document.getElementById('text_in_red').value;
    var body = document.getElementById('body').value;
    var legs = document.getElementById('legs').value;

    var font_choose = document.getElementById('font-choose');
    var font = font_choose.options[font_choose.selectedIndex].value;
    var head_weight_s = document.getElementById('head-weight');
    var head_weight = head_weight_s.options[head_weight_s.selectedIndex].value;

    var red_weight_s = document.getElementById('text_in_red-weight');
    var red_weight = red_weight_s.options[red_weight_s.selectedIndex].value;

    var body_weight_s = document.getElementById('body-weight');
    var body_weight = body_weight_s.options[body_weight_s.selectedIndex].value;
    var legs_weight_s = document.getElementById('legs-weight');
    var legs_weight = legs_weight_s.options[legs_weight_s.selectedIndex].value;


    render(document.getElementById('template-choose'), 1);
    ctx.textBaseline = "middle";
    ctx.font = '60px ' + font + head_weight;
    ctx.textAlign = 'center';

    if (ctx.measureText(head).width > 1680) {
        ctx.fillText('Слишком много символов!', 960, 103);
    }
    else {
        ctx.fillText(head, 960, 103);
    }

    ctx.fillStyle = "#ffffff";
    ctx.font = '90px ' + font + red_weight;

    if (ctx.measureText(red).width > 1680) {
        ctx.fillText('Слишком много символов!', 960, 645);
    }
    else {
        ctx.fillText(red, 960, 645);
    }

    ctx.fillStyle = "#000000";
    ctx.font = '30px ' + font + body_weight;

    wrapText(ctx, body, 960, 735, 1680, 40);


    ctx.font = '60px ' + font + legs_weight;
    wrapText(ctx, legs, 960, 850, 1680, 90);






}

var head_w = '', red_w = '', body_w = '', legs_w = '';


function change_weight() {
    var font_choose = document.getElementById('font-choose');
    var font = font_choose.options[font_choose.selectedIndex].value;
    var head_weight_s = document.getElementById('head-weight');
    var head_weight = head_weight_s.options[head_weight_s.selectedIndex].value;
    var red_weight_s = document.getElementById('text_in_red-weight');
    var red_weight = red_weight_s.options[red_weight_s.selectedIndex].value;
    var body_weight_s = document.getElementById('body-weight');
    var body_weight = body_weight_s.options[body_weight_s.selectedIndex].value;
    var legs_weight_s = document.getElementById('legs-weight');
    var legs_weight = legs_weight_s.options[legs_weight_s.selectedIndex].value;

    $("#font-choose").addClass(font)

    $("#head-weight").removeClass(head_w)
    $(".head-regular").removeClass(head_w)
    $(".head-bold").removeClass(head_w)
    $(".head-italic").removeClass(head_w)
    head_w = font+head_weight;
    $("#head-weight").addClass(font+head_weight)
    $(".head-regular").addClass(font+head_weight)
    $(".head-bold").addClass(font+head_weight)
    $(".head-italic").addClass(font+head_weight)

    $("#text_in_red-weight").removeClass(red_w)
    $(".text_in_red-regular").removeClass(red_w)
    $(".text_in_red-bold").removeClass(red_w)
    $(".text_in_red-italic").removeClass(red_w)
    red_w = font+red_weight;
    $("#text_in_red-weight").addClass(font+red_weight)
    $(".text_in_red-regular").addClass(font+red_weight)
    $(".text_in_red-bold").addClass(font+red_weight)
    $(".text_in_red-italic").addClass(font+red_weight)

    $("#body-weight").removeClass(body_w)
    $(".body-regular").removeClass(body_w)
    $(".body-bold").removeClass(body_w)
    $(".body-italic").removeClass(body_w)
    body_w = font+body_weight;
    $("#body-weight").addClass(font+body_weight)
    $(".body-regular").addClass(font+body_weight)
    $(".body-bold").addClass(font+body_weight)
    $(".body-italic").addClass(font+body_weight)

    $("#legs-weight").removeClass(legs_w)
    $(".legs-regular").removeClass(legs_w)
    $(".legs-bold").removeClass(legs_w)
    $(".legs-init").removeClass(legs_w)
    legs_w = font+legs_weight;
    $("#legs-weight").addClass(font+legs_weight)
    $(".legs-regular").addClass(font+legs_weight)
    $(".legs-bold").addClass(font+legs_weight)
    $(".legs-init").addClass(font+legs_weight)

}

$(document).ready(function (){
    $('.font_loader').addClass('font-hider')
});

$('#head').keyup(function () {
    draw_text()
});

$('#text_in_red').keyup(function () {
    draw_text()
});

$('#body').keyup(function () {
    draw_text()
});

$('#legs').keyup(function () {
    draw_text()
});

function sec_tmp() {
    var template_choose = document.getElementById('template-choose');
    var template = template_choose.options[template_choose.selectedIndex].value;
    var red = document.getElementById('text_in_red');

    if (template == 'two'){
        $('#text_in_red').removeClass('font-hider')
        $('#text_in_red-weight').removeClass('font-hider')
        $('#red_br').removeClass('font-hider')

    }
    else {
        $('#text_in_red').addClass('font-hider')
        $('#text_in_red-weight').addClass('font-hider')
        $('#red_br').addClass('font-hider')
        red.value = "";
    }
}