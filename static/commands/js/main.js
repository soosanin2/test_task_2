
var openButtons = document.querySelectorAll('.open-popup');
var myPopup = document.getElementById('myPopup');
var bindingField = document.querySelector('#myPopup [name="binding"]');
var bindingFieldCom = document.querySelector('#myPopup [name="binding_com"]');

openButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        var bindingValue = button.getAttribute('data-binding');
        var bindingValueCom = button.getAttribute('data-binding-com');
        bindingField.value = bindingValue;
        bindingFieldCom.value = bindingValueCom;
        myPopup.classList.add('show');
    });
});

var closePopup = document.getElementById('closePopup');
closePopup.addEventListener('click', function () {
    myPopup.classList.remove('show');
});
var submitComit = document.getElementById('submitComit');
submitComit.addEventListener('click', function () {
  location.reload();
});

window.addEventListener('click', function (event) {
    if (event.target == myPopup) {
        myPopup.classList.remove('show');
    }
});




