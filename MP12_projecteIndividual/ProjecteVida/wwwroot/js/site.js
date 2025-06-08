// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.
    let finestraEmergent;

    function obrirEmergent() {
        // Obre la finestra emergent amb un contingut en blanc i dimensions personalitzades
        finestraEmergent = window.open('', 'popupWindow', 'width=600,height=500');

        // Comprova si la finestra emergent està bloquejada pel navegador
        if (finestraEmergent === null || typeof (finestraEmergent) === 'undefined') {
            alert('La finestra emergent ha estat bloquejada pel navegador. Si us plau, permeteu les finestres emergents per a aquest lloc.');
            return;
        }

        // Escriu el contingut a la finestra emergent
        finestraEmergent.document.write(`
                <html>
                <head>
                    <title>Informació de la seva tarjeta</title>
                </head>
                <body>
                    <h1>Introdueixi els valors en els camps corresponents</h1>
                    <p>Nom del titular: Andreu</p>
                    <p>Numero de la tarjeta de credit: XXXXXXXXXXXXXXXXXXX</p>
                    <p>CSV: 000</p>
                    <button>Enviar</button>
                </body>
                </html>
            `);

        finestraEmergent.focus();
    }