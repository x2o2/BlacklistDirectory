import os


def 统计黑名单文件(directory='黑名单', endswith=".md"):
    """
    列出指定目录下所有的Markdown (.md) 文件。

    参数:
    directory (str): 需要搜索的目录路径。

    返回:
    list: 找到的Markdown文件路径列表。
    """
    md_files = []
    for filename in os.listdir(directory):
        if filename.endswith(endswith):
            md_files.append(filename)
    return md_files


def 黑名单数量(*file_paths, directory='黑名单', endswith=".md"):
    """
    计算多个文件中的单词数量，处理多种类型的空白字符。

    参数:
    *file_paths: 一个包含多个文件路径的元组。

    返回:
    dict: 键为文件路径，值为对应文件的单词数量。
    """
    word_counts = {}
    for file_path in file_paths[0]:
        filename = file_path[:-len(endswith)] if file_path.endswith(endswith) else file_path
        try:
            with open(os.path.join(directory, file_path), 'r', encoding='utf-8') as file:
                content = file.read()
                # 使用默认的split()来正确处理所有类型的空白字符
                words = content.split()
                word_counts[filename] = len(words)
        except FileNotFoundError:
            word_counts[filename] = "文件未找到，请检查路径是否正确。"
        except Exception as e:
            word_counts[filename] = f"读取文件时出错: {e}"
    return f"总计：{sum(word_counts.values())}",word_counts

def 输出黑名单txt(*file_paths, directory='黑名单', endswith=".md"):
    """
    计算多个文件中的单词数量，处理多种类型的空白字符。

    参数:
    *file_paths: 一个包含多个文件路径的元组。

    """
    words = []
    for file_path in file_paths[0]:
        try:
            with open(os.path.join(directory, file_path), 'r', encoding='utf-8') as file:
                content = file.read()
                # 使用默认的split()来正确处理所有类型的空白字符
                words += content.split()
        except Exception as e:
            print(f"读取文件时出错: {e}")

    with open("黑名单.txt", 'w', encoding='utf-8') as file:
        file.write(" ".join(words))

黑名单文件 = 统计黑名单文件()
print(黑名单数量(黑名单文件))
输出黑名单txt(黑名单文件)
