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

{Models}
