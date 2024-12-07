import os
from PIL import Image
import shutil
import argparse

def rename_and_move_files(directory, base_name):
    # 変更後のファイルを保存するディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 指定されたディレクトリ内のファイルのリストを取得
    files = os.listdir(directory)
    
    # 画像ファイルのカウント
    count = 1

    for file_name in files:
        # ファイルの拡張子を取得
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # 画像ファイルかどうかをチェック
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            # 新しいファイル名を作成
            new_name = f"{base_name}_{count}{file_extension}"
            
            # 古いファイルのパスと新しいファイルのパスを作成
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)
            
            # ファイル名を変更し、ディレクトリ内で移動
            shutil.move(old_path, new_path)
            
            print(f"Renamed and moved: {old_path} -> {new_path}")
            
            # カウントをインクリメント
            count += 1

def compress_images_by_sizes(directory, base_name, sizes):
    # 指定されたディレクトリ内のファイルのリストを取得
    files = os.listdir(directory)

    for size in sizes:
        output_directory = os.path.join(directory, f"{base_name}_compressed_{size}")
        
        # 圧縮画像を保存するディレクトリが存在しない場合は作成
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        for file_name in files:
            # ファイルの拡張子を取得
            file_extension = os.path.splitext(file_name)[1].lower()

            # 画像ファイルかどうかをチェック
            if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                # 古いファイルのパスを作成
                file_path = os.path.join(directory, file_name)
                
                # 画像を開く
                with Image.open(file_path) as img:
                    # 圧縮後のファイル名を作成
                    new_file_path = os.path.join(output_directory, file_name)
                    
                    # 画像を圧縮して保存
                    img.save(new_file_path, optimize=True, quality=size)
                    
                    print(f"Compressed: {file_path} -> {new_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename, move and compress image files.")
    parser.add_argument("input_directory", type=str, help="Path to the input directory containing images.")
    parser.add_argument("base_name", type=str, help="Base name for renaming files.")
    parser.add_argument("sizes", type=int, nargs='+', help="List of compression sizes (quality percentages).")
    args = parser.parse_args()

    # 入力ディレクトリのパスを取得
    input_directory = args.input_directory
    base_name = args.base_name
    sizes = args.sizes

    # リネームと移動
    rename_and_move_files(input_directory, base_name)
    
    # 圧縮
    compress_images_by_sizes(input_directory, base_name, sizes)

# 実行コマンド例：
# python ./compress_images/compress_images.py ./input_directory compressFileName 50 25 10
