# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Shortest Path.
"""
Dijkstra's Algorithm.

This program takes in a graph from the internet and
calculates the sum of the shortest paths to every node
"""
import argparse
import urllib.request
import gzip
import heapq
import copy
from sys import stderr, stdout

parser = argparse.ArgumentParser(description="Dijkstra's Shortest Path")
parser.add_argument("--graph", help="URL to compressed graph")
parser.add_argument("--source", help="Node ID to run Dijkstra's from")
args = parser.parse_args()

try:
    with urllib.request.urlopen(args.graph) as compressed_graph:
        graph_file = open("graph.txt", "wb")
        graph_file.write(compressed_graph.read())
        graph_file.close()
except ValueError:
    stderr.write("Inaccessible URL")
    exit(0)

graph = gzip.open("graph.txt", "rb").read().decode("utf-8")
source = args.source


class GraphNode:
    """This defines a node in our digraph."""

    def __init__(self, node_id):
        """Define a node in our digraph."""
        self.node_id = node_id
        self.neighbors = []
        self.distance = float("inf")

    def __lt__(self, other):
        """Allow heapq to sort the graph properly."""
        return self.distance < other.distance


node_list = []
num_nodes = 0
num_edges = 0
counter = 0
try:
    for string in graph.splitlines():
        if not string.startswith("#"):
            if num_nodes == 0:
                graph_dimensions = string.split(" ")
                num_nodes = graph_dimensions[0]
                num_edges = graph_dimensions[1]
                for i in range(1, int(num_nodes) + 1):
                    node_list.append(GraphNode(i))
            elif counter > int(num_edges):
                stderr.write("More edges than specified")
                exit(0)
            else:
                node_data = string.split(" ")
                source_id = node_data[0]
                dest_id = int(node_data[1])
                weight = int(node_data[2])
                if int(weight) < 0:
                    stderr.write("negative edge")
                    exit(0)
                if int(source_id) > int(num_nodes) or \
                        int(dest_id) > int(num_nodes):
                    stderr.write("incorrect node id")
                    exit(0)
                node_list[int(source_id) - 1].neighbors\
                    .append([dest_id, weight])
            counter += 1
except (ValueError, IndexError):
    stderr.write("Incorrect Format")
    exit(0)


def ignore_inf_sum(array):
    """Ignore inf when summing distances array."""
    sum = 0
    for i in array:
        if i != float("inf"):
            sum += i
    return sum


def dijkstra(start_index):
    """
    Implement Dijkstra's Algorithm.

    Based on my final assignment for CSE2010 where we
    programmed Dijkstra's in C.
    """
    distances_array = []
    for i in range(len(node_list)):
        if i == start_index:
            distances_array.append(0)
        else:
            distances_array.append(float("inf"))

    node_list[start_index].distance = 0

    node_queue = copy.deepcopy(node_list)
    heapq.heapify(node_queue)
    while len(node_queue) > 1:
        min_index = heapq.heappop(node_queue)
        for neighbor in min_index.neighbors:
            for i in node_queue:
                if i.node_id == neighbor[0]:
                    if distances_array[min_index.node_id - 1] + \
                            neighbor[1] < distances_array[neighbor[0] - 1]:
                        new_edge_weight = \
                            distances_array[min_index.node_id - 1] \
                            + neighbor[1]
                        distances_array[neighbor[0] - 1] = new_edge_weight
                        i.distance = new_edge_weight
                        heapq.heapify(node_queue)
    stdout.write(str(ignore_inf_sum(distances_array)))


dijkstra(int(source) - 1)
