from sqlalchemy import create_engine

DATABASE_URL = (

"postgresql://postgres:password@localhost/neuralretail"

)

engine = create_engine(

DATABASE_URL

)

print(

engine

)