# Models

This page describes all the texture additions in the resource pack. Use the below IDs inside your block's material instance.

```json
{
    "minecraft:geometry": "geometry.template_cake_with_candle", // The model refrance

    "minecraft:material_instances": { // Textures to display
        "*": {"texture": "minecraft:cake_bottom"}, // `*` is needed for the block particle
        "side": {"texture": "minecraft:cake_side"},
        "top": {"texture": "minecraft:cake_top"},
        "bottom": {"texture": "minecraft:cake_bottom"},
        "candle": {"texture": "minecraft:candle"}
    }
}
```

## Definitions

### TIP

> Press `Control + f` to search this document

### Blocks

The below table lists all the models that are included in this version of Assets Plus

- `Name` The name of the model used in a block's geometry.
- `Material Instances` If the model has any special material instances it will be defined here. If none is defined you can use the default instances (north, south, east, west, up, down, *)
- `Bones` A list of all bone names. All models should have the `bb_main` bone. Bones with other names typically will be used in the block. (For making certain parts invisible)
- `Path` The location of the model file

| Name | Material Instances | Bones | Path |
|--|--|--|--|
| `geometry.template_anvil` | `top` | `bb_main` | `models/blocks/template_anvil` |
| `geometry.template_azalea` | `top`<br> `side`<br> `plant` | `bone` | `models/blocks/template_azalea` |
| `geometry.template_bamboo4_age1` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo4_age0` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo1_age0` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo2_age0` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo1_age1` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo3_age1` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo3_age0` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo2_age1` |  | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_beacon` | `glass`<br> `obsidian`<br> `beacon` | `bb_main` | `models/blocks/template_beacon` |
| `geometry.template_cake.slice0` | `side`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice1` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice2` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice3` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice4` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice5` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice6` | `side`<br> `inside`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake_with_candle` | `side`<br> `top`<br> `bottom`<br> `candle` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_campfire` | `log`<br> `lit_log`<br> `fire` | `bb_main` | `models/blocks/template_campfire` |
| `geometry.template_candle` |  | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_two_candles` |  | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_three_candles` |  | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_four_candles` |  | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_cauldron` | `side`<br> `top`<br> `inner`<br> `bottom` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_level2` | `content`<br> `side`<br> `top`<br> `inner`<br> `bottom` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_level1` | `content`<br> `side`<br> `top`<br> `inner`<br> `bottom` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_full` | `content`<br> `side`<br> `top`<br> `inner`<br> `bottom` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_chorus_flower` | `texture` | `bb_main` | `models/blocks/template_chorus_flower` |
| `geometry.template_crop` |  | `bb_main` | `models/blocks/template_crop` |
| `geometry.template_cross` |  | `bb_main` | `models/blocks/template_cross` |
| `geometry.template_daylight_detector` |  | `bb_main` | `models/blocks/template_daylight_detector` |
| `geometry.template_door_top_right` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_bottom_left_open` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_bottom_left` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_top_right_open` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_bottom_right` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_bottom_right_open` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_top_left` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_top_left_open` |  | `bb_main` | `models/blocks/template_door` |
| `geometry.template_farmland` | `top` | `bb_main` | `models/blocks/template_farmland` |
| `geometry.template_fence` |  | `bb_main`<br> `post`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_fence` |
| `geometry.template_fence_gate` |  | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.open` |  | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.wall` |  | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.wall_open` |  | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fire_floor` |  | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_fire_side` |  | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_fire_up` |  | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_flower_pot` | `flower_pot`<br> `dirt` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_flower_pot_cross` | `flower_pot`<br> `dirt`<br> `flower` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_tinted_flower_pot_cross` | `flower_pot`<br> `dirt`<br> `flower` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_potted_azalea_bush` | `flower_pot`<br> `dirt`<br> `bush_top`<br> `bush_side`<br> `bush_plant` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_glass_pane_side` | `edge` | `bb_main`<br> `post`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_glass_pane` |
| `geometry.template_height0` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height1` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height2` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height3` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height4` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height5` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height6` |  | `bb_main` | `models/blocks/template_height` |
| `geometry.template_item_frame` | `frame`<br> `wood` | `bb_main` | `models/blocks/template_item_frame` |
| `geometry.template_item_frame_map` | `frame`<br> `wood` | `bb_main` | `models/blocks/template_item_frame` |
| `geometry.template_lantern` |  | `bb_main` | `models/blocks/template_lantern` |
| `geometry.template_hanging_lantern` |  | `bb_main` | `models/blocks/template_lantern` |
| `geometry.template_orientable_trapdoor_bottom` |  | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_orientable_trapdoor_open` |  | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_orientable_trapdoor_top` |  | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_pressure_plate.powered` |  | `bb_main` | `models/blocks/template_pressure_plate` |
| `geometry.template_pressure_plate` |  | `bb_main` | `models/blocks/template_pressure_plate` |
| `geometry.template_rail_flat` |  | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_rail_raised_sw` |  | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_rail_raised_ne` |  | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_sculk_shrieker` | `side`<br> `top`<br> `bottom` | `bb_main` | `models/blocks/template_sculk_shrieker` |
| `geometry.template_single_face` |  | `bb_main` | `models/blocks/template_single_face` |
| `geometry.template_slab.bottom` |  | `bb_main` | `models/blocks/template_slab` |
| `geometry.template_slab.top` |  | `bb_main` | `models/blocks/template_slab` |
| `geometry.template_stairs` |  | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.inner` |  | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.outer` |  | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_torch` |  | `bb_main` | `models/blocks/template_torch` |
| `geometry.template_torch_wall` |  | `bb_main` | `models/blocks/template_torch` |
| `geometry.template_trapdoor_top` |  | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_trapdoor_bottom` |  | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_trapdoor_open` |  | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_turtle_egg` |  | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_four_turtle_eggs` |  | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_three_turtle_eggs` |  | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_two_turtle_eggs` |  | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_wall_post` |  | `bb_main`<br> `post`<br> `north_tall`<br> `east_tall`<br> `south_tall`<br> `west_tall`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_wall` |

