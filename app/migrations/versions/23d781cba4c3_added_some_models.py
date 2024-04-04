"""added some models

Revision ID: 23d781cba4c3
Revises: 
Create Date: 2024-04-01 15:51:39.237686

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '23d781cba4c3'
down_revision = '33818da4d544'
branch_labels = None
depends_on = None


def upgrade():
    # Crear tabla 'schools'
    op.create_table('schools',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(), nullable=False),
                    sa.Column('latitude', sa.Float(), nullable=True),
                    sa.Column('longitude', sa.Float(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )

    # Crear tabla 'teachers'
    op.create_table('teachers',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('document', sa.String(), nullable=False, unique=True),
                    sa.Column('specialty', sa.String(), nullable=False),
                    sa.Column('school_id', UUID(as_uuid=True), sa.ForeignKey('schools.id')),
                    sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )

    # Crear tabla 'preceptors'
    op.create_table('preceptors',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('document', sa.String(), nullable=False, unique=True),
                    sa.Column('school_id', UUID(as_uuid=True), sa.ForeignKey('schools.id')),
                    sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )

    # Crear tabla 'classrooms'
    op.create_table('classrooms',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )

    # Crear tabla 'courses'
    op.create_table('courses',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('school_id', UUID(as_uuid=True), sa.ForeignKey('schools.id')),
                    sa.Column('teacher_id', UUID(as_uuid=True), sa.ForeignKey('teachers.id')),
                    sa.Column('preceptor_id', UUID(as_uuid=True), sa.ForeignKey('preceptors.id')),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )

    # Crear tabla 'students'
    op.create_table('students',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('document', sa.String(), nullable=False, unique=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('nationality', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
                    sa.Column('school_id', UUID(as_uuid=True), sa.ForeignKey('schools.id')),
                    sa.Column('classroom_id', UUID(as_uuid=True), sa.ForeignKey('classrooms.id'), nullable=True),
                    sa.Column('course_id', UUID(as_uuid=True), sa.ForeignKey('courses.id'), nullable=True),
                    sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False)
                    )


def downgrade():
    # Comandos para revertir los cambios
    op.drop_table('students')
    op.drop_table('courses')
    op.drop_table('classrooms')
    op.drop_table('preceptors')
    op.drop_table('teachers')
    op.drop_table('schools')
