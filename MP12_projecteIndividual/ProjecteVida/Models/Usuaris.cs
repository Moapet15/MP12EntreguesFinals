namespace ProjecteVida.Models;
public class Usuaris
{
    public string? Nom { get; set; }
    public string? Cognoms { get; set; }
    public int Edat { get; set; }
    public string? CorreuElectronic { get; set; }
    public string? CorreuElectronicRepetit { get; set; }
    public string? Contrassenya { get; set; }
    public string? ContrassenyaRepetida { get; set; }
    public string? Adressa { get; set; }
    public int CodiPostal { get; set; }
    public string? Poblacio { get; set; }
    public string? Sexe { get; set; }
    public float Pes { get; set; }
    public float Alsada { get; set; }
    public float HoresDeFeina { get; set; }
    public string? EstilDeVida { get; set; }
}