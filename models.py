from database import Base
from sqlalchemy import Column,String,Integer



class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    short_url = Column(String, index=True)
    whatsapp = Column(String, index=True)
    facebook = Column(String, index=True)
    gmail = Column(String, index=True)
    

