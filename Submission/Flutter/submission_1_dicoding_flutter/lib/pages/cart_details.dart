import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/providers/cart_provider.dart';
import 'package:flutter_slidable/flutter_slidable.dart';

class CartDetails extends StatefulWidget {
  const CartDetails({super.key});

  @override
  State<CartDetails> createState() => _CartDetailsState();
}

class _CartDetailsState extends State<CartDetails> {
  @override
  Widget build(BuildContext context) {
    final provider = CartProvider.of(context);
    final cartList = provider.cart;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Cart Details'),
        centerTitle: true,
      ),
      body: cartList.isEmpty
          ? const Center(
              child: Text(
                'Your cart is empty!',
                style: TextStyle(fontSize: 18, color: Colors.grey),
              ),
            )
          : Column(
              children: [
                Expanded(
                  child: ListView.builder(
                    itemCount: cartList.length,
                    itemBuilder: (context, index) {
                      final product = cartList[index];
                      return Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Slidable(
                          endActionPane: ActionPane(
                            motion: const ScrollMotion(),
                            children: [
                              SlidableAction(
                                onPressed: (context) {
                                  provider.removeProduct(index);
                                  setState(() {});
                                },
                                backgroundColor: Colors.red,
                                foregroundColor: Colors.white,
                                icon: Icons.delete,
                                label: 'Delete',
                              ),
                            ],
                          ),
                          child: Card(
                            elevation: 2,
                            child: ListTile(
                              leading: CircleAvatar(
                                backgroundImage: AssetImage(product.image),
                                backgroundColor: Colors.grey.shade300,
                              ),
                              title: Text(
                                product.name,
                                style: const TextStyle(
                                    fontSize: 16, fontWeight: FontWeight.bold),
                              ),
                              subtitle: Text(
                                "IDR ${product.price}",
                                style: const TextStyle(fontSize: 14),
                              ),
                              trailing: SizedBox(
                                width: 120,
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.end,
                                  children: [
                                    _buildProductQuantity(Icons.remove, index),
                                    Padding(
                                      padding: const EdgeInsets.symmetric(
                                          horizontal: 8.0),
                                      child: Text(
                                        product.quantity.toString(),
                                        style: const TextStyle(fontSize: 16),
                                      ),
                                    ),
                                    _buildProductQuantity(Icons.add, index),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  width: MediaQuery.of(context).size.width,
                  alignment: Alignment.center,
                  height: MediaQuery.of(context).size.height * 0.1,
                  decoration: const BoxDecoration(
                    color: Colors.red,
                    borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(15),
                      topRight: Radius.circular(15),
                    ),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Flexible(
                        child: Text(
                          'Total: IDR ${provider.getTotalPrice()}',
                          style: const TextStyle(
                            fontSize:
                                20, // Tingkatkan ukuran font agar tetap terlihat
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                          overflow: TextOverflow
                              .ellipsis, // Mencegah teks melampaui batas
                        ),
                      ),
                      ElevatedButton.icon(
                        onPressed: () {},
                        icon: const Icon(Icons.shopping_cart),
                        label: const Text('Checkout'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white,
                          foregroundColor: Colors.red,
                        ),
                      ),
                    ],
                  ),
                )
              ],
            ),
    );
  }

  Widget _buildProductQuantity(IconData icon, int index) {
    return GestureDetector(
      onTap: () {
        setState(() {
          if (icon == Icons.add) {
            CartProvider.of(context, listen: false).incrementQuantity(index);
          } else if (icon == Icons.remove) {
            if (CartProvider.of(context, listen: false).cart[index].quantity >
                0) {
              CartProvider.of(context, listen: false).decrementQuantity(index);
            }
          }
        });
      },
      child: Container(
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: Colors.red.shade100,
        ),
        child: Icon(icon, color: Colors.red),
      ),
    );
  }
}
