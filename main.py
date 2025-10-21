import tkinter as tk
from tkinter import ttk, messagebox

# ===== 数据部分（保持不变）=====
data_training_day = {
    '160cm': {'60kg': '2.7/1.7', '65kg': '2.6/1.6', '70kg': '2.5/1.5', '75kg': '2.4/1.4', '80kg': '2.3/1.3', '85kg': '2.2/1.3', '90kg': '2.2/1.2', '95kg': '2.1/1.2', '100kg': '2.0/1.1', '105kg': '2.0/1.1', '110kg': '1.9/1.1', '115kg': '1.9/1.0', '120kg': None,      '125kg': None,      '130kg': None,      '135kg': None,      '140kg': None},
    '165cm': {'60kg': '2.9/1.7', '65kg': '2.7/1.6', '70kg': '2.6/1.5', '75kg': '2.5/1.4', '80kg': '2.4/1.4', '85kg': '2.3/1.3', '90kg': '2.2/1.3', '95kg': '2.2/1.2', '100kg': '2.1/1.2', '105kg': '2.1/1.1', '110kg': '2.0/1.1', '115kg': '2.0/1.1', '120kg': '1.9/1.0', '125kg': None,      '130kg': None,      '135kg': None,      '140kg': None},
    '170cm': {'60kg': None,      '65kg': '2.8/1.7', '70kg': '2.7/1.6', '75kg': '2.6/1.5', '80kg': '2.5/1.4', '85kg': '2.4/1.4', '90kg': '2.3/1.3', '95kg': '2.3/1.2', '100kg': '2.2/1.2', '105kg': '2.2/1.2', '110kg': '2.1/1.1', '115kg': '2.1/1.1', '120kg': '2.0/1.1', '125kg': '2.0/1.0', '130kg': None,      '135kg': None,      '140kg': None},
    '175cm': {'60kg': None,      '65kg': None,      '70kg': '2.8/1.6', '75kg': '2.7/1.5', '80kg': '2.6/1.5', '85kg': '2.5/1.4', '90kg': '2.4/1.3', '95kg': '2.4/1.3', '100kg': '2.3/1.2', '105kg': '2.2/1.2', '110kg': '2.2/1.2', '115kg': '2.1/1.1', '120kg': '2.1/1.1', '125kg': '2.0/1.1', '130kg': '2.0/1.0', '135kg': None,      '140kg': None},
    '180cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': '2.8/1.6', '80kg': '2.7/1.5', '85kg': '2.6/1.4', '90kg': '2.5/1.4', '95kg': '2.5/1.3', '100kg': '2.4/1.3', '105kg': '2.3/1.2', '110kg': '2.3/1.2', '115kg': '2.2/1.1', '120kg': '2.2/1.1', '125kg': '2.1/1.1', '130kg': '2.1/1.1', '135kg': '2.0/1.0', '140kg': None},
    '185cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': None,      '80kg': '2.8/1.5', '85kg': '2.7/1.5', '90kg': '2.6/1.4', '95kg': '2.5/1.4', '100kg': '2.5/1.3', '105kg': '2.4/1.3', '110kg': '2.3/1.2', '115kg': '2.3/1.2', '120kg': '2.2/1.1', '125kg': '2.2/1.1', '130kg': '2.1/1.1', '135kg': '2.1/1.0', '140kg': '2.1/1.0'},
    '190cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': None,      '80kg': None,      '85kg': '2.8/1.5', '90kg': '2.7/1.4', '95kg': '2.6/1.4', '100kg': '2.6/1.3', '105kg': '2.5/1.3', '110kg': '2.4/1.2', '115kg': '2.4/1.2', '120kg': '2.3/1.2', '125kg': '2.2/1.1', '130kg': '2.2/1.1', '135kg': '2.2/1.1', '140kg': '2.1/1.0'}
}

data_rest_day = {
    '160cm': {'60kg': '2.2/1.7', '65kg': '2.1/1.6', '70kg': '2.0/1.5', '75kg': '1.9/1.4', '80kg': '1.8/1.3', '85kg': '1.8/1.3', '90kg': '1.7/1.2', '95kg': '1.7/1.2', '100kg': '1.6/1.1', '105kg': '1.6/1.1', '110kg': '1.6/1.1', '115kg': '1.5/1.0', '120kg': None,      '125kg': None,      '130kg': None,      '135kg': None,      '140kg': None},
    '165cm': {'60kg': '2.3/1.7', '65kg': '2.2/1.6', '70kg': '2.1/1.5', '75kg': '2.0/1.4', '80kg': '1.9/1.4', '85kg': '1.9/1.3', '90kg': '1.8/1.3', '95kg': '1.7/1.2', '100kg': '1.7/1.2', '105kg': '1.7/1.1', '110kg': '1.6/1.1', '115kg': '1.6/1.1', '120kg': '1.6/1.0', '125kg': None,      '130kg': None,      '135kg': None,      '140kg': None},
    '170cm': {'60kg': None,      '65kg': '2.3/1.7', '70kg': '2.2/1.6', '75kg': '2.1/1.5', '80kg': '2.0/1.4', '85kg': '1.9/1.4', '90kg': '1.9/1.3', '95kg': '1.8/1.2', '100kg': '1.8/1.2', '105kg': '1.7/1.2', '110kg': '1.7/1.1', '115kg': '1.6/1.1', '120kg': '1.6/1.1', '125kg': '1.6/1.0', '130kg': None,      '135kg': None,      '140kg': None},
    '175cm': {'60kg': None,      '65kg': None,      '70kg': '2.3/1.6', '75kg': '2.2/1.5', '80kg': '2.1/1.5', '85kg': '2.0/1.4', '90kg': '1.9/1.3', '95kg': '1.8/1.2', '100kg': '1.8/1.2', '105kg': '1.8/1.2', '110kg': '1.7/1.2', '115kg': '1.7/1.1', '120kg': '1.7/1.1', '125kg': '1.6/1.1', '130kg': '1.6/1.0', '135kg': None,      '140kg': None},
    '180cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': '2.3/1.6', '80kg': '2.2/1.5', '85kg': '2.1/1.4', '90kg': '2.0/1.4', '95kg': '2.0/1.3', '100kg': '1.9/1.3', '105kg': '1.9/1.2', '110kg': '1.8/1.2', '115kg': '1.8/1.1', '120kg': '1.7/1.1', '125kg': '1.7/1.1', '130kg': '1.7/1.1', '135kg': '1.6/1.0', '140kg': None},
    '185cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': None,      '80kg': '2.3/1.5', '85kg': '2.2/1.5', '90kg': '2.1/1.4', '95kg': '2.0/1.4', '100kg': '2.0/1.3', '105kg': '1.9/1.3', '110kg': '1.9/1.2', '115kg': '1.8/1.2', '120kg': '1.8/1.1', '125kg': '1.7/1.1', '130kg': '1.7/1.1', '135kg': '1.7/1.0', '140kg': '1.6/1.0'},
    '190cm': {'60kg': None,      '65kg': None,      '70kg': None,      '75kg': None,      '80kg': None,      '85kg': '2.3/1.5', '90kg': '2.2/1.4', '95kg': '2.1/1.4', '100kg': '2.0/1.3', '105kg': '2.0/1.3', '110kg': '1.9/1.2', '115kg': '1.9/1.2', '120kg': '1.8/1.2', '125kg': '1.8/1.1', '130kg': '1.8/1.1', '135kg': '1.7/1.1', '140kg': '1.7/1.0'}
}

BG_COLOR = '#f5f5f5'

def find_closest_value(target, available_values):
    try:
        target_num = float(target.replace('cm', '').replace('kg', ''))
        available_nums = [float(x.replace('cm', '').replace('kg', '')) for x in available_values]
        closest = min(available_nums, key=lambda x: abs(x - target_num))
        for val in available_values:
            if float(val.replace('cm', '').replace('kg', '')) == closest:
                return val
    except:
        return None
    return None

def get_nutrition_values(height: float, weight: float, is_training_day: bool = True):
    height_key = f"{int(height)}cm"
    weight_key = f"{int(weight)}kg"
    data = data_training_day if is_training_day else data_rest_day

    used_height = height_key
    used_weight = weight_key

    if height_key not in data:
        available_heights = list(data.keys())
        used_height = find_closest_value(height_key, available_heights)
        if used_height is None:
            return None, None, None, None, "未找到匹配的身高"

    if weight_key not in data[used_height]:
        available_weights = list(data[used_height].keys())
        used_weight = find_closest_value(weight_key, available_weights)
        if used_weight is None:
            return None, None, None, None, "未找到匹配的体重"

    value = data[used_height][used_weight]
    if value is None:
        return None, None, None, None, "该身高体重组合无数据"

    carb, protein = value.split('/')
    return float(carb), float(protein), used_height, used_weight, ""

def calculate(event=None):
    try:
        height = float(entry_height.get().strip())
        weight = float(entry_weight.get().strip())
        is_training = var_day.get() == 1

        if height < 140 or height > 200 or weight < 40 or weight > 150:
            messagebox.showwarning("输入范围提示", "请输入合理范围：\n身高 140–200 cm\n体重 40–150 kg")
            return

        carb, protein, used_h, used_w, error = get_nutrition_values(height, weight, is_training)

        if error:
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, error, "error")
            result_text.config(state='disabled')
            return

        total_carb = carb * weight # type: ignore
        total_protein = protein * weight # type: ignore
        day_str = "力训日" if is_training else "休息日/无锻炼"

        # 构建结果
        lines = [f"📅 {day_str} 营养建议：", ""]
        lines.append(f"  碳水摄入：{carb} g/kg × {weight} kg = {total_carb:.2f} g/天")
        lines.append(f"蛋白质摄入：{protein} g/kg × {weight} kg = {total_protein:.2f} g/天")
        lines.append(f"  脂肪摄入：0.8 g/kg × {weight} kg = {0.8 * weight:.2f} g/天")
        lines.append("")
        lines.append("💡 建议：")
        lines.append("•   脂肪: 0.8g/kg，大体重可适当降低，小体重可适当增加")
        lines.append("• 力训日: 练前补充碳水，练后安排大碳水餐")
        lines.append("")

        original_h = f"{int(height)}cm"
        original_w = f"{int(weight)}kg"
        if original_h != used_h or original_w != used_w:
            lines.append("🔍 使用了最接近的数据：")
            lines.append(f"   身高：{original_h} → {used_h}")
            lines.append(f"   体重：{original_w} → {used_w}")
        full_text = "\n".join(lines)

        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, full_text)
        result_text.config(state='disabled')

    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字！")

# ===== GUI 界面（标签+输入框整体居中，内部对齐）=====
root = tk.Tk()
root.title("个性化营养建议工具")
root.geometry("500x480")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use('clam')

main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
main_frame.pack(expand=True)  # 让内容整体垂直居中（可选）

# 标题
tk.Label(main_frame, text="个性化营养建议", font=("Arial", 16, "bold"), bg=BG_COLOR, fg="#333").pack(pady=(0, 20))

# 身高行（整体居中）
height_frame = tk.Frame(main_frame, bg=BG_COLOR)
height_frame.pack(pady=(0, 10))
tk.Label(height_frame, text="身高 (cm)：", bg=BG_COLOR, width=12, anchor="e").pack(side="left")
entry_height = ttk.Entry(height_frame, width=15, justify="center")
entry_height.pack(side="left", padx=(5, 0))

# 体重行（整体居中）
weight_frame = tk.Frame(main_frame, bg=BG_COLOR)
weight_frame.pack(pady=(0, 15))
tk.Label(weight_frame, text="体重 (kg)：", bg=BG_COLOR, width=12, anchor="e").pack(side="left")
entry_weight = ttk.Entry(weight_frame, width=15, justify="center")
entry_weight.pack(side="left", padx=(5, 0))

# 训练日选择（也居中）
var_day = tk.IntVar(value=1)
frame_radio = tk.Frame(main_frame, bg=BG_COLOR)
frame_radio.pack(pady=(0, 15))
ttk.Radiobutton(frame_radio, text="力训日", variable=var_day, value=1).pack(side="left", padx=15)
ttk.Radiobutton(frame_radio, text="休息日/无锻炼", variable=var_day, value=2).pack(side="left", padx=15)

# 计算按钮（居中）
btn = ttk.Button(main_frame, text="计算营养建议", command=calculate)
btn.pack(pady=(0, 15))

# 绑定回车键
root.bind('<Return>', calculate)

# 结果显示区域
result_frame = tk.Frame(main_frame, bg=BG_COLOR)
result_frame.pack(fill="both", expand=True, pady=(0, 10))
result_text = tk.Text(
    result_frame,
    wrap="word",
    height=13,
    bg="#ffffff",
    relief="solid",
    borderwidth=1
)
result_text.tag_configure("error", foreground="red")
result_text.config(state='disabled')
result_text.pack(fill="both", expand=True)

# 底部说明（居中）
tk.Label(main_frame, text="支持身高 160–190 cm，体重 60–140 kg\n无精确匹配时将自动使用最接近的有效数据",
         fg="gray", bg=BG_COLOR, justify="center").pack(pady=(10, 0))

# 配置列权重（可选，让右侧有空间）
main_frame.grid_columnconfigure(1, weight=1)

root.mainloop()
