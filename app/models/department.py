from sqlmodel import SQLModel, Field, Relationship

class Department(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    name: str = Field(max_length = 255)

    employees: list['Employee'] | None = Relationship(back_populates = 'department', 
                                                      cascade_delete = False)