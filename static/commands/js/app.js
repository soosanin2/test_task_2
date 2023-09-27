new Vue({
    el: '#post_app',
    data: {
        posts: []
    },
    created: function (){
        const vm = this;
        axios.get('/api/post/')
            .then(function (response){
                vm.posts = response.data
                // console.log(response.data)
            })
    }
}
)

