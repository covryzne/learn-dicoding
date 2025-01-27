import 'package:device_preview/device_preview.dart';
import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/pages/favorite_screen.dart';
import 'package:submission_1_dicoding_flutter/pages/home_screen.dart';
import 'package:submission_1_dicoding_flutter/pages/profile_screen.dart';
import 'package:submission_1_dicoding_flutter/pages/cart_details.dart';
import 'package:submission_1_dicoding_flutter/pages/login_screen.dart';
import 'package:provider/provider.dart';
import 'package:submission_1_dicoding_flutter/providers/favorite_provider.dart';
import 'package:submission_1_dicoding_flutter/providers/cart_provider.dart';

void main() => runApp(
      DevicePreview(
        builder: (context) => MyApp(),
      ),
    );

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => FavoriteProvider()),
          ChangeNotifierProvider(create: (_) => CartProvider()),
        ],
        child: MaterialApp(
          locale: DevicePreview.locale(context),
          builder: DevicePreview.appBuilder,
          debugShowCheckedModeBanner: false,
          title: 'E - Commerce Shop',
          theme: ThemeData(
            primarySwatch: Colors.red,
            visualDensity: VisualDensity.adaptivePlatformDensity,
          ),
          initialRoute: '/',
          routes: {
            '/': (context) => const LoginScreen(),
            '/home': (context) => const HomePage(),
          },
        ),
      );
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int currentIndex = 0;

  final List<Widget> screens = [
    const HomeScreen(),
    const FavoriteScreen(),
    const ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'E - Commerce Shop',
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        backgroundColor: Colors.red,
        actions: [
          IconButton(
            onPressed: () => Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const CartDetails()),
            ),
            icon: const Icon(
              Icons.shopping_cart,
              color: Colors.white,
            ),
          ),
        ],
      ),
      body: screens[currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        onTap: (value) => setState(() => currentIndex = value),
        selectedItemColor: Colors.red,
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.favorite),
            label: 'Favorite',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
      ),
    );
  }
}
