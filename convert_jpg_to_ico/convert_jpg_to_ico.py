
# pip install pillow
from PIL import Image

def convert_jpg_to_ico(jpg_path, ico_path, icon_size=(32, 32)):
    # 画像を開く
    img = Image.open(jpg_path)
    
    # ICO用にリサイズ
    img = img.resize(icon_size, Image.LANCZOS)
    
    # ICO形式で保存
    img.save(ico_path, format='ICO')

# 使用例
jpg_path = 'path/～.jpg'
ico_path = 'path/～.ico'
convert_jpg_to_ico(jpg_path, ico_path)
