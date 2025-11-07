import matplotlib.pyplot as plt
import ternary
import random


# ---- 辅助类：用于让 lambda 函数与 ternary 库的旧式 % 格式化兼容 ----
class CustomFormatter:
    """一个辅助类，使可调用对象与 ternary 库的旧式 % 格式化兼容。"""

    def __init__(self, func):
        self.func = func

    def __mod__(self, value):
        # 当 `formatter % value` 被调用时，这个方法会被执行
        return self.func(value)


# ---- 1) 参数：把 0~0.2 放大到 0~200（整数 scale 更稳）----
SCALE_FLOAT = 0.2
SCALE_INT = 200  # ternary 的整数 scale
MULT = SCALE_INT / SCALE_FLOAT  # = 1000，把小数映射成整数
N = 50


def generate_random_points_in_zoom(n, scale=0.2):
    pts = []
    for _ in range(n):
        a = random.uniform(0, scale)
        b = random.uniform(0, scale - a)
        c = scale - a - b
        p = [a, b, c]  # (Sc, Al_var, Hf)
        random.shuffle(p)
        pts.append(tuple(p))
    return pts


data_raw = generate_random_points_in_zoom(N, scale=SCALE_FLOAT)
print("原始点(按注释顺序 Sc, Al_var, Hf)示例:", data_raw[:5])

# ★ 重排为 (left, right, bottom) = (Al_var, Hf, Sc)，并映射到 0~200
plotting_data = [(al * MULT, hf * MULT, sc * MULT) for (sc, al, hf) in data_raw]

# ---- 2) 画布 ----
fig, tax = ternary.figure(scale=SCALE_INT)
fig.set_size_inches(10, 8)
tax.set_background_color("white")

# ---- 3) 边界/网格 ----
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=50, color="gray", linestyle="--")  # 0.05 → 50

# ---- 4) 散点 ----
tax.scatter(plotting_data, marker="o", c="red", s=40, zorder=3)

# ---- 5) 轴标签 ----
tax.left_axis_label("Al (%)", fontsize=14, offset=0.18)
tax.bottom_axis_label("Sc (%)", fontsize=14, offset=0.12)
# tax.right_axis_label("Hf (%)", fontsize=14, offset=0.18)

# ---- 6) 设轴范围 → 生成刻度缓存 → 自定义刻度标签 ----
# 先把每个轴的范围显式设为 0~200（与你的整数 scale 一致）
tax.set_axis_limits({"l": [0, SCALE_INT], "r": [0, SCALE_INT], "b": [0, SCALE_INT]})

# 依据轴范围生成刻度缓存（每 50 一个刻度：0, 50, 100, 150, 200）
tax.get_ticks_from_axis_limits(multiple=50)

# 【★ 修正版】
# 修正所有轴的刻度标签，使其正确显示
tax.set_custom_ticks(
    multiple=50,
    fontsize=10,
    linewidth=1,
    # axes="lb",
    tick_formats={
        # ★ 修正 b 轴：v 是 0, 50, ..., 200。需要 v/1000 变回 0, 0.05, ...
        "b": CustomFormatter(lambda v: f"{v / MULT:.2f}"),  # v/1000
        # ★ 修正 r 轴：同理
        "r": CustomFormatter(lambda v: f""),  # v/1000
        # ★ 修正 l 轴：使用 99.8 + v_float 的逻辑
        # v=0  (底部) -> 99.8 + 0     = 99.80
        # v=200 (顶部) -> 99.8 + 0.2  = 100.00
        "l": CustomFormatter(lambda v: f"{SCALE_FLOAT - (v / MULT):.2f}"),
    },
)

# ---- 7) 标题 & 清理 ----
tax.set_title("Zoomed-in Ternary Plot\n(Al-rich corner)", fontsize=16, pad=20)
tax.clear_matplotlib_ticks()
tax.get_axes().set_axis_off()

# ---- 8) 保存 ----
out = "zoomed_ternary_plot_final_fixed.png"
print(f"将绘图保存到 {out}...")
fig.savefig(out, dpi=300, bbox_inches="tight")
print("绘图完成。")
