<?php
session_start();
// Simulació llista d'usuaris (exemple estàtic)
$users = [
    ['id'=>1,'name'=>'Joan','email'=>'joan@example.com'],
    ['id'=>2,'name'=>'Maria','email'=>'maria@example.com'],
    ['id'=>3,'name'=>'Pere','email'=>'pere@example.com'],
];

include '../includes/header.php';
?>

<div class="container mt-4">
    <h1>Gestió d'usuaris</h1>
    <table class="table">
        <thead>
            <tr><th>ID</th><th>Nom</th><th>Email</th></tr>
        </thead>
        <tbody>
            <?php foreach($users as $user): ?>
            <tr>
                <td><?= $user['id'] ?></td>
                <td><?= htmlspecialchars($user['name']) ?></td>
                <td><?= htmlspecialchars($user['email']) ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
    <a href="index.php" class="btn btn-secondary">Tornar al dashboard</a>
</div>

<?php include '../includes/footer.php'; ?>