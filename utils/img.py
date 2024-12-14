from PIL import Image

def get_img_ext(file_path):
    """
    Determines the image file extension based on its MIME type.

    Args:
        file_path (str): The path to the image file.

    Returns:
        str: The file extension (e.g., 'jpg', 'png', 'gif').
    """
    try:
        with Image.open(file_path) as img:
            format = img.format
            if format == 'JPEG':
                return 'jpg'
            elif format == 'PNG':
                return 'png'
            elif format == 'GIF':
                return 'gif'
            else:
                return format.lower()
    except (IOError, SyntaxError):
        # Handle corrupted or unreadable images
        print(f"无法确定图片格式: {file_path}")
        return 'bin'  # 未知或二进制文件的默认扩展名

def convert_gif_to_jpg(gif_path, jpg_path):
    """
    将GIF图像转换为JPG图像。

    Args:
        gif_path (str): GIF图像的文件路径。
        jpg_path (str): 转换后JPG图像的保存路径。
    """
    try:
        with Image.open(gif_path) as img:
            # 转换图像模式为RGB，以去除透明背景
            img = img.convert('RGB')
            img.save(jpg_path, 'JPEG')
            print(f"GIF已转换为JPG: {jpg_path}")
    except Exception as e:
        print(f"转换GIF为JPG时出错: {e}")

# 主程序示例
if __name__ == "__main__":
    #python -m utils.img
    img_path = r"C:\Code\wxqunBot\tmp\369743613501245641.gif"
    ext = get_img_ext(img_path)
    print(f"图片扩展名: {ext}")

    if ext == 'gif':
        # 指定转换后的JPG文件路径
        jpg_path = img_path.replace('.gif', '.jpg')
        convert_gif_to_jpg(img_path, jpg_path)