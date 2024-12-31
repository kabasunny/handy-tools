# add_relative_path_commen\add_relative_path_comment_py.py
import os


def add_relative_path_to_python_files(root_dir, target_dir):
    for dirpath, _, filenames in os.walk(target_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                # プロジェクトルートからの相対パスを計算
                relative_path = os.path.relpath(file_path, root_dir)

                # ファイル内容を読み込む
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.readlines()

                # コメントアウトされた相対パスを追加
                comment_line = f"# {relative_path}\n"

                # 最初の行が既にコメントアウトされている場合はスキップ
                if content and content[0].startswith("#"):
                    if content[0].strip() == comment_line.strip():
                        continue

                # コメントを最初の行に追加
                content.insert(0, comment_line)

                # ファイル内容を上書き
                with open(file_path, "w", encoding="utf-8") as file:
                    file.writelines(content)

                print(f"Updated: {relative_path}")


if __name__ == "__main__":
    # ルートディレクトリと対象ディレクトリを指定
    project_root = input("ルートディレクトリのパスを指定してください: ")
    target_directory = input("対象ディレクトリのパスを指定してください: ")

    project_root = os.path.abspath(project_root)
    target_directory = os.path.abspath(target_directory)

    add_relative_path_to_python_files(project_root, target_directory)
