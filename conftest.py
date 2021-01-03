import pytest
import pathlib

@pytest.fixture
def test_data_dir():
    return pathlib.Path.cwd() / 'output' / 'data' / 'testing'

@pytest.fixture
def test_player_info():
    player = {
        "player_first_name": "Dion",
        "player_last_name": "Lewis",
        "player_full_name": "Dion Lewis",
        "player_team_abbr": "PHI",
        "player_position": "RB"}
    return player