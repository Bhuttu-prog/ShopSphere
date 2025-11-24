#!/usr/bin/env python3
"""
Generate a pictorial flowchart for ShopSphere Recommendation System
Style similar to ML pipeline flowchart
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as patches

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(16, 11))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Define colors
cloud_color = '#4A90E2'  # Blue for data source (similar to Hospital Data)
box_color = '#E8F4F8'   # Light blue/gray for data boxes
algorithm_color = '#FFD93D'  # Yellow for algorithm container
alg_box_colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181']  # Colors for individual algorithms
model_color = '#6C5CE7'  # Purple for model
final_color = '#00B894'  # Green for final output

# Title
ax.text(5, 9.7, 'System Architecture', fontsize=22, fontweight='bold', 
        ha='center', va='center', family='sans-serif')

# 1. Starting Point - Cloud shape for "ShopSphere E-commerce Data" (similar to Hospital Data)
cloud = mpatches.Ellipse((1.5, 8), 2.2, 1.4, color=cloud_color, alpha=0.9, 
                         edgecolor='darkblue', linewidth=2)
ax.add_patch(cloud)
ax.text(1.5, 8, 'ShopSphere\nE-commerce Data', fontsize=13, fontweight='bold',
        ha='center', va='center', color='white', family='sans-serif')

# 2. Data Division - Arrow labeled "Data Sources"
arrow1 = FancyArrowPatch((3.6, 8), (4.3, 8), 
                         arrowstyle='->', lw=2.5, color='black', 
                         connectionstyle="arc3,rad=0")
ax.add_patch(arrow1)
ax.text(3.95, 8.3, 'Data Sources', fontsize=11, ha='center', 
        style='italic', fontweight='bold', family='sans-serif')

# Split point - Diamond shape
split_x, split_y = 4.8, 8
diamond = mpatches.RegularPolygon((split_x, split_y), 4, radius=0.5, 
                                  orientation=0.785, facecolor=box_color, 
                                  edgecolor='black', linewidth=2)
ax.add_patch(diamond)
ax.text(split_x, split_y, 'Data\nProcessing', fontsize=10, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Three paths from split
# Path 1: Order History (Training Data) - Left path
arrow2a = FancyArrowPatch((split_x-0.35, split_y-0.35), (2.5, 6.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=0.1")
ax.add_patch(arrow2a)

box1 = FancyBboxPatch((1.5, 5.5), 2, 1.2, boxstyle="round,pad=0.15", 
                      facecolor=box_color, edgecolor='black', linewidth=2)
ax.add_patch(box1)
ax.text(2.5, 6.1, 'Order History\nTraining Data', fontsize=11, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Path 2: Product Catalog - Middle path
arrow2b = FancyArrowPatch((split_x, split_y-0.5), (4.5, 6.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=0")
ax.add_patch(arrow2b)

box2 = FancyBboxPatch((3.5, 5.5), 2, 1.2, boxstyle="round,pad=0.15", 
                      facecolor=box_color, edgecolor='black', linewidth=2)
ax.add_patch(box2)
ax.text(4.5, 6.1, 'Product Catalog\nFeatures & Associations', fontsize=11, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Path 3: User Behavior - Right path
arrow2c = FancyArrowPatch((split_x+0.35, split_y-0.35), (6.5, 6.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=-0.1")
ax.add_patch(arrow2c)

box3 = FancyBboxPatch((5.5, 5.5), 2, 1.2, boxstyle="round,pad=0.15", 
                      facecolor=box_color, edgecolor='black', linewidth=2)
ax.add_patch(box3)
ax.text(6.5, 6.1, 'User Behavior\nCart & Wishlist', fontsize=11, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# 3. Arrows from data boxes to Algorithms container
arrow3a = FancyArrowPatch((2.5, 5.5), (3, 4.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=0")
ax.add_patch(arrow3a)

arrow3b = FancyArrowPatch((4.5, 5.5), (4.5, 4.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=0")
ax.add_patch(arrow3b)

arrow3c = FancyArrowPatch((6.5, 5.5), (6, 4.2), 
                          arrowstyle='->', lw=2, color='black',
                          connectionstyle="arc3,rad=0")
ax.add_patch(arrow3c)

# 4. ML Algorithms Container (large box) - similar to ML Algorithms box
alg_container = FancyBboxPatch((2, 3), 6, 1.5, boxstyle="round,pad=0.2", 
                               facecolor=algorithm_color, edgecolor='black', linewidth=2.5)
ax.add_patch(alg_container)
ax.text(5, 4.2, 'Recommendation Algorithms', fontsize=14, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Four algorithm boxes inside the container (similar to Naïve Bayes, Random Forest, etc.)
alg_names = ['Collaborative\nFiltering\n(50% Weight)', 
             'Content-Based\nFiltering\n(30% Weight)', 
             'Association\nRule Mining\n(20% Weight)', 
             'Category-Based\nRecommendations']

for i, (name, color) in enumerate(zip(alg_names, alg_box_colors)):
    x_pos = 2.8 + i * 1.4
    alg_box = FancyBboxPatch((x_pos-0.5, 3.3), 1, 0.9, boxstyle="round,pad=0.08", 
                            facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(alg_box)
    ax.text(x_pos, 3.75, name, fontsize=9, ha='center', va='center', 
            fontweight='bold', color='white', family='sans-serif')

# 5. Arrow from Algorithms to Model - labeled "Learn Patterns"
arrow4 = FancyArrowPatch((5, 3), (5, 2.2), 
                         arrowstyle='->', lw=2.5, color='black',
                         connectionstyle="arc3,rad=0")
ax.add_patch(arrow4)
ax.text(5.4, 2.6, 'Learn Patterns', fontsize=11, ha='left', 
        style='italic', fontweight='bold', family='sans-serif')

# 6. Model box (similar to "Model" box in reference)
model_box = FancyBboxPatch((4, 1.2), 2, 1, boxstyle="round,pad=0.15", 
                          facecolor=model_color, edgecolor='black', linewidth=2)
ax.add_patch(model_box)
ax.text(5, 1.7, 'Recommendation\nEngine', fontsize=12, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# 7. Arrow from Model to Final - labeled "Generate Scores"
arrow5 = FancyArrowPatch((5, 1.2), (5, 0.3), 
                         arrowstyle='->', lw=2.5, color='black',
                         connectionstyle="arc3,rad=0")
ax.add_patch(arrow5)
ax.text(5.4, 0.75, 'Generate Scores', fontsize=11, ha='left', 
        style='italic', fontweight='bold', family='sans-serif')

# 8. Final Recommendations box
final_box = FancyBboxPatch((4, -0.3), 2, 0.6, boxstyle="round,pad=0.1", 
                          facecolor=final_color, edgecolor='black', linewidth=2)
ax.add_patch(final_box)
ax.text(5, 0, 'Final\nRecommendations', fontsize=12, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Adjust y-axis to show final box
ax.set_ylim(-0.8, 10)

# Save the figure
plt.tight_layout()
plt.savefig('ShopSphere_Recommendation_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)
print("✓ Flowchart image saved as 'ShopSphere_Recommendation_Flowchart.png'")
print("  File size: High resolution (300 DPI) for clear printing and presentation")
plt.close()


