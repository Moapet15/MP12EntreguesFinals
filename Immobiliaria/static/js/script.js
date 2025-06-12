// Obtenim el pathname de la pàgina actual
function detectarIdioma() {
  let idiomaBrowser = '';

  if (navigator.languages && navigator.languages.length) {
    idiomaBrowser = navigator.languages[0];
  } else if (navigator.language) {
    idiomaBrowser = navigator.language;
  } else if (navigator.userLanguage) {
    idiomaBrowser = navigator.userLanguage;
  } else if (navigator.browserLanguage) {
    idiomaBrowser = navigator.browserLanguage;
  } else {
    idiomaBrowser = 'ca';
  }

  const idiomaSimple = idiomaBrowser.substring(0, 2).toLowerCase();
  const idiomesSoportats = ['ca', 'es', 'en'];

  if (idiomesSoportats.includes(idiomaSimple)) {
    return idiomaSimple;
  }

  return 'en';
}

async function enviarIdioma() {
  const lang = detectarIdioma();
  try {
    const resposta = await fetch('/set_lang', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token() }}'
      },
      body: JSON.stringify({ lang: lang })
    });

    const text = await resposta.text();
    try {
      const data = JSON.parse(text);
      if (!data.success) {
        console.error("No s'ha pogut guardar l'idioma");
      }
    } catch {
      console.error("La resposta no és JSON:", text);
    }

  } catch (err) {
    console.error("Error enviant l'idioma al servidor:", err);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  enviarIdioma();
});

// document.getElementById('idioma').addEventListener('change', function() {
//   fetch('/canvia_idioma', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': '{{ csrf_token }}'  // si tens CSRF habilitat
//     },
//     body: JSON.stringify({ idioma: this.value })
//   }).then(res => {
//     if(res.ok) {
//       window.location.reload();  // recarrega la pàgina per aplicar idioma
//     } else {
//       alert('Error canviant l\'idioma');
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
    // Per a cada bloc d'immoble
    document.querySelectorAll('.imatges-immoble').forEach(container => {
        const imgGran = container.querySelector('.img-gran');
        const miniatures = container.querySelectorAll('.miniatura');

        miniatures.forEach(mini => {
            mini.addEventListener('click', () => {
                imgGran.src = mini.src;
            });
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
  // Inicialitza la secció visible per defecte (Urbana)
  mostrarSeccioVisible("finquesUrbanaDestacades", [
    "finquesRustiquesDestacades",
    "finquesLloguerDestacades"
  ]);

  // Assigna accions als botons de navegació
  document.getElementById("btnAnterior").onclick = mostrarAnterior;
  document.getElementById("btnSeguent").onclick = mostrarSeguent;
});

// Llista d'ids de seccions
const seccionsIds = [
  "finquesUrbanaDestacades",
  "finquesRustiquesDestacades",
  "finquesLloguerDestacades"
];

let indexActual = 0;

function mostrarSeccioVisible(seccioVisibleId, seccionsOcultesIds) {
  const visible = document.getElementById(seccioVisibleId);
  const ocultes = seccionsOcultesIds.map(id => document.getElementById(id));

  if (visible) visible.style.display = "flex";
  ocultes.forEach(seccio => {
    if (seccio) seccio.style.display = "none";
  });
}

function mostrarSeccioPerIndex(index) {
  indexActual = index;
  const visibleId = seccionsIds[index];
  const ocultesIds = seccionsIds.filter((_, i) => i !== index);
  mostrarSeccioVisible(visibleId, ocultesIds);
}

function mostrarAnterior() {
  indexActual = (indexActual - 1 + seccionsIds.length) % seccionsIds.length;
  mostrarSeccioPerIndex(indexActual);
}

function mostrarSeguent() {
  indexActual = (indexActual + 1) % seccionsIds.length;
  mostrarSeccioPerIndex(indexActual);
}

document.addEventListener('DOMContentLoaded', () => {
  const btnNext = document.getElementById('btnNext');
  const btnPrev = document.getElementById('btnPrev');
  const llistaImmobles = document.getElementById('llistaImmobles');

  function getItemWidth() {
    const item = llistaImmobles.children[0];
    if (!item) return 0;
    const style = window.getComputedStyle(item);
    const marginRight = parseInt(style.marginRight) || 20;
    return item.offsetWidth + marginRight;
  }

  function updateButtons() {
    const scrollAmount = llistaImmobles.scrollLeft;
    const maxScroll = llistaImmobles.scrollWidth - llistaImmobles.clientWidth;
    btnPrev.disabled = scrollAmount <= 0;
    btnNext.disabled = scrollAmount >= maxScroll - 1; // petita tolerància
  }

  btnNext.addEventListener('click', () => {
    llistaImmobles.scrollBy({
      left: getItemWidth(),
      behavior: 'smooth'
    });
    setTimeout(updateButtons, 300);
  });

  btnPrev.addEventListener('click', () => {
    llistaImmobles.scrollBy({
      left: -getItemWidth(),
      behavior: 'smooth'
    });
    setTimeout(updateButtons, 300);
  });

  llistaImmobles.addEventListener('scroll', updateButtons);
  window.addEventListener('resize', updateButtons);

  updateButtons();
});

const pagina = window.location.pathname;

console.log(`Pàgina actual: ${pagina}`);

// Control del comportament específic per a la pàgina "serveis"
if (pagina === "/serveis") {
    alert(`Estàs a la pàgina ${pagina}`);

    // Quan el DOM està completament carregat
    window.onload = function () {
        ocultarSeccions("tarjetes", ["webLloguer", "webValoracio"]);
        ocultarFormularis("formularis", ["formulariSignIn", "formulariLogIn"])
    };

    // Funció genèrica per mostrar una secció i ocultar les altres
    function ocultarSeccions(seccioVisibleId, seccionsOcultesIds) {
        const seccioVisible = document.getElementById(seccioVisibleId);
        const seccionsOcultes = seccionsOcultesIds.map(id => document.getElementById(id));

        // Mostrem la secció visible
        if (seccioVisible) {
            seccioVisible.style.display = "flex";
        }

        // Ocultem les altres seccions
        seccionsOcultes.forEach(seccio => {
            if (seccio) {
                seccio.style.display = "none";
            }
        });
    }

    // Funció per mostrar informació de "Lloguers"
    function mostrarInfoLloguers() {
        ocultarSeccions("webLloguer", ["targetes", "webValoracio"]);
    }

    // Funció per mostrar informació de "Valoració"
    function mostrarInfoValoracio() {
        ocultarSeccions("webValoracio", ["targetes", "webLloguer"]);
    }

    // Opcional: pots assignar els esdeveniments directament des del JavaScript
    document.getElementById("webLloguer").onclick = mostrarInfoLloguers;
    document.getElementById("webValoracio").onclick = mostrarInfoValoracio;
}

function ocultarFormularis(formulariVisibleId, formularisOcultsIds) {
    // Mostrar el formulari desitjat
    const formulariVisible = document.getElementById(formulariVisibleId);
    if (formulariVisible) {
        formulariVisible.style.display = "block";
    }

    // Amagar tots els altres formularis
    formularisOcultsIds.forEach(id => {
        const formulariOcult = document.getElementById(id);
        if (formulariOcult) {
            formulariOcult.style.display = "none";
        }
    });
}

function mostrarFormulariSignIn() {
    ocultarFormularis("signup-form", ["login-form"]);
}

function mostrarFormulariLogIn() {
    ocultarFormularis("login-form", ["signup-form"]);
}

function closeForm() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("signup-form").style.display = "none";
}

function afegirImmoble() {
    let formData = new FormData();

    // 🔹 Captura tots els camps de text i números
    let camps = ["referencia", "tipusFinca", "tipusHabitatge", "provincia", "municipi", "poblacio", "barri", "estatConservacio",
                 "habitacions", "superficieUtil", "superficieConstruida", "superficieTerreny", "preu", "pisos",
                 "lavabos", "qualificacioEnergetica", "descripcio"];

    camps.forEach(camp => {
        formData.append(camp, document.getElementById(camp).value);
    });

    // 🔹 Captura els checkboxos
    let checkboxes = ["terrassa", "traster", "garatge", "jardi"];
    checkboxes.forEach(camp => {
        formData.append(camp, document.getElementById(camp).checked ? "on" : "off");
    });

    // 🔹 Captura les imatges
    let imatges = document.getElementById("imatges").files;
    for (let i = 0; i < imatges.length; i++) {
        formData.append("imatges", imatges[i]);
    }

    // 🔹 Enviar la petició al backend
    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Finca i imatges desades correctament!");
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => console.error("Error en la petició:", error));
}

function eliminarImmoble(referencia) {
    const formData = new FormData();
    formData.append("referencia", referencia);

    fetch("/delete", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Finca i imatges borrades correctament!");
            location.reload(); // Opcional: recarrega per actualitzar la llista
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => console.error("Error en la petició:", error));
}

function guardarCanvi(referencia, camp, nouValor) {
    fetch('/api/modificar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            referencia: referencia,
            camp: camp,
            nou_valor: nouValor
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            console.log("Modificació desada correctament");
        } else {
            console.error("Error en desar la modificació:", data.error);
        }
    })
    .catch(error => {
        console.error("Error de xarxa:", error);
    });
}

async function guardarCheckbox(referencia, camp, valor) {
    try {
        const resposta = await fetch('/api/modificar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                referencia,
                camp,
                nou_valor: valor ? 1 : 0
            })
        });
        const data = await resposta.json();
        if (!data.success) {
            console.error('Error en guardar:', data.error);
            alert("No s'ha pogut desar el canvi.");
        }
    } catch (error) {
        console.error('Error en la sol·licitud:', error);
        alert("Error en la connexió amb el servidor.");
    }
}

document.addEventListener("DOMContentLoaded", () => {
  const carruselImages = document.querySelector(".carrusel-images");
  const images = carruselImages.querySelectorAll("img");
  const btnPrev = document.querySelector(".carrusel-btn.prev");
  const btnNext = document.querySelector(".carrusel-btn.next");

  let currentIndex = 0;
  const totalImages = images.length;

  function updateCarousel() {
    const slideWidth = images[0].offsetWidth;
    const offset = currentIndex * slideWidth;
    carruselImages.style.transform = `translateX(-${offset}px)`;
  }

  btnNext.addEventListener("click", () => {
    if (currentIndex < totalImages - 1) {
      currentIndex++;
      updateCarousel();
    }
  });

  btnPrev.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  });

  // Recalcula si redimensiona la finestra
  window.addEventListener("resize", updateCarousel);
});

setInterval(() => {
  if (currentIndex < totalImages - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  updateCarousel();
}, 5000); // cada 5 segons

// Quan el DOM està carregat
document.addEventListener('DOMContentLoaded', () => {
    // Funció per mostrar una secció i ocultar les altres
    function mostrarSeccio(seccioVisibleId, seccionsOcultesIds) {
        const seccioVisible = document.getElementById(seccioVisibleId);
        if (seccioVisible) {
            seccioVisible.style.display = "block";
        }
        seccionsOcultesIds.forEach(id => {
            const seccio = document.getElementById(id);
            if (seccio) seccio.style.display = "none";
        });
    }

    // Per exemple, inicialment només mostrar els immobles
    mostrarSeccio('mostrarImmobles', ['formulariNovaFinca', 'missatgesRebuts', 'consultesRebudes']);

    // Assignar esdeveniments per canviar entre seccions
    document.getElementById('btnMostrarImmobles')?.addEventListener('click', () => {
        mostrarSeccio('mostrarImmobles', ['formulariNovaFinca', 'missatgesRebuts', 'consultesRebudes']);
    });

    document.getElementById('btnFormNovaFinca')?.addEventListener('click', () => {
        mostrarSeccio('formulariNovaFinca', ['mostrarImmobles', 'missatgesRebuts', 'consultesRebudes']);
    });

    document.getElementById('btnMostrarMissatges')?.addEventListener('click', () => {
        mostrarSeccio('missatgesRebuts', ['mostrarImmobles', 'formulariNovaFinca', 'consultesRebudes']);
    });

    document.getElementById('btnMostrarConsultes')?.addEventListener('click', () => {
        mostrarSeccio('consultesRebudes', ['mostrarImmobles', 'formulariNovaFinca', 'missatgesRebuts']);
    });
});
