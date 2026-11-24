from pydantic import BaseModel, Field

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int = Field(ge=1, le=50)

class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=120)
    customer_phone: str = Field(min_length=8, max_length=30)
    delivery_address: str = Field(min_length=5, max_length=500)
    items: list[OrderItemIn] = Field(min_length=1)

class OrderOut(BaseModel):
    id: int
    customer_name: str
    total: float
    status: str
    payment_status: str

    class Config:
        from_attributes = True
