using ProjecteVida.Models;
using System.Data.SQLite;

public class SqlLite
{
    public void CrearEsquema()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();
            string createSchemaaQuery = "create schema if not exists ProjecteVida";
            using (SQLiteCommand createSchemaComand = new SQLiteCommand(createSchemaaQuery, connection))
            {
                createSchemaComand.ExecuteNonQuery();
            }
        }
    }
    public void CrearTablaUsuaris()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists Usuaris (Id int primary key auto_increment, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), TipusUsuari varchar(50) not null)";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
    public void CrearTablaContrassenya()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists Contrassenya (Id int primary key auto_increment, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), Contrassenya varchar(50) not null, foreign key (Id) references Usuaris (Id))";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
    public void CrearTablaClients()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists Clients (Id int primary key auto_increment, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), Genere varchar(50), Edat int not null, CorreuElectronic varchar(100) not null, Adreça varchar(100), CodiPostal int, Poblacio varchar(50), foreign key (Id) references Usuaris (Id))";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
    public void CrearTablaEmpleats()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists Empleats (Id int primary key auto_increment, IdEmpleat int not null, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), foreign key (Id) references Usuaris (Id), foreign key (Id) references Clients (Id))";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
    public void CrearTablaProfessionals()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists InformacioProfessionals (Id int primary key auto_increment, IdEmpleat int not null, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), Genere varchar(50), Edat int not null, CorreuElectronic varchar(100) not null, Adreça varchar(100), CodiPostal int, Poblacio varchar(50), Carrec varchar(50), IniciContractacio date not null, FiContractacio date, EstatCivil varchar(50), Fills boolean, NombreFills int, foreign key (IdEmpleat) references Usuaris (Id))";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
        public void CrearTablaInfoSalut()
    {
        string connectionString = "Data Source=personas.db";
        using (SQLiteConnection connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            // Para crear la tabla
            string createTableQuery = "create table if not exists InformacioDeSalut (Id int primary key auto_increment, Nom varchar(50) not null, Cognom1 varchar(50) not null, Cognom2 varchar(50), Pes float not null, Alçada float not null, HoresJornada float, TipusDeFeina varchar(50) not null, EstilDeVida varchar(50) not null, Patologies varchar(500) not null, Alergies varchar(500) not null, Intolerancies varchar(500) not null, foreign key (Id) references Clients (Id), foreign key (Id) references Empleats (Id))";
            using (SQLiteCommand createTableCommand = new SQLiteCommand(createTableQuery, connection))
            {
                createTableCommand.ExecuteNonQuery();
            }

            connection.Close();
        }
    }
}