<?php
session_start();
// Simulació d'informes (dades estàtiques)
$sales_report = [
    ['month'=>'Abril','sales'=>1200],
    ['month'=>'Maig','sales'=>1500],
    ['month'=>'Juny','sales'=>900],
];

include '../includes/header.php';
?>

<div class="container mt-4">
    <h1>Informe de vendes</h1>
    <table class="table">
        <thead><tr><th>Mes</th><th>Vendes (€)</th></tr></thead>
        <tbody>
            <?php foreach($sales_report as $row): ?>
            <tr>
                <td><?= htmlspecialchars($row['month']) ?></td>
                <td><?= number_format($row['sales'], 2) ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
    <a href="index.php" class="btn btn-secondary">Tornar al dashboard</a>
</div>

<?php include '../includes/footer.php'; ?>