<?php
// Connexió a SQLite
try {
    $db = new PDO('sqlite:database.sqlite');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    die('No es pot connectar a la base de dades: ' . $e->getMessage());
}

// Crear taula i dades inicials si no existeixen
$db->exec("CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)");

$count = $db->query("SELECT COUNT(*) FROM products")->fetchColumn();
if ($count == 0) {
    $db->exec("INSERT INTO products (name, description, price) VALUES
        ('Camiseta', 'Camiseta de cotó 100%', 15.00),
        ('Pantalons', 'Pantalons texans blau', 30.00),
        ('Samarreta esportiva', 'Samarreta per esport', 22.50),
        ('Sabatilles', 'Sabatilles còmode per caminar', 45.00)
    ");
}
?>