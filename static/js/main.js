let addItems = document.getElementsByClassName('add-items');

for(var i = 0; i < addItems.length; i++){
	addItems[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:',  action);

        console.log('USER:', user);
        if(user == 'AnonymousUser'){
            console.log('User is an Anonymous User');
        }
        else{
            updateUserOrder(productId, action);
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, Sending data...');

    let url = '/update_item/';
    fetch(url , {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        console.log('data',data);
        location.reload();
    })
}

