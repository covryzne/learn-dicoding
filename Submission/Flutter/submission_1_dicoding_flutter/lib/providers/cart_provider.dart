import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/models/product.dart';
import 'package:provider/provider.dart';

class CartProvider extends ChangeNotifier {
  final List<Product> _cart = [];
  List<Product> get cart => _cart;

  void toggleProduct(Product product) {
    if (_cart.contains(product)) {
      for (Product element in _cart) {
        element.quantity++;
      }
    } else {
      _cart.add(product);
    }
    notifyListeners();
  }

  void removeProduct(int index) {
    _cart.removeAt(index);
    notifyListeners();
  }

  getTotalPrice() {
    double total = 0;
    for (Product element in _cart) {
      total += element.price * element.quantity;
    }
    return double.parse(total.toStringAsFixed(4));
  }

  incrementQuantity(int index) => _cart[index].quantity++;
  decrementQuantity(int index) => _cart[index].quantity--;

  static CartProvider of(
    BuildContext context, {
    bool listen = true,
  }) {
    return Provider.of<CartProvider>(
      context,
      listen: listen,
    );
  }
}
