
var myButton = document.getElementById('myButton');
var myPopup = document.getElementById('myPopup');
var closePopup = document.getElementById('closePopup');

if (myButton) {
    myButton.addEventListener("click", function () {
        if (myPopup) {
            myPopup.classList.add("show");
        }
    });
}

if (closePopup) {
    closePopup.addEventListener("click", function () {
        if (myPopup) {
            myPopup.classList.remove("show");
        }
    });
}

window.addEventListener("click", function (event) {
    if (myPopup && event.target == myPopup) {
        myPopup.classList.remove("show");
    }
});


var deleteLinks = document.querySelectorAll('.delete-link');

deleteLinks.forEach(function (link) {
    link.addEventListener('click', function () {
        var id = link.getAttribute('data-id');
        delete_quesion(id);
    });
});

function delete_quesion(id) {
    if (confirm("Вы уверены?")) {
        var formId = 'delete_form' + id;
        var form = document.getElementById(formId);
        if (form){
            form.submit();
        }
    }
}

