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
        populate_rule(this);
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

function populate_rule(element){
    for (let count = 0; count < rules_data.length; count++){
        //console.log(rules_data[count]["name"]);
        //console.log(element.innerHTML);
        if (rules_data[count]["name"] == element.innerHTML){
            let x = "";
            for (let count1 = 0; count1 < rules_data[count]["to"].length; count1++){
                x += rules_data[count]["to"][count1] + ",";
            }
            x = x.slice(0,-1);
            //console.log(x);
            //document.getElementById("exampleFormControlTextarea1").value = rules_data[count].value;
            document.getElementById("TO").value = x;
            let y = rules_data[count]["description"];
            document.getElementById("exampleFormControlTextarea1").value = y;
            let z = "";
            for (let count1 = 0; count1 < rules_data[count]["bcc"].length; count1++){
                z += rules_data[count]["bcc"][count1] + ",";
            }
            z = z.slice(0,-1);        
            document.getElementById("BCC").value = z;
            let t = "";
            for (let count1 = 0; count1 < rules_data[count]["cc"].length; count1++){
                t += rules_data[count]["cc"][count1] + ",";
            }
            t = t.slice(0,-1); 
            document.getElementById("CC").value = t;
        }
    }
}

function save_field(){
    let dict = retrieveemaildetails();    
    // dict['to']=[]
}
//var array = string.split(',');
function retrieveemaildetails(){
    let dict = {};
    let array0 = document.getElementById("TO").value.split(',');
    let array1 = document.getElementById("BCC").value.split(',');
    let array2 = document.getElementById("CC").value.split(',');
    let para = document.getElementById("exampleFormControlTextarea1").value;
    dict.to = array0;
    dict.bcc = array1;
    dict.cc = array2;
    dict.description = para;
    console.log(dict);
    console.log(array0);
    console.log(array1);
    console.log(array2);
    return dict;
}