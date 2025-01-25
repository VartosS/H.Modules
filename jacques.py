



        img = Image.open(io.BytesIO(pic_data)).convert("RGB")








        wrapped_text = "\n".join(wrap(txt, 19)) + "\n"
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(io.BytesIO(font_data), 32, encoding="UTF-8")








        text_size = draw.textbbox((0, 0), wrapped_text, font=font)
        imtext = Image.new("RGBA", (text_size[0] + 10, text_size[1] + 10), (0, 0, 0, 0))
        draw_imtext = ImageDraw.Draw(imtext)
        draw_imtext.multiline_text((10, 10), wrapped_text, (0, 0, 0), font=font, align=self.config["location"])








        imtext.thumbnail((350, 195))
        img.paste(imtext, (10, 10), imtext)








        out = io.BytesIO()
        out.name = "hikka_mods.jpg"
        img.save(out)
        out.seek(0)








        await message.client.send_file(message.to_id, out, reply_to=reply)
        await message.delete()
