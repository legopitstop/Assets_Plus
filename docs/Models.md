# [<](.) Models

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
- `Material Instances` If the model has any special material instances they will be defined here. If none is defined you can use the default instances (north, south, east, west, up, down, *)
- `Bones` A list of all bone names. All models should have the `bb_main` bone. Bones with other names typically will be used in the block. (For making certain parts invisible)
- `Path` The location of the model file

| Name | Material Instances | Bones | Path |
|--|--|--|--|
| `geometry.cube` |  | `bb_main` | `models/blocks/cube` |
| `geometry.template_anvil` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_anvil` |
| `geometry.template_azalea` | `up`<br> `side`<br> `plant` | `bone` | `models/blocks/template_azalea` |
| `geometry.template_bamboo4_age1` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo4_age0` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo1_age0` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo2_age0` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo1_age1` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo3_age1` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo3_age0` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_bamboo2_age1` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_bamboo` |
| `geometry.template_beacon` | `glass`<br> `obsidian`<br> `beacon` | `bb_main` | `models/blocks/template_beacon` |
| `geometry.template_cake.slice0` | `side`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice1` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice2` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice3` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice4` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice5` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake.slice6` | `side`<br> `inside`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_cake_with_candle` | `side`<br> `up`<br> `down`<br> `candle` | `bb_main` | `models/blocks/template_cake` |
| `geometry.template_calibrated_sculk_sensor` | `side`<br> `up`<br> `down`<br> `tendril`<br> `amethyst` | `bb_main` | `models/blocks/template_calibrated_sculk_sensor` |
| `geometry.template_campfire` | `log`<br> `lit_log`<br> `fire` | `bb_main` | `models/blocks/template_campfire` |
| `geometry.template_candle` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_two_candles` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_three_candles` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_four_candles` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_candle` |
| `geometry.template_cauldron` | `side`<br> `up`<br> `inner`<br> `down` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_level2` | `content`<br> `side`<br> `up`<br> `inner`<br> `down` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_level1` | `content`<br> `side`<br> `up`<br> `inner`<br> `down` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_cauldron_full` | `content`<br> `side`<br> `up`<br> `inner`<br> `down` | `bb_main` | `models/blocks/template_cauldron` |
| `geometry.template_chiseled_bookshelf` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main`<br> `slot_up_left`<br> `slot_up_mid`<br> `slot_up_right`<br> `slot_down_left`<br> `slot_down_mid`<br> `slot_down_right` | `models/blocks/template_chiseled_bookshelf` |
| `geometry.template_chorus_flower` | `north`<br> `east`<br> `south`<br> `west`<br> `texture`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_chorus_flower` |
| `geometry.template_crop` | `north`<br> `east` | `bb_main` | `models/blocks/template_crop` |
| `geometry.template_cross` | `north`<br> `east` | `bb_main` | `models/blocks/template_cross` |
| `geometry.template_daylight_detector` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_daylight_detector` |
| `geometry.template_door_up_right` | `north`<br> `east`<br> `south`<br> `west`<br> `up` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_down_left_open` | `north`<br> `east`<br> `south`<br> `west`<br> `down` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_down_left` | `north`<br> `east`<br> `south`<br> `west`<br> `down` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_up_right_open` | `north`<br> `east`<br> `south`<br> `west`<br> `up` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_down_right` | `north`<br> `east`<br> `south`<br> `west`<br> `down` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_down_right_open` | `north`<br> `east`<br> `south`<br> `west`<br> `down` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_up_left` | `north`<br> `east`<br> `south`<br> `west`<br> `up` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_door_up_left_open` | `north`<br> `east`<br> `south`<br> `west`<br> `up` | `bb_main` | `models/blocks/template_door` |
| `geometry.template_farmland` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_farmland` |
| `geometry.template_fence` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main`<br> `post`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_fence` |
| `geometry.template_fence_gate` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.open` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.wall` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fence_gate.wall_open` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_fence_gate` |
| `geometry.template_fire_floor` | `south`<br> `north`<br> `west`<br> `east` | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_fire_side` | `north`<br> `south` | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_fire_up` | `down` | `bb_main` | `models/blocks/template_fire` |
| `geometry.template_flowerbed_1` | `flowerbed`<br> `stem` | `bb_main` | `models/blocks/template_flowerbed` |
| `geometry.template_flowerbed_2` | `flowerbed`<br> `stem` | `bb_main` | `models/blocks/template_flowerbed` |
| `geometry.template_flowerbed_3` | `flowerbed`<br> `stem`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_flowerbed` |
| `geometry.template_flowerbed_4` | `flowerbed`<br> `stem` | `bb_main` | `models/blocks/template_flowerbed` |
| `geometry.template_flower_pot` | `flower_pot`<br> `dirt` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_flower_pot_cross` | `flower_pot`<br> `dirt`<br> `flower` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_tinted_flower_pot_cross` | `flower_pot`<br> `dirt`<br> `flower` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_potted_azalea_bush` | `flower_pot`<br> `dirt`<br> `bush_up`<br> `bush_side`<br> `bush_plant` | `bb_main` | `models/blocks/template_flower_pot` |
| `geometry.template_glass_pane_side` | `north`<br> `east`<br> `south`<br> `west`<br> `edge` | `bb_main`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_glass_pane` |
| `geometry.template_height0` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height1` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height2` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height3` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height4` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height5` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_height6` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_height` |
| `geometry.template_item_frame` | `frame`<br> `wood` | `bb_main` | `models/blocks/template_item_frame` |
| `geometry.template_item_frame_map` | `frame`<br> `wood` | `bb_main` | `models/blocks/template_item_frame` |
| `geometry.template_lantern` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_lantern` |
| `geometry.template_hanging_lantern` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_lantern` |
| `geometry.template_orientable_trapdoor_down` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_orientable_trapdoor_open` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_orientable_trapdoor_up` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_orientable_trapdoor` |
| `geometry.template_pitcher_crop_down_small` | `side`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_pitcher_crop_bottom` |
| `geometry.template_pitcher_crop_down_large` | `plant`<br> `side`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_pitcher_crop_bottom` |
| `geometry.template_pressure_plate.powered` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_pressure_plate` |
| `geometry.template_pressure_plate` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_pressure_plate` |
| `geometry.template_rail_flat` | `up`<br> `down` | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_rail_raised_sw` | `up`<br> `down` | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_rail_raised_ne` | `up`<br> `down` | `bb_main` | `models/blocks/template_rail` |
| `geometry.template_sculk_shrieker` | `side`<br> `up`<br> `down`<br> `north`<br> `south`<br> `west`<br> `east` | `bb_main` | `models/blocks/template_sculk_shrieker` |
| `geometry.template_single_face` | `north` | `bb_main` | `models/blocks/template_single_face` |
| `geometry.template_slab.down` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_slab` |
| `geometry.template_slab.up` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_slab` |
| `geometry.template_sniffer_egg` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_sniffer_egg` |
| `geometry.template_stairs` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.inner_right` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.outer_right` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.inner_left` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_stairs.outer_left` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_stairs` |
| `geometry.template_torch` | `up`<br> `down`<br> `east`<br> `west`<br> `north`<br> `south` | `bb_main` | `models/blocks/template_torch` |
| `geometry.template_torch_wall` | `up`<br> `down`<br> `north`<br> `south`<br> `east`<br> `west` | `bb_main` | `models/blocks/template_torch` |
| `geometry.template_trapdoor_up` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_trapdoor_down` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_trapdoor_open` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_trapdoor` |
| `geometry.template_turtle_egg` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_four_turtle_eggs` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_three_turtle_eggs` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_two_turtle_eggs` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_turtle_egg` |
| `geometry.template_vertical_slab` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main` | `models/blocks/template_vertical_slab` |
| `geometry.template_wall_post` | `north`<br> `east`<br> `south`<br> `west`<br> `up`<br> `down` | `bb_main`<br> `post`<br> `north_tall`<br> `east_tall`<br> `south_tall`<br> `west_tall`<br> `north`<br> `east`<br> `south`<br> `west` | `models/blocks/template_wall` |

