function loadDashboard() {

    
    console.log('world2')
    

    loadRulesButton();
}

function loadRulesButton(){
    $.get("/getpythondata", function(data) {
        console.log("BEFORE JSON")
        rules_data = $.parseJSON(data)
        window.rules_data = rules_data
        console.log("AFTER JSON")
        for (let count = 0; count < rules_data.length; count++){
            plusFunction(window.rules_data[count].name)
        } 
    })
    // console.log({{rules_dict}})


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

    // HEREREERERERERERERERERERE
    // GETS INFORMATION
    button.onclick = function() {

        $.get("/getpythondata", function(data) {
            window.rules_data = $.parseJSON(data)
        })
        
        nameChange(this);

        populate_rule(this);
        
        console.log(this);
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

function nameChange(element){
   let title = document.getElementById("ruleHeader");
    console.log(element.innerHTML)
    title.innerHTML = element.innerHTML;
    window.rule_name = element.innerHTML;

}

function populate_rule(element){
    for (let i = 0; i < window.rules_data.length; i++) {
        rule_dict = rules_data[i];
        if (rule_dict['name'] == window.rule_name) {
            console.log("FOUND, let's POPULATE", rules_basic);
            rules_basic = rule_dict['tree'];
            console.log("POPULATED WITH", rules_basic);
            $('#builder').queryBuilder('setRules', rules_basic);
            break;
        }
    }
    console.log("HI")
    // for (let count = 0; count < rules_data.length; count++){
    //     if rules_data[count].name
    // }
}