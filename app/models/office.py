from sqlmodel import SQLModel, Field, Relationship

class Office(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    address: str = Field(max_length = 255)
    city: str = Field(max_length = 255)
    country: str = Field(max_length = 64)
    phone: str = Field(max_length = 16)

    employees: list['Employee'] | None = Relationship(back_populates = 'office',
                                                      cascade_delete = False)