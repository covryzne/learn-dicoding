import 'package:submission_1_dicoding_flutter/models/product.dart';

class MyProduct {
  static List<Product> allProductsList = [
    Product(
      id: 1,
      name: 'Nike Big Swoosh',
      price: 1.299,
      image: 'assets/jackets/jacket_1.png',
      category: 'Trending Now',
      description:
          'The Nike Big Swoosh Sportswear jacket is a bold statement piece for outdoor enthusiasts. Made with wind-resistant material, it provides lightweight protection against the elements. The oversized Swoosh logo across the back enhances its sporty aesthetic. Perfect for jogging, casual outings, or layering during cooler weather.',
      quantity: 1,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Alphabet Zipper',
      price: 1.599,
      image: 'assets/jackets/jacket_2.png',
      category: 'Out of Stock',
      description:
          'The Nike Alphabet Zipper Hooded Jacket combines cozy comfort with a playful design. Crafted from soft fleece material, it offers warmth and flexibility. The abstract alphabet pattern adds a unique flair, while the full-front zipper ensures easy wearability. This hoodie is a versatile option for relaxed days or light workouts.',
      quantity: 0,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Vintage Bomber',
      price: 1.999,
      image: 'assets/jackets/jacket_3.png',
      category: 'Trending Now',
      description:
          'The Nike Vintage Bomber Jacket channels retro vibes with a modern twist. Made from windproof material and featuring a soft lining, it ensures both style and comfort. The ribbed collar, cuffs, and hem bring a classic bomber jacket feel, while the subtle Nike branding adds a touch of sophistication. Ideal for urban explorers.',
      quantity: 10,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Mens College',
      price: 1.699,
      image: 'assets/jackets/jacket_4.png',
      category: 'Out of Stock',
      description:
          'Show off a sporty yet polished look with the Nike Mens College Jacket. Inspired by varsity style, it features a durable construction with contrasting color panels. The embroidered Nike logo on the chest adds an elegant detail, while its lightweight design makes it perfect for layering in cooler temperatures.',
      quantity: 0,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Mens Lebron',
      price: 2.599,
      image: 'assets/jackets/jacket_5.png',
      category: 'Trending Now',
      description:
          'Designed for both style and performance, the Nike Mens Lebron Protect Jacket offers premium protection against unpredictable weather. Made from water-resistant material, it keeps you dry and comfortable. The sleek design, complete with functional pockets and subtle Nike branding, reflects LeBron James signature excellence. A jacket that seamlessly blends form and function.',
      quantity: 20,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Kids Court',
      price: 1.899,
      image: 'assets/sneakers/sneaker_1.png',
      category: 'Trending Now',
      description:
          'The Nike Kids Court is a perfect blend of comfort and durability, crafted specifically for active young adventurers. Its lightweight design features a flexible sole for unrestricted movement, while the non-marking rubber outsole ensures excellent grip on various surfaces. With its modern, sporty look and iconic Nike branding, this sneaker is ideal for school, playtime, and beyond.',
      quantity: 1,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Nike Court Legacy',
      price: 1.499,
      image: 'assets/sneakers/sneaker_2.png',
      category: 'Out of Stock',
      description:
          'A stylish nod to retro fashion, the Nike Court Legacy Lift combines timeless design with modern comfort. The platform sole offers a subtle elevation, enhancing both style and support. Made from premium leather, this sneaker ensures durability while maintaining a sleek appearance. It’s a versatile choice that complements casual outfits effortlessly.',
      quantity: 0,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 1 Sea',
      price: 2.699,
      image: 'assets/sneakers/sneaker_3.png',
      category: 'Trending Now',
      description:
          'The Air Jordan 1 Sea Foam reimagines the legendary silhouette with a refreshing palette of soft green and white. Crafted from premium leather, it delivers both elegance and durability. The high-top design offers added ankle support, while the Air-Sole unit ensures responsive cushioning. This sneaker strikes the perfect balance between heritage style and contemporary fashion.',
      quantity: 10,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 1 Retro',
      price: 1.999,
      image: 'assets/sneakers/sneaker_4.png',
      category: 'Out of Stock',
      description:
          'The Air Jordan 1 Retro High celebrates the legacy of Michael Jordan with its iconic high-top design. Made with top-quality leather, it provides lasting comfort and support. The Air-Sole cushioning technology absorbs impact, making it suitable for all-day wear. Its classic colorways and sleek details make it a must-have for sneaker enthusiasts.',
      quantity: 0,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 4 Retro',
      price: 2.399,
      image: 'assets/sneakers/sneaker_5.png',
      category: 'Trending Now',
      description:
          'The Air Jordan 4 Retro elevates the game with its fusion of performance and style. Featuring breathable mesh panels and durable leather construction, it ensures comfort and longevity. The signature Air-Sole unit delivers responsive cushioning, while the unique outsole pattern offers exceptional grip. A true classic for both the court and the streets.',
      quantity: 20,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
  ];

  static List<Product> jacketsList = [
    Product(
      id: 1,
      name: 'Nike Big Swoosh',
      price: 1.299,
      image: 'assets/jackets/jacket_1.png',
      category: 'Trending Now',
      description:
          'The Nike Big Swoosh Sportswear jacket is a bold statement piece for outdoor enthusiasts. Made with wind-resistant material, it provides lightweight protection against the elements. The oversized Swoosh logo across the back enhances its sporty aesthetic. Perfect for jogging, casual outings, or layering during cooler weather.',
      quantity: 1,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Alphabet Zipper',
      price: 1.599,
      image: 'assets/jackets/jacket_2.png',
      category: 'Out of Stock',
      description:
          'The Nike Alphabet Zipper Hooded Jacket combines cozy comfort with a playful design. Crafted from soft fleece material, it offers warmth and flexibility. The abstract alphabet pattern adds a unique flair, while the full-front zipper ensures easy wearability. This hoodie is a versatile option for relaxed days or light workouts.',
      quantity: 0,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Vintage Bomber',
      price: 1.999,
      image: 'assets/jackets/jacket_3.png',
      category: 'Trending Now',
      description:
          'The Nike Vintage Bomber Jacket channels retro vibes with a modern twist. Made from windproof material and featuring a soft lining, it ensures both style and comfort. The ribbed collar, cuffs, and hem bring a classic bomber jacket feel, while the subtle Nike branding adds a touch of sophistication. Ideal for urban explorers.',
      quantity: 10,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Mens College',
      price: 1.699,
      image: 'assets/jackets/jacket_4.png',
      category: 'Out of Stock',
      description:
          'Show off a sporty yet polished look with the Nike Mens College Jacket. Inspired by varsity style, it features a durable construction with contrasting color panels. The embroidered Nike logo on the chest adds an elegant detail, while its lightweight design makes it perfect for layering in cooler temperatures.',
      quantity: 0,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
    Product(
      id: 1,
      name: 'Nike Mens Lebron',
      price: 2.599,
      image: 'assets/jackets/jacket_5.png',
      category: 'Trending Now',
      description:
          'Designed for both style and performance, the Nike Mens Lebron Protect Jacket offers premium protection against unpredictable weather. Made from water-resistant material, it keeps you dry and comfortable. The sleek design, complete with functional pockets and subtle Nike branding, reflects LeBron James signature excellence. A jacket that seamlessly blends form and function.',
      quantity: 20,
      availableSize: ['S', 'M', 'L', 'XL'],
      availableColor: ['Red', 'Blue', 'Green'],
    ),
  ];

  static List<Product> sneakersList = [
    Product(
      id: 1,
      name: 'Nike Kids Court',
      price: 1.899,
      image: 'assets/sneakers/sneaker_1.png',
      category: 'Trending Now',
      description:
          'The Nike Kids Court is a perfect blend of comfort and durability, crafted specifically for active young adventurers. Its lightweight design features a flexible sole for unrestricted movement, while the non-marking rubber outsole ensures excellent grip on various surfaces. With its modern, sporty look and iconic Nike branding, this sneaker is ideal for school, playtime, and beyond.',
      quantity: 1,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Nike Court Legacy',
      price: 1.499,
      image: 'assets/sneakers/sneaker_2.png',
      category: 'Out of Stock',
      description:
          'A stylish nod to retro fashion, the Nike Court Legacy Lift combines timeless design with modern comfort. The platform sole offers a subtle elevation, enhancing both style and support. Made from premium leather, this sneaker ensures durability while maintaining a sleek appearance. It’s a versatile choice that complements casual outfits effortlessly.',
      quantity: 0,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 1 Sea',
      price: 2.699,
      image: 'assets/sneakers/sneaker_3.png',
      category: 'Trending Now',
      description:
          'The Air Jordan 1 Sea Foam reimagines the legendary silhouette with a refreshing palette of soft green and white. Crafted from premium leather, it delivers both elegance and durability. The high-top design offers added ankle support, while the Air-Sole unit ensures responsive cushioning. This sneaker strikes the perfect balance between heritage style and contemporary fashion.',
      quantity: 10,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 1 Retro',
      price: 1.999,
      image: 'assets/sneakers/sneaker_4.png',
      category: 'Out of Stock',
      description: '',
      quantity: 0,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
    Product(
      id: 1,
      name: 'Air Jordan 4 Retro',
      price: 2.399,
      image: 'assets/sneakers/sneaker_5.png',
      category: 'Trending Now',
      description:
          'The Air Jordan 4 Retro elevates the game with its fusion of performance and style. Featuring breathable mesh panels and durable leather construction, it ensures comfort and longevity. The signature Air-Sole unit delivers responsive cushioning, while the unique outsole pattern offers exceptional grip. A true classic for both the court and the streets.',
      quantity: 20,
      availableSize: ['30', '31', '32', '33', '34', '35'],
      availableColor: ['Black', 'White', 'Red'],
    ),
  ];
}
