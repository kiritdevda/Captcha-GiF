from PIL   import ImageFont,Image, ImageDraw
from random import randrange

## create captcha frame will create a single frame for our captcha gif
    

def create_captcha_frame(width, height, ball_x, ball_y, ball_size, text):
    
    img = Image.new('RGBA',(width,height),(255,255,255,0))
    draw = ImageDraw.Draw(img)

    draw.ellipse((ball_x - ball_size, ball_y - ball_size, ball_x + ball_size, ball_y + ball_size), fill='red')
    
    for i in range(1,15):
        draw.line([(randrange(width),0), (0,randrange(height)),(randrange(width),height),(width,randrange(height))], fill='black', width=(randrange(1,3)))

    font = ImageFont.truetype("arial.ttf",width/2)
    txt_image_size = font.getsize(text)[0]
    
    img_text = Image.new('RGBA',(txt_image_size*2,txt_image_size*2),(255,255,255,0))
    draw_text = ImageDraw.Draw(img_text, 'RGBA')


    draw_text.text((0,0), text , fill=(0,0,0,255),font=font)

    img_text = img_text.rotate((ball_size % 4) * 90)
    
    
    img.paste(img_text,(ball_x - ball_size, ball_y - ball_size),img_text)
    return img


# Create the frames
frames = []
x, y = 0, 0
image_width, image_height = 100, 100
ball_x = image_width/2
ball_y = image_height/2

# generate Random_number
verification_number = randrange(1000, 9999)

for digit in str(verification_number):
    for size in range(0,image_width/2, 3 ):
        new_frame = create_captcha_frame(image_width, image_height, ball_x, ball_y, size, digit)
        frames.append(new_frame)
    

# Save into a GIF file that loops forever
frames[0].save('moving_ball.gif', format='GIF', transparency=0,append_images=frames[1:], save_all=True, duration=100, disposal=2, loop=0)