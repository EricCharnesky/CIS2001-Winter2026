from planesandtrains import Dock


number_of_train_items = (2, 7, 1 )
number_of_plane_items = (3, 2)
train_items = (2, 2, 2, 1, 3, 2, 2, 2, 1, 2 )
plane_items = (2, 1, 1, 2, 1)

dock = Dock(number_of_train_items, number_of_plane_items, train_items, plane_items)
dock.load_trains()
dock.load_planes()

print(dock.get_train_full_times())
print(dock.get_plane_full_times())