import os

"""
指定されたディレクトリ内のファイルを検索し、
除外ディレクトリを除いたツリー構造と指定された拡張子のファイルの内容を出力する。
出力内容は、最初にディレクトリとファイルのツリー構造、その後各指定拡張子ファイルの全容。
"""


def list_files(root_dir, extensions, excluded_dirs):
    result = []
    for root, dirs, files in os.walk(root_dir):
        # 除外ディレクトリを削除
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        result.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                result.append(f"{sub_indent}{file}")
    return result


def list_files_with_content(root_dir, extensions, excluded_dirs):
    result = []
    for root, dirs, files in os.walk(root_dir):
        # 除外ディレクトリを削除
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        result.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                result.append(f"{sub_indent}{file}")
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    result.extend(
                        f"{sub_indent}{line.strip()}" for line in f.readlines()
                    )
    return result


def save_to_file(output_path, tree_data, content_data):
    os.makedirs(
        os.path.dirname(output_path), exist_ok=True
    )  # ディレクトリが存在しない場合に作成
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Directory and File Tree:\n")
        for line in tree_data:
            f.write(f"{line}\n")
        f.write("\nFull File Content:\n")
        for line in content_data:
            f.write(f"{line}\n")


if __name__ == "__main__":
    project_dir = "."  # プロジェクトディレクトリからの相対パスを指定
    output_file = os.path.join(
        project_dir, "file_concat/full_code.txt"
    )  # 出力ファイルのパスを修正
    file_extensions = [".go"]  # .goファイルのみを取得
    excluded_dirs = [".git", "__pycache__"]  # 除外するディレクトリを指定

    # ファイルツリーのみを取得
    file_tree = list_files(project_dir, file_extensions, excluded_dirs)
    # ファイル内容も含めて取得
    file_tree_with_content = list_files_with_content(
        project_dir, file_extensions, excluded_dirs
    )
    # 一つのファイルに保存
    save_to_file(output_file, file_tree, file_tree_with_content)
    print(f"Output saved to {output_file}")
