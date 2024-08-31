from PIL import Image
files = [
    "button.png",
    "button_highlighted.png",
    "crafting_overlay.png",
    "crafting_overlay_disabled.png",
    "crafting_overlay_disabled_highlighted.png",
    "crafting_overlay_highlighted.png",
    "filter_disabled.png",
    "filter_disabled_highlighted.png",
    "filter_enabled.png",
    "filter_enabled_highlighted.png",
    "furnace_filter_disabled.png",
    "furnace_filter_disabled_highlighted.png",
    "furnace_filter_enabled.png",
    "furnace_filter_enabled_highlighted.png",
    "furnace_overlay.png",
    "furnace_overlay_disabled.png",
    "furnace_overlay_disabled_highlighted.png",
    "furnace_overlay_highlighted.png",
    "overlay_recipe.png",
    "overlay_recipe.png.mcmeta",
    "page_backward.png",
    "page_backward_highlighted.png",
    "page_forward.png",
    "page_forward_highlighted.png",
    "slot_craftable.png",
    "slot_many_craftable.png",
    "slot_many_uncraftable.png",
    "slot_uncraftable.png",
    "tab.png",
    "tab_selected.png"
  ]
img = Image.new('RGBA', (1,1),(0,0,0,0))
for file in files:
    img.save(file,"PNG")