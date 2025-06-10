<?php
session_start();
// Admin bàsic sense login, només per exemple
include '../includes/header.php';
?>

<div class="container mt-4">
    <h1>Dashboard Administració</h1>
    <ul>
        <li><a href="users.php">Gestió d'usuaris</a></li>
        <li><a href="reports.php">Informes de venda</a></li>
    </ul>
</div>

<?php include '../includes/footer.php'; ?>