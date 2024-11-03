import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#from matplotlib.font_manager import FontManager
#fm = FontManager()
#mat_fonts = set(f.name for f in fm.ttflist)
#print(mat_fonts)
#exit(1)

def spider(df, *, id_column, title=None, max_values=None, padding=1.25):	
    plt.rcParams['font.sans-serif'] = ['SimSun']
    plt.rcParams['axes.unicode_minus'] = False	
    categories = df._get_numeric_data().columns.tolist()
    data = df[categories].to_dict(orient='list')
    ids = df[id_column].tolist()
    if max_values is None:
        max_values = {key: padding*max(value) for key, value in data.items()}
        
    normalized_data = {key: np.array(value) / max_values[key] for key, value in data.items()}
    num_vars = len(data.keys())
    tiks = list(data.keys())
    tiks += tiks[:1]
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for i, model_name in enumerate(ids):
        values = [normalized_data[key][i] for key in data.keys()]
        actual_values = [data[key][i] for key in data.keys()]
        values += values[:1]  # Close the plot for a better look
        ax.plot(angles, values, label=model_name)
        ax.fill(angles, values, alpha=0.15)
        for _x, _y, t in zip(angles, values, actual_values):
            t = f'{t:.2f}' if isinstance(t, float) else str(t)
            ax.text(_x, _y, t, size='xx-small')
            
    ax.fill(angles, np.ones(num_vars + 1), alpha=0.05)
    ax.set_yticklabels([])
    ax.set_xticks(angles)
    ax.set_xticklabels(tiks)
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    if title is not None: plt.suptitle(title)
    plt.show()
    
radar = spider

spider(
    pd.DataFrame({
        'x': ['deepseek', 'qwen'],
        '数学': [10,11],
        '物理': [0.1, 0.3],
        '化学': [26, 14],
        '历史': [9, 12],
        '语文': [2.4,1.3]
    }),
    id_column='x',
    title='学科考试',
    padding=1.1
)