# Tests for Cloud AI Processing
from Edithra.backend.cloud_processing import analyze_game_data

def test_cloud_analysis():
    """Tests AI cloud processing functionality."""
    mock_data = {"player": "test_user", "score": 5000}
    result = analyze_game_data(mock_data)
    assert "analysis" in result




