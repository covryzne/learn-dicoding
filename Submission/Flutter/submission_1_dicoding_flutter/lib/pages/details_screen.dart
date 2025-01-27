import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/models/product.dart';
import 'package:submission_1_dicoding_flutter/pages/cart_details.dart';
import 'package:submission_1_dicoding_flutter/widgets/available_color.dart';
import 'package:submission_1_dicoding_flutter/widgets/available_size.dart';
import 'package:submission_1_dicoding_flutter/providers/cart_provider.dart';
import 'package:submission_1_dicoding_flutter/providers/favorite_provider.dart';

class DetailsScreen extends StatelessWidget {
  final Product product;
  const DetailsScreen({super.key, required this.product});

  @override
  Widget build(BuildContext context) {
    // Memisahkan provider untuk cart dan favorite
    final cartProvider = CartProvider.of(context);
    final favoriteProvider = FavoriteProvider.of(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Detail Product'),
        centerTitle: true,
      ),
      body: Stack(
        children: [
          SingleChildScrollView(
            child: Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    SizedBox(
                      height: 300,
                      width: 300,
                      child: Image.asset(product.image, fit: BoxFit.cover),
                    ),
                  ],
                ),
                const SizedBox(height: 10),
                Container(
                  padding: const EdgeInsets.all(20),
                  width: MediaQuery.of(context).size.width,
                  height: MediaQuery.of(context).size.height * 0.6,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: const BorderRadius.only(
                      topLeft: Radius.circular(30),
                      topRight: Radius.circular(30),
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey.withOpacity(0.5),
                        spreadRadius: 5,
                        blurRadius: 7,
                        offset: const Offset(0, 5),
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            product.name,
                            style: const TextStyle(
                                fontSize: 20, fontWeight: FontWeight.bold),
                          ),
                          Text(
                            "IDR ${product.price}",
                            style: const TextStyle(
                                fontSize: 20, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      Text(
                        product.description,
                        textAlign: TextAlign.justify,
                        style: const TextStyle(fontSize: 12),
                      ),
                      const SizedBox(height: 10),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: const [
                          Text(
                            "Size",
                            style: TextStyle(
                                fontSize: 16, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      Row(
                        children: product.availableSize
                            .map((e) => AvailableSize(size: e))
                            .toList(),
                      ),
                      const SizedBox(height: 10),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: const [
                          Text(
                            "Color",
                            style: TextStyle(
                                fontSize: 16, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      Row(
                        children: product.availableColor
                            .map((color) => AvailableColor(
                                  color: mapColorFromString(color),
                                ))
                            .toList(),
                      )
                    ],
                  ),
                ),
              ],
            ),
          ),
          Align(
            alignment: Alignment.topRight,
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: GestureDetector(
                onTap: () => favoriteProvider.toggleFavorite(product),
                child: Icon(
                  favoriteProvider.isExist(product)
                      ? Icons.favorite
                      : Icons.favorite_border_outlined,
                  color: Colors.red,
                ),
              ),
            ),
          )
        ],
      ),
      bottomSheet: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 0),
        child: Container(
          width: MediaQuery.of(context).size.width,
          alignment: Alignment.center,
          height: MediaQuery.of(context).size.height * 0.1,
          decoration: BoxDecoration(
            color: Colors.red,
            borderRadius: const BorderRadius.only(
              topLeft: Radius.circular(15),
              topRight: Radius.circular(15),
            ),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Padding(
                padding: const EdgeInsets.only(left: 20),
                child: Text(
                  'IDR ${product.price}',
                  style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(right: 20),
                child: ElevatedButton.icon(
                  onPressed: () {
                    cartProvider.toggleProduct(product);
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const CartDetails(),
                      ),
                    );
                  },
                  icon: const Icon(Icons.shopping_cart),
                  label: const Text("Add to Cart"),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
