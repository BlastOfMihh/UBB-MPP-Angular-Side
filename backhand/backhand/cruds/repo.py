from .motivation import Motivation
from .founder import Founder
from faker import Faker

class Repo:
    def __init__(self, db) -> None:
        # self.entities=[ ]
        self.db=db

    def add(self, entity):
        self.db.session.add(entity)
        self.db.session.commit()
    
    def founder_add(self, founder):
        self.db.session.add(founder)
        self.db.session.commit()

    def remove(self, id):
        Motivation.query.filter(Motivation._id ==id).delete()
        self.db.session.commit()

    def founder_remove(self, id):
        Founder.query.filter(Founder._id==id).delete()
        self.db.session.commit()


    def update(self, id, entity:Motivation):
        motivation = Motivation.query.filter_by(_id=id).first()
        if motivation is not None:
            motivation.name=entity.name
            motivation.strength=entity.strength
            self.db.session.commit()
    
    def founder_update(self, id, founder:Founder):
        found_founder:Founder = Founder.query.filter_by(_id=id).first()
        if founder is not None:
            found_founder.name=founder.name
            found_founder.motivation_id = founder.motivation_id
            found_founder.email = founder.email
            self.db.session.commit()


    def get(self, id):
        return Motivation.query.filter_by(_id=id).first()
    def founder_get(self, id):
        return Founder.query.filter_by(_id=id).first()

    def get_all(self):
        return Motivation.query.all()
    def founder_get_all(self):
        return Founder.query.all()
    
    def commit_to_db(self):
        self.db.session.commit()

    def add_secondary_faker_data(self, count=100000):
        from random import choice
        fakerul=Faker()
        elements=self.get_all()
        all_ids=[x._id for x in elements]
        # print(all_ids)
        new_founders=[]
        for i in range(count):
            _id=choice(all_ids)
            new_founder=Founder(fakerul.name(), fakerul.email(), _id)
            new_founders.append(new_founder)
        self.db.session.bulk_save_objects(new_founders)
        self.db.session.commit()

    def get_founders_by_motivation_id(self, id):
        founders = Founder.query.filter(Founder.motivation_id ==id)
        return founders