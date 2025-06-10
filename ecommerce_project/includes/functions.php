<?php
function getProducts($db) {
    $stmt = $db->query("SELECT * FROM products");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getProductById($db, $id) {
    $stmt = $db->prepare("SELECT * FROM products WHERE id = ?");
    $stmt->execute([$id]);
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

function calculateCartTotals($cart, $db) {
    $subtotal = 0;
    foreach ($cart as $id => $qty) {
        $product = getProductById($db, $id);
        if ($product) {
            $subtotal += $product['price'] * $qty;
        }
    }
    $tax = $subtotal * 0.21;
    $total = $subtotal + $tax;
    return ['subtotal' => $subtotal, 'tax' => $tax, 'total' => $total];
}
?>