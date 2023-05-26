"""empty message

Revision ID: 2bd2d3fedcc6
Revises: 
Create Date: 2023-05-26 19:23:51.088584

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2bd2d3fedcc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('product')
    op.drop_table('issue_order_item')
    op.drop_table('purchase_order')
    op.drop_table('issue_order')
    op.drop_table('purchase_order_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase_order_item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('unit_price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['purchase_order.id'], name='purchase_order_item_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='purchase_order_item_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='purchase_order_item_pkey')
    )
    op.create_table('issue_order',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('issue_order_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('order_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('recipient', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('PREPARED', 'APPROVED', 'RECEIVED', name='issue_enum'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], name='issue_order_created_by_fkey'),
    sa.PrimaryKeyConstraint('id', name='issue_order_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('supplier', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('PREPARED', 'APPROVED', 'PURCHASED', name='purchaser_enum'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], name='purchase_order_created_by_fkey'),
    sa.PrimaryKeyConstraint('id', name='purchase_order_pkey')
    )
    op.create_table('issue_order_item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('unit_price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['issue_order.id'], name='issue_order_item_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='issue_order_item_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='issue_order_item_pkey')
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('category', postgresql.ENUM('FOOD', 'BEVERAGE', 'CLEANING', 'STATIONERY', name='category_enum'), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('unit_price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('ADMIN', 'STORE_KEEPER', 'MANAGER', 'PURCHASER', 'USER', name='users_enum'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    # ### end Alembic commands ###
