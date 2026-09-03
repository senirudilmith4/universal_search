import uuid
from sqlalchemy import  String, DateTime,Text, ForeignKey
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy.sql import func
from db.database import Base

# mapped_column is used to define the columns in the database tables for sqlalchemy ORM models.
# Mapped is used to specify the type of the column for python type checking and autocompletion
class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    source_type: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

     # One-to-Many Relationship to Chunks
    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document", 
        cascade="all, delete-orphan"
    )


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    chunk_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("documents.id", ondelete="CASCADE"), nullable=False)
    page_number: Mapped[int] # Implicitly NOT NULL, no mapped_column needed!
    
    # Text type is better for chunks as they can exceed standard string limits
    chunk_text: Mapped[str] = mapped_column(Text) 
    
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Many-to-One Relationship back to Document
    document: Mapped["Document"] = relationship(back_populates="chunks")