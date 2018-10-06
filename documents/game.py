from mongoengine import Document, StringField, IntField, DynamicField

class Game(Document):
		game_id = StringField(primary_key=True)
		away_team_id = IntField()
		home_team_id = IntField()
		home_code = StringField()
		away_code = StringField()
		home_pitching = DynamicField()
		away_pitching = DynamicField()
		home_additional_pitching = DynamicField()
		away_additional_pitching = DynamicField()
		home_batting = DynamicField()
		away_batting = DynamicField()
		home_additional_batting = DynamicField()
		away_additional_batting = DynamicField()