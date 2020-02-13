function loadDashboard() {

    $('#builder').queryBuilder({
        plugins: ['bt-tooltip-errors'],
        filters: [{
          id: 'name',
          label: 'Name',
          type: 'string' },
        {
          id: 'category',
          label: 'Category',
          type: 'integer',
          input: 'select',
          values: {
            1: 'Books',
            2: 'Movies',
            3: 'Music',
            4: 'Tools',
            5: 'Goodies',
            6: 'Clothes' },
          operators: ['equal', 'not_equal', 'less', 'not_in', 'is_null', 'is_not_null'] },
        {
          id: 'in_stock',
          label: 'In stock',
          type: 'integer',
          input: 'radio',
          values: {
            1: 'Yes',
            0: 'No' },
          operators: ['equal'] },
        {
          id: 'price',
          label: 'Price',
          type: 'double',
          validation: {
            min: 0,
            step: 0.01 } },
        {
          id: 'id',
          label: 'Identifier',
          type: 'string',
          placeholder: '____-____-____',
          operators: ['equal', 'not_equal'],
          validation: {
            format: /^.{4}-.{4}-.{4}$/ } }],
        rules: rules_data });
    /****************************************************************
                                                Triggers and Changers QueryBuilder
                         *****************************************************************/
                         $('#btn-get').on('click', function () {
    var result = $('#builder').queryBuilder('getRules');
    if (!$.isEmptyObject(result)) {
      rules_data = result;
    }
    result = $('#builder').queryBuilder('getRules');
    if (!$.isEmptyObject(result)) {
      var to_return = JSON.stringify(result, null, 2);
      $.post( "/postmethod", {
        javascript_data : to_return
      });
      
    } else
    {
      console.log("invalid object :");
    }
    console.log(result);
  });
  $('#btn-reset').on('click', function () {
  //   $('#builder').queryBuilder('reset');
  });
  $('#btn-set').on('click', function () {
    //$('#builder').queryBuilder('setRules', rules_data);
    var result = $('#builder').queryBuilder('getRules');
    if (!$.isEmptyObject(result)) {
      rules_data = result;
    }
  });
  //When rules changed :
  $('#builder').on('getRules.queryBuilder.filter', function (e) {
    //$log.info(e.value);
  });
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
    // for (let count = 0; count < rules_data.length; count++){
    //     if rules_data[count].name
    // }
}