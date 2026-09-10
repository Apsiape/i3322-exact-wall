"""Compose already-rendered pages for development visual QA; not proof checking."""
from pathlib import Path
from PIL import Image, ImageDraw
from pypdf import PdfReader
import argparse

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=Path, default=root/'tmp/revision-checks')
parser.add_argument('--pdf', type=Path, default=root/'output/pdf/resolution.pdf')
args = parser.parse_args()
folder = args.folder
count = len(PdfReader(args.pdf).pages)
assert 1 <= count <= 50
for start in range(1, count+1, 8):
    sheet = Image.new('RGB', (1400,1000), 'white')
    draw = ImageDraw.Draw(sheet)
    for j, number in enumerate(range(start,min(start+8,count+1))):
        with Image.open(folder/f'page-{number:02d}.png') as img:
            img.thumbnail((340,465))
            x,y = (j%4)*350,(j//4)*500
            sheet.paste(img,(x,y+25))
            draw.text((x+10,y+5),f'Page {number}',fill='black')
    dest = folder/f'contact-{(start-1)//8+1}.png'
    sheet.save(dest)
    print(dest)
