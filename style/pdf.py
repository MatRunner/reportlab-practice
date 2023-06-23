from .base import BASE_TABLE
from reportlab.lib.colors import gray


class PERFORMANCE:
    @staticmethod
    def get():
        performance_table = [('GRID', (0, 0), (-1, -1), 1, gray),
                             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]
        performance_table.extend(BASE_TABLE.bold_gray((0, 0), (-1, 0)))
        performance_table.extend(BASE_TABLE.bold((0, 1), (-1, 1)))
        performance_table.extend(BASE_TABLE.normal((0, 2), (-1, -1)))
        return performance_table
