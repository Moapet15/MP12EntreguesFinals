// Funció per validar el formulari de Login
function validateLoginForm() {
    // Obtenim els valors dels inputs
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    // Validem el format de l'email
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!emailPattern.test(email)) {
        alert('L\'email introduït no és vàlid.');
        return false;
    }

    // Validem que la contrasenya sigui segura (mínim 6 caràcters)
    if (password.length < 6) {
        alert('La contrasenya ha de tenir almenys 6 caràcters.');
        return false;
    }

    // Si tot és correcte, retornem les dades
    return { email: email, password: password };
}

// Funció per validar el formulari de Sign-up
function validateSignUpForm() {
    // Obtenim els valors dels inputs
    const nom = document.getElementById('signup-nom').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;

    // Validem que el nom no estigui buit
    if (nom.trim() === '') {
        alert('El nom no pot estar buit.');
        return false;
    }

    // Validem el format de l'email
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!emailPattern.test(email)) {
        alert('L\'email introduït no és vàlid.');
        return false;
    }

    // Validem que la contrasenya sigui segura (mínim 6 caràcters)
    if (password.length < 6) {
        alert('La contrasenya ha de tenir almenys 6 caràcters.');
        return false;
    }

    console.log(nom, email, password);
    // Si tot és correcte, retornem les dades
    return { nom: nom, email: email, password: password };
}

// Funció per enviar les dades al backend (AJAX)
function sendDataToBackend(formType) {
    let url;
    let data;

    // Determinem si és un login o un registre
    if (formType === 'login') {
        data = validateLoginForm();  // Validem les dades
        url = '/logIn';  // URL per al login
    } else if (formType === 'signup') {
        data = validateSignUpForm();  // Validem les dades
        url = '/signIn';  // URL per al registre
    }

    // Si les dades no són vàlides, no enviem res
    if (data === false) return;

    // Enviem les dades al backend amb fetch (AJAX)
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Ens assegurem de que el servidor accepta JSON
        },
        body: JSON.stringify(data)  // Convertim les dades a JSON
    })
    .then(response => response.json())  // Esperem la resposta en format JSON
    .then(responseData => {
        if (responseData.success) {
            alert(responseData.message);
            // Fer alguna cosa amb les dades de resposta (com redirigir a una altra pàgina, etc.)
        } else {
            alert(responseData.message);
        }
    })
    .catch(error => {
        console.error("Error al enviar les dades:", error);
    });
}

// Secció que gestiona les finques:

// Funció per validar els camps del formulari
function validarFormulari() {
    let valid = true; // Inicialitzem la variable de validació
    let errors = [];  // Array per emmagatzemar els errors
    
    // Comprovem cada camp requerit
    if (document.getElementById("referencia").value.trim() === "") {
        errors.push("El camp 'Referència' és obligatori.");
        valid = false;
    }

    if (document.getElementById("tipusFinca").value.trim() === "") {
        errors.push("El camp 'Referència' és obligatori.");
        valid = false;
    }

    if (document.getElementById("tipusHabitatge").value.trim() === "") {
        errors.push("El camp 'Tipus d'Habitatge' és obligatori.");
        valid = false;
    }

    if (document.getElementById("provincia").value.trim() === "") {
        errors.push("El camp 'Província' és obligatori.");
        valid = false;
    }

    if (document.getElementById("municipi").value.trim() === "") {
        errors.push("El camp 'Municipi' és obligatori.");
        valid = false;
    }

    if (document.getElementById("poblacio").value.trim() === "") {
        errors.push("El camp 'Població' és obligatori.");
        valid = false;
    }

    if (document.getElementById("barri").value.trim() === "") {
        errors.push("El camp 'Barri' és obligatori.");
        valid = false;
    }

    if (document.getElementById("estatConservacio").value.trim() === "") {
        errors.push("El camp 'Estat de Conservació' és obligatori.");
        valid = false;
    }

    // Verifiquem que els camps numèrics tinguin un valor vàlid
    let habitacions = document.getElementById("habitacions").value;
    if (habitacions === "" || isNaN(habitacions) || habitacions <= 0) {
        errors.push("El camp 'Habitacions' ha de ser un número vàlid.");
        valid = false;
    }

    let superficieUtil = document.getElementById("superficieUtil").value;
    if (superficieUtil === "" || isNaN(superficieUtil) || superficieUtil <= 0) {
        errors.push("El camp 'Superfície Útil' ha de ser un número vàlid.");
        valid = false;
    }

    let superficieConstruida = document.getElementById("superficieConstruida").value;
    if (superficieConstruida === "" || isNaN(superficieConstruida) || superficieConstruida <= 0) {
        errors.push("El camp 'Superfície Construïda' ha de ser un número vàlid.");
        valid = false;
    }

    let superficieTerreny = document.getElementById("superficieTerreny").value;
    if (superficieTerreny === "" || isNaN(superficieTerreny) || superficieTerreny <= 0) {
        errors.push("El camp 'Superfície Terreny' ha de ser un número vàlid.");
        valid = false;
    }

    let preu = document.getElementById("preu").value;
    if (preu === "" || isNaN(preu) || preu <= 0) {
        errors.push("El camp 'Preu' ha de ser un número vàlid.");
        valid = false;
    }

    let pisos = document.getElementById("pisos").value;
    if (pisos === "" || isNaN(pisos) || pisos <= 0) {
        errors.push("El camp 'Nombre de Pisos' ha de ser un número vàlid.");
        valid = false;
    }

    let lavabos = document.getElementById("lavabos").value;
    if (lavabos === "" || isNaN(lavabos) || lavabos <= 0) {
        errors.push("El camp 'Nombre de Lavabos' ha de ser un número vàlid.");
        valid = false;
    }

    // Comprovem si les imatges han estat seleccionades
    let imatges = document.getElementById("imatges").files;
    if (imatges.length === 0) {
        errors.push("Cal afegir almenys una imatge.");
        valid = false;
    }

    // Si hi ha errors, els mostrem
    if (!valid) {
        alert("Errors en el formulari:\n" + errors.join("\n"));
    }

    return valid; // Retornem si el formulari és vàlid
}

// Cridem la funció de validació quan l'usuari fa click al botó de 'Afegir'
function afegirImmoble() {
    if (validarFormulari()) {
        // Enviar dades del formulari al servidor si el formulari és vàlid
        console.log("Enviant formulari...");
        // Aquí pots posar el codi per enviar la informació al servidor (usant fetch, ajax, etc.)
    }
}

// Funció d'exemple per modificar immoble
function modificarImmoble() {
    if (validarFormulari()) {
        // Enviar dades per modificar el immoble
        console.log("Modificant immoble...");
    }
}

// Funció d'exemple per eliminar immoble
function eliminarImmoble() {
    if (validarFormulari()) {
        // Enviar dades per eliminar el immoble
        console.log("Eliminant immoble...");
    }
}
