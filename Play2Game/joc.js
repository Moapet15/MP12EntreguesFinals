// Constants i variables globals
const ALT = 30; // Alçada graella fixa
let ample; // Amplada graella variable
let posicioJugadorX;
let posicioJugadorY;
let temps = 0;
let punts = 0;
let vides = 3;
let obstacles = [];
let obstacleGeneratorInterval;
let obstacleMoverInterval;
let posicioInicialY;


// Inicialització del joc i menú de benvinguda
window.onload = () => {
  mostrarMenuBenvinguda();
  calcularDimensions();
  generarGraella();
  mostrarVides();
};

// --- Funcions del menú de benvinguda ---
function mostrarMenuBenvinguda() {
  const fons = crearElement('div', null, 'fonsSemiTransparent', 'fonsSemiTransparent');
  document.body.appendChild(fons);

  const menu = crearElement('div', null, 'menuBenvinguda', 'menuBenvinguda');
  document.body.appendChild(menu);

  menu.appendChild(crearElement('h1', 'Jungle Scape', 'titolMenu', 'titolMenu'));
  menu.appendChild(crearElement('h2', 'Benvingut al Jungle Scape', 'benvinguda', 'benvinguda'));

  const nivells = [
    { text: 'Me da amsieda', id: 'nivell1', vides: 3 },
    { text: 'Sin miedo al exito', id: 'nivell2', vides: 1 },
  ];

  nivells.forEach(({ text, id, vides: videsAssignades }) => {
    const boto = crearElement('button', text, id, id);
    boto.addEventListener('click', () => {
      vides = videsAssignades;
      mostrarVides();
      tancarMenu();
    });
    menu.appendChild(boto);
  });

  menu.appendChild(
    crearElement(
      'p',
      'Tots els drets relacionats al videojoc a Andreu Beltran i Dani Lupión estudiants de 2n DAW 24-25.',
      'aboutUs',
      'aboutUs'
    )
  );

  const ol = crearElement('ol', null, 'guia', 'guia');
  [
    'Obrir la consola del navegador.',
    'Redimensionar la pantalla del joc a menys de la meitat.',
    'Amb les fletxes del teclat provar de moure el quadrat groc que apareix al taulell de joc.',
    "Abans de seguir, heu de saber que disposeu de 10s per a moure el quadrat groc després d'haver tancat el menu.",
    'Apreteu un dels botóns disponibles.'
  ].forEach(text => ol.appendChild(crearElement('li', text)));
  menu.appendChild(ol);

  document.removeEventListener('keydown', moureJugador);
}

// Funció auxiliar per crear elements HTML
function crearElement(tag, textContent = null, id = null, className = null) {
  const el = document.createElement(tag);
  if (id) el.id = id;
  if (className) el.classList.add(className);
  if (textContent) el.textContent = textContent;
  return el;
}

// --- Funció per tancar menú i començar joc ---
function tancarMenu() {
  ['menuBenvinguda', 'fonsSemiTransparent', 'menuFinal'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.remove();
  });

  // Iniciar temporitzadors i esdeveniments
  setInterval(actualitzarTemps, 1000);
  document.addEventListener('keydown', moureJugador);

  iniciarObstacles();
}

// --- Configuració i moviment jugador ---

function calcularDimensions() {
  const ampleFinestra = window.innerWidth;
  const ampladaPantalla = screen.width;

  if (ampleFinestra < ampladaPantalla / 2) {
    ample = 15;
    posicioJugadorX = Math.floor(ample / 2) + 1;
  } else {
    ample = 30;
    posicioJugadorX = Math.floor(ample / 2);
  }

  posicioJugadorY = ALT;
  posicioInicialY = ALT; // Guardem la posició original de Y
  console.log(`Ample: ${ample}, Posició jugador X: ${posicioJugadorX}`);
}


function generarGraella() {
  const campDeJoc = document.getElementById('campDeJoc');
  if (!campDeJoc) return;

  campDeJoc.innerHTML = '';
  campDeJoc.style.gridTemplateColumns = `repeat(${ample}, 1fr)`;
  campDeJoc.style.gridTemplateRows = `repeat(${ALT}, 1fr)`;

  for (let fila = 1; fila <= ALT; fila++) {
    for (let col = 1; col <= ample; col++) {
      const cel·la = crearElement('div', null, null, 'cel·la');
      cel·la.dataset.row = fila;
      cel·la.dataset.col = col;
      campDeJoc.appendChild(cel·la);
    }
  }

  posicionamentJugador();
}

function posicionamentJugador() {
  let heroi = document.querySelector('svg.heroi');

  if (!heroi) {
    heroi = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    heroi.classList.add('icon', 'heroi');

    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', 'sprites.xml#heroi');

    heroi.appendChild(use);
    document.body.appendChild(heroi);
  }

  const novaCel·la = document.querySelector(`[data-row="${posicioJugadorY}"][data-col="${posicioJugadorX}"]`);

  if (novaCel·la) {
    novaCel·la.appendChild(heroi);
    heroi.classList.add('saltant');
    setTimeout(() => heroi.classList.remove('saltant'), 400);
  } else {
    console.warn('No s\'ha trobat la cel·la per posicionar l\'heroi.');
  }
}

function moureJugador(event) {
  switch (event.key) {
    case 'ArrowUp':
      if (posicioJugadorY > posicioInicialY - 5) posicioJugadorY--;
      break;
    case 'ArrowDown':
      if (posicioJugadorY < ALT) posicioJugadorY++;
      break;
    case 'ArrowLeft':
      if (posicioJugadorX > 1) posicioJugadorX--;
      break;
    case 'ArrowRight':
      if (posicioJugadorX < ample) posicioJugadorX++;
      break;
  }
  posicionamentJugador();
}

// --- Obstacles i col·lisions ---

function iniciarObstacles() {
  obstacleGeneratorInterval = setInterval(generarObstacle, 1000);

  let intervalMoure = 500;
  obstacleMoverInterval = setInterval(moureObstacles, intervalMoure);

  setInterval(() => {
    if (intervalMoure > 100) {
      intervalMoure -= 50;
      clearInterval(obstacleMoverInterval);
      obstacleMoverInterval = setInterval(moureObstacles, intervalMoure);
    }
  }, 10000);
}

function generarObstacle() {
  const tipus = ['tronc', 'roca', 'planta'];
  const tipusAleatori = tipus[Math.floor(Math.random() * tipus.length)];
  const posX = Math.floor(Math.random() * ample) + 1;
  obstacles.push({ x: posX, y: 1, tipus: tipusAleatori });
}

function moureObstacles() {
  for (let i = obstacles.length - 1; i >= 0; i--) {
    obstacles[i].y++;

    // Comprovar col·lisió amb jugador
    if (obstacles[i].x === posicioJugadorX && obstacles[i].y === posicioJugadorY) {
      vides--;
      obstacles.splice(i, 1);
      comporvarVides();
      continue;
    }

    // Eliminar obstacles fora de graella
    if (obstacles[i].y > ALT) {
      obstacles.splice(i, 1);
      incrementarPunts(1);
    }
  }

  dibuixarObstacles();
}

function dibuixarObstacles() {
  // Netejar obstacles anteriors (excloent heroi)
  document.querySelectorAll('div.cel·la').forEach(cel·la => {
    const obs = cel·la.querySelector('svg.icon:not(.heroi)');
    if (obs) obs.remove();
  });

  // Dibuixar obstacles actuals
  obstacles.forEach(({ x, y, tipus }) => {
    const cel·la = document.querySelector(`[data-row="${y}"][data-col="${x}"]`);
    if (cel·la && !cel·la.querySelector('svg.icon:not(.heroi)')) {
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.classList.add('icon');

      const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', `sprites.xml#${tipus}`);

      svg.appendChild(use);
      cel·la.appendChild(svg);
    }
  });
}

// --- Gestió de vides i punts ---

// Funció que mostra els cors segons les vides actuals
function mostrarCors() {
  let divCors = document.getElementById('cors');
  
  if (!divCors) {
    divCors = crearElement('div', null, 'cors', 'cors');
    document.body.appendChild(divCors);
  }
  
  // Netejar cors anteriors
  divCors.innerHTML = '';
  
  for (let i = 0; i < vides; i++) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.classList.add('icon', 'cor');
    
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', 'sprites.xml#cor');
    
    svg.appendChild(use);
    divCors.appendChild(svg);
  }
}

function comporvarVides() {
    mostrarVides();  // Actualitza la vista de vides amb cors

    if (vides > 0) {
        console.log(`Encara et queden ${vides} vides`);
    } else {
        console.log("Has perdut");

        // Aturar intervals
        clearInterval(obstacleGeneratorInterval);
        clearInterval(obstacleMoverInterval);
        document.removeEventListener('keydown', moureJugador);

        // Eliminar tots els obstacles en memòria
        obstacles = [];

        // Eliminar obstacles visualment del DOM
        const cel·lesAmbObstacles = document.querySelectorAll('[data-row][data-col]');
        cel·lesAmbObstacles.forEach(el => {
            const obstacle = el.querySelector('svg.icon:not(.heroi)');
            if (obstacle) obstacle.remove();
        });

        // Crear menú final
        const menuFinal = document.createElement('div');
        menuFinal.id = 'menuFinal';
        menuFinal.classList.add('menuFinal');
        document.body.appendChild(menuFinal);

        menuFinal.appendChild(crearElement('h1', 'Jungle Scape', 'titolMenu', 'titolMenu'));
        menuFinal.appendChild(crearElement('h2', 'Oooooh, has mort', 'missatgeFinal', 'missatgeFinal'));
        menuFinal.appendChild(crearElement('h3', `Has aconseguit ${punts} punts en ${temps} segons`, 'resum', 'resum'));
        menuFinal.appendChild(crearElement('h4', 'Vols tornar a intentar-ho?', 'tornar', 'tornar'));

        // Botó de reinici
        const botoReinici = crearElement('button', 'Reiniciar', 'reinici', 'reinici');
        botoReinici.addEventListener('click', () => location.reload());
        menuFinal.appendChild(botoReinici);
    }
}

function mostrarVides() {
  // Amaguem l'anterior text de vides per evitar duplicats (opcional)
  let divVides = document.getElementById('vides');
  if (!divVides) {
    divVides = crearElement('div', null, 'vides', 'vides');
    document.body.appendChild(divVides);
  }
  divVides.textContent = ''; // O deixa buit si només mostrem cors

  mostrarCors();
}

function incrementarPunts(val) {
  punts += val;
  let divPunts = document.getElementById('punts');
  if (!divPunts) {
    divPunts = crearElement('div', null, 'punts', 'punts');
    document.body.appendChild(divPunts);
  }
  divPunts.textContent = `Punts: ${punts}`;
}

function actualitzarTemps() {
  temps++;
  let divTemps = document.getElementById('temps');
  if (!divTemps) {
    divTemps = crearElement('div', null, 'temps', 'temps');
    document.body.appendChild(divTemps);
  }
  divTemps.textContent = `Temps: ${temps}s`;
}

function mostrarFinal(missatge) {
  const menuFinal = crearElement('div', null, 'menuFinal', 'menuFinal');
  const fons = crearElement('div', null, 'fonsSemiTransparent', 'fonsSemiTransparent');

  menuFinal.appendChild(crearElement('h1', missatge));
  menuFinal.appendChild(crearElement('p', `Has aconseguit ${punts} punts en ${temps} segons.`));
  document.body.appendChild(fons);
  document.body.appendChild(menuFinal);
}

function pararJoc() {
  clearInterval(obstacleGeneratorInterval);
  clearInterval(obstacleMoverInterval);
  document.removeEventListener('keydown', moureJugador);
}
