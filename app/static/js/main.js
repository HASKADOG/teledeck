$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
        items: 1
    });
});

$(document).ready(function () {
    $("#mobilka").mask("+7 (999) 99-99-999");
});

$(document).ready(function () {
    $("#mulo").mask("");
});

function validate() {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var name = document.getElementById("name");
    var email = document.getElementById("mulo");
    var tel = document.getElementById("mobilka");

    var name_err = document.getElementById("name_err");
    var email_err = document.getElementById("email_err");
    var mobile_err = document.getElementById("mobile_err");

    if (!name.value) {
        name_err.style.color = "red"
        return false
    }
    name_err.style.color = "white"


    if (!email.value) {
        email_err.style.color = "red"
        return false
    }
    email_err.style.color = "white"


    if (!regex.test(email.value)) {
        email_err.style.color = "red"
        return false
    }

    if (!mobilka.value) {
        mobile_err.style.color = "red"
        return false
    }
    mobile_err.style.color = "white"
    setTimeout(100000000);

    alert('Спасибо за заявку!');

    email_err.style.color = "white"


    return true
}




jQuery(document).ready(function () {
    jQuery('#waste').change(function () {

        let finish_price = parseInt($('#bonus').text());
        let price = parseInt($('#price').text());
        let total = price - finish_price;

        if ($(this).prop('checked')) {
            $('#submit').attr('value', 'Оплатить ' + total);
        } else {
            $('#submit').attr('value', 'Оплатить ' + price);
        }
    });
});

$(document).ready(function () {
    var is_entity = document.getElementById("is_entity");
    var entity = document.getElementById("entity_block");
    var personal = document.getElementById("personal_block");

    if (is_entity.checked) {
        entity.style.display = "";
        personal.style.display = "none";
    }
    else {
        entity.style.display = "none";
        personal.style.display = "";
    }
});

jQuery(document).ready(function () {
    var entity = document.getElementById("entity_block");
    var personal = document.getElementById("personal_block");


    jQuery('#is_entity').change(function () {


        if ($(this).prop('checked')) {
            entity.style.display = "";
            personal.style.display = "none";
        } else {
            entity.style.display = "none";
            personal.style.display = ""
        }
    });
});


$('.header-ham').click(function () {
    $('.menuphka').addClass('avadakedavra')
});
$('.dualshock').click(function () {
    $('.menuphka').removeClass('avadakedavra')
});

$(document).ready(function () {
    $('#update_lk').click(function () {
        $.ajax({
            data: {
                update_lk: 'true',
                username: $('#username').val(),
                second_name: $('#second_name').val(),
                third_name: $('#third_name').val(),
                phone_number: $('#phone_number').val(),
                email: $('#email').val(),
                is_entity: $('#is_entity').val(),
                entity_name: $('#entity_name').val(),
                iin: $('#iin').val(),
                ogrn: $('#ogrn').val()
            },
            type: 'POST',
            url: '/lk'
        })
            .done(function (data) {
                alert(data.response);
            });
    });
});
let start = '';
let clicked_elems = [];
$(document).ready(function () {


    if ($('#track_code').val() != "none") {
        let added_days = document.getElementsByClassName('added_day');
        $.each(added_days, function (index, value) {
            clicked_elems.push(value.getAttribute('data-date').replace(/\./g, "_"));
        });
        alert(clicked_elems);
    }

    $('#moderate').click(function () {
        var canvas = document.getElementById('img');
        var dataurl = canvas.toDataURL();

        if ($('#notify_email').val() == '') {
            alert('Введите email');
        } else {
            var soup = 1;
            //alert(soup + "soup");
        }

        if ($('#is_entity:checked').val() == 'on') {
            if ($('#entity_name').val() == '') {
                alert('Введите название организации');
            } else {
                var uno = 1;
                //alert(uno + "uno");
            }
            if ($('#iin').val() == '') {
                alert('Введите ИИН');
            } else {
                var dos = 1;
                //alert(dos + "dos");
            }
            if ($('#ogrn').val() == '') {
                //alert('Введите ОГРН');
            } else {
                var tres = 1;
                //alert(tres + "tres");
            }
            if (uno == 1 && dos == 1 && tres == 1) {
                var done = 1;
                //alert(done + "done");
            }
        }

        if ($('#is_entity:checked').val() == undefined) {
            if ($('#username').val() == '') {
                alert('Введите имя');
            } else {
                var an = 1;
                //alert(an + "an");
            }
            if ($('#second_name').val() == '') {
                //alert('Введите фамилию');
            } else {
                var tsvai = 1;
                //alert(tsvai + "tsvai");
            }
            if ($('#third_name').val() == '') {
                alert('Введите оттечство');
            } else {
                var dry = 1;
                //alert(dry + "dry");
            }
            if (an == 1 && tsvai == 1 && dry == 1) {
                var done_o = 1;
                //alert(done_o + "done_o");
            }
            var is_ent = 0;
        } else {
            var is_ent = 1;
        }

        if ($('#phone_number').val() == '') {
            alert('Введите номер телефона');
        } else {
            var ph = 1;
            alert(ph + "ph");
        }

        //alert(done);
        //alert(done_o);
        //alert(ph);
        if ((done == 1 || done_o == 1) && ph == 1 && soup == 1) {
            let checked_days = '';
            $.each(clicked_elems, function (index, value) {
                checked_days += value + ',';
                alert(checked_days);
            });
            $.ajax({
                data: {
                    moderate: 'true',
                    username: $('#username').val(),
                    second_name: $('#second_name').val(),
                    third_name: $('#third_name').val(),
                    phone_number: $('#phone_number').val(),
                    notify_email: $('#notify_email').val(),
                    is_entity: is_ent,
                    entity_name: $('#entity_name').val(),
                    iin: $('#iin').val(),
                    ogrn: $('#ogrn').val(),
                    time: checked_days,
                    head: $('#head').val(),
                    body: $('#body').val(),
                    legs: $('#legs').val(),
                    promo: $('#promo').val(),
                    price: $('#price_input').attr('value'),
                    start: start,
                    image: dataurl
                },
                type: 'POST',
                url: '/add_add'
            })
                .done(function (data) {
                    alert(data.response);
                });
        }


    });




    $('#get_ad').click(function () {

        $.ajax({
            data: {
                get_ad: 'true',
                track_code: $('#track_code').val(),
            },
            type: 'POST',
            url: '/payment'
        })
            .done(function (data) {
                $('.place').html(data.ad)
            });
    });




    let month_n = 0;
    let year = 0;

    function draw_clicked() {
        for (let i_day = 1; i_day < 36; i_day++) {
            let day_to_check = document.getElementById('day' + i_day);
            let converted_date = day_to_check.getAttribute('data-date').replace(/\./g, "_");
            if (clicked_elems.indexOf(converted_date) != -1) {
                $('#day'+ i_day).addClass('day_clicked');
            }
            else {
                $('#day'+ i_day).removeClass('day_clicked');
            }
        }
    }

    function organise(response) {
        let i = 0;
        month_n = response.month_n;
        year = response.year;
        start = response.start;
        $('.month').html(response.month);
        $.each(response.days, function (index, value) {
            let id = parseInt(index) + 1;
            $.each(value, function (property, val) {
                if (property == 'number') {
                    $('#day' + id).html(val);
                }
                if (property == 'available') {
                    $('#day' + id).attr('data-available', val);
                    if (val == 0) {
                        $('#day' + id).css('background', 'red');
                        $('#day' + id).css('background', 'red');
                        $('#day' + id).css('cursor', 'default');
                        $('#day' + id).hover(function () {
                            $('#' + id).css('color', 'white');
                        });
                    }
                    else {
                        $('#day' + id).css('cursor', 'pointer');
                    }

                }
                if (property == 'sale') {
                    $('#day' + id).attr('data-sale', val);
                    if (val == '1') {
                        if ($('#day' + id).attr('data-available') == '1') {
                            $('#day' + id).css('background', 'green');
                        }

                    }
                    else if (val == '0' && $('#day' + id).attr('data-available') == '1') {
                        $('#day' + id).css('background', '#1f2227');
                    }
                }
                if (property == 'date') {
                    $('#day' + id).attr('data-date', val);
                }
                if (property == 'next_m') {
                    if (val == 1) {$('#day' + id).css('background', '#1f2227');
                        $('#day' + id).css('cursor', 'pointer');
                        $('#day' + id).attr('data-next', val);
                    }
                }
            });
        });
        draw_clicked();
    }

    $.ajax({
            data: {
                method: 'get_calendar_date',
                button: 'init'
            },
            type: 'POST',
            url: '/api'
        })
            .done(function (data) {
                let resp = data.response;
                organise(resp);
            });



    let calculated_price = 0;


    function calculate_price() {
        let added_days = document.getElementsByClassName('added_day');
        let price = 0;
        let sailed = 0;
        let no_sale = 0;
        let counter = 0;

        $.each(added_days, function (index, value) {
            counter += 1;
            if (value.getAttribute('data-sale') == '1') {
                sailed += 1;
            }
            else {
                price += 1;
            }

        });

        if (price > 0 && sailed == 0) {
            calculated_price = (3000 + (3000*(counter-1)*(100-5)/100));
        }
        else if (sailed > 0 && price == 0) {
            calculated_price = (3000 + (3000*(counter-1)*(100-5)/100))*(100-15)/100;
        }
        else if (price > 0 && sailed > 0) {
            let saled_days_q = 1 - (counter/100*sailed);
            let sale_amount = ((3000 + (3000*(counter-1)*(100-5)/100)) * saled_days_q)/100*15;
            calculated_price = ((3000 + (3000*(counter-1)*(100-5)/100))) - sale_amount;
        }

     }





    $('.day').click(function () {
        let choosen_day = $(this).attr('data-date').replace(/\./g, "_");
        let date = $(this).attr('data-date');


        if ($(this).attr('data-available') == "1") {
            if (clicked_elems.indexOf(choosen_day) != -1) {
                $("#"+choosen_day+"_picked").remove();
                delete clicked_elems[clicked_elems.indexOf(choosen_day)];
                $(this).removeClass('day_clicked');
                calculate_price();
            } else {
                $('.info').append('<div class="added_day" data-sale="' + $(this).attr('data-sale') + '" data-date="'+ $(this).attr('data-date') +'" id=' + choosen_day + '_picked' + '>' + date + '</div>');
                clicked_elems.push(choosen_day);
                calculate_price()
                $(this).addClass('day_clicked');
            }
        }
        else if ($(this).attr('data-next') == "1") {
            $.ajax({
            data: {
                method: 'get_next_month',
                button: 'init',
                month_n: month_n,
                year: year
            },
            type: 'POST',
            url: '/api'
        })
            .done(function (data) {
                organise(data.response)
            });
        }
        $('#price').html(calculated_price);
        $('#price_input').attr('value', calculated_price);
    });

    $('#activate_promo').click(function () {
        alert('activated!');
        $.ajax({
            data: {
                method: 'activate_promo',
                button: 'init',
                promo: $('#promo').val(),
                month_n: month_n,
                year: year
            },
            type: 'POST',
            url: '/api'
        })
            .done(function (data) {
                alert('got_it');
                let resp = data.response;
                organise(resp);
            });

        for (let i = 0; i < clicked_elems.length; i++) {
            $('#' + clicked_elems[i] + '_picked').remove();
        }

        clicked_elems = [];
        calculated_price = 0;
        $('#price').html(calculated_price);
        $('#price_input').attr('value', calculated_price);
    });

    $('.clear').click(function () {
        for (let i = 0; i < clicked_elems.length; i++) {
            $('#' + clicked_elems[i] + '_picked').remove();
        }

        clicked_elems = [];
        calculated_price = 0;
        $('#price').html(calculated_price);
        $('#price_input').attr('value', calculated_price);
        draw_clicked();
    });


    $('.left').click(function () {
        $.ajax({
            data: {
                method: 'get_prev_month',
                button: 'unit',
                month_n: month_n,
                year: year,
            },
            type: 'POST',
            url: '/api'
        })
            .done(function (data) {
                organise(data.response);
            });
    });

    $('.right').click(function () {
        $.ajax({
            data: {
                method: 'get_next_month',
                button: 'init',
                month_n: month_n,
                year: year
            },
            type: 'POST',
            url: '/api'
        })
            .done(function (data) {
                organise(data.response)
            });
    });

    $('#edit').click(function () {
        var canvas = document.getElementById('img');
        var dataurl = canvas.toDataURL();

        if ($('#notify_email').val() == '') {
            alert('Введите email');
        } else {
            var soup = 1;
            //alert(soup + "soup");
        }

        if ($('#is_entity:checked').val() == 'on') {
            if ($('#entity_name').val() == '') {
                alert('Введите название организации');
            } else {
                var uno = 1;
                //alert(uno + "uno");
            }
            if ($('#iin').val() == '') {
                alert('Введите ИИН');
            } else {
                var dos = 1;
                //alert(dos + "dos");
            }
            if ($('#ogrn').val() == '') {
                //alert('Введите ОГРН');
            } else {
                var tres = 1;
                //alert(tres + "tres");
            }
            if (uno == 1 && dos == 1 && tres == 1) {
                var done = 1;
                //alert(done + "done");
            }
        }

        if ($('#is_entity:checked').val() == undefined) {
            if ($('#username').val() == '') {
                alert('Введите имя');
            } else {
                var an = 1;
                //alert(an + "an");
            }
            if ($('#second_name').val() == '') {
                //alert('Введите фамилию');
            } else {
                var tsvai = 1;
                //alert(tsvai + "tsvai");
            }
            if ($('#third_name').val() == '') {
                alert('Введите оттечство');
            } else {
                var dry = 1;
                //alert(dry + "dry");
            }
            if (an == 1 && tsvai == 1 && dry == 1) {
                var done_o = 1;
                //alert(done_o + "done_o");
            }
            var is_ent = 0;
        } else {
            var is_ent = 1;
        }

        if ($('#phone_number').val() == '') {
            alert('Введите номер телефона');
        } else {
            var ph = 1;
            alert(ph + "ph");
        }

        //alert(done);
        //alert(done_o);
        //alert(ph);
        if ((done == 1 || done_o == 1) && ph == 1 && soup == 1) {
            let checked_days = '';
            $.each(clicked_elems, function (index, value) {
                checked_days += value + ',';
                alert(checked_days);
            });
            $.ajax({
                data: {
                    moderate: 'true',
                    username: $('#username').val(),
                    second_name: $('#second_name').val(),
                    third_name: $('#third_name').val(),
                    phone_number: $('#phone_number').val(),
                    notify_email: $('#notify_email').val(),
                    is_entity: is_ent,
                    entity_name: $('#entity_name').val(),
                    iin: $('#iin').val(),
                    ogrn: $('#ogrn').val(),
                    time: checked_days,
                    head: $('#head').val(),

                    body: $('#body').val(),
                    legs: $('#legs').val(),
                    promo: $('#promo').val(),
                    price: $('#price_input').attr('value'),
                    image: dataurl
                },
                type: 'POST',
                url: '/edit/' + $('#track_code').val()
            })
                .done(function (data) {
                    alert(data.response);
                });
        }


    });
});
