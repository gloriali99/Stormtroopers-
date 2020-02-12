function loadDashboard() {

    console.log('world')
    console.log(rules_data)
    loadRulesButton()
}


// function Windowopen() {
// document.getElementById("myChart")
// }
// 

function loadRulesButton(){
    for (let count = 0; count < rules_data.length; count++){
        plusFunction(rules_data[count].name)
    } 

}

function plusFunction(name) {
    

    let button = document.createElement("button");
    let buttonwrapper = document.createElement("li");
    let container = document.getElementById("plus");
    buttonwrapper.appendChild(button);
    container.appendChild(buttonwrapper);

    button.classList.add("btn");
    button.classList.add("btn-dark");
    button.style.textAlign = "left";
    buttonwrapper.classList.add("nav-item");
    if (name === undefined) {
        button.innerHTML = " NEW RULE ";
    }
    else {
        button.innerHTML = name;
    }
}
