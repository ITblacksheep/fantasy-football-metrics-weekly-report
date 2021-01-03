from calculate.bad_boy_stats import BadBoyStats
import pytest

def test_local_file_missing(test_data_dir):
    with pytest.raises(FileNotFoundError):
        bad_boy_stats = BadBoyStats(
            data_dir=test_data_dir,
            save_data=True,
            dev_offline=True,
            refresh=False
        )

def test_bad_boy_init(test_data_dir,test_player_info):
    bad_boy_stats = BadBoyStats(
        data_dir=test_data_dir,
        save_data=True,
        dev_offline=False,
        refresh=True
    )
    bad_boy_stats.generate_crime_categories_json()

    print(f"Player Bad Boy crime for {test_player_info['player_full_name']}: {bad_boy_stats.get_player_bad_boy_crime(test_player_info['player_full_name'], test_player_info['player_team_abbr'], test_player_info['player_position'])}")
    print(f"Player Bad Boy crime for {test_player_info['player_full_name']}: {bad_boy_stats.get_player_bad_boy_points(test_player_info['player_full_name'], test_player_info['player_team_abbr'], test_player_info['player_position'])}")

    assert bad_boy_stats.bad_boy_data is not None