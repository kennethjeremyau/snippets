#!/usr/bin/env python3

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
