class Product {
  final int id;
  final String name;
  final String category;
  final String image;
  final String description;
  final double price;
  int quantity;
  final List<String> availableSize;
  final List<String> availableColor;

  Product({
    required this.id,
    required this.name,
    required this.category,
    required this.image,
    required this.description,
    required this.price,
    required this.quantity,
    required this.availableSize,
    required this.availableColor,
  });
}
