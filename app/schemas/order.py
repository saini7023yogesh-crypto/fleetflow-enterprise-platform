from pydantic import BaseModel, ConfigDict, Field


# Data required when creating an order
class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    product_name: str = Field(min_length=1, max_length=150)
    quantity: int = Field(gt=0)


# Data required when updating order status
class OrderStatusUpdate(BaseModel):
    status: str = Field(pattern="^(pending|processing|completed|cancelled)$")


# Format returned by the API
class OrderResponse(BaseModel):
    id: int
    customer_name: str
    product_name: str
    quantity: int
    status: str

    model_config = ConfigDict(from_attributes=True)
