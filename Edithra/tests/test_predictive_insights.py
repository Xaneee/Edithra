# Predictive Insights Tests
from Edithra.backend.predictive_insights import predict_win_probability

def test_predict_win_probability():
    """Tests AI-driven predictive gaming insights."""
    stats = {"accuracy": 80, "speed": 90}
    result = predict_win_probability(stats)
    
    assert 0 <= result <= 1




