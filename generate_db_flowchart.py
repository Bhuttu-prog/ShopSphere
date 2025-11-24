#!/usr/bin/env python3
"""
Generate a pictorial flowchart for ShopSphere Database Design
Shows entity relationships and data flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(18, 14))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Define colors
entity_color = '#4A90E2'  # Blue for entities
relation_color = '#6DB33F'  # Green for relationships
primary_color = '#FF6B6B'  # Red for primary keys
foreign_color = '#FFA500'  # Orange for foreign keys

# Title
ax.text(6, 9.5, 'ShopSphere Database Design - Entity Relationship Flow', fontsize=20, fontweight='bold', 
        ha='center', va='center', family='sans-serif')

# ========== CENTER: USER Entity ==========
user_box = FancyBboxPatch((5, 7), 2, 1, boxstyle="round,pad=0.15", 
                         facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(user_box)
ax.text(6, 7.7, 'USER', fontsize=14, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(6, 7.3, 'id (PK)\nemail\npassword\nfirstName\nlastName\nrole', fontsize=9, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== TOP: PRODUCT Entity ==========
product_box = FancyBboxPatch((1, 5), 2, 1.2, boxstyle="round,pad=0.15", 
                            facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(product_box)
ax.text(2, 5.8, 'PRODUCT', fontsize=14, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(2, 5.3, 'id (PK)\nname\nprice\ncategory\nstock\nrating', fontsize=9, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== RIGHT: ORDER Entity ==========
order_box = FancyBboxPatch((8, 5), 2, 1.2, boxstyle="round,pad=0.15", 
                          facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(order_box)
ax.text(9, 5.8, 'ORDER', fontsize=14, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(9, 5.3, 'id (PK)\nuser_id (FK)\ntotalAmount\nstatus\ncreatedAt', fontsize=9, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== BOTTOM LEFT: CART Entity ==========
cart_box = FancyBboxPatch((1, 2.5), 2, 0.8, boxstyle="round,pad=0.1", 
                          facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(cart_box)
ax.text(2, 3, 'CART', fontsize=12, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(2, 2.6, 'id (PK)\nuser_id (FK)\nproduct_id (FK)\nquantity', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== BOTTOM CENTER: WISHLIST Entity ==========
wishlist_box = FancyBboxPatch((4.5, 2.5), 2, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(wishlist_box)
ax.text(5.5, 3, 'WISHLIST', fontsize=12, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(5.5, 2.6, 'id (PK)\nuser_id (FK)\nproduct_id (FK)\ncreatedAt', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== BOTTOM RIGHT: REVIEW Entity ==========
review_box = FancyBboxPatch((8, 2.5), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(review_box)
ax.text(9, 3, 'REVIEW', fontsize=12, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(9, 2.6, 'id (PK)\nuser_id (FK)\nproduct_id (FK)\nrating\ncomment', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== RIGHT SIDE: ORDER_ITEM Entity ==========
orderitem_box = FancyBboxPatch((10.5, 4.5), 1.5, 1, boxstyle="round,pad=0.1", 
                               facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(orderitem_box)
ax.text(11.25, 5.2, 'ORDER_ITEM', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(11.25, 4.7, 'id (PK)\norder_id (FK)\nproduct_id (FK)\nquantity\nprice', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== LEFT SIDE: PRODUCT_ASSOCIATION Entity ==========
assoc_box = FancyBboxPatch((0, 4.5), 1.5, 1, boxstyle="round,pad=0.1", 
                           facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(assoc_box)
ax.text(0.75, 5.2, 'PRODUCT_ASSOCIATION', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(0.75, 4.7, 'id (PK)\nproduct_id (FK)\nassociated_product_id (FK)\ntype\nstrength', fontsize=7, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== BELOW ORDER: ORDER_STATUS_HISTORY Entity ==========
status_box = FancyBboxPatch((8, 0.5), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=entity_color, edgecolor='black', linewidth=2)
ax.add_patch(status_box)
ax.text(9, 1, 'ORDER_STATUS_HISTORY', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(9, 0.6, 'id (PK)\norder_id (FK)\nstatus\nchangedAt', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== RELATIONSHIPS ==========
# User to Order (One-to-Many)
arrow1 = FancyArrowPatch((7, 7.5), (8, 5.8), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow1)
ax.text(7.5, 6.5, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# User to Cart (One-to-Many)
arrow2 = FancyArrowPatch((5, 7), (2, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow2)
ax.text(3.5, 5, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# User to Wishlist (One-to-Many)
arrow3 = FancyArrowPatch((5, 7), (5.5, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow3)
ax.text(5.25, 5, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# User to Review (One-to-Many)
arrow4 = FancyArrowPatch((6.5, 7), (8, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow4)
ax.text(7.25, 5, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to Cart (One-to-Many)
arrow5 = FancyArrowPatch((2, 5), (2, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow5)
ax.text(2.3, 4, '1:N', fontsize=10, ha='left', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to Wishlist (One-to-Many)
arrow6 = FancyArrowPatch((3, 5.2), (4.5, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow6)
ax.text(3.75, 4, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to Review (One-to-Many)
arrow7 = FancyArrowPatch((3, 5), (8, 3.2), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow7)
ax.text(5.5, 4, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to ProductAssociation (One-to-Many)
arrow8 = FancyArrowPatch((1, 5.5), (0.5, 5), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow8)
ax.text(0.75, 5.3, '1:N', fontsize=9, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to ProductAssociation (Many-to-One for associated product)
arrow9 = FancyArrowPatch((1.5, 5.5), (0.75, 5.5), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow9)
ax.text(1.1, 5.7, 'N:1', fontsize=9, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.2", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Order to OrderItem (One-to-Many)
arrow10 = FancyArrowPatch((10, 5.5), (10.5, 5), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow10)
ax.text(10.25, 5.3, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Product to OrderItem (One-to-Many)
arrow11 = FancyArrowPatch((3, 5.5), (10.5, 5), arrowstyle='->', lw=2, color=relation_color, 
                         connectionstyle="arc3,rad=0.3")
ax.add_patch(arrow11)
ax.text(6.75, 5.8, '1:N', fontsize=10, ha='center', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Order to OrderStatusHistory (One-to-Many)
arrow12 = FancyArrowPatch((9, 5), (9, 1.3), arrowstyle='->', lw=2, color=relation_color)
ax.add_patch(arrow12)
ax.text(9.3, 3, '1:N', fontsize=10, ha='left', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8), family='sans-serif')

# Legend
legend_y = 0.2
ax.text(1, legend_y, 'Legend:', fontsize=11, fontweight='bold', family='sans-serif')
legend_box1 = FancyBboxPatch((1, legend_y-0.3), 0.4, 0.2, boxstyle="round,pad=0.05", 
                            facecolor=entity_color, edgecolor='black', linewidth=1)
ax.add_patch(legend_box1)
ax.text(1.2, legend_y-0.2, 'Entity', fontsize=9, ha='left', va='center', color='white', family='sans-serif')

legend_box2 = FancyBboxPatch((2.5, legend_y-0.3), 0.4, 0.2, boxstyle="round,pad=0.05", 
                            facecolor=relation_color, edgecolor='black', linewidth=1)
ax.add_patch(legend_box2)
ax.text(2.7, legend_y-0.2, 'Relationship', fontsize=9, ha='left', va='center', color='white', family='sans-serif')

# Save
plt.tight_layout()
plt.savefig('ShopSphere_Database_Design_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)
print("✓ Database Design Flowchart saved as 'ShopSphere_Database_Design_Flowchart.png'")
plt.close()


