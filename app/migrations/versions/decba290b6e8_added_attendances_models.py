"""added attendances models

Revision ID: decba290b6e8
Revises: 33818da4d544
Create Date: 2024-04-01 17:26:01.985461

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision = 'decba290b6e8'
down_revision = '23d781cba4c3'
branch_labels = None
depends_on = None


def upgrade():
    # Crear el Enum para las razones de ausencia
    absence_reason_enum = ENUM('illness', 'personal matter', 'medical appointment', 'rainy day', 'other',
                               name='absence_reason_enum')

    # Crear la tabla 'attendances'
    op.create_table('attendances',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('date', sa.Date(), nullable=False),
                    sa.Column('is_rainy_day', sa.Boolean(), nullable=False, default=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False),
                    )

    # Crear la tabla 'attendance_details'
    op.create_table('attendance_details',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True),
                    sa.Column('attendance_id', UUID(as_uuid=True)),
                    sa.Column('student_id', UUID(as_uuid=True),),
                    sa.Column('is_present', sa.Boolean(), nullable=False, default=True),
                    sa.Column('absence_reason', absence_reason_enum, nullable=True),
                    sa.ForeignKeyConstraint(['student_id'], ['students.id']),
                    sa.ForeignKeyConstraint(['attendance_id'], ['attendances.id']),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False),
                    )


def downgrade():
    # Comandos para revertir los cambios
    op.drop_table('attendance_details')
    op.drop_table('attendances')

    # Eliminar el Enum
    sa.Enum(name='absence_reason_enum').drop(op.get_bind(), checkfirst=True)
