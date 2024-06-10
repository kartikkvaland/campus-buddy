// var menuIcon = document.querySelector(".menu");
// var sidebar = document.querySelector(".sidebar");
// var container = document.querySelector(".container");
// var listcontainer = document.querySelector(".list-container");


// menuIcon.onclick = function(){
//     sidebar.classList.toggle("small-sidebar");
//     container.classList.toggle("large-container");
//     listcontainer.classList.toggle("large-list-container")
// }


var menuIcon = document.querySelector(".menu");
var sidebar = document.querySelector(".sidebar");
var listcontainer = document.querySelector(".list-container");

menuIcon.onclick = function(){
    sidebar.classList.toggle("small-sidebar");
    
    listcontainer.classList.toggle("large-list-container");
}

