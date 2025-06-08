using Microsoft.EntityFrameworkCore;
using ProjecteVida.Models;

public class ProjecteVidaContext : DbContext
{
    public ProjecteVidaContext(DbContextOptions<ProjecteVidaContext> options) : base(options) { }

    public DbSet<Usuaris> Persones { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Aquí pots configurar opcions addicionals del model si és necessari
    }
}
