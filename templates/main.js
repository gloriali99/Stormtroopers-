function loadDashboard() {

    console.log('world')
}


// function Windowopen() {
// document.getElementById("myChart")
// }
// 

function plusFunction() {
    let ruletext = "Rule";
    let rulecount = 1;

    let button = document.createElement("button");
    let buttonwrapper = document.createElement("li");
    let container = document.getElementById("plus");
    buttonwrapper.appendChild(button);
    container.appendChild(buttonwrapper);

    button.classList.add("btn");
    button.classList.add("btn-dark");
    buttonwrapper.classList.add("nav-item");

    button.innerHTML = "Rule" + String( 1);
}
