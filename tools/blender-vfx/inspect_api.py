"""Chỉ dò API Blender tại máy qua dịch vụ; không render."""
import bpy
print('EEVEE', [p.identifier for p in bpy.context.scene.eevee.bl_rna.properties])
g = bpy.data.node_groups.new('probe', 'CompositorNodeTree')
n = g.nodes.new('CompositorNodeGlare')
print('GLARE', [(i.name, str(i.default_value) if hasattr(i, 'default_value') else '') for i in n.inputs])
for kind in ['CompositorNodeSetAlpha', 'CompositorNodePremulKey']:
    n = g.nodes.new(kind)
    print(kind, [(i.name,str(i.default_value) if hasattr(i,'default_value') else '') for i in n.inputs])
