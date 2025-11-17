let mapCreator = document.getElementById("mapCreator");
let largeurInput = document.getElementById("largeurInput");
let longeurInput = document.getElementById("longeurInput");

let map = document.getElementById("map");

let largeur = 1;
let longeur = 1;

largeurInput.addEventListener('change', function() {
    largeur = largeurInput.value;
})
longeurInput.addEventListener('change', function() {
    longeur = longeurInput.value;
})

mapCreator.addEventListener('submit', function (e){
    e.preventDefault()
    map.innerHTML = "";

    map.style.gridTemplateColumns = `repeat(${largeur}, 1fr)`;

    for (let step = 0; step < longeur; step++) {
        for (let step = 0; step < largeur; step++) {
            map.innerHTML += "<span>!</span>";
        }
    }
})