// using Microsoft.EntityFrameworkCore;
// using Microsoft.Extensions.DependencyInjection;
// using ProjecteVida.Data;
// using ProjecteVida.Models;
// using System;
// using System.Linq;

// namespace MvcProjecteVida.Models;
// public static class SeedData{
//     public static void Initialize(IServiceProvider serviceProvider){
//         using (var context = new ProjecteVidaContext(serviceProvider.GetRequiredService<DbContextOptions<ProjecteVidaContext>>())){
//             if (context.Persones.Any()){
//                 return;
//             }
//             context.Persones.AddRange(
//                 new Persona{
//                     Nom = "Andreu",
//                     Cognoms = "Beltran i Franquet",
//                     Edat = 28
//                 }
//             );
//         }
//     }
// }
