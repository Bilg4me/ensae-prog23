from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.00.in"

g = graph_from_file(data_path + file_name)
print(g)