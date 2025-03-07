"""Initial migration

Revision ID: 34bf72832c90
Revises: 
Create Date: 2025-03-04 17:55:16.536926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bf72832c90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_subject',
    sa.Column('subject_id', sa.UUID(), nullable=False),
    sa.Column('subject_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('account_type', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('date_joined', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('class',
    sa.Column('class_id', sa.UUID(), nullable=False),
    sa.Column('subject_id', sa.UUID(), nullable=False),
    sa.Column('class_name', sa.String(length=100), nullable=False),
    sa.Column('class_code', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['class_subject.subject_id'], ),
    sa.PrimaryKeyConstraint('class_id')
    )
    op.create_table('direct_message',
    sa.Column('message_id', sa.UUID(), nullable=False),
    sa.Column('sender_id', sa.UUID(), nullable=False),
    sa.Column('receiver_id', sa.UUID(), nullable=False),
    sa.Column('content', sa.String(length=1000), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('student',
    sa.Column('student_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('major', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('tutor',
    sa.Column('tutor_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('available_hours', sa.Text(), nullable=True),
    sa.Column('hourly_rate', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('tutor_id')
    )
    op.create_table('tutor_subject',
    sa.Column('tutor_id', sa.UUID(), nullable=False),
    sa.Column('subject_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['class_subject.subject_id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutor.tutor_id'], ),
    sa.PrimaryKeyConstraint('tutor_id', 'subject_id')
    )
    op.create_table('tutoring_session',
    sa.Column('session_id', sa.UUID(), nullable=False),
    sa.Column('tutor_id', sa.UUID(), nullable=False),
    sa.Column('student_id', sa.UUID(), nullable=False),
    sa.Column('class_id', sa.UUID(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('duration', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.class_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutor.tutor_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('review',
    sa.Column('review_id', sa.UUID(), nullable=False),
    sa.Column('session_id', sa.UUID(), nullable=False),
    sa.Column('review_title', sa.String(length=200), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['tutoring_session.session_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('tutoring_session')
    op.drop_table('tutor_subject')
    op.drop_table('tutor')
    op.drop_table('student')
    op.drop_table('direct_message')
    op.drop_table('class')
    op.drop_table('user')
    op.drop_table('class_subject')
    # ### end Alembic commands ###
