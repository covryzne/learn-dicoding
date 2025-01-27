import 'package:flutter/material.dart';
import 'package:submission_1_dicoding_flutter/providers/favorite_provider.dart';
import 'package:flutter_slidable/flutter_slidable.dart';

class FavoriteScreen extends StatefulWidget {
  const FavoriteScreen({super.key});

  @override
  State<FavoriteScreen> createState() => _FavoriteScreenState();
}

class _FavoriteScreenState extends State<FavoriteScreen> {
  @override
  Widget build(BuildContext context) {
    final provider = FavoriteProvider.of(context);
    final finaList = provider.favorites;

    return Scaffold(
        body: Column(
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 20, left: 20),
          child: Row(
            children: const [
              Text(
                "Favorites",
                style: TextStyle(
                  fontSize: 27,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
        ),
        // Cek apakah list favorit kosong
        Expanded(
            child: finaList.isEmpty
                ? Center(
                    child: Text(
                      'No favorite items!',
                      style: TextStyle(fontSize: 18, color: Colors.grey),
                    ),
                  )
                : ListView.builder(
                    itemCount: finaList.length,
                    itemBuilder: (context, index) {
                      return Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Slidable(
                          endActionPane: ActionPane(
                              motion: const ScrollMotion(),
                              children: [
                                SlidableAction(
                                  onPressed: (context) {
                                    finaList.removeAt(index);
                                    setState(() {});
                                  },
                                  icon: Icons.delete,
                                  backgroundColor: Colors.red,
                                  foregroundColor: Colors.white,
                                  label: 'Delete',
                                )
                              ]),
                          child: ListTile(
                            title: Text(
                              finaList[index].name,
                              style: const TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                            subtitle: Text(
                              finaList[index].description,
                              style: const TextStyle(fontSize: 14),
                              overflow: TextOverflow.ellipsis,
                            ),
                            leading: CircleAvatar(
                              backgroundImage:
                                  AssetImage(finaList[index].image),
                              backgroundColor: Colors.grey.shade300,
                            ),
                            trailing: Text(
                              "IDR ${finaList[index].price}",
                              style: const TextStyle(
                                  fontSize: 14, fontWeight: FontWeight.bold),
                            ),
                            tileColor: Colors.white70,
                          ),
                        ),
                      );
                    }))
      ],
    ));
  }
}
