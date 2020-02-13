function loadDashboard() {

    
    console.log('world')
    console.log(rules_data)
    loadRulesButton()
}

function loadRulesButton(){
    for (let count = 0; count < rules_data.length; count++){
        plusFunction(rules_data[count].name)
    } 

}

function plusFunction(name) {
    
    if (document.getElementById("plus").childElementCount > 0 ){
        if (document.getElementById("plus").lastElementChild.lastElementChild.innerHTML == "New Rule"){
        return;
        }
    }

    let button = document.createElement("button");
    let buttonwrapper = document.createElement("li");
    let container = document.getElementById("plus");
    buttonwrapper.appendChild(button);
    container.appendChild(buttonwrapper);

    button.classList.add("btn");
    button.classList.add("btn-dark");
    button.style.textAlign = "left";
    buttonwrapper.classList.add("nav-item");
    button.onclick = function() {
        nameChange(this);
    }
    if (name === undefined) {
        button.innerHTML = "New Rule";
        let title = document.getElementById("ruleHeader")
        title.innerHTML = "New Rule";
    }
    else {
        button.innerHTML = name;
    }

}

function searchFunction() {
    let input = document.getElementById("myInput");
    let filter = input.value.toUpperCase();
    let ul = document.getElementById("plus");
    let li = ul.getElementsByTagName("li");
    for (let i = 0; i < li.length; i++) {
        let button= li[i].getElementsByTagName("button")[0];
        let txtValue = button.textContent || button.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function nameChange(name){
   let title = document.getElementById("ruleHeader");
    console.log(name.innerHTML)
    title.innerHTML = name.innerHTML;

}
