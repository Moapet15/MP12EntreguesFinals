const canvas = document.getElementById("snowCanvas");
const ctx = canvas.getContext("2d");

// Configurar les dimensions del canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Array per emmagatzemar els flocs de neu
const snowflakes = [];

// Crear flocs de neu
function createSnowflakes() {
    for (let i = 0; i < 100; i++) { // Quantitat de flocs
        snowflakes.push({
            x: Math.random() * canvas.width,  // Posició horitzontal aleatòria
            y: Math.random() * canvas.height, // Posició vertical aleatòria
            radius: Math.random() * 4 + 1,    // Mida del floc
            speed: Math.random() * 1 + 0.5,   // Velocitat de caiguda
            angle: Math.random() * Math.PI * 2, // Angle de moviment horitzontal
        });
    }
}

// Dibuixar flocs de neu
function drawSnowflakes() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Netejar canvas

    snowflakes.forEach(flake => {
        ctx.beginPath();
        ctx.arc(flake.x, flake.y, flake.radius, 0, Math.PI * 2);
        ctx.fillStyle = "white";
        ctx.fill();
    });
}

// Actualitzar la posició dels flocs
function updateSnowflakes() {
    snowflakes.forEach(flake => {
        flake.y += flake.speed; // Mou cap avall
        flake.x += Math.sin(flake.angle); // Lleuger moviment lateral
        flake.angle += 0.01; // Ajust de l'angle

        // Reapareix a la part superior si surt per la part inferior
        if (flake.y > canvas.height) flake.y = -flake.radius;
        if (flake.x > canvas.width) flake.x = -flake.radius;
        if (flake.x < -flake.radius) flake.x = canvas.width + flake.radius;
    });
}

// Animació
function animate() {
    drawSnowflakes();
    updateSnowflakes();
    requestAnimationFrame(animate); // Tornar a cridar
}

// Inicialitzar
createSnowflakes();
animate();

// Ajustar dimensions del canvas en redimensionar la finestra
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    snowflakes.length = 0; // Netejar flocs
    createSnowflakes();    // Crear nous flocs
});
