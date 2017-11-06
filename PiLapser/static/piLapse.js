/**
 * Created by joncanning on 2017-11-05.
 */
var slider = document.getElementById("length");
length = slider.value;


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
        moveCamera()
    }

}
