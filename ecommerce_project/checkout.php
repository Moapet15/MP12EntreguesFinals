<?php
session_start();
require_once 'includes/db.php';
require_once 'includes/functions.php';

if (!isset($_SESSION['cart']) || empty($_SESSION['cart'])) {
    header('Location: index.php');
    exit;
}

$totals = calculateCartTotals($_SESSION['cart'], $db);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Simulem pagament correcte
    // Aquí aniria la integració real amb Stripe
    $_SESSION['cart'] = [];
    header('Location: success.php');
    exit;
}

include 'includes/header.php';
?>

<div class="container mt-4">
    <h1>Pagament</h1>
    <p>Import total: <strong><?= number_format($totals['total'], 2) ?> €</strong></p>
    <form method="post" action="checkout.php">
        <button type="submit" class="btn btn-primary">Pagar amb Stripe (simulat)</button>
    </form>
    <a href="cart.php" class="btn btn-secondary mt-3">Tornar al carro</a>
</div>

<?php include 'includes/footer.php'; ?>