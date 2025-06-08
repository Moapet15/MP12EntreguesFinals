// using System;
// using System.Collections.Generic;
// using System.Linq;
// using System.Threading.Tasks;
// using Microsoft.AspNetCore.Mvc;
// using Microsoft.AspNetCore.Mvc.Rendering;
// using Microsoft.EntityFrameworkCore;
// using ProjecteVida.Data;
// using ProjecteVida.Models;
// using SQLitePCL;

// namespace ProjecteVida.Controllers
// {
//     public class UsuarisController : Controller
//     {
//         private readonly ProjecteVidaContext _context;
//         public UsuarisController(ProjecteVidaContext context)
//         {
//             _context = context;
//         }
//         // GET: Usuaris
//         public async Task<IActionResult> Index()
//         {
//             return View(await _context.Persona.ToListAsync());
//         }
//     }
// }