from PIL import Image, ImageFont, ImageDraw


def health_condition_image(head_hp: dict, body_hp: dict, r_leg_hp: dict, l_leg_hp: dict, r_arm_hp: dict, l_arm_hp: dict, sp: dict):
    print('Making health condition image')

    body = Image.open('images/bg.png').convert("RGBA")
    stat1 = Image.open('images/HP_high.png').convert("RGBA")
    stat2 = Image.open('images/HP_mid.png').convert("RGBA")
    stat3 = Image.open('images/HP_low.png').convert("RGBA")
    stat4 = Image.open('images/SP_high.png').convert("RGBA")
    stat5 = Image.open('images/SP_mid.png').convert("RGBA")
    stat6 = Image.open('images/SP_low.png').convert("RGBA")

    font = ImageFont.truetype('norwester.otf', size=14)
    text = ImageDraw.Draw(body)

    for part_hp in [[head_hp[0], head_hp[1], (132, 11), (136, 13)],
                    [body_hp[0], body_hp[1], (203, 108), (207, 110)],
                    [l_arm_hp[0], l_arm_hp[1], (234, 197), (238, 199)],
                    [r_arm_hp[0], r_arm_hp[1], (36, 199), (40, 201)],
                    [l_leg_hp[0], l_leg_hp[1], (223, 266), (227, 268)],
                    [r_leg_hp[0], r_leg_hp[1], (48, 264), (52, 266)]]:

        division = (part_hp[0] / part_hp[1])

        if division > 0.75:
            body.paste(stat1, part_hp[2], stat1)
        elif division >= 0.25:
            body.paste(stat2, part_hp[2], stat2)
        else:
            body.paste(stat3, part_hp[2], stat3)

        text.text(part_hp[3], str(part_hp[0]), font=font, fill=(
            '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

    part_sp = [sp[0], sp[1], (42, 69), (46, 71)]

    division = (part_sp[0] / part_sp[1])

    if division > 0.75:
        body.paste(stat4, part_sp[2], stat4)
    elif division >= 0.25:
        body.paste(stat5, part_sp[2], stat5)
    else:
        body.paste(stat6, part_sp[2], stat6)

    text.text(part_sp[3], str(part_sp[0]), font=font, fill=(
        '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

    body.save("temp/hp_temp.png")
    return
