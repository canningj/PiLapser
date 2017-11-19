$(document).ready(function() {


var slider = document.getElementById("length");
length = slider.value;

function move_pos() {
    $.ajax({
        url: '/move_pos/'
    });
}


/* This would store the information on whether a button was being held down or not. */
var hold = false;

function mousedown()
{
  hold = true;
  checkForHold();
}
function mouseup()
{
  hold = false;
}

function checkForHold() {
    if (hold) {
        /* figure out a way to call the python script to move the camera while
        button is held...
         */

    }

}
});
