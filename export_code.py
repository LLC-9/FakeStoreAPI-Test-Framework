import os


def export_project(output_filename="project_all_code.txt"):
    # 需要提取的文件后缀
    valid_extensions = ('.py', '.yaml', '.ini', '.txt')
    # 需要过滤的黑名单文件夹
    ignore_dirs = ['.venv', '__pycache__', '.git', 'allure-results', 'allure-report']

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk("."):
            # 过滤黑名单目录
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for file in files:
                if file.endswith(valid_extensions) and file != "export_code.py":
                    file_path = os.path.join(root, file)
                    outfile.write(f"\n{'=' * 50}\n")
                    outfile.write(f"【文件路径】: {file_path}\n")
                    outfile.write(f"{'=' * 50}\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"读取失败: {e}\n")
    print(f"提取完成！所有代码已保存到当前目录下的 {output_filename}")


if __name__ == "__main__":
    export_project()