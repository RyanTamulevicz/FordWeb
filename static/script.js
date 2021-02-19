axios.get('http://127.0.0.1:5000/search/')
    .then(function (response) {
        console.log(response)
    })
    .catch(function (error) {
        console.log(error)
    })
    .then(function () {

    });