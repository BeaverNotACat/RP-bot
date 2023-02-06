from PIL import Image, ImageFont, ImageDraw


class Images:

    def __init__(self):
        self.body = Image.open('assets/images/bg.png').convert("RGBA")
        self.high_physical_health = Image.open(
            'assets/images/HP_high.png').convert("RGBA")
        self.middle_physical_health = Image.open(
            'assets/images/HP_mid.png').convert("RGBA")
        self.low_physical_health = Image.open(
            'assets/images/HP_low.png').convert("RGBA")
        self.high_mental_health = Image.open(
            'assets/images/SP_high.png').convert("RGBA")
        self.middle_mental_health = Image.open(
            'assets/images/SP_mid.png').convert("RGBA")
        self.low_mental_health = Image.open(
            'assets/images/SP_low.png').convert("RGBA")
        self.font = ImageFont.truetype('assets/fonts/norwester.otf', size=14)
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

    def health_condition_image(self, head, body, right_leg, left_leg, right_arm, left_arm, sanity):

        for part_hp in [[head[0], head[1], (132, 11), (136, 13)],
                        [body[0], body[1], (203, 108), (207, 110)],
                        [left_arm[0], left_arm[1], (234, 197), (238, 199)],
                        [right_arm[0], right_arm[1], (36, 199), (40, 201)],
                        [left_leg[0], left_leg[1], (223, 266), (227, 268)],
                        [right_leg[0], right_leg[1], (48, 264), (52, 266)]]:

            self.body.paste(self.__check_health(part_hp[0] / part_hp[1]), part_hp[2], self.__check_health(part_hp[0] / part_hp[1]))
            self.text.text(part_hp[3], str(part_hp[0]), font=self.font, fill=(
                '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

        part_sp = [sanity[0], sanity[1], (42, 69), (46, 71)]

        self.body.paste(self.__check_mental_health(part_hp[0] / part_hp[1]), part_sp[2], self.__check_mental_health(part_hp[0] / part_hp[1]))

        self.text.text(part_sp[3], str(part_sp[0]), font=self.font, fill=(
            '#FFFFFF'), stroke_width=2, stroke_fill=('#000000'))

        self.body.save("assets/images/temp/hp_temp.png")
        return
