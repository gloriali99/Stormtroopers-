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

            let g = rules_data[count]["name"];
            document.getElementById("ruleName").value = g;

            
        }
    }
}

function save_field(){
    // set rules
  var result = $('#builder').queryBuilder('getRules');

  if (!$.isEmptyObject(result)) {
      rules_basic = result;
  }

  // get and save 
result = $('#builder').queryBuilder('getRules');

// save field 
let dict = retrieveemaildetails(); 
result = Object.assign({},result,dict);

  if (!$.isEmptyObject(result)) {
  console.log("home time")
      // get json
      var to_return = JSON.stringify(result, null, 2);
      console.log(to_return)
      // send json file
      $.post( "/postmethod", {
  javascript_data : to_return
  
      });
  } else {
      console.log("invalid object :");
  }
  console.log(result);
}
//var array = string.split(',');
function retrieveemaildetails(){
    let dict = {};
    let array0 = document.getElementById("TO").value.split(',');
    let array1 = document.getElementById("BCC").value.split(',');
    let array2 = document.getElementById("CC").value.split(',');
    let rule = document.getElementById("ruleName").value;
    let para = document.getElementById("exampleFormControlTextarea1").value;
    dict.to = array0;
    dict.bcc = array1;
    dict.cc = array2;
    dict.description = para;
    dict.name = rule; 
    console.log(dict);
    console.log(array0);
    console.log(array1);
    console.log(array2);
    return dict;
}

function email_all(){
    // $.post( "/trigger_email");
    console.log("email")
}