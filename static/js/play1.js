var menuIcon = document.querySelector(".menu");
var sidebar = document.querySelector(".sidebar");
var listcontainer = document.querySelector(".list-container");

menuIcon.onclick = function(){
    sidebar.classList.toggle("small-sidebar");
     container.classList.toggle("row");

    listcontainer.classList.toggle("large-list-container");
}