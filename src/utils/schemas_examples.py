from datetime import datetime

user_schema = {
    "example": {
        "first_name": "Challenge",
        "last_name": "Demo",
        "years_previous_experience": 5,
        "skills": [{
                        "name": "Python",
                        "experience": 2
                    }],
        "update_date": datetime.utcnow()
    }
}