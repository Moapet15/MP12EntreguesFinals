<?php
session_start();
require_once 'includes/db.php';
require_once 'includes/functions.php';

$products = getProducts($db);
include 'includes/header.php';
?>

<div class="container mt-4">
    <h1 class="mb-4">Botiga en línia</h1>
    <div class="row">
        <?php foreach ($products as $product): ?>
        <div class="col-md-3 mb-3">
            <div class="card h-100">
                <img src="assets/img/product-placeholder.png" class="card-img-top" alt="Producte">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title"><?= htmlspecialchars($product['name']) ?></h5>
                    <p class="card-text"><?= htmlspecialchars($product['description']) ?></p>
                    <p class="card-text"><strong><?= number_format($product['price'], 2) ?> €</strong></p>
                    <form method="post" action="cart.php" class="mt-auto">
                        <input type="hidden" name="product_id" value="<?= $product['id'] ?>">
                        <input type="number" name="quantity" value="1" min="1" class="form-control mb-2" />
                        <button type="submit" name="add_to_cart" class="btn btn-primary btn-block">Afegir al carro</button>
                    </form>
                </div>
            </div>
        </div>
        <?php endforeach; ?>
    </div>
</div>

<?php include 'includes/footer.php'; ?>