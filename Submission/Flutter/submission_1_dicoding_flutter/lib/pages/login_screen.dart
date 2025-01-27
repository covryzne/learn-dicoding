import 'package:flutter/material.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool _isLoading = false;

  void _login() {
    setState(() {
      _isLoading = true;
    });

    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        _isLoading = false;
      });

      if (_usernameController.text == "user" &&
          _passwordController.text == "password") {
        Navigator.pushReplacementNamed(context, '/home');
      } else {
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text("Login Failed"),
            content: const Text("Incorrect username or password."),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: const Text("OK"),
              ),
            ],
          ),
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.red.shade50,
      appBar: AppBar(
        title: const Text(
          "Login",
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        backgroundColor: Colors.red,
        elevation: 0,
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 25),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const SizedBox(height: 10),
              Image.asset(
                'assets/logo/logo.png',
                height: 300,
              ),
              const SizedBox(height: 20),
              _buildTextField(
                controller: _usernameController,
                label: 'Username',
                isPassword: false,
              ),
              const SizedBox(height: 20),
              _buildTextField(
                controller: _passwordController,
                label: 'Password',
                isPassword: true,
              ),
              const SizedBox(height: 30),
              _isLoading
                  ? const CircularProgressIndicator(
                      valueColor: AlwaysStoppedAnimation(Colors.red),
                    )
                  : ElevatedButton(
                      onPressed: _login,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.red,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(12),
                        ),
                        padding: const EdgeInsets.symmetric(vertical: 18),
                        minimumSize: const Size(double.infinity, 60),
                      ),
                      child: const Text(
                        "Login",
                        style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white),
                      ),
                    ),
              const SizedBox(height: 20),
              TextButton(
                onPressed: () {},
                child: const Text(
                  "Forgot Password?",
                  style:
                      TextStyle(color: Colors.red, fontWeight: FontWeight.bold),
                ),
              ),
              const SizedBox(height: 30),
              TextButton(
                onPressed: () {},
                child: const Text(
                  "Don't have an account? Sign up",
                  style:
                      TextStyle(color: Colors.red, fontWeight: FontWeight.bold),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    required bool isPassword,
  }) {
    return TextField(
      controller: controller,
      obscureText: isPassword,
      decoration: InputDecoration(
        labelText: label,
        labelStyle: TextStyle(color: Colors.red.shade800),
        filled: true,
        fillColor: Colors.white,
        contentPadding:
            const EdgeInsets.symmetric(vertical: 16, horizontal: 20),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: Colors.red.shade800),
        ),
      ),
    );
  }
}
