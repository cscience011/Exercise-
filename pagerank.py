import numpy as np

def pagerank_sampling(adj_matrix, num_samples, damping_factor=0.85, epsilon=1e-8):
    n = adj_matrix.shape[0]
    pagerank = np.ones(n) / n

    for _ in range(num_samples):
        pagerank = (1 - damping_factor) / n + damping_factor * adj_matrix.dot(pagerank)

    return pagerank

def pagerank_iteration(adj_matrix, damping_factor=0.85, epsilon=1e-8):
    n = adj_matrix.shape[0]
    pagerank = np.ones(n) / n
    prev_pagerank = np.zeros(n)

    while np.linalg.norm(pagerank - prev_pagerank) > epsilon:
        prev_pagerank = pagerank
        pagerank = (1 - damping_factor) / n + damping_factor * adj_matrix.dot(pagerank)

    return pagerank

def main():
    # Sample adjacency matrix for a small web graph
    adj_matrix = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ])

    num_samples = 10000

    # Calculate PageRank scores using sampling
    pagerank_sampling_scores = pagerank_sampling(adj_matrix, num_samples)

    # Calculate PageRank scores using iteration
    pagerank_iteration_scores = pagerank_iteration(adj_matrix)

    # Print the results
    print("PageRank Results from Sampling (n =", num_samples, ")")
    for i, score in enumerate(pagerank_sampling_scores):
        print(f"{i + 1}.html: {score:.4f}")

    print("\nPageRank Results from Iteration")
    for i, score in enumerate(pagerank_iteration_scores):
        print(f"{i + 1}.html: {score:.4f}")

if __name__ == "__main__":
    main()
