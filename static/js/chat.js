const text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
    '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
    '{message}' +
    '</div>';

    function send(sender, receiver, message) {
      //POST to '/api/messages', the data in JSON string format
      $.post('/api/messages/', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
          console.log(data);
          //alert("sucess");
          var box = text_box.replace('{sender}', "You"); // Replace the text '{sender}' with 'You'
          box = box.replace('{message}', message); // Replace the text '{message}' with the message that has been sent.
      })
  }


  function receive() {
    // 'sender_id' and 'receiver_id' are global variable declared in the messages.html, which contains the ids of the users.
    $.get('/api/messages/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);
                scrolltoend();
            }
        }
    })
}

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}
