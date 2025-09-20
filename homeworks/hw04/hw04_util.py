import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
from itertools import combinations

import re

def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple (0-255)."""
    hex_color = hex_color.strip()
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB tuple (0-255) to hex color string."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def color_to_rgb(color):
    """Convert a color name or hex to rgb tuple."""
    # Plotly named colors
    plotly_named = {
        'orange': (255, 165, 0),
        'gold': (255, 215, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 128, 0),
        'purple': (128, 0, 128),
        'yellow': (255, 255, 0),
        'pink': (255, 192, 203),
        'brown': (165, 42, 42),
        'gray': (128, 128, 128),
        'grey': (128, 128, 128),
        # Add more as needed
    }
    if isinstance(color, tuple) and len(color) == 3:
        return color
    if color.startswith('#'):
        return hex_to_rgb(color)
    if color in plotly_named:
        return plotly_named[color]
    # Try to parse rgb(r,g,b)
    m = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color)
    if m:
        return tuple(int(m.group(i)) for i in range(1, 4))
    # Fallback: white
    return (255, 255, 255)

def mix_colors(color1, color2, alpha=0.5):
    """Mix two colors (hex or named) in RGB space."""
    rgb1 = color_to_rgb(color1)
    rgb2 = color_to_rgb(color2)
    mixed = tuple(int(round(alpha * c1 + (1 - alpha) * c2)) for c1, c2 in zip(rgb1, rgb2))
    return rgb_to_hex(mixed)

def draw_equations(equations, plotting_range=None):
    """
    Draw equations in 2D or 3D space with intersection highlighting.

    Parameters:
    n (int): Either 2 or 3, determines 2D or 3D plotting
    equations (list): 
        - For n=3: list of planes [a, b, c, d] representing ax + by + cz + d = 0.
        - For n=2: list of lines [a, b, c] representing ax + by + c = 0.
    """
    n = len(equations[0]) - 1
    if n == 3:
        # 3D case - planes
        fig = go.Figure()

        # Define a color palette (extend as needed)
        base_colors = ['#3d81f6', 'orange', '#d81b60', '#43a047', '#8e24aa', '#00838f', '#fbc02d', '#e64a19', '#6d4c41', '#c62828']
        colors = base_colors * ((len(equations) // len(base_colors)) + 1)

        # --- Dynamically determine plotting_range to include all intersection points ---
        A = np.array([[eq[0], eq[1], eq[2]] for eq in equations])
        b_vec = np.array([-eq[3] for eq in equations])
        intersection = None
        triple_point_exists = False
        try:
            intersection, residuals, rank, s = np.linalg.lstsq(A, b_vec, rcond=None)
            if np.allclose(np.dot(A, intersection) - b_vec, 0) and len(equations) >= 3:
                triple_point_exists = True
        except np.linalg.LinAlgError:
            pass

        # If plotting_range not given, calculate it to include all intersection points
        if plotting_range is None:
            max_coord = 0
            
            # Check triple intersection point if it exists
            if triple_point_exists:
                max_coord = max(max_coord, np.max(np.abs(intersection)))
            
            # Check all pairwise intersection points
            for pair in combinations(range(len(equations)), 2):
                i, j = pair
                eq1 = equations[i]
                eq2 = equations[j]
                
                # Cross product of normal vectors gives direction
                normal1 = np.array([eq1[0], eq1[1], eq1[2]])
                normal2 = np.array([eq2[0], eq2[1], eq2[2]])
                direction = np.cross(normal1, normal2)
                
                if np.linalg.norm(direction) > 1e-10:  # Not parallel
                    try:
                        # Find a point on the line by setting one coordinate to 0
                        A_2d = np.array([[eq1[0], eq1[1]], [eq2[0], eq2[1]]])
                        b_2d = np.array([-eq1[3], -eq2[3]])
                        point = np.zeros(3)
                        
                        if abs(np.linalg.det(A_2d)) > 1e-10:
                            point[:2] = np.linalg.solve(A_2d, b_2d)
                        else: # Try another combination of coordinates
                            A_2d = np.array([[eq1[0], eq1[2]], [eq2[0], eq2[2]]])
                            b_2d = np.array([-eq1[3], -eq2[3]])
                            if abs(np.linalg.det(A_2d)) > 1e-10:
                                point[0] = np.linalg.solve(A_2d, b_2d)[0]
                                point[2] = np.linalg.solve(A_2d, b_2d)[1]
                            else:
                                A_2d = np.array([[eq1[1], eq1[2]], [eq2[1], eq2[2]]])
                                b_2d = np.array([-eq1[3], -eq2[3]])
                                if abs(np.linalg.det(A_2d)) > 1e-10:
                                    point[1] = np.linalg.solve(A_2d, b_2d)[0]
                                    point[2] = np.linalg.solve(A_2d, b_2d)[1]
                                else:
                                    continue # Planes are parallel or coincident
                        
                        # Sample points along the intersection line to find max coordinate
                        t_values = np.linspace(-50, 50, 100)  # Sample a wide range
                        line_points = point[:, np.newaxis] + direction[:, np.newaxis] * t_values
                        max_coord = max(max_coord, np.max(np.abs(line_points)))
                        
                    except Exception:
                        pass # Silently ignore non-intersecting or parallel planes
            
            # Set plotting range with margin
            plotting_range = max(5, np.ceil(max_coord) + 3)
        else:
            # If plotting_range is given, still check if any intersection points are outside and warn
            if triple_point_exists and np.any(np.abs(intersection) > plotting_range):
                print("Warning: The intersection point is outside the plotting range.")

        # Create grid for plane visualization
        x_range = np.linspace(-plotting_range, plotting_range, 100)
        y_range = np.linspace(-plotting_range, plotting_range, 100)
        X, Y = np.meshgrid(x_range, y_range)

        # Plot each plane with proper equation labels
        for i, (a, b, c, d) in enumerate(equations):
            # Format equation label
            terms = []
            if a != 0:
                if a == 1:
                    terms.append("x")
                elif a == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{a}x")
            
            if b != 0:
                if b == 1:
                    terms.append("+ y" if terms else "y")
                elif b == -1:
                    terms.append("- y")
                else:
                    if b > 0 and terms:
                        terms.append(f"+ {b}y")
                    else:
                        terms.append(f"{b}y")
            
            if c != 0:
                if c == 1:
                    terms.append("+ z" if terms else "z")
                elif c == -1:
                    terms.append("- z")
                else:
                    if c > 0 and terms:
                        terms.append(f"+ {c}z")
                    else:
                        terms.append(f"{c}z")

            if d != 0:
                if d == 1:
                    terms.append("+ 1")
                elif d == -1:
                    terms.append("- 1")
                else:
                    if d > 0 and terms:
                        terms.append(f"+ {d}")
                    else:
                        terms.append(f"{d}")

            
            equation_str = " ".join(terms) + " = 0"
            
            # Only plot if at least one of a, b, c is nonzero
            if c != 0:
                Z = (-d - a*X - b*Y) / c
                fig.add_trace(go.Surface(
                    x=X, y=Y, z=Z,
                    colorscale=[[0, colors[i]], [1, colors[i]]],
                    opacity=0.6,
                    showscale=False,
                    name=f'Equation {i+1}: {equation_str}',
                    showlegend=True
                ))
            elif b != 0:
                # Plane is vertical in z, so solve for y
                # Create a proper meshgrid for the vertical plane
                x_vals = np.linspace(-plotting_range, plotting_range, 100)
                z_vals = np.linspace(-plotting_range, plotting_range, 100)
                X_plane, Z_plane = np.meshgrid(x_vals, z_vals)
                Y_plane = (-d - a*X_plane) / b
                fig.add_trace(go.Surface(
                    x=X_plane, y=Y_plane, z=Z_plane,
                    colorscale=[[0, colors[i]], [1, colors[i]]],
                    opacity=0.6,
                    showscale=False,
                    name=f'Equation {i+1}: {equation_str}',
                    showlegend=True
                ))
            elif a != 0:
                # Plane is vertical in x, so solve for x
                # Create a proper meshgrid for the vertical plane
                y_vals = np.linspace(-plotting_range, plotting_range, 100)
                z_vals = np.linspace(-plotting_range, plotting_range, 100)
                Y_plane, Z_plane = np.meshgrid(y_vals, z_vals)
                X_plane = (-d - b*Y_plane) / a
                fig.add_trace(go.Surface(
                    x=X_plane, y=Y_plane, z=Z_plane,
                    colorscale=[[0, colors[i]], [1, colors[i]]],
                    opacity=0.6,
                    showscale=False,
                    name=f'Equation {i+1}: {equation_str}',
                    showlegend=True
                ))

        # Add thin f0f0f0 lines along the x, y, and z axes (not in legend, not removable)
        axis_color = '#f0f0f0'
        axis_width = 2
        axis_range = plotting_range
        # X axis: from (-axis_range, 0, 0) to (axis_range, 0, 0)
        fig.add_trace(go.Scatter3d(
            x=[-axis_range, axis_range],
            y=[0, 0],
            z=[0, 0],
            mode='lines',
            line=dict(color=axis_color, width=axis_width),
            showlegend=False,
            hoverinfo='skip'
        ))
        # Y axis: from (0, -axis_range, 0) to (0, axis_range, 0)
        fig.add_trace(go.Scatter3d(
            x=[0, 0],
            y=[-axis_range, axis_range],
            z=[0, 0],
            mode='lines',
            line=dict(color=axis_color, width=axis_width),
            showlegend=False,
            hoverinfo='skip'
        ))
        # Z axis: from (0, 0, -axis_range) to (0, 0, axis_range)
        fig.add_trace(go.Scatter3d(
            x=[0, 0],
            y=[0, 0],
            z=[-axis_range, axis_range],
            mode='lines',
            line=dict(color=axis_color, width=axis_width),
            showlegend=False,
            hoverinfo='skip'
        ))

        # Handle intersections
        if len(equations) >= 2:
            # Always show pairwise intersection lines
            for pair in combinations(range(len(equations)), 2):
                i, j = pair
                eq1 = equations[i]
                eq2 = equations[j]
                
                # Cross product of normal vectors gives direction
                normal1 = np.array([eq1[0], eq1[1], eq1[2]])
                normal2 = np.array([eq2[0], eq2[1], eq2[2]])
                direction = np.cross(normal1, normal2)
                
                if np.linalg.norm(direction) > 1e-10:  # Not parallel
                    try:
                        # Find a point on the line by setting one coordinate to 0
                        A_2d = np.array([[eq1[0], eq1[1]], [eq2[0], eq2[1]]])
                        b_2d = np.array([-eq1[3], -eq2[3]])
                        point = np.zeros(3)
                        
                        if abs(np.linalg.det(A_2d)) > 1e-10:
                            point[:2] = np.linalg.solve(A_2d, b_2d)
                        else: # Try another combination of coordinates
                            A_2d = np.array([[eq1[0], eq1[2]], [eq2[0], eq2[2]]])
                            b_2d = np.array([-eq1[3], -eq2[3]])
                            if abs(np.linalg.det(A_2d)) > 1e-10:
                                point[0] = np.linalg.solve(A_2d, b_2d)[0]
                                point[2] = np.linalg.solve(A_2d, b_2d)[1]
                            else:
                                A_2d = np.array([[eq1[1], eq1[2]], [eq2[1], eq2[2]]])
                                b_2d = np.array([-eq1[3], -eq2[3]])
                                if abs(np.linalg.det(A_2d)) > 1e-10:
                                    point[1] = np.linalg.solve(A_2d, b_2d)[0]
                                    point[2] = np.linalg.solve(A_2d, b_2d)[1]
                                else:
                                    continue # Planes are parallel or coincident
                        
                        # Create line points
                        t_values = np.linspace(-plotting_range, plotting_range, 100)
                        line_points = point[:, np.newaxis] + direction[:, np.newaxis] * t_values

                        # Mix the two plane colors for the intersection line
                        color1 = colors[i]
                        color2 = colors[j]
                        # mixed_color = mix_colors(color1, color2, alpha=0.5)
                        mixed_color = 'black'

                        fig.add_trace(go.Scatter3d(
                            x=line_points[0],
                            y=line_points[1],
                            z=line_points[2],
                            mode='lines',
                            line=dict(color=mixed_color, width=6),
                            name=f'Intersection: Eq{i+1} & Eq{j+1}'
                        ))
                    except Exception as e:
                        # print(f"Intersection error: {e}")
                        pass # Silently ignore non-intersecting or parallel planes

        # Plot the triple intersection point if it exists
        # if triple_point_exists:
        #     fig.add_trace(go.Scatter3d(
        #         x=[intersection[0]],
        #         y=[intersection[1]], 
        #         z=[intersection[2]],
        #         mode='markers',
        #         marker=dict(size=12, color='gold', symbol='circle',
        #                     line=dict(color='gold', width=3)),
        #         name='Intersection Point'
        #     ))

        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y', 
                zaxis_title='Z',
                xaxis=dict(
                    backgroundcolor='white',
                    gridcolor='#f0f0f0',
                    zerolinecolor='#f0f0f0',
                    range=[-plotting_range, plotting_range]
                ),
                yaxis=dict(
                    backgroundcolor='white',
                    gridcolor='#f0f0f0',
                    zerolinecolor='#f0f0f0',
                    range=[-plotting_range, plotting_range]
                ),
                zaxis=dict(
                    backgroundcolor='white',
                    gridcolor='#f0f0f0',
                    zerolinecolor='#f0f0f0',
                    range=[-plotting_range, plotting_range]
                ),
                bgcolor='white',
                aspectmode='cube'
            ),
            scene_camera=dict(
                eye=dict(x=1.5, y=-1.5, z=0.2)
            ),
            font=dict(family='Palatino, serif', size=12),
            height=500,
            width=700,
            showlegend=True
        )
        
    elif n == 2:
        # 2D case - lines
        fig = go.Figure()
        
        # Define colors
        base_colors = ['#3d81f6', 'orange', '#d81b60', '#43a047', '#8e24aa', '#00838f', '#fbc02d', '#e64a19', '#6d4c41', '#c62828']
        colors = base_colors * ((len(equations) // len(base_colors)) + 1)
        
        # Dynamically determine plotting_range to include intersection if it exists
        A = np.array([[eq[0], eq[1]] for eq in equations])
        b_vec = np.array([eq[2] for eq in equations])
        intersection = None
        intersection_exists = False
        try:
            intersection, residuals, rank, s = np.linalg.lstsq(A, b_vec, rcond=None)
            if np.allclose(np.dot(A, intersection) - b_vec, 0) and len(equations) >= 2:
                intersection_exists = True
        except np.linalg.LinAlgError:
            pass

        if plotting_range is None:
            if intersection_exists:
                max_abs = np.max(np.abs(intersection))
                plotting_range = max(5, np.ceil(max_abs) + 3)
            else:
                plotting_range = 25
        else:
            if intersection_exists and np.any(np.abs(intersection) > plotting_range):
                print("Warning: The intersection point is outside the plotting range.")

        # Plot each line with proper equation labels
        x_range = np.linspace(-plotting_range, plotting_range, 100)
        
        for i, (a, b, c) in enumerate(equations):
            # Format equation label
            terms = []
            if a != 0:
                if a == 1:
                    terms.append("x")
                elif a == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{a}x")
            
            if b != 0:
                if b == 1:
                    terms.append("+ y" if terms else "y")
                elif b == -1:
                    terms.append("- y")
                else:
                    if b > 0 and terms:
                        terms.append(f"+ {b}y")
                    else:
                        terms.append(f"{b}y")
            
            equation_str = " ".join(terms) + f" = {c}"
            
            if b != 0:  # Avoid division by zero
                y = (c - a*x_range) / b
                fig.add_trace(go.Scatter(
                    x=x_range, y=y,
                    mode='lines',
                    line=dict(color=colors[i], width=3),
                    opacity=0.6,
                    name=f'Equation {i+1}: {equation_str}'
                ))
            elif a != 0:
                fig.add_trace(go.Scatter(
                    x=np.full_like(x_range, c / a), y=x_range,
                    mode='lines',
                    line=dict(color=colors[i], width=3),
                    opacity=0.6,
                    name=f'Equation {i+1}: {equation_str}'
                ))

        # Plot pairwise intersection points as dashed lines (if more than 2 lines, not just the triple point)
        if len(equations) >= 2:
            for pair in combinations(range(len(equations)), 2):
                i, j = pair
                eq1 = equations[i]
                eq2 = equations[j]
                a1, b1, c1 = eq1
                a2, b2, c2 = eq2
                A_ = np.array([[a1, b1], [a2, b2]])
                b_ = np.array([c1, c2])
                try:
                    if abs(np.linalg.det(A_)) > 1e-10:
                        pt = np.linalg.solve(A_, b_)
                        # Draw a short dashed line segment at the intersection
                        # Pick a direction perpendicular to both lines for the segment
                        # We'll just plot a small cross at the intersection
                        dx = plotting_range * 0.05
                        dy = plotting_range * 0.05
                        color1 = colors[i]
                        color2 = colors[j]
                        mixed_color = mix_colors(color1, color2, alpha=0.5)
                        fig.add_trace(go.Scatter(
                            x=[pt[0] - dx, pt[0] + dx],
                            y=[pt[1] - dy, pt[1] + dy],
                            mode='lines',
                            line=dict(color=mixed_color, width=6, dash='dash'),
                            name=f'Intersection: Eq{i+1} & Eq{j+1}'
                        ))
                    else:
                        continue
                except Exception as e:
                    pass

        # Plot the intersection point for all lines if it exists
        # if intersection_exists:
        #     fig.add_trace(go.Scatter(
        #         x=[intersection[0]],
        #         y=[intersection[1]],
        #         mode='markers',
        #         marker=dict(size=12, color='white', symbol='circle',
        #                     line=dict(color='gold', width=3)),
        #         name='Intersection Point'
        #     ))

        fig.update_layout(
            xaxis_title='X',
            yaxis_title='Y',
            xaxis=dict(
                backgroundcolor='white',
                gridcolor='#f0f0f0',
                zerolinecolor='#f0f0f0',
                range=[-plotting_range, plotting_range]
            ),
            yaxis=dict(
                backgroundcolor='white',
                gridcolor='#f0f0f0',
                zerolinecolor='#f0f0f0',
                range=[-plotting_range, plotting_range]
            ),
            plot_bgcolor='white',
            font=dict(family='Palatino, serif', size=12),
            height=700,
            width=700,
            showlegend=True
        )
    
    else:
        raise ValueError("n must be either 2 or 3")
    
    fig.show()