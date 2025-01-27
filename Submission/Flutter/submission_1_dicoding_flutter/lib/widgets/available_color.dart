import 'package:flutter/material.dart';

class AvailableColor extends StatefulWidget {
  final Color color;
  final bool isSelected;
  const AvailableColor({Key? key, required this.color, this.isSelected = false})
      : super(key: key);

  @override
  State<AvailableColor> createState() => _AvailableColorState();
}

class _AvailableColorState extends State<AvailableColor> {
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
        height: 40,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: widget.color,
          border: Border.all(
            color: isSelected ? Colors.black : Colors.grey,
            width: isSelected ? 2 : 1,
          ),
        ),
        child: isSelected
            ? const Icon(
                Icons.check,
                color: Colors.white,
              )
            : null,
      ),
    );
  }
}

Color mapColorFromString(String color) {
  switch (color.toLowerCase()) {
    case 'red':
      return Colors.red;
    case 'blue':
      return Colors.blue;
    case 'green':
      return Colors.green;
    default:
      return Colors.grey;
  }
}
