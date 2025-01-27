import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/models/my_product.dart';
import 'package:submission_1_dicoding_flutter/widgets/product_card.dart';
import 'package:submission_1_dicoding_flutter/pages/details_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int isSelected = 0;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Our Products",
            style: TextStyle(
              fontSize: 27,
              fontWeight: FontWeight.bold,
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              _buildProductCategory(
                  index: 0, name: "All Products", isSelected: isSelected),
              _buildProductCategory(
                  index: 1, name: "Jackets", isSelected: isSelected),
              _buildProductCategory(
                  index: 2, name: "Sneakers", isSelected: isSelected),
            ],
          ),
          const SizedBox(height: 20),
          Expanded(
            child: isSelected == 0
                ? _buildAllProducts()
                : isSelected == 1
                    ? _buildJackets()
                    : _buildSneakers(),
          ),
        ],
      ),
    );
  }

  Widget _buildProductCategory(
      {required int index, required String name, required int isSelected}) {
    return GestureDetector(
      onTap: () {
        setState(() {
          this.isSelected = index;
        });
      },
      child: Container(
        width: 100,
        height: 40,
        margin: const EdgeInsets.only(top: 10, right: 10),
        decoration: BoxDecoration(
          color: isSelected == index ? Colors.red : Colors.red.shade300,
          borderRadius: BorderRadius.circular(10),
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.5),
              spreadRadius: 1,
              blurRadius: 2,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Center(
          child: Text(
            name,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}

Widget _buildAllProducts() => GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        childAspectRatio: (100 / 140),
        crossAxisSpacing: 12,
        mainAxisSpacing: 12,
      ),
      scrollDirection: Axis.vertical,
      itemCount: MyProduct.allProductsList.length,
      itemBuilder: (context, index) {
        final allProductsList = MyProduct.allProductsList[index];
        return GestureDetector(
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => DetailsScreen(product: allProductsList),
            ),
          ),
          child: ProductCard(product: allProductsList),
        );
      },
    );

Widget _buildJackets() => GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        childAspectRatio: (100 / 140),
        crossAxisSpacing: 12,
        mainAxisSpacing: 12,
      ),
      scrollDirection: Axis.vertical,
      itemCount: MyProduct.jacketsList.length,
      itemBuilder: (context, index) {
        final jacketsList = MyProduct.jacketsList[index];
        return GestureDetector(
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => DetailsScreen(product: jacketsList),
            ),
          ),
          child: ProductCard(product: jacketsList),
        );
      },
    );

Widget _buildSneakers() => GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        childAspectRatio: (100 / 140),
        crossAxisSpacing: 12,
        mainAxisSpacing: 12,
      ),
      scrollDirection: Axis.vertical,
      itemCount: MyProduct.sneakersList.length,
      itemBuilder: (context, index) {
        final sneakersList = MyProduct.sneakersList[index];
        return GestureDetector(
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => DetailsScreen(product: sneakersList),
            ),
          ),
          child: ProductCard(product: sneakersList),
        );
      },
    );
