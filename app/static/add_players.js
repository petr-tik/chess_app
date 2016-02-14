document.getElementById('button').onclick = add_player;


var i = 0;
var original = document.getElementById('player');

function add_player() {
    var clone = original.cloneNode(true); // "deep" clone
    clone.id = "player" + ++i; // there can only be one element with an ID
    original.parentNode.appendChild(clone);
}