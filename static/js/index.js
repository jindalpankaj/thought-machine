$(document).ready(function() {
    $("#tb1_id").keypress(function(event) {
        if(event.key == 'Enter' || event.which == 13) {
            // alert("key is " + event.key);
            // alert("which is "+ event.which);
            var thought = $("#tb1").val();
            // alert("The thought you entered is: " + thought);
            // alert("Now, the next page will be displayed based on your entered thought.");
            alert("Text captured!");
            $.post("/_receivedata", {"new_thought": thought});
            window.open('http://127.0.0.1:5000/second_page', '_self');
            // window.open("/receive_data", {"new_thought": thought});
            // event.stopPropagation();
        }
    });
});
