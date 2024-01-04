class Job:
    def __init__(self, audio_path, model, user, _id):
        self._id = _id
        self.audio_path = audio_path
        self.model = model
        self.user = user

    def transcribe(self):
        

class Plan:
    def __init__(self, name, minutes, price, _id):
        self._id = _id
        self.name = name
        self.minutes = minutes
        self.price = price

class User:
    def __init__(self, username, email, plan: Plan, _id, minutes_used):
        self._id = _id
        self.username = username
        self.plan = plan
        self.email = email
        self.minutes_used = minutes_used

    def get_minutes_left(self):
        minutes_included = self.plan.minutes
        minutes_used = self.minutes_used
        minutes_left = minutes_included-minutes_used

        return minutes_left

class Transcribe:
    def __init__(self, job: Job):
        self.job = job