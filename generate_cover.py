"""Generate a clean book cover for REBOOT."""
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1600, 2400
img = Image.new('RGB', (WIDTH, HEIGHT), '#1a1a2e')
draw = ImageDraw.Draw(img)

# Background gradient effect with rectangles
for i in range(HEIGHT):
    r = int(26 + (i / HEIGHT) * 20)
    g = int(26 + (i / HEIGHT) * 10)
    b = int(46 + (i / HEIGHT) * 30)
    draw.line([(0, i), (WIDTH, i)], fill=(r, g, b))

# Accent bar
draw.rectangle([(100, 500), (1500, 510)], fill='#e94560')
draw.rectangle([(100, 1300), (1500, 1310)], fill='#e94560')

# Try to use a good font, fallback to default
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 180)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45)
    tiny_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()
    tiny_font = ImageFont.load_default()

# Title
draw.text((WIDTH//2, 700), "REBOOT", fill='#ffffff', font=title_font, anchor='mm')

# Subtitle
draw.text((WIDTH//2, 850), "6 Semaines pour", fill='#e94560', font=subtitle_font, anchor='mm')
draw.text((WIDTH//2, 930), "Reprogrammer ta Vie", fill='#e94560', font=subtitle_font, anchor='mm')

# Description lines
draw.text((WIDTH//2, 1100), "Quitter les addictions", fill='#cccccc', font=small_font, anchor='mm')
draw.text((WIDTH//2, 1170), "Réactiver la discipline", fill='#cccccc', font=small_font, anchor='mm')
draw.text((WIDTH//2, 1240), "Devenir la meilleure version de toi-même", fill='#cccccc', font=small_font, anchor='mm')

# Progress bar visual
bar_y = 1500
bar_width = 1000
bar_x = (WIDTH - bar_width) // 2
draw.rectangle([(bar_x, bar_y), (bar_x + bar_width, bar_y + 30)], fill='#333355')
draw.rectangle([(bar_x, bar_y), (bar_x + bar_width, bar_y + 30)], fill='#e94560')

# Week markers
for i in range(7):
    x = bar_x + (bar_width * i) // 6
    if i == 0:
        label = "J1"
    elif i == 6:
        label = "S6"
    else:
        label = f"S{i}"
    draw.ellipse([(x-12, bar_y+3), (x+12, bar_y+27)], fill='#ffffff')
    draw.text((x, bar_y + 60), label, fill='#888888', font=tiny_font, anchor='mm')

# Pillars
pillars = ["Neurosciences", "Atomic Habits", "Miracle Morning", "Méditation", "Ultra Trail"]
for i, p in enumerate(pillars):
    y = 1650 + i * 65
    draw.text((WIDTH//2, y), f"— {p} —", fill='#666688', font=tiny_font, anchor='mm')

# Bottom
draw.text((WIDTH//2, 2150), "Un guide pragmatique basé sur la science", fill='#888888', font=tiny_font, anchor='mm')
draw.text((WIDTH//2, 2220), "Pour ingénieurs et esprits analytiques", fill='#666666', font=tiny_font, anchor='mm')

img.save(os.path.join(os.path.dirname(__file__), 'cover.png'), 'PNG')
print("Cover generated: cover.png")
