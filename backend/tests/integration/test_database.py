import sys
import uuid

from sqlalchemy import select

sys.path.insert(0, "backend")

from app.db.database import SessionLocal
from app.models import Template


def test_create_and_read_template():
    session = SessionLocal()

    try:
        template = Template(
            id=uuid.uuid4(),
            name=f"Test Template {uuid.uuid4().hex[:8]}",
            description="Template creado durante una prueba de integración",
            version="1.0.0",
            is_active=True,
        )

        session.add(template)
        session.commit()
        session.refresh(template)

        result = session.scalar(
            select(Template).where(Template.id == template.id)
        )

        assert result is not None
        assert result.id == template.id
        assert result.name == template.name
        assert result.version == "1.0.0"
        assert result.is_active is True

    finally:
        if "template" in locals():
            session.delete(template)
            session.commit()

        session.close()