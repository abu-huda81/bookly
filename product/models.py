from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    original_price = Column(Float, default=0.0, nullable=False)
    new_price = Column(Float, default=0.0, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="products")

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    images = relationship("Image", back_populates="product")

    def __repr__(self):
        return f"<Product(name={self.name})>"


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="images")

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="images")

    def __repr__(self):
        return f"<Image(url={self.url})>"
