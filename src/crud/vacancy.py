from models.vacancy import VacancyModel
from sqlalchemy.orm import Session

def get_data(db: Session):
    try:
        data = db.query(VacancyModel).filter(VacancyModel.positionname == 'ad').all()
        return data
    except Exception as ex:
        db.close()
        raise ex
