#!/usr/bin/env python3
"""
Generate a pictorial flowchart for ShopSphere Recommendation System
Similar to ML pipeline flowchart style
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.patches as patches

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Define colors
cloud_color = '#4A90E2'  # Blue for data source
box_color = '#E8F4F8'   # Light blue for boxes
algorithm_color = '#FFD93D'  # Yellow for algorithm container
alg_box_colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181']  # Colors for individual algorithms
model_color = '#6C5CE7'  # Purple for model
final_color = '#00B894'  # Green for final output

# Title
ax.text(5, 9.5, 'System Architecture', fontsize=20, fontweight='bold', 
        ha='center', va='center')

# 1. Starting Point - Cloud shape for "ShopSphere E-commerce Data"
cloud = mpatches.Ellipse((1.5, 7.5), 2, 1.2, color=cloud_color, alpha=0.8)
ax.add_patch(cloud)
ax.text(1.5, 7.5, 'ShopSphere\nE-commerce Data', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')

# 2. Data Division - Split into three paths
# Arrow from cloud to split point
arrow1 = FancyArrowPatch((3.5, 7.5), (4.5, 7.5), 
                         arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow1)
ax.text(4, 7.8, 'Data Sources', fontsize=10, ha='center', style='italic')

# Split point (diamond shape)
split_x, split_y = 5, 7.5
diamond = mpatches.RegularPolygon((split_x, split_y), 4, radius=0.4, 
                                  orientation=0.785, color=box_color, 
                                  edgecolor='black', linewidth=1.5)
ax.add_patch(diamond)
ax.text(split_x, split_y, 'Data\nProcessing', fontsize=9, ha='center', va='center', fontweight='bold')

# Three paths from split
# Path 1: Order History (Training Data)
arrow2a = FancyArrowPatch((split_x, split_y-0.4), (3, 5.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow2a)
ax.text(3.5, 6.2, 'Order History', fontsize=9, ha='center', style='italic')

box1 = FancyBboxPatch((2, 4.5), 2, 1, boxstyle="round,pad=0.1", 
                      facecolor=box_color, edgecolor='black', linewidth=1.5)
ax.add_patch(box1)
ax.text(3, 5, 'Order History\nTraining Data', fontsize=10, ha='center', va='center', fontweight='bold')

# Path 2: Product Catalog
arrow2b = FancyArrowPatch((split_x, split_y-0.4), (5, 5.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow2b)
ax.text(5, 6.2, 'Product Catalog', fontsize=9, ha='center', style='italic')

box2 = FancyBboxPatch((4, 4.5), 2, 1, boxstyle="round,pad=0.1", 
                      facecolor=box_color, edgecolor='black', linewidth=1.5)
ax.add_patch(box2)
ax.text(5, 5, 'Product Catalog\nFeatures & Associations', fontsize=10, ha='center', va='center', fontweight='bold')

# Path 3: User Behavior
arrow2c = FancyArrowPatch((split_x, split_y-0.4), (7, 5.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow2c)
ax.text(6.5, 6.2, 'User Behavior', fontsize=9, ha='center', style='italic')

box3 = FancyBboxPatch((6, 4.5), 2, 1, boxstyle="round,pad=0.1", 
                      facecolor=box_color, edgecolor='black', linewidth=1.5)
ax.add_patch(box3)
ax.text(7, 5, 'User Behavior\nCart & Wishlist', fontsize=10, ha='center', va='center', fontweight='bold')

# 3. Arrows from data boxes to Algorithms container
arrow3a = FancyArrowPatch((3, 4.5), (3.5, 3.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow3a)

arrow3b = FancyArrowPatch((5, 4.5), (5, 3.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow3b)

arrow3c = FancyArrowPatch((7, 4.5), (6.5, 3.5), 
                          arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow3c)

# 4. ML Algorithms Container (large box)
alg_container = FancyBboxPatch((2.5, 2), 5, 1.5, boxstyle="round,pad=0.15", 
                               facecolor=algorithm_color, edgecolor='black', linewidth=2)
ax.add_patch(alg_container)
ax.text(5, 3.2, 'Recommendation Algorithms', fontsize=12, ha='center', 
        va='center', fontweight='bold')

# Four algorithm boxes inside the container
alg_names = ['Collaborative\nFiltering\n(50% Weight)', 
             'Content-Based\nFiltering\n(30% Weight)', 
             'Association\nRule Mining\n(20% Weight)', 
             'Category-Based\nRecommendations']

for i, (name, color) in enumerate(zip(alg_names, alg_box_colors)):
    x_pos = 3 + i * 1.25
    alg_box = FancyBboxPatch((x_pos-0.4, 2.3), 0.8, 0.9, boxstyle="round,pad=0.05", 
                            facecolor=color, edgecolor='black', linewidth=1.2)
    ax.add_patch(alg_box)
    ax.text(x_pos, 2.75, name, fontsize=8, ha='center', va='center', 
            fontweight='bold', color='white')

# 5. Arrow from Algorithms to Model
arrow4 = FancyArrowPatch((5, 2), (5, 1.2), 
                         arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow4)
ax.text(5.3, 1.6, 'Learn Patterns', fontsize=10, ha='left', style='italic')

# 6. Model box
model_box = FancyBboxPatch((4, 0.5), 2, 0.7, boxstyle="round,pad=0.1", 
                          facecolor=model_color, edgecolor='black', linewidth=1.5)
ax.add_patch(model_box)
ax.text(5, 0.85, 'Recommendation\nEngine', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white')

# 7. Arrow from Model to Final Recommendations
arrow5 = FancyArrowPatch((5, 0.5), (5, -0.2), 
                         arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow5)
ax.text(5.3, 0.15, 'Generate Scores', fontsize=10, ha='left', style='italic')

# 8. Final Recommendations box
final_box = FancyBboxPatch((4, -1), 2, 0.7, boxstyle="round,pad=0.1", 
                          facecolor=final_color, edgecolor='black', linewidth=1.5)
ax.add_patch(final_box)
ax.text(5, -0.65, 'Final\nRecommendations', fontsize=11, ha='center', va='center', 
        fontweight='bold', color='white')

# Adjust y-axis to show final box
ax.set_ylim(-1.5, 10)

# Save the figure
plt.tight_layout()
plt.savefig('ShopSphere_Recommendation_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Flowchart saved as 'ShopSphere_Recommendation_Flowchart.png'")
plt.close()


