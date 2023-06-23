from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


class BASE_TABLE:
    @staticmethod
    def bold(x, y):
        return [('FONTSIZE', x, y, 12)]

    @staticmethod
    def bold_gray(x, y):
        return [('BACKGROUND', x, y, colors.gray), ('FONTSIZE', x, y, 12)]

    @staticmethod
    def normal(x, y):
        return [('FONTSIZE', x, y, 12)]
