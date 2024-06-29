function consultuser() {
   let id_user = document.getElementById("ident").value
   let obj_user = {
       "id": id_user,
       "passw":"12345"
   }
    fetch("/consult_user", {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body":JSON.stringify(obj_user)
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.status == "ok") {
            document.getElementById("txt-data").value = "ID: " + data.id
            + "\nPet Name: "+ data.name 
            + "\nOwner Name: "+ data.ownername 
            + "\nOwner Lastname: " + data.ownerlastname 
            + "\nBirthday: " + data.birthday 
            + "\nAnimal: "+ data.animal
            + "\nBreed: "+ data.breed
            + "\nURL photo: " + data.url_photo
            
            document.getElementById("image_user").src = data.url_photo
        }   
        else {
            alert("Ususario no encontrado")
            document.getElementById("txt-data").value = ""
            document.getElementById("image_user").src = ""
        }
    })
    .catch(err => {
        alert("Error" + err)
    })
}