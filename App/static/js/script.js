// 1) Character remaining counter

$(document).ready(function() {
    var start = 0;
    var limit = 1000;

    $("#message").keyup(function() {
        start = this.value.length
        if(start > limit){
            return false;
        }
        else if (start == 1000) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'red');
            Swal.fire("Opps !", "Characters limit exceeded !", "info");
        }
        else if (start > 984) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'red');
        }
        else if (start < 1000) {
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'black');
        }
        else{
            $("#remaining").html("Characters remaining: " + (limit - start)).css('color', 'black');
        }
    })
})

// 2) Get RealTime

setInterval(function() {
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// 3) update page always at (0:00)

function autoRefresh(hours, minutes, seconds) {
    var now = new Date(), then = new Date();
    then.setHours(hours, minutes, seconds, 0);
    if(then.getTime() < now.getTime()){
        then.setDate(now.getDate() + 1);
    }
    var timeout  = (then.getTime() - now.getTime());
    setTimeout(function () {
        window.location.reload(true);
    }, timeout);
}
autoRefresh(0,0,0)


// 4) If no messages, hide all content

$(document).ready(function () {
    var verify = $('#chk_td').length;
    if(verify == 0){
        $(".hide").css('display', 'none')
        $("#msg").text('No message found')
        $("#refresh").html(' <i class="fas fa-sync-alt fa-3x"></i> ')

    }
})

// 5) Warns Loggedout after 5 minutes
setTimeout(function() {
    var notice = document.querySelector('#warning');
    if(notice){
        notice.click();
    }
}, 25 * 60000) // 25 minutes   = 25 * 60000 For testing use = 1*10000


// 6) Loggedout after 5 minutes passed
setTimeout(function() {
    var notice = document.querySelector('#info');
    if(notice){
        notice.click();
    }
}, 30 * 60000) // 30 minutes = 30 * 60000 For testing use = 1*15000