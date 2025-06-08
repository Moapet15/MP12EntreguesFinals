using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;
using Microsoft.AspNetCore.Mvc;
using ProjecteVida.Models;

namespace ProjecteVida.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }

    public IActionResult Inici()
    {
        return View();
    }
    public IActionResult PresentacioProjecte()
    {
        return View();
    }
    [HttpPost]
    public IActionResult Sign_In(Usuaris persona)
    {
        // Processa les dades de la persona aquí
        // Per exemple, guarda-les a la base de dades, valida-les, etc.
        // Console.WriteLine(persona.Nom);
        // Console.WriteLine(persona.Cognoms);
        foreach (var error in ModelState.Values.SelectMany(v => v.Errors))
        {
            Console.WriteLine(error.ErrorMessage);
        }

        if (ModelState.IsValid)
        {
            // El model és vàlid, emmagatzema les dades a TempData
            TempData["Nom"] = persona.Nom;
            TempData["Cognoms"] = persona.Cognoms;
            TempData["Edat"] = persona.Edat;

            // Redirigeix a l'acció SignInOk
            return RedirectToAction("SignInOk");
        }
        else
        {
            // Si el model no és vàlid, torna a mostrar la vista amb els errors
            return View(persona);
        }
    }

    public IActionResult Sign_In()
    {
        return View();
    }
    public IActionResult SignInOk()
    {
        // Obtenim les dades emmagatzemades a TempData
        string nom = TempData["Nom"] as string;
        string cognoms = TempData["Cognoms"] as string;
        int edat = (int)TempData["Edat"];

        // Aquí pots fer el que vulguis amb les dades
        // En aquest exemple, passem les dades a la vista
        ViewBag.Nom = nom;
        ViewBag.Cognoms = cognoms;
        ViewBag.Edat = edat;

        return View();
    }

    public IActionResult Login()
    {
        // public int Usuari { get; set; }
        return View();
    }
    public IActionResult Forum()
    {
        return View();
    }
    public IActionResult Receptari()
    {
        return View();
    }
    public IActionResult BodyLab()
    {
        return View();
    }
    public IActionResult MenuUsuari()
    {
        return View();
    }
    public IActionResult Dietes()
    {
        return View();
    }
    public IActionResult Perfil()
    {
        return View();
    }
    public IActionResult SeleccioUsuari()
    {
        return View();
    }
    public IActionResult MenusUsuari()
    {
        return View();
    }
    public IActionResult MenuSetmanal()
    {
        return View();
    }
    public IActionResult ReceptaPa()
    {
        return View();
    }
    public IActionResult EntrenamentBicepsAmbMancuernas()
    {
        return View();
    }

}
