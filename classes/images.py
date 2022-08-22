from PIL import Image, ImageFont, ImageDraw


class Images:

    def __init__(self):
        self.body = Image.open('images/bg.png').convert("RGBA")
        self.high_physical_health = Image.open(
            'images/HP_high.png').convert("RGBA")
        self.middle_physical_health = Image.open(
            'images/HP_mid.png').convert("RGBA")
        self.low_physical_health = Image.open(
            'images/HP_low.png').convert("RGBA")
        self.high_mental_health = Image.open(
            'images/SP_high.png').convert("RGBA")
        self.middle_mental_health = Image.open(
            'images/SP_mid.png').convert("RGBA")
        self.low_mental_health = Image.open(
            'images/SP_low.png').convert("RGBA")
        self.font = ImageFont.truetype('norwester.otf', size=14)
        self.text = ImageDraw.Draw(self.body)

    def __check_health(self, division):
        if division > 0.75:
            return self.high_physical_health
        elif division >= 0.25:
            return self.middle_physical_health
        else:
            return self.low_physical_health

    def __check_mental_health(self, division):
        if division > 0.75:
            return self.high_mental_health
        elif division >= 0.25:
            return self.middle_mental_health
        else:
            return self.low_mental_health

    def health_condition_image(self, head_hp, body_hp, r_leg_hp, l_leg_hp, r_arm_hp, l_arm_hp, sp):

        for part_hp in [[head_hp[0], head_hp[1], (132, 11), (136, 13)],
                        [body_hp[0], body_hp[1], (203, 108), (207, 110)],
                        [l_arm_hp[0], l_arm_hp[1], (234, 197), (238, 199)],
                        [r_arm_hp[0], r_arm_hp[1], (36, 199), (40, 201)],
                        [l_leg_hp[0], l_leg_hp[1], (223, 266), (227, 268)],
                        [r_leg_hp[0], r_leg_hp[1], (48, 264), (52, 266)]]:

            self.body.paste(self.__check_health(part_hp[0] / part_hp[1]))

            self.text.text(part_hp[3], str(part_hp[0]), font=self.font, fill=(
                '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

        part_sp = [sp[0], sp[1], (42, 69), (46, 71)]

        self.body.paste(self.__check_mental_health(part_hp[0] / part_hp[1]))

        self.text.text(part_sp[3], str(part_sp[0]), font=self.font, fill=(
            '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

        self.body.save("images/temp/hp_temp.png")
        return
