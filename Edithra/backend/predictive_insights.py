# AI Predictive Gaming Insights
import numpy as np

def predict_win_probability(stats):
    """Predicts player's probability of winning based on statistics."""
    if "accuracy" not in stats or "speed" not in stats:
        return "Invalid input data"
    
    win_prob = (0.6 * stats["accuracy"] + 0.4 * stats["speed"]) / 2
    return min(max(win_prob, 0), 1)  # Ensure value is between 0 and 1




