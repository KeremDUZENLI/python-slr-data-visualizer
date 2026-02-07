# COLORS = {
#     "study_focus": {
#         "Reconstruction": "#ff0000",
#         "Restoration": "#008000",
#         "Visualization": "#0000ff",
#     },
#     "historical_site_type": {
#         "Archaeological Site": "#ff0000",
#         "Artistic Feature": "#008000",
#         "Building": "#0000ff",
#         "Natural Space": "#800000",
#     },
#     "historical_site_type_sub": {
#         "LandBased": "#ff000050",
#         "Underwater": "#ff000050",
#         "ArchitecturalAsset": "#00800050",
#         "Artifact": "#00800050",
#         "Fortification": "#0000ff50",
#         "Religious": "#0000ff50",
#         "UrbanSpace": "#0000ff50",
#         "Cave": "#80000050",
#     },
#     "platform": {
#         "VR": "#ff0000",
#         "AR": "#008000",
#         "MR": "#0000ff",
#         "XR": "#800000",
#     },
#     "device": {
#         "HMD": "#ff0000",
#         "Immersive Display": "#008000",
#         "Mobile": "#0000ff",
#         "PC": "#800000",
#     },
#     "technique": {
#         "3D Scanning": "#ff0000",
#         "Data Processing": "#008000",
#         "Geospatial Techniques": "#0000ff",
#         "Image-Based Techniques": "#800000",
#         "Modeling & Reconstruction": "#000080",
#     },
#     "technique_sub": {
#         "Laser Scanning": "#ff000050",
#         "RGB-D Imaging": "#ff000050",
#         "Real-Time Volumetric Capture": "#ff000050",
#         "3D Texturing": "#00800050",
#         "HDR Imaging": "#00800050",
#         "Range-Based Modeling (RBM)": "#00800050",
#         "Semantic Data Extraction": "#00800050",
#         "Texture Mapping": "#00800050",
#         "Beacon Localization": "#0000ff50",
#         "Digital Elevation Models (DEM)": "#0000ff50",
#         "Geographic Information System (GIS)": "#0000ff50",
#         "Global Navigation Satellite System (GNSS)": "#0000ff50",
#         "Visual-Inertial SLAM": "#0000ff50",
#         "Image-Based Modelling (IBM)": "#80000050",
#         "Multi-View Stereo (MVS)": "#80000050",
#         "Photogrammetry": "#80000050",
#         "Spherical Imaging": "#80000050",
#         "Structure from Motion (SfM)": "#80000050",
#         "UAV Aerial Imaging": "#80000050",
#         "3D Modeling": "#00008050",
#         "BIM (Building Information Modeling)": "#00008050",
#         "HBIM (Historical Building Information Modeling)": "#00008050",
#         "Stratigraphic Mapping": "#00008050",
#         "Virtual Anastylosis": "#00008050",
#     },
#     "software_category": {
#         "software_data": "#ff0000",
#         "software_modeling": "#008000",
#         "software_render": "#0000ff",
#     },
#     "software": {
#         "Agisoft Metashape": "#ff000025",
#         "Autodesk ReCap": "#ff000050",
#         "Leica Cyclone": "#ff000075",
#         "Autodesk 3ds Max": "#00800025",
#         "Autodesk Revit": "#00800050",
#         "Blender": "#00800075",
#         "Unity": "#0000ff33",
#         "Unreal Engine": "#0000ff66",
#     },
#     "continent": {
#         "Africa": "#ff0000",
#         "Antarctica": "#000000",
#         "Asia": "#008000",
#         "Europe": "#0000ff",
#         "North America": "#800000",
#         "South America": "#008000",
#         "Oceania": "#000080",
#     },
# }


COLORS = {
    "study_focus": {
        "Reconstruction": "#D32F2F",
        "Restoration": "#388E3C",
        "Visualization": "#1976D2",
    },
    "historical_site_type": {
        "Archaeological Site": "#D32F2F",
        "Artistic Feature": "#388E3C",
        "Building": "#1976D2",
        "Natural Space": "#795548",
    },
    "historical_site_type_sub": {
        # --- Archaeological Site ---
        "LandBased": "#D32F2F99",
        "Underwater": "#D32F2F66",
        # --- Artistic Feature ---
        "ArchitecturalAsset": "#388E3C99",
        "Artifact": "#388E3C66",
        # --- Building ---
        "Fortification": "#1976D2CC",
        "Religious": "#1976D299",
        "UrbanSpace": "#1976D266",
        # --- Natural Space ---
        "Cave": "#79554899",
    },
    "platform": {
        "VR": "#D32F2F95",
        "AR": "#388E3C95",
        "MR": "#1976D295",
        "XR": "#673AB795",
    },
    "device": {
        "HMD": "#C2185B",
        "Immersive Display": "#388E3C",
        "Mobile": "#1976D2",
        "PC": "#455A64",
    },
    "technique": {
        "3D Scanning": "#D32F2F",
        "Data Processing": "#388E3C",
        "Geospatial Techniques": "#1976D2",
        "Image-Based Techniques": "#E6CF00",
        "Modeling & Reconstruction": "#673AB7",
    },
    "technique_sub": {
        # --- 3D Scanning ---
        "Laser Scanning": "#D32F2F99",
        "RGB-D Imaging": "#D32F2F66",
        "Real-Time Volumetric Capture": "#D32F2F33",
        # --- Data Processing ---
        "3D Texturing": "#388E3CCC",
        "HDR Imaging": "#388E3CB3",
        "Range-Based Modeling (RBM)": "#388E3C99",
        "Semantic Data Extraction": "#388E3C80",
        "Texture Mapping": "#388E3C4D",
        # --- Geospatial Techniques ---
        "Geographic Information System (GIS)": "#1976D2CC",
        "Global Navigation Satellite System (GNSS)": "#1976D2B3",
        "Beacon Localization": "#1976D299",
        "Digital Elevation Models (DEM)": "#1976D280",
        "Visual-Inertial SLAM": "#1976D24D",
        # --- Image-Based Techniques ---
        "Photogrammetry": "#E6CF00CC",
        "Structure from Motion (SfM)": "#E6CF00B3",
        "UAV Aerial Imaging": "#E6CF0099",
        "Multi-View Stereo (MVS)": "#E6CF0080",
        "Image-Based Modelling (IBM)": "#E6CF0066",
        "Spherical Imaging": "#E6CF0033",
        # --- Modeling & Reconstruction ---
        "3D Modeling": "#673AB7CC",
        "HBIM (Historical Building Information Modeling)": "#673AB7B3",
        "Virtual Anastylosis": "#673AB780",
        "BIM (Building Information Modeling)": "#673AB766",
        "Stratigraphic Mapping": "#673AB733",
    },
    "software_category": {
        "software_data": "#D32F2F",
        "software_modeling": "#388E3C",
        "software_render": "#1976D2",
    },
    "software": {
        "Agisoft Metashape": "#E57373",
        "Autodesk ReCap": "#FF8A65",
        "Leica Cyclone": "#D32F2F",
        "Autodesk 3ds Max": "#81C784",
        "Autodesk Revit": "#388E3C",
        "Blender": "#1B5E20",
        "Unity": "#64B5F6",
        "Unreal Engine": "#1976D2",
    },
    "continent": {
        "Africa": "#C2185B",
        "Antarctica": "#B0BEC5",
        "Asia": "#388E3C",
        "Europe": "#1976D2",
        "North America": "#D32F2F",
        "South America": "#F57C00",
        "Oceania": "#0097A7",
    },
}


FONTS_PLOT = {
    "title": {
        "size": 14,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "xlabel": {
        "size": 12,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "ylabel": {
        "size": 12,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "xticks": {
        "size": 9,
        "family": "sans-serif",
        "weight": "normal",
        "style": "normal",
        "stretch": "condensed",
    },
    "yticks": {
        "size": 9,
        "family": "sans-serif",
        "weight": "normal",
        "style": "normal",
        "stretch": "condensed",
    },
    "pie_label": {
        "size": 8,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "pie_label_inner": {
        "size": 6,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "pie_label_outer": {
        "size": 6,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "labels_height_numbers": {
        "size": 8,
        "family": "sans-serif",
        "weight": "normal",
        "style": "normal",
        "stretch": "condensed",
    },
    "labels_heatmap_numbers": {
        "size": 10,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "sunburst_label": {
        "size": 16,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
    },
    "sunburst_label_inner": {
        "size": 16,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
    },
    "sunburst_label_outer": {
        "size": 16,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
    },
    "sankey_header": {
        "size": 24,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
    },
    "sankey_label": {
        "size": 16,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
    },
    "labels_extra": {
        "size": 8,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
}


FONTS_LEGEND = {
    "legend_title": {
        "size": 9,
        "family": "sans-serif",
        "weight": "bold",
        "style": "normal",
        "stretch": "condensed",
    },
    "legend_text": {
        "size": 8,
        "family": "sans-serif",
        "weight": "normal",
        "style": "normal",
        "stretch": "condensed",
    },
}


STYLE_PRISMA = {
    "box_main": {
        "id": "box",
        ### font ###
        "fontsize": "14",
        "fontname": "Calibri Bold",
        ### color ###
        "fontcolor": "black",
        "fillcolor": "#CCE5FF",
        ### shape ###
        "shape": "box",
        "style": "rounded,filled",
        ### size ###
        "width": "4.5",
        "height": "0.6",
    },
    "box_excluded": {
        "id": "box",
        ### font ###
        "fontsize": "14",
        "fontname": "Calibri Bold",
        ### color ###
        "fontcolor": "black",
        "fillcolor": "#FFFFFF",
        ### shape ###
        "shape": "box",
        "style": "dashed,filled",
        ### size ###
        "width": "4.5",
        "height": "0.6",
    },
    "note": {
        "id": "note",
        ### font ###
        "fontsize": "12",
        "fontname": "Calibri",
        ### color ###
        "fontcolor": "black",
        "fillcolor": "#FFFFFF",
        ### shape ###
        "shape": "note",
        "style": "filled",
    },
    "edge_flow": {
        "id": "edge",
        ### font ###
        "fontsize": "10",
        "fontname": "Calibri",
        ### color ###
        "fontcolor": "black",
        "color": "black",
        ### style ###
        "arrowhead": "normal",
        "style": "solid",
    },
    "edge_note": {
        "id": "edge",
        ### font ###
        "fontsize": "10",
        "fontname": "Calibri",
        ### color ###
        "fontcolor": "black",
        "color": "black",
        ### style ###
        "arrowhead": "none",
        "style": "dotted",
    },
}
