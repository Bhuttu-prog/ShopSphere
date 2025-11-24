#!/usr/bin/env python3
"""
Generate a pictorial flowchart for ShopSphere User Interface Design
Shows component hierarchy and navigation flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(18, 12))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Define colors
app_color = '#4A90E2'  # Blue for app level
page_color = '#6DB33F'  # Green for pages
component_color = '#FF6B6B'  # Red for components
common_color = '#FFA500'  # Orange for common components

# Title
ax.text(6, 9.5, 'ShopSphere User Interface Design - Component Architecture', fontsize=20, fontweight='bold', 
        ha='center', va='center', family='sans-serif')

# ========== TOP: App Component ==========
app_box = FancyBboxPatch((4, 8), 4, 0.8, boxstyle="round,pad=0.15", 
                        facecolor=app_color, edgecolor='black', linewidth=2.5)
ax.add_patch(app_box)
ax.text(6, 8.4, 'App.tsx (Main Application)', fontsize=13, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(6, 8.1, 'React Router | State Management | Layout', fontsize=9, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== Common Components ==========
header_box = FancyBboxPatch((1, 6.5), 2, 0.6, boxstyle="round,pad=0.1", 
                           facecolor=common_color, edgecolor='black', linewidth=2)
ax.add_patch(header_box)
ax.text(2, 6.8, 'Header.tsx', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(2, 6.5, 'Navigation | Cart | Auth', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

footer_box = FancyBboxPatch((9, 6.5), 2, 0.6, boxstyle="round,pad=0.1", 
                           facecolor=common_color, edgecolor='black', linewidth=2)
ax.add_patch(footer_box)
ax.text(10, 6.8, 'Footer.tsx', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(10, 6.5, 'Links | Info', fontsize=8, ha='center', 
        va='center', color='white', family='sans-serif')

# ========== Pages Row 1 ==========
home_box = FancyBboxPatch((0.5, 5), 1.8, 0.7, boxstyle="round,pad=0.1", 
                         facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(home_box)
ax.text(1.4, 5.35, 'Home.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

products_box = FancyBboxPatch((2.5, 5), 1.8, 0.7, boxstyle="round,pad=0.1", 
                             facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(products_box)
ax.text(3.4, 5.35, 'Products.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

cart_box = FancyBboxPatch((4.5, 5), 1.8, 0.7, boxstyle="round,pad=0.1", 
                         facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(cart_box)
ax.text(5.4, 5.35, 'Cart.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

checkout_box = FancyBboxPatch((6.5, 5), 1.8, 0.7, boxstyle="round,pad=0.1", 
                             facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(checkout_box)
ax.text(7.4, 5.35, 'Checkout.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

orders_box = FancyBboxPatch((8.5, 5), 1.8, 0.7, boxstyle="round,pad=0.1", 
                           facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(orders_box)
ax.text(9.4, 5.35, 'Orders.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# ========== Pages Row 2 ==========
login_box = FancyBboxPatch((1, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1", 
                          facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(login_box)
ax.text(1.75, 3.8, 'Login.tsx', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

register_box = FancyBboxPatch((2.8, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1", 
                             facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(register_box)
ax.text(3.55, 3.8, 'Register.tsx', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

profile_box = FancyBboxPatch((4.6, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1", 
                            facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(profile_box)
ax.text(5.35, 3.8, 'Profile.tsx', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

wishlist_box = FancyBboxPatch((6.4, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1", 
                              facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(wishlist_box)
ax.text(7.15, 3.8, 'Wishlist.tsx', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

payment_box = FancyBboxPatch((8.2, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1", 
                            facecolor=page_color, edgecolor='black', linewidth=2)
ax.add_patch(payment_box)
ax.text(8.95, 3.8, 'Payment.tsx', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# ========== Product Components ==========
productcard_box = FancyBboxPatch((1, 2), 2, 0.6, boxstyle="round,pad=0.1", 
                                 facecolor=component_color, edgecolor='black', linewidth=2)
ax.add_patch(productcard_box)
ax.text(2, 2.3, 'ProductCard.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(2, 2, 'Product Tile', fontsize=8, ha='center', va='center', 
        color='white', family='sans-serif')

productdetail_box = FancyBboxPatch((3.5, 2), 2, 0.6, boxstyle="round,pad=0.1", 
                                   facecolor=component_color, edgecolor='black', linewidth=2)
ax.add_patch(productdetail_box)
ax.text(4.5, 2.3, 'ProductDetail.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(4.5, 2, 'Detail View', fontsize=8, ha='center', va='center', 
        color='white', family='sans-serif')

productlist_box = FancyBboxPatch((6, 2), 2, 0.6, boxstyle="round,pad=0.1", 
                                 facecolor=component_color, edgecolor='black', linewidth=2)
ax.add_patch(productlist_box)
ax.text(7, 2.3, 'ProductList.tsx', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')
ax.text(7, 2, 'List View', fontsize=8, ha='center', va='center', 
        color='white', family='sans-serif')

# ========== Arrows from App ==========
arrow1 = FancyArrowPatch((5, 8), (2, 7.1), arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((6, 8), (6, 7.1), arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((7, 8), (10, 7.1), arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow3)

# ========== Arrows to Pages ==========
arrow4 = FancyArrowPatch((6, 6.5), (1.4, 5.7), arrowstyle='->', lw=1.5, color='gray', linestyle='--')
ax.add_patch(arrow4)

arrow5 = FancyArrowPatch((6, 6.5), (3.4, 5.7), arrowstyle='->', lw=1.5, color='gray', linestyle='--')
ax.add_patch(arrow5)

arrow6 = FancyArrowPatch((6, 6.5), (5.4, 5.7), arrowstyle='->', lw=1.5, color='gray', linestyle='--')
ax.add_patch(arrow6)

arrow7 = FancyArrowPatch((6, 6.5), (7.4, 5.7), arrowstyle='->', lw=1.5, color='gray', linestyle='--')
ax.add_patch(arrow7)

arrow8 = FancyArrowPatch((6, 6.5), (9.4, 5.7), arrowstyle='->', lw=1.5, color='gray', linestyle='--')
ax.add_patch(arrow8)

# ========== Arrows from Products to Components ==========
arrow9 = FancyArrowPatch((3.4, 5), (2, 2.6), arrowstyle='->', lw=1.5, color='darkred')
ax.add_patch(arrow9)

arrow10 = FancyArrowPatch((3.4, 5), (4.5, 2.6), arrowstyle='->', lw=1.5, color='darkred')
ax.add_patch(arrow10)

arrow11 = FancyArrowPatch((3.4, 5), (7, 2.6), arrowstyle='->', lw=1.5, color='darkred')
ax.add_patch(arrow11)

# ========== Navigation Flow Labels ==========
ax.text(3.5, 6.8, 'Routes', fontsize=9, ha='center', style='italic', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7), family='sans-serif')

ax.text(4.5, 4.2, 'Uses', fontsize=9, ha='center', style='italic', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.7), family='sans-serif')

# ========== Technology Stack Box ==========
tech_box = FancyBboxPatch((0.5, 0.5), 11, 0.8, boxstyle="round,pad=0.1", 
                          facecolor='#E8F4F8', edgecolor='black', linewidth=2)
ax.add_patch(tech_box)
ax.text(6, 0.9, 'UI Technology Stack: React 19 + TypeScript | Redux Toolkit | React Router | Tailwind CSS | Axios', 
        fontsize=10, ha='center', va='center', fontweight='bold', family='sans-serif')

# Save
plt.tight_layout()
plt.savefig('ShopSphere_UI_Design_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)
print("✓ UI Design Flowchart saved as 'ShopSphere_UI_Design_Flowchart.png'")
plt.close()


