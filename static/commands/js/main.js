
// popap img
var myImg = document.getElementById('myImg');
var myImgPopup = document.getElementById('myImgPopup');
var closeImgPopup = document.getElementById('closeImgPopup');

if (myImg) {
    myImg.addEventListener("click", function () {
        if (myImgPopup) {
            myImgPopup.classList.add("show");
        }
    });
}

if (closeImgPopup) {
    closeImgPopup.addEventListener("click", function () {
        if (myImgPopup) {
            myImgPopup.classList.remove("show");
        }
    });
}


// // Открыть модальное окно при нажатии на изображение
// document.getElementById("myImg").addEventListener("click", function() {
//     document.getElementById("myImgPopup").style.display = "block";
// });
//
// // Закрыть модальное окно при нажатии на кнопку закрытия
// document.getElementById("closeImgPopup").addEventListener("click", function() {
//     document.getElementById("myImgPopup").style.display = "none";
// });


// popap post
var myButton = document.getElementById('myButton');
var myPopup = document.getElementById('myPopup');
var closePopup = document.getElementById('closePopup');


if (myButton && myPopup) {
    myButton.addEventListener("click", function () {
        if (myPopup) {
            myPopup.classList.add("show");
var bindingComInput = myPopup.querySelector('input[name="binding_com"]');
        var bindingComLabel = myPopup.querySelector('label[for="id_binding_com"]');

        if (bindingComInput) {
            bindingComInput.style.display = "none";
        }

        if (bindingComLabel) {
            bindingComLabel.style.display = "none";
        }


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

//remove popaps window
window.addEventListener("click", function (event) {
    if (myPopup && event.target == myPopup) {
        myPopup.classList.remove("show");
    }
    if (myImgPopup && event.target == myImgPopup) {
        myImgPopup.classList.remove("show");
    }
});


// popup commentary
var openReplyButtons = document.querySelectorAll('.open-reply-popup');
var replyPopup = document.getElementById('replyPopup');
var closeReplyPopup = document.getElementById('closeReplyPopup');

if (openReplyButtons && replyPopup) {
    openReplyButtons.forEach(function(button) {
        button.addEventListener("click", function () {
            replyPopup.classList.add("show");
            var articleId = button.getAttribute('data-article-id');
            var bindingComInput = document.querySelector('#replyForm input[name="binding_com"]');
            var bindingComLabel = document.querySelector('label[for="id_binding_com"]');

            if (bindingComInput) {
                bindingComInput.value = articleId;
                bindingComInput.hidden = true;
            }
            if (bindingComLabel) {
                bindingComLabel.hidden = true;
            }

        });
    });
}

if (closeReplyPopup) {
    closeReplyPopup.addEventListener("click", function () {
        if (replyPopup) {
            replyPopup.classList.remove("show");
        }
    });
}

window.addEventListener("click", function (event) {
    if (replyPopup && event.target == replyPopup) {
        replyPopup.classList.remove("show");
    }
});

// delte post
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
        if (form) {
            form.submit();
        }
    }
}

//
// document.addEventListener("DOMContentLoaded", function () {
//     const filterAuthorButton = document.getElementById("filter-author");
//     const sortAscButton = document.getElementById("sort-asc");
//     const sortDescButton = document.getElementById("sort-desc");
//     const filterEmailButton = document.getElementById("filter-email");
//
//     function updateData(ordering) {
//         // Создайте новый объект URLSearchParams для создания URL-параметров
//         const params = new URLSearchParams();
//         params.append('ordering', ordering.join(','));
//
//         // Используйте fetch API для отправки GET-запроса с параметрами сортировки
//         // fetch("{% url 'commentary-list' %}?" + params.toString())
//         fetch("/your-commentary-list-url?" + params.toString())
//
//             .then(response => response.json())
//             .then(responseData => {
//                 // Обработайте успешный ответ от сервера, как вы делали ранее
//                 // ...
//             })
//             .catch(error => {
//                 console.error('Ошибка:', error);
//             });
//     }
//
//
//     filterAuthorButton.addEventListener("click", function () {
//         const ordering = ["author"];
//         updateData(ordering);
//     });
//
//     sortAscButton.addEventListener("click", function () {
//         const ordering = ["created_at"];
//         updateData(ordering);
//     });
//
//     sortDescButton.addEventListener("click", function () {
//         const ordering = ["-created_at"];
//         updateData(ordering);
//     });
//
//     filterEmailButton.addEventListener("click", function () {
//         const ordering = ["author__email"];
//         updateData(ordering);
//     });

