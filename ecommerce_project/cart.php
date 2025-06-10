<?php
session_start();
require_once 'includes/db.php';
require_once 'includes/functions.php';

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

// Afegir producte al carro
if (isset($_POST['add_to_cart'])) {
    $product_id = (int)$_POST['product_id'];
    $quantity = max(1, (int)$_POST['quantity']);
    if (isset($_SESSION['cart'][$product_id])) {
        $_SESSION['cart'][$product_id] += $quantity;
    } else {
        $_SESSION['cart'][$product_id] = $quantity;
    }
    header('Location: cart.php');
    exit;
}

// Modificar quantitat
if (isset($_POST['update_cart'])) {
    foreach ($_POST['quantities'] as $id => $qty) {
        if ($qty <= 0) {
            unset($_SESSION['cart'][$id]);
        } else {
            $_SESSION['cart'][$id] = (int)$qty;
        }
    }
    header('Location: cart.php');
    exit;
}

$cart = $_SESSION['cart'];
$totals = calculateCartTotals($cart, $db);

include 'includes/header.php';
?>

<div class="container mt-4">
    <h1>Carro de la compra</h1>
    <?php if (empty($cart)): ?>
        <p>El teu carro està buit.</p>
        <a href="index.php" class="btn btn-primary">Tornar a la botiga</a>
    <?php else: ?>
        <form method="post" action="cart.php">
            <table class="table">
                <thead>
                    <tr>
                        <th>Producte</th>
                        <th>Preu unitari</th>
                        <th>Quantitat</th>
                        <th>Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($cart as $id => $qty):
                        $product = getProductById($db, $id);
                        if (!$product) continue;
                        $subtotal = $product['price'] * $qty;
                    ?>
                    <tr>
                        <td><?= htmlspecialchars($product['name']) ?></td>
                        <td><?= number_format($product['price'], 2) ?> €</td>
                        <td>
                            <input type="number" name="quantities[<?= $id ?>]" value="<?= $qty ?>" min="0" class="form-control" style="width: 80px;">
                        </td>
                        <td><?= number_format($subtotal, 2) ?> €</td>
                    </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
            <button type="submit" name="update_cart" class="btn btn-warning">Actualitzar carro</button>
        </form>
        <div class="mt-4">
            <p>Subtotal: <strong><?= number_format($totals['subtotal'], 2) ?> €</strong></p>
            <p>IVA (21%): <strong><?= number_format($totals['tax'], 2) ?> €</strong></p>
            <p>Total: <strong><?= number_format($totals['total'], 2) ?> €</strong></p>
            <a href="checkout.php" class="btn btn-success">Anar a pagar</a>
        </div>
    <?php endif; ?>
</div>

<?php include 'includes/footer.php'; ?>