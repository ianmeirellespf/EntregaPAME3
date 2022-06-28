from  .extensions import db

class basemodel(db.Model):
     
    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.save(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

