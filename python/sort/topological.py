#!/usr/bin/env python3

# Topological sort (a.k.a. dependency graph).
# Traverse a graph with no cycles (DAG: directed acyclical graph) starting with
# a given node and ensure nodes are ordered such that all children come last.
# The first node cannot be a child of any other node.

# Find itinerary of tickets. Start at JFK.

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# expected output: ["JFK","MUC","LHR","SFO","SJC"]

def find_itinerary(tickets):
    result = []

    # First construct the hashmap. Key on source.
    ticketmap = { ticket[0]: ticket[1] for ticket in tickets }

    # Define the traversal function.
    def dfs(src):
        if src in ticketmap:
            dfs(ticketmap[src])
            result.insert(0, src)
    dfs('JFK')

    # Only the starting flights are listed. Show the last destination.
    result.append(ticketmap[result[-1]])

    return result

print(find_itinerary(tickets))
