import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
total_videos = 1000
viral_videos = 50
shared_interest_weight = 0.6
num_trials = 10000
max_swipes = 200

# Generate video IDs
videos = np.arange(total_videos)
viral_ids = set(np.random.choice(videos, viral_videos, replace=False))

# Assign weights: viral videos get more weight
def get_weights():
    weights = np.ones(total_videos)
    for i in range(total_videos):
        if i in viral_ids:
            weights[i] += 3  # boost for viral videos
    return weights / weights.sum()

# Run Monte Carlo simulation
swipe_counts = []

for _ in range(num_trials):
    weights_a = get_weights()
    weights_b = get_weights()

    seen_a = set()
    seen_b = set()

    for swipe in range(1, max_swipes + 1):
        video_a = np.random.choice(videos, p=weights_a)
        video_b = np.random.choice(videos, p=weights_b)

        seen_a.add(video_a)
        seen_b.add(video_b)

        if video_a in seen_b or video_b in seen_a or video_a == video_b:
            swipe_counts.append(swipe)
            break
    else:
        swipe_counts.append(max_swipes)  # if no match within max_swipes

# Plot the distribution of swipe counts
plt.figure(figsize=(10, 6))
plt.hist(swipe_counts, bins=range(1, max_swipes + 1), edgecolor='black', alpha=0.7)
plt.title("Distribution of Swipes Until Overlap (10,000 Trials)")
plt.xlabel("Number of Swipes Until Same Video Seen by Both Users")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# Summary statistics
average_swipes = np.mean(swipe_counts)
median_swipes = np.median(swipe_counts)
average_swipes, median_swipes
