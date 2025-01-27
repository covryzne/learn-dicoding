import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/pages/login_screen.dart'; // Pastikan import LoginScreen

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Account',
            style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Center(
              child: CircleAvatar(
                radius: 60,
                backgroundImage: AssetImage('assets/avatars/avatar.jpg'),
                backgroundColor: Colors.grey.shade300,
              ),
            ),
            const SizedBox(height: 16),
            const Text(
              'Shendi Teuku',
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Card(
              elevation: 2,
              margin: const EdgeInsets.symmetric(vertical: 8),
              child: ListTile(
                leading: const Icon(Icons.email, color: Colors.red),
                title: const Text('Email'),
                subtitle: const Text('shendyteuku2@gmail.com'),
              ),
            ),
            Card(
              elevation: 2,
              margin: const EdgeInsets.symmetric(vertical: 8),
              child: ListTile(
                leading: const Icon(Icons.phone, color: Colors.red),
                title: const Text('Phone'),
                subtitle: const Text('+62 895 121 725'),
              ),
            ),
            Card(
              elevation: 2,
              margin: const EdgeInsets.symmetric(vertical: 8),
              child: ListTile(
                leading: const Icon(Icons.location_on, color: Colors.red),
                title: const Text('Address'),
                subtitle: const Text('114, Madiun, East Java'),
              ),
            ),
            const Spacer(),
            ElevatedButton.icon(
              onPressed: () {
                // Logout action, akan kembali ke LoginScreen
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (context) => const LoginScreen()),
                );
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Logged out')),
                );
              },
              icon: const Icon(Icons.logout, color: Colors.white),
              label: const Text('Logout'),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                foregroundColor: Colors.white,
                padding:
                    const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(8),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
