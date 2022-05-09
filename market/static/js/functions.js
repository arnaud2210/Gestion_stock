function checkQuantity(){
    var quantity = document.getElementById("quantity").value

    if (quantity < 0){
        document.getElementById("msg").innerHTML = "Veuillez saisir une valeur positive"
        document.getElementById("msg").style.color = "red" 
    }
    else {
        document.getElementById("msg").innerHTML = "Valide"
        document.getElementById("msg").style.color = "green"
    }
}


function checkPrice(){
    var price = document.getElementById("price").value

    if (price <= 0){
        document.getElementById("message").innerHTML = "Veuillez saisir une valeur non nulle et positive"
        document.getElementById("message").style.color = "red" 
    }
    else {
        document.getElementById("message").innerHTML = "Valide"
        document.getElementById("message").style.color = "green"
    }
}