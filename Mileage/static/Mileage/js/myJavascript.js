// About page, swaps text
document.addEventListener('DOMContentLoaded', function() {
  let switchLocationVariable = document.querySelector('#about_switch_location')
  switchLocationVariable.onclick = switchLocation;
});

// About page, swaps text function
function switchLocation() {
  headerText = document.querySelector('#header_title').innerHTML;
  bodyText = document.querySelector('#p_body').innerHTML;
  document.querySelector('#header_title').innerHTML = bodyText;
  document.querySelector('#p_body').innerHTML = headerText;
}

// Mileage page, opens chosen form
document.querySelectorAll('.button-change').forEach(function(button){
  button.onclick = switchActiveButton;
});

// Mileage page, highlights and deselects chosen button
function switchActiveButton(){
  const selectedButton = document.querySelector('#' + this.id);
  const allButtons = document.querySelectorAll('.button-change');
  allButtons.forEach(function(button){
    button.classList.remove('btn-primary')
    button.classList.add('btn-light')
  });
  selectedButton.classList.remove('btn-light');
  selectedButton.classList.add('btn-primary');
  load_mileage(selectedButton.dataset.mileage_select);
}

// Mileage page, opens one of three form options
function load_mileage(mileageForm){
  document.querySelector('#mileage_form_body').innerHTML = mileageForm;
  const request = new XMLHttpRequest();
  request.open('GET', `/${mileageForm}`);
  request.onload = () => {
    const response = request.responseText;
    document.querySelector('#mileage_form_body').innerHTML = response;
  };
  request.send();
}

// Add additional location input field
locationFieldCount = 3;
function addLocationInput(locationList) {
  console.log(locationList);
  var wrapper = $(".input_fields_wrap"); //Fields wrapper
  var add_button = $(".add_field_button"); //Add button ID
  //var locationList = document.getElementById('location_lfdsfsd');
  // var temp = locationList.options.text;
  // alert(temp);
  var formGroup = document.createElement('div')
  formGroup.classList.add('form-group')
  var label = document.createElement('label')
  label.innerHTML = 'Location' + locationFieldCount.toString()
  var selectBox = document.createElement('select')
  selectBox.classList.add('form-control')
  selectBox.setAttribute('name', 'location ' + locationFieldCount.toString())
  locationList.map(l => {
    var newNode = document.createElement('option');
    newNode.setAttribute('value', l)
    newNode.innerHTML = l
    selectBox.appendChild(newNode)
  })
  formGroup.appendChild(label)
  formGroup.appendChild(selectBox)
  var htmlInput = `
  <div class="form-group">
    <label for="exampleFormControlSelect1">Location ` + locationFieldCount.toString() + `</label>
    <select class="form-control" name="location ` + locationFieldCount.toString() + `" id="exampleFormControlSelect ` + locationFieldCount.toString() + `">
      {% for locations in locationList %}
        <option>
          {{ locations }}
        </options>
      {% endfor %}
    </select>
  </div>
  `;
	$(".input_fields_wrap").append(formGroup); //add input box

  locationFieldCount++;


	// $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
	// 	e.preventDefault(); $(this).parent('div').remove(); x--;
	// })
}
