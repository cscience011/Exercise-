# Sample data: Dictionary containing actors and their co-stars
# Replace this data with an actual dataset for real-world applications
actor_connections = {
    "Actor A": ["Actor B", "Actor C", "Actor D"],
    "Actor B": ["Actor A", "Actor C", "Actor E"],
    "Actor C": ["Actor A", "Actor B", "Actor D"],
    "Actor D": ["Actor A", "Actor C", "Actor F"],
    "Actor E": ["Actor B", "Actor F"],
    "Actor F": ["Actor D", "Actor E", "Actor G"],
    "Actor G": ["Actor F"]
}

def degrees_of_separation(actor_connections, source_actor, target_actor):
    queue = [(source_actor, 0)]  # Tuple: (actor_name, degrees of separation)
    visited = set()

    while queue:
        current_actor, degrees = queue.pop(0)
        visited.add(current_actor)

        if current_actor == target_actor:
            return degrees

        for co_star in actor_connections[current_actor]:
            if co_star not in visited:
                queue.append((co_star, degrees + 1))

    return -1  # Target actor is not reachable from the source actor

# Test the program with sample data
source_actor = "Actor A"
target_actor = "Actor G"
result = degrees_of_separation(actor_connections, source_actor, target_actor)

if result != -1:
    print(f"The degrees of separation between {source_actor} and {target_actor} is {result}.")
else:
    print(f"Sorry, there is no connection between {source_actor} and {target_actor} in the dataset.")
