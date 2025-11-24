#!/usr/bin/env python3
"""
Generate a comprehensive pictorial flowchart for ShopSphere Application Flow
Shows complete system architecture and data flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as patches

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(18, 12))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Define colors
user_color = '#4A90E2'  # Blue for user
frontend_color = '#61DAFB'  # React blue
backend_color = '#6DB33F'  # Spring green
auth_color = '#FF6B6B'  # Red for security
db_color = '#00758F'  # MySQL blue
cache_color = '#DC382D'  # Redis red
docker_color = '#0DB7ED'  # Docker blue

# Title
ax.text(6, 9.5, 'ShopSphere Application Architecture Flow', fontsize=20, fontweight='bold', 
        ha='center', va='center', family='sans-serif')

# ========== LEFT SIDE: CLIENT LAYER ==========
# User
user_circle = mpatches.Circle((1.5, 7.5), 0.6, color=user_color, alpha=0.9, 
                               edgecolor='darkblue', linewidth=2)
ax.add_patch(user_circle)
ax.text(1.5, 7.5, '👤\nUser', fontsize=10, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Browser
arrow1 = FancyArrowPatch((2.1, 7.5), (3.2, 7.5), 
                         arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow1)

browser_box = FancyBboxPatch((3.5, 6.8), 2, 1.4, boxstyle="round,pad=0.15", 
                             facecolor=frontend_color, edgecolor='black', linewidth=2)
ax.add_patch(browser_box)
ax.text(4.5, 7.5, '🌐 Web Browser\nChrome/Firefox/Safari', fontsize=10, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# ========== MIDDLE: FRONTEND APPLICATION ==========
arrow2 = FancyArrowPatch((5.5, 7.5), (6.2, 7.5), 
                         arrowstyle='->', lw=2, color='black')
ax.add_patch(arrow2)
ax.text(5.85, 7.8, 'HTTP/HTTPS', fontsize=9, ha='center', style='italic')

# React Frontend Container
frontend_container = FancyBboxPatch((6.5, 5.5), 2.5, 2.5, boxstyle="round,pad=0.2", 
                                    facecolor=frontend_color, edgecolor='black', linewidth=2.5, alpha=0.3)
ax.add_patch(frontend_container)
ax.text(7.75, 8.2, 'Frontend Application', fontsize=12, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# React
react_box = FancyBboxPatch((6.8, 7.2), 1.9, 0.6, boxstyle="round,pad=0.1", 
                          facecolor=frontend_color, edgecolor='black', linewidth=1.5)
ax.add_patch(react_box)
ax.text(7.75, 7.5, '⚛️ React 19 + TypeScript', fontsize=9, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Redux
redux_box = FancyBboxPatch((6.8, 6.5), 0.85, 0.5, boxstyle="round,pad=0.08", 
                          facecolor='#764ABC', edgecolor='black', linewidth=1.2)
ax.add_patch(redux_box)
ax.text(7.225, 6.75, '📦 Redux', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Router
router_box = FancyBboxPatch((7.85, 6.5), 0.85, 0.5, boxstyle="round,pad=0.08", 
                            facecolor='#CA4245', edgecolor='black', linewidth=1.2)
ax.add_patch(router_box)
ax.text(8.275, 6.75, '🛣️ Router', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Tailwind CSS
ui_box = FancyBboxPatch((6.8, 5.8), 1.9, 0.5, boxstyle="round,pad=0.08", 
                       facecolor='#38BDF8', edgecolor='black', linewidth=1.2)
ax.add_patch(ui_box)
ax.text(7.75, 6.05, '🎨 Tailwind CSS', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# ========== RIGHT SIDE: BACKEND SERVICES ==========
arrow3 = FancyArrowPatch((9, 7.5), (9.7, 7.5), 
                         arrowstyle='->', lw=2.5, color='black')
ax.add_patch(arrow3)
ax.text(9.35, 7.8, 'REST API', fontsize=9, ha='center', style='italic', fontweight='bold')

# Spring Boot Backend Container
backend_container = FancyBboxPatch((10, 4), 2.5, 4, boxstyle="round,pad=0.2", 
                                  facecolor=backend_color, edgecolor='black', linewidth=2.5, alpha=0.3)
ax.add_patch(backend_container)
ax.text(11.25, 8.2, 'Backend Services', fontsize=12, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Spring Boot
spring_box = FancyBboxPatch((10.3, 7.2), 1.9, 0.6, boxstyle="round,pad=0.1", 
                           facecolor=backend_color, edgecolor='black', linewidth=1.5)
ax.add_patch(spring_box)
ax.text(11.25, 7.5, '☕ Spring Boot 3.2.0', fontsize=9, ha='center', 
        va='center', fontweight='bold', color='white', family='sans-serif')

# Spring Security
security_box = FancyBboxPatch((10.3, 6.5), 0.85, 0.5, boxstyle="round,pad=0.08", 
                             facecolor=auth_color, edgecolor='black', linewidth=1.2)
ax.add_patch(security_box)
ax.text(10.725, 6.75, '🔒 Security', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Controllers
controller_box = FancyBboxPatch((11.25, 6.5), 0.85, 0.5, boxstyle="round,pad=0.08", 
                               facecolor='#FFA500', edgecolor='black', linewidth=1.2)
ax.add_patch(controller_box)
ax.text(11.675, 6.75, '🎮 API', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# Services
service_box = FancyBboxPatch((10.3, 5.8), 1.9, 0.5, boxstyle="round,pad=0.08", 
                            facecolor='#4A90E2', edgecolor='black', linewidth=1.2)
ax.add_patch(service_box)
ax.text(11.25, 6.05, '⚙️ Business Logic', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# JPA
jpa_box = FancyBboxPatch((10.3, 5.1), 1.9, 0.5, boxstyle="round,pad=0.08", 
                         facecolor='#6C5CE7', edgecolor='black', linewidth=1.2)
ax.add_patch(jpa_box)
ax.text(11.25, 5.35, '💾 Spring Data JPA', fontsize=8, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# ========== AUTHENTICATION SERVICE ==========
arrow_auth = FancyArrowPatch((10.3, 6.5), (9.2, 5.5), 
                             arrowstyle='->', lw=2, color='red', linestyle='--')
ax.add_patch(arrow_auth)
ax.text(9.5, 5.9, 'OAuth/OIDC', fontsize=8, ha='center', style='italic', color='red')

keycloak_box = FancyBboxPatch((8, 4.8), 1.5, 1, boxstyle="round,pad=0.1", 
                             facecolor=auth_color, edgecolor='black', linewidth=2)
ax.add_patch(keycloak_box)
ax.text(8.75, 5.3, '🔐 Keycloak\nPort: 8081', fontsize=9, ha='center', va='center', 
        fontweight='bold', color='white', family='sans-serif')

# ========== DATA LAYER ==========
# MySQL Database
arrow_db = FancyArrowPatch((11.25, 5.1), (11.25, 3.5), 
                           arrowstyle='->', lw=2.5, color='black')
ax.add_patch(arrow_db)
ax.text(11.6, 4.3, 'Read/Write', fontsize=9, ha='left', style='italic')

mysql_box = FancyBboxPatch((10, 2.2), 2.5, 1.2, boxstyle="round,pad=0.15", 
                          facecolor=db_color, edgecolor='black', linewidth=2)
ax.add_patch(mysql_box)
ax.text(11.25, 2.8, '🗄️ MySQL 8.0\nPort: 3307\nPersistent Storage', fontsize=10, ha='center', 
        va='center', fontweight='bold', color='white', family='sans-serif')

# Redis Cache
arrow_cache = FancyArrowPatch((10.3, 5.8), (8.5, 3.5), 
                             arrowstyle='->', lw=2, color='red', linestyle='--')
ax.add_patch(arrow_cache)
ax.text(9.2, 4.5, 'Cache', fontsize=9, ha='center', style='italic', color='red')

redis_box = FancyBboxPatch((7, 2.2), 1.5, 1.2, boxstyle="round,pad=0.15", 
                          facecolor=cache_color, edgecolor='black', linewidth=2)
ax.add_patch(redis_box)
ax.text(7.75, 2.8, '⚡ Redis 7\nPort: 6379\nCache & Sessions', fontsize=10, ha='center', 
        va='center', fontweight='bold', color='white', family='sans-serif')

# ========== DOCKER INFRASTRUCTURE ==========
docker_box = FancyBboxPatch((1, 0.5), 10, 1, boxstyle="round,pad=0.15", 
                            facecolor=docker_color, edgecolor='black', linewidth=2, alpha=0.2)
ax.add_patch(docker_box)
ax.text(6, 1, '🐳 Docker Compose - Container Orchestration', fontsize=11, ha='center', 
        va='center', fontweight='bold', family='sans-serif')

# Docker arrows (dotted lines connecting to services)
docker_arrow1 = FancyArrowPatch((2, 1.5), (4.5, 7.2), 
                                arrowstyle='->', lw=1.5, color=docker_color, 
                                linestyle=':', alpha=0.6)
ax.add_patch(docker_arrow1)

docker_arrow2 = FancyArrowPatch((4, 1.5), (11.25, 7.2), 
                                arrowstyle='->', lw=1.5, color=docker_color, 
                                linestyle=':', alpha=0.6)
ax.add_patch(docker_arrow2)

docker_arrow3 = FancyArrowPatch((6, 1.5), (11.25, 2.8), 
                                arrowstyle='->', lw=1.5, color=docker_color, 
                                linestyle=':', alpha=0.6)
ax.add_patch(docker_arrow3)

docker_arrow4 = FancyArrowPatch((8, 1.5), (7.75, 2.8), 
                                arrowstyle='->', lw=1.5, color=docker_color, 
                                linestyle=':', alpha=0.6)
ax.add_patch(docker_arrow4)

docker_arrow5 = FancyArrowPatch((10, 1.5), (8.75, 5.3), 
                                arrowstyle='->', lw=1.5, color=docker_color, 
                                linestyle=':', alpha=0.6)
ax.add_patch(docker_arrow5)

# ========== DATA FLOW LABELS ==========
# Add flow descriptions
ax.text(1.5, 6.5, 'User\nInteraction', fontsize=9, ha='center', 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7), 
        family='sans-serif')

ax.text(7.75, 4.8, 'State\nManagement', fontsize=9, ha='center', 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7), 
        family='sans-serif')

ax.text(11.25, 3.8, 'Data\nPersistence', fontsize=9, ha='center', 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7), 
        family='sans-serif')

# Adjust y-axis
ax.set_ylim(0, 10)

# Save the figure
plt.tight_layout()
plt.savefig('ShopSphere_Application_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.2)
print("✓ Complete Application Flowchart saved as 'ShopSphere_Application_Flowchart.png'")
print("  Shows: User → Frontend → Backend → Database/Cache → Docker Infrastructure")
print("  File size: High resolution (300 DPI) for clear printing and presentation")
plt.close()


