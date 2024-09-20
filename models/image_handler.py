from werkzeug.utils import secure_filename
import os

class ImageChecker:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def validate_file(request):
        # 检查是否有文件在请求中
        if 'file' not in request.files:
            return False, "No file part"

        file = request.files['file']

        # 检查文件名是否为空
        if file.filename == '':
            return False, "No selected file"

        # 检查文件类型
        if not ImageChecker.allowed_file(file.filename):
            return False, "File type is not allowed"

        return True, None
    


class ImageSaver:
    @staticmethod
    def save_file(file, upload_folder):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename