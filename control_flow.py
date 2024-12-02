import networkx as nx
import matplotlib.pyplot as plt

def draw_control_flow_for_is_prime():
    # Create a directed graph for is_prime
    G = nx.DiGraph()

    # Add nodes representing the control flow blocks
    G.add_node("Start")
    G.add_node("Check n < 5 or n is even or n % 3 == 0")
    G.add_node("Return True (2 <= n <= 3)")
    G.add_node("Calculate s and d")
    G.add_node("Loop over a values")
    G.add_node("Check pow(a, d, n)")
    G.add_node("Inner loop on s")
    G.add_node("Return False")
    G.add_node("Return True")

    # Add edges representing transitions
    G.add_edges_from([
        ("Start", "Check n < 5 or n is even or n % 3 == 0"),
        ("Check n < 5 or n is even or n % 3 == 0", "Return True (2 <= n <= 3)"),
        ("Check n < 5 or n is even or n % 3 == 0", "Calculate s and d"),
        ("Calculate s and d", "Loop over a values"),
        ("Loop over a values", "Check pow(a, d, n)"),
        ("Check pow(a, d, n)", "Inner loop on s"),
        ("Inner loop on s", "Return False"),
        ("Inner loop on s", "Return True"),
        ("Check pow(a, d, n)", "Loop over a values"),
        ("Loop over a values", "Return True"),
    ])

    # Draw the graph
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=8, font_weight="bold", arrowsize=20)
    plt.title("Control Flow Diagram for is_prime", fontsize=16)
    plt.show()


def draw_control_flow_for_gcd():
    # Create a directed graph for gcd
    G = nx.DiGraph()

    # Add nodes representing the control flow blocks
    G.add_node("Start")
    G.add_node("Check y != 0")
    G.add_node("Update x, y = y, x % y")
    G.add_node("Return x")

    # Add edges representing transitions
    G.add_edges_from([
        ("Start", "Check y != 0"),
        ("Check y != 0", "Update x, y = y, x % y"),
        ("Update x, y = y, x % y", "Check y != 0"),
        ("Check y != 0", "Return x"),
    ])

    # Draw the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, font_weight="bold", arrowsize=20)
    plt.title("Control Flow Diagram for gcd", fontsize=16)
    plt.show()


# Draw control flow diagrams for both functions
draw_control_flow_for_is_prime()
draw_control_flow_for_gcd()
