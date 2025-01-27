import 'package:flutter/material.dart';

class AvailableSize extends StatefulWidget {
  final String size;
  final bool isClothing;
  const AvailableSize({Key? key, required this.size, this.isClothing = true})
      : super(key: key);

  @override
  State<AvailableSize> createState() => _AvailableSizeState();
}

class _AvailableSizeState extends State<AvailableSize> {
  bool isSelected = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() {
          isSelected = !isSelected;
        });
      },
      child: Container(
        margin: const EdgeInsets.only(right: 10),
        width: 40,
        height: 30,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: isSelected
              ? (widget.isClothing ? Colors.red : Colors.red)
              : Colors.white10,
          borderRadius: BorderRadius.circular(6),
          border: Border.all(color: Colors.grey),
        ),
        child: Text(
          widget.size,
          textAlign: TextAlign.center,
          style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 12,
            color: isSelected ? Colors.white : Colors.black,
          ),
        ),
      ),
    );
  }
}
