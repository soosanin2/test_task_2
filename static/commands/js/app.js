
// new Vue({
//         el: '#post_app',
//         data: {
//             posts: []
//         },
//         created: function () {
//             const vm = this;
//             axios.get('/api/post/')
//                 .then(function (response) {
//                     console.log(response.data);
//                     vm.posts = response.data;
//                 });
//         }
//     }
// )
//
// new Vue({
//         el: '#comm_app',
//         data: {
//             commentaries: []
//         },
//         created: function () {
//             const vm = this;
//             axios.get('api/commentary/')
//                 .then(function (response) {
//                     console.log(response.data);
//                     vm.commentaries = response.data;
//                 })
//         }
//     }
// )