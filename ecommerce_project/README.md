# Projecte E-commerce PHP

Aquest projecte és una botiga online bàsica feta amb PHP, SQLite i Bootstrap.

## Funcionament

- `index.php`: Mostra els productes disponibles.
- `cart.php`: Carro de la compra amb edició de quantitats.
- `checkout.php`: Simulació de pagament amb Stripe.
- `admin/`: Dashboard d'administració bàsic.

## Requisits

- PHP 7.4+
- SQLite
- Composer per instal·lar Stripe PHP SDK (no inclòs en aquest zip)

## Instal·lació

1. Col·loca els fitxers al servidor web.
2. Executa `composer require stripe/stripe-php` a la carpeta `stripe/` si vols integrar Stripe real.
3. Obre `index.php` al navegador.

## Notes

El pagament amb Stripe està simulat per facilitar l'exercici.