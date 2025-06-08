using Microsoft.EntityFrameworkCore;
using ProjecteVida.Models;


namespace ProjecteVida.Data
{
    public class ProjecteVidaContext : DbContext
    {
        public ProjecteVidaContext(DbContextOptions<ProjecteVidaContext> options)
            : base(options)
        {
        }
        public DbSet<ProjecteVida.Models.Usuaris> Persona { get; set; } = default!;
    }
}